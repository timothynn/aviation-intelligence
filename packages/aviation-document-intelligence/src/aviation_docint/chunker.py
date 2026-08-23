from __future__ import annotations

import hashlib
import re

from .models import Chunk, Document

HEADING_RE = re.compile(r"^(?:CHAPTER|Chapter|PART|Part|SECTION|Section|SUBPART|Subpart|APPENDIX|Appendix|[A-Z][A-Z0-9 /&()\-]{3,})\s*$")
PARAGRAPH_RE = re.compile(r"^(?:\d+(?:\.\d+){0,5}|[A-Z]\d{1,3}|[A-Z]{1,3}-\d{1,3})\b")


def _chunk_id(document_id: str, page: int, ordinal: int, text: str) -> str:
    digest = hashlib.sha1(text.encode("utf-8")).hexdigest()[:12]
    return f"{document_id}:{page}:{ordinal}:{digest}"


def chunk_document(document: Document, max_chars: int = 3500, overlap_chars: int = 350) -> list[Chunk]:
    chunks: list[Chunk] = []
    ordinal = 0
    heading_path: list[str] = []
    for page in document.pages:
        paragraphs = [p.strip() for p in re.split(r"\n\s*\n|\n(?=[A-Z]\d{1,3}\b|\d+(?:\.\d+){0,5}\b)", page.text) if p.strip()]
        current = ""
        current_section: str | None = None
        current_paragraph: str | None = None

        def emit(text: str) -> None:
            nonlocal ordinal
            if not text.strip():
                return
            value = text.strip()
            ordinal += 1
            chunks.append(Chunk(
                chunk_id=_chunk_id(document.document_id, page.number, ordinal, value),
                document_id=document.document_id,
                text=value,
                page_start=page.number,
                page_end=page.number,
                section=current_section,
                paragraph=current_paragraph,
                heading_path=tuple(heading_path),
                metadata={"authority": document.authority, "jurisdiction": document.jurisdiction, "status": document.status, "version": document.version},
            ))

        for paragraph in paragraphs:
            if HEADING_RE.match(paragraph) and len(paragraph) < 180:
                if current:
                    emit(current)
                    current = ""
                heading_path = (heading_path + [paragraph])[-6:]
                current_section = paragraph
                continue
            match = PARAGRAPH_RE.match(paragraph)
            if match:
                current_paragraph = match.group(0)
            candidate = f"{current}\n\n{paragraph}".strip() if current else paragraph
            if len(candidate) > max_chars:
                if current:
                    emit(current)
                    tail = current[-overlap_chars:] if overlap_chars else ""
                    current = (tail + "\n\n" + paragraph).strip()
                else:
                    start = 0
                    while start < len(paragraph):
                        part = paragraph[start:start + max_chars]
                        emit(part)
                        start += max_chars - overlap_chars
                    current = ""
            else:
                current = candidate
        emit(current)
    return chunks
