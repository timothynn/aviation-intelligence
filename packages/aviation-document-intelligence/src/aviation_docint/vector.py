from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable

try:
    import numpy as np
except ImportError:  # pragma: no cover
    np = None


class EmbeddingIndex:
    """Optional local embedding index.

    Uses sentence-transformers when installed. Vectors are persisted as an NPZ
    plus a JSONL mapping so the retrieval engine can remain provider-neutral.
    """

    def __init__(self, root: str | Path, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)
        self.model_name = model_name
        self.ids_path = self.root / "ids.json"
        self.vectors_path = self.root / "vectors.npy"
        self._model = None

    @property
    def available(self) -> bool:
        return np is not None

    def _load_model(self):
        if self._model is None:
            try:
                from sentence_transformers import SentenceTransformer
            except ImportError as exc:
                raise RuntimeError("Install requirements-vector.txt for vector search") from exc
            self._model = SentenceTransformer(self.model_name)
        return self._model

    def build(self, items: Iterable[tuple[str, str]], batch_size: int = 32) -> int:
        pairs = list(items)
        if not pairs:
            self.ids_path.write_text("[]", encoding="utf-8")
            if np is not None:
                np.save(self.vectors_path, np.empty((0, 0), dtype=np.float32))
            return 0
        model = self._load_model()
        ids = [item[0] for item in pairs]
        texts = [item[1] for item in pairs]
        vectors = model.encode(texts, batch_size=batch_size, normalize_embeddings=True, show_progress_bar=True)
        np.save(self.vectors_path, np.asarray(vectors, dtype=np.float32))
        self.ids_path.write_text(json.dumps(ids), encoding="utf-8")
        return len(ids)

    def search(self, query: str, limit: int = 50) -> list[tuple[str, float]]:
        if np is None or not self.vectors_path.exists() or not self.ids_path.exists():
            return []
        vectors = np.load(self.vectors_path)
        ids = json.loads(self.ids_path.read_text(encoding="utf-8"))
        if len(ids) == 0:
            return []
        query_vector = self._load_model().encode([query], normalize_embeddings=True)[0]
        scores = vectors @ query_vector
        indices = np.argsort(-scores)[:limit]
        return [(ids[int(i)], float(scores[int(i)])) for i in indices]
