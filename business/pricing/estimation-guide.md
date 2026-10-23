---
title: Estimation guide
type: guide
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# Estimation guide

**Proposed.** How to estimate effort by stage and role. This guide holds
structure and judgement only: no hours benchmarks and no money. Hours come
from the people doing the work and, over time, from the studio's own actuals
in the vault.

## Purpose

Make effort visible stage by stage so that prices, timelines and
collaborator bookings rest on the same numbers, and so estimates can be
compared with actuals after close-out.

## When it applies

From L2 Discover & scope (rough estimate to qualify budget fit) through L3
Propose (full estimate for each option), and for every change order and care
plan.

## Roles

The pricing lead (Sales — pricing-deal-desk) owns the file. Each craft lead
estimates their own stages: Strategy for research and positioning, Design for
concept and system, Engineering for build and performance, Media for asset
production, Production for management. The founder reviews and signs off.
Nobody estimates another person's craft alone.

## Inputs

Discovery notes, the offer's stage list, the option scope, collaborator
availability and the vault history of estimated versus actual hours.

## Steps

1. Render the estimate bundle into the vault:
   `$THREEW_VAULT/<codename>/finance/estimate.yaml`.
2. List stages from the offer method (tables below). Add a `management`
   stage for production, client communication and reviews.
3. For each stage, list roles that exist in `rates.yaml` and estimate hours
   for the work, including internal critique and one round of revisions per
   checkpoint unless the scope says otherwise.
4. Estimate each stage three ways: likely, best case, worst case. Record the
   likely figure; use the spread to choose the risk buffer.
5. Set `risk_buffer` from the uncertainty table.
6. List pass-through expenses: type and stock licences, plugins, hosting,
   specialist production, travel. Use `only:` for option-specific items.
7. Define options as stage subsets in `options:`. If an option needs extra
   work, add it as its own stage so it stays visible.
8. Have each craft lead confirm their numbers, then run the calculator.

## Stage structure by offer

**Identity System** (from the [offer page](../../studio/identity-system-offer.md)):

| Stage | Typical roles | Effort drivers |
| --- | --- | --- |
| discover-diagnose | founder, strategist | stakeholders, markets, material volume, interviews |
| strategy | founder, strategist | decision-makers, workshop format, sign-off rounds |
| concept | founder, designer | routes (at least three), critique cycles |
| identity-system | founder, designer, motion-designer | logo family, type, colour, image direction, verbal foundations |
| applications | designer | number and kind of applications |
| validate-deliver | designer, producer | guideline depth, asset formats, languages and scripts |
| management | founder, producer | duration, meetings, reporting cadence |

**Digital Experience** ([Digital Experience offer](../../studio/digital-experience-offer.md)):

| Stage | Typical roles | Effort drivers |
| --- | --- | --- |
| frame | founder, strategist, creative-engineer | audience tasks, content audit, integrations |
| prototype | designer, creative-engineer | the hardest interaction, target hardware |
| system-and-build | designer, frontend-engineer, creative-engineer, motion-designer | templates, components, scenes, CMS, integrations, languages |
| verify-refine | designer, frontend-engineer | browsers and devices, accessibility, performance budgets |
| release-learn | frontend-engineer, producer | deployment, training, documentation |
| management | founder, producer | duration, stakeholders |

**Brand Direction Sprint:** discover, synthesise, territories, recommend,
management. **Care plan:** monthly allowance by role plus a monitoring and
reporting stage.

## Uncertainty table

| Situation | Risk buffer |
| --- | --- |
| Repeat of a delivered scope, decision-maker engaged, content ready | 0.10 |
| Normal new project | 0.15 |
| New offer, new segment or several stakeholders | 0.20 |
| Unproven technique (new 3D or shader work), unclear content, committee decisions | 0.30, or sell a paid prototype first |

Above 0.30 the scope is not ready to price: split off a paid discovery or
prototype phase.

## Outputs

The vault estimate file, confirmed by each craft lead and ready for
[scripts/pricing.py](../../scripts/pricing.py).

## Quality gate

- [ ] Every stage of the offer method appears, or its absence is a stated exclusion.
- [ ] Every role used exists in `rates.yaml`.
- [ ] Management and review time is estimated, not assumed.
- [ ] Each craft lead confirmed their stages.
- [ ] Buffer matches the uncertainty table, with a reason if not.
- [ ] Expenses list every third-party licence named in the scope.

## Metrics

Estimate accuracy per stage and role (actual ÷ estimated hours), recorded at
L9 close-out. Persistent error above a fifth in either direction on a stage
should change how that stage is estimated.

## Failure modes

- Estimating only the craft and forgetting meetings, reviews and handover.
- One person estimating every role.
- Buffer hidden inside each line, so nobody knows the real estimate.
- Copying a previous project's hours without checking the scope differences.

## Related

[Pricing method](README.md) · [Rates and estimates format](rates-and-estimates.md) ·
[Commercial rules](commercial-rules.md)
