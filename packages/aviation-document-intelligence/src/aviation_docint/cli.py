from __future__ import annotations

import argparse
import json
from pathlib import Path

from .ingest import ingest_path
from .retrieval import Retriever
from .store import Store
from .vector import EmbeddingIndex


def main() -> None:
    parser = argparse.ArgumentParser(prog="avdoc")
    sub = parser.add_subparsers(dest="command", required=True)

    init = sub.add_parser("init")
    init.add_argument("--db", default="data/docint.sqlite")

    ingest = sub.add_parser("ingest")
    ingest.add_argument("--input", required=True)
    ingest.add_argument("--db", default="data/docint.sqlite")

    search = sub.add_parser("search")
    search.add_argument("query")
    search.add_argument("--db", default="data/docint.sqlite")
    search.add_argument("--limit", type=int, default=8)
    search.add_argument("--authority")
    search.add_argument("--jurisdiction")
    search.add_argument("--status")
    search.add_argument("--document-type")

    stats = sub.add_parser("stats")
    stats.add_argument("--db", default="data/docint.sqlite")

    args = parser.parse_args()
    store = Store(args.db)
    try:
        if args.command == "init":
            print(json.dumps(store.stats(), indent=2))
        elif args.command == "ingest":
            result = ingest_path(Path(args.input), store)
            print(json.dumps(result, indent=2))
        elif args.command == "stats":
            print(json.dumps(store.stats(), indent=2))
        elif args.command == "search":
            filters = {k: v for k, v in {
                "authority": args.authority,
                "jurisdiction": args.jurisdiction,
                "status": args.status,
                "document_type": args.document_type,
            }.items() if v}
            vector_root = Path(args.db).with_suffix("")
            retriever = Retriever(store, EmbeddingIndex(vector_root / "vectors"))
            pack = retriever.search(args.query, args.limit, filters=filters, use_vector=False)
            print(json.dumps({
                "query": pack.query,
                "abstain": pack.abstain,
                "reason": pack.abstain_reason,
                "results": [e.__dict__ for e in pack.evidences],
            }, indent=2, ensure_ascii=False))
    finally:
        store.close()
