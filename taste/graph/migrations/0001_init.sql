-- Taste Graph v1: nodes and typed edges on plain PostgreSQL.
-- Applied once by `scripts/taste_graph.py init`; never edit after release, add a new migration instead.

CREATE EXTENSION IF NOT EXISTS pg_trgm;

-- array_to_string is only STABLE in general; for text[] it is safe to treat as immutable,
-- which lets the search vector be a stored generated column.
CREATE FUNCTION tg_tags(text[]) RETURNS text
LANGUAGE sql IMMUTABLE PARALLEL SAFE
AS $$ SELECT coalesce(array_to_string($1, ' '), '') $$;

CREATE TABLE node (
    id          bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    type        text NOT NULL CHECK (type IN (
                    'asset', 'brand', 'creator', 'platform', 'pattern', 'principle',
                    'technique', 'tone', 'audience', 'industry', 'project')),
    slug        text NOT NULL CHECK (slug ~ '^[a-z0-9]+(-[a-z0-9]+)*$'),
    title       text NOT NULL CHECK (title <> ''),
    body        text NOT NULL DEFAULT '',          -- the studio's analysis
    url         text CHECK (url IS NULL OR url ~ '^https?://'),
    url_norm    text,
    kind        text CHECK (kind IN (
                    'landing_page', 'website', 'ui_component', 'thumbnail', 'brand_asset', 'copy',
                    'tweet', 'linkedin_post', 'tiktok', 'reel', 'short_video', 'ad', 'email', 'other')),
    verdict     text CHECK (verdict IN ('exemplar', 'anti_pattern', 'mixed')),
    score       smallint CHECK (score BETWEEN 1 AND 5),
    status      text NOT NULL DEFAULT 'inbox' CHECK (status IN ('inbox', 'curated', 'archived')),
    captured_by text NOT NULL DEFAULT 'agent' CHECK (captured_by IN ('founder', 'agent')),
    media       jsonb NOT NULL DEFAULT '[]' CHECK (jsonb_typeof(media) = 'array'),
    content     text NOT NULL DEFAULT '',          -- captured third-party text: private
    tags        text[] NOT NULL DEFAULT '{}',
    props       jsonb NOT NULL DEFAULT '{}' CHECK (jsonb_typeof(props) = 'object'),
    created_at  timestamptz NOT NULL DEFAULT now(),
    updated_at  timestamptz NOT NULL DEFAULT now(),
    search      tsvector GENERATED ALWAYS AS (
                    setweight(to_tsvector('english', title), 'A')
                    || setweight(to_tsvector('english', tg_tags(tags)), 'A')
                    || setweight(to_tsvector('english', replace(coalesce(kind, ''), '_', ' ')), 'B')
                    || setweight(to_tsvector('english', body), 'B')
                    || setweight(to_tsvector('english', content), 'D')
                ) STORED,
    UNIQUE (type, slug),
    CHECK (type = 'asset' OR kind IS NULL)
);

CREATE UNIQUE INDEX node_asset_url_norm ON node (url_norm) WHERE type = 'asset' AND url_norm IS NOT NULL;
CREATE INDEX node_search ON node USING gin (search);
CREATE INDEX node_title_tags_trgm ON node USING gin ((title || ' ' || tg_tags(tags)) gin_trgm_ops);
CREATE INDEX node_type_status ON node (type, status);

CREATE TABLE edge (
    src        bigint NOT NULL REFERENCES node (id) ON DELETE CASCADE,
    rel        text NOT NULL CHECK (rel IN (
                   'exemplifies', 'violates', 'by', 'on', 'for', 'has_tone',
                   'related', 'contrasts', 'used_in')),
    dst        bigint NOT NULL REFERENCES node (id) ON DELETE CASCADE,
    note       text NOT NULL DEFAULT '',
    weight     real NOT NULL DEFAULT 1,
    created_at timestamptz NOT NULL DEFAULT now(),
    PRIMARY KEY (src, rel, dst),
    CHECK (src <> dst)
);

CREATE INDEX edge_dst ON edge (dst, rel);

CREATE FUNCTION tg_touch() RETURNS trigger LANGUAGE plpgsql AS $$
BEGIN
    NEW.updated_at := now();
    RETURN NEW;
END $$;

CREATE TRIGGER node_touch BEFORE UPDATE ON node FOR EACH ROW EXECUTE FUNCTION tg_touch();
