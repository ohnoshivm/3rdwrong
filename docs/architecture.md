---
title: Repository architecture
type: guide
status: proposed
owner: founder
last_reviewed: 2026-10-22
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
| `taste/` | Curated aesthetic and experiential references; inspiration only, with no policy or offer change. |
| `templates/` | Reusable starts for projects, research, learning, and critique. |
| `skills/` | Experimental, structured AI workflows. |
| `projects/` | Internal identity exploration and sanitised examples. |
| `experiments/` | Explicit hypotheses and documented outcomes. |
| `business/` | Proposed engagement operations. |
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

This repository does not include a custom database, CMS, client portal, CRM, design-asset hosting service, automation platform, or generated case-study system. Those would add ongoing maintenance before the studio has a need for them. Private client operations remain outside this public repository.
