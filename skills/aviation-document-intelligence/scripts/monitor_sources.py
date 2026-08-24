from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

import yaml

PACKAGE_ROOT = Path(__file__).resolve().parents[3] / "packages" / "aviation-document-intelligence"
src = PACKAGE_ROOT / "src"
if str(src) not in sys.path:
    sys.path.insert(0, str(src))

from aviation_docint.monitor import MemorySnapshotStore, SourceMonitor  # noqa: E402


def load_sources(manifest: Path) -> list[tuple[str, str]]:
    payload = yaml.safe_load(manifest.read_text(encoding="utf-8"))
    sources: list[tuple[str, str]] = []
    for source in payload.get("sources", []):
        source_id = source.get("id")
        url = source.get("source_page")
        if source_id and url and source.get("local_test", False):
            sources.append((source_id, url))
    return sources


def main() -> int:
    parser = argparse.ArgumentParser(description="Check registered aviation source pages for changes.")
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--output", default="source-monitor-report.json")
    args = parser.parse_args()

    monitor = SourceMonitor(MemorySnapshotStore())
    results = []
    for source_id, url in load_sources(Path(args.manifest)):
        try:
            snapshot, changed = monitor.check(source_id, url)
            results.append({
                "sourceId": source_id,
                "url": snapshot.url,
                "changed": changed,
                "sha256": snapshot.sha256,
                "contentType": snapshot.content_type,
                "bytes": snapshot.byte_count,
                "retrievedAt": snapshot.retrieved_at.isoformat(),
                "error": None,
            })
        except Exception as exc:  # pragma: no cover - network behavior
            results.append({"sourceId": source_id, "url": url, "changed": False, "error": str(exc)})

    report = {"sourcesChecked": len(results), "results": results}
    Path(args.output).write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0 if all(item.get("error") is None for item in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
