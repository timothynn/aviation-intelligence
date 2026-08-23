# Implementation Blueprint

This roadmap is ordered by dependency. The repository should build deterministic regulated-system foundations before probabilistic AI features.

## Phase 0 — Contracts and governance

1. Domain identifiers and common enums
2. Jurisdiction / authority / applicability model
3. Provenance and temporal validity
4. Security classifications and data-retention metadata
5. Versioning policy for rules, skills, schemas, models and datasets

## Phase 1 — Core aviation domain

Implement strongly typed contracts for:

```text
Authority / Jurisdiction
Organization / Operator
Aircraft / AircraftType / Engine / Component
Aerodrome / Runway / Facility
Personnel / Licence / Training
Certificate / Approval / Authorization
Application / Case / Document / Evidence
Regulation / Requirement / Guidance
Inspection / Audit / Finding / CorrectiveAction
Occurrence / Hazard / Risk / SafetyIndicator
MaintenanceEvent / AD / SB
Fee / Invoice / Payment
```

Acceptance criteria:
- stable identifiers
- lifecycle states
- relationship integrity
- serialization contracts
- temporal validity
- provenance
- audit events

## Phase 2 — Regulatory intelligence

Build a source-agnostic regulatory ingestion layer supporting PDF, HTML and machine-readable sources such as EASA XML.

Pipeline:

```text
Source monitor
 → acquisition
 → fingerprint
 → parser
 → structural hierarchy
 → legal metadata
 → requirement extraction
 → applicability
 → version graph
 → indexed knowledge
```

Implement:
- regulation hierarchy
- requirement objects
- effective/applicability dates
- amendment/supersession chain
- guidance relationships
- source evidence
- jurisdiction resolution
- change detection

## Phase 3 — Document / evidence engine

Support:
- PDF/DOCX/image/XML
- OCR and layout extraction
- classification
- field extraction
- evidence linking
- signatures
- controlled copies
- retention/disposition
- field-level provenance
- hash/checksum
- source citation

Every extracted fact should be distinguishable from an AI-derived interpretation.

## Phase 4 — Compliance engine

Model:

```text
Requirement
 → Applicability
 → Evidence
 → Assessment
 → Status
 → Reviewer Decision
 → Audit trail
```

Statuses:

```text
COMPLIANT
PARTIALLY_COMPLIANT
NON_COMPLIANT
NOT_APPLICABLE
INSUFFICIENT_EVIDENCE
PENDING_REVIEW
```

## Phase 5 — Workflow / case engine

Implement:
- workflow definitions and versions
- cases
- stages
- tasks
- assignments
- transitions
- guards/policies
- parallel branches
- SLAs
- escalations
- delegated authority
- notifications
- immutable audit events

AI can recommend; deterministic authorization/policy controls the transition.

## Phase 6 — Generic inspection and audit engine

Implement common primitives:

```text
Programme
Scheme
InspectionPlan
TargetSelection
Inspector
Qualification
Team
Checklist
ChecklistVersion
Criterion
Evidence
Observation
Finding
Severity
Action
CAP
Verification
Reinspection
Closure
Report
Appeal/Challenge
```

## Phase 7 — Scheme adapters

Priority order:

```text
1. KCAA authority surveillance
2. SAFA/SACA
3. AOC surveillance
4. Airworthiness / AMO / CAMO
5. Aerodrome / AGA
6. PEL
7. USOAP-style State oversight
8. IOSA
9. ISAGO
10. Security / Dangerous Goods / ANS
```

Scheme-specific rules must remain inside adapters.

## Phase 8 — KCAA end-to-end reference platform

```text
Organization
 → ASL/AOC application
 → Workflow
 → Documents
 → Fees
 → Compliance screening
 → Detailed assessment
 → Inspection
 → Findings/CAP
 → Approval decision
 → Certificate
 → Surveillance
 → SSP/Safety Intelligence
```

Use synthetic data and explicit jurisdiction/version metadata.

## Phase 9 — SSP / Safety Intelligence

Connect:
- occurrences
- inspections
- audits
- approvals
- corrective actions
- maintenance
- flight/airport events
- safety reports

Capabilities:
- hazard clustering
- risk registers
- SPIs/SPTs
- trend detection
- emerging risk
- safety assurance
- safety briefings

## Phase 10 — RAG / knowledge graph

RAG requirements:
- hybrid retrieval
- jurisdiction filter
- applicability filter
- temporal filter
- source authority weighting
- reranking
- citation generation
- answer/evidence separation

Knowledge graph:

```text
Authority → Regulation → Requirement
Requirement → Approval / Application
Application → Evidence / Finding
Organization → Aircraft / Approvals
Inspection → Finding → CAP
Occurrence → Hazard → Risk
```

## Phase 11 — AI agents

Agents must be tool-constrained and permission-aware.

Examples:
- Regulatory Agent
- Compliance Agent
- Inspection Agent
- Safety Agent
- Workflow Agent
- Document Agent

Each agent must declare tools, permissions, evidence requirements and escalation rules.

## Phase 12 — AI assurance and security

Implement benchmark suites for:
- groundedness
- citation correctness
- applicability
- temporal correctness
- completeness
- uncertainty
- safety escalation
- prompt injection
- retrieval poisoning
- malicious documents
- unauthorized tool calls
- data leakage

## Phase 13 — Reference applications

First applications:

1. KCAA Authority Workspace
2. Aviation Regulatory Explorer
3. AOC Compliance Assistant
4. SAFA/SACA Inspection Assistant
5. Safety Intelligence Dashboard
6. Aviation Document Assistant

## Phase 14 — Multi-authority expansion

Add adapters for:

```text
KCAA → EASA → FAA → TCCA → UK CAA → CASA
```

Conformance tests must verify that authorities can express different legal hierarchies, terminology and oversight methods without altering the shared core.

## Definition of Done for a serious v1

The project is not ready for a v1 release until it can demonstrate one complete, reproducible journey from regulatory requirement to application evidence, workflow decision, inspection finding, corrective action and safety/oversight output, with every stage versioned and auditable.