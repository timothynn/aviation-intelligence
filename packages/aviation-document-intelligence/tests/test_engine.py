from pathlib import Path

from aviation_docint.chunker import chunk_document
from aviation_docint.models import Document, Page
from aviation_docint.store import Store


def test_chunker_preserves_regulatory_identifier():
    doc = Document(
        document_id="easa-test",
        title="Test Regulation",
        authority="EASA",
        jurisdiction="EU/EEA",
        status="CURRENT",
        version="2026",
        pages=[Page(1, "PART-TCO\n\nTCO.GEN.100 Operator responsibilities\n\nThe operator shall establish and maintain procedures for safe operation.")],
    )
    chunks = chunk_document(doc)
    assert chunks
    assert any("TCO.GEN.100" in c.text for c in chunks)


def test_fts_exact_identifier_and_filtering(tmp_path: Path):
    store = Store(tmp_path / "test.sqlite")
    doc = Document(
        document_id="safa",
        title="SAFA Test",
        authority="EASA",
        jurisdiction="EU/EEA",
        status="CURRENT",
        version="2026",
        pages=[Page(1, "A17\n\nHarness requirement for flight crew seats.")],
    )
    store.upsert_document(doc)
    store.replace_chunks(doc.document_id, chunk_document(doc))
    hits = store.lexical_search("A17", filters={"authority": "EASA", "current_only": True})
    assert hits
    assert hits[0].metadata["authority"] == "EASA"
    assert "A17" in hits[0].text
    store.close()


def test_abstention_when_no_evidence(tmp_path: Path):
    store = Store(tmp_path / "test.sqlite")
    assert store.lexical_search("does-not-exist") == []
    store.close()
