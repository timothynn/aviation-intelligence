# Aviation Intelligence Architecture

Aviation Intelligence is a reusable platform architecture for aviation authorities, operators, airports, MROs, training organizations, ANSPs and industry-assurance use cases.

## Reference architecture

```text
                    Reference Applications / Portals
                               │
                               ▼
                         API / BFF Layer
                               │
        ┌──────────────────────┼────────────────────────┐
        ▼                      ▼                        ▼
   Domain Services       Workflow / Case          Inspection / Audit
        │                      │                        │
        ├──────────────┬───────┴────────┬───────────────┤
        ▼              ▼                ▼               ▼
 Regulation       Compliance       Evidence         Finance
 Intelligence     Engine           / Records        / Fees
        │              │                │               │
        └──────────────┴────────┬───────┴───────────────┘
                                ▼
                       Aviation Data Platform
                                │
             ┌──────────────────┼──────────────────┐
             ▼                  ▼                  ▼
        PostgreSQL         Search / Vector       Object Store
                              / Graph
                                │
                        Intelligence Gateway
                                │
              ┌─────────────────┼─────────────────┐
              ▼                 ▼                 ▼
             RAG                ML               Agents
              │                 │                 │
              └─────────────────┼─────────────────┘
                                ▼
                         Assurance / Governance
                                │
          Evidence • Evaluation • Security • Audit • Human Review
```

## Architectural planes

### 1. Domain plane

Stable aviation facts and lifecycles:
- organization
- authority
- aircraft
- aerodrome
- personnel
- application
- approval
- certificate
- inspection
- finding
- occurrence
- safety
- maintenance

### 2. Regulatory plane

```text
Source
 → Version
 → Instrument
 → Requirement
 → Applicability
 → Compliance
```

The regulatory plane is jurisdiction-aware and temporal.

### 3. Evidence plane

Provides document ingestion, controlled records, evidence links, provenance, retention, signatures, source hashes and audit history.

### 4. Workflow plane

Provides case orchestration, tasks, roles, SLAs, transitions, escalations, decisions and audit events.

### 5. Oversight plane

Provides generic inspection/audit/surveillance services and scheme adapters such as SAFA/SACA, USOAP-style State oversight, authority surveillance, IOSA and ISAGO.

### 6. Safety plane

Connects occurrences, findings, inspections, approvals, risk registers and safety performance into SSP/SMS intelligence.

### 7. Intelligence plane

RAG, extraction, classification, prediction, graph analytics and constrained agents.

### 8. Assurance plane

Every consequential AI capability should record:

```text
Input context
Source versions
Model / prompt / policy version
Output
Confidence / warnings
Evidence
Human reviewer
Decision
Timestamp
```

## Data architecture

Recommended reference stack:

- PostgreSQL: transactional system of record
- pgvector: semantic retrieval
- object storage: documents/evidence
- relational full-text / search engine: exact regulatory and identifier search
- optional graph store: relationship-heavy knowledge graph
- event bus: integration/audit/event-driven workflows
- Redis: caching / transient workloads

## Security architecture

```text
Identity
 ↓
Organization context
 ↓
Role / attribute authorization
 ↓
Record classification
 ↓
Policy enforcement
 ↓
Data access
 ↓
Audit event
```

AI tools must use the same authorization model as the underlying domain operations. An agent must not gain more authority than the user/policy allows.

## Design rules

1. Domain rules are deterministic where possible.
2. AI is probabilistic and must be isolated behind explicit interfaces.
3. Every regulatory answer is tied to source/version/applicability context.
4. Inspection schemes are adapters, not core-domain types.
5. Portal state is derived from backend authoritative records.
6. Safety data is classified and protected.
7. Consequential decisions require explicit human authorization.
8. Every reference implementation should be reproducible using synthetic/public data.
