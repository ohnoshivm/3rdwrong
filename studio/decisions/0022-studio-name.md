---
id: D-0022
title: Studio name
type: decision
status: approved
date: 2026-10-23
owner: founder
last_reviewed: 2026-10-23
approved_by: founder
approved_on: 2026-10-23
approval_source: founder decisions session, 2026-10-23
---

# D-0022: Studio name

## Context

Most documents, the founding blueprint and the toolkit manifests named the
studio **3RDWRONGS**. The repository, plugins and some newer pages already used
**3RDWRONG**. Two spellings of one name make the studio look unsure of itself
and split search, attribution and future trademark records.

## Decision

The company and studio name is **3RDWRONG**, everywhere. First-party documents,
decision records, studio strategy pages, methods, templates, bundles, skills,
scripts, tests, licence attribution and generated toolkit manifests use
3RDWRONG; the possessive is 3RDWRONG's, and the core offer is "The 3RDWRONG
Identity System".

Exceptions:

- The [founding source archive](../archive/founding-blueprint-v1.0.md) stays
  verbatim as historical source, with a one-line note pointing here.
- Vendored third-party content (`toolkit/vendor/`, `.claude/agents/`) is not
  edited.
- Historical repository names `3rdwrongs-os` and `3rdwrongs-private` stay as
  written; they were real repository names. The path
  `projects/internal/3rdwrongs-identity/` is also unchanged for now, so links
  stay stable.

## Status

Approved by the founder on 2026-10-23. The rename of
[positioning](../positioning.md) and [the initial ICP](../initial-icp.md) is
founder-authorised and changes only the name; their status and content are
unchanged. The meaning of the name stays open under
[D-0014](0014-meaning-of-the-name.md).

## Rationale

**Interpretation** — One spelling, chosen once, removes ambiguity for clients,
collaborators and agents. The singular already matches the repository and
plugin namespace (`3rdwrong`), so the rename aligns the documents with the
infrastructure rather than the reverse.

## Alternatives considered

- **Keep 3RDWRONGS:** would require renaming the repository, marketplace and
  plugins, and keeps the split for every existing install.
- **Allow both spellings:** keeps the inconsistency this decision removes.

## Evidence

**Documented** — Founder decision, 2026-10-23 (founder decisions session).
**Unknown** — trademark availability, domain availability and pronunciation of
"3RDWRONG"; none has been checked.

## Consequences

- Before any brand investment (identity assets, domain purchase, signage,
  printed material), run a search of the Indian Trade Marks Registry for
  "3RDWRONG" and similar marks in the relevant classes, and check domain
  availability. Record the results as a decision or an update to this record.
- Licence attribution in [LICENSING.md](../../LICENSING.md) and `LICENSE` now
  names 3RDWRONG.
- The studio email domain is still open
  ([D-0023](0023-commercial-and-delivery-defaults.md)).

## Revision triggers

Revisit if the trademark search finds a conflicting mark, the needed domains
are unavailable or unaffordable, pronunciation testing shows the name is
consistently misheard, or the own-identity project
([D-0012](0012-strategy-before-own-visual-identity.md)) recommends a change.
