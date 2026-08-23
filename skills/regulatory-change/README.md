# Regulatory Change Intelligence Skill

Detect, interpret and route changes in aviation regulations, guidance, approvals and supporting material.

## Why this is P0

Aviation rules are versioned and time-dependent. EASA's 2026 eRules platform publishes machine-readable XML and explicitly supports synchronization with local applications; KCAA's 2025 transition introduced 29 revised regulations with transitional compliance and further regulations pending publication. citeturn647973search0turn934489search0

## Inputs

- regulations
- consolidated rules
- amendments
- AMC/GM
- advisory circulars
- authority decisions
- forms/templates
- implementation guidance
- future-applicability rules
- transition notices

## Pipeline

```text
Source monitor
    ↓
Acquire publication
    ↓
Fingerprint / checksum
    ↓
Version resolution
    ↓
Structural diff
    ↓
Semantic diff
    ↓
Requirement impact
    ↓
Applicability resolution
    ↓
Affected organization / approval / workflow resolution
    ↓
Impact assessment
    ↓
Human review
    ↓
Tasks / notifications / migration plan
```

## Change types

```text
NEW
AMENDED
CORRECTED
SUPERSEDED
WITHDRAWN
REISSUED
FUTURE_APPLICABILITY
TRANSITIONAL
TEMPORARY_DEVIATION
GUIDANCE_ONLY
FORM_OR_TEMPLATE_CHANGE
```

## Change object

```json
{
  "authority": "KCAA",
  "jurisdiction": "KE",
  "instrument": "...",
  "previousVersion": "...",
  "newVersion": "...",
  "changeType": "AMENDED",
  "publishedAt": "...",
  "effectiveDate": "...",
  "applicabilityDate": "...",
  "affectedRequirements": [],
  "affectedApprovals": [],
  "affectedWorkflows": [],
  "impactLevel": "HIGH",
  "evidence": [],
  "reviewRequired": true
}
```

## Impact dimensions

### Regulatory impact
Does the obligation itself change?

### Applicability impact
Does the population subject to the rule change?

### Operational impact
Do manuals, procedures, training or systems need revision?

### Approval impact
Could certificates, approvals, Ops Specs or limitations need amendment?

### Workflow impact
Do application forms, review tasks, checklists or decision rules change?

### Data impact
Do new fields, records, classifications or retention requirements appear?

### AI/RAG impact
Should indexed knowledge, prompts, evaluation sets or agent policies be re-baselined?

## High-value use cases

- regulator change monitoring
- authority implementation tracking
- operator compliance monitoring
- KCAA transition management
- EASA eRules synchronization
- AD/SB applicability tracking
- application/workflow impact analysis
- cross-jurisdiction comparison
- internal policy synchronization

## Guardrail

A semantic diff is a recommendation. It must not automatically declare legal applicability or modify an authoritative approval without review under the applicable authority process.