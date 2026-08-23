# Regulatory Change Intelligence Skill

Detect and reason about changes in aviation regulations and guidance.

## Inputs

- new/revised regulations
- amendments
- consolidated rules
- AMC/GM
- advisory circulars
- authority decisions
- forms and guidance
- effective/applicability dates

## Pipeline

```text
Source monitor
    ↓
Document fingerprint
    ↓
Version diff
    ↓
Semantic change extraction
    ↓
Affected requirements
    ↓
Affected approvals / workflows
    ↓
Impact assessment
    ↓
Human validation
```

## Change types

```text
New
Amended
Corrected
Superseded
Withdrawn
Reissued
Future applicability
Temporary deviation
Guidance-only
```

## Key output

```json
{
  "authority": "...",
  "instrument": "...",
  "changeType": "Amended",
  "effectiveDate": "...",
  "applicabilityDate": "...",
  "affectedRequirements": [],
  "affectedApprovals": [],
  "impactLevel": "High",
  "evidence": []
}
```

## High-value use cases

- regulator change monitoring
- application/workflow impact analysis
- operator compliance monitoring
- maintenance AD/SB applicability
- internal policy synchronization
- cross-jurisdiction comparison
