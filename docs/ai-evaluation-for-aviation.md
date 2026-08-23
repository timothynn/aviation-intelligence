# Aviation AI Evaluation Framework

Generic LLM benchmarks are insufficient for aviation systems. Evaluation must test domain correctness, evidence, applicability, time validity, safety behavior, security and human oversight.

## 1. Evaluation dimensions

### Groundedness
Is the output supported by retrieved evidence?

### Citation correctness
Do the source, section, paragraph and version actually support the claim?

### Applicability
Is the rule applicable to the stated jurisdiction, organization, aircraft, operation and date?

### Temporal correctness
Did the system use the requirement version that applied at the relevant time?

### Completeness
Did the system identify material requirements and evidence gaps?

### Decision-boundary correctness
Does the model stop at recommendation when an authoritative human decision is required?

### Uncertainty
Does the output expose uncertainty and missing evidence rather than manufacturing certainty?

### Human factors
Can an authorized reviewer understand, challenge, correct and override the recommendation?

### Robustness
How does it behave with missing, contradictory, corrupted or adversarial inputs?

### Security
Test prompt injection, retrieval poisoning, malicious documents, unauthorized tool calls and data leakage.

### Drift
Does performance change when regulations, guidance, knowledge bases, models or data distributions change?

## 2. Aviation test categories

```text
A. Normal question
B. Ambiguous question
C. Cross-jurisdiction question
D. Historical question
E. Future-applicability question
F. Conflicting-source question
G. Missing-evidence question
H. Insufficient-evidence case
I. Safety-critical escalation case
J. Adversarial / prompt-injection case
K. Unauthorized-action case
L. Stale-source case
```

## 3. Example scorecard

```text
Groundedness             ≥ 0.95
Citation correctness     ≥ 0.95
Applicability            ≥ 0.95
Temporal correctness     ≥ 0.98
Completeness             ≥ 0.90
Unsafe decisions         0 tolerated
Unauthorized tool calls  0 tolerated
```

Thresholds are illustrative and must be tailored to the intended skill and authority context.

## 4. AI decision record

Every consequential recommendation should be reconstructable:

```json
{
  "decisionSupportId": "...",
  "model": "...",
  "modelVersion": "...",
  "promptPolicyVersion": "...",
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

## 5. RAG-specific evaluation

Measure:
- retrieval recall
- precision of top-k sources
- reranker effectiveness
- citation coverage
- citation entailment
- stale-source rejection
- jurisdiction filtering
- applicability filtering
- source-authority weighting
- answer/evidence separation

## 6. Agent-specific evaluation

Agents must be tested for:
- tool selection
- permission checks
- scope adherence
- safe failure
- escalation
- evidence requirements
- state mutation boundaries
- replay/audit completeness

## 7. Inspection AI evaluation

Use test sets for:
- target-selection suggestions
- checklist prioritization
- evidence classification
- finding suggestions
- severity/category suggestions
- recurrence detection
- CAP quality assessment

The benchmark must never score an AI system as “correct” merely because it agrees with a historical inspector decision; the underlying applicable standard and evidence must also be validated.

## 8. Regulatory-change evaluation

A change engine should be tested against:
- additions
- deletions
- wording changes
- applicability-date changes
- supersession
- corrected publications
- changed AMC/GM
- future rules
- multiple simultaneous amendments

## 9. Release gates

A production-oriented skill should define minimum thresholds and fail CI when regressions exceed tolerance.

```text
Source version check
Schema validation
Unit tests
Domain-rule tests
RAG retrieval tests
AI benchmark
Security tests
Human-review workflow test
Audit reconstruction test
```

## 10. Safety principle

A model can score highly and still be inappropriate for a particular aviation use case. Evaluation proves bounded behavior against defined use cases; it does not establish universal safety or regulatory approval.