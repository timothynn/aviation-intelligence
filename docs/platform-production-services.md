# Aviation Platform Production Services

This layer sits above the shared domain packages and below application/AI experiences. It turns domain contracts into replaceable service boundaries.

## Regulatory resolution

`RegulatoryResolutionService` evaluates rule candidates using the existing domain resolver with jurisdiction, authority, effective date, operation type and aircraft context. Multiple applicable authorities are surfaced as `RequiresHumanReview` rather than silently choosing a legal interpretation.

## Search and grounded retrieval

`SearchProviderContracts` defines lexical, vector and hybrid providers. `GroundedRetrievalService` filters results through access control and an evidence score threshold; when no authorised evidence clears the threshold it abstains.

## Document processing

`DocumentProcessingOrchestrator` models a queue/worker pipeline:

```text
Discovered → Downloaded → Normalized → Parsed → Chunked → Indexed → GraphUpdated → Complete
```

Failures are explicit and include an attempt count and error message. A production queue such as Azure Service Bus, RabbitMQ, Kafka or SQS can implement `IDocumentProcessingQueue`.

## Regulatory change impact

`ChangeImpactService` maps a changed source to dependent knowledge artifacts. Those artifacts are marked for review rather than being silently invalidated.

## Service health

`ServiceHealth` provides a common health/readiness contract for composing APIs and workers behind Kubernetes, containers or cloud monitoring.

## Production provider examples

The contracts are intentionally provider-neutral and can be wired to:

- PostgreSQL / pgvector for relational persistence and vector storage
- Azure AI Search, OpenSearch or Elasticsearch for managed hybrid retrieval
- S3 or Azure Blob Storage for document objects
- Redis for queues/caching where appropriate
- Azure Service Bus, RabbitMQ, Kafka or SQS for distributed document jobs
- Neo4j or PostgreSQL graph structures for knowledge relationships
- enterprise LLM gateways for grounded generation

These components do not make regulatory decisions. They expose evidence and deterministic service results to human-authorised aviation workflows.