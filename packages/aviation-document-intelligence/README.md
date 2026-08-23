# Aviation Document Intelligence Engine

A provider-neutral reference engine for ingesting, indexing, and retrieving aviation regulatory and technical documents.

## Implemented layers

1. Acquisition/provenance: source manifests, download metadata, SHA-256.
2. Parsing: PDF, XML, HTML/text inputs with a common document model.
3. Structure-aware chunking: headings, paragraph identifiers, page/source locations.
4. Lexical retrieval: SQLite FTS5 for fast exact/keyword search.
5. Vector retrieval: optional local embeddings through `sentence-transformers`.
6. Hybrid fusion: reciprocal-rank fusion of lexical and vector candidates.
7. Metadata filtering: authority, jurisdiction, status, document type, effective date.
8. Evidence packs: source/version/location metadata for grounded answers.
9. HTTP API: ingest, search, health and document inspection.

## Quick start

```bash
cd packages/aviation-document-intelligence
python -m venv .venv
. .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m aviation_docint.cli init --db data/docint.sqlite
python -m aviation_docint.cli ingest --input ../../data/corpus --db data/docint.sqlite
python -m aviation_docint.cli search "SAFA ramp inspection" --db data/docint.sqlite
python -m aviation_docint.api --db data/docint.sqlite
```

Vector search is optional. Install the `vector` extra when local embeddings are required:

```bash
pip install -r requirements-vector.txt
```

The engine remains useful with lexical-only retrieval and is designed so a managed vector store or reranker can be added later without changing the domain model.

## Architecture

```text
Source files
   ↓
Parser adapters
   ↓
Document + page/section model
   ↓
Structure-aware chunker
   ↓
SQLite metadata + FTS5
   │
   └──── optional embeddings
             ↓
        Vector store
             ↓
      Hybrid RRF fusion
             ↓
       Evidence pack
```

## Regulatory safety boundary

This engine retrieves and ranks evidence. It does not determine compliance, airworthiness, enforcement action, aircraft grounding, finding closure, or any other regulatory decision.
