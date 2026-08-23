# Aviation Document Intelligence Architecture

## 1. Ingestion

```text
Source Registry
   ↓
Fetch / Snapshot
   ↓
SHA-256 + MIME + byte size
   ↓
Duplicate detection
   ↓
Document classifier
```

Prefer official publisher URLs. Keep `source_url`, `retrieved_at`, `publisher`, `license_policy`, `checksum` and `version_metadata` with every artifact.

## 2. Parsing

The parser should detect:

- native PDF text
- scanned/image-only PDF
- PDF tables
- XML / structured regulatory source
- HTML/online publications
- attachments and referenced documents

OCR is a fallback, not the default.

For PDFs preserve:

```text
page number
heading hierarchy
paragraph identifier
list numbering
table boundaries
footnotes
cross-references
source bookmarks
```

## 3. Canonical document model

```text
Document
 ├── Identity
 ├── Authority
 ├── Jurisdiction
 ├── Publication metadata
 ├── Version / issue / amendment
 ├── Effective/applicability dates
 ├── Status
 ├── Source URLs
 ├── License / redistribution policy
 ├── Sections
 │    └── Paragraphs
 │         └── Chunks
 ├── Entities
 └── References
```

## 4. Chunking

Do not split every document into arbitrary fixed token sizes.

Use a parent/child structure:

```text
Document
  ↓
Part / Chapter
  ↓
Section
  ↓
Paragraph
  ↓
Retrieval chunk
```

A retrieval chunk should normally carry its parent heading, identifiers and enough preceding context to be meaningful by itself.

For tables, preserve row/column relationships and create a text representation that can be searched without losing the original table attachment.

## 5. Indexing

Maintain at least three complementary representations:

### Lexical index

BM25/inverted index for exact tokens and identifiers:

`A23`, `TCO.GEN.100`, `ICAO Annex 6`, `AMM 32-10`, `ATA 32`, `CS-25`.

### Vector index

Embeddings for conceptual similarity and paraphrases.

### Relationship index

Graph or graph-compatible tables for relationships such as:

```text
EASA → publishes → EAR TCO
EAR TCO → contains → Part-TCO
Part-TCO → references → Regulation (EU) 452/2014
Finding → maps to → SAFA inspection item
Aircraft system → maps to → ATA chapter
```

## 6. Query processing

```text
User query
  ↓
Query normalization
  ↓
Entity / identifier extraction
  ↓
Intent classification
  ↓
Metadata filters
  ↓
Lexical + vector retrieval
  ↓
RRF / rank fusion
  ↓
Semantic reranker
  ↓
Authority/version/applicability ranking
  ↓
Evidence pack
```

### Regulatory-aware ranking

A practical scoring model should consider:

```text
lexical relevance
semantic relevance
authority relevance
jurisdiction match
status/currentness
version/effective-date fit
applicability fit
section/paragraph match
entity match
```

Weights must be benchmarked against an expert-labeled evaluation set.

## 7. Version resolution

When the query asks for the current requirement:

```text
candidate sources
   ↓
remove withdrawn/superseded where policy says so
   ↓
select jurisdiction
   ↓
select latest applicable effective version
   ↓
retrieve evidence
```

When the user asks for a historical date, perform temporal retrieval against that effective period instead.

## 8. Contradiction handling

If two sources conflict:

```text
Conflict detected
     ↓
source authority ranking
     ↓
version / effective date comparison
     ↓
jurisdiction comparison
     ↓
applicability comparison
     ↓
show both sources if unresolved
```

Never silently merge conflicting regulatory text.

## 9. Evidence pack

The LLM receives a compact evidence package rather than raw search results.

```json
{
  "query": "...",
  "answerable": true,
  "sources": [
    {
      "documentId": "...",
      "title": "...",
      "version": "...",
      "status": "CURRENT",
      "authority": "EASA",
      "section": "Part-TCO",
      "paragraph": "...",
      "page": 42,
      "text": "...",
      "sourceUrl": "...",
      "score": 0.94
    }
  ]
}
```

## 10. Abstention

Use an explicit review state where:

- evidence is missing
- source status is unknown
- only historical sources support the answer
- conflicting current sources exist
- the query is outside corpus coverage
- the retrieved context is insufficient

Recommended result contract:

```text
ANSWERED
ANSWERED_WITH_CAUTION
CONFLICT_REQUIRES_REVIEW
INSUFFICIENT_EVIDENCE
OUT_OF_SCOPE
```

## 11. Performance targets

Targets should be established empirically, but the initial engineering objectives should be:

- metadata prefilter before expensive semantic retrieval
- top-N lexical/vector retrieval in parallel
- rerank only a small candidate set
- cache normalized queries and hot evidence packs
- precompute embeddings/entities at ingestion
- store OCR/parse results so documents are never reparsed per query
- support incremental indexing when a source revision changes

## 12. Storage recommendation for ~6 GB

Do not make the Git repository the primary binary corpus.

Recommended split:

```text
GitHub
 ├── manifest
 ├── ingestion code
 ├── schemas
 ├── evaluation set
 └── source policies

Object storage / artifact store
 └── raw documents + parsed intermediates

Search platform
 ├── lexical index
 ├── vector index
 └── metadata / relationship index
```

For repeatable CI tests, use downloadable official sources and publish a generated corpus artifact rather than committing gigabytes of PDFs into Git.
