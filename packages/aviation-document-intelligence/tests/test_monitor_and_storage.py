from io import BytesIO

from aviation_docint.monitor import MemorySnapshotStore, SourceMonitor
from aviation_docint.storage import LocalObjectStore


def test_local_object_store_roundtrip(tmp_path):
    store = LocalObjectStore(tmp_path)
    stored = store.put("documents/example.txt", BytesIO(b"aviation"), "text/plain")
    assert stored.sha256
    assert stored.size == 8
    assert store.exists("documents/example.txt")
    assert store.open("documents/example.txt").read() == b"aviation"


def test_source_monitor_detects_change(monkeypatch):
    store = MemorySnapshotStore()
    monitor = SourceMonitor(store)

    class Response:
        url = "https://example.test/doc.pdf"
        headers = {"content-type": "application/pdf"}

        def __init__(self, payload):
            self.content = payload

        def raise_for_status(self):
            return None

    payloads = [b"v1", b"v1", b"v2"]

    def fake_get(*args, **kwargs):
        return Response(payloads.pop(0))

    monkeypatch.setattr("aviation_docint.monitor.requests.get", fake_get)

    _, changed1 = monitor.check("example", "https://example.test/doc.pdf")
    _, changed2 = monitor.check("example", "https://example.test/doc.pdf")
    _, changed3 = monitor.check("example", "https://example.test/doc.pdf")

    assert changed1 is True
    assert changed2 is False
    assert changed3 is True
