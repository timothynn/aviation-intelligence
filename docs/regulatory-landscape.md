# Aviation Regulatory Landscape

This document defines the engineering model Aviation Intelligence uses to represent aviation regulation. It is not legal advice and does not replace current authority publications.

## 1. Regulatory hierarchy

```text
Chicago Convention
       ↓
ICAO SARPs / PANS / guidance
       ↓
Regional / national legal framework
       ↓
Regulations / rules / implementing measures
       ↓
AMC / GM / advisory circulars / policy / decisions
       ↓
Certificates / approvals / authorizations / declarations
       ↓
Surveillance / inspections / audits
       ↓
Findings / corrective actions / enforcement
       ↓
Safety information / safety intelligence
```

The core software rule is that a requirement is never just a text string. It must carry **authority, jurisdiction, version, status, effective/applicability dates, provenance, applicability criteria and relationships**.

## 2. ICAO global baseline

ICAO remains the global reference layer. Its SARPs are organized through 19 Annexes, complemented by PANS and other guidance. Annex 19 and the modern safety-management framework now put greater emphasis on safety data, information and safety intelligence.

### Annex-to-skill map

| Annex | Domain | Software capabilities |
|---|---|---|
| 1 | Personnel Licensing | licence/rating lifecycle, eligibility, training/competency |
| 2 | Rules of the Air | rules engine, operational validation |
| 3 | Meteorology | MET ingestion, normalization, alerts |
| 4 | Charts | chart/data validation, geospatial services |
| 5 | Units | aviation units and conversion |
| 6 | Operations | AOC, Ops Specs, manuals, FDM, crew/time limits |
| 7 | Registration | aircraft registry, ownership/registration lifecycle |
| 8 | Airworthiness | certification, continuing airworthiness, AD compliance |
| 9 | Facilitation | passenger/cargo facilitation workflows |
| 10 | Telecom | CNS, communications, interoperability |
| 11 | ATS | ATM/ATS operational intelligence |
| 12 | SAR | incident workflow, resource coordination |
| 13 | Accident/Incident Investigation | evidence, investigation, causal-analysis support |
| 14 | Aerodromes | certification, inspections, facilities/data |
| 15 | AIS | AIP, NOTAM, AIM and digital information |
| 16 | Environment | emissions/noise/CORSIA analytics |
| 17 | Security | security compliance and controlled evidence |
| 18 | Dangerous Goods | classification, acceptance and compliance |
| 19 | Safety Management | SSP/SMS, hazards, risk, SPIs and safety intelligence |

For this repository, Annex 6, 8, 13, 14, 15, 18 and 19 are especially important because they connect directly to operational systems, evidence, inspections, airworthiness, information management and safety intelligence.

## 3. ICAO USOAP CMA / State oversight

USOAP CMA is a **continuous, risk-based monitoring model**, not simply a periodic audit. ICAO uses eight Critical Elements and standardized Protocol Questions to assess State safety-oversight capability. The eight broad audit areas are LEG, ORG, PEL, OPS, AIR, AIG, ANS and AGA. ICAO also introduced SSP-related integrated assessment work through SSPIA.

Engineering implications:

```text
State profile
 → applicable PQ set
 → evidence
 → assessment
 → effective implementation / maturity
 → findings
 → corrective action
 → continuous monitoring
```

The model therefore needs question/version management, evidence requests, State submissions, assessment history, findings and longitudinal analytics.

## 4. EASA / European Union

EASA operates inside the EU legal framework established by Regulation (EU) 2018/1139. A major engineering opportunity is EASA's **eRules / Easy Access Rules** ecosystem.

Current 2026 evidence shows that Air Operations Revision 24 from March 2026 is published as PDF, enhanced online content and machine-readable XML. EASA explicitly states that the XML can be processed and synchronized with local applications and databases, and that eRules are regularly updated. citeturn647973search0turn647973search6

The current EASA library also includes 2026 revisions for Air Operations, Aerodromes, Third Country Operators and other rule families, while future applicability dates are explicitly marked in the online rules. citeturn647973search2turn647973search3turn647973search8

This leads to a concrete repository requirement:

```text
Rule article
 ├── source regulation / decision
 ├── amendment provenance
 ├── AMC / GM relationships
 ├── applicability date
 ├── jurisdiction
 ├── version
 └── machine-readable representation
```

Priority EASA adapters:
- Air Operations / AOC / Ops Specs
- Specific Approvals
- TCO
- Aircrew
- Initial / Continuing Airworthiness
- Aerodromes
- ATM/ANS
- Ground Handling
- Information Security
- Occurrence Reporting
- UAS / SORA

## 5. FAA / United States

The FAA's regulatory model is based primarily on 14 CFR plus policy, advisory circulars, orders and other guidance. For software architecture, the most important lesson is the FAA **Safety Assurance System (SAS)**: a standardized, risk-based and data-supported oversight system used for certification, surveillance and Continued Operational Safety, with software supporting inspector data capture and oversight decisions. citeturn647973search12

The repository should therefore model:

```text
Certificate Holder
 → Risk Profile
 → Oversight Plan
 → Certification / Surveillance / COS
 → Protocol / Assessment
 → Finding
 → Corrective action
 → Reassessment
```

This is a reference pattern for authority-side inspection software, not a proposal to reproduce FAA proprietary software.

## 6. Transport Canada

Transport Canada provides another strong risk-based oversight pattern. Its surveillance model can be represented around assessments/inspections, audits, enforcement, **Process Inspections** and **Targeted Inspections**, with risk used to select the level and focus of surveillance.

Engineering implication: make inspection planning a separate service from checklist execution so that risk-based targeting can be reused across schemes.

## 7. UK Civil Aviation Authority

The UK CAA maintains UK-specific legislation, regulations, CAA decisions and guidance. The architecture must treat UK applicability as its own jurisdiction rather than assuming that EASA-derived structures have identical legal effect.

Priority skills:
- jurisdiction-aware rule resolution
- legal-status/version tracking
- Part-21/145/CAMO-style approval models
- SMS and management-of-change oversight
- regulatory change analysis

## 8. CASA Australia

CASA's CASR/CAR ecosystem provides another useful adapter pattern for rule hierarchy, airworthiness directives, approvals and applicability. The reusable pattern is the same: rule → applicability → affected entity/product → compliance evidence → closure.

## 9. Kenya Civil Aviation Authority

KCAA is the first complete reference jurisdiction for Aviation Intelligence.

KCAA's 2025 regulatory transition is especially important: KCAA published **29 revised Civil Aviation Regulations** and requires stakeholders to review them, align operations/systems/procedures, revise relevant manuals/documentation and train personnel. KCAA states that existing certificates/licences/approvals generally continue subject to transitional requirements and that enhanced surveillance, inspections and audits will be used during implementation. KCAA also lists **nine additional revised regulations pending Gazette publication**. citeturn934489search0

This means the KCAA adapter must support:

```text
Current Regulation
     ↓
Transition provision
     ↓
Existing approval
     ↓
Progressive compliance
     ↓
Manual / procedure amendment
     ↓
Inspection / audit
     ↓
Final alignment
```

KCAA Flight Operations and surveillance material also supports an extensible approval model because the Authority handles AOC renewal/recertification, surveillance, amendments and special approvals such as PBN, RVSM, LVO and EDTO. The inspection/surveillance advisory circular calls for an entry meeting and review of items including ASL, AOC/Ops Specs, ATO approvals, aircraft registration, leases, statistics, audited financial statements and insurance. citeturn535738search36

Priority KCAA adapters:
- Organization / registry
- ASL / AOC
- Ops Specs / specific approvals
- Aircraft registration / airworthiness
- AMO / ATO / CAMO-style approvals
- Personnel licensing
- Aerodrome certification
- ANS/CNS/AIS
- UAS
- Safety management / SSP
- Surveillance / inspection / enforcement
- Fees and service payments

## 10. Cross-authority abstraction

```text
Authority
 ├── Jurisdiction
 ├── LegalFramework
 ├── Instrument
 │    ├── Regulation
 │    ├── Rule
 │    ├── Guidance
 │    ├── Decision
 │    └── AdvisoryCircular
 ├── Version
 │    ├── publishedAt
 │    ├── effectiveFrom
 │    ├── applicableFrom
 │    ├── effectiveTo
 │    └── supersedes
 ├── Requirement
 ├── Approval
 ├── Oversight
 └── Enforcement
```

## 11. Regulatory change intelligence

The regulatory-change engine is a core platform capability:

```text
Source monitor
 → fingerprint
 → structural diff
 → semantic diff
 → changed requirements
 → applicability resolution
 → affected approvals / workflows / organizations
 → impact assessment
 → review task
 → human validation
```

Change types:
- new
- amended
- corrected
- superseded
- withdrawn
- reissued
- future applicability
- temporary transition
- guidance-only
- form/template change

## 12. Source hierarchy

For regulated use, the engine should prefer:

1. Applicable law/regulation
2. Competent-authority rule/decision
3. Official AMC/GM/advisory material
4. Official authority guidance
5. Recognized international standard/guidance
6. Industry programme material
7. Secondary commentary

The source hierarchy must be stored as metadata and should influence retrieval and confidence.

## Sources

- ICAO Safety Intelligence: https://www.icao.int/safety-management/SMI/SI
- ICAO USOAP FAQ: https://www.icao.int/usoap/frequently-asked-questions-about-usoap
- EASA Easy Access Rules Air Operations: https://www.easa.europa.eu/en/document-library/easy-access-rules/easy-access-rules-air-operations
- EASA Ramp Inspection Programmes: https://www.easa.europa.eu/en/domains/air-operations/ramp-inspection-programmes-safa-saca
- FAA Safety Assurance System: https://www.faa.gov/about/initiatives/sas
- KCAA Regulations 2025: https://www.kcaa.or.ke/published-regs-2025
- KCAA Safety Performance Measurement: https://www.kcaa.or.ke/safety-security-oversight/aviation-safety/safety-performance-measurement
- KCAA Air Operator Surveillance AC-ATD012A: https://mail.kcaa.or.ke/sites/default/files/circulars/AC%20-%20Surveillance%20and%20inspection%20of%20air%20operators.pdf
- Transport Canada: https://tc.canada.ca/en/aviation
- UK CAA: https://www.caa.co.uk/
- CASA: https://www.casa.gov.au/
