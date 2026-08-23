# Aviation Domain Model Blueprint

The repository should use a common aviation domain model so AI skills can compose instead of inventing incompatible schemas.

## Core entities

```text
Authority
Jurisdiction
LegalInstrument
Regulation
Requirement
Guidance
Organization
Operator
Aircraft
AircraftType
Engine
Component
Aerodrome
Runway
AirportFacility
Flight
Route
Airspace
Personnel
Licence
Certificate
Approval
Application
Manual
Document
Inspection
Audit
Finding
CorrectiveAction
Occurrence
Hazard
Risk
SafetyIndicator
MaintenanceEvent
AD
SB
WeatherObservation
```

## Core relationships

```text
Authority ──issues──> Regulation / Guidance
Regulation ──contains──> Requirement
Requirement ──appliesTo──> Organization / Aircraft / Operation
Organization ──holds──> Certificate / Approval
Operator ──operates──> Aircraft
Aircraft ──has──> Engine / Component
Aircraft ──has──> Certificate / MaintenanceHistory / ADStatus
Operator ──submits──> Application
Application ──requires──> Evidence / ComplianceAssessment
Authority ──conducts──> Inspection / Audit
Inspection ──produces──> Finding
Finding ──requires──> CorrectiveAction
Occurrence ──mayIndicate──> Hazard / Risk
```

## Jurisdiction-aware representation

A requirement must not simply be stored as text. At minimum:

```json
{
  "requirementId": "...",
  "authority": "KCAA",
  "jurisdiction": "KE",
  "framework": "civil-aviation-regulations",
  "instrument": "...",
  "reference": "...",
  "title": "...",
  "status": "in-force",
  "effectiveFrom": "...",
  "effectiveTo": null,
  "applicability": {
    "operation": ["commercial-air-transport"],
    "organization": ["air-operator"]
  },
  "source": {
    "uri": "...",
    "version": "..."
  }
}
```

## Approval model

An aviation approval should support:

```text
Application
 ├── Applicant
 ├── Scope
 ├── Regulatory Basis
 ├── Evidence
 ├── Assessments
 ├── Findings
 ├── Limitations
 ├── Decision
 ├── Effective Period
 └── Audit Trail
```

## Finding model

```text
Finding
 ├── Source (inspection/audit/review)
 ├── Requirement
 ├── Observation
 ├── Evidence
 ├── Severity / classification
 ├── Root-cause information
 ├── Corrective action
 ├── Due date
 ├── Verification
 └── Closure decision
```

## Design objectives

- stable identifiers
- explicit jurisdiction
- temporal validity
- source provenance
- versioning
- auditability
- extensibility for new authorities
- clean separation between fact, prediction and decision
