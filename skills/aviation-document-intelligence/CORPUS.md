# Corpus governance

The corpus is generated from first-party aviation authorities using the source manifest.

Binary files are not committed by default because:

- 6 GB is inappropriate for a normal Git repository;
- authority documents have different redistribution terms;
- current documents change and should be re-fetched from the authoritative publisher;
- reproducible checksums and source/version metadata are more valuable than unmanaged copies.

Use the CI workflow to produce a test artifact or download locally for indexing.
