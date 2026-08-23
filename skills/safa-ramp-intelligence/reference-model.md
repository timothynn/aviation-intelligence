# SAFA / SACA Reference Model

This skill combines the supplied SAFA Ramp Inspections Guidance Material Version 2.0 (2012) with the current EASA Ramp Inspection Programme context. The 2012 material is a historical/reference source. Production implementations must reconcile every scheme rule, checklist item, finding definition and action with the current EASA legal framework, current Ramp Inspection Manual (RIM), current AMC/GM, applicable national requirements and other authoritative standards.

## Current authority model

```text
Current applicable law / regulation
          ↓
Current EASA RIM + AMC/GM / authority procedure
          ↓
Current scheme checklist + finding catalogue
          ↓
Current technical / manufacturer standards
          ↓
Historical guidance / examples
```

The current EASA programme page describes a 53-item checklist. The supplied historical 2012 guidance describes 54 items. Checklist and finding catalogues must therefore be versioned, not hard-coded globally.

## Core lifecycle

```text
Target selection
  -> Pre-inspection intelligence
  -> Preparation
  -> Ramp inspection
  -> Evidence / observations
  -> Applicability + standard assessment
  -> Finding / General Remark / satisfactory result
  -> Scheme categorisation
  -> Action determination
  -> POI + crew debrief
  -> Final report / database
  -> Corrective action / CAP
  -> Verification / reinspection
  -> Human closure decision
  -> Safety intelligence
```

## Targeting model

Support:

- long-term planning
- short-term / targeted planning
- focused inspections
- spot checks
- follow-up inspections
- approved prioritisation lists
- previous inspections and recurrent findings
- occurrence and safety information
- operator / State-of-Oversight concerns
- aircraft type, age and configuration
- operation profile and airport context

The targeting engine must preserve the underlying evidence and policy rule that caused a candidate to be recommended.

## Pre-inspection intelligence

A preparation workspace should combine:

- aircraft identity and configuration
- operator and State context
- prior inspection history
- open findings and corrective actions
- recurrent finding families
- previous inspection evidence
- technical references available to the inspector
- current flight/turnaround context

The AI assistant may summarise and rank this information but cannot create a regulatory priority outside the authority's configured policy.

## Inspection structure

The historical guidance describes checklist groups:

```text
A — Operations / flight deck
B — Safety / cabin
C — Aircraft condition
D — Cargo
E — General / other issues
```

The exact item list must be retrieved from the active checklist version. Limited inspections are a first-class workflow state because not all items may be possible within the available time/resources.

## Time and scope model

The inspection model should record:

- planned arrival and departure
- actual arrival and departure
- inspection start/end
- available inspection window
- number of inspectors
- selected items
- unselected/deferred items
- reason for reduced scope
- safety-driven prioritisation
- delay and delay reason, where applicable

The system should never enforce an arbitrary universal inspection duration such as 30 or 60 minutes. The governing concept is a comprehensive inspection within available time/resources while avoiding unreasonable delay, subject to safety.

## Findings and evidence

A finding is produced through:

```text
Observation
   ↓
Applicability
   ↓
Applicable standard
   ↓
Evidence
   ↓
Finding / General Remark
   ↓
Scheme category
```

The evidence chain should support:

- photographs / video
- POI
- technical log entries
- licences and certificates
- manuals / checklists
- AMM / SRM / CMM / MEL / CDL references
- inspector notes
- correspondence
- corrective-action evidence

Technical findings require careful assessment against the applicable aircraft/manufacturer documentation and operational limitations. AI may retrieve and compare references but must never invent a limit or autonomously determine airworthiness.

## Finding catalogue

Where the active scheme provides predefined findings, use them to improve consistency. Support:

- finding catalogue version
- inspection item
- finding code
- description
- standard reference
- categorisation guidance
- detailed description
- applicability conditions
- evidence requirements

Permit User-Described Findings only with a mandatory standard/reference and human approval.

## Categorisation

The historical SAFA v2.0 reference defines:

```text
Category 1 = minor safety influence
Category 2 = significant safety influence
Category 3 = major safety influence
Category G = general remark / information that is not a finding
```

These are versioned scheme concepts, not generic platform enums.

The platform must preserve the distinction between:

```text
Finding severity/category
        ≠
Resulting action class
```

## Action model

Historical SAFA v2.0 mapping:

```text
Category 1 → Class 1 information to captain
Category 2 → Class 1 + Class 2 communication/follow-up
Category 3 → Class 1 + Class 2 + Class 3 immediate action
```

The active RIM/legal framework must control the current action mapping and available operational consequences.

Possible historical Class 3 outcomes include restrictions, corrective action before flight, detention and immediate operating restrictions. These must remain controlled, permissioned and human-authorised.

## POI model

The Proof of Inspection should capture the inspection result provided to the PIC/operator representative.

Track:

- inspection context
- checked items
- findings/remarks included on the POI
- inspector identity
- timestamp and location
- delivery status
- acknowledgement/signature
- later final-report changes

A signature represents acknowledgement of receipt, not agreement with findings.

## Follow-up

The follow-up workflow should support:

```text
Notification
  -> Corrective action plan
  -> Root cause
  -> Preventive action
  -> Evidence
  -> Authority review
  -> Verification / reinspection
  -> Human closure decision
```

The system must retain all correspondence, evidence, decisions and dates needed to explain why a finding was closed or remains open.

## AI assistance matrix

| Capability | AI role | Human authority |
|---|---|---|
| Targeting | Rank / summarise approved signals | Approve target |
| Inspector briefing | Summarise context and history | Validate brief |
| Checklist prioritisation | Recommend focus items | Select scope |
| Standard retrieval | Retrieve / cite source | Interpret / decide |
| Applicability | Highlight relevant conditions | Decide applicability |
| Finding assistance | Suggest PDF/UDF + wording | Confirm finding |
| Categorisation | Suggest with evidence | Set final category |
| Technical defects | Retrieve technical limits/evidence | Assess defect |
| Vision | Flag visual anomaly | Inspect / verify |
| Reporting | Draft narrative | Approve report |
| CAP review | Detect missing elements | Accept/reject CAP |
| Recurrence | Detect patterns | Use in oversight planning |
| Closure | Summarise readiness | Close finding |

## AI non-delegable decisions

AI must not independently:

- impose an operational restriction
- ground or ban an aircraft
- declare an aircraft airworthy or unairworthy
- set a final finding category
- approve a corrective-action plan
- close a finding
- change an applicable regulation or standard

## AI provenance

Every material AI recommendation should reference:

- data sources
- source document and version
- effective date where applicable
- retrieved passage/record identifiers
- model/prompt version
- confidence/uncertainty where useful
- inspector decision

## Data retention and audit

Retain an auditable relationship between:

```text
Input data
  -> AI recommendation
  -> Evidence / source
  -> Human decision
  -> Final regulatory record
```

Historical observations and current regulatory sources must never be conflated.
