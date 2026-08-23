# Aviation Document Intelligence

A reusable document intelligence capability for aviation regulatory, operational, airworthiness, safety and technical knowledge bases.

## Objective

Turn large aviation document collections into a searchable, version-aware, evidence-first knowledge layer without treating the LLM as the search engine or regulatory authority.

## Core pipeline

```text
Official source
    ↓
Acquisition + provenance
    ↓
Document classification
    ↓
Text / structure / table / OCR extraction
    ↓
Metadata + entities + citations
    ↓
Structure-aware chunking
    ↓
Lexical index + vector index + knowledge graph
    ↓
Metadata filtering
    ↓
Hybrid retrieval
    ↓
Reranking
    ↓
Regulatory applicability / authority policy
    ↓
Evidence pack
    ↓
Grounded LLM response
    ↓
Citations + audit event
```

## Design principles

1. **Source first.** Official authority material should outrank secondary material.
2. **Version first.** Current, historical, draft and superseded material are separate states.
3. **Structure first.** Preserve document hierarchy, paragraph identifiers, tables, pages and references.
4. **Hybrid retrieval.** Combine lexical search for exact aviation identifiers with semantic/vector retrieval for conceptual queries.
5. **Rerank before generation.** The LLM should receive a small, high-quality evidence pack rather than an entire document set.
6. **Evidence first.** Every material claim should be traceable to source document, version and location.
7. **Fail closed.** Insufficient or conflicting evidence should produce an abstention/review state, not a guessed answer.
8. **Scheme-neutral.** SAFA, AOC, airworthiness, personnel licensing and other domains should consume the same platform capability.

## Recommended stack contract

The skill is implementation-neutral, but should expose adapters for:

- object storage / file stores
- PDF, XML, HTML and OCR parsers
- lexical search (BM25 or equivalent)
- vector database / vector-capable search engine
- semantic reranker
- graph store or graph-compatible relational model
- LLM gateway
- audit/provenance service

Azure AI Search is a strong implementation option in a Microsoft/.NET environment because it supports hybrid text/vector retrieval, reciprocal-rank fusion and semantic ranking, but the skill does not depend on Azure.

## Required document states

```text
CURRENT
HISTORICAL
DRAFT
SUPERSEDED
WITHDRAWN
UNKNOWN
```

The state must never be inferred from the model alone; it should come from source metadata and/or an authority verification policy.

## Required evidence object

```json
{
  "documentId": "easa-ear-tco-2026-07",
  "version": "2026-07",
  "authority": "EASA",
  "jurisdiction": "EU/EEA",
  "status": "CURRENT",
  "section": "Part-TCO",
  "paragraph": "TCO.GEN.100",
  "page": 42,
  "chunkId": "...",
  "sourceUrl": "https://...",
  "retrievalMethod": "hybrid",
  "score": 0.93
}
```

## Query modes

Support explicit query modes where useful:

- `exact` — regulation/document/item identifier lookup
- `semantic` — conceptual question
- `hybrid` — default
- `temporal` — query against a historical effective date
- `jurisdictional` — authority/state constrained search
- `technical` — manufacturer/aircraft/system-focused retrieval
- `cross_document` — compare or synthesize multiple authorities

## Aviation-aware entity extraction

Extract and normalize entities such as:

- authority / CAA
- jurisdiction / State
- regulation and legal instrument
- Annex / Part / Chapter / paragraph
- aircraft type / variant
- aircraft registration
- operator
- AOC / certificate identifier
- inspection item / finding code
- ATA chapter / system
- AMM / SRM / CMM / MEL / CDL reference
- revision / issue / amendment
- effective / applicability date

## Safety boundary

This skill is a knowledge and retrieval capability. It must not independently:

- determine aircraft airworthiness
- impose an operational restriction
- ground or ban an aircraft
- make a final regulatory finding
- close a corrective action
- override an authoritative rule engine

Those actions remain in the consuming workflow and are subject to human authorization.

## Evaluation

At minimum measure:

- retrieval Recall@5 and Recall@10
- NDCG / MRR
- citation accuracy
- source-version accuracy
- jurisdiction accuracy
- unsupported-answer rate
- abstention accuracy
- latency p50/p95
- indexing throughput
- cost per query
- human override rate
