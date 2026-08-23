# Safety Intelligence Skill

Transform aviation safety data into structured hazards, risk indicators and decision-support insights.

## Reference concepts

The skill is aligned conceptually with ICAO safety-management architecture: State Safety Programme (SSP), Safety Management System (SMS), safety-data collection/analysis, safety-performance management and safety intelligence.

## Inputs

- occurrence reports
- mandatory/voluntary reports
- inspection findings
- audit findings
- flight-data indicators
- maintenance defects
- wildlife/airport events
- human factors reports
- safety performance indicators

## Capabilities

- occurrence classification
- hazard extraction
- duplicate/related event detection
- risk-factor extraction
- trend analysis
- precursor detection
- safety-performance indicator calculation
- risk register assistance
- mitigation tracking
- safety report summarization

## Pipeline

```text
Safety Data
    ↓
Normalize
    ↓
Classify
    ↓
Extract hazards / factors
    ↓
Assess risk indicators
    ↓
Identify trends / precursors
    ↓
Recommend mitigation candidates
    ↓
Safety professional review
    ↓
Action + monitoring
```

## Guardrails

Safety intelligence may inform decisions but must not replace an organization's approved SMS processes or the competent authority's legal responsibilities.
