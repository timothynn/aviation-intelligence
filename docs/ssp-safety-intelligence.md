# State Safety Programme and Safety Intelligence

## 1. Current direction

The SSP module should be treated as a State-level management and intelligence system, not simply a dashboard.

ICAO's 2025 Safety Intelligence Manual (Doc 10159) expands guidance on collecting, processing, analysing and applying safety data and safety information and supports the enhanced Annex 19 safety-intelligence provisions. citeturn535738search0turn535738search1

The 2026–2028 Global Aviation Safety Plan places emphasis on SSP implementation, safety data collection and processing systems and protection of safety data/information. citeturn535738search37turn535738search38

## 2. SSP operating model

```text
State aviation system
        ↓
Safety policy / objectives / resources
        ↓
Safety data & information
        ↓
Hazards / risks / safety issues
        ↓
Controls / mitigations
        ↓
Safety assurance
        ↓
Safety performance
        ↓
Safety promotion
        ↺
Continuous improvement
```

## 3. SSP modules

### Governance
- accountable authority
- participating government/aviation organizations
- roles and responsibilities
- safety policy
- objectives
- resources
- legal framework
- governance decisions

### State Safety Risk Management
- hazards
- threats
- safety issues
- risk assessments
- controls/mitigations
- residual risk
- risk acceptance
- risk register

### State Safety Assurance
- certification results
- surveillance programme
- inspections
- audits
- findings
- corrective actions
- occurrence information
- SPIs / SPTs
- State oversight capability
- effectiveness of controls

### Safety Promotion
- training
- safety publications
- campaigns
- stakeholder engagement
- lessons learned
- safety communication

## 4. Safety data collection and processing system

Model the SDCPS as an explicit platform capability:

```text
Sources
 ├── Occurrence reports
 ├── Inspections
 ├── Audits
 ├── Flight data
 ├── Maintenance
 ├── Airport events
 ├── ATS/ANS events
 ├── Complaints
 ├── Confidential reports
 └── Other safety data
        ↓
Data ingestion
        ↓
Validation / normalization
        ↓
Protection / classification
        ↓
Analysis
        ↓
Safety intelligence
        ↓
Decision / action
```

ICAO's current safety-intelligence direction explicitly links collection, processing, analysis, sharing and exchange of safety data/information. citeturn934489search3

## 5. KCAA safety intelligence

KCAA's Safety Performance Measurement service says SPIs are based on data from multiple sources, should be linked to safety objectives, and should identify who collects, validates, monitors and acts on the indicator. KCAA also operationalizes online SPI submissions through its eServices portal. citeturn934489search1

The repository should therefore model:

```text
SPI
 ├── definition
 ├── purpose
 ├── formula
 ├── unit
 ├── owner
 ├── source(s)
 ├── validation rule
 ├── frequency
 ├── target
 ├── alert threshold
 └── action rule
```

KCAA publishes State-level indicators across flight operations, maintenance, ATO, aerodrome and ATS domains. citeturn934489search1

## 6. NASP alignment

The Kenya National Aviation Safety Plan (NASP) provides another useful reference for a State-level safety-information implementation, including safety performance measures, safety-data protection and system-level initiatives. citeturn934489search2

The project should model a State safety plan as:

```text
Safety Goal
 ↓
Target
 ↓
Safety Enhancement Initiative
 ↓
Owner
 ↓
Indicator
 ↓
Milestone
 ↓
Evidence
 ↓
Status
```

## 7. Safety intelligence analytics

### Occurrence intelligence
- classify occurrence narratives
- extract event entities
- preserve original narrative
- assign confidence
- identify repeated patterns

### Hazard clustering
Cluster occurrences, findings, inspections, maintenance events and reports into candidate hazard families.

### Emerging risk detection
Monitor changes in:
- frequency
- severity
- recurrence
- exposure
- geography
- operator
- aircraft type
- aerodrome
- phase of flight
- system/ATA chapter

### SPI analytics
- trend analysis
- control-chart style monitoring
- forecast with confidence intervals
- threshold alerts
- data quality checks
- denominator/exposure validation

## 8. Authority oversight integration

USOAP CMA and State oversight data should feed SSP rather than live in a disconnected subsystem. ICAO describes USOAP CMA as a continuous risk-based mechanism using current information to prioritize monitoring activities. citeturn535738search5

Recommended integration:

```text
USOAP / Authority Oversight
        +
Certification
        +
Inspections / Audits
        +
Occurrences
        +
SPIs
        +
Safety Issues
        ↓
State Safety Intelligence
```

## 9. Safety information protection

Model explicit classifications such as:

```text
PUBLIC
OPERATIONAL
CONFIDENTIAL
PROTECTED_SAFETY_INFORMATION
RESTRICTED_REGULATOR
```

Every AI pipeline should enforce classification-aware retrieval, storage, tool use and logging.

## 10. AI use cases

- hazard summarization
- occurrence classification
- thematic analysis
- risk clustering
- emerging-risk detection
- SPI anomaly detection
- SSP gap analysis
- safety briefing generation
- evidence-backed executive summaries

AI must show the underlying evidence, uncertainty and data-quality limitations. Safety intelligence is decision support, not an automatic risk-acceptance authority.
