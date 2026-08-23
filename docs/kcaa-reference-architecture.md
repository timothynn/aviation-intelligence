# KCAA Reference Architecture

KCAA is the first complete jurisdictional reference implementation for Aviation Intelligence.

## Regulatory transition context

KCAA published 29 revised Civil Aviation Regulations in 2025 and describes transitional compliance, implementation guidance and enhanced surveillance/inspection/audit activity. Nine additional regulations were pending publication at the time of the KCAA notice. citeturn934489search0

## End-to-end model

```text
Organization Registration
        ↓
ASL / Pre-Application
        ↓
AOC Application
        ↓
Workflow / Screening
        ↓
Fees
        ↓
Document / Evidence
        ↓
Compliance Assessment
        ↓
Technical / Operations Review
        ↓
Inspection / Surveillance
        ↓
Findings / CAP
        ↓
Decision
        ↓
Certificate + Ops Specs / Specific Approvals
        ↓
Continuing Surveillance
        ↓
Renewal / Amendment / Suspension / Enforcement
        ↓
SSP / Safety Intelligence
```

## Organization model

Support:
- legal entity
- operator
- AOC holder
- ASL holder
- AMO / ATO / other approved organization types
- key personnel
- bases/facilities
- aircraft
- approvals/certificates
- organizational changes

## AOC / approval model

Keep approval types extensible:

```text
AOC
Operations Specifications
Specific Approval
Authorization
Certificate
Renewal
Amendment
Limitation
```

Special-approval examples should include EDTO, PBN, RVSM, LVO, dangerous goods and other authority-approved operational capabilities where applicable.

## Application workflow

Use the common workflow engine:

```text
Pre-Application
 → Formal Application
 → Screening
    ├── Return for Corrections
    ├── Reject
    └── Proceed
 → Fees
 → Detailed Assessment
 → Compliance
 → Inspection
 → CAP
 → Decision
 → Approval
```

## Surveillance integration

KCAA's air-operator surveillance guidance includes an entry meeting and document review such as ASL, AOC/Ops Specs, ATO certification, aircraft registration, leases, statistics, audited financial statements and insurance. citeturn535738search36

The reference implementation should make these configurable inspection-evidence requests rather than hard-coded UI fields.

## Safety integration

KCAA's safety-performance service accepts SPIs through eServices and publishes indicators across flight operations, maintenance, ATO, aerodrome operations and ATS. citeturn934489search1

The reference architecture should therefore connect:

```text
Inspection findings
+ Occurrences
+ Maintenance
+ Surveillance
+ SPIs/SPTs
+ Risk controls
        ↓
Safety Intelligence
        ↓
SSP / NASP
```

## AI opportunities

- application completeness
- evidence extraction
- requirement matching
- reviewer briefing
- inspection targeting
- finding recurrence
- CAP quality
- regulatory-change impact
- surveillance risk profile
- safety intelligence

AI outputs remain recommendations and are stored with provenance and human review.