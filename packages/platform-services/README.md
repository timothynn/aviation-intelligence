# Aviation Platform Services

Production-oriented service boundaries layered on top of the domain packages.

## Services

- `RegulatoryResolutionService` — resolves candidate rules by authority, jurisdiction, effective date and operation scope.
- `SearchProviderContracts` — provider-neutral lexical/vector/hybrid search interfaces.
- `GroundedRetrievalService` — builds evidence packs from search results and enforces an explicit abstention threshold.
- `DocumentProcessingOrchestrator` — queue/worker boundary for document ingestion and re-indexing.
- `ChangeImpactService` — maps changed regulatory sources to affected downstream knowledge artifacts.
- `ServiceHealth` — common health/readiness contract for service composition.

These are deliberately provider-neutral. PostgreSQL, Azure AI Search, OpenSearch, Redis, object storage and LLM providers can be wired behind the interfaces without changing the domain layer.

Regulatory outcomes remain human-authorised.