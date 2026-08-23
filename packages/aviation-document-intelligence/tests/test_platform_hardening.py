from datetime import date

from aviation_docint.applicability import ApplicabilityContext, rank_applicable
from aviation_docint.graph import Edge, KnowledgeGraph, Node
from aviation_docint.llm import build_grounded_prompt
from aviation_docint.models import Document, EvidencePack
from aviation_docint.security import AccessDecision, DocumentPolicy, Principal, authorize
from aviation_docint.temporal import resolve_documents


def doc(document_id: str, version: str, start: date, end: date | None, status: str = "CURRENT") -> Document:
    return Document(document_id, "Air Ops", "EASA", "EU/EEA", status, version, "regulation", effective_from=start, effective_to=end)


def test_temporal_resolution_selects_applicable_versions() -> None:
    old = doc("old", "2024", date(2024, 1, 1), date(2025, 12, 31), "HISTORICAL")
    new = doc("new", "2026", date(2026, 1, 1), None)
    result = resolve_documents([old, new], date(2026, 6, 1))
    assert [item.document_id for item in result.selected] == ["new"]


def test_applicability_uses_authority_and_jurisdiction() -> None:
    d = doc("easa", "2026", date(2026, 1, 1), None)
    result = rank_applicable([d], ApplicabilityContext(authority="EASA", jurisdiction="EU/EEA", effective_date=date(2026, 8, 1)))
    assert result[0].applicable


def test_graph_resolves_regulatory_path() -> None:
    g = KnowledgeGraph()
    g.bulk_add(
        [Node("icao6", "annex", "Annex 6", {}), Node("easaops", "rule", "Air Ops", {}), Node("safa", "scheme", "SAFA", {})],
        [Edge("icao6", "implemented_by", "easaops"), Edge("easaops", "supports", "safa")],
    )
    assert g.path("icao6", "safa") == [["icao6", "easaops", "safa"]]


def test_private_document_denied_without_role() -> None:
    decision = authorize(Principal("u1"), DocumentPolicy(visibility="restricted", required_roles=frozenset({"inspector"})))
    assert decision is AccessDecision.DENY


def test_grounded_prompt_contains_evidence_and_guardrail() -> None:
    pack = EvidencePack("What is A17?", __import__("datetime").datetime.now(__import__("datetime").timezone.utc), [])
    prompt = build_grounded_prompt("What is A17?", pack)
    assert "Do not invent regulatory requirements" in prompt.system
    assert "No sufficient evidence" in prompt.user
