# Ingestion Quickstart

## Local

```bash
python -m pip install -r skills/aviation-document-intelligence/requirements.txt
python skills/aviation-document-intelligence/scripts/download_corpus.py \
  --manifest skills/aviation-document-intelligence/source-manifest.yaml \
  --output data/corpus
```

Target a small test set first:

```bash
python skills/aviation-document-intelligence/scripts/download_corpus.py \
  --only easa-ear-tco-2026-07 \
  --only kcaa-safety-management-2018 \
  --only faa-ac-43-13-1b
```

## What the downloader does

1. Reads the official-source manifest.
2. Resolves direct URLs or downloadable assets from official publisher pages.
3. Downloads into authority/source-specific folders.
4. Calculates SHA-256 checksums.
5. Records version/source metadata in `data/corpus/manifest.jsonl`.
6. Writes failures separately so one unavailable publisher does not destroy the whole run.

## Important

The downloader is intentionally separate from indexing. This allows the same raw corpus to be fed into different parsers, embedding models and search engines without repeatedly downloading authoritative sources.
