# Air Operations & Approvals Skill

A common domain layer for operator certification, operational approvals and lifecycle workflows.

## Key entities

```text
Operator
 ├── AOC / operating certificate
 ├── Operations Specifications / approved capabilities
 ├── Aircraft
 ├── Bases / areas of operation
 ├── Manuals
 ├── Key personnel
 ├── Specific approvals
 └── Surveillance history
```

## Approval lifecycle

```text
Pre-application
      ↓
Formal application
      ↓
Screening
      ↓
Fees / administrative checks
      ↓
Formal acceptance
      ↓
Compliance demonstration
      ↓
Document review
      ↓
Inspection / demonstration
      ↓
Findings / corrective actions
      ↓
Approval / authorization
      ↓
Continued surveillance
```

The workflow engine must permit controlled outcomes at relevant stages:

```text
Proceed
Return for Correction
Pending Information
Accepted
Accepted with Limitations
Rejected
Suspended
Revoked
Closed
```

## Specific approval model

Support approval families such as:

- PBN
- RVSM
- LVO
- EDTO / ETOPS
- dangerous goods
- CAT II/III
- MNPS / oceanic operations
- specialized operations
- UAS authorizations

## AI capabilities

- application completeness checks
- document-to-requirement mapping
- missing-evidence identification
- reviewer briefing
- approval-condition extraction
- limitation drafting assistance
- workflow next-action recommendations
- application risk triage
- regulatory-impact detection

## Design rule

Approval decisions remain explicit domain events performed by authorized actors. AI provides evidence-backed assistance around the workflow.
