# Aviation AI Evaluation Framework

Generic LLM benchmarks are not enough for regulated aviation applications.

## Evaluation dimensions

### 1. Groundedness
Does the answer stay supported by retrieved evidence?

### 2. Citation correctness
Do cited source, section, paragraph and version actually support the statement?

### 3. Applicability
Does the requirement apply to the stated jurisdiction, organization, aircraft, operation and date?

### 4. Completeness
Did the system identify the material requirements and evidence gaps?

### 5. Temporal correctness
Did the system use the regulation version effective for the date in question?

### 6. Safety conservatism
Does the system avoid presenting uncertain AI output as an authoritative safety determination?

### 7. Human factors
Can an inspector/reviewer understand, challenge and correct the recommendation?

### 8. Robustness
How does the system behave with missing, contradictory, corrupted or adversarial inputs?

### 9. Security
Test prompt injection, retrieval poisoning, malicious documents, unauthorized tool calls and data leakage.

## Example scorecard

```text
Groundedness          0.97
Citation correctness  0.95
Applicability         0.93
Temporal correctness  0.99
Completeness          0.89
Human review usability 4.5/5
```

These numbers are illustrative. A real benchmark must be built from validated aviation test cases.

## Evaluation set design

Include:
- clean questions
- ambiguous questions
- cross-jurisdiction questions
- historical questions
- conflicting-source questions
- missing-evidence cases
- negative cases where the correct answer is "insufficient evidence"
- safety-critical cases requiring human escalation

## Release gate

A production-oriented skill should define minimum thresholds for its intended use case and fail the build when evaluation regressions exceed the allowed tolerance.