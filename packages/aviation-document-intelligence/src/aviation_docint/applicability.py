from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Iterable, Mapping

from .models import Document


@dataclass(frozen=True, slots=True)
class ApplicabilityContext:
    authority: str | None = None
    jurisdiction: str | None = None
    operator_type: str | None = None
    aircraft_type: str | None = None
    operation: str | None = None
    effective_date: date | None = None
    entities: Mapping[str, str] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class ApplicabilityResult:
    document_id: str
    applicable: bool
    score: float
    reasons: tuple[str, ...]


def score_document(document: Document, context: ApplicabilityContext) -> ApplicabilityResult:
    score = 0.0
    reasons: list[str] = []
    if context.authority and document.authority == context.authority:
        score += 0.35
        reasons.append("authority match")
    if context.jurisdiction and document.jurisdiction == context.jurisdiction:
        score += 0.25
        reasons.append("jurisdiction match")
    if context.effective_date:
        if document.effective_from and context.effective_date < document.effective_from:
            return ApplicabilityResult(document.document_id, False, 0.0, ("effective date precedes document",))
        if document.effective_to and context.effective_date > document.effective_to:
            return ApplicabilityResult(document.document_id, False, 0.0, ("effective date follows document",))
        score += 0.15
        reasons.append("effective-date match")

    declared = {k.lower(): str(v).lower() for k, v in document.metadata.get("applicability", {}).items()}
    for key, expected in context.entities.items():
        actual = declared.get(key.lower())
        if actual and actual == str(expected).lower():
            score += 0.15
            reasons.append(f"{key} match")
        elif actual and actual != str(expected).lower():
            return ApplicabilityResult(document.document_id, False, score, (f"{key} mismatch",))

    if not reasons:
        reasons.append("no positive applicability evidence")
    return ApplicabilityResult(document.document_id, score >= 0.25, score, tuple(reasons))


def rank_applicable(documents: Iterable[Document], context: ApplicabilityContext) -> list[ApplicabilityResult]:
    results = [score_document(doc, context) for doc in documents]
    return sorted(results, key=lambda item: (item.applicable, item.score), reverse=True)
