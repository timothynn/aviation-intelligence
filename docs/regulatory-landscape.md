# Aviation Regulatory Landscape

This document defines the regulatory model that Aviation Intelligence is designed to represent. It is intentionally an engineering abstraction, not legal advice.

## 1. Global baseline: ICAO

The Chicago Convention establishes the international framework for civil aviation. ICAO develops Standards and Recommended Practices (SARPs) in 19 Technical Annexes and Procedures for Air Navigation Services (PANS). ICAO states that its framework contains more than 12,000 SARPs across the 19 Annexes and five PANS families.

Aviation Intelligence should therefore treat ICAO as the **global reference layer**, rather than as a substitute for national law.

### ICAO Annex-to-skill map

| Annex | Domain | Candidate software skills |
| --- | --- | --- |
| 1 Personnel Licensing | Licences, ratings, medical/competency | licence lifecycle, eligibility rules, training records |
| 2 Rules of the Air | Operating rules | rule engines, route/airspace validation |
| 3 Meteorological Service | MET information | weather ingestion, alerting, data quality |
| 4 Aeronautical Charts | Charts | geospatial validation, chart data processing |
| 5 Units of Measurement | Aviation units | unit normalization and conversion |
| 6 Operation of Aircraft | Flight operations | AOC, Ops Specs, FDM, manuals, flight-time rules |
| 7 Nationality & Registration Marks | Registration | aircraft identity and registry services |
| 8 Airworthiness | Design/certification/continuing airworthiness | certificate management, AD/SB tracking, maintenance compliance |
| 9 Facilitation | Passenger/cargo/immigration facilitation | document workflows, API/PNR data, border-process automation |
| 10 Aeronautical Telecommunications | CNS and communications | surveillance, communication, interoperability/data standards |
| 11 Air Traffic Services | ATS/ATM | flight data, airspace, surveillance, operational decision support |
| 12 Search and Rescue | SAR | incident workflow, geospatial dispatch, resource coordination |
| 13 Accident/Incident Investigation | Investigation | occurrence ingestion, evidence, causal analysis, investigation workflow |
| 14 Aerodromes | Airport/heliport design and operations | aerodrome certification, inspections, obstacle/data management |
| 15 Aeronautical Information Services | AIS/AIM | AIP data, NOTAM workflows, data validation, digital AIM |
| 16 Environmental Protection | Noise, emissions, CORSIA | emissions analytics, reporting, compliance workflows |
| 17 Aviation Security | Security | access/control workflows, risk analytics, security compliance |
| 18 Dangerous Goods | Dangerous goods | classification, acceptance checks, shipment compliance |
| 19 Safety Management | SSP/SMS/safety intelligence | hazard, occurrence, risk, KPI and assurance tooling |

ICAO Annex 6 is especially important to operator-facing systems because it addresses flight operations, operating limitations, aircraft equipment, navigation/communication equipment, maintenance, crew, dispatch, manuals, records, cabin crew, security and flight/duty limitations. Annex 8 provides the international airworthiness baseline but explicitly recognizes that detailed national airworthiness codes remain necessary.

## 2. The national/regional implementation pattern

The core design pattern is:

```text
Chicago Convention
      ↓
ICAO SARPs / PANS / guidance
      ↓
Regional or national legal framework
      ↓
Implementing regulations / rules
      ↓
Acceptable Means of Compliance / advisory material / guidance
      ↓
Approvals, certificates, authorizations and declarations
      ↓
Oversight: surveillance, audits, inspections, findings
      ↓
Corrective action / enforcement / safety intelligence
```

This is the most important domain abstraction for the repository.

## 3. EASA / European Union

EASA operates within the EU legal framework. Regulation (EU) 2018/1139 (the Basic Regulation) establishes EASA and the common aviation-safety framework. Detailed delegated and implementing regulations cover areas including airworthiness, aircrew, air operations, ATM/ANS, aerodromes, ground handling and unmanned aircraft.

EASA's **Easy Access Rules** are particularly useful as a machine-readable engineering target. Current EASA publications include XML as well as PDF and online versions. The Air Operations Easy Access Rules consolidate regulation, AMC, GM and related certification material across Part-ARO, Part-ORO, Part-CAT, Part-SPA, Part-NCC, Part-NCO, Part-SPO and Part-IAM.

Recommended EASA skills:

- rule/AMC/GM relationship extraction
- machine-readable regulation ingestion
- AOC and Operations Specification modeling
- specific approval management: PBN, RVSM, LVO, dangerous goods, etc.
- Part-CAMO / Part-145 / continuing-airworthiness intelligence
- occurrence reporting
- information-security risk compliance
- third-country operator intelligence
- aerodrome compliance
- UAS regulatory decision support

## 4. FAA / United States

The FAA expresses requirements primarily through Title 14 of the Code of Federal Regulations (14 CFR), supported by policy, advisory circulars, orders, notices and other guidance.

Important software-relevant areas include:

- Part 21: type, production and airworthiness certification
- Part 39: Airworthiness Directives
- Part 121: scheduled air carrier operations
- Part 135: commuter/on-demand operations
- Part 141: pilot schools
- Part 145: repair stations
- Part 5: Safety Management Systems
- UAS rules and certification pathways

The FAA pattern reinforces a key repository requirement: **rules, guidance, certificates, surveillance and corrective actions must be represented separately but linked**.

## 5. Transport Canada Civil Aviation

The Canadian Aviation Regulations (CARs) use a structured Part system. Examples include Part I general provisions and SMS requirements, Part II aircraft identification and registration, Part III aerodromes/airports/maintenance organizations, Part V airworthiness, Part VI general operating/flight rules and Part VII commercial air services.

Recommended skills:

- regulation Part/Subpart/section parsing
- certificate and approval management
- SMS data processing
- AMO and operator compliance
- aircraft registration linkage
- airworthiness directive tracking

## 6. UK Civil Aviation Authority

The UK CAA maintains a post-EU-exit UK aviation regulatory framework incorporating UK legislation, UK regulations and CAA decisions/guidance. The structure remains recognizably EASA-derived in several areas, but the source of legal authority and the current UK-specific applicability must always be modeled.

Software implications:

- jurisdiction-aware rule resolution
- UK-specific versioning and legal status
- Part-21 / Part-145 / Part-CAMO-style structures
- UK CAA decisions and AMC/GM linkage
- occurrence reporting and SMS
- regulatory-change monitoring

## 7. Kenya Civil Aviation Authority

KCAA is particularly important as an initial reference jurisdiction for this project. Its public regulatory framework includes regulations for AOC certification and administration, airworthiness, personnel licensing, AMOs, approved training organizations, safety management, aircraft registration, commercial air transport, aerodromes, ATS, AIS, communications, navigation, surveillance, dangerous goods and UAS.

KCAA also publishes Advisory Circulars and technical publications. In 2025 KCAA announced a revised set of 29 Civil Aviation Regulations, with additional regulations pending publication, demonstrating why the repository needs **regulatory versioning and effective-date awareness** rather than a static rules database.

Recommended KCAA skills:

- AOC certification workflow
- ASL / air service licensing workflow
- aircraft registration and airworthiness linkage
- AMO / ATO certification
- personnel licensing
- safety management and occurrence reporting
- aerodrome certification
- ANS/CNS/AIS compliance
- UAS approvals
- inspection/audit findings
- regulatory migration/version comparison

## 8. CASA Australia

CASA uses the Civil Aviation Safety Regulations (CASR) framework alongside Civil Aviation Regulations (CAR), airworthiness directives and advisory material. CASA's airworthiness material illustrates another reusable pattern: ADs can have affected products, effective dates, review mechanisms and AMOCs.

This maps directly to reusable Aviation Intelligence skills for regulatory change detection, applicability resolution and compliance evidence.

## 9. Cross-authority engineering abstraction

Do not model every regulator as a separate application. Model authorities using a common schema:

```text
Authority
 ├── Jurisdiction
 ├── LegalFramework
 ├── Regulation
 │    ├── Part / Chapter / Subpart
 │    ├── Section / Paragraph
 │    ├── EffectiveDate
 │    ├── ApplicabilityDate
 │    └── Status
 ├── Guidance
 │    ├── AMC
 │    ├── GM
 │    ├── AdvisoryCircular
 │    └── Policy / Decision
 ├── Approval
 │    ├── Certificate
 │    ├── Authorisation
 │    ├── Declaration
 │    └── SpecificApproval
 ├── Oversight
 │    ├── Audit
 │    ├── Inspection
 │    ├── Finding
 │    └── CorrectiveAction
 └── Enforcement
```

## 10. Regulatory change intelligence

This should become one of the project's flagship capabilities.

The engine should detect:

- new regulations
- amendments
- applicability-date changes
- revoked/superseded rules
- guidance changes
- new AMC/GM
- changed forms
- affected approvals
- affected system workflows

Example output:

```text
Regulatory Change
        ↓
Identify affected rules
        ↓
Resolve affected approvals
        ↓
Find affected organizations/applications
        ↓
Estimate compliance impact
        ↓
Create review tasks
        ↓
Human validation
```

## 11. Important disclaimer

Regulatory content in this repository should be treated as a technical knowledge representation. It must never be presented as authoritative legal advice or as a substitute for the current source publication from the applicable authority.

## Sources

- ICAO SARPs: https://www.icao.int/safety-management/standards-and-recommended-practices-sarps
- ICAO Annexes: https://store.icao.int/en/annexes
- ICAO Airworthiness: https://www.icao.int/airworthiness-aircraft
- EASA Basic Regulation: https://www.easa.europa.eu/en/faq/19107
- EASA Easy Access Rules: https://www.easa.europa.eu/en/document-library/easy-access-rules
- EASA Air Operations: https://www.easa.europa.eu/en/document-library/easy-access-rules/easy-access-rules-air-operations
- FAA: https://www.faa.gov/
- Transport Canada CARs: https://tc.canada.ca/en/aviation
- UK CAA: https://www.caa.co.uk/
- KCAA Aviation Regulations: https://kcaa.or.ke/legislation-publications/aviation-regulations
- KCAA 2025 Regulations Notice: https://www.kcaa.or.ke/published-regs-2025
- CASA: https://www.casa.gov.au/
