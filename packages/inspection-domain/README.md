# Inspection Domain

A scheme-neutral model for inspections, audits and surveillance.

## Lifecycle

```text
Target selection
  -> Preparation
  -> Scope / checklist
  -> Evidence collection
  -> Observation
  -> Finding
  -> Assessment
  -> Action / corrective action
  -> Verification
  -> Closure / escalation
```

## Scheme adapters

A scheme adapter defines:

- checklist taxonomy
- applicable standards
- finding categories
- action classes
- required evidence
- closure rules
- reporting format

The generic domain deliberately does not encode SAFA category numbers, USOAP protocol questions, IOSA standard IDs or national enforcement outcomes.
