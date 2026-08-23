# State Safety Programme and Safety Intelligence

ICAO Annex 19 establishes overarching State safety management provisions and links SSP, State safety oversight, safety information, and safety intelligence. ICAO's Safety Management Manual describes four SSP components: policy/objectives/resources; State safety risk management; State safety assurance; and State safety promotion.

## SSP operating model

```text
State aviation system
        ↓
Safety policy & objectives
        ↓
Hazard / risk picture
        ↓
Safety assurance
        ↓
Safety promotion
        ↓
Safety performance
        ↺
Continuous improvement
```

## SSP modules

### Governance
- SSP authority / accountable owner
- participating State organizations
- roles and responsibilities
- policy
- objectives
- resources
- legal framework

### State safety risk management
- hazards
- safety issues
- risk assessments
- controls / mitigations
- residual risk
- risk acceptance
- risk register

### State safety assurance
- oversight programme
- audit / inspection results
- certification results
- occurrence information
- SPI/SPT monitoring
- safety performance assessment
- corrective actions

### State safety promotion
- safety communication
- training
- safety publications
- safety events
- stakeholder engagement
- lessons learned

## Safety data model

```text
Occurrence
   ↓
Event classification
   ↓
Hazard / threat
   ↓
Risk assessment
   ↓
Control / mitigation
   ↓
Safety performance indicator
   ↓
Target / threshold
   ↓
State safety decision
```

## AI skills

### Occurrence intelligence
Classify occurrence narratives and extract event entities while retaining the original source text and confidence.

### Hazard clustering
Group related events, findings, inspection results and reports into candidate hazard families.

### Emerging risk detection
Detect changes in frequency, severity, recurrence, exposure and geographic/operator/aircraft concentration.

### SPI forecasting
Forecast safety indicators using validated statistical or ML methods. Display confidence intervals and data quality.

### SSP gap analysis
Map State capabilities and evidence against a chosen SSP framework/version.

### Safety intelligence assistant
Answer questions with source-backed evidence and expose the underlying data, assumptions and uncertainty.

## Safety information protection

Safety information should have explicit handling controls. The system should distinguish:
- public
- operational
- confidential
- protected safety information
- restricted regulator data

AI pipelines must respect those classifications and must not train or persist sensitive information without explicit policy.

## KCAA alignment

KCAA's safety policy commits to a national regulatory framework consistent with ICAO SARPs and a data-driven, performance-based and risk-based approach to safety oversight.

## Design principle

SSP is not simply a dashboard. It is a management system linking policy, risk, assurance, promotion, data and decisions. AI should support that loop rather than become an opaque risk score.