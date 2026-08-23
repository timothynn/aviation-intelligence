from __future__ import annotations

from collections import defaultdict
from typing import Any

from .models import Evidence, EvidencePack, SearchHit
from .store import Store
from .vector import EmbeddingIndex


class Retriever:
    def __init__(self, store: Store, vectors: EmbeddingIndex | None = None):
        self.store = store
        self.vectors = vectors

    @staticmethod
    def _authority_boost(hit: SearchHit, filters: dict[str, Any]) -> float:
        score = 0.0
        if filters.get("authority") and hit.metadata.get("authority") == filters["authority"]:
            score += 0.08
        if filters.get("jurisdiction") and hit.metadata.get("jurisdiction") == filters["jurisdiction"]:
            score += 0.06
        if hit.metadata.get("status") == "CURRENT":
            score += 0.03
        return score

    def search(self, query: str, limit: int = 8, candidate_limit: int = 50,
               filters: dict[str, Any] | None = None, use_vector: bool = True) -> EvidencePack:
        filters = filters or {}
        lexical = self.store.lexical_search(query, candidate_limit, filters)
        vector_hits: list[tuple[str, float]] = []
        if use_vector and self.vectors:
            vector_hits = self.vectors.search(query, candidate_limit)

        by_id: dict[str, SearchHit] = {hit.chunk_id: hit for hit in lexical}
        for rank, (chunk_id, score) in enumerate(vector_hits, 1):
            if chunk_id not in by_id:
                rows = self.store.get_chunks([chunk_id])
                if not rows:
                    continue
                row = rows[0]
                by_id[chunk_id] = SearchHit(
                    chunk_id=chunk_id,
                    document_id=row["document_id"],
                    title=row["title"],
                    text=row["text"],
                    score=0.0,
                    metadata={"authority": row["authority"], "jurisdiction": row["jurisdiction"], "status": row["status"],
                              "version": row["version"], "source_url": row["source_url"], "section": row["section"],
                              "paragraph": row["paragraph"], "page_start": row["page_start"], "page_end": row["page_end"]},
                )
            by_id[chunk_id].vector_score = score

        ranked: dict[str, float] = defaultdict(float)
        for rank, hit in enumerate(lexical, 1):
            ranked[hit.chunk_id] += 1.0 / (60 + rank)
        for rank, (chunk_id, _) in enumerate(vector_hits, 1):
            ranked[chunk_id] += 1.0 / (60 + rank)

        scored: list[SearchHit] = []
        for chunk_id, fusion in ranked.items():
            hit = by_id[chunk_id]
            hit.authority_score = self._authority_boost(hit, filters)
            hit.score = fusion + hit.authority_score
            scored.append(hit)
        scored.sort(key=lambda h: h.score, reverse=True)

        # Lightweight lexical/entity reranking. Exact regulatory identifiers receive a modest boost.
        lowered = query.lower()
        tokens = [t for t in lowered.replace("/", " ").split() if len(t) >= 2]
        for hit in scored:
            text = hit.text.lower()
            exact = sum(1 for token in tokens if token in text)
            hit.score += min(0.05, exact * 0.005)
        scored.sort(key=lambda h: h.score, reverse=True)

        evidences = [Evidence(
            document_id=h.document_id,
            title=h.title,
            authority=h.metadata.get("authority"),
            jurisdiction=h.metadata.get("jurisdiction"),
            status=h.metadata.get("status", "UNKNOWN"),
            version=h.metadata.get("version"),
            section=h.metadata.get("section"),
            paragraph=h.metadata.get("paragraph"),
            page_start=h.metadata.get("page_start"),
            page_end=h.metadata.get("page_end"),
            chunk_id=h.chunk_id,
            source_url=h.metadata.get("source_url"),
            text=h.text,
            score=h.score,
        ) for h in scored[:limit]]

        abstain = not evidences or evidences[0].score < 0.005
        return EvidencePack(query=query, generated_at=__import__("datetime").datetime.now(__import__("datetime").timezone.utc),
                            evidences=evidences, filters=filters, retrieval_method="hybrid" if vector_hits else "lexical",
                            abstain=abstain,
                            abstain_reason="No sufficiently relevant indexed evidence was found." if abstain else None)
