# Architecture

Aviation Intelligence is organized as a set of reusable aviation-domain and AI capabilities rather than a single application.

## Reference architecture

```text
Clients / Reference Apps
          │
          ▼
   ASP.NET Core APIs
          │
    ┌─────┼──────────┐
    ▼     ▼          ▼
 Domain  Workflow   AI Gateway
    │       │          │
    │       │    ┌─────┼─────┐
    │       │    ▼     ▼     ▼
    │       │   RAG   ML   Agents
    │       │    │     │     │
    └───────┴────┼─────┴─────┘
                 ▼
       PostgreSQL / pgvector
                 │
                 ▼
       Evidence + Audit Trail
                 │
                 ▼
          Human Review
```

## Architectural boundaries

### Aviation domain
Contains stable domain concepts such as aircraft, operators, airports, flights, approvals, inspections, findings, certificates and occurrences.

### Intelligence layer
Contains retrieval, extraction, classification, prediction, agents and other AI capabilities.

### Assurance layer
Provides evaluation, evidence tracking, confidence, auditability, guardrails and human review.

### Reference applications
Demonstrate how the reusable packages can be assembled into real aviation workflows.

## Design goals

- Provider-neutral AI integrations where practical.
- Clear separation between domain rules and probabilistic AI.
- Evidence and source provenance for knowledge-based answers.
- Human approval for consequential aviation decisions.
- Testable components with deterministic domain logic around AI.
- Synthetic/public data for reproducible examples.
