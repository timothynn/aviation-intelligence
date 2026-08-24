from __future__ import annotations

import json
from dataclasses import asdict
from typing import Iterable

from .graph import Edge, Node

SCHEMA = """
CREATE TABLE IF NOT EXISTS graph_nodes (
    node_id TEXT PRIMARY KEY,
    kind TEXT NOT NULL,
    label TEXT NOT NULL,
    metadata JSONB NOT NULL DEFAULT '{}'::jsonb
);
CREATE TABLE IF NOT EXISTS graph_edges (
    source TEXT NOT NULL REFERENCES graph_nodes(node_id) ON DELETE CASCADE,
    relation TEXT NOT NULL,
    target TEXT NOT NULL REFERENCES graph_nodes(node_id) ON DELETE CASCADE,
    source_document TEXT,
    confidence DOUBLE PRECISION NOT NULL DEFAULT 1.0,
    PRIMARY KEY (source, relation, target)
);
CREATE INDEX IF NOT EXISTS idx_graph_edges_source ON graph_edges(source);
CREATE INDEX IF NOT EXISTS idx_graph_edges_target ON graph_edges(target);
CREATE INDEX IF NOT EXISTS idx_graph_edges_relation ON graph_edges(relation);
"""


class PostgresKnowledgeGraph:
    def __init__(self, dsn: str):
        try:
            import psycopg
        except ImportError as exc:  # pragma: no cover
            raise RuntimeError("Install the postgres extra: pip install psycopg[binary]") from exc
        self.conn = psycopg.connect(dsn)
        self.conn.execute(SCHEMA)
        self.conn.commit()

    def close(self) -> None:
        self.conn.close()

    def add_nodes(self, nodes: Iterable[Node]) -> None:
        for node in nodes:
            self.conn.execute(
                """INSERT INTO graph_nodes(node_id,kind,label,metadata) VALUES(%s,%s,%s,%s)
                ON CONFLICT(node_id) DO UPDATE SET kind=EXCLUDED.kind,label=EXCLUDED.label,metadata=EXCLUDED.metadata""",
                (node.node_id, node.kind, node.label, json.dumps(node.metadata)),
            )
        self.conn.commit()

    def add_edges(self, edges: Iterable[Edge]) -> None:
        for edge in edges:
            self.conn.execute(
                """INSERT INTO graph_edges(source,relation,target,source_document,confidence)
                VALUES(%s,%s,%s,%s,%s)
                ON CONFLICT(source,relation,target) DO UPDATE SET source_document=EXCLUDED.source_document,confidence=EXCLUDED.confidence""",
                (edge.source, edge.relation, edge.target, edge.source_document, edge.confidence),
            )
        self.conn.commit()

    def neighbors(self, node_id: str, relation: str | None = None) -> list[Node]:
        params = [node_id]
        clause = "source=%s"
        if relation:
            clause += " AND relation=%s"
            params.append(relation)
        rows = self.conn.execute(
            f"SELECT n.node_id,n.kind,n.label,n.metadata FROM graph_edges e JOIN graph_nodes n ON n.node_id=e.target WHERE {clause}",
            params,
        ).fetchall()
        return [Node(row[0], row[1], row[2], row[3]) for row in rows]

    def incoming(self, node_id: str, relation: str | None = None) -> list[Node]:
        params = [node_id]
        clause = "target=%s"
        if relation:
            clause += " AND relation=%s"
            params.append(relation)
        rows = self.conn.execute(
            f"SELECT n.node_id,n.kind,n.label,n.metadata FROM graph_edges e JOIN graph_nodes n ON n.node_id=e.source WHERE {clause}",
            params,
        ).fetchall()
        return [Node(row[0], row[1], row[2], row[3]) for row in rows]
