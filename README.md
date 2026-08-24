# Aviation Intelligence ✈️🤖

> Open-source AI engineering toolkit for building intelligent aviation applications.

Aviation Intelligence is a developer-focused open-source project for engineers building AI-enabled aviation systems. It combines aviation domain models, regulatory intelligence, document/evidence processing, workflow, inspections/audits, compliance, safety intelligence, RAG, agents and AI assurance.

## Current status

The project has moved beyond a research-only foundation. The repository contains a **working aviation document-intelligence reference engine**, a reproducible global aviation-source registry, SAFA RAMP intelligence, temporal/applicability contracts, a knowledge-graph contract and PostgreSQL adapter, source-change monitoring, document access policy, a grounded LLM gateway contract, PostgreSQL persistence and local development infrastructure.

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
- aviation-aware reranking
- temporal resolution contracts
- applicability scoring contracts
- provider-neutral knowledge graph
- PostgreSQL knowledge-graph persistence
- regulatory change fingerprinting
- deterministic first-party source monitoring
- document object-storage abstraction
- document-level access policy
- grounded LLM prompt/provider contract
- explicit abstention when evidence is insufficient
- CLI for initialization, ingestion, vector indexing, search and statistics
- FastAPI search/health reference service
- PostgreSQL document persistence adapter
- PostgreSQL graph/source-monitoring schema
- local PostgreSQL/Redis development infrastructure
- regression tests and GitHub Actions CI

See [`packages/aviation-document-intelligence/README.md`](packages/aviation-document-intelligence/README.md), [`docs/aviation-document-intelligence.md`](docs/aviation-document-intelligence.md) and [`docs/aviation-document-intelligence-production-hardening.md`](docs/aviation-document-intelligence-production-hardening.md).

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
                    Aviation Document Intelligence
                                  │
       ┌──────────────────────────┼──────────────────────────┐
       │                          │                          │
   Acquisition               Processing                 Knowledge
       │                          │                          │
 Official sources            PDF/XML/HTML             Metadata/entities
 Provenance                   OCR/tables               Versioning
 SHA-256                      Chunking                 Relationships
 Source monitoring            Object storage            Graph persistence
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
                   Hybrid / Rerank / Temporal
                                  │
                 Authority / Jurisdiction /
                   Applicability / Security
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
├── apps/
├── services/
├── packages/
│   └── aviation-document-intelligence/
├── skills/
│   ├── aviation-document-intelligence/
│   └── safa-ramp-intelligence/
├── infra/
│   ├── docker-compose.document-intelligence.yml
│   └── postgres/init/
├── datasets/
├── evaluation/
├── examples/
├── notebooks/
├── docs/
└── .github/
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

Build/use the optional local vector index and enable hybrid retrieval:

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

Build the public/source-managed corpus separately:

```bash
python skills/aviation-document-intelligence/scripts/download_corpus.py \
  --manifest skills/aviation-document-intelligence/source-manifest-global.yaml \
  --output data/corpus
```

### PostgreSQL / Redis local infrastructure

```bash
docker compose -f infra/docker-compose.document-intelligence.yml up -d
```

Install the PostgreSQL adapter:

```bash
pip install -r packages/aviation-document-intelligence/requirements-postgres.txt
```

The local Compose stack is development infrastructure only. Production deployments should use managed credentials, secret storage, TLS, backups and appropriate network isolation.

## Priority roadmap

### P0 — Core regulated-system foundation

- [x] Initial aviation document-intelligence engine
- [x] Authority / jurisdiction / version metadata contracts
- [x] Evidence/provenance contract
- [x] Reproducible source acquisition registry
- [x] Temporal/applicability/knowledge-graph reference contracts
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

- [x] Reference lexical/vector/hybrid retrieval
- [x] Reference change detection
- [x] Reference security/access policy
- [x] Grounded LLM gateway contract
- [x] PostgreSQL production persistence adapter
- [x] PostgreSQL graph/source-monitoring schema
- [x] Local PostgreSQL/Redis development stack
- [x] Object-storage abstraction
- [x] Deterministic source-monitoring service
- [ ] Production object storage and large-corpus lifecycle
- [ ] Production PDF/XML/OCR/table extraction workers
- [ ] Managed lexical + vector search backend
- [ ] Production semantic reranker
- [ ] Production knowledge graph service deployment
- [ ] Production temporal/version resolution
- [ ] Production regulatory applicability engine
- [ ] Regulatory change-impact workflow
- [ ] Scheduled source freshness and revision monitoring deployment
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

## Evaluation

The current hardening benchmark is in [`evaluation/document-intelligence-hardening.jsonl`](evaluation/document-intelligence-hardening.jsonl). It covers exact SAFA identifiers, technical semantic retrieval, temporal questions, jurisdiction filtering, cross-authority comparison, source precedence, abstention, security and change detection.

Production evaluation should add expert-labeled gold evidence and score retrieval, citations, temporal correctness, applicability, abstention, latency and cost.

## Research references

- [`docs/regulatory-landscape.md`](docs/regulatory-landscape.md)
- [`docs/authority-oversight-architecture.md`](docs/authority-oversight-architecture.md)
- [`docs/inspection-and-audit-landscape.md`](docs/inspection-and-audit-landscape.md)
- [`docs/inspection-schemes.md`](docs/inspection-schemes.md)
- [`docs/ssp-safety-intelligence.md`](docs/ssp-safety-intelligence.md)
- [`docs/aviation-document-intelligence.md`](docs/aviation-document-intelligence.md)
- [`docs/aviation-document-intelligence-production-hardening.md`](docs/aviation-document-intelligence-production-hardening.md)
- [`docs/aviation-document-intelligence-sources.md`](docs/aviation-document-intelligence-sources.md)
- [`skills/aviation-document-intelligence/`](skills/aviation-document-intelligence/)
- [`skills/safa-ramp-intelligence/`](skills/safa-ramp-intelligence/)

## Engineering principles

1. AI assists; qualified humans remain accountable for authoritative decisions.
2. Important AI outputs must be traceable to evidence and source versions.
3. Jurisdiction, applicability and time are first-class data.
4. Inspection observations, findings, actions and closure are separate objects.
5. Industry schemes are adapters; they do not redefine the generic domain.
6. The portal is never the source of regulatory truth.
7. Synthetic/public data is preferred for examples; proprietary operational data does not belong in the public repository.
8. Security, privacy, retention and auditability are design requirements.
9. Historical documents must never silently outrank current authoritative material.
10. When evidence is unavailable or conflicting, the system should abstain and escalate for human review.

## Disclaimer

This project is an engineering and research toolkit. It does not provide regulatory approval, legal advice, safety certification or authoritative aviation determinations. Always validate implementations against the current applicable source material and competent-authority requirements.

## Status

🚧 **Active implementation.** The reference document-intelligence engine, global source registry, SAFA intelligence foundation, production-hardening contracts, PostgreSQL persistence, graph persistence, object-storage abstraction, source monitoring and local infrastructure are in place. Remaining work is primarily managed production search/storage, distributed document processing, domain-specific regulatory execution, expert evaluation and the broader regulated-system core.
