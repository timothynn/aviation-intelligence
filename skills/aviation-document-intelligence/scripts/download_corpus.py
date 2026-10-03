#!/usr/bin/env python3
"""Download an aviation document test corpus from official first-party sources.

The script deliberately keeps binaries outside git by default. It reads the
source manifest, downloads direct assets or resolves PDF/XML links from the
publisher page, computes SHA-256 checksums, and writes a metadata JSONL file.

Index pages can define ``download_all: true`` and an optional
``link_match`` regular expression so a single authority page can contribute
multiple documents (for example ICAO Annexes 1-19 published by a CAA).

Requirements:
    pip install requests beautifulsoup4 pyyaml
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
import time
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


def request_with_retry(url: str, timeout: int = 60, max_retries: int = 3, stream: bool = False) -> requests.Response:
    """Make HTTP request with exponential backoff retry for timeouts and 5xx errors."""
    for attempt in range(max_retries):
        try:
            response = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=timeout, stream=stream)
            response.raise_for_status()
            return response
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as exc:
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt
                print(f"Timeout/connection error on attempt {attempt + 1}/{max_retries} for {url}, retrying in {wait_time}s...", file=sys.stderr)
                time.sleep(wait_time)
            else:
                raise
        except requests.exceptions.HTTPError as exc:
            if exc.response.status_code >= 500 and attempt < max_retries - 1:
                wait_time = 2 ** attempt
                print(f"Server error {exc.response.status_code} on attempt {attempt + 1}/{max_retries} for {url}, retrying in {wait_time}s...", file=sys.stderr)
                time.sleep(wait_time)
            else:
                raise


def discover_links(page_url: str, desired_types: list[str], link_match: str | None = None) -> list[tuple[str, str, str]]:
    response = request_with_retry(page_url, timeout=60)
    soup = BeautifulSoup(response.text, "html.parser")
    matcher = re.compile(link_match, re.IGNORECASE) if link_match else None
    results: list[tuple[str, str, str]] = []
    for anchor in soup.find_all("a", href=True):
        href = urljoin(page_url, anchor["href"])
        label = " ".join(anchor.get_text(" ", strip=True).split())
        path = href.lower().split("?", 1)[0]
        if matcher and not matcher.search(label) and not matcher.search(href):
            continue
        if "pdf" in desired_types and (path.endswith(".pdf") or "pdf" in label.lower()):
            results.append(("pdf", href, label))
        if "xml" in desired_types and (path.endswith(".xml") or "xml" in label.lower()):
            results.append(("xml", href, label))
        if "zip" in desired_types and (path.endswith(".zip") or "zip" in label.lower()):
            results.append(("zip", href, label))
    unique: list[tuple[str, str, str]] = []
    seen: set[tuple[str, str]] = set()
    for kind, url, label in results:
        key = (kind, url)
        if key not in seen:
            unique.append((kind, url, label))
            seen.add(key)
    return unique


def resolve_assets(record: dict[str, Any]) -> list[tuple[str, str, str | None]]:
    assets: list[tuple[str, str, str | None]] = []
    if record.get("source_url"):
        for kind in record.get("asset_types", ["pdf"]):
            assets.append((kind, record["source_url"], None))
    if record.get("source_page"):
        desired = list(record.get("asset_types", ["pdf"]))
        discovered = discover_links(record["source_page"], desired, record.get("link_match"))
        if not discovered:
            raise RuntimeError(f"No downloadable links discovered from {record['source_page']}")
        if record.get("download_all"):
            for item in discovered:
                assets.append(item)
        else:
            by_type: dict[str, tuple[str, str, str]] = {}
            for item in discovered:
                by_type.setdefault(item[0], item)
            for kind in desired:
                if kind in by_type:
                    assets.append(by_type[kind])
    seen: set[tuple[str, str]] = set()
    final: list[tuple[str, str, str | None]] = []
    for kind, url, label in assets:
        key = (kind, url)
        if key not in seen:
            final.append((kind, url, label))
            seen.add(key)
    return final


def download_one(source: Source, output_dir: Path, timeout: int = 120) -> list[dict[str, Any]]:
    record = source.record
    source_dir = output_dir / safe_name(record["authority"]) / safe_name(source.id)
    source_dir.mkdir(parents=True, exist_ok=True)
    metadata: list[dict[str, Any]] = []
    for kind, url, link_label in resolve_assets(record):
        response = request_with_retry(url, timeout=timeout, stream=True)
        content_type = response.headers.get("content-type", "").split(";", 1)[0].lower()
        suffix = mimetypes.guess_extension(content_type) or ("." + kind)
        if suffix == ".jpe":
            suffix = ".jpg"
        asset_title = link_label or record["title"]
        filename = safe_name(asset_title) + suffix
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
                "title": asset_title,
                "parentTitle": record["title"],
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
                "publisherDisclaimer": record.get("publisher_disclaimer"),
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
    parser.add_argument("--failure-threshold", type=int, default=None, 
                       help="Maximum allowed failures before exiting with error (default: fail if any source fails)")
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
                print(f"OK  {source.id} ({len(future.result())} assets)")
            except Exception as exc:  # noqa: BLE001
                failures.append({"sourceId": source.id, "error": str(exc)})
                print(f"ERR {source.id}: {exc}", file=sys.stderr)

    metadata_path = output_dir / "manifest.jsonl"
    with metadata_path.open("w", encoding="utf-8") as handle:
        for row in sorted(rows, key=lambda item: (item["authority"], item["sourceId"], item["assetType"], item["title"])):
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")

    if failures:
        (output_dir / "failures.json").write_text(json.dumps(failures, indent=2), encoding="utf-8")
        failure_count = len(failures)
        total_count = len(sources)
        print(f"Completed with {failure_count}/{total_count} failures. See {output_dir / 'failures.json'}", file=sys.stderr)
        
        threshold = args.failure_threshold if args.failure_threshold is not None else 0
        if failure_count > threshold:
            print(f"Failure count {failure_count} exceeds threshold {threshold}", file=sys.stderr)
            return 2
        else:
            print(f"Failure count {failure_count} within threshold {threshold}, continuing", file=sys.stderr)

    print(f"Downloaded {len(rows)} assets. Metadata: {metadata_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
