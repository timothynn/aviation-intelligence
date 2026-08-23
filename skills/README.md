# Aviation Intelligence Skills

Skills are reusable aviation engineering capabilities. A mature skill must be domain-aware, independently understandable, testable and explicit about its assurance boundary.

## Skill contract

Every mature skill should document:

1. Purpose
2. Aviation/domain scope
3. Authority or standards references
4. Inputs and required context
5. Outputs and evidence
6. Architecture and dependencies
7. Deterministic rules versus probabilistic AI
8. Evaluation strategy
9. Security/privacy considerations
10. Human-review and escalation points
11. Known limitations
12. Version/source policy

## P0 — Regulated-system foundation

- `aviation-domain-model`
- `aviation-data-engineering`
- `organization-intelligence`
- `aviation-entity-resolution`
- `regulatory-intelligence`
- `regulatory-ingestion`
- `regulatory-change`
- `aviation-document-intelligence`
- `evidence-provenance`
- `compliance-assurance`
- `workflow-intelligence`
- `inspection-intelligence`
- `audit-intelligence`
- `portal-platform`
- `cost-intelligence`
- `ssp-safety-intelligence`

## P1 — Aviation certification, oversight and inspections

- `air-operations-approvals`
- `aoc-certification`
- `operational-approvals`
- `authority-oversight-intelligence`
- `safa-ramp-intelligence`
- `saca-ramp-intelligence`
- `usop-cma-style-oversight`
- `airworthiness-certification`
- `airworthiness-maintenance`
- `airworthiness-directives`
- `ato-amo-camo-certification`
- `aerodrome-certification`
- `personnel-licensing`
- `dangerous-goods-compliance`
- `aviation-security-compliance`

## P2 — Safety and operational intelligence

- `safety-intelligence`
- `occurrence-intelligence`
- `risk-modeling`
- `safety-performance`
- `flight-data-intelligence`
- `flight-risk-intelligence`
- `airport-operations`
- `aeronautical-information`
- `weather-intelligence`
- `atm-ans-intelligence`
- `reliability-intelligence`
- `predictive-maintenance`

## P3 — Knowledge and AI

- `aviation-rag`
- `aviation-knowledge-graph`
- `aviation-nlp`
- `aviation-speech`
- `aviation-computer-vision`
- `anomaly-detection`
- `forecasting`
- `classification`
- `aviation-agents`

## P4 — AI assurance and governance

- `human-in-the-loop`
- `ai-evaluation`
- `ai-groundedness`
- `ai-applicability`
- `ai-temporal-validation`
- `ai-explainability`
- `ai-confidence`
- `ai-audit-trail`
- `ai-safety-guardrails`
- `ai-security`
- `ai-model-monitoring`
- `data-provenance`
- `data-retention`

## Scheme adapter principle

The generic platform owns:

```text
Case
Workflow
Evidence
Finding
CorrectiveAction
Verification
Audit
Notification
Authorization
```

A scheme adapter owns:

```text
Criteria
Checklist
Targeting
Categorisation
Scheme-specific Actions
Follow-up rules
Reporting format
```

This is mandatory for SAFA/SACA, USOAP-style oversight, IOSA, ISAGO and national inspection frameworks.

## Implementation priority

```text
P0  Domain + Regulatory + Evidence + Compliance + Workflow + Inspection
P1  KCAA AOC + KCAA Surveillance + SAFA/SACA + Airworthiness
P1  Portal + Cost + SSP/Safety
P2  RAG + Change Impact + Knowledge Graph
P3  Agents + Predictive ML + CV + Speech
P4  Assurance + Security + Production Observability
```

Avoid vendor-specific wrappers as standalone skills. A skill should expose reusable domain contracts and adapters.