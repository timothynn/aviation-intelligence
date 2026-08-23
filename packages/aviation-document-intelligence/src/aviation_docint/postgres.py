from __future__ import annotations

import json
from datetime import date
from typing import Any, Iterable

from .models import Chunk, Document


SCHEMA = """
CREATE EXTENSION IF NOT EXISTS pgcrypto;
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
    effective_from DATE,
    effective_to DATE,
    publisher TEXT,
    checksum_sha256 TEXT,
    metadata JSONB NOT NULL DEFAULT '{}'::jsonb,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE TABLE IF NOT EXISTS chunks (
    chunk_id TEXT PRIMARY KEY,
    document_id TEXT NOT NULL REFERENCES documents(document_id) ON DELETE CASCADE,
    text TEXT NOT NULL,
    page_start INTEGER,
    page_end INTEGER,
    section TEXT,
    paragraph TEXT,
    heading_path JSONB NOT NULL DEFAULT '[]'::jsonb,
    metadata JSONB NOT NULL DEFAULT '{}'::jsonb,
    search_vector TSVECTOR GENERATED ALWAYS AS (
        setweight(to_tsvector('simple', coalesce(section, '')), 'A') ||
        setweight(to_tsvector('simple', coalesce(paragraph, '')), 'A') ||
        setweight(to_tsvector('simple', coalesce(text, '')), 'B')
    ) STORED
);
CREATE INDEX IF NOT EXISTS idx_documents_authority ON documents(authority);
CREATE INDEX IF NOT EXISTS idx_documents_jurisdiction ON documents(jurisdiction);
CREATE INDEX IF NOT EXISTS idx_documents_status ON documents(status);
CREATE INDEX IF NOT EXISTS idx_documents_effective ON documents(effective_from, effective_to);
CREATE INDEX IF NOT EXISTS idx_chunks_document ON chunks(document_id);
CREATE INDEX IF NOT EXISTS idx_chunks_search_vector ON chunks USING GIN(search_vector);
"""


class PostgresStore:
    """Production persistence adapter.

    psycopg is imported lazily so the local SQLite reference engine remains
    dependency-light. This adapter preserves the same document/chunk contract.
    """

    def __init__(self, dsn: str):
        try:
            import psycopg
        except ImportError as exc:  # pragma: no cover
            raise RuntimeError("Install the postgres extra: pip install psycopg[binary]") from exc
        self._psycopg = psycopg
        self.conn = psycopg.connect(dsn)
        self.conn.execute(SCHEMA)
        self.conn.commit()

    def close(self) -> None:
        self.conn.close()

    def upsert_document(self, doc: Document) -> None:
        self.conn.execute(
            """
            INSERT INTO documents (
                document_id,title,authority,jurisdiction,status,version,document_type,
                source_url,source_path,effective_from,effective_to,publisher,checksum_sha256,metadata
            ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            ON CONFLICT(document_id) DO UPDATE SET
                title=EXCLUDED.title, authority=EXCLUDED.authority,
                jurisdiction=EXCLUDED.jurisdiction, status=EXCLUDED.status,
                version=EXCLUDED.version, document_type=EXCLUDED.document_type,
                source_url=EXCLUDED.source_url, source_path=EXCLUDED.source_path,
                effective_from=EXCLUDED.effective_from, effective_to=EXCLUDED.effective_to,
                publisher=EXCLUDED.publisher, checksum_sha256=EXCLUDED.checksum_sha256,
                metadata=EXCLUDED.metadata, updated_at=now()
            """,
            (
                doc.document_id, doc.title, doc.authority, doc.jurisdiction, doc.status,
                doc.version, doc.document_type, doc.source_url, doc.source_path,
                doc.effective_from, doc.effective_to, doc.publisher, doc.checksum_sha256,
                json.dumps(doc.metadata, ensure_ascii=False),
            ),
        )
        self.conn.commit()

    def replace_chunks(self, document_id: str, chunks: Iterable[Chunk]) -> int:
        self.conn.execute("DELETE FROM chunks WHERE document_id=%s", (document_id,))
        count = 0
        for chunk in chunks:
            self.conn.execute(
                """
                INSERT INTO chunks (
                    chunk_id,document_id,text,page_start,page_end,section,paragraph,heading_path,metadata
                ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """,
                (
                    chunk.chunk_id, chunk.document_id, chunk.text, chunk.page_start, chunk.page_end,
                    chunk.section, chunk.paragraph, json.dumps(chunk.heading_path), json.dumps(chunk.metadata),
                ),
            )
            count += 1
        self.conn.commit()
        return count

    def search(self, query: str, limit: int = 50, authority: str | None = None,
               jurisdiction: str | None = None, current_only: bool = False) -> list[dict[str, Any]]:
        clauses = ["c.search_vector @@ websearch_to_tsquery('simple', %s)"]
        params: list[Any] = [query]
        if authority:
            clauses.append("d.authority = %s")
            params.append(authority)
        if jurisdiction:
            clauses.append("d.jurisdiction = %s")
            params.append(jurisdiction)
        if current_only:
            clauses.append("d.status = 'CURRENT'")
        params.append(limit)
        rows = self.conn.execute(
            f"""
            SELECT c.chunk_id,c.document_id,c.text,c.page_start,c.page_end,c.section,c.paragraph,
                   d.title,d.authority,d.jurisdiction,d.status,d.version,d.source_url,
                   ts_rank_cd(c.search_vector, websearch_to_tsquery('simple', %s)) AS score
            FROM chunks c
            JOIN documents d ON d.document_id=c.document_id
            WHERE {' AND '.join(clauses)}
            ORDER BY score DESC
            LIMIT %s
            """,
            [query, *params],
        ).fetchall()
        columns = ["chunk_id","document_id","text","page_start","page_end","section","paragraph",
                   "title","authority","jurisdiction","status","version","source_url","score"]
        return [dict(zip(columns, row)) for row in rows]
