from __future__ import annotations

from pathlib import Path
import re
import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup
from pypdf import PdfReader

from .models import Document, Page


def _clean(text: str) -> str:
    return re.sub(r"\n{3,}", "\n\n", re.sub(r"[ \t]+", " ", text)).strip()


def parse_pdf(path: Path) -> tuple[str, list[Page]]:
    reader = PdfReader(str(path))
    pages: list[Page] = []
    title = path.stem
    for number, raw in enumerate(reader.pages, 1):
        text = _clean(raw.extract_text() or "")
        pages.append(Page(number=number, text=text))
    return title, pages


def parse_html(path: Path) -> tuple[str, list[Page]]:
    soup = BeautifulSoup(path.read_text(encoding="utf-8", errors="ignore"), "html.parser")
    title = soup.title.get_text(" ", strip=True) if soup.title else path.stem
    text = _clean(soup.get_text("\n"))
    return title, [Page(number=1, text=text)]


def parse_xml(path: Path) -> tuple[str, list[Page]]:
    root = ET.fromstring(path.read_bytes())
    title = root.findtext(".//title") or path.stem
    text = _clean("\n".join(root.itertext()))
    return title, [Page(number=1, text=text)]


def parse_text(path: Path) -> tuple[str, list[Page]]:
    return path.stem, [Page(number=1, text=_clean(path.read_text(encoding="utf-8", errors="ignore")))]


def parse_file(path: Path) -> tuple[str, list[Page]]:
    suffix = path.suffix.lower()
    if suffix == ".pdf":
        return parse_pdf(path)
    if suffix in {".html", ".htm"}:
        return parse_html(path)
    if suffix == ".xml":
        return parse_xml(path)
    if suffix in {".txt", ".md"}:
        return parse_text(path)
    raise ValueError(f"Unsupported document type: {path}")


def build_document(path: Path, document_id: str, metadata: dict) -> Document:
    title, pages = parse_file(path)
    return Document(
        document_id=document_id,
        title=metadata.get("title") or title,
        authority=metadata.get("authority"),
        jurisdiction=metadata.get("jurisdiction"),
        status=metadata.get("status", "UNKNOWN"),
        version=metadata.get("version"),
        document_type=metadata.get("type"),
        source_url=metadata.get("downloadUrl") or metadata.get("sourceUrl"),
        source_path=str(path),
        publisher=metadata.get("publisher"),
        checksum_sha256=metadata.get("sha256"),
        metadata=metadata,
        pages=pages,
    )
