# Aviation AI Evaluation Contract

Every aviation AI capability should be evaluated beyond generic model accuracy.

## Minimum dimensions

| Dimension | Question |
| --- | --- |
| Groundedness | Is the answer supported by retrieved evidence? |
| Citation correctness | Does the citation actually support the claim? |
| Applicability | Is the right jurisdiction, aircraft, operator and operation being considered? |
| Temporal correctness | Is the applicable rule/version valid for the relevant date? |
| Completeness | Were material requirements or evidence omitted? |
| Safety conservatism | Does uncertainty trigger appropriate human review? |
| Robustness | Does the system behave safely under incomplete or conflicting inputs? |
| Security | Can prompt injection, malicious documents or tool misuse alter authoritative outcomes? |
| Auditability | Can the answer and its evidence be reconstructed later? |

## Gate

An AI result should be treated as advisory when any required evidence, applicability or confidence condition is not satisfied.
