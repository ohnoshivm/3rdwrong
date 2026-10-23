---
id: D-0021
title: Client work public and anonymised
type: decision
status: approved
date: 2026-10-23
owner: founder
last_reviewed: 2026-10-23
approved_by: founder
approved_on: 2026-10-23
approval_source: founder decision, 2026-10-23
---

# D-0021: Client work public and anonymised

## Context

[D-0017](0017-fully-open-repository.md) made the knowledge base fully public
and required a non-public store to be chosen before the first client or
interview data exists. The delivery engine needs project records (briefs, gate
logs, decisions, status, QA and retrospectives) that the studio and its AI
agents can retrieve alongside the methods they apply. No store had been chosen.

## Decision

Client work is **public and anonymised**. Project records live in this public
repository under codenames, with client names, people, contacts, money and
client files removed. Confidential material lives in a private **vault**
outside the repository: real names, contacts, domains, contracts, invoices,
all money, raw client files and credentials.

A project enters the public repository only when its contract permits
anonymised publication (**cleared**). Otherwise its whole workspace lives in
the vault (**private**).

## Status

Approved by the founder on 2026-10-23. This decision chooses the non-public
store that D-0017 required and revises the
[publication rules](../../docs/public-private-boundary.md) accordingly. It does
not approve any specific project's clearance; each contract decides that.

## Rationale

**Interpretation** — Public anonymised records keep delivery knowledge next to
the methods it tests, so lessons compound and agents can retrieve real
operating history without seeing confidential data. Making clearance a contract
term puts the client's permission before publication rather than after it. A
local vault with a machine-readable deny-list lets the studio prevent leaks
mechanically instead of relying on memory.

## Alternatives considered

- **All client work private:** safest, but delivery history would stay outside
  the operating system, and methods would be revised without project evidence.
- **Public named case records:** maximum transparency, but incompatible with
  confidentiality obligations and personal-data law for most clients.
- **A separate private repository:** D-0017 retired this model; it fragments
  retrieval, and a private GitHub repository is still a third-party store that
  is easy to make public by mistake.

## Evidence

**Documented** — Founder decision, 2026-10-23, recorded in the delivery-engine
brief. **Unknown** — whether prospective clients will accept an anonymised
publication clause, and how often projects will be cleared.

## Consequences

- Projects are created with `bin/3w new <bundle> --cleared` (public, anonymised)
  or `--private` (vault only); there is no default. See
  [template bundles](../../templates/bundles/README.md).
- The vault lives at `THREEW_VAULT` or `~/3rdwrong-vault`, outside any git work
  tree. It holds `clients.yaml` (codename to real identity) and per-codename
  `contracts/`, `finance/`, `files/` and `private-notes/`.
- The validator blocks emails, phone numbers, currency amounts, Indian
  identifiers and non-text files in `projects/`. Locally, `bin/3w check` and an
  optional pre-commit hook also block every value in the vault's
  `clients.yaml`, anywhere in the repository.
- Proposals, contracts and invoices are vault material; the Business engine
  keeps only templates and rules public.
- Case studies naming a client need separate written permission, beyond
  clearance.
- The vault is backed up with Time Machine and an encrypted off-site copy.

## Guardrails

- Anonymisation removes combinations as well as names: sector, city, dates,
  launch events and distinctive facts can identify a client together.
- Approvers are recorded by role or code (`C1`, founder), never by name.
- A guard pass is necessary, not sufficient: a human reviews every project
  commit for identifying combinations.
- If a leak is committed, treat it as published (D-0017): remove it, rewrite
  history only with the founder's approval, tell the client when the contract
  or law requires it, and record the incident.
- Clearance can be withdrawn by the client; move the workspace to the vault and
  remove the public folder in the next commit.

## Revision triggers

Review after the first cleared project, after any leak or near miss, when a
client refuses the publication clause, when collaborators need vault access, or
when legal advice on the Digital Personal Data Protection Act, 2023 changes the
handling of client personal data.
