-- Optional production/reference extensions.
CREATE EXTENSION IF NOT EXISTS pgcrypto;
-- pgvector is intentionally optional; enable it in deployments that install pgvector.
DO $$
BEGIN
  IF EXISTS (SELECT 1 FROM pg_available_extensions WHERE name = 'vector') THEN
    EXECUTE 'CREATE EXTENSION IF NOT EXISTS vector';
  END IF;
END $$;

CREATE TABLE IF NOT EXISTS knowledge_nodes (
  node_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  node_type TEXT NOT NULL,
  canonical_key TEXT NOT NULL,
  label TEXT NOT NULL,
  authority TEXT,
  jurisdiction TEXT,
  status TEXT NOT NULL DEFAULT 'UNKNOWN',
  effective_from DATE,
  effective_to DATE,
  properties JSONB NOT NULL DEFAULT '{}'::jsonb,
  UNIQUE(node_type, canonical_key)
);

CREATE TABLE IF NOT EXISTS knowledge_edges (
  edge_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  subject_id UUID NOT NULL REFERENCES knowledge_nodes(node_id) ON DELETE CASCADE,
  predicate TEXT NOT NULL,
  object_id UUID NOT NULL REFERENCES knowledge_nodes(node_id) ON DELETE CASCADE,
  valid_from DATE,
  valid_to DATE,
  provenance JSONB NOT NULL DEFAULT '{}'::jsonb,
  UNIQUE(subject_id, predicate, object_id, valid_from, valid_to)
);

CREATE INDEX IF NOT EXISTS idx_knodes_type_key ON knowledge_nodes(node_type, canonical_key);
CREATE INDEX IF NOT EXISTS idx_kedges_subject ON knowledge_edges(subject_id);
CREATE INDEX IF NOT EXISTS idx_kedges_object ON knowledge_edges(object_id);

CREATE TABLE IF NOT EXISTS source_snapshots (
  source_id TEXT PRIMARY KEY,
  source_url TEXT NOT NULL,
  retrieved_at TIMESTAMPTZ NOT NULL,
  checksum_sha256 TEXT,
  http_etag TEXT,
  http_last_modified TEXT,
  content_length BIGINT,
  status TEXT NOT NULL DEFAULT 'UNKNOWN',
  metadata JSONB NOT NULL DEFAULT '{}'::jsonb
);

CREATE TABLE IF NOT EXISTS source_changes (
  change_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  source_id TEXT NOT NULL REFERENCES source_snapshots(source_id) ON DELETE CASCADE,
  detected_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  previous_checksum TEXT,
  current_checksum TEXT,
  change_type TEXT NOT NULL,
  summary TEXT,
  impacted_document_ids JSONB NOT NULL DEFAULT '[]'::jsonb
);
