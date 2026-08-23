# Authority Oversight Architecture

The repository supports three related perspectives:

```text
              Aviation Intelligence
                       │
        ┌──────────────┼──────────────┐
        │              │              │
     Authority       Operator     Service Provider
        │              │              │
    Oversight       Operations     Delivery
```

## Authority capability model

The authority side should represent the eight broad USOAP CMA audit areas while allowing each regulator to organize departments differently.

```text
LEG  — Legislation / regulations
ORG  — Civil aviation organization
PEL  — Personnel licensing
OPS  — Aircraft operations
AIR  — Airworthiness
AIG  — Accident / incident investigation
ANS  — Air navigation services
AGA  — Aerodromes / ground aids
```

## Critical element lifecycle

```text
Establish
  CE-1 Legislation
  CE-2 Specific regulations
  CE-3 State system and functions
  CE-4 Qualified technical personnel
  CE-5 Technical guidance / tools
       ↓
Implement
  CE-6 Licensing / certification / approval
  CE-7 Surveillance
  CE-8 Resolution of safety issues
```

## Department model

A CAA implementation can define departments such as:

- Flight Operations
- Airworthiness
- Personnel Licensing
- Aerodromes
- ANS
- AIG
- Aviation Security
- Safety Management
- Legal / Rulemaking
- Finance
- Corporate Services
- ICT / Data

The domain model should not hard-code these as mandatory departments. Instead use configurable organizational units and capability mappings.

## Authority intelligence use cases

### Oversight planning
Identify organizations, certificates, aircraft or areas requiring surveillance based on risk, history and regulatory obligations.

### Resource planning
Forecast inspector workload, audit days, travel, specialist needs and upcoming certificate actions.

### Safety assurance
Correlate approvals, inspections, findings, occurrences and corrective actions.

### Regulatory effectiveness
Measure whether requirements are implemented consistently and whether findings indicate weaknesses in the regulatory system itself.

### Executive oversight
Provide organization, sector, fleet, airport, domain and State-level views.

## Key rule

Aviation authorities should be modeled as organizations with regulatory powers, not as a special hard-coded application type. Their powers, responsibilities, jurisdiction and delegated functions should be explicit data.