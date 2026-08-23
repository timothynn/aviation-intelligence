from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime
from typing import Any


@dataclass(slots=True)
class Page:
    number: int
    text: str
    title: str | None = None


@dataclass(slots=True)
class Document:
    document_id: str
    title: str
    authority: str | None
    jurisdiction: str | None
    status: str = "UNKNOWN"
    version: str | None = None
    document_type: str | None = None
    source_url: str | None = None
    source_path: str | None = None
    effective_from: date | None = None
    effective_to: date | None = None
    publisher: str | None = None
    checksum_sha256: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)
    pages: list[Page] = field(default_factory=list)


@dataclass(slots=True)
class Chunk:
    chunk_id: str
    document_id: str
    text: str
    page_start: int | None = None
    page_end: int | None = None
    section: str | None = None
    paragraph: str | None = None
    heading_path: tuple[str, ...] = ()
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class SearchHit:
    chunk_id: str
    document_id: str
    title: str
    text: str
    score: float
    lexical_score: float = 0.0
    vector_score: float = 0.0
    authority_score: float = 0.0
    version_score: float = 0.0
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class Evidence:
    document_id: str
    title: str
    authority: str | None
    jurisdiction: str | None
    status: str
    version: str | None
    section: str | None
    paragraph: str | None
    page_start: int | None
    page_end: int | None
    chunk_id: str
    source_url: str | None
    text: str
    score: float


@dataclass(slots=True)
class EvidencePack:
    query: str
    generated_at: datetime
    evidences: list[Evidence]
    filters: dict[str, Any] = field(default_factory=dict)
    retrieval_method: str = "hybrid"
    abstain: bool = False
    abstain_reason: str | None = None
