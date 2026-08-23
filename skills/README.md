# Aviation AI Skills

Skills are the core reusable capabilities of Aviation Intelligence. Each skill should solve one focused aviation engineering problem and be independently understandable, testable and reusable.

## Skill contract

Every mature skill should document:

1. **Purpose** — the aviation problem being solved.
2. **Domain references** — relevant ICAO Annexes, regulations, authority material or standards.
3. **Inputs** — data, documents or events it accepts.
4. **Outputs** — structured results and confidence/evidence where relevant.
5. **Architecture** — components and dependencies.
6. **Implementation** — production-oriented code, not only a notebook.
7. **Evaluation** — aviation/domain-specific tests and AI metrics.
8. **Assurance** — traceability, human review, limitations and failure modes.

## Catalogue

### Foundation

- `aviation-domain-model` — common aviation entities, identifiers and relationships.
- `aviation-data-engineering` — schemas, validation, provenance and synthetic data.
- `aviation-document-intelligence` — PDF, DOCX, OCR, XML, layout and metadata extraction.
- `aviation-entity-resolution` — aircraft, operators, airports, people, certificates and identifiers.

### Regulatory & compliance

- `regulatory-intelligence` — authority/rule/requirement knowledge layer.
- `regulatory-change` — amendment detection, versioning and compliance impact.
- `aviation-rag` — evidence-backed regulatory and operational retrieval.
- `compliance-assurance` — requirement-to-evidence mapping and gap analysis.
- `aviation-knowledge-graph` — graph of regulations, organizations, aircraft, approvals and findings.

### Certification & approvals

- `air-operations-approvals` — AOC and operational-approval lifecycle.
- `airworthiness-certification` — aircraft/product certification intelligence.
- `personnel-licensing` — licence, rating, training and competency workflows.
- `ato-amo-camo-certification` — organization approval lifecycle.
- `aerodrome-certification` — airport/heliport certification and surveillance.

### Operations & oversight

- `workflow-intelligence` — bottlenecks, next actions and workflow analytics.
- `inspection-intelligence` — risk-based inspection preparation, findings and follow-up.
- `safa-ramp-intelligence` — ramp inspection preparation, finding support and trend analysis.
- `safety-intelligence` — hazards, occurrences, risk indicators and safety performance.
- `occurrence-intelligence` — classification, correlation and investigation support.
- `audit-intelligence` — audit planning, evidence, findings and corrective actions.

### Airworthiness & maintenance

- `airworthiness-maintenance` — maintenance, defects, components and continuing airworthiness.
- `airworthiness-directives` — AD ingestion, applicability and compliance tracking.
- `reliability-intelligence` — fleet/component reliability analysis.
- `predictive-maintenance` — anomaly detection and remaining-useful-life research.

### Flight / ATM / aeronautical information

- `flight-data-intelligence` — schedules, trajectories and operational analytics.
- `flight-risk-intelligence` — operational risk indicators and decision support.
- `aeronautical-information` — AIP, NOTAM and AIM processing.
- `weather-intelligence` — METAR, TAF, SIGMET and weather-data fusion.
- `atm-ans-intelligence` — airspace, ATS, CNS, surveillance and ATM decision support.
- `airport-operations` — runway, stand, turnaround and airport-event intelligence.

### AI / ML capabilities

- `aviation-nlp`
- `aviation-speech`
- `aviation-computer-vision`
- `anomaly-detection`
- `forecasting`
- `classification`
- `risk-modeling`
- `aviation-agents`

### Assurance & governance

- `human-in-the-loop`
- `ai-evaluation`
- `ai-groundedness`
- `ai-explainability`
- `ai-confidence`
- `ai-audit-trail`
- `ai-safety-guardrails`
- `ai-security`
- `ai-model-monitoring`
- `data-provenance`

## Initial implementation priority

```text
P0  Aviation Domain Model
P0  Regulatory Intelligence
P0  Document Intelligence
P0  Aviation RAG
P0  Compliance Assurance
P1  Air Operations & Approvals
P1  Inspection Intelligence
P1  Safety Intelligence
P1  Airworthiness & Maintenance
P1  Regulatory Change Intelligence
P2  Aviation Knowledge Graph
P2  Aviation Agents
P2  Predictive Maintenance
P2  Computer Vision
P2  Weather / Flight Intelligence
P3  Advanced autonomy and optimization research
```

## Contribution rule

A new skill should be narrow enough to explain in one README and broad enough to be reused by more than one aviation application. Avoid creating skills that are merely wrappers around a single vendor API.
