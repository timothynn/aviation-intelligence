# Evaluation Framework

## Retrieval

Measure against expert-labeled source chunks:

- Recall@1, @5, @10
- Precision@5, @10
- MRR
- NDCG

## Grounding

Measure:

- citation correctness
- citation completeness
- source-version correctness
- jurisdiction correctness
- paragraph/page accuracy
- unsupported claim rate
- contradiction handling
- abstention accuracy

## Performance

Measure:

- ingestion throughput
- average parse time/document
- embedding throughput
- indexing throughput
- query p50/p95/p99 latency
- reranking latency
- end-to-end answer latency
- cost/query
- cache hit ratio

## Golden set

Start with the cases in:

`examples/document-intelligence-evaluation.yaml`

Expand the set with expert-created examples for each:

```text
exact identifiers
semantic paraphrase
cross-document comparison
version conflict
historical query
jurisdiction conflict
technical reference lookup
applicability
missing evidence
abstention
```

## Regression policy

A new parser, embedding model, reranker or search configuration must not be promoted without comparing against the existing golden set.

Track results by:

```text
pipeline version
parser version
embedding model
reranker model
retrieval configuration
source corpus snapshot
```
