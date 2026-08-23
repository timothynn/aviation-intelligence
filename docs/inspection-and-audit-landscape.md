# Aviation Inspection and Audit Landscape

## Purpose

Inspection and audit systems are related but not interchangeable.

- **Inspection:** direct observation or assessment of an aircraft, operation, facility, person, document set or activity against defined requirements.
- **Audit:** systematic, independent and documented assessment of a management system, process or control framework against defined criteria.
- **Surveillance:** the continuing oversight programme used by an authority or organization to determine whether an approved entity continues to comply and manage risk effectively.

The platform should use common primitives but keep these semantics distinct.

## Regulatory / oversight schemes

### ICAO USOAP CMA

USOAP CMA evaluates State safety oversight implementation. ICAO identifies eight audit areas: legislation/regulations, organization, personnel licensing, operations, airworthiness, accident/incident investigation, air navigation services, and aerodromes/ground aids. Its critical elements range from primary legislation through surveillance and resolution of safety issues.

Software implications:
- protocol-question model
- evidence mapping
- State capability assessment
- audit-area scorecards
- effective implementation calculation
- corrective-action tracking
- State profile and trend analytics

### EASA Standardisation

EASA standardisation assesses Member State competent authorities and other national systems for effective implementation of the applicable EU aviation framework.

Software implications:
- authority assessment programmes
- standardisation findings
- evidence requests
- observation/finding lifecycle
- follow-up
- horizontal findings / cross-authority trends

### SAFA / SACA Ramp Inspections

The EU Ramp Inspection Programme contains two components:
- **SAFA** — third-country operators assessed against applicable international safety standards.
- **SACA** — operators under another EU Member State's oversight assessed against applicable EU requirements.

The programme can use targeted inspections based on safety information and database analysis and can also conduct spot checks.

### SAFA inspection process

```text
Safety information / selection
          ↓
Aircraft & operator preparation
          ↓
Targeted / planned / spot inspection
          ↓
Checklist execution
          ↓
Evidence capture
          ↓
Finding assessment
          ↓
Finding categorisation
          ↓
Immediate action if required
          ↓
POI / debrief
          ↓
Written follow-up
          ↓
Operator corrective action / CAP
          ↓
State-of-oversight involvement
          ↓
Verification / reinspection
          ↓
Closure
          ↓
Database analysis / risk intelligence
```

The uploaded SAFA Guidance Material v2.0 identifies the inspection preparation sequence as selection, information gathering and preparation of the inspection. It also states that the checklist contains 54 items: 24 operational (A), 14 safety/cabin (B), 12 aircraft condition (C), 3 cargo (D), plus E-General for other issues. fileciteturn27file7L503-L520

The same guidance states that inspectors should prioritize safety-critical items when time is constrained and consider prior inspection results, aircraft configuration and aircraft age/type when selecting focus areas. fileciteturn27file7L515-L520

### SAFA finding model

A finding is a deviation from an applicable standard. Categories represent perceived influence on flight safety:

- Category 1 — minor influence
- Category 2 — significant influence
- Category 3 — major influence
- Cat G — general remark for relevant issues that do not constitute a finding

The guidance stresses that inspectors should establish applicability and assess the situation before categorisation. fileciteturn27file0L178-L191

A technical finding may need assessment against aircraft manufacturer documentation and certification standards; this means the inspection platform needs support for AMM, SRM, CMM, WDM/SWPM, MEL and related controlled references. fileciteturn26file1L575-L606

### SAFA action model

The v2.0 material defines a follow-up chain involving the State of Inspection, operator, State of Operator and, where relevant, State of Registry. The process includes the POI, written communication for category 2/3 findings, corrective-action evidence, State-of-Oversight involvement, closure and possible subsequent inspections. fileciteturn27file0L13-L33

Class 3 actions require additional controls. They include restrictions on operations, corrective actions before flight, grounding by the inspecting authority and immediate operating bans. The system must model the action imposed and its verification separately from finding category. fileciteturn27file1L80-L120

### IOSA

IOSA is an IATA industry audit programme, not a State regulatory inspection. Since 2024 it has used a risk-based approach with audit scope tailored to the auditee and a maturity assessment of safety-critical systems and programmes. citeturn567848search0turn567848search2

Software implications:
- audit programme
- auditee profile
- risk-based scope selection
- ISARP/control model
- evidence sampling
- implementation assessment
- maturity assessment
- findings and corrective actions
- renewal / registration lifecycle

### ISAGO

ISAGO is IATA's global oversight programme for ground handling service providers. It covers management and operational disciplines including passenger handling, baggage, ramp, load control and cargo/mail handling. In 2025 the methodology was enhanced for deeper implementation assessment, and the 2026 checklist uses ICHM in place of the former cargo module. citeturn567848search3turn567848search8

Software implications:
- HQ audit
- station audit
- discipline-based checklist
- gap analysis / self-assessment
- findings
- registration / station accreditation
- 24-month lifecycle

## Inspection platform architecture

```text
Inspection Programme
      │
      ├── Scheme
      ├── Scope
      ├── Jurisdiction
      ├── Criteria / Standards
      └── Risk Model
              │
              ▼
       Inspection Plan
              │
      ┌───────┴────────┐
      ▼                ▼
 Inspector Team     Target / Entity
      │                │
      └───────┬────────┘
              ▼
        Checklist Run
              │
      ┌───────┼────────┐
      ▼       ▼        ▼
 Evidence  Observation Finding
                       │
                Categorisation
                       │
                 Action / CAP
                       │
                 Verification
                       │
                    Closure
                       │
                 Risk Analytics
```

## Common inspection primitives

- Programme
- Scheme
- Inspection type
- Inspection plan
- Target selection rule
- Inspector
- Inspector qualification
- Team
- Checklist
- Checklist version
- Item
- Standard / criterion
- Evidence
- Observation
- Finding
- Finding category
- Severity
- Immediate action
- Corrective action
- Preventive action
- CAP
- Response
- Verification
- Reinspection
- Closure
- Appeal / challenge
- Report
- Attachment
- Notification
- Audit trail

## AI skills

### Inspection planning
Use historical findings, risk indicators, fleet/operator profile and upcoming movements to propose a focus list. Human approval remains mandatory.

### Inspector briefing
Produce a concise pre-inspection briefing containing relevant history, open actions, previous recurrent findings, aircraft/operator information and applicable standards.

### Checklist optimization
When time or access is constrained, rank checklist items while preserving mandatory coverage rules.

### Evidence assistant
Attach photographs, documents, technical references and notes to specific checklist items and preserve provenance.

### Finding assistant
Suggest applicable finding text/category and retrieve the controlling standard, but require inspector confirmation.

### Recurrence detection
Detect the same or related findings by operator, aircraft, fleet, ATA chapter, airport, station, organization, inspector or process.

### Root-cause assistance
Cluster findings into potential systemic causes without asserting causal conclusions without evidence.

### CAP assessment
Compare proposed corrective/preventive actions against the finding, evidence and historical recurrence.

### Oversight intelligence
Convert inspection results into operator, fleet, organization, airport and State-level safety trends.

## Key design rule

Inspection software must preserve the difference between:

```text
Observation → Finding → Categorisation → Action → Closure
```

AI may assist at every step, but it must not silently convert an observation into an authoritative finding.