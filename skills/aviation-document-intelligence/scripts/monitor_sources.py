from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path
import sys

import yaml

PACKAGE_ROOT = Path(__file__).resolve().parents[3] / "packages" / "aviation-document-intelligence"
src = PACKAGE_ROOT / "src"
if str(src) not in sys.path:
    sys.path.insert(0, str(src))

from aviation_docint.monitor import MemorySnapshotStore, SourceSnapshot, SourceMonitor  # noqa: E402


def load_sources(manifest: Path) -> list[tuple[str, str]]:
    payload = yaml.safe_load(manifest.read_text(encoding="utf-8"))
    sources: list[tuple[str, str]] = []
    for source in payload.get("sources", []):
        source_id = source.get("id")
        url = source.get("source_page")
        if source_id and url and source.get("local_test", False):
            sources.append((source_id, url))
    return sources


def load_snapshots(path: Path) -> MemorySnapshotStore:
    store = MemorySnapshotStore()
    if not path.exists():
        return store

    payload = json.loads(path.read_text(encoding="utf-8"))
    for item in payload.get("snapshots", []):
        if not item.get("sourceId") or not item.get("sha256"):
            continue
        store.save(SourceSnapshot(
            source_id=item["sourceId"],
            url=item["url"],
            retrieved_at=datetime.fromisoformat(item["retrievedAt"]),
            sha256=item["sha256"],
            content_type=item.get("contentType"),
            byte_count=int(item.get("bytes", 0)),
        ))
    return store


def save_snapshots(path: Path, store: MemorySnapshotStore, source_ids: list[str]) -> None:
    snapshots = []
    for source_id in source_ids:
        snapshot = store.latest(source_id)
        if snapshot is None:
            continue
        snapshots.append({
            "sourceId": snapshot.source_id,
            "url": snapshot.url,
            "retrievedAt": snapshot.retrieved_at.isoformat(),
            "sha256": snapshot.sha256,
            "contentType": snapshot.content_type,
            "bytes": snapshot.byte_count,
        })
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({"snapshots": snapshots}, indent=2), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Check registered aviation source pages for changes.")
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--output", default="source-monitor-report.json")
    parser.add_argument("--state", default=".cache/source-monitor/snapshots.json")
    parser.add_argument("--fail-on-error", action="store_true")
    args = parser.parse_args()

    state_path = Path(args.state)
    store = load_snapshots(state_path)
    monitor = SourceMonitor(store)
    results = []
    source_ids: list[str] = []

    for source_id, url in load_sources(Path(args.manifest)):
        source_ids.append(source_id)
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

    save_snapshots(state_path, store, source_ids)
    report = {
        "sourcesChecked": len(results),
        "changed": sum(1 for item in results if item.get("changed")),
        "errors": sum(1 for item in results if item.get("error")),
        "results": results,
    }
    Path(args.output).write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 1 if args.fail_on_error and report["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
