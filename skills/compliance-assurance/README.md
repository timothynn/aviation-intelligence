# Compliance Assurance Skill

Reusable capabilities for determining whether an aviation entity, application, aircraft, organization, document set or operation has demonstrated compliance against applicable requirements.

## Core flow

```text
Applicable requirements
        ↓
Compliance criteria
        ↓
Evidence discovery
        ↓
Evidence validation
        ↓
Gap assessment
        ↓
Finding / recommendation
        ↓
Human review
        ↓
Disposition + audit trail
```

## Capabilities

- requirement-to-evidence mapping
- document/evidence classification
- missing evidence detection
- inconsistent evidence detection
- expiration/validity checks
- requirement applicability resolution
- compliance matrix generation
- gap analysis
- finding drafting
- corrective-action tracking
- evidence traceability

## Compliance states

The domain model should support more than pass/fail:

```text
Not Assessed
Applicable
Not Applicable
Compliant
Partially Compliant
Non-Compliant
Evidence Missing
Evidence Expired
Returned for Correction
Pending Review
Accepted with Limitation
Rejected
```

## Important design rule

A model score must not be confused with a regulatory compliance determination. The system should expose the evidence and reasoning so an authorized reviewer can accept, reject or modify the recommendation.
