# Generic Inspection / Audit Engine Specification

## Purpose

Provide a reusable case engine for inspections, audits and surveillance while keeping scheme-specific criteria inside versioned adapters.

## Core objects

```text
Programme
Scheme
SchemeVersion
InspectionPlan
TargetSelection
Inspector
Qualification
Team
Checklist
ChecklistVersion
Criterion
Observation
Evidence
Finding
FindingClassification
ImmediateAction
CorrectiveAction
PreventiveAction
CAP
Verification
Reinspection
Closure
Report
Challenge
AuditEvent
```

## Lifecycle

```text
Planned
 → Scheduled
 → Prepared
 → In Progress
 → Debrief
 → Reported
 → Follow-up
 → Verification
 → Closed / Escalated
```

Scheme adapters can add or rename states, but the core must preserve the lifecycle semantics.

## Risk-based planning

Target selection should combine configurable inputs:

- regulatory obligation
- risk profile
- prior findings
- recurrence
- overdue corrective actions
- certificate/approval status
- occurrence signals
- fleet/operator characteristics
- geographic/exposure context
- scheduled movement or operational timing

The selection engine produces a recommendation and reason codes; an authorized planner approves the plan.

## Checklist versioning

A checklist item must identify:

```text
scheme
schemeVersion
checklistVersion
itemId
criterion
standardReference
applicability
mandatory
```

## Observation vs finding

```text
Observation
  = what was observed

Finding
  = assessed non-compliance against a criterion

Classification
  = scheme-specific severity/category

Action
  = what must happen next
```

AI must not collapse these layers.

## Evidence

Evidence can include:

- documents
- photographs
- screenshots
- technical references
- interviews/notes
- system records
- structured measurements

Every evidence item preserves source/provenance and security classification.

## CAP

Corrective-action handling should support:

```text
Finding
 → Immediate containment
 → Root cause
 → Corrective action
 → Preventive action
 → Owner
 → Due date
 → Evidence
 → Verification
 → Closure
```

## Scheme adapter interface

```text
getCriteria(version)
getTargetingRules(version)
getChecklist(version)
assessObservation(input)
categorizeFinding(input)
determineActions(input)
getFollowUpRules(version)
getReportSchema(version)
```

## AI integration

### Allowed recommendations

- target ranking
- inspector briefing
- checklist prioritisation
- evidence linking
- finding text suggestion
- recurrence detection
- CAP quality check
- report summarization

### Prohibited autonomous outcomes

- final enforcement decision
- automatic finding creation without configured human acceptance
- changing finding severity without review
- lifting restrictions/grounding
- certificate approval

## Initial adapters

1. KCAA authority surveillance
2. SAFA/SACA
3. AOC surveillance
4. Airworthiness
5. Aerodrome
6. PEL
7. USOAP-style State oversight
8. IOSA
9. ISAGO