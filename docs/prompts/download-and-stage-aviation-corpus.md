# Prompt: Download and Stage the Aviation Document Corpus

Use this prompt with an agent that has terminal/network access to this repository.

---

You are working in `timothynn/aviation-intelligence`.

## Objective

Acquire the aviation PDF corpus defined by:

- `skills/aviation-document-intelligence/source-manifest.yaml`
- `skills/aviation-document-intelligence/source-manifest-global.yaml`

Download the latest/current public documents from first-party authority websites where they are legally and technically available, stage them under `data/corpus/downloads/`, and generate a complete acquisition manifest with provenance and SHA-256 checksums.

## Hard constraints

1. **Do not bypass authentication, subscriptions, paywalls, robots restrictions, CAPTCHAs, rate limits, or access controls.**
2. **Do not download private/licensed material** listed in the manifests, including OEM manuals (AMM/SRM/CMM/IPC/FCOM/QRH/SB/SIL/MEL/CDL), IATA Dangerous Goods Regulations, operator-private manuals, or subscription-only ICAO publications.
3. **Do not assume that “publicly downloadable” means “safe to redistribute on GitHub.”** Keep downloaded third-party PDFs local unless the source explicitly permits redistribution or the repository owner has separately verified the license/terms.
4. For ICAO material hosted by Swiss FOCA/BAZL, preserve the FOCA disclaimer and classify the copies as illustrative/reference material. Do not represent them as the authoritative ICAO publication.
5. Prefer the current authoritative source over older copies. Record publication/version dates where available.
6. Never overwrite a newer document with an older one.
7. Do not commit the PDF/XML corpus to Git unless the source's redistribution terms clearly permit it. The repo currently intentionally ignores `data/corpus/downloads/` binaries.

## Source families to process

### Kenya / KCAA
- KCAA aviation regulations library
- KCAA publications, advisory circulars and safety material
- Civil Aviation (Safety Management) Regulations, 2018
- CAA-AC-OPS001D Certification of an Air Operator
- Current KCAA Kenya Civil Aviation Regulations, including the 2025 revised regulations published by KCAA

### ICAO / global
- ICAO Annexes 1–19 available through Swiss FOCA/BAZL illustration pages
- ICAO PANS references: Docs 4444, 8168, 9868, 9981, 10066
- ICAO Docs 9760 and 8126 via Swiss FOCA/BAZL
- ICAO Safety Reports
- ICAO RASG-PA Annual Safety Reports
- ICAO public SARPs/PANS reference material
- Do not acquire ICAO Store commercial/subscription publications

### EASA
- Easy Access Rules full library
- Easy Access Rules for Air Operations
- Easy Access Rules for Third Country Operators
- Easy Access Rules for Continuing Airworthiness
- Easy Access Rules for Aerodromes
- Easy Access Rules for Aircrew
- Easy Access Rules for Initial Airworthiness and Environmental Protection
- Easy Access Rules for Ground Handling
- Easy Access Rules for Information Security
- EASA regulations/decisions public library
- EASA Airworthiness Directives
- EASA airworthiness/product rule families
- EASA ATM/ANS rules
- Include current UAS, SERA and other Easy Access Rules available from EASA when they are in the registry

### FAA
- FAA Advisory Circulars
- FAA Airworthiness Directives
- FAA handbooks/manuals/orders
- FAA Safety Management reference library
- Specifically ensure the registry's AC 43.13-1B and AC 120-92D are acquired where currently available

### UK CAA
- CAP publications library
- CAP 747
- CAP 562

### Transport Canada
- Transport Canada Aviation Reference Centre
- Transport Canada Airworthiness Directives
- Transport Canada Aeronautical Information Manual (TP 14371)

### CASA Australia
- CASA aviation publications/documentation
- CASA Airworthiness Directives
- AC 139.A-04

### New Zealand CAA
- New Zealand Civil Aviation Rules
- Part 91
- Part 121

### UAE GCAA
- Civil Aviation Regulations (CARs)
- Safety alerts and information bulletins
- Specifically ensure the registry's CAR Part IV Foreign Operators Regulation, Safety Alert 2017-14 and Information Bulletin 2018-10 are acquired where currently available

### DGCA India
- DGCA Civil Aviation Requirements public library

### Accident / safety investigation
- NTSB aviation accident reports
- BEA aviation investigation reports
- UK AAIB reports
- TSB Canada aviation investigations
- ATSB aviation investigations

## Also account for topics discussed in the project

The repository documentation and corpus should support research around:

- AOC / Air Operator Certification
- AOC application workflows and five-phase approval concepts
- EDTO / ETOPS
- PBN
- EFB
- AMO / CAMO
- SSP / safety management
- SPO / SPA
- SAFA/SACA ramp inspections
- CPL / personnel licensing workflows
- aviation oversight and inspection
- compliance evidence and document intelligence
- regulatory change impact

Use the manifests as the authoritative acquisition scope. Do not invent or fabricate missing publications.

## Required local outputs

Create:

```text
data/corpus/downloads/<authority>/<document>.pdf
data/corpus/manifests/generated/acquisition-manifest.json
```

The acquisition manifest must record for every attempted source:

- source id
- authority
- title
- source page/url
- resolved PDF URL
- filename
- retrieved UTC timestamp
- HTTP status
- content type
- byte size
- SHA-256
- publication/version date if discoverable
- currentness notes
- redistribution status: `local-only`, `redistributable`, `unknown`, or `private/licensed`
- failure reason if not downloaded

## Verification

After acquisition:

1. Run the repository's document-intelligence tests.
2. Validate that every downloaded file is actually a PDF before treating it as one.
3. Detect duplicate files by SHA-256.
4. Detect obvious HTML/error pages masquerading as PDFs.
5. Extract basic metadata where possible: title, producer, page count, creation date, modification date.
6. Report broken or stale source links without silently substituting random mirrors.

## Git behavior

Because the repository is public, do **not** commit the downloaded PDF corpus unless explicit redistribution permission is established. Commit only:

- scripts
- source manifests
- metadata
- checksums
- documentation
- tests
- sanitized examples

If a specific document is confirmed redistributable, note the evidence in the acquisition manifest before considering it for Git.

## Final report

Return a table with:

| Status | Authority | Document | Version/Date | Local Path | Redistribution |
|---|---|---|---|---|---|

And summarize:

- downloaded successfully
- blocked by access
- private/licensed
- source unavailable
- currentness uncertain
- duplicates
- recommended follow-up

Do not claim a document was downloaded unless the file was actually retrieved and verified.
