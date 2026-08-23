# Aviation Document Intelligence Skill

Process the large document volumes used across aviation certification, operations, airworthiness, maintenance, safety and oversight.

## Document types

- regulations
- advisory circulars
- manuals
- operations specifications
- certificates
- licences
- inspection reports
- audit reports
- maintenance records
- occurrence reports
- aircraft records
- applications and forms

## Pipeline

```text
PDF / DOCX / Image / XML
        ↓
Ingestion
        ↓
OCR / parsing
        ↓
Layout + section detection
        ↓
Classification
        ↓
Structured extraction
        ↓
Validation / normalization
        ↓
Entity linking
        ↓
Search / RAG / workflow
```

## Aviation-specific extraction

The skill should be able to identify common concepts such as:

- aircraft registration
- MSN
- engine/component identifiers
- certificate numbers
- licence numbers
- effective and expiry dates
- approvals
- limitations
- operating areas
- specific approvals
- findings
- corrective actions
- regulatory references

## Quality requirements

Every extracted field should retain its source location and confidence where practical:

```json
{
  "field": "certificateNumber",
  "value": "...",
  "source": {
    "page": 3,
    "section": "Certificate Details",
    "boundingBox": [0, 0, 0, 0]
  },
  "confidence": 0.99
}
```

This enables review, citation and reproducible testing.
