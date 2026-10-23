---
title: Scorecard
type: method
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# Scorecard

**Proposed.** The metrics the studio runs on: definition, formula, data
source, cadence and owner. **Money metrics are computed from the vault and
never published.** Non-money metrics may be published only after founder
approval and only in aggregate. Targets are founder decisions recorded in the
vault; none are set here.

## Purpose

A small set of numbers that tell the founder whether the studio is winning
the right work, delivering it profitably, getting paid and improving.

## When it applies

Updated monthly in the business review; delivery and pipeline metrics glanced
at in the Friday review.

## Roles

Operations — finance-legal computes money metrics; Sales —
pipeline-forecasting computes pipeline metrics; Production computes delivery
metrics. The **founder** reviews and sets targets.

## Inputs

Vault: invoices, receipts, time records, estimates, win/loss log, collaborator
costs. Repository: project status and lifecycle stage by codename.

## Steps

1. In the first week of the month, compute each metric with the formulas
   below for the month and trailing three months.
2. Compare with the founder's targets; mark green, amber or red.
3. For each red metric, record one cause and one action in the monthly
   review.

### Money metrics (vault only)

| Metric | Formula | Source | Cadence | Owner |
| --- | --- | --- | --- | --- |
| Gross margin per project | (fees invoiced − direct costs) ÷ fees invoiced; direct costs = collaborator cost + founder hours × founder cost rate + pass-through expenses | Invoices, time records, rates.yaml | At L9 close-out; monthly for open projects | Operations — finance-legal |
| Effective hourly rate | (fees − pass-through expenses) ÷ total hours logged on the project | Invoices, time records | At close-out | Operations — finance-legal |
| Days sales outstanding | Receivables at month-end ÷ revenue invoiced in the trailing three months × days in those months | Invoices, receipts | Monthly | Operations — finance-legal |
| Revenue concentration | Largest single client's revenue ÷ total revenue, trailing twelve months | Invoices | Monthly | Operations — finance-legal |
| Overdue receivables | Sum of invoices past due date | Invoices | Weekly | Operations — finance-legal |
| Runway | Reserve balance ÷ average monthly fixed costs | Bank, books | Monthly | Operations — finance-legal |
| Tax cover | Tax account balance ÷ estimated tax liability to date | Bank, CA estimate | Monthly | Operations — finance-legal |
| Average discount | Σ (full price − agreed price) ÷ Σ full price, won deals | Estimates, SOWs | Quarterly | Sales — pricing-deal-desk |

### Non-money metrics (may be public after approval)

| Metric | Formula | Source | Cadence | Owner |
| --- | --- | --- | --- | --- |
| Utilisation | Billable hours ÷ available hours, per person | Time records | Monthly | Production — producing-pm |
| Estimate accuracy | Actual hours ÷ estimated hours, per stage | Time records, estimates | At close-out | Sales — pricing-deal-desk |
| Discovery-to-presentation days | Working days from discovery call to live proposal | Pipeline | Per proposal | Sales — proposals-pitches |
| Proposal win rate | Proposals won ÷ proposals decided | Win/loss log | Monthly, trailing 6 months | Sales — pipeline-forecasting |
| Win rate by option | Wins at each option ÷ wins | Win/loss log | Quarterly | Sales — pricing-deal-desk |
| Share of invoices paid on time | Invoices paid by due date ÷ invoices due | Invoices | Monthly | Operations — finance-legal |
| Absorbed change hours | Hours of change work not billed, per project | Time records | At close-out | Production — producing-pm |
| Checkpoints on time | Sign-offs reached by the SOW date ÷ sign-offs due | Project boards | Monthly | Production — producing-pm |
| Review queue age | Days since the oldest proposed operating-critical document was reviewed | [scripts/review_queue.py](../scripts/review_queue.py) | Monthly | Operations — knowledge-systems |

Ratios computed from money (margin as a percentage, for example) are still
money metrics: keep them in the vault unless the founder approves publishing
an aggregate.

## Outputs

Monthly scorecard in the vault finance review; agreed non-money aggregates
in public retrospectives only after approval.

## Quality gate

- [ ] Every metric uses the formula on this page.
- [ ] Money metrics stay in the vault.
- [ ] Each red metric has a cause and an action.

## Metrics

This page is the metric set. Add a metric only when a decision depends on it;
remove one that has not changed a decision in two quarters.

## Failure modes

- Tracking revenue only; margin and cash problems hide inside growth.
- Utilisation targets that squeeze out sales and learning time.
- Publishing a margin "as a percentage" and revealing price structure.

## Related

[Operating rhythm](operating-rhythm.md) · [Finance](finance/README.md) ·
[Pricing method](pricing/README.md) · [Proposals](proposals.md)
