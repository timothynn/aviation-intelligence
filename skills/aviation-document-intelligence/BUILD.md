# Build checklist

This skill is intentionally split into layers so a team can replace components independently.

## P0

- source registry
- acquisition/provenance
- canonical metadata
- parser/OCR adapter
- structure-aware chunker
- lexical index
- vector index
- hybrid retrieval
- reranking
- evidence pack
- citation/audit contract

## P1

- relationship graph
- temporal retrieval
- jurisdiction/applicability resolver
- contradiction detector
- evaluation runner
- source freshness monitor

## P2

- computer vision document/aircraft evidence
- table reasoning
- technical-document relation extraction
- operator/aircraft safety intelligence

SAFA, AOC and other regulatory capabilities should consume P0/P1 rather than rebuilding document search independently.
