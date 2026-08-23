# Regulatory document versioning

Aviation retrieval must distinguish document identity from document state.

```text
Document family
  ↓
Revision / issue / amendment
  ↓
Publication date
  ↓
Effective / applicability period
  ↓
Status
```

For current-answer queries, use the authority's current publication state and verify whether a newer adopted rule has superseded the consolidation.

For historical queries, resolve the effective date instead of using the newest file on disk.

Never silently merge text from two revisions into one answer.
