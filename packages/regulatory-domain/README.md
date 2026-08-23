# Regulatory Domain

Regulations are modeled as versioned, jurisdiction-aware knowledge objects.

## Key distinction

```text
Source document
  != Regulation
  != Requirement
  != Guidance
  != Evidence
  != Compliance result
```

Each requirement should be traceable to the source and applicable time period.

## Core fields

- authority
- jurisdiction
- instrument type
- reference / locator
- version
- publication date
- effective date
- applicability
- supersession
- source provenance

This design supports historical queries such as: "Which requirement applied to this case on the decision date?"
