# Aviation AI Assurance Skill

Aviation AI should be evaluated not only for model accuracy but for evidence quality, regulatory applicability, temporal correctness, operational suitability, traceability, security and human oversight.

## Assurance dimensions

| Dimension | Question |
|---|---|
| Correctness | Is the result factually/domain correct? |
| Groundedness | Can the answer be traced to evidence? |
| Applicability | Does the rule apply to the jurisdiction, entity, operation and date? |
| Temporal correctness | Did the system use the requirement version effective at the relevant time? |
| Completeness | Were material requirements/evidence gaps identified? |
| Uncertainty | Is uncertainty represented appropriately? |
| Explainability | Can a reviewer understand the basis? |
| Auditability | Can inputs, sources, model/policy and output be reconstructed? |
| Human oversight | Can an authorized reviewer accept, reject or modify it? |
| Decision-boundary correctness | Does AI stop at recommendation where required? |
| Security | Can prompt injection, data leakage and unauthorized tools be prevented/detected? |
| Drift | Does performance change as sources, models or operational data change? |

## Required decision record

```text
Dataset version
Model version
Prompt/policy version
Knowledge-base version
Source versions
Input context
Retrieved evidence
Output
Warnings
Confidence / uncertainty
Human reviewer
Human decision
Timestamp
```

## Tool authorization

Agents must not inherit unrestricted privileges.

```text
User / service identity
        ↓
Role + attributes
        ↓
Policy evaluation
        ↓
Tool authorization
        ↓
Tool execution
        ↓
Evidence / audit event
```

Write operations, approval changes, enforcement actions and safety-significant operations require explicit configured authorization and, where applicable, human approval.

## Regulatory-aware RAG guardrails

Before answering:

1. identify jurisdiction
2. identify relevant date/time
3. identify entity/operation applicability
4. retrieve authoritative sources
5. compare source versions
6. detect conflicting requirements
7. expose evidence and uncertainty

A response such as **insufficient evidence** is preferable to unsupported certainty.

## Inspection AI guardrails

AI may:
- summarize history
- rank inspection targets
- prioritize checklist items
- retrieve standards
- link evidence
- suggest finding text/category
- detect recurrence
- assess CAP completeness

AI must not silently:
- create an authoritative finding
- change finding severity
- impose an enforcement action
- clear a grounding/restriction
- approve a certificate
- alter regulatory applicability

## Security tests

Test:
- prompt injection
- malicious documents
- retrieval poisoning
- source spoofing
- cross-organization data leakage
- unauthorized tool calls
- policy bypass
- secret exfiltration
- unsafe state mutation
- adversarial evidence

## Principle

The goal is not to prove that an AI model is universally safe. The goal is to produce evidence that a specific capability is bounded, understood, tested and appropriately supervised for its intended aviation use.