# Global Aviation Document Corpus

The repository's aviation-document-intelligence capability uses a two-level registry:

- `source-manifest.yaml` contains the curated starter corpus.
- `source-manifest-global.yaml` contains global source families and crawlable regulator libraries.

The global registry covers:

- ICAO Annexes 1-19 and selected PANS through the Swiss FOCA/BAZL illustration publication page
- ICAO safety reports and regional safety reports
- EASA Easy Access Rules, airworthiness directives, operations, airworthiness, aerodromes, ATM/ANS and related regulatory families
- KCAA regulations, guidance and safety publications
- FAA Advisory Circulars, Airworthiness Directives, manuals and SMS reference material
- UK CAA CAP publications
- Transport Canada aviation references and Airworthiness Directives
- CASA aviation documentation and Airworthiness Directives
- New Zealand Civil Aviation Rules
- UAE GCAA regulations and safety publications
- DGCA India Civil Aviation Requirements
- NTSB, BEA, AAIB, TSB Canada and ATSB investigation reports
- private/licensed hooks for OEM technical publications, IATA DGR and operator documentation

## Acquisition model

The downloader treats regulator index pages as dynamic catalogs. It records the direct download URL, retrieval timestamp, source metadata, MIME type, size and SHA-256 checksum. Raw documents stay outside Git.

## Provenance

Swiss FOCA/BAZL states that its public ICAO Annex/PANS copies are illustrative and assumes no liability for correctness or completeness. They are therefore stored as `source_reference` material and should be reconciled against the authoritative ICAO publication where a regulatory decision depends on the document.

## Currentness

A source family is not automatically current merely because a PDF is downloadable. Ingestion should capture edition/amendment/effective-date metadata and apply the retrieval policy before a document becomes an authoritative answer source.
