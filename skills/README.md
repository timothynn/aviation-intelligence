# Aviation AI Skills

Skills are the core reusable capabilities of Aviation Intelligence. Each skill should solve one focused aviation engineering problem and be independently understandable, testable and reusable.

## Skill contract

Every mature skill should document:

1. **Purpose** — the aviation problem being solved.
2. **Inputs** — data, documents or events it accepts.
3. **Outputs** — structured results and confidence/evidence where relevant.
4. **Architecture** — components and dependencies.
5. **Implementation** — production-oriented code, not only a notebook.
6. **Evaluation** — domain-specific tests and AI metrics.
7. **Aviation considerations** — safety, traceability, human review and limitations.

## Planned catalogue

### Foundation

- `aviation-domain-model` — common aviation entities and value objects.
- `aviation-data` — schemas, validation and synthetic data generation.
- `aviation-document-processing` — PDF, DOCX, OCR and metadata extraction.

### Knowledge & regulatory intelligence

- `regulatory-requirement-extraction`
- `aviation-rag`
- `regulatory-search`
- `compliance-gap-analysis`
- `aviation-knowledge-graph`

### Operations & workflow

- `workflow-intelligence`
- `application-assistance`
- `inspection-intelligence`
- `safety-occurrence-classification`
- `maintenance-intelligence`

### AI capabilities

- `aviation-nlp`
- `aviation-speech`
- `aviation-computer-vision`
- `anomaly-detection`
- `predictive-maintenance`
- `aviation-agents`

### Assurance

- `human-in-the-loop`
- `ai-evaluation`
- `ai-groundedness`
- `ai-explainability`
- `ai-audit-trail`
- `ai-safety-guardrails`

## Contribution rule

A new skill should be narrow enough to explain in one README and broad enough to be reused by more than one aviation application. Avoid creating skills that are merely wrappers around a single vendor API.
