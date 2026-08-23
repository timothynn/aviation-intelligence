from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Iterable

from .chunker import chunk_document
from .models import Document
from .parsers import build_document
from .store import Store

SUPPORTED = {".pdf", ".xml", ".html", ".htm", ".txt", ".md"}


def load_download_manifest(corpus_root: Path) -> dict[str, dict[str, Any]]:
    manifest = corpus_root / "manifest.jsonl"
    rows: dict[str, dict[str, Any]] = {}
    if not manifest.exists():
        return rows
    for line in manifest.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        rows[row.get("path", "")] = row
    return rows


def iter_documents(root: Path) -> Iterable[Path]:
    for path in root.rglob("*"):
        if path.is_file() and path.suffix.lower() in SUPPORTED and path.name != "manifest.jsonl":
            yield path


def ingest_path(root: Path, store: Store) -> dict[str, int]:
    metadata = load_download_manifest(root)
    docs = chunks = 0
    for path in iter_documents(root):
        key = str(path).replace("\\", "/")
        info = metadata.get(key, {})
        relative = str(path.relative_to(root)).replace("\\", "/")
        document_id = info.get("sourceId") or f"local:{relative}"
        doc: Document = build_document(path, document_id, info)
        store.upsert_document(doc)
        created = chunk_document(doc)
        chunks += store.replace_chunks(doc.document_id, created)
        docs += 1
    return {"documents": docs, "chunks": chunks}
