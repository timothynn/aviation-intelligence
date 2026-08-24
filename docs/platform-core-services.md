# Aviation Platform Core Services

This package set is the shared foundation for regulated aviation applications. It deliberately separates domain facts, regulatory rules, evidence, workflow, inspection schemes and AI retrieval.

## Implemented in this branch

### Aviation domain

`packages/aviation-domain/`

Provides strongly typed core entities for:

- jurisdictions
- validity windows
- provenance
- organizations
- aircraft
- certificates
- approvals
- entity relationships

These entities are intended to be stable shared contracts across AOC, surveillance, airworthiness, SAFA and other aviation applications.

### Regulatory domain

`packages/regulatory-domain/`

Provides:

- regulatory source types
- version/effective-date modeling
- jurisdiction and authority context
- applicability-aware rule resolution
- authority precedence
- scope matching

The resolver is intentionally advisory. A final legal/regulatory interpretation must remain subject to the competent authority and source hierarchy.

### Workflow domain

`packages/workflow-domain/`

Provides a regulated case state engine with explicit transitions such as:

```text
Draft → Open → InReview
                  ├── Returned → InReview
                  ├── Accepted → Closed
                  └── Rejected
```

Transitions that change a regulatory outcome can require comments, making the audit trail requirement explicit in the domain contract.

### Evidence domain

`packages/evidence-domain/`

Provides a common evidence object for documents, photographs, scans, observations, signatures and technical records. Sensitive evidence is modeled separately so retrieval and UI layers can enforce permission checks before exposure.

### Compliance domain

`packages/compliance-domain/`

Provides requirements, assessments and a reference evaluator. The default evaluator intentionally returns `RequiresReview` when evidence is present rather than pretending evidence presence alone proves compliance.

### Inspection domain

`packages/inspection-domain/`

Includes the generic inspection contracts plus a concrete SAFA scheme adapter for finding category/action relationships. The scheme adapter is decision support only and does not autonomously ground, ban or clear aircraft.

## CI strategy

Python document intelligence and .NET domain packages are tested independently.

Python CI validates:

- package installation
- dependency consistency (`pip check`)
- imports
- bytecode compilation
- unit tests

.NET CI validates:

- restore
- release build
- all shared domain projects

Keeping these checks separate makes it easier to identify whether a failure belongs to the document-intelligence runtime or to the aviation domain layer.

## Next production steps

The next layer should connect these shared contracts to persistent application services:

1. EF Core/PostgreSQL repositories for aviation domain entities, workflow cases and evidence.
2. A real regulatory applicability/rules engine populated from authoritative source mappings.
3. Temporal amendment and supersession resolution backed by the regulatory knowledge graph.
4. Queue-based document ingestion and source-monitoring workers.
5. Managed lexical/vector retrieval with tenant-aware permissions.
6. AI copilot APIs that accept an evidence pack and return citations plus explicit confidence/abstention state.
