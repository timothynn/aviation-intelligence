# Aviation document corpus

This directory is intentionally kept out of git via `.gitignore`.

Run the corpus downloader to fetch official-source documents into `data/corpus/`:

```bash
python -m pip install requests beautifulsoup4 pyyaml
python skills/aviation-document-intelligence/scripts/download_corpus.py
```

The generated corpus includes `manifest.jsonl` with:

- source authority
- jurisdiction
- source/version metadata
- official source URL
- resolved download URL
- retrieval timestamp
- SHA-256 checksum
- MIME type
- byte size

The GitHub Actions workflow can generate the same corpus as a short-lived workflow artifact.

Do not commit large document collections or documents whose redistribution rights have not been verified. Use the manifest and official source links as the reproducible source registry.
