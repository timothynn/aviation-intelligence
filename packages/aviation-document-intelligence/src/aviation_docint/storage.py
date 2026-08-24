from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import BinaryIO, Protocol


@dataclass(frozen=True, slots=True)
class StoredObject:
    key: str
    uri: str
    sha256: str
    size: int
    content_type: str | None = None


class ObjectStore(Protocol):
    def put(self, key: str, stream: BinaryIO, content_type: str | None = None) -> StoredObject: ...
    def open(self, key: str) -> BinaryIO: ...
    def exists(self, key: str) -> bool: ...


class LocalObjectStore:
    """Local filesystem implementation used for development and tests."""

    def __init__(self, root: str | Path):
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)

    def put(self, key: str, stream: BinaryIO, content_type: str | None = None) -> StoredObject:
        import hashlib

        destination = self.root / key
        destination.parent.mkdir(parents=True, exist_ok=True)
        digest = hashlib.sha256()
        size = 0
        with destination.open("wb") as handle:
            for block in iter(lambda: stream.read(1024 * 1024), b""):
                if not block:
                    break
                handle.write(block)
                digest.update(block)
                size += len(block)
        return StoredObject(key, destination.as_uri(), digest.hexdigest(), size, content_type)

    def open(self, key: str) -> BinaryIO:
        return (self.root / key).open("rb")

    def exists(self, key: str) -> bool:
        return (self.root / key).exists()
