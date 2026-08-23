# Aviation Domain Model

The domain model is the shared vocabulary for organizations, authorities, approvals, aircraft, inspections, audits, safety and workflows.

## Design goals

- Stable identifiers
- Jurisdiction-aware entities
- Effective/expiry dates
- Source provenance
- Explicit relationships
- Versionable regulatory references
- Scheme-specific extensions without contaminating the core model

## Core entities

```text
Authority
Jurisdiction
Regulation
Requirement
Organization
Operator
Aircraft
Aerodrome
Personnel
Licence
Certificate
Approval
Application
Document
Inspection
Audit
Finding
CorrectiveAction
Occurrence
Hazard
Risk
MaintenanceEvent
AirworthinessDirective
WorkflowCase
WorkflowTask
FeeSchedule
FeeAssessment
Payment
```

## Inspection scheme principle

The core `Finding`, `Inspection` and `CorrectiveAction` entities are generic. A scheme adapter supplies its own checklist taxonomy, categorisation, actions and references.

Examples:

- SAFA / SACA
- USOAP
- Authority surveillance
- IOSA
- ISAGO
- Airworthiness inspections
- Aerodrome inspections

This prevents scheme-specific categories from becoming accidental global business rules.
