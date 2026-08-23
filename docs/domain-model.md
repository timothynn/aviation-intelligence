# Aviation Domain Model

The common domain model is the foundation of Aviation Intelligence. AI skills must compose around shared facts rather than invent incompatible schemas.

## 1. Identity and temporal envelope

Every material domain record should support:

```text
id
type
status
jurisdiction
authority
validFrom
validTo
createdAt
updatedAt
source
provenance
securityClassification
```

The system must distinguish:

```text
Observed fact
Derived fact
Prediction
Recommendation
Authoritative decision
```

## 2. Core entities

### Governance / legal

```text
Authority
Jurisdiction
LegalFramework
LegalInstrument
Regulation
Requirement
Guidance
Standard
SourcePublication
RegulatoryChange
```

### Organization / people

```text
Organization
OrganizationUnit
Operator
AOCHandler
ServiceProvider
AccountableManager
KeyPersonnel
Personnel
Licence
Rating
TrainingRecord
Competency
Medical
```

### Aircraft / airspace / airport

```text
Aircraft
AircraftType
Engine
Component
Registration
CertificateOfAirworthiness
AircraftConfiguration
Aerodrome
Runway
Taxiway
AirportFacility
Airspace
Route
Flight
```

### Approval / certification

```text
Application
ApplicationPhase
Assessment
Approval
Authorization
Certificate
OperationsSpecification
SpecificApproval
Limitation
Exemption
Deviation
Renewal
Amendment
Suspension
Revocation
```

### Records / evidence

```text
Document
DocumentVersion
Record
Evidence
EvidenceLink
Signature
RetentionPolicy
Correspondence
Attachment
```

### Workflow / finance

```text
Case
WorkflowDefinition
WorkflowVersion
WorkflowInstance
Stage
Task
Decision
Transition
SLA
FeeSchedule
FeeRule
FeeAssessment
Invoice
Payment
Refund
Reconciliation
```

### Inspection / safety

```text
InspectionProgramme
InspectionScheme
InspectionPlan
Inspection
Checklist
ChecklistVersion
ChecklistItem
Observation
Finding
FindingClassification
ImmediateAction
CorrectiveAction
PreventiveAction
CAP
Verification
Reinspection
Audit
AuditFinding
Occurrence
Hazard
Threat
Risk
RiskControl
SafetyIndicator
SafetyTarget
SafetyIssue
SafetyReport
```

### Airworthiness / maintenance

```text
MaintenanceEvent
Defect
DeferredDefect
WorkOrder
ApprovedMaintenanceData
AD
SB
MaintenanceProgramme
ReliabilityEvent
ComponentHistory
```

## 3. Key relationships

```text
Authority ──governs──> Jurisdiction
Authority ──publishes──> LegalInstrument / Guidance
LegalInstrument ──contains──> Regulation / Requirement
RegulatoryChange ──changes──> Requirement
Requirement ──appliesTo──> Organization / Operation / Aircraft / Personnel
Organization ──holds──> Certificate / Approval
Organization ──employs──> Personnel
Operator ──operates──> Aircraft
Aircraft ──registeredAs──> Registration
Aircraft ──has──> CertificateOfAirworthiness
Aircraft ──has──> Engine / Component
Application ──submittedBy──> Organization
Application ──requires──> Requirement / Evidence
Application ──runsThrough──> WorkflowInstance
WorkflowInstance ──creates──> Task / Decision
Inspection ──targets──> Organization / Aircraft / Aerodrome / Personnel
Inspection ──uses──> InspectionScheme / Checklist
Inspection ──produces──> Observation / Finding
Finding ──references──> Requirement / Standard
Finding ──requires──> CorrectiveAction
CorrectiveAction ──verifiedBy──> Verification
Occurrence ──mayIndicate──> Hazard / Risk
Risk ──controlledBy──> RiskControl
SafetyIndicator ──measures──> SafetyObjective
FeeAssessment ──produces──> Invoice
Invoice ──settledBy──> Payment
```

## 4. Regulatory requirement object

```json
{
  "requirementId": "REQ-KE-KCAA-OPS-001",
  "authority": "KCAA",
  "jurisdiction": "KE",
  "framework": "civil-aviation-regulations",
  "instrument": "...",
  "reference": "...",
  "title": "...",
  "status": "in-force",
  "publishedAt": "...",
  "effectiveFrom": "...",
  "effectiveTo": null,
  "applicability": {
    "organizationTypes": ["air-operator"],
    "operationTypes": ["commercial-air-transport"],
    "aircraftTypes": [],
    "geography": ["KE"]
  },
  "source": {
    "uri": "...",
    "publicationId": "...",
    "version": "...",
    "retrievedAt": "...",
    "hash": "..."
  }
}
```

## 5. Approval lifecycle

```text
PreApplication
 → Application
 → Screening
 → Fees
 → DetailedAssessment
 → Compliance
 → Inspection
 → Finding/CAP
 → Decision
 → Approval/Certificate
 → Surveillance
 → Amendment/Renewal
 → Suspension/Revocation/Closure
```

Approval state is never inferred solely from workflow state. The authoritative approval record has its own lifecycle and effective period.

## 6. Inspection / finding model

```text
Inspection
 ├── Programme / Scheme / Version
 ├── Target
 ├── Team / Qualifications
 ├── Plan
 ├── Checklist Version
 ├── Observations
 ├── Evidence
 ├── Findings
 ├── Actions
 ├── Report
 └── Audit Trail

Finding
 ├── Requirement / Standard
 ├── Observation
 ├── Evidence
 ├── Classification
 ├── Severity
 ├── Immediate Action
 ├── Corrective Action
 ├── Preventive Action
 ├── Due Date
 ├── Verification
 ├── Closure
 └── Challenge / Appeal
```

## 7. Safety model

```text
Occurrence / Finding / Report
        ↓
Event classification
        ↓
Hazard / Threat
        ↓
Risk assessment
        ↓
Risk control
        ↓
Residual risk
        ↓
SPI / SPT
        ↓
Safety assurance
        ↓
Safety decision
```

## 8. Evidence model

Evidence should preserve:

```text
EvidenceId
SourceType
SourceRecord
DocumentId / Page / Section
ObservedValue
ExtractionMethod
Confidence
CapturedBy
CapturedAt
Hash
SecurityClassification
Validity
```

## 9. Design objectives

- stable identifiers
- explicit authority/jurisdiction
- temporal validity
- provenance
- versioning
- lifecycle semantics
- auditability
- security classification
- interoperability
- separation of facts from AI-derived outputs
- extensibility for new authorities and schemes