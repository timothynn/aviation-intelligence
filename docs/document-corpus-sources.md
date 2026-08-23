# Official corpus source notes

The current manifest intentionally uses first-party publisher sources.

## EASA

EASA's Easy Access Rules catalogue currently exposes PDF, online and XML representations. Several current publications explicitly state that the XML is machine-readable and suitable for synchronisation with local applications/search databases.

High-value sources include:

- Air Operations — Revision 24, March 2026
- Third Country Operators — Revision July 2026
- Continuing Airworthiness — Revision September 2025
- Aerodromes — Revision March 2026
- Aircrew — Revision November 2025
- Initial Airworthiness and Environmental Protection — Revision November 2025
- Ground Handling — November 2025
- Information Security — Revision December 2025

## ICAO

Use ICAO's public safety-report libraries and other openly published first-party material. Do not mirror ICAO commercial publications unless redistribution rights have been verified.

## National authorities

The manifest includes public first-party material from:

- KCAA
- FAA
- UK CAA
- Transport Canada
- New Zealand CAA
- UAE GCAA
- CASA Australia
- DGCA India

## Why the manifest stores pages instead of binaries

Aviation sources change and their redistribution terms differ. The safest reproducible design is:

```text
official source page
       ↓
resolve current asset
       ↓
download locally
       ↓
SHA-256
       ↓
index
       ↓
record source/version/date
```

The raw file should remain outside git unless its redistribution rights have been explicitly verified.
