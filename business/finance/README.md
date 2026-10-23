---
title: Finance
type: method
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# Finance

**Proposed.** Bookkeeping cadence, cash management and the finance KPIs. All
figures live in the vault; the method lives here. Billing is in
[invoicing and collections](invoicing-and-collections.md); tax orientation in
[Indian tax basics](india-tax-basics.md).

## Purpose

Know at any moment what the studio has earned, is owed, owes and can safely
spend, so that pricing, hiring and investment decisions rest on facts.

## When it applies

Continuously; reviewed weekly (cash), monthly (books and KPIs), quarterly
(margins and rates) and annually (accounts and tax).

## Roles

Operations — finance-legal keeps the books and prepares reviews. The
**chartered accountant** (external) files returns and advises. The
**founder** approves spending, transfers and every review.

## Inputs

Bank and payment-platform statements, invoices, receipts, collaborator
invoices, the vault `rates.yaml`, time records by project.

## Steps

### Bookkeeping cadence

| When | Task |
| --- | --- |
| Weekly (Friday review) | Categorise transactions; match receipts to invoices; file expense receipts; check overdue invoices |
| Monthly (first week) | Close the month: reconcile every account, reconcile TDS, prepare GST data for the CA, run the [finance-review bundle](../../templates/bundles/finance-review/) |
| Quarterly | Review project margins against estimates, rates, overheads and collaborator costs; advance-tax check with the CA |
| Annually | Accounts and income-tax return with the CA; renew the LUT; reset targets in the annual reset |

### Cash management

1. **Separate accounts.** Keep at least three: an operating account (all
   receipts and spending), a tax account and a reserve account. Never mix
   personal and studio money.
2. **Tax set-aside.** On every receipt, move the `tax_set_aside` share from
   `rates.yaml` to the tax account the same week. GST collected belongs to
   the government: set it aside in full. Agree the income-tax share with the
   CA.
3. **Runway buffer.** Hold a reserve equal to a founder-set number of months
   of fixed costs (tools, founder pay, overheads). Rebuild it before any
   discretionary spending.
4. **Pay yourself on a schedule.** The founder draws a fixed monthly amount;
   surpluses above the reserve target go to tax first, reserve second,
   discretionary third.
5. **Commitments match cash.** Book collaborators only against signed work
   with a cleared deposit.

### KPIs

Gross margin per project, effective hourly rate, utilisation, days sales
outstanding and revenue concentration are defined in the
[scorecard](../scorecard.md). Money metrics are computed in the vault and
reviewed monthly; only non-money ratios may ever appear publicly, and only
after founder approval.

## Outputs

Monthly finance review and quarterly margin review in the vault; CA filings.

## Quality gate

- [ ] Books closed by the end of the first week of each month.
- [ ] Tax and reserve transfers made for every receipt.
- [ ] Reserve at or above target, or a recovery plan recorded.
- [ ] KPIs computed with scorecard formulas.

## Metrics

Months of runway in reserve, tax account covers estimated liability, days to
close the month.

## Failure modes

- Treating the operating balance as profit; GST and income tax are inside it.
- Closing the books only at year-end; margin problems surface too late.
- Booking collaborators against a verbal yes.

## Related

[Invoicing and collections](invoicing-and-collections.md) ·
[Indian tax basics](india-tax-basics.md) · [Scorecard](../scorecard.md) ·
[Operating rhythm](../operating-rhythm.md)
