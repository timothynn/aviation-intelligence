from __future__ import annotations

import hashlib
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Iterable, Protocol

import requests


@dataclass(frozen=True, slots=True)
class SourceSnapshot:
    source_id: str
    url: str
    retrieved_at: datetime
    sha256: str
    content_type: str | None
    byte_count: int


class SnapshotStore(Protocol):
    def latest(self, source_id: str) -> SourceSnapshot | None: ...
    def save(self, snapshot: SourceSnapshot) -> None: ...


class MemorySnapshotStore:
    def __init__(self) -> None:
        self._items: dict[str, SourceSnapshot] = {}

    def latest(self, source_id: str) -> SourceSnapshot | None:
        return self._items.get(source_id)

    def save(self, snapshot: SourceSnapshot) -> None:
        self._items[snapshot.source_id] = snapshot


class SourceMonitor:
    """Fetches first-party sources and reports content changes.

    Scheduling is intentionally external (cron, Celery, Hangfire, Kubernetes
    CronJob, GitHub Actions, etc.). This component remains deterministic.
    """

    def __init__(self, store: SnapshotStore, timeout: int = 60) -> None:
        self.store = store
        self.timeout = timeout

    def check(self, source_id: str, url: str) -> tuple[SourceSnapshot, bool]:
        response = requests.get(url, timeout=self.timeout, allow_redirects=True,
                                headers={"User-Agent": "aviation-intelligence-source-monitor/1.0"})
        response.raise_for_status()
        body = response.content
        snapshot = SourceSnapshot(
            source_id=source_id,
            url=response.url,
            retrieved_at=datetime.now(timezone.utc),
            sha256=hashlib.sha256(body).hexdigest(),
            content_type=response.headers.get("content-type"),
            byte_count=len(body),
        )
        previous = self.store.latest(source_id)
        changed = previous is None or previous.sha256 != snapshot.sha256
        if changed:
            self.store.save(snapshot)
        return snapshot, changed

    def check_many(self, sources: Iterable[tuple[str, str]]) -> list[tuple[SourceSnapshot, bool]]:
        return [self.check(source_id, url) for source_id, url in sources]
