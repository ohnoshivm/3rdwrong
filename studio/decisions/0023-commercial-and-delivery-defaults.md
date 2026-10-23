---
id: D-0023
title: Commercial and delivery defaults
type: decision
status: approved
date: 2026-10-23
owner: founder
last_reviewed: 2026-10-23
approved_by: founder
approved_on: 2026-10-23
approval_source: founder decisions session, 2026-10-23
---

# D-0023: Commercial and delivery defaults

## Context

The Business engine, the contract templates, the offer pages and the Digital
Experience method left payment shares, feedback rounds, portfolio use, dispute
resolution, AI use, warranty and the web performance budget as founder
decisions. Without defaults, every proposal and contract would reopen them.

## Decision

These are the studio defaults. A proposal, SOW or contract may vary a default
for one project only with the founder's written approval, recorded in the
project (money and contract detail in the vault).

1. **Payment split 50 / 30 / 20** for Identity System and Digital Experience
   projects: 50% to start, 30% on approval of the chosen direction, 20% before
   final files are released. Brand Direction Sprint terms stay per proposal.
2. **Feedback: two rounds per phase** (concept, refinement, applications). Each
   round is one consolidated set of comments. Further rounds are change
   requests.
3. **Portfolio: named use after public launch.** The studio may show the work
   in its portfolio, naming the client, after the client's public launch; the
   client approves case-study wording. A confidential client may opt out in
   the contract. This governs external portfolio use only and does not change
   [D-0021](0021-client-work-public-anonymised.md): in this repository client
   work stays codenamed and anonymised until cleared.
4. **Disputes: arbitration** under the Arbitration and Conciliation Act, 1996,
   by a sole arbitrator, seated in the founder's city. The seat stays the
   placeholder `{{arbitration_seat}}` until the founder fills it.
5. **AI use:** the studio discloses AI use in its process. Any AI-generated
   material in final deliverables requires the client's written consent.
6. **Warranty:** 30 days of free defect fixes after launch. Longer support is
   a paid care plan.
7. **Digital Experience performance budget (award-grade):**
   - mobile p75 Largest Contentful Paint ≤ 2.0 s, Interaction to Next Paint
     ≤ 200 ms, Cumulative Layout Shift ≤ 0.1;
   - ≤ 2 MB transferred before first interaction, with the rest lazy-loaded;
   - a 60 fps target on a mid-range phone;
   - a complete `prefers-reduced-motion` fallback.

   Projects may set stricter budgets. A looser budget needs a founder-approved
   exception recorded in the project.

### Still open

These remain founder decisions; documents keep them as placeholders:

- cancellation fee (`{{cancellation_share}}` in the MSA);
- rates and margins (private vault only);
- care-plan pricing;
- record retention periods (ask the chartered accountant);
- studio email domain;
- off-site backup choice for the vault.

## Status

Approved by the founder on 2026-10-23. Approval sets defaults; it does not
approve offer prices, which stay hypotheses, or make the contract templates
legally reviewed. The lawyer-review note on each template still applies.

## Rationale

**Interpretation** — Fixed defaults shorten proposals and keep terms
consistent between clients. Tying payment to visible milestones (start,
direction approval, final files) matches the lifecycle gates. Two rounds per
phase is enough for considered work while keeping scope finite. Named
portfolio use matters for a new studio that must build proof; the opt-out and
the D-0021 boundary protect confidential clients. A strict performance budget
makes "award-grade" testable instead of a claim.

## Alternatives considered

- **Payment 50 / 50:** simpler, but leaves a larger final amount at risk at
  file release.
- **Unlimited or three rounds:** more comfortable for clients, but weakens
  decision discipline and margin.
- **Anonymised portfolio only:** safer, but slows the proof the studio needs.
- **Courts instead of arbitration:** slower and less private for a small
  studio.
- **Core Web Vitals "good" thresholds only (LCP 2.5 s):** easier, but not the
  quality bar set by [D-0018](0018-design-engineering-studio.md).

## Evidence

**Documented** — Founder decisions, 2026-10-23 (founder decisions session).
**Documented** — Google's published "good" thresholds are LCP ≤ 2.5 s,
INP ≤ 200 ms and CLS ≤ 0.1 at the 75th percentile
([web.dev Web Vitals](https://web.dev/articles/vitals)); the studio's LCP
budget is deliberately stricter. **Unknown** — whether clients accept these
terms; whether the budget is achievable for every 3D-heavy concept.

## Consequences

- The [MSA](../../business/legal/master-services-agreement.md) resolves its
  portfolio (Option A with opt-out), dispute (Option A, arbitration) and AI
  (consent required) options; other options and the lawyer review remain.
- [Commercial rules](../../business/pricing/commercial-rules.md),
  [engagement operations](../../business/engagement-operations.md),
  [invoicing](../../business/finance/invoicing-and-collections.md),
  [handover and care](../../methods/handover-and-care.md), the
  [web standards](../../methods/quality/web-standards.md), the offer pages and
  the proposal, SOW and contract bundles carry these defaults as pre-filled,
  editable values.
- Performance-budget exceptions are logged in the project's `decisions.md`
  with the founder's approval.

## Revision triggers

Review after the first three signed projects, when a client refuses a default,
when a payment stage is late more than once, when a project regularly needs a
third round, when a lawyer reviews the templates, or when a project cannot meet
the performance budget without compromising the concept.
