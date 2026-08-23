# Source selection strategy

The curated starter corpus intentionally spans multiple authorities and document types.

## EASA

Highest priority for SAFA/TCO and European regulatory retrieval:

- Air Operations
- Third Country Operators
- Continuing Airworthiness
- Aerodromes
- Aircrew
- Initial Airworthiness
- Ground Handling
- Information Security

## ICAO

Use public safety-report libraries and openly published first-party material. Treat commercial publications as source references unless redistribution rights are verified.

### Swiss FOCA / BAZL illustration copies

The Swiss Federal Office of Civil Aviation (FOCA/BAZL) publishes downloadable illustration copies of ICAO Annexes 1–19 and selected ICAO Procedures for Air Navigation Services (PANS) and manuals from an official Swiss government domain:

`https://www.bazl.admin.ch/en/annexes-to-the-convention-on-international-civil-aviation-icao`

The Swiss page states that the publications are provided for illustration and that the authority assumes no liability for correctness or completeness; it also points users to ICAO for commercial printouts and digital subscriptions. Therefore the corpus should store these as **public test sources**, not as an automatic substitute for the current ICAO publication channel.

Recommended metadata:

- `authority: ICAO`
- `publisher: Swiss FOCA/BAZL`
- `authorityRole: secondary_publication`
- `policy: source_reference`
- `currentness: verify_at_ingestion`

The Annex corpus should include all linked Annex 1–19 files, including multi-volume Annexes 6, 10, 14 and 16, plus the linked PANS and manuals where useful for testing.

## National authorities

The starter set includes KCAA, FAA, UK CAA, Transport Canada, NZ CAA, UAE GCAA, CASA and DGCA India.

## Testing value

This mix deliberately introduces:

- different terminology for similar concepts
- different regulatory hierarchies
- exact identifiers
- large consolidated rules
- revision/issue metadata
- historical vs current material
- jurisdiction conflicts
- technical and operational content
- tables and long-form PDFs
- multi-document authority index pages
