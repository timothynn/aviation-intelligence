# Regulatory Ingestion Architecture

## Objective

Create a source-agnostic pipeline that can ingest legally accessible aviation regulations, guidance, standards metadata and published updates without copying protected publications into the repository.

## Source hierarchy

```text
Authority / Organization
        ↓
Legal instrument / Regulation
        ↓
Rule / Article / Paragraph
        ↓
AMC / GM / AC / Policy / Guidance
        ↓
Requirement
        ↓
Applicability
        ↓
Evidence / Compliance control
```

## Required metadata

- authority
- jurisdiction
- instrument type
- title
- identifier
- edition / amendment
- publication date
- effective date
- applicability date
- supersedes / superseded-by
- source URI
- source licence / access conditions
- section / paragraph locator
- language
- extraction status

## Requirement representation

```json
{
  "id": "KE-OPS-EXAMPLE-001",
  "authority": "KCAA",
  "jurisdiction": "KE",
  "source": "published-regulation",
  "sourceVersion": "version-id",
  "effectiveFrom": "2026-01-01T00:00:00Z",
  "text": "Normalized requirement text",
  "applicability": {
    "operatorType": ["commercial"],
    "aircraft": ["aeroplane"]
  },
  "evidenceTypes": ["document", "record", "inspection"],
  "provenance": {
    "locator": "Part X / Regulation Y / Paragraph Z"
  }
}
```

## First adapters

1. ICAO metadata / controlled-source references
2. KCAA
3. EASA
4. FAA
5. UK CAA
6. Transport Canada
7. CASA Australia

## Key design constraint

The repo stores schemas, adapters, parsers, test fixtures, synthetic examples and source metadata. Protected regulatory publications should be obtained from authorized sources by the consumer of the library.

## AI use

LLMs can help extract candidate requirements from source documents, but the extraction pipeline must preserve raw text, source location, version and human validation status.