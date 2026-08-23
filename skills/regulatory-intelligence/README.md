# Regulatory Intelligence Skill

Turn aviation regulations, AMC/GM, advisory circulars, policies and other authoritative material into a searchable, versioned and explainable knowledge layer.

## Why it matters

Aviation requirements are distributed across global standards, regional frameworks and national rules. A useful engineering system must know **which requirement applies, where it came from, when it applies and what evidence demonstrates compliance**.

## Capabilities

- jurisdiction-aware regulatory ingestion
- regulation hierarchy parsing
- section/paragraph extraction
- applicability and effective-date resolution
- supersession/version tracking
- requirement extraction
- obligation/actor identification
- exceptions and conditions
- source citation
- cross-authority comparison
- regulatory change detection
- compliance impact analysis

## Target abstraction

```text
Authority
  ↓
Legal Instrument
  ↓
Regulation / Rule
  ↓
Section / Paragraph
  ↓
Requirement
  ↓
Applicability
  ↓
Evidence
  ↓
Compliance Assessment
```

## Initial authority adapters

- ICAO
- EASA / EU
- FAA / US
- KCAA / Kenya
- Transport Canada
- UK CAA
- CASA / Australia

The adapter interface should allow new authorities to be added without changing downstream applications.

## AI responsibilities

AI may assist with extraction, classification, comparison and summarization. It should not silently transform AI output into an authoritative regulatory decision.

## Evaluation

Minimum evaluation dimensions:

- extraction accuracy
- citation accuracy
- jurisdiction accuracy
- effective-date accuracy
- applicability accuracy
- completeness
- hallucination rate
