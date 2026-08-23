# SAFA / Ramp Inspection Intelligence Skill

A regulated-system skill for AI-assisted SAFA/SACA ramp inspection workflows. The skill separates scheme rules and authoritative sources from probabilistic AI assistance so that AI can accelerate inspection work without becoming the source of regulatory authority.

## Current programme context

For EU Ramp Inspection Programme implementations, use the current EASA legal and procedural framework as the source of truth:

- [EASA Ramp Inspection Programmes (SAFA/SACA)](https://www.easa.europa.eu/en/domains/air-operations/ramp-inspection-programmes-safa-saca)
- Commission Regulation (EU) No 965/2012, Subpart RAMP
- EASA Easy Access Rules for Air Operations, current revision
- EASA Ramp Inspection Manual (RIM) and its current appendices
- Applicable published national standards
- ICAO standards for SAFA inspections of third-country operators, where applicable
- Manufacturer standards for technical-condition assessments, where applicable

The supplied **SAFA Ramp Inspections Guidance Material Version 2.0 (2012)** is retained as a historical/reference source for workflow understanding and legacy mappings. It must not silently override the current RIM, Regulation, AMC/GM or current checklist.

Current EASA material describes a **53-item** ramp checklist, while the supplied historical 2012 guidance describes **54 items**. Therefore checklist counts and item definitions must be versioned rather than hard-coded globally.

## Purpose

Use this skill to implement:

- inspection planning and targeting
- pre-inspection intelligence
- dynamic checklist selection
- evidence capture and provenance
- finding and remark assistance
- applicable-standard retrieval
- corrective-action and follow-up management
- recurrence and trend intelligence
- AI-assisted reporting and quality checks

## Core workflow

```text
Safety information / target selection
        ↓
Aircraft + operator + flight context
        ↓
Pre-inspection intelligence
        ↓
Inspection preparation
        ↓
Planned / targeted / focused / spot / follow-up inspection
        ↓
Dynamic checklist execution
        ↓
Observations + evidence
        ↓
Applicability + standard assessment
        ↓
Finding / General Remark / satisfactory result
        ↓
Scheme categorisation
        ↓
Action determination
        ↓
POI + crew debrief
        ↓
Final report / database submission
        ↓
Corrective action / CAP
        ↓
Verification / reinspection
        ↓
Human closure decision
        ↓
Safety intelligence / future targeting
```

## Inspection targeting

Targeting must be explainable and policy-controlled. Support signals such as:

- prior ramp inspections
- recurrent findings
- open corrective actions
- safety reports and occurrence information
- operator / State of oversight concerns
- aircraft type and age
- operational profile
- scheduled movements and airport context
- targeted-priority lists
- new operator / new aircraft / new operation signals
- approved spot-check policies

AI may rank or summarise candidates, but the authority's approved targeting policy remains deterministic and inspectable.

## Pre-inspection intelligence

The inspector workspace should provide a concise briefing containing:

- aircraft identity and configuration
- operator and State-of-Oversight context
- recent inspections
- previous Category 2/3 or other significant findings, where the scheme version supports them
- recurrent finding families
- outstanding corrective actions
- aircraft/manufacturer technical references available to the inspector
- recommended inspection focus with evidence and rationale

Every AI recommendation must expose the underlying records and source references.

## Dynamic checklist

Do not assume every inspection must execute every checklist item.

The current EASA framework says the inspection should start as soon as possible and be as comprehensive as possible within available time and resources. Where time/resources are constrained, a reduced set may be inspected, with priority given to safety-critical or previously deficient areas.

The checklist adapter must therefore support:

- versioned checklist definitions
- item applicability
- selected vs non-selected items
- selection rationale
- previous-finding priority
- arrival vs departure inspection context
- time/resource constraints
- deferred inspection items for later inspections

## Findings model

Use the generic platform model:

```text
Observation
  ↓
Applicability assessment
  ↓
Applicable Standard
  ↓
Finding / General Remark / Satisfactory
  ↓
Scheme category
  ↓
Scheme action
```

For the historical SAFA v2.0 reference model, categories 1/2/3 and Cat G plus class 1/2/3 actions are scheme-version data. Do not make them global platform enums.

Use versioned Pre-Described Findings (PDFs) where the current RIM provides them; allow User-Described Findings (UDFs) with mandatory standard references where no suitable predefined finding exists.

## Technical defect assessment

Technical observations must be assessed against the applicable aircraft/manufacturer documentation and operational limitations before categorisation. Depending on the applicable scheme and evidence, references may include:

- AMM
- SRM
- CMM
- MEL
- CDL
- technical log / tech log entries
- aircraft certification specifications
- other approved technical references

AI may retrieve and compare evidence, but it must not invent a technical limit or independently declare an aircraft unairworthy.

## Evidence model

Support a full provenance chain for:

- photographs / video
- POI
- technical log references
- licences
- certificates
- manuals and checklists
- AMM / SRM / CMM / MEL / CDL references
- inspector observations
- correspondence
- corrective-action evidence
- verification evidence

Each finding should be traceable to the evidence and standard reference used to support it.

## Proof of Inspection (POI)

The POI is part of the operational workflow, not merely a report attachment. Track:

- inspected items
- remarks/findings included on the POI
- inspector identity
- date/time/place
- flight/operator/aircraft context
- delivery to PIC/operator representative
- acknowledgement/signature
- later report-quality changes

The crew signature represents receipt/acknowledgement, not agreement with findings. The final report may be amended following quality review, so the system should preserve version history.

## Findings and action boundary

The platform must distinguish **finding severity/category** from **resulting action class**.

For the historical SAFA scheme adapter:

```text
Category 1 → Class 1 information
Category 2 → Class 1 + Class 2 follow-up
Category 3 → Class 1 + Class 2 + Class 3 immediate action
```

Class 3 variants may include operational restrictions, corrective action before flight, detention or operating-ban consequences depending on the applicable version of the rules.

AI must never autonomously impose these actions.

## Follow-up lifecycle

Track:

- operator notification
- State-of-Oversight notification
- response requested
- corrective action plan
- root-cause analysis
- preventive action
- evidence received
- authority review
- verification required
- reinspection
- restriction verification
- closure decision
- closure justification
- escalation
- recurrence

Closure must be a controlled human/regulatory decision.

## AI capabilities

### 1. Targeting assistant
Rank or summarise inspection candidates from approved safety signals and show the evidence behind the recommendation.

### 2. Inspector briefing
Generate a focused pre-inspection brief from operator, aircraft, flight, historical finding and open-action data.

### 3. Checklist prioritisation assistant
Recommend inspection items when time/resources are constrained, taking account of previous findings, flight configuration, safety relevance and available time.

### 4. Regulatory / technical retrieval
Retrieve the current applicable standard, RIM instruction, AMC/GM, ICAO reference or manufacturer document and present the source with the answer.

### 5. Finding assistant
Suggest the most relevant predefined finding/UDF, standard reference and draft wording while requiring inspector confirmation.

### 6. Applicability assistant
Help determine whether an observed condition is applicable to the inspected flight, aircraft configuration and operating context.

### 7. Technical-defect assistant
Index and retrieve technical references, compare the observed evidence with documented limits, and identify missing evidence. Do not allow unsupported autonomous airworthiness conclusions.

### 8. Evidence intelligence
Automatically associate photographs, logs, documents and notes with findings while preserving provenance.

### 9. Finding consistency checker
Flag possible mismatch between evidence, standard, finding category and historical treatment. Present this as a review warning, not as an automatic correction.

### 10. Report assistant
Draft inspection summaries, findings narratives and correspondence from structured data. Inspector/authority approval remains mandatory.

### 11. Corrective-action assistant
Assess whether a response contains sufficient root cause, correction, preventive action, evidence and verification information. It may identify gaps but must not close the finding.

### 12. Recurrence engine
Detect recurrent finding families across operator, aircraft, fleet, airport, ATA/system, station, standard and time.

### 13. Safety-intelligence assistant
Surface fleet/operator trends, repeat deficiencies and emerging risk signals for approved oversight planning.

### 14. Computer-vision assistant
Flag possible visual anomalies from ramp photographs such as apparent damage, leakage, tyre anomalies or missing components. Vision output is an observation lead only and requires inspector verification.

## AI governance boundary

```text
Deterministic regulatory layer
        │
        ├── Applicable law / RIM / standards
        ├── Checklist version
        ├── Categorisation rules
        ├── Action rules
        ├── Workflow permissions
        └── Human approval requirements

AI assistance layer
        │
        ├── Retrieval
        ├── Summarisation
        ├── Ranking
        ├── Classification suggestions
        ├── Pattern detection
        ├── Drafting
        └── Vision anomaly detection

Human / authorised authority
        │
        ├── Final finding
        ├── Final category
        ├── Operational action
        ├── Corrective-action acceptance
        └── Closure / enforcement decision
```

AI must not independently:

- determine final compliance
- issue a Category 3 action
- restrict, detain or ban an aircraft
- declare an aircraft airworthy/unairworthy
- approve a corrective action plan
- close a finding
- change a regulatory requirement

## Explainability requirements

Every material AI recommendation should expose:

- recommendation type
- evidence used
- source documents
- source/version timestamps
- applicable rule or standard
- model/version identifier
- confidence or uncertainty indicator where meaningful
- human decision outcome
- audit event ID

## Security and privacy

SAFA data can contain commercially and operationally sensitive information. Implement:

- role-based access
- least-privilege document access
- evidence-level permissions
- source/document redaction where required
- immutable audit logging
- retention and deletion policies
- tenant/operator isolation
- prompt/output logging subject to applicable data policies
- protection against prompt injection from uploaded documents

## Evaluation strategy

Evaluate AI separately from deterministic regulatory logic.

### Retrieval
- source citation accuracy
- stale-source detection
- standard/version correctness

### Finding assistance
- correct checklist-item retrieval
- correct PDF/UDF matching
- category recommendation agreement with expert inspectors
- unsupported-claim rate

### Targeting
- ranking usefulness
- historical-signal coverage
- false-positive rate
- explanation quality

### Follow-up
- missing-evidence detection
- action-plan completeness detection
- recurrence detection precision/recall

### Vision
- anomaly detection precision/recall
- false-negative safety review
- human acceptance rate

## Source and version policy

The source hierarchy should be explicit:

1. Current applicable law/regulation
2. Current EASA RIM / AMC / GM and applicable authority procedures
3. Current ICAO standards or other scheme-authoritative standards
4. Current manufacturer/approved technical documentation
5. Historical guidance and examples, clearly labelled as historical

Never silently treat historical checklist counts, finding text or action mappings as current requirements.

## Related skills

- `inspection-intelligence`
- `regulatory-intelligence`
- `aviation-rag`
- `evidence-provenance`
- `aviation-computer-vision`
- `anomaly-detection`
- `ai-groundedness`
- `ai-temporal-validation`
- `ai-explainability`
- `ai-audit-trail`
- `ai-safety-guardrails`
