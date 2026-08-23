from __future__ import annotations

import argparse
from pathlib import Path

from fastapi import FastAPI, Query

from .retrieval import Retriever
from .store import Store
from .vector import EmbeddingIndex


def create_app(db_path: str = "data/docint.sqlite") -> FastAPI:
    store = Store(db_path)
    vectors = EmbeddingIndex(Path(db_path).with_suffix("") / "vectors")
    retriever = Retriever(store, vectors)
    app = FastAPI(title="Aviation Document Intelligence", version="0.2.0")

    @app.get("/health")
    def health():
        return {"status": "ok", "stats": store.stats()}

    @app.get("/search")
    def search(
        q: str,
        limit: int = Query(8, ge=1, le=50),
        authority: str | None = None,
        jurisdiction: str | None = None,
        status: str | None = None,
        document_type: str | None = None,
    ):
        filters = {k: v for k, v in {
            "authority": authority,
            "jurisdiction": jurisdiction,
            "status": status,
            "document_type": document_type,
        }.items() if v}
        pack = retriever.search(q, limit, filters=filters)
        return {
            "query": pack.query,
            "retrievalMethod": pack.retrieval_method,
            "abstain": pack.abstain,
            "abstainReason": pack.abstain_reason,
            "results": [
                {
                    "documentId": e.document_id,
                    "title": e.title,
                    "authority": e.authority,
                    "jurisdiction": e.jurisdiction,
                    "status": e.status,
                    "version": e.version,
                    "section": e.section,
                    "paragraph": e.paragraph,
                    "pageStart": e.page_start,
                    "pageEnd": e.page_end,
                    "chunkId": e.chunk_id,
                    "sourceUrl": e.source_url,
                    "score": e.score,
                    "text": e.text,
                }
                for e in pack.evidences
            ],
        }

    return app


app = create_app()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", default="data/docint.sqlite")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8090)
    args = parser.parse_args()
    import uvicorn
    uvicorn.run(create_app(args.db), host=args.host, port=args.port)
