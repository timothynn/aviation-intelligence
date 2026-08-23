from __future__ import annotations

import json
import re
import sqlite3
from pathlib import Path
from typing import Any, Iterable

from .models import Chunk, Document, SearchHit

SCHEMA = """
PRAGMA journal_mode=WAL;
CREATE TABLE IF NOT EXISTS documents (
    document_id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    authority TEXT,
    jurisdiction TEXT,
    status TEXT NOT NULL,
    version TEXT,
    document_type TEXT,
    source_url TEXT,
    source_path TEXT,
    effective_from TEXT,
    effective_to TEXT,
    publisher TEXT,
    checksum_sha256 TEXT,
    metadata_json TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS chunks (
    chunk_id TEXT PRIMARY KEY,
    document_id TEXT NOT NULL REFERENCES documents(document_id),
    text TEXT NOT NULL,
    page_start INTEGER,
    page_end INTEGER,
    section TEXT,
    paragraph TEXT,
    heading_path_json TEXT NOT NULL,
    metadata_json TEXT NOT NULL
);
CREATE VIRTUAL TABLE IF NOT EXISTS chunks_fts USING fts5(
    chunk_id UNINDEXED,
    document_id UNINDEXED,
    text,
    section,
    paragraph,
    tokenize='unicode61'
);
CREATE INDEX IF NOT EXISTS idx_documents_authority ON documents(authority);
CREATE INDEX IF NOT EXISTS idx_documents_jurisdiction ON documents(jurisdiction);
CREATE INDEX IF NOT EXISTS idx_documents_status ON documents(status);
CREATE INDEX IF NOT EXISTS idx_chunks_document ON chunks(document_id);
"""


def safe_fts_query(query: str) -> str:
    tokens = re.findall(r"[A-Za-z0-9][A-Za-z0-9_.:/-]*", query)
    if not tokens:
        return '""'
    # Quote tokens so identifiers such as A17, Part-TCO, Annex 6 and TCO.GEN.100
    # are treated as literals rather than FTS5 operators.
    return " AND ".join(f'"{token.replace(chr(34), "")}"' for token in tokens[:32])


class Store:
    def __init__(self, path: str | Path):
        self.path = str(path)
        Path(self.path).parent.mkdir(parents=True, exist_ok=True)
        self.db = sqlite3.connect(self.path, check_same_thread=False)
        self.db.row_factory = sqlite3.Row
        self.db.executescript(SCHEMA)

    def close(self) -> None:
        self.db.close()

    def upsert_document(self, doc: Document) -> None:
        self.db.execute(
            """INSERT INTO documents VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(document_id) DO UPDATE SET title=excluded.title, authority=excluded.authority,
            jurisdiction=excluded.jurisdiction, status=excluded.status, version=excluded.version,
            document_type=excluded.document_type, source_url=excluded.source_url, source_path=excluded.source_path,
            publisher=excluded.publisher, checksum_sha256=excluded.checksum_sha256, metadata_json=excluded.metadata_json""",
            (doc.document_id, doc.title, doc.authority, doc.jurisdiction, doc.status, doc.version,
             doc.document_type, doc.source_url, doc.source_path,
             doc.effective_from.isoformat() if doc.effective_from else None,
             doc.effective_to.isoformat() if doc.effective_to else None,
             doc.publisher, doc.checksum_sha256, json.dumps(doc.metadata, ensure_ascii=False)),
        )
        self.db.commit()

    def replace_chunks(self, document_id: str, chunks: Iterable[Chunk]) -> int:
        self.db.execute("DELETE FROM chunks_fts WHERE document_id = ?", (document_id,))
        self.db.execute("DELETE FROM chunks WHERE document_id = ?", (document_id,))
        count = 0
        for chunk in chunks:
            self.db.execute(
                "INSERT INTO chunks VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (chunk.chunk_id, chunk.document_id, chunk.text, chunk.page_start, chunk.page_end,
                 chunk.section, chunk.paragraph, json.dumps(chunk.heading_path), json.dumps(chunk.metadata)),
            )
            self.db.execute(
                "INSERT INTO chunks_fts(chunk_id, document_id, text, section, paragraph) VALUES (?, ?, ?, ?, ?)",
                (chunk.chunk_id, chunk.document_id, chunk.text, chunk.section or "", chunk.paragraph or ""),
            )
            count += 1
        self.db.commit()
        return count

    def lexical_search(self, query: str, limit: int = 50, filters: dict[str, Any] | None = None) -> list[SearchHit]:
        filters = filters or {}
        where = []
        params: list[Any] = [safe_fts_query(query)]
        for key in ("authority", "jurisdiction", "status", "document_type"):
            if filters.get(key):
                where.append(f"d.{key} = ?")
                params.append(filters[key])
        if filters.get("current_only"):
            where.append("d.status = 'CURRENT'")
        clause = (" AND " + " AND ".join(where)) if where else ""
        sql = f"""
        SELECT c.*, d.title, d.authority, d.jurisdiction, d.status, d.version, d.document_type, d.source_url,
               bm25(chunks_fts) AS rank
        FROM chunks_fts
        JOIN chunks c ON c.chunk_id = chunks_fts.chunk_id
        JOIN documents d ON d.document_id = c.document_id
        WHERE chunks_fts MATCH ? {clause}
        ORDER BY rank
        LIMIT ?
        """
        params.append(limit)
        rows = self.db.execute(sql, params).fetchall()
        hits: list[SearchHit] = []
        for row in rows:
            score = 1.0 / (1.0 + max(0.0, float(row["rank"])))
            hits.append(SearchHit(row["chunk_id"], row["document_id"], row["title"], row["text"], score,
                                   lexical_score=score,
                                   metadata={"authority": row["authority"], "jurisdiction": row["jurisdiction"],
                                             "status": row["status"], "version": row["version"],
                                             "document_type": row["document_type"], "source_url": row["source_url"],
                                             "section": row["section"], "paragraph": row["paragraph"],
                                             "page_start": row["page_start"], "page_end": row["page_end"]}))
        return hits

    def get_chunks(self, chunk_ids: list[str]) -> list[dict[str, Any]]:
        if not chunk_ids:
            return []
        placeholders = ",".join("?" for _ in chunk_ids)
        rows = self.db.execute(
            f"SELECT c.*, d.title, d.authority, d.jurisdiction, d.status, d.version, d.source_url FROM chunks c JOIN documents d ON d.document_id=c.document_id WHERE c.chunk_id IN ({placeholders})",
            chunk_ids,
        ).fetchall()
        return [dict(r) for r in rows]

    def stats(self) -> dict[str, int]:
        doc_count = self.db.execute("SELECT COUNT(*) FROM documents").fetchone()[0]
        chunk_count = self.db.execute("SELECT COUNT(*) FROM chunks").fetchone()[0]
        return {"documents": doc_count, "chunks": chunk_count}
