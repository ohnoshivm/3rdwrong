---
title: Repository architecture
type: guide
status: proposed
owner: founder
last_reviewed: 2026-10-23
---

# Repository architecture

The repository is a version-controlled second brain for durable studio knowledge. It keeps evidence and status visible in plain text, an inbox for quick capture, and a generated index for retrieval.

## Layout

| Path | Purpose |
| --- | --- |
| `INDEX.md` | Generated index of frontmatter documents for people and AI retrieval. |
| `inbox/` | Temporary capture area for rough public-safe notes, triaged weekly. |
| `studio/` | Positioning, offer, philosophy, roadmap, and decision records. |
| `methods/` | Engagement stages, quality practices, and the learning loop. |
| `intelligence/` | Cited studies and transferable observations from public work. |
| `taste/` | Curated aesthetic and experiential references; inspiration only. |
| `taste/graph/` | PostgreSQL migrations, public seeds, reference-pack guide and proposals; captured media and the database remain local outside Git (D-0020). |
| `templates/` | Reusable starts for projects, research, learning, and critique. |
| `templates/bundles/` | CLI-rendered project, proposal, SOW and change-order records; studio content briefs and case studies; vault-only invoice, reviews, rates, estimates, discovery, outreach and win/loss records. |
| `bin/` | `3w` workspace, vault and anonymity-check command wrapper. |
| `skills/` | Six `3w-` experimental, structured AI workflows. |
| `agents/` and `.claude/agents/` | Upstream MIT personas, pinned hashes and repo-level update instructions; excluded from knowledge indexing. |
| `projects/` | Codenamed, contract-cleared anonymised client records (D-0021) and internal exploration; no client identities, money or files. |
| `experiments/` | Explicit hypotheses and documented outcomes. |
| `growth/` | Qualification/discovery, content, outbound, proof, partnerships, advertising and acquisition metrics; named prospect records stay in the vault. |
| `business/` | Pricing, proposals, legal/IP, finance, people and operating rhythm; monetary records remain in the vault. |
| `schemas/` | Metadata rules and required repository paths. |
| `scripts/` and `tests/` | Small maintenance tools and their checks. |
| `docs/` | Onboarding, governance, workflows, and boundaries. |
| `.github/` | Contribution forms, labels, ownership, and CI. |
| `.obsidian/` | Local vault settings; ignored by Git and not part of the shared knowledge base. |

## Sources of truth

Keep one canonical home for each fact. The decision log in `studio/decisions/` wins when records conflict. Studio strategy follows it; methods explain how to work; intelligence documents what public sources support; templates provide reusable structure but do not establish facts. Link to canonical records instead of copying them.

## Why Markdown, YAML, and small Python

Markdown keeps the knowledge readable in GitHub, editors, and AI tools. YAML frontmatter makes type, status, ownership, dates, and evidence machine-readable without taking that context away from a human reader. A small Python validator can check those rules, relative links, skills, secrets, and review dates using the standard library and PyYAML.

The allowed metadata, review intervals, required paths, exemptions, and section names live in one place: [`schemas/metadata.json`](../schemas/metadata.json). The validator reads that file rather than maintaining a second copy of the policy.

## Deliberately not built

The Taste Graph uses a local PostgreSQL database outside Git. This repository does not host a CMS, client portal, CRM, design assets or a generated case-study system. Confidential client operations and all monetary records stay in the private vault; only contract-cleared anonymised project records enter the public tree.
