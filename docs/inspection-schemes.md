# Inspection Scheme Adapter Matrix

| Scheme / domain | Nature | Primary subject | Criteria source | Key software needs |
|---|---|---|---|---|
| SAFA | Ramp inspection | Foreign / third-country aircraft/operators | ICAO / EU / manufacturer / published national standards as applicable | Targeting, 54-item legacy mapping, findings, action classes, follow-up |
| SACA | Ramp inspection | EU operator under another EU State oversight | EU requirements | Jurisdiction-aware standards, findings, follow-up |
| USOAP CMA | State oversight audit | States / CAA systems | ICAO SARPs, PANS, guidance / protocol questions | PQs, evidence, EI, audit areas, CEs, CAPs |
| Authority surveillance | Regulatory inspection/audit | Certificate / approval holders | National regulations and authority procedures | Risk-based plan, inspections, findings, enforcement |
| IOSA | Industry audit | Airline | IOSA standards | Risk-based scope, evidence, maturity, corrective actions |
| ISAGO | Industry audit | GHSP | IATA ground-operation standards | HQ/station audit, discipline checklists, registration/accreditation |
| Airworthiness | Inspection/surveillance | Aircraft / maintenance organizations | Airworthiness rules + approved technical data | Technical evidence, AD/AMP/MEL linkage, repeat defects |
| Aerodrome | Inspection/surveillance | Airport / aerodrome | Annex 14 and national requirements | Movement-area checks, facilities, findings |
| PEL | Inspection / licensing | Personnel | Licensing regulations | Licence evidence, ratings, currency, competence |
| ATO/AMO/CAMO | Organization audit/inspection | Approved organization | Organization approval rules | Scope, facilities, personnel, manuals, quality/SMS evidence |
| Safety / SMS | Audit / assurance | Organization / State | Annex 19 + applicable rules | Safety performance, risk controls, assurance |
| Dangerous goods | Inspection | Operator / cargo / handling | Annex 18 and applicable technical instructions | Documentation, packaging, handling, findings |
| Security | Inspection / audit | Aircraft / airport / entity | Annex 17 + national security programme | Controlled access, confidential evidence, findings |

## Adapter rule

Each scheme should implement the generic interfaces:

```text
IInspectionScheme
  getCriteria(version)
  getTargetingRules(version)
  getChecklist(version)
  assessObservation(input)
  categorizeFinding(input)
  determineActions(input)
  getFollowUpRules(version)
```

The adapter owns scheme-specific rules; the platform owns generic case, workflow, evidence, notification and audit primitives.