---
title: 01 Discovery & audit
type: method
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# 01 Discovery & audit

## Purpose

Establish what the experience must achieve, for whom, with what content and
under which constraints, and audit what exists today. Discovery records
evidence and limits; it does not choose a concept.

## Roles and sign-off

- **Strategy** (research-perception, positioning): audience tasks, competitor
  and category context.
- **Design** (experience-design): content inventory, journeys, current-site UX
  audit.
- **Engineering** (platform-performance, product-frontend): technical audit of
  the current site, hosting, CMS, integrations and analytics.
- **Production:** input schedule and access.
- **Sign-off:** founder; client `C1` confirms facts, success criteria and the
  content plan (gate DX-01).

## Inputs

- Signed scope and anonymised brief (`projects/<codename>/brief.md`).
- The approved identity system, or the agreed identity engagement output.
- Current site, analytics access and CMS access, granted through the vault
  process.
- Content owners and the content delivery dates agreed at kickoff.

## Steps

1. Interview `C1` and content owners on goals, audiences, tasks, constraints
   and definitions of success.
2. Inventory content: pages, templates, media, languages, owners, state
   (ready, needs rewrite, missing) and delivery date.
3. Audit the current site: Core Web Vitals field data where it exists, a lab
   run on the reference mobile profile, an accessibility spot check, analytics
   and consent set-up, SEO basics, hosting and CMS.
4. Map the top three to five audience tasks and the journeys that serve them.
5. Collect references for principles only, each with a note of what it
   teaches; record sources. Never collect them as layouts to reproduce.
6. Write success criteria the client can accept against: tasks, measures and
   targets, without money.
7. List risks: content readiness, integrations, approvals, device mix.

## Outputs

- Discovery synthesis with evidence labels (Documented, Interpretation,
  Hypothesis, Unknown).
- Content inventory and delivery plan; technical audit; success criteria.
- Reference board notes (principles, not copies).
- Risks added to `risks.md`.

## Quality gate

- [ ] Every audience claim is sourced or labelled as a hypothesis.
- [ ] Content owner and delivery date exist for every page type.
- [ ] Baseline measurements recorded with device, network profile and date.
- [ ] Success criteria are observable and agreed by `C1`.
- [ ] Integrations, languages and CMS needs match the signed scope, or a
      change request is raised.

## Evidence required

Audit measurements (tool, device profile, date), content inventory, interview
notes in the vault, and `C1`'s written confirmation logged in `decisions.md`.

## Failure modes

- Designing before content exists, then forcing content into the design.
- Treating stakeholder preference as audience evidence.
- Missing an integration or language that changes the architecture later.
- Collecting reference sites as templates.

## Related

[Method index](README.md) · [02 Experience strategy & concept](02-experience-strategy-and-concept.md) ·
[Perception-to-identity map](../perception-to-identity-map.md) ·
[Web standards](../quality/web-standards.md)
