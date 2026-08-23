# Portal, Workflow and Cost Architecture

## 1. Portal as a controlled experience layer

The portal is a delivery channel for applicants, operators, inspectors, reviewers, auditors and executives. It must never be the source of regulatory truth.

```text
Public / External Portal
        ↓
Identity + Organization Context
        ↓
BFF / API
        ↓
Domain Services
 ├── Organization
 ├── Application
 ├── Document/Evidence
 ├── Workflow
 ├── Compliance
 ├── Inspection
 ├── Fees/Payments
 ├── Certificate/Approval
 └── Notifications
        ↓
AI Gateway
```

### Portal workspaces

- Public information / regulatory explorer
- Organization self-service
- Applicant workspace
- Operator workspace
- Inspector workspace
- Reviewer workspace
- Auditor workspace
- Executive/authority dashboard

### Required portal capabilities

- registration and organization setup
- delegated access
- organization-scoped permissions
- guided applications
- dynamic forms
- document/evidence upload
- document versioning
- fee quotation
- payment initiation
- status tracking
- clarification requests
- correspondence
- corrective-action responses
- certificate/approval views
- notifications
- appointments
- dashboard/reporting
- accessibility and localization
- AI assistance

### AI portal capabilities

```text
Application Copilot
Document Pre-check
Status Copilot
Correspondence Copilot
Inspection Briefing
Knowledge Assistant
```

AI must use authoritative domain/workflow data and must not infer a status or approval that does not exist in the system of record.

## 2. Workflow / case management

Workflow is domain-neutral and must support both authority and operator processes.

### Core primitives

```text
WorkflowDefinition
WorkflowVersion
Case
Stage
Task
Assignment
Role
Permission
Decision
Guard
Transition
ParallelBranch
Join
SLA
Escalation
Delegation
Notification
AuditEvent
```

### Transition contract

Every authoritative transition records:

```text
actor
role
permission
previousState
newState
reason
comment
evidence
policyVersion
workflowVersion
timestamp
```

### Aviation patterns

```text
Pre-application
 → Formal application
 → Screening
    ├─ Return for corrections ──┐
    ├─ Reject                   │
    └─ Proceed                  ▼
         Fees
           ↓
      Assessment
           ↓
      Compliance
           ↓
      Inspection
           ↓
      Findings / CAP
           ↓
      Decision
           ↓
      Approval
           ↓
      Surveillance
```

### AI workflow intelligence

- case summarization
- next-best action
- queue prioritization
- SLA breach prediction
- workload balancing
- bottleneck detection
- missing-task detection
- workflow anomaly detection
- transition recommendation

AI may recommend but may not bypass authorization or silently mutate workflow state.

## 3. Cost / fee engine

Fees are versioned domain data, not UI logic.

```text
Jurisdiction
 ↓
FeeSchedule Version
 ↓
FeeRule
 ├── Service
 ├── Applicant class
 ├── Organization type
 ├── Aircraft / size / category
 ├── Inspection type
 ├── Location
 ├── Urgency
 ├── Currency
 ├── Tax
 └── Exemption / waiver
 ↓
FeeAssessment
 ↓
Invoice
 ↓
Payment
 ↓
Receipt / Reconciliation
```

### Fee requirements

- effective dates
- versioning
- calculation trace
- currency and tax separation
- waivers/exemptions with authorization
- refunds/adjustments
- payment state separate from workflow state
- reconciliation state
- immutable audit history

### AI opportunities

- fee estimator
- fee-rule explanation
- invoice anomaly detection
- payment reconciliation assistant
- revenue forecasting
- cost-to-serve analysis
- inspection travel-cost optimization

## 4. Identity and authorization

Security must be organization-aware:

```text
User
 ↓
Identity
 ↓
Organization Membership
 ↓
Delegated Role
 ↓
Permissions
 ↓
Case / Record / Action Scope
```

Support RBAC and, where required, attribute-based conditions such as jurisdiction, department, case ownership, sensitivity and delegated authority.

## 5. Audit and records

Portal actions create audit events, but domain events remain authoritative. Record retention, signatures, correspondence and evidence must be managed independently of the web UI.

## 6. Reference architecture

```text
Angular / Web / Mobile
          ↓
       BFF/API
          ↓
 ┌────────┼──────────────┐
 ▼        ▼              ▼
Domain  Workflow      AI Gateway
Services  Service          │
 ▼        ▼          ┌─────┼─────┐
DB       Event Bus   RAG   ML  Agents
          │
          ▼
      Audit / Events
```
