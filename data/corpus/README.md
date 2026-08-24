# Local Aviation Document Corpus

This directory is the intended destination for documents downloaded for local document-intelligence testing.

## Important

The public repository does **not** vendor third-party regulatory PDFs by default. The source registries intentionally set `repository_binary: false` / `repo_binary: false` for source material that may have redistribution, licensing, or currency concerns.

Use the acquisition tooling to download documents locally, then ingest them into the document-intelligence pipeline.

## Layout

```text
data/corpus/
├── README.md
├── downloads/          # local downloaded PDFs/XML; ignored by Git
├── manifests/          # generated acquisition manifests/checksums
└── extracted/          # optional local text/structured output; ignored by Git
```

## Source of truth

- `skills/aviation-document-intelligence/source-manifest.yaml`
- `skills/aviation-document-intelligence/source-manifest-global.yaml`

## Rules

1. Prefer the current first-party regulator/authority source.
2. Record the source URL, publication/version date, retrieval timestamp and SHA-256 checksum.
3. Do not commit private, licensed, subscription-only or clearly copyrighted third-party binaries merely because they are downloadable.
4. For ICAO material hosted by Swiss FOCA/BAZL, retain the publisher disclaimer and treat those copies as illustrative/reference material rather than an authoritative replacement for ICAO publications.
5. Revalidate currentness before ingestion because regulator libraries change over time.
6. Keep the public repository focused on source metadata, ingestion code, tests and reproducible acquisition—not a frozen copy of every external publication.
