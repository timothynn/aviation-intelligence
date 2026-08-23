# SAFA / Ramp Inspection Intelligence Skill

A focused reference implementation for AI-assisted ramp inspection workflows inspired by the European ramp inspection ecosystem and common State/operator surveillance patterns.

## Workflow

```text
Inspection target selection
        ↓
Aircraft / operator context
        ↓
Risk-informed inspection briefing
        ↓
Ramp inspection
        ↓
Evidence + observations
        ↓
Finding classification
        ↓
Severity / category support
        ↓
Report generation
        ↓
Corrective action / follow-up
```

## AI capabilities

- pre-inspection briefing
- previous-finding summarization
- recurring-finding detection
- checklist support
- evidence classification
- requirement matching
- finding categorization assistance
- narrative/report drafting
- fleet/operator trend analysis
- inspection risk signals

## Data model

```text
Inspection
 ├── State / Authority
 ├── Operator
 ├── Aircraft
 ├── Location
 ├── Date/Time
 ├── Inspection Items
 ├── Evidence
 ├── Findings
 ├── Corrective Actions
 └── Follow-up
```

## Guardrails

SAFA/ramp inspection recommendations must be reviewable and traceable to inspection evidence and the applicable inspection framework. AI should not determine legal enforcement outcomes independently.
