---
title: Sales department
type: guide
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# Sales department

Qualify discovery through signed work: proposals, pricing, deal strategy and pipeline forecasting.

Status: proposed registry routing. Source review does not establish live tool performance, licence clearance, runtime connectivity or founder approval.

40 tools; 12 lead, 7 specialist, 21 bench, 0 parked, 0 excluded; 19 active / 21 library.

## Sub-departments → jobs → leads

### discovery-qualification

| Job | Lead(s) |
| --- | --- |
| `meeting-prep` | `sales:prepare-for-meeting` |
| `discovery-calls` | `agency:sales-discovery-coach` |
| `deal-qualification` | `agency:sales-coach` |

### proposals-pitches

| Job | Lead(s) |
| --- | --- |
| `proposal-decks` | `sales:sales-presentations` |
| `business-cases` | `sales:build-business-case` |
| `seller-enablement` | `skill:sales-enablement` |

### pricing-deal-desk

| Job | Lead(s) |
| --- | --- |
| `pricing-models` | `agency:specialized-pricing-analyst` |
| `offer-packaging` | `skill:offers` |
| `deal-strategy` | `agency:sales-deal-strategist` |

### pipeline-forecasting

| Job | Lead(s) |
| --- | --- |
| `pipeline-forecast` | `agency:sales-pipeline-analyst` |
| `revenue-operations` | `skill:revops` |
| `sales-reporting` | `agency:data-consolidation-agent` |

## Specialists with activation triggers

| Tool | Job | Trigger |
| --- | --- | --- |
| `agency:sales-engineer` | `proposals-pitches/seller-enablement` | Use for sales/proposals-pitches/seller-enablement when the brief specifically requires: Senior pre-sales engineer specializing in technical discovery, demo engineering, POC scoping, competitive battlecards, and bridging product capabilities to business outcomes . |
| `sales:find-customer-quotes` | `proposals-pitches/seller-enablement` | When gathering approved, verbatim client proof for a proposal or case study. |
| `sales:follow-up-after-call` | `discovery-qualification/discovery-calls` | After a client or qualified prospect call when a draft follow-up is requested. |
| `sales:plan-deal-strategy` | `pricing-deal-desk/deal-strategy` | For an active studio opportunity with a defined buyer, scope, and decision process. |
| `sales:review-forecast` | `pipeline-forecasting/pipeline-forecast` | When reviewing a real, maintained studio pipeline and forecast. |
| `skill:pricing` | `pricing-deal-desk/pricing-models` | Use for sales/pricing-deal-desk/pricing-models when the brief specifically requires: When the user wants help with pricing decisions, packaging, or monetization strategy . |
| `skill:pricing-packaging-planner` | `pricing-deal-desk/pricing-models` | Use for sales/pricing-deal-desk/pricing-models when the brief specifically requires: Use when the user asks to "plan launch pricing", "design pricing tiers / packaging", or "set up a launch discount / early-bird offer"; produces a launch pricing and packaging plan — tier structure and naming, a value-to-price map aligned to the message house, a launch-offer ladder with a true deadline reason, beta / early-adopter pricing with a post-launch graduation path, and guarantee / refund terms — with every price claim and offer term submitted to memory/events/claims.ndjson . |

## Bench and parked summary

- **bench: 21.** `agency-mcp:crm-followup`, `agency:government-digital-presales-consultant`, `agency:grant-writer`, `agency:legal-client-intake`, `agency:report-distribution-agent`, `agency:sales-data-extraction-agent`, `agency:specialized-korean-business-navigator`, `sales:analyze-account-signals`, `sales:build-competitive-brief`, `sales:demo-exec-and-seller-dash`, `sales:find-key-internal-sources`, `sales:get-rep-call-feedback`, `sales:index`, `sales:review-rep-call-trends`, `sales:sales-leadership-dashboard`, `sales:seller-account-dashboard`, `skill:ai-agency-cofounder`, `skill:business-growth-partner`, `skill:pitch-narrative-builder`, `skill:pricing-page`, `skill:sales-enablement-kit`
- **parked: 0.** None.
- **excluded: 0.** None.

Individual reasons and activation requirements are in the [canonical registry](../../toolkit/sources/registry.json). Library means callable by explicit name after review; it is not loaded by default.

## Gaps

No lead coverage gaps.

## Counts by sub-department and role

| Sub-department | Lead | Specialist | Bench | Parked | Excluded | Active | Library | Total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| discovery-qualification | 3 | 1 | 2 | 0 | 0 | 4 | 2 | 6 |
| proposals-pitches | 3 | 2 | 13 | 0 | 0 | 5 | 13 | 18 |
| pricing-deal-desk | 3 | 3 | 3 | 0 | 0 | 6 | 3 | 9 |
| pipeline-forecasting | 3 | 1 | 3 | 0 | 0 | 4 | 3 | 7 |

## Operating contract

Use the job lead first and a specialist only on its trigger. Maker and checker must be separate people/agent instances; a reviewer never approves its own department alone. Proposed `load: active` is the desired loading policy, while the source inventory records installation presence. No physical activation was performed.

Design and Engineering prototype together early; the handoff names artefacts, constraints, budgets and evidence rather than creating a wall. Human judgement and founder approval remain separate from tool routing.
