# Workflow / Case Engine Specification

## Purpose

A domain-neutral case and workflow engine for regulated aviation processes.

## Core model

```text
WorkflowDefinition
  └── WorkflowVersion
        └── State / Stage
              └── Transition
                    ├── Guard
                    ├── Permission
                    ├── Task
                    ├── SLA
                    └── AuditEvent
```

## Case

A case is the long-lived container for a regulated process such as an AOC application, inspection, corrective action or renewal.

```text
Case
- id
- type
- organizationId
- jurisdiction
- workflowDefinitionId
- workflowVersion
- currentState
- status
- createdAt
- dueAt
- securityClassification
```

## Transition rules

Every transition must evaluate:

1. current state
2. actor identity
3. organization context
4. role/permission
5. deterministic guards
6. required evidence/tasks
7. approval/delegation policy
8. workflow version

## Rework

Common aviation patterns:

```text
Proceed
Return for Corrections
Reject
Escalate
Request Information
Suspend
Resume
Close
```

Rework creates traceable state history rather than overwriting the previous decision.

## AI capabilities

- next-best-action recommendation
- case summary
- workload balancing
- SLA risk
- bottleneck detection
- missing-task detection
- routing recommendation

AI recommendations are non-authoritative until accepted through the configured workflow permission gate.

## Audit

Record:

```text
actor
organization
role
permission
previousState
newState
reason
comment
evidence
workflowVersion
policyVersion
timestamp
```

## Integration

The workflow engine integrates with organization, documents, compliance, inspection, cost/payment, notifications and approval services but does not own their authoritative records.