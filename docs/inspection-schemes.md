# Inspection Scheme Adapter Matrix

The generic inspection platform provides common lifecycle, evidence, workflow and audit services. Scheme adapters supply the scheme-specific criteria, targeting, categorisation, reporting and follow-up rules.

| Scheme / domain | Nature | Primary subject | Criteria source | Core software model |
|---|---|---|---|---|
| SAFA | Ramp inspection | Third-country aircraft/operators | ICAO standards + EU framework + RIM + manufacturer/national standards as applicable | Targeting, 53-item current checklist, findings, actions, follow-up |
| SACA | Ramp inspection | Operators under another EU State oversight | EU requirements + RIM | Jurisdiction-aware standards, findings, follow-up |
| USOAP CMA | State oversight audit/monitoring | States / CAAs | ICAO SARPs, PQs, PANS/guidance | PQs, evidence, EI, CEs, corrective actions, continuous monitoring |
| EASA Standardisation | Authority oversight | National aviation authorities | EU aviation framework / EASA standards | Continuous monitoring, maturity, inspections, findings |
| FAA SAS-style oversight | Authority surveillance | Certificate holders | 14 CFR + FAA policy/protocols | Risk profile, certification, surveillance, COS, assessment |
| KCAA authority surveillance | Regulatory surveillance | Operators / approval holders | KCAA regulations + procedures | Planned/targeted/special inspections, evidence, CAP, enforcement |
| Airworthiness | Inspection/surveillance | Aircraft / maintenance orgs | Applicable airworthiness rules + approved technical data | AD/AMP/MEL/data linkage, defects, repeat findings |
| Aerodrome / AGA | Inspection/surveillance | Airports / aerodromes | Annex 14 + national framework | Movement area, rescue/fire, facilities, obstacles, data |
| PEL | Inspection/licensing | Personnel | Licensing regulations | Licence, rating, currency, training, medical evidence |
| AMO/CAMO/ATO | Organization inspection/audit | Approved organizations | Organization approval rules | Scope, facilities, personnel, manuals, quality/SMS |
| IOSA | Industry audit | Airline | IATA ISARPs | Risk-scoped audit, conformity, maturity, corrective actions |
| ISAGO | Industry audit | Ground handling service provider | IATA GOSARPs / programme rules | HQ/station audit, disciplines, findings, registration |
| Dangerous Goods | Inspection | Operator / cargo / handler | Annex 18 + Technical Instructions + national rules | Documentation, packaging, acceptance, loading/handling |
| Security | Inspection/audit | Airport / operator / regulated entity | Annex 17 + national security programme | Controlled evidence, access/security controls |
| ANS/CNS/AIS | Inspection/surveillance | ANSP / service provider | Annexes 10/11/15 + national framework | Procedures, systems, technical controls, data quality |

## 1. Current SAFA/SACA adapter

EASA's current programme uses 53 ramp-inspection items. The programme is governed by Regulation (EU) 965/2012, AMC/GM to Part-ARO and the Ramp Inspection Manual. SAFA applies to third-country operators; SACA applies to operators under the oversight of another EU Member State. citeturn535738search2

The supplied historical SAFA v2.0 PDF uses the older 54-item model. It must remain a historical dataset/reference, not the current RIM.

## 2. USOAP-style adapter

USOAP CMA uses eight Critical Elements and Protocol Questions; it is a continuous, risk-based activity rather than a one-off audit. citeturn535738search5

Adapter objects:

```text
AuditArea
CriticalElement
ProtocolQuestion
EvidenceRequirement
StateResponse
Assessment
EI / Maturity
Finding
CorrectiveAction
FollowUp
```

## 3. Authority-surveillance adapter

The authority adapter should support:

```text
Risk Profile
 → Surveillance Programme
 → Target Selection
 → Inspection Type
 → Checklist / Protocol
 → Finding / Assessment
 → CAP / Enforcement
 → Verification
```

FAA SAS and Transport Canada surveillance are useful architecture references because both emphasize risk-informed/data-supported oversight rather than uniform inspection frequency. citeturn647973search12

## 4. KCAA adapter

The KCAA adapter must support 2025 regulatory transition states and inspection/surveillance evidence. KCAA published 29 revised regulations and says enhanced surveillance, inspections and audits will support implementation; nine additional regulations were pending Gazette publication at the time of the notice. citeturn934489search0

## 5. Industry audit adapters

IOSA and ISAGO are not government regulatory schemes. They must use the same platform primitives but separate legal authority, criteria, confidentiality and outcome semantics.

Risk-Based IOSA is explicitly scoped around operator-specific safety risks, history and maturity. citeturn535738search39turn535738search40

## 6. Generic interface

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

## 7. Adapter boundary

### Platform owns

```text
Case
Workflow
Evidence
Observation
Finding container
CorrectiveAction container
Verification
Notifications
Audit events
Permissions
```

### Scheme owns

```text
Criteria
Checklist
Targeting logic
Categorisation
Action mapping
Follow-up rules
Reporting format
Scheme-specific references
```

This boundary is required to keep KCAA, SAFA, SACA, USOAP, IOSA and ISAGO extensible without duplicating the whole inspection platform.