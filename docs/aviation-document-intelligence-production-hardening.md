# Aviation Document Intelligence — Production Hardening

This document tracks the remaining work required to move the reference engine toward a production-grade aviation regulatory intelligence platform.

## Implemented reference capabilities

- Source acquisition and SHA-256 provenance
- PDF/XML/HTML/text ingestion contracts
- Structure-aware chunks and evidence objects
- SQLite FTS5 lexical retrieval
- Optional local sentence-transformer vectors
- Hybrid fusion and aviation-aware reranking
- Temporal version resolution
- Basic applicability scoring
- Provider-neutral knowledge graph contract
- Regulatory change fingerprinting
- Document-level access policy contract
- Grounded LLM prompt/provider contract
- Evaluation regression tests

## Production workstreams

### Search infrastructure

Move the local store to a production search platform with:

- BM25/inverted index
- vector index
- semantic/cross-encoder reranking
- filter pushdown
- aliases and zero-downtime index rebuilds
- shard/replica strategy
- query telemetry

### Ingestion at scale

Add:

- distributed workers
- OCR fallback for scanned documents
- table and figure extraction
- document deduplication
- incremental ingestion based on checksum/ETag
- retry/dead-letter handling
- source-page crawling
- page-level extraction validation

### Regulatory temporal engine

Resolve a query against an effective date using:

1. authority status
2. effective-from/effective-to dates
3. amendment/supersession relationships
4. jurisdiction
5. applicability
6. source precedence

An ambiguous result must remain ambiguous until resolved by policy or human review.

### Applicability engine

Model at minimum:

- State/jurisdiction
- authority
- operator type
- aircraft type/variant
- operation
- approval/certificate type
- route/airspace where relevant
- effective date
- special conditions/exemptions

### Knowledge graph

Recommended relationships include:

```text
Authority -> publishes -> Instrument
Instrument -> amends -> Instrument
Instrument -> supersedes -> Instrument
Annex -> implemented_by -> National Regulation
Regulation -> supported_by -> AMC/GM
Requirement -> evidenced_by -> Document/Record
Inspection Item -> produces -> Finding
Finding -> requires -> Corrective Action
Aircraft Type -> governed_by -> Technical Standard
```

### Change intelligence

Build periodic authority crawlers that:

- detect new revisions
- compare normalized text
- identify changed paragraphs
- re-index affected chunks
- mark superseded versions
- emit downstream impact events

### Security

Apply document policies before retrieval results reach the LLM. Do not rely on prompt instructions to enforce authorization.

### LLM gateway

The LLM layer should provide:

- provider abstraction
- structured output
- model/version records
- timeout/retry policy
- token/cost telemetry
- prompt versioning
- safety filters
- audit events

The LLM must consume an evidence pack rather than searching the corpus itself.

### Evaluation

Track:

- Recall@5/10
- MRR/NDCG
- authority accuracy
- jurisdiction accuracy
- temporal accuracy
- applicability accuracy
- citation precision/recall
- unsupported-claim rate
- abstention precision
- p50/p95 latency
- indexing throughput
- cost per query

## Regulatory safety boundary

The platform is decision support. It must not independently:

- determine airworthiness
- ground/ban aircraft
- impose operational restrictions
- issue final regulatory findings
- accept corrective actions
- close findings

Those decisions belong to the consuming regulated workflow and authorized personnel.
