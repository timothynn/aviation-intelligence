from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True, slots=True)
class Node:
    node_id: str
    kind: str
    label: str
    metadata: dict[str, str]


@dataclass(frozen=True, slots=True)
class Edge:
    source: str
    relation: str
    target: str
    source_document: str | None = None
    confidence: float = 1.0


class KnowledgeGraph:
    """Small provider-neutral graph layer for regulatory relationships.

    It is deliberately in-memory so the same contract can later be backed by
    PostgreSQL, Neo4j, Cosmos DB or another graph-capable store.
    """

    def __init__(self) -> None:
        self.nodes: dict[str, Node] = {}
        self.edges: list[Edge] = []

    def add_node(self, node: Node) -> None:
        self.nodes[node.node_id] = node

    def add_edge(self, edge: Edge) -> None:
        if edge.source not in self.nodes or edge.target not in self.nodes:
            raise KeyError("Both source and target nodes must exist before an edge is added")
        self.edges.append(edge)

    def neighbors(self, node_id: str, relation: str | None = None) -> list[Node]:
        targets = [e.target for e in self.edges if e.source == node_id and (relation is None or e.relation == relation)]
        return [self.nodes[item] for item in targets if item in self.nodes]

    def incoming(self, node_id: str, relation: str | None = None) -> list[Node]:
        sources = [e.source for e in self.edges if e.target == node_id and (relation is None or e.relation == relation)]
        return [self.nodes[item] for item in sources if item in self.nodes]

    def path(self, source: str, target: str, max_hops: int = 4) -> list[list[str]]:
        results: list[list[str]] = []
        queue: list[list[str]] = [[source]]
        while queue:
            current = queue.pop(0)
            if len(current) - 1 > max_hops:
                continue
            if current[-1] == target:
                results.append(current)
                continue
            for node in self.neighbors(current[-1]):
                if node.node_id not in current:
                    queue.append(current + [node.node_id])
        return results

    def bulk_add(self, nodes: Iterable[Node], edges: Iterable[Edge]) -> None:
        for node in nodes:
            self.add_node(node)
        for edge in edges:
            self.add_edge(edge)
