---
title: Growth metrics
type: method
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# Growth metrics

**Proposed.** Definitions, formulas, cadence and owners for the growth
engine's measures. Feeds the [Business engine](../business/README.md)'s scorecard ([business/scorecard.md](../business/scorecard.md))
and monthly business review.

## Purpose

Show whether the studio is reaching the right people and turning
conversations into the right work — with a small set of measures the founder
can compute in minutes.

## When it applies

Weekly counts in the Friday review; full metrics monthly; channel and ICP
decisions quarterly.

## Roles

| Role | Department | Responsibility |
| --- | --- | --- |
| Metrics owner | Sales — pipeline-forecasting | Computes pipeline and conversion metrics |
| Content metrics | Marketing — content-social | Output and engagement |
| **Founder** | Sign-off | Sets targets (vault); decides actions |

## Inputs

The vault pipeline (`growth/pipeline.yaml`), win/loss reviews, the content log,
platform analytics and, for money metrics, the vault's estimates, invoices
and budgets.

## Steps

1. **Friday:** update the weekly counts.
2. **First week of the month:** compute the metrics below for the month and
   the trailing three months.
3. **Compare** with the founder's targets (vault); mark green, amber or red;
   for each red, record one cause and one action.
4. **Quarterly:** decide which channels to keep, cut or test, using source
   attribution and win/loss themes.

### Setting targets

There are no industry benchmarks here on purpose. Set the studio's own
targets from its own data: run three months to establish a baseline, then
set targets from capacity (how many projects the studio can deliver well) and
work backwards through observed conversion rates. Record targets in the vault.

### Non-money metrics (anonymised counts may be public after approval)

| Metric | Formula | Source | Cadence | Owner |
| --- | --- | --- | --- | --- |
| Leads | Count of new L0 records | Pipeline | Weekly | Sales — pipeline-forecasting |
| Leads by source | Leads with each source code ÷ leads | Pipeline | Monthly | Sales — pipeline-forecasting |
| Qualified conversations | Count of opportunities entering stage 2 Qualified | Pipeline | Weekly | Sales — discovery-qualification |
| Lead-to-qualified rate | Qualified ÷ leads, same cohort | Pipeline | Monthly, trailing 3 months | Sales — discovery-qualification |
| Discovery-to-proposal rate | Proposals presented ÷ discovery calls held | Pipeline | Monthly, trailing 3 months | Sales |
| Proposals sent | Count of proposals presented live | Pipeline | Weekly | Sales — proposals-pitches |
| Win rate | Won ÷ (won + lost) at the proposal stage, decided in the period (same definition as the Business scorecard's proposal win rate) | Pipeline, win/loss | Monthly, trailing 6 months | Sales — pipeline-forecasting |
| Win rate by source | Win rate per source code | Pipeline | Quarterly | Sales — pipeline-forecasting |
| Sales-cycle length | Median days from L0 record to contract signed, won deals | Pipeline | Quarterly | Sales — pipeline-forecasting |
| Pipeline coverage (count) | Open qualified opportunities ÷ projects the studio can start next quarter | Pipeline, capacity plan | Monthly | Sales — pipeline-forecasting |
| First-response time | Median working hours from enquiry to first reply | Inbound log | Monthly | Marketing — content-social |
| Outbound reply rate | Replies ÷ accounts contacted | Outreach log (vault) | Monthly | Outbound — outreach-sequences |
| Outbound positive-reply rate | Interested replies ÷ accounts contacted | Outreach log | Monthly | Outbound — outreach-sequences |
| Opt-out rate | Opt-outs ÷ accounts contacted | Outreach log | Monthly | Outbound — outreach-sequences |
| Content output | Pieces published ÷ pieces planned, by pillar | Content log | Monthly | Marketing — content-social |
| Engagement quality | (saves + shares + meaningful replies) ÷ reach, per piece | Platform analytics | Monthly | Marketing — content-social |
| Content-sourced enquiries | Leads with an inbound source ÷ leads | Pipeline | Monthly | Marketing — content-social |
| Proof published | Case studies published ÷ cleared projects closed | Proof log | Quarterly | Marketing — pr-awards |
| Referral asks | Asks made ÷ projects closed at L9 | Pipeline | Quarterly | Outbound — partnerships-referrals |

### Money metrics (vault only)

| Metric | Formula | Source | Cadence | Owner |
| --- | --- | --- | --- | --- |
| Pipeline value | Σ value of open opportunities by stage | Pipeline | Monthly | Sales — pipeline-forecasting |
| Weighted pipeline | Σ (value × stage probability, midpoint of the range in [pipeline](sales/pipeline.md#stages) until the studio has its own rates) | Pipeline | Monthly | Sales — pipeline-forecasting |
| Pipeline coverage (value) | Weighted pipeline ÷ revenue target for the next quarter | Pipeline, targets | Monthly | Sales — pipeline-forecasting |
| Average won deal value | Σ won value ÷ won deals | Pipeline | Quarterly | Sales — pricing-deal-desk |
| Customer acquisition cost (CAC) | (growth spend + growth hours × founder cost rate) ÷ new clients won, per quarter; growth spend = ads, awards, tools, events | Budgets, time records, pipeline | Quarterly | Sales with Operations — finance-legal |
| CAC by source | As above, allocating spend and hours to each source | Budgets, time records | Quarterly | Sales |
| Award and ad spend per qualified conversation | Spend ÷ qualified conversations from that source | Budgets, pipeline | Per test or entry | Advertising; Marketing — pr-awards |

Ratios computed from money are still money metrics; keep them in the vault
unless the founder approves publishing an aggregate.

## Outputs

Weekly counts in the weekly review; the monthly growth section of the
business review (vault); approved anonymised aggregates may be published.

## Quality gate

- [ ] Every metric computed from the vault records, not memory.
- [ ] Small samples stated ("2 of 3") rather than percentages.
- [ ] No money figure or name outside the vault.
- [ ] Each red metric has a cause and an action.

## Metrics

Share of months with the growth review completed on time.

## Failure modes

- Tracking vanity metrics (followers, impressions) instead of qualified
  conversations and wins.
- Percentages on tiny samples.
- Copying another agency's benchmarks as targets.

## Related

- [Pipeline and follow-up](sales/pipeline.md)
- [Growth engine](README.md)
- The [Business engine](../business/README.md)'s scorecard ([business/scorecard.md](../business/scorecard.md))
