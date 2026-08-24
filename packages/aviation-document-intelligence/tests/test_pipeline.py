from pathlib import Path

from aviation_docint.models import Chunk, Document
from aviation_docint.pipeline import IngestionPipeline


class MemorySink:
    def __init__(self):
        self.documents = {}
        self.chunks = {}

    def upsert_document(self, document: Document) -> None:
        self.documents[document.document_id] = document

    def replace_chunks(self, document_id: str, chunks: list[Chunk]) -> int:
        self.chunks[document_id] = chunks
        return len(chunks)


def test_ingestion_pipeline_writes_document_and_chunks(tmp_path, monkeypatch):
    sink = MemorySink()
    pipeline = IngestionPipeline(sink)
    source = tmp_path / "sample.txt"
    source.write_text("# SAFA\n\nA17 harness requirement", encoding="utf-8")

    result = pipeline.ingest_file(Path(source))

    assert result.document_id in sink.documents
    assert result.chunks == len(sink.chunks[result.document_id])
    assert result.chunks > 0
