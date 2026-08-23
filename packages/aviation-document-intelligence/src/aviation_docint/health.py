from __future__ import annotations

from .store import Store


def health(store: Store) -> dict:
    return {"status": "ok", "stats": store.stats()}
