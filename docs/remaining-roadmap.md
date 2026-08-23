# Remaining Work — Research-Driven 2026 Roadmap

This document records what remains after the regulatory/domain research pass and the current repository expansion.

## Current maturity

```text
Research / domain map       ~95%
Architecture                ~90%
Skill catalogue             ~95%
Domain contracts            ~60%
Reusable production code    ~30%
Reference applications      ~10%
AI/RAG implementation       ~10%
Automated evaluation        ~15%
Production hardening         ~5%
```

These are planning estimates, not measured project metrics.

## 1. Highest priority: domain contracts

Remaining work:

- strongly typed domain classes/interfaces
- lifecycle state machines
- relationship constraints
- identifiers and code systems
- temporal validity
- provenance envelope
- organization hierarchy
- authority powers/delegations
- approval/certificate state model
- inspection/audit common model
- safety domain model
- serialization/integration contracts

Definition of done: domain records can be serialized, validated and used by at least two independent reference services without incompatible models.

## 2. Regulatory ingestion and change engine

Research finding: EASA currently publishes important Easy Access Rules in XML and explicitly describes the XML as machine-readable and synchronizable with local applications; KCAA's 2025 regulatory transition demonstrates the need for version/effective-date management.

Remaining work:

- source monitors
- PDF/HTML/XML parsers
- document fingerprinting
- hierarchy extraction
- requirement extraction
- legal-status metadata
- effective/applicability modeling
- supersession chains
- semantic diff
- affected-requirement resolution
- affected-approval/workflow resolution
- human review queue

## 3. Evidence/document platform

Remaining work:

- OCR/layout service
- document classification
- metadata extraction
- field extraction
- evidence object model
- field-level provenance
- controlled document versions
- signatures
- retention policy
- source hashing
- evidence packages for inspectors/auditors

## 4. Compliance engine

Remaining work:

- applicability resolver
- requirement-to-evidence mapping
- assessment states
- reviewer workflow
- gap analysis
- conflicting evidence detection
- historical-version assessment
- compliance snapshots
- audit trail

## 5. Workflow/case engine

Remaining work:

- workflow definition schema
- versioned definitions
- state transition guards
- role/permission model
- SLAs
- escalations
- delegation
- parallel work
- return/rework patterns
- notifications
- immutable audit events
- AI recommendation boundary

## 6. Inspection/audit platform

Remaining work:

- planning service
- target-selection service
- risk inputs
- checklist versioning
- evidence capture
- observations
- findings
- corrective actions
- verification
- reinspection
- closure
- challenge/appeal
- report generation
- inspection analytics

### Scheme adapters still to implement

1. KCAA authority surveillance
2. SAFA
3. SACA
4. AOC surveillance
5. Airworthiness
6. AMO/CAMO
7. ATO
8. Aerodrome
9. PEL
10. USOAP-style State oversight
11. IOSA
12. ISAGO
13. Dangerous Goods
14. Security
15. ANS/CNS/AIS

## 7. KCAA reference implementation

KCAA should remain the first complete jurisdictional implementation.

Remaining:

- authority data
- organization model
- ASL/AOC application
- phase/workflow model
- documents
- fee assessment
- compliance matrix
- inspection/surveillance
- findings/CAP
- approval decision
- certificate
- continuing surveillance
- SSP integration

KCAA currently lists AOC surveillance, AOC renewal/recertification, Ops Spec amendments, foreign-aircraft ramp inspections and special approvals such as EDTO, PBN, RVSM and LVO among its flight-operations functions. The reference implementation should therefore model approvals as extensible objects rather than hard-coded AOC-only fields.

## 8. Portal

Remaining:

- applicant portal
- operator workspace
- inspector workspace
- reviewer workspace
- executive dashboard
- organization-scoped access
- delegated access
- notifications
- document/evidence interactions
- payment interactions
- AI assistant

## 9. Cost/fees

Remaining:

- fee schedule versioning
- effective dates
- fee-rule engine
- exemptions/waivers
- invoice lifecycle
- payment lifecycle
- reconciliation
- refund/adjustment
- cost-of-service analytics

## 10. SSP and safety intelligence

ICAO's 2025 Safety Intelligence Manual expands guidance for collecting, processing, analyzing and applying safety data/information. KCAA currently publishes SMS guidance for voluntary/confidential reporting, emergency response planning, management of change, safety performance management and safety risk management.

Remaining:

- occurrence model
- safety data catalog
- hazard register
- risk register
- safety controls
- SPIs / SPTs
- assurance monitoring
- safety intelligence pipeline
- emerging-risk detection
- State safety dashboards
- SSP assessment

## 11. RAG and knowledge graph

Remaining:

- authoritative-source ranking
- hybrid retrieval
- temporal retrieval
- jurisdiction retrieval
- applicability filters
- reranking
- citation engine
- graph construction
- graph/RAG hybrid queries
- evaluation dataset

## 12. AI agents

Remaining:

- tool registry
- permissions
- agent policies
- approval gates
- evidence requirements
- task execution audit
- human escalation
- safe failure
- agent evaluation

## 13. Advanced ML

Remaining:

- predictive maintenance
- safety-risk models
- delay/ETA forecasting
- anomaly detection
- computer vision
- speech/NLP
- uncertainty quantification
- drift monitoring

## 14. Security/governance

Remaining:

- RBAC/ABAC
- organization isolation
- document classification
- encryption
- secrets management
- audit logs
- retention/disposition
- prompt injection testing
- retrieval poisoning controls
- malicious document sandboxing
- model/tool authorization
- sensitive-data redaction

## 15. Testing and CI/CD

Remaining:

- unit tests
- contract tests
- integration tests
- schema validation
- migration tests
- domain-rule tests
- synthetic test datasets
- AI evaluation regression tests
- security scans
- dependency scanning
- documentation validation

## 16. Production-grade reference applications

Target sequence:

1. KCAA Authority Workspace
2. Regulatory Explorer
3. AOC Compliance Assistant
4. SAFA/SACA Inspection Assistant
5. Safety Intelligence Dashboard
6. Aviation Document Assistant

## V1 acceptance threshold

A serious v1 should demonstrate one end-to-end journey:

```text
Regulation
 → Requirement
 → Applicability
 → Application
 → Evidence
 → Compliance assessment
 → Workflow decision
 → Inspection
 → Finding
 → Corrective action
 → Verification
 → Approval / surveillance
 → Safety intelligence
```

Every step must preserve source/version/time/provenance and distinguish facts, predictions, recommendations and authoritative decisions.