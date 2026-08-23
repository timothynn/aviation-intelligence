# Inspection Intelligence Skill

A reusable foundation for aviation inspections, audits, surveillance and corrective-action workflows.

## Scope

Applicable to:

- authority surveillance
- SAFA/SACA-style ramp inspections
- AOC surveillance
- AMO/CAMO/ATO inspections
- aerodrome inspections
- ANS/CNS/AIS inspections
- dangerous goods inspections
- licensing inspections
- special / focused / spot inspections
- internal operator audits

## Workflow

```text
Programme
      ↓
Target selection
      ↓
Preparation / inspector briefing
      ↓
Checklist / scope
      ↓
Evidence collection
      ↓
Observation
      ↓
Finding assessment
      ↓
Categorisation / severity
      ↓
Action
      ↓
Corrective / preventive action
      ↓
Verification / reinspection
      ↓
Closure / escalation
```

## Core data

Programme, scheme, inspection type, checklist version, item, criterion, inspector, team, target entity, evidence, observation, finding, category, severity, immediate action, CAP, response, verification, closure and audit trail.

## AI assistance

- risk-based target selection
- pre-inspection briefing
- historical finding summarization
- recurring-finding detection
- checklist prioritization
- evidence-to-requirement matching
- finding wording/category suggestions
- standards/source retrieval
- report drafting
- corrective-action quality checks
- inspection trend analysis

## SAFA-specific extensions

The SAFA implementation should add a dedicated scheme layer rather than embedding SAFA behavior in the generic inspection engine. See `skills/safa-ramp-intelligence`.

## Human control

AI-generated findings, categories, severity assessments and enforcement/action recommendations remain recommendations until reviewed and accepted by an authorized inspector/auditor.