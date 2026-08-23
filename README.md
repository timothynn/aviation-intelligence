# Aviation Intelligence ✈️🤖

> Open-source AI engineering toolkit for building intelligent aviation applications.

Aviation Intelligence is a developer-focused open-source project for engineers building AI-enabled aviation systems. It combines aviation domain models, regulatory intelligence, document/evidence processing, workflow, inspections/audits, compliance, safety intelligence, RAG, agents and AI assurance.

## Current status

The project has moved beyond a research-only foundation. The repository now contains a **working aviation document-intelligence reference engine**, a reproducible global aviation-source registry, SAFA RAMP intelligence, and the contracts needed to extend the platform into regulated aviation workflows.

The document-intelligence engine is intentionally **evidence-first and provider-neutral**: the LLM is not the search engine and is not the regulatory authority. Retrieval returns source-backed evidence with authority, jurisdiction, version, status, section, paragraph, page and provenance metadata.

## What is implemented

### Aviation Document Intelligence ✅

`packages/aviation-document-intelligence/` provides a runnable reference implementation with:

- PDF, XML, HTML, Markdown and text ingestion
- document metadata and SHA-256 provenance
- structure-aware chunking with page/section/paragraph context
- aviation-aware identifier handling such as `A17`, `A23`, `Part-TCO` and `TCO.GEN.100`
- SQLite + FTS5 lexical retrieval
- optional local vector index using sentence-transformers
- hybrid lexical/vector retrieval with reciprocal-rank fusion
- authority, jurisdiction, status and document-type filters
- lightweight identifier/entity-aware reranking
- evidence-pack generation
- grounded LLM prompt contract
- explicit abstention when evidence is insufficient
- CLI for initialization, ingestion, indexing, search and statistics
- FastAPI search/health reference service
- regression tests and GitHub Actions CI

See [`packages/aviation-document-intelligence/README.md`](packages/aviation-document-intelligence/README.md) and [`docs/aviation-document-intelligence.md`](docs/aviation-document-intelligence.md).

### Global aviation source registry ✅

The repository includes a global first-party acquisition registry covering source families across:

- **ICAO** — Annexes 1–19, PANS, manuals, safety reports and public safety material
- **EASA** — Easy Access Rules, certification specifications, airworthiness directives and regulatory families
- **KCAA** — Kenyan regulations, advisory material and safety-management material
- **FAA** — Advisory Circulars, safety/operations material and airworthiness material
- **UK CAA** — CAP publications and airworthiness material
- **Transport Canada** — operational and regulatory publications
- **CASA Australia** — advisory and aerodrome material
- **NZ CAA** — consolidated operating rules
- **UAE GCAA** — CARs, foreign-operator and safety publications
- **DGCA India** — Civil Aviation Requirements and public regulatory library
- **Safety/investigation authorities** — NTSB, BEA, AAIB, TSB Canada, ATSB and related public sources
- **Private/licensed hooks** — OEM technical publications, IATA DGR and organization-private material

The registry records official acquisition points rather than blindly committing regulator binaries into Git. See [`skills/aviation-document-intelligence/source-manifest-global.yaml`](skills/aviation-document-intelligence/source-manifest-global.yaml).

### SAFA RAMP Intelligence ✅

The SAFA capability models the inspection as a regulated surveillance workflow rather than a simple checklist:

```text
Selection / Preparation
        ↓
Ramp Inspection
        ↓
Observations / Findings
        ↓
Categorisation
        ↓
Immediate Action / Corrective Action
        ↓
POI / Report
        ↓
Follow-up
        ↓
Closure / Recurrence Intelligence
```

The AI layer is constrained to decision support: preparation intelligence, checklist prioritisation, regulatory retrieval, finding assistance, technical-reference retrieval, evidence organisation, recurrence detection and corrective-action review. Final regulatory findings, operational restrictions, grounding, bans, airworthiness decisions and closure remain human-authorised.

See [`skills/safa-ramp-intelligence/`](skills/safa-ramp-intelligence/) and [`docs/safa-ai-integration.md`](docs/safa-ai-integration.md).

## 2026 research-driven direction

The project is deliberately being designed around the way aviation oversight actually works: **risk-based, data-supported, continuously monitored, jurisdiction-aware, evidence-backed, version-aware and human-controlled**.

The research set spans ICAO, EASA/EU, FAA, Transport Canada, UK CAA, CASA, KCAA, other national authorities, IATA material where appropriately licensed, safety/investigation bodies and ramp-inspection programmes.

## Core pillars

| Area | Focus | Status |
| --- | --- | --- |
| 🛩️ Aviation Domain | Aircraft, operators, organizations, aerodromes, personnel, approvals and certificates | Foundation |
| ⚖️ Regulatory Intelligence | Rules, guidance, applicability, effective dates, changes and provenance | In progress |
| 📄 Evidence | Documents, records, OCR, extraction, evidence chains and controlled references | **Engine implemented** |
| 🔄 Workflow | Case management, stages, tasks, decisions, SLAs, escalation and audit history | Foundation / next major build |
| 🔎 Inspection & Audit | Generic engine plus SAFA/SACA and authority surveillance adapters | SAFA capability in progress |
| 🛡️ Compliance | Requirement-to-evidence mapping and controlled assessments | Next major build |
| 💰 Cost | Fee schedules, effective dates, billing, payments and reconciliation | Planned |
| 🧭 SSP / Safety | Hazards, risks, occurrences, SPIs, assurance and safety intelligence | Foundation |
| 🧠 AI / ML | RAG, classification, anomaly detection, forecasting and domain models | Document intelligence implemented |
| 🤖 Agents | Regulatory, compliance, inspection, safety and workflow assistants | Planned |
| 🔐 AI Assurance | Groundedness, applicability, temporal correctness, security, human oversight and auditability | Partially implemented |

## Architecture

```text
                         AVIATION INTELLIGENCE
                                  │
        ┌─────────────────────────┼─────────────────────────┐
        │                         │                         │
    Domain Core             Regulatory Core          Evidence Core
        │                         │                         │
 Organization / Aircraft    Rules / Requirements    Documents / Records
 Application / Approval     Guidance / Versions     Evidence / Provenance
 Inspection / Safety       Applicability / Change  Signatures / Retention
        │                         │                         │
        └─────────────────────────┼─────────────────────────┘
                                  │
                       Workflow / Compliance
                                  │
            ┌─────────────────────┼─────────────────────┐
            │                     │                     │
        Portal/API           Inspection/Audit        Cost/Finance
            │                     │                     │
            └─────────────────────┼─────────────────────┘
                                  │
                     Aviation Document Intelligence
                                  │
       ┌──────────────────────────┼──────────────────────────┐
       │                          │                          │
   Acquisition               Processing                 Knowledge
       │                          │                          │
 Official sources            PDF/XML/HTML             Metadata/entities
 Provenance                   OCR/tables               Versioning
 SHA-256                      Chunking                 Relationships
       │                          │                          │
       └──────────────────────────┼──────────────────────────┘
                                  │
                           Retrieval Layer
                                  │
             ┌────────────────────┼────────────────────┐
             │                    │                    │
           BM25                 Vector             Knowledge Graph
             │                    │                    │
             └────────────────────┼────────────────────┘
                                  │
                          Hybrid / Rerank
                                  │
                     Authority / Jurisdiction /
                       Version / Applicability
                                  │
                           Evidence Pack
                                  │
                           Grounded LLM
                                  │
                         AI Assurance / Audit
```

## Repository structure

```text
aviation-intelligence/
├── apps/                 # Reference applications
├── services/             # API, workflow, inspection, AI and RAG services
├── packages/             # Reusable domain and engineering packages
│   └── aviation-document-intelligence/
├── skills/               # Reusable aviation capabilities
│   ├── aviation-document-intelligence/
│   └── safa-ramp-intelligence/
├── datasets/             # Public/synthetic datasets and generators
├── evaluation/           # Benchmarks and regression suites
├── examples/             # Small runnable reference examples
├── notebooks/            # Exploratory data/ML research
├── docs/                 # Research, architecture and implementation guides
└── .github/              # CI and project automation
```

## Document-intelligence quick start

From the repository root:

```bash
cd packages/aviation-document-intelligence
pip install -r requirements.txt
```

Initialize a local index:

```bash
python -m aviation_docint.cli init --db ../../data/docint.sqlite
```

Ingest a local corpus:

```bash
python -m aviation_docint.cli ingest \
  --input ../../data/corpus \
  --db ../../data/docint.sqlite
```

Search with lexical retrieval:

```bash
python -m aviation_docint.cli search \
  "SAFA A17 harness" \
  --db ../../data/docint.sqlite
```

Restrict retrieval to an authority or jurisdiction:

```bash
python -m aviation_docint.cli search \
  "third country operator" \
  --authority EASA \
  --db ../../data/docint.sqlite
```

Build/use the optional local vector index and enable hybrid retrieval where the vector dependencies are installed:

```bash
python -m aviation_docint.cli index-vector --db ../../data/docint.sqlite
python -m aviation_docint.cli search \
  "requirements for foreign operators" \
  --vector \
  --db ../../data/docint.sqlite
```

Run tests:

```bash
pytest -q packages/aviation-document-intelligence/tests
```

The global acquisition registry and downloader are separate from the engine so that large regulator corpora remain external to Git:

```bash
python skills/aviation-document-intelligence/scripts/download_corpus.py \
  --manifest skills/aviation-document-intelligence/source-manifest-global.yaml \
  --output data/corpus
```

## Priority roadmap

### P0 — Core regulated-system foundation

- [x] Initial aviation document-intelligence engine
- [x] Authority / jurisdiction / version metadata contracts
- [x] Evidence/provenance contract
- [x] Reproducible source acquisition registry
- [ ] Strongly typed common aviation domain model
- [ ] Production regulatory ingestion/versioning service
- [ ] Generic evidence and records service
- [ ] Workflow / case engine
- [ ] Generic inspection / audit engine
- [ ] Compliance assessment engine

### P1 — Regulatory and oversight reference platform

- [ ] Complete KCAA regulatory reference implementation
- [ ] KCAA organization and approval adapters
- [ ] KCAA fee / payment model
- [ ] KCAA surveillance model
- [ ] Complete SAFA/SACA operational workflow
- [ ] Authority oversight / USOAP-style model
- [ ] SSP / safety intelligence implementation
- [ ] Airworthiness / maintenance compliance implementation

### P2 — Production document intelligence

- [ ] Production object storage and large-corpus lifecycle
- [ ] Production PDF/XML/OCR/table extraction workers
- [ ] Managed lexical + vector search backend
- [ ] Production semantic reranker
- [ ] Knowledge graph / regulatory relationship graph
- [ ] Temporal/version resolution engine
- [ ] Regulatory applicability engine
- [ ] Regulatory change-impact engine
- [ ] Source freshness and revision monitoring
- [ ] Inspector/compliance document workspace

### P3 — Aviation intelligence

- [ ] Evidence-backed aviation RAG service
- [ ] Compliance copilot
- [ ] Regulatory copilot
- [ ] SAFA inspector copilot
- [ ] Safety intelligence copilot
- [ ] Inspection risk targeting
- [ ] Recurrence detection at scale
- [ ] Corrective-action intelligence
- [ ] Cross-authority regulatory comparison
- [ ] Accident/incident knowledge integration

### P4 — Advanced AI/ML

- [ ] Predictive maintenance
- [ ] Flight/weather/ATM analytics
- [ ] Aviation computer vision for ramp/aircraft condition
- [ ] Aviation speech/NLP
- [ ] Constrained agentic workflows

### P5 — Production and assurance maturity

- [ ] Large-scale retrieval benchmark suite
- [ ] Release gates for retrieval/citation quality
- [ ] Prompt/model/knowledge versioning
- [ ] Red-team and AI security testing
- [ ] Tenant/access-control aware retrieval
- [ ] PII/data classification and policy enforcement
- [ ] Retention/legal-hold controls
- [ ] Full audit/event trail
- [ ] Observability and drift monitoring
- [ ] Multi-authority adapter conformance tests
- [ ] Disaster recovery and backup strategy

## What remains in the document-intelligence engine

The reference engine is intentionally local and lightweight. The major remaining production capabilities are:

1. **Industrial ingestion** — robust OCR, table extraction, scanned-PDF handling, document deduplication and very large corpus parallelism.
2. **Managed retrieval** — replace or complement SQLite/local vectors with a production search backend such as Azure AI Search, OpenSearch or equivalent.
3. **Semantic reranking** — plug in a dedicated reranker and benchmark it against the current lightweight reranking layer.
4. **Knowledge graph** — represent relationships between ICAO SARPs, PANS, EASA rules, national regulations, AMC/GM, findings, ADs, safety events and technical references.
5. **Temporal reasoning** — determine which version was applicable on a requested date rather than only storing version metadata.
6. **Applicability reasoning** — aircraft/operator/state/operation/jurisdiction-specific applicability rules.
7. **Regulatory change monitoring** — detect new amendments, revisions and superseded material and trigger re-indexing/impact analysis.
8. **Security and tenancy** — document-level authorization, private/licensed sources, encrypted storage, tenant isolation and permission-aware retrieval.
9. **Evaluation at scale** — thousands of expert-authored queries with retrieval, citation, temporal, jurisdiction and abstention metrics.
10. **LLM gateway** — provider abstraction, rate limits, caching, model routing, structured outputs and safety controls.

## Research references

- [`docs/regulatory-landscape.md`](docs/regulatory-landscape.md)
- [`docs/authority-oversight-architecture.md`](docs/authority-oversight-architecture.md)
- [`docs/inspection-and-audit-landscape.md`](docs/inspection-and-audit-landscape.md)
- [`docs/inspection-schemes.md`](docs/inspection-schemes.md)
- [`docs/portal-workflow-cost-architecture.md`](docs/portal-workflow-cost-architecture.md)
- [`docs/ssp-safety-intelligence.md`](docs/ssp-safety-intelligence.md)
- [`docs/aviation-document-intelligence.md`](docs/aviation-document-intelligence.md)
- [`docs/aviation-document-intelligence-sources.md`](docs/aviation-document-intelligence-sources.md)
- [`docs/document-corpus-sources.md`](docs/document-corpus-sources.md)
- [`skills/aviation-document-intelligence/`](skills/aviation-document-intelligence/)
- [`skills/safa-ramp-intelligence/`](skills/safa-ramp-intelligence/)
- [`skills/README.md`](skills/README.md)

## Engineering principles

1. AI assists; qualified humans remain accountable for authoritative decisions.
2. Important AI outputs must be traceable to evidence and source versions.
3. Jurisdiction, applicability and time are first-class data.
4. Inspection observations, findings, actions and closure are separate objects.
5. Industry schemes are adapters; they do not redefine the generic domain.
6. The portal is never the source of regulatory truth.
7. Synthetic/public data is preferred for examples; proprietary operational data does not belong in the public repository.
8. Security, privacy, retention and auditability are design requirements.
9. Historical documents are valuable for testing but must never silently outrank current authoritative material.
10. When reliable evidence is unavailable or conflicting, the system should abstain and escalate for human review.

## Technology direction

Reference implementation:

- Python 3.11+ for document intelligence and ML tooling
- SQLite FTS5 for local/reference lexical search
- sentence-transformers for optional local embeddings
- FastAPI for the reference search service

Platform direction:

- Backend: .NET / ASP.NET Core
- Frontend: Angular / TypeScript
- AI/ML: Python, scikit-learn, PyTorch, provider-neutral LLM interfaces
- Production data: PostgreSQL, pgvector and/or managed search
- Caching: Redis
- Deployment: Docker, GitHub Actions

These are reference choices, not mandatory implementation constraints.

## Disclaimer

This project is an engineering and research toolkit. It does not provide regulatory approval, legal advice, safety certification or authoritative aviation determinations. Always validate implementations against the current applicable source material and competent-authority requirements.

## Status

🚧 **Active implementation.** The reusable document-intelligence engine, source registry and SAFA intelligence foundations are in the repository. The next major work is production-scale ingestion/retrieval, regulatory applicability/version reasoning, knowledge graph integration and the broader regulated-system core.