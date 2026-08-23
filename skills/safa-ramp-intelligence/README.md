# SAFA / Ramp Inspection Intelligence Skill

A dedicated scheme adapter for SAFA/SACA-style ramp inspection workflows built on the generic inspection engine.

## Current programme context

The current EASA Ramp Inspection Programme contains SAFA inspections for third-country operators and SACA inspections for operators under another EU Member State's oversight. Current implementations should use the applicable EASA rules, AMC/GM and Ramp Inspection Manual version rather than hard-coding historical guidance.

## Workflow

```text
Safety information / target selection
        ↓
Aircraft + operator context
        ↓
Inspection preparation
        ↓
Targeted / planned / spot inspection
        ↓
Checklist execution
        ↓
Evidence + observations
        ↓
Applicable standard assessment
        ↓
Finding / remark
        ↓
Category / severity
        ↓
Immediate action, if required
        ↓
POI / debrief
        ↓
Written follow-up
        ↓
Corrective action / CAP
        ↓
Verification / reinspection
        ↓
Closure
        ↓
Safety intelligence
```

## Selection signals

Support configurable rules using:
- prior ramp findings
- repeat findings
- safety reports
- occurrence information
- operator / State oversight concerns
- aircraft type and age
- operational profile
- scheduled movements
- targeted-priority lists
- new operator / new aircraft / new operation signals
- spot-check policy

The model should expose the evidence for every recommendation.

## Checklist adapter

The supplied historical SAFA Guidance Material v2.0 describes 54 checklist items: A operational, B safety/cabin, C aircraft condition and D cargo, with E-General for other issues. The current system must version this checklist and its associated standards.

## Finding model

The generic platform stores:

```text
Observation
  ↓
Applicable Standard
  ↓
Finding / General Remark
  ↓
Scheme Category
  ↓
Action Class
```

The historical SAFA v2.0 scheme adapter includes category 1/2/3 and Cat G as well as class 1/2/3 action variants. These are scheme-version data, not global platform enums.

## Evidence model

Support:
- photographs
- POI
- technical log references
- licences
- certificates
- manuals
- AMM / SRM / CMM / MEL references
- inspector notes
- correspondence
- corrective-action evidence

Each finding needs a provenance chain back to the evidence and the standard reference used.

## Follow-up model

Track:
- operator notification
- State-of-Oversight notification
- response requested
- response received
- evidence received
- verification required
- reinspection
- restriction verification
- closure decision
- closure justification
- escalation

## AI capabilities

### Targeting assistant
Rank inspection candidates from policy-approved safety signals.

### Inspector briefing
Summarize history, open findings, aircraft data, operator context and likely focus areas.

### Finding assistant
Retrieve the controlling standard and propose wording/category while requiring inspector confirmation.

### Recurrence engine
Identify recurrent findings across operator, aircraft, fleet, airport, ATA chapter, station, standard and finding family.

### Follow-up assistant
Track deadlines, missing evidence and closure readiness.

### Fleet/operator intelligence
Convert repeated ramp observations into oversight signals for the appropriate authority.

## Guardrails

Ramp inspection output is a point-in-time assessment and does not replace continuing regulatory oversight or establish general aircraft airworthiness. AI must preserve this distinction.