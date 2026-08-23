# Aviation Document Intelligence Guide

## What this solves

A 6 GB aviation corpus should not be passed directly to an LLM. The platform should parse once, enrich once, index once, and retrieve a small evidence pack per query.

## Reference architecture

```text
Official documents
       ↓
Acquisition / provenance
       ↓
Canonical document model
       ↓
Parser / OCR / table extraction
       ↓
Metadata + entity extraction
       ↓
Structure-aware chunks
       ↓
┌─────────────┬─────────────┬──────────────┐
│ BM25 index  │ Vector index│ Relationship │
│ exact terms │ semantics   │ graph        │
└──────┬──────┴──────┬──────┴──────┬───────┘
       └─────────────┼──────────────┘
                     ↓
              Hybrid retrieval
                     ↓
                RRF fusion
                     ↓
             Semantic reranker
                     ↓
       Authority/version/applicability
                     ↓
                Evidence pack
                     ↓
                     LLM
                     ↓
          Cited grounded response
```

## Why hybrid search matters

Aviation queries contain both exact identifiers and natural-language concepts.

Exact:

- `A23`
- `TCO.GEN.100`
- `ICAO Annex 6`
- `AMM 32-10`
- `ATA 32`

Semantic:

- "What should an inspector do when an apparent technical defect is found during turnaround?"
- "How do previous findings affect inspection prioritisation?"

BM25/lexical retrieval handles exact identifiers well; embeddings handle paraphrase; reranking improves the final candidate order.

## Why metadata matters

Use filters before expensive semantic retrieval where possible:

```text
authority
jurisdiction
programme
operator
aircraft type
status
version
publication date
effective date
document type
inspection item
ATA chapter
```

## Version safety

Do not assume the newest document on disk is the current rule.

The ingestion pipeline records:

```text
authority
version
issue
amendment
published_at
effective_from
effective_to
status
supersedes
superseded_by
source_url
retrieved_at
sha256
```

Queries should support both:

- current requirement
- requirement effective at a historical date

## Source hierarchy

A regulatory answer should prefer, subject to jurisdiction and applicability:

1. Current legal/regulatory source
2. Current authority AMC/GM / procedural material
3. Current ICAO or national standard where applicable
4. Current approved technical source
5. Historical authority source
6. Secondary explanation

The system must expose when the answer relies on historical material.

## RAG answer contract

Every answer should return:

```text
answer
confidence / uncertainty
source authority
source title
source version
source status
section / paragraph
page where available
source URL
retrieval trace ID
```

## Large-corpus performance strategy

For a corpus around 6 GB:

- extract and normalize once
- precompute embeddings once
- precompute entities once
- store parsed pages/chunks
- use metadata prefilters
- run lexical and vector retrieval in parallel
- rerank only a small candidate set
- cache hot queries and evidence packs
- incrementally reindex changed sources
- separate raw storage from Git

## Corpus strategy

The repository keeps a manifest of official source pages and URLs. The binary corpus is generated locally or as a GitHub Actions artifact so the public repository is not turned into a multi-gigabyte document mirror.

Run:

```bash
python -m pip install requests beautifulsoup4 pyyaml
python skills/aviation-document-intelligence/scripts/download_corpus.py
```

The workflow `.github/workflows/build-document-corpus.yml` can build the same corpus as a CI artifact.

## SAFA integration

SAFA uses this capability for:

```text
Pre-inspection brief
      ↓
Historical finding retrieval
      ↓
Regulatory / RIM retrieval
      ↓
Checklist prioritisation support
      ↓
Finding assistance
      ↓
Evidence indexing
      ↓
Corrective-action analysis
      ↓
Recurrence intelligence
```

The SAFA workflow remains the authority for inspection state, finding categorisation, operational action and closure.

## Security and privacy

The document layer should support:

- source-level access control
- document retention policy
- sensitive-attachment tagging
- immutable provenance
- audit logs
- tenant/jurisdiction isolation
- encryption at rest and in transit
- prompt/context redaction where required

## Production recommendation

Treat the repository as the **code and source registry**. Treat object storage/search infrastructure as the **document corpus and index**. This makes updates, rollback, reproducibility and source-license controls manageable.
