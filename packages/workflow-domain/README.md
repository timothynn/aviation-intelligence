# Workflow Domain

A reusable case-management and approval workflow model for aviation systems.

## Core concepts

```text
Case
  -> Workflow Definition
  -> Stage
  -> Task
  -> Decision
  -> Transition
  -> SLA / Escalation
  -> Notification
  -> Audit Event
```

A workflow transition should be deterministic and policy-controlled. AI can recommend a next action or draft a decision, but an authorized actor or deterministic rule must commit an authoritative transition for regulated processes.

## Examples

- AOC application
- Aircraft registration
- Certificate issuance
- Licence application
- Inspection follow-up
- Corrective action
- Renewal
- Suspension / reinstatement
