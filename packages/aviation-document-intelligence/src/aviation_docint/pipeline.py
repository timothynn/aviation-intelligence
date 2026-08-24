from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Protocol

from .chunker import chunk_document
from .ingest import ingest_path
from .models import Chunk, Document


class DocumentSink(Protocol):
    def upsert_document(self, document: Document) -> None: ...
    def replace_chunks(self, document_id: str, chunks: list[Chunk]) -> int: ...


@dataclass(slots=True)
class IngestResult:
    document_id: str
    title: str
    chunks: int
    source_path: str


class IngestionPipeline:
    """Deterministic ingestion coordinator.

    Storage, search and scheduling are intentionally injected so this can run
    locally or behind queue workers without changing parsing behavior.
    """

    def __init__(self, sink: DocumentSink):
        self.sink = sink

    def ingest_file(self, path: str | Path) -> IngestResult:
        source = Path(path)
        document = ingest_path(source)
        chunks = list(chunk_document(document))
        self.sink.upsert_document(document)
        count = self.sink.replace_chunks(document.document_id, chunks)
        return IngestResult(document.document_id, document.title, count, str(source))

    def ingest_many(self, paths: list[str | Path]) -> list[IngestResult]:
        return [self.ingest_file(path) for path in paths]
