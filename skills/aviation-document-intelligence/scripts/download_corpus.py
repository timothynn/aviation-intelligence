#!/usr/bin/env python3
"""Download an aviation document test corpus from official first-party sources.

The script deliberately keeps binaries outside git by default. It reads the
source manifest, downloads direct assets or resolves PDF/XML links from the
publisher page, computes SHA-256 checksums, and writes a metadata JSONL file.

Requirements:
    pip install requests beautifulsoup4 pyyaml

Examples:
    python scripts/download_corpus.py --manifest skills/aviation-document-intelligence/source-manifest.yaml
    python scripts/download_corpus.py --only easa-ear-tco-2026-07 --output data/corpus
"""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import mimetypes
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import urljoin

import requests
import yaml
from bs4 import BeautifulSoup

USER_AGENT = "aviation-intelligence-document-corpus/1.0 (+https://github.com/timothynn/aviation-intelligence)"


@dataclass(frozen=True)
class Source:
    id: str
    record: dict[str, Any]


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def safe_name(value: str) -> str:
    value = re.sub(r"[^A-Za-z0-9._-]+", "-", value).strip("-")
    return value[:180] or "document"


def discover_links(page_url: str, desired_types: list[str]) -> list[tuple[str, str]]:
    response = requests.get(page_url, headers={"User-Agent": USER_AGENT}, timeout=60)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    results: list[tuple[str, str]] = []
    for anchor in soup.find_all("a", href=True):
        href = urljoin(page_url, anchor["href"])
        label = " ".join(anchor.get_text(" ", strip=True).split()).lower()
        path = href.lower().split("?", 1)[0]
        if "pdf" in desired_types and (path.endswith(".pdf") or "pdf" in label):
            results.append(("pdf", href))
        if "xml" in desired_types and (path.endswith(".xml") or "xml" in label):
            results.append(("xml", href))
        if "zip" in desired_types and (path.endswith(".zip") or "zip" in label):
            results.append(("zip", href))
    unique: list[tuple[str, str]] = []
    seen: set[str] = set()
    for kind, url in results:
        if url not in seen:
            unique.append((kind, url))
            seen.add(url)
    return unique


def resolve_assets(record: dict[str, Any]) -> list[tuple[str, str]]:
    assets: list[tuple[str, str]] = []
    if record.get("source_url"):
        for kind in record.get("asset_types", ["pdf"]):
            assets.append((kind, record["source_url"]))
    if record.get("source_page"):
        desired = list(record.get("asset_types", ["pdf"]))
        discovered = discover_links(record["source_page"], desired)
        if not discovered:
            raise RuntimeError(f"No downloadable links discovered from {record['source_page']}")
        by_type: dict[str, tuple[str, str]] = {}
        for kind, url in discovered:
            by_type.setdefault(kind, (kind, url))
        for kind in desired:
            if kind in by_type:
                assets.append(by_type[kind])
    seen: set[str] = set()
    final: list[tuple[str, str]] = []
    for kind, url in assets:
        if url not in seen:
            final.append((kind, url))
            seen.add(url)
    return final


def download_one(source: Source, output_dir: Path, timeout: int = 120) -> list[dict[str, Any]]:
    record = source.record
    source_dir = output_dir / safe_name(record["authority"]) / safe_name(source.id)
    source_dir.mkdir(parents=True, exist_ok=True)
    metadata: list[dict[str, Any]] = []
    for kind, url in resolve_assets(record):
        response = requests.get(url, headers={"User-Agent": USER_AGENT}, stream=True, timeout=timeout)
        response.raise_for_status()
        content_type = response.headers.get("content-type", "").split(";", 1)[0].lower()
        suffix = mimetypes.guess_extension(content_type) or ("." + kind)
        if suffix == ".jpe":
            suffix = ".jpg"
        filename = safe_name(record["title"]) + suffix
        destination = source_dir / filename
        with destination.open("wb") as handle:
            for chunk in response.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    handle.write(chunk)
        metadata.append(
            {
                "sourceId": source.id,
                "authority": record["authority"],
                "jurisdiction": record.get("jurisdiction"),
                "title": record["title"],
                "version": record.get("version"),
                "type": record.get("type"),
                "assetType": kind,
                "sourceUrl": record.get("source_url") or record.get("source_page"),
                "downloadUrl": url,
                "retrievedAt": __import__("datetime").datetime.now(__import__("datetime").timezone.utc).isoformat(),
                "path": str(destination).replace(os.sep, "/"),
                "mimeType": content_type,
                "bytes": destination.stat().st_size,
                "sha256": sha256_file(destination),
                "licensePolicy": record.get("policy", "source_reference"),
            }
        )
    return metadata


def load_sources(path: Path) -> list[Source]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    return [Source(item["id"], item) for item in data.get("sources", [])]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", default="skills/aviation-document-intelligence/source-manifest.yaml")
    parser.add_argument("--output", default="data/corpus")
    parser.add_argument("--only", action="append", default=[])
    parser.add_argument("--workers", type=int, default=4)
    args = parser.parse_args()

    manifest = Path(args.manifest)
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    sources = load_sources(manifest)
    if args.only:
        wanted = set(args.only)
        sources = [source for source in sources if source.id in wanted]

    failures: list[dict[str, str]] = []
    rows: list[dict[str, Any]] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, args.workers)) as pool:
        future_map = {pool.submit(download_one, source, output_dir): source for source in sources}
        for future in concurrent.futures.as_completed(future_map):
            source = future_map[future]
            try:
                rows.extend(future.result())
                print(f"OK  {source.id}")
            except Exception as exc:  # noqa: BLE001
                failures.append({"sourceId": source.id, "error": str(exc)})
                print(f"ERR {source.id}: {exc}", file=sys.stderr)

    metadata_path = output_dir / "manifest.jsonl"
    with metadata_path.open("w", encoding="utf-8") as handle:
        for row in sorted(rows, key=lambda item: (item["authority"], item["sourceId"], item["assetType"])):
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")

    if failures:
        (output_dir / "failures.json").write_text(json.dumps(failures, indent=2), encoding="utf-8")
        print(f"Completed with {len(failures)} failures. See {output_dir / 'failures.json'}", file=sys.stderr)
        return 2

    print(f"Downloaded {len(rows)} assets. Metadata: {metadata_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
