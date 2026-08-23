from __future__ import annotations

import re
from typing import Any

from .models import SearchHit


IDENTIFIER = re.compile(r"\b(?:A\d{1,2}|B\d{1,2}|C\d{1,2}|D\d{1,2}|E\d{1,2}|[A-Z]{2,}[.-][A-Z0-9.-]+|Annex\s+\d{1,2}|Doc\s+\d+)\b", re.I)


def score_match(query: str, hit: SearchHit, authority: str | None = None, jurisdiction: str | None = None) -> float:
    q = query.lower()
    text = hit.text.lower()
    score = hit.score
    score += min(0.08, sum(1 for token in q.split() if len(token) > 2 and token in text) * 0.004)
    identifiers = [m.group(0).lower() for m in IDENTIFIER.finditer(query)]
    for identifier in identifiers:
        if identifier in text:
            score += 0.08
    if authority and hit.metadata.get("authority") == authority:
        score += 0.08
    if jurisdiction and hit.metadata.get("jurisdiction") == jurisdiction:
        score += 0.06
    if hit.metadata.get("status") == "CURRENT":
        score += 0.03
    return score


def rerank(query: str, hits: list[SearchHit], metadata: dict[str, Any] | None = None) -> list[SearchHit]:
    metadata = metadata or {}
    for hit in hits:
        hit.score = score_match(query, hit, metadata.get("authority"), metadata.get("jurisdiction"))
    return sorted(hits, key=lambda item: item.score, reverse=True)
