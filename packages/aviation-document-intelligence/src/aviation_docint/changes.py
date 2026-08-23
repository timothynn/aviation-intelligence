from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from typing import Iterable


@dataclass(frozen=True, slots=True)
class Change:
    path: str
    kind: str
    before_hash: str | None
    after_hash: str | None
    summary: str


def fingerprint(text: str) -> str:
    return sha256(" ".join(text.split()).encode("utf-8")).hexdigest()


def compare_documents(before: dict[str, str], after: dict[str, str]) -> list[Change]:
    changes: list[Change] = []
    for path in sorted(set(before) | set(after)):
        old = before.get(path)
        new = after.get(path)
        if old is None:
            changes.append(Change(path, "added", None, fingerprint(new), "new source item"))
        elif new is None:
            changes.append(Change(path, "removed", fingerprint(old), None, "source item removed"))
        elif fingerprint(old) != fingerprint(new):
            changes.append(Change(path, "modified", fingerprint(old), fingerprint(new), "normalized document content changed"))
    return changes


def changed_ratio(before: Iterable[str], after: Iterable[str]) -> float:
    old = set(before)
    new = set(after)
    if not old and not new:
        return 0.0
    return len(old ^ new) / max(1, len(old | new))
