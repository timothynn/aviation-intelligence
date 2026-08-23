# Aviation AI Assurance Skill

Aviation AI should be evaluated not only for model accuracy but for evidence quality, operational suitability, traceability, robustness and human oversight.

## Assurance dimensions

| Dimension | Question |
| --- | --- |
| Correctness | Is the result factually/domain correct? |
| Groundedness | Can the answer be traced to authoritative evidence? |
| Applicability | Did the system select the right jurisdiction/rule/context? |
| Completeness | Did it identify all material requirements/evidence? |
| Uncertainty | Does it expose uncertainty and confidence appropriately? |
| Robustness | Does it behave safely on malformed/adversarial inputs? |
| Explainability | Can a reviewer understand the basis of the output? |
| Auditability | Can the input, model, sources and output be reconstructed? |
| Human oversight | Can an authorized person review and override it? |
| Drift | Does performance degrade as regulations/data/models change? |

## Required evaluation artifacts

```text
Dataset version
Model version
Prompt / policy version
Knowledge-base version
Source versions
Evaluation run
Metrics
Failures
Reviewer decisions
```

## AI decision record

```json
{
  "decisionSupportId": "...",
  "model": "...",
  "modelVersion": "...",
  "knowledgeVersion": "...",
  "inputs": [],
  "sources": [],
  "output": {},
  "confidence": 0.91,
  "warnings": [],
  "humanDecision": "accepted",
  "reviewer": "...",
  "reviewedAt": "..."
}
```

## Security

The assurance layer should also test prompt injection, malicious documents, data exfiltration, unauthorized tool use, retrieval poisoning and unsafe agent actions.

## Principle

The goal is not to prove that an AI model is universally safe. The goal is to produce evidence that a specific AI capability is understood, bounded, tested and appropriately supervised for its intended aviation use.
