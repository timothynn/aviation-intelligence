# Evidence and Compliance Service Specification

## Purpose

Provide the deterministic layer that converts regulatory requirements and submitted evidence into reviewable compliance assessments.

## Evidence pipeline

```text
Document / Record
      ↓
Document classification
      ↓
Extraction
      ↓
Evidence object
      ↓
Requirement link
      ↓
Assessment
```

## Evidence object

```text
Evidence
- id
- type
- sourceRecordId
- documentId
- page/section/locator
- observedValue
- extractionMethod
- confidence
- capturedAt
- capturedBy
- sourceVersion
- effectiveContext
- securityClassification
- hash
```

## Compliance assessment

```text
Requirement
   ↓
Applicability
   ↓
Evidence sufficiency
   ↓
Assessment
   ↓
Reviewer decision
```

Statuses:

```text
COMPLIANT
PARTIALLY_COMPLIANT
NON_COMPLIANT
NOT_APPLICABLE
INSUFFICIENT_EVIDENCE
PENDING_REVIEW
```

## Rules

- Never mark compliant solely from an LLM statement.
- Store the exact regulatory source/version used.
- Preserve contradictory evidence.
- Preserve reviewer override.
- Permit reassessment when a regulation changes.
- Distinguish document presence from evidence sufficiency.

## AI assistance

AI may extract fields, match candidate requirements, summarize evidence and identify apparent gaps. The assessment engine owns final status transitions and reviewer gates.