# Aviation Inspection and Audit Landscape

Inspection, audit and surveillance share technical primitives but must remain semantically distinct.

- **Inspection:** direct assessment of an aircraft, operation, person, facility, document set or activity against defined criteria.
- **Audit:** systematic, independent and documented assessment of a system, process or control framework against defined criteria.
- **Surveillance:** continuing oversight used by an authority to verify that an approved entity remains compliant, safe and effectively controlled.
- **Monitoring / assurance:** continuous analysis of evidence, risk and performance between formal inspection events.

## Common platform model

```text
Programme
  ↓
Scheme + Version
  ↓
Risk / Target Selection
  ↓
Plan
  ↓
Team + Qualifications
  ↓
Checklist / Protocol
  ↓
Evidence + Observation
  ↓
Finding / Assessment
  ↓
Action / CAP
  ↓
Verification / Reinspection
  ↓
Closure / Escalation
  ↓
Risk + Safety Intelligence
```

## 1. ICAO USOAP CMA / State oversight

USOAP CMA is a continuous, risk-based monitoring approach. ICAO assesses implementation of eight Critical Elements and uses standardized Protocol Questions. SSP-related integrated assessment adds a maturity perspective. citeturn535738search5

Software model:
- audit programme
- State profile
- PQ library + version
- evidence request
- State response
- assessment
- effective implementation / maturity
- finding
- corrective action
- follow-up
- cross-State benchmarking

## 2. EASA Standardisation

EASA Standardisation is itself an oversight/monitoring function over competent authorities. Current planning material emphasizes continuous monitoring, maturity-based prioritisation and use of IT tools to support proactive standardisation. citeturn934489search6

This suggests a reusable authority-level model:

```text
Authority profile
 → maturity/risk
 → monitoring programme
 → desktop assessment
 → onsite/system inspection
 → finding
 → corrective action
 → maturity reassessment
```

## 3. SAFA / SACA ramp inspection programme

The current EASA programme is the **EU Ramp Inspection Programme** with two components:

- **SAFA** — third-country operators assessed against applicable international safety standards.
- **SACA** — operators under the oversight of another EU Member State assessed against applicable EU requirements.

The current legal framework is Regulation (EU) 965/2012, AMC/GM to Part-ARO and the Ramp Inspection Manual (RIM). EASA states that the current checklist has **53 items**, not the 54-item count appearing in the historical 2012 SAFA v2.0 material supplied for this project. citeturn535738search2

### Historical source separation

The uploaded SAFA v2.0 material remains useful as historical/process reference for:
- preparation
- targeting
- evidence
- findings
- corrective actions
- follow-up
- database reporting

It must not be treated as the current EASA operational source. The repository therefore stores **scheme version/source metadata** rather than a single timeless SAFA rule set.

### Current programme workflow

```text
Safety information / scheduled movement
             ↓
Target selection
             ↓
Operator + aircraft preparation
             ↓
Ramp inspection
             ↓
Checklist execution
             ↓
Evidence / observations
             ↓
Finding assessment
             ↓
Category 1 / 2 / 3
             ↓
Immediate / follow-up action
             ↓
POI / debrief
             ↓
Operator + State-of-Oversight communication
             ↓
Corrective action / evidence
             ↓
Verification / reinspection
             ↓
Closure
             ↓
Central analysis / risk targeting
```

### SAFA targeting intelligence

The historical guidance identifies safety information, previous inspection results, central database information, complaints, ANSP reports, whistleblower information and State-oversight concerns as useful targeting inputs. These are ideal inputs to a risk-ranking service, but the rank must remain a recommendation for authorized inspectors. 

### Technical evidence

Ramp findings may depend on aircraft technical documentation such as AMM, SRM, CMM, WDM/SWPM, MEL and manufacturer standards. Evidence capture must therefore support document/page/reference provenance. The supplied guidance explicitly emphasizes documenting technical defects and preserving supporting evidence. fileciteturn26file1L575-L606

### Current SAFA/SACA data products

The adapter should model:
- inspection
- aircraft/operator/state
- checklist item
- standard reference
- observation
- finding category
- evidence
- POI
- communication
- operator response
- State-of-Oversight response
- corrective action
- verification
- closure

## 4. FAA Safety Assurance System pattern

FAA SAS is a strong reference architecture for authority oversight because it combines standardized policy/process with software for certification, surveillance and Continued Operational Safety and explicitly supports risk-based, data-supported inspector decisions. citeturn647973search12

Reusable patterns:
- certificate-holder profile
- risk indicators
- surveillance plan
- assessment protocols
- specialist involvement
- evidence
- findings
- COS events
- enforcement/mitigation

Do not reproduce FAA proprietary content; implement an equivalent open domain abstraction.

## 5. Transport Canada surveillance pattern

Transport Canada provides a useful model in which surveillance can include assessments/inspections, audits, Process Inspections and Targeted Inspections. This supports a common planning layer in which risk selects the surveillance type and depth.

Repository implication:

```text
Risk
 ↓
Surveillance method
 ├── Desktop assessment
 ├── Process inspection
 ├── Targeted inspection
 ├── Full inspection
 └── Audit
```

## 6. KCAA authority surveillance

KCAA's 2025 air-operator surveillance advisory circular calls for notification, entry meetings and review of operational records including ASL, AOC/Ops Specs, ATO approvals, aircraft registration, lease approvals, statistics, audited financial statements and insurance. citeturn535738search36

This leads to a KCAA inspection adapter with:
- inspection programme
- operator risk profile
- scheduled/targeted/special inspection
- entry meeting
- document request pack
- inspection checklist
- finding/CAP workflow
- follow-up
- enforcement linkage
- surveillance history

KCAA's 2025 regulatory transition further means the inspection engine should understand transition dates and progressive compliance requirements. citeturn934489search0

## 7. IOSA

IOSA is an IATA industry audit programme, not State regulatory oversight. Risk-Based IOSA tailors the audit scope to an airline's safety profile, conformity history and relevant risks and adds maturity assessment of safety-critical systems/programmes. citeturn535738search39turn535738search40

The adapter should therefore model:
- audit programme
- operator profile
- risk-scoping decisions
- ISARP/control set version
- sample/evidence plan
- conformity assessment
- maturity assessment
- findings
- corrective actions
- registration lifecycle

## 8. ISAGO

ISAGO is IATA's global programme for ground handling service providers. It has headquarters/station auditing and discipline-specific operational coverage. The adapter should keep industry audit semantics separate from regulatory surveillance.

Recommended model:
- GHSP profile
- HQ assessment
- station assessment
- discipline
- checklist/version
- evidence
- finding/CAP
- registration/accreditation lifecycle

## 9. Other inspection adapters

The generic engine should support:

### Airworthiness / maintenance
- aircraft condition
- approved technical data
- maintenance records
- MEL/AMP/AD linkage
- repeat defects
- component traceability

### Aerodrome / AGA
- runway/taxiway
- markings/lighting
- rescue/firefighting
- obstacles
- facilities
- safety management
- published aerodrome data

### PEL
- licence
- ratings
- recency/currency
- training
- medical evidence
- examiner/ATO records

### AMO / CAMO / ATO
- scope
- facilities
- personnel
- manuals
- quality/compliance monitoring
- SMS
- records
- competence

### Dangerous Goods
- acceptance
- packaging
- documentation
- loading/stowage
- training
- quantity/limitation checks

### Security
- controlled access
- confidential evidence
- airport/entity security controls
- corrective actions

### ANS / CNS / AIS
- procedures
- systems
- technical capability
- service performance
- data quality
- occurrence integration

## 10. Generic scheme interface

```text
IInspectionScheme
  getCriteria(version)
  getTargetingRules(version)
  getChecklist(version)
  assessObservation(input)
  categorizeFinding(input)
  determineActions(input)
  getFollowUpRules(version)
  getReportSchema(version)
```

The core platform owns case management, evidence, workflow, notifications, permissions and audit. The adapter owns scheme-specific criteria and decisions.

## 11. AI opportunities

### Targeting
Combine risk, history, exposure and current information to propose targets.

### Briefing
Generate evidence-linked pre-inspection briefs.

### Checklist prioritisation
Rank items under constrained time while respecting mandatory coverage.

### Evidence assistant
Link photos, documents and notes to items and standards.

### Finding assistant
Retrieve the applicable standard and propose structured finding text/category; inspector confirms.

### Recurrence / systemic detection
Cluster by operator, aircraft, fleet, ATA chapter, location, process or organisation.

### CAP quality
Check proposed actions for relation to finding, evidence, root cause and recurrence.

### Oversight intelligence
Aggregate findings into operator/fleet/State trends.

## Key safety boundary

```text
Observation
   ↓
Assessment
   ↓
Finding
   ↓
Categorisation
   ↓
Action
   ↓
Closure
```

AI may assist each stage. It must not silently turn an observation into an authoritative finding, enforcement action or airworthiness decision.