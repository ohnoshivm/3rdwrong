---
id: D-0020
title: Taste Graph
type: decision
status: approved
date: 2026-10-23
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
approved_by: founder
approved_on: 2026-10-23
approval_source: founder instruction, 2026-10-23
---

# D-0020: Taste Graph

## Decision

Build the Taste Graph: a local PostgreSQL knowledge graph that turns the swipe file into structured, queryable taste memory. Capture the best content and assets seen online every day (landing pages, YouTube thumbnails, branding assets, copywriting, tweets, LinkedIn posts, TikToks and Instagram Reels, UI/UX components and similar), and inject it into every creative-output task as a reference pack of what to do and what not to do, with exemplars. Agents load the pack through the [`3w-taste-graph`](../../skills/3w-taste-graph/SKILL.md) skill; the [Taste Graph guide](../../taste/graph/README.md) covers setup, capture, curation and backup.

## Status

Approved by the founder on 2026-10-23. The approval covers building and using the system. The implementation defaults below are reversible choices made by the implementer, not separate founder decisions. The skill is experimental.

## Rationale

The swipe file is a reading list; a graph makes it usable at the moment of work. Linking each reference to the patterns and principles it exemplifies, and anti-patterns to the principles they violate, lets an agent retrieve a short, relevant brief instead of loading every taste document. Recording which references informed which deliverable makes influence traceable.

## Alternatives considered

- **Markdown swipe file only:** zero setup, but no ranking, relationships or capture pipeline; agents would load whole files and miss media.
- **A hosted database or vector service:** less local setup, but captured third-party material would leave the founder's machine and add a paid dependency.
- **Graph extension (Apache AGE) or embeddings (pgvector):** more expressive search, but extra installation for a v1 that full-text search, trigram matching and typed edges already serve. Kept as a later step.
- **Local PostgreSQL with typed nodes and edges:** chosen. Free, private by default, queryable and backed up with standard tools.

## Evidence

**Documented** — Founder instruction, 2026-10-23: build a knowledge graph using PostgreSQL, the swipe-file concept on a whole different level; every day capture the best content and assets seen online, and whatever AI is used for, always inject this knowledge as reference, as inspiration, as things to do and not to do.

**Interpretation** — A curated reference pack is a taste input, not evidence that any reference performs well or suits an audience. Implementation choices below were made by the implementer to satisfy the instruction.

## Consequences

Reversible implementation defaults:

- PostgreSQL 17 from Homebrew, local only; database `taste_graph` (`TASTE_GRAPH_DSN`); bundled `pg_trgm`; no embeddings in v1.
- Plain tables: `node` (types asset, brand, creator, platform, pattern, principle, technique, tone, audience, industry, project) and `edge` (exemplifies, violates, by, on, for, has_tone, related, contrasts, used_in); versioned migrations in `taste/graph/migrations/`.
- One Python CLI, `scripts/taste_graph.py`, with `psycopg` as its only dependency; captures through public oEmbed endpoints, direct image downloads and `playwright-cli` screenshots.
- Captured media and third-party text live only in `TASTE_GRAPH_HOME` (default `~/.3rdwrong/taste`) and the database. The CLI refuses a data home inside a git work tree. The repository holds code, schema, docs, the skill and a seed of public URLs and studio notes.
- No login, cookies, stored credentials, paywall or anti-bot circumvention.
- Governance: agent captures enter as `inbox`; only the founder curates. Re-adding a reference never overwrites existing analysis.

Studio rule unchanged: references are inspiration only. Extract principles; never copy layouts, assets, copy or brand identity. [D-0018](0018-design-engineering-studio.md) governs offer scope (superseding D-0002), and [D-0006](0006-rejected-own-identity-direction.md) still governs the rejected own-identity direction.

## Revision triggers

Review if captured material is ever found in a repository, if a platform's terms or public endpoints change, if the graph outgrows full-text ranking (consider local embeddings), if the founder wants capture from a phone without a desktop step, or after 90 days of use.
