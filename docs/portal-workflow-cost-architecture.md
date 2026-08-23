# Portal, Workflow and Cost Architecture

## Portal

A portal is a delivery channel that exposes aviation services to external users. It should not contain the authoritative business rules.

### Portal layers

```text
Experience
  ├── Public information
  ├── Organization self-service
  ├── Inspector workspace
  ├── Reviewer workspace
  └── Executive / oversight dashboard
        ↓
API / BFF
        ↓
Business Services
        ↓
Workflow / Rules / Documents / Payments
```

### Portal capabilities

- identity and organization registration
- delegated access
- application submission
- guided forms
- document upload
- document versioning
- payment initiation
- appointment booking
- status tracking
- correspondence
- clarification requests
- corrective-action responses
- certificate downloads
- notifications
- dashboards
- support / knowledge assistant

### AI capabilities

**Application Copilot** — guides the applicant through requirements without making eligibility decisions.

**Document Pre-check** — identifies unreadable, incomplete or apparently mismatched evidence.

**Status Copilot** — explains the current workflow state using authoritative workflow data.

**Correspondence Copilot** — drafts responses from approved templates and evidence.

**Inspector Copilot** — prepares a field briefing and surfaces prior results.

## Workflow

The workflow engine should be domain-neutral.

### Workflow primitives

- Definition
- Version
- Case
- State
- Stage
- Task
- Assignment
- Role
- Decision
- Guard / condition
- Transition
- Parallel branch
- Join
- SLA
- Escalation
- Delegation
- Notification
- Work item
- Audit event

### Aviation workflow pattern

```text
Application
   ↓
Pre-application
   ↓
Formal application
   ↓
Screening
   ├── Return for correction ──┐
   ├── Reject                  │
   └── Proceed                 ▼
        Fees / Assessment / Compliance
                     ↓
                Inspection
                     ↓
             Corrective actions
                     ↓
                  Approval
                     ↓
              Continuing oversight
                     ↓
           Renewal / Amendment / Enforcement
```

Every transition should have:
- actor
- timestamp
- previous state
- new state
- reason
- comment
- supporting evidence
- required permission
- rule/version used

### AI workflow skills

- next-best action
- case summarization
- SLA breach prediction
- workload balancing
- queue prioritization
- bottleneck detection
- missing-task detection
- workflow anomaly detection
- transition recommendation

AI should never bypass an authorization gate or create a state transition without an explicitly configured policy allowing it.

## Cost / fee engine

Cost is a cross-cutting capability that should serve certification, inspections, approvals, licensing, renewals and other chargeable services.

### Fee model

```text
Jurisdiction
   ↓
Fee Schedule
   ↓
Effective Date / Version
   ↓
Fee Rule
   ├── Service
   ├── Applicant / Organization class
   ├── Aircraft / size / category
   ├── Inspection type
   ├── Location
   ├── Urgency
   └── exemptions / waivers
           ↓
        Calculation
           ↓
        Invoice
           ↓
        Payment
           ↓
       Reconciliation
```

### Important design rules

1. Fees are data, not code.
2. Fee schedules are versioned and effective-dated.
3. Every invoice line should resolve back to the fee rule that generated it.
4. Currency and tax treatment must be explicit.
5. Waivers and exemptions require provenance and authorization.
6. Payment state must be distinct from workflow state.

### AI opportunities

- fee estimator
- fee-rule explanation
- invoice anomaly detection
- reconciliation assistant
- revenue forecasting
- cost-of-service analytics
- inspection travel-cost optimization

## Integration pattern

```text
Portal
  ↓
BFF/API
  ├── Identity
  ├── Organization
  ├── Application
  ├── Workflow
  ├── Document
  ├── Cost/Payment
  └── Notification
        ↓
AI Gateway
  ├── RAG
  ├── Agents
  ├── Evaluation
  └── Audit
```
