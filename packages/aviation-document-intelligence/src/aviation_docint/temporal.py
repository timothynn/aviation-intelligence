from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Iterable

from .models import Document


@dataclass(frozen=True, slots=True)
class TemporalResolution:
    query_date: date
    selected: tuple[Document, ...]
    excluded: tuple[tuple[str, str], ...]
    ambiguous: bool
    reason: str


def _contains(doc: Document, when: date) -> bool:
    if doc.effective_from and when < doc.effective_from:
        return False
    if doc.effective_to and when > doc.effective_to:
        return False
    return True


def resolve_documents(documents: Iterable[Document], when: date, prefer_current: bool = True) -> TemporalResolution:
    docs = list(documents)
    candidates = [d for d in docs if _contains(d, when) and d.status not in {"WITHDRAWN", "DRAFT"}]
    excluded: list[tuple[str, str]] = []
    for d in docs:
        if d not in candidates:
            excluded.append((d.document_id, "outside effective window or non-authoritative status"))

    candidates.sort(key=lambda d: (
        d.status != "CURRENT" if prefer_current else False,
        d.effective_from is None,
        d.effective_from or date.min,
        d.version or "",
    ), reverse=True)

    ambiguous = False
    reason = "exactly one applicable version" if len(candidates) == 1 else "multiple applicable versions require authority/version precedence"
    if len(candidates) > 1:
        groups = {(d.authority, d.document_type, d.title) for d in candidates}
        ambiguous = len(groups) == 1

    return TemporalResolution(when, tuple(candidates), tuple(excluded), ambiguous, reason)
