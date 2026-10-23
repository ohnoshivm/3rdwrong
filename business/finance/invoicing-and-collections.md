---
title: Invoicing and collections
type: method
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# Invoicing and collections

**Proposed.** How the studio bills and gets paid from L4 Contract & deposit to
L9 Close-out. Payment-term lengths and shares are founder decisions recorded
in the MSA and vault; this page holds the process.

## Purpose

Get paid on time without awkwardness: money conversations happen at the
proposal, payment events are tied to visible milestones, and reminders run
on a schedule rather than on mood.

## When it applies

Every client invoice: deposit (L4), milestone invoices (L6), final invoice
before final file release (L7), care-plan invoices (L8) and change orders.

## Roles

| Role | Department | Responsibility |
| --- | --- | --- |
| Billing | Operations — finance-legal | Raises invoices, tracks receivables, sends reminders |
| Client contact | Production — client-experience | Warns the client of upcoming milestones and invoices |
| **Founder** | Sign-off | Approves every invoice before it is sent; decides work pauses |

## Inputs

The signed SOW payment milestones, the vault invoice schedule, the
[Indian tax basics](india-tax-basics.md) invoice must-haves, any change
orders.

## Steps

1. **Schedule at signature.** When the SOW is signed, create the vault
   invoice schedule: every milestone, its trigger and expected date.
2. **Deposit before kickoff.** Issue the deposit invoice on signature. Work
   and kickoff (L5) start only when the deposit has cleared. No exceptions
   without founder approval recorded in the vault.
3. **Milestone invoices.** Raise each invoice on the day its trigger occurs
   (a sign-off, a delivery, a date). Render from the
   [invoice bundle](../../templates/bundles/invoice/) into
   `<codename>/finance/invoices/`, generate the formal invoice in the
   accounting tool, and attach both to the client email.
4. **Final invoice before release.** Final source files and assignment of
   rights are released when the final invoice is paid (MSA clause 6.2).
   Share previews and staging links before then, not masters.
5. **Tell the client first.** The client contact mentions each upcoming
   invoice at the milestone review: "Sign-off today triggers the second
   invoice; it will arrive this afternoon."
6. **Reminder cadence** (from the invoice date, adjust to agreed terms):

   | When | Action | Tone |
   | --- | --- | --- |
   | Sent | Invoice with milestone, due date and payment details | Matter-of-fact |
   | 3 days before due | Friendly reminder with the invoice attached | Helpful |
   | Due date + 1 | Note that payment is due; ask if anything blocks it | Direct |
   | Due + 7 | Founder call or message to the decision-maker | Personal |
   | Due + MSA pause threshold | Written notice of work pause under MSA 5.6 | Formal |
   | Due + 30 after pause | Founder decides: payment plan, suspension, recovery or legal notice | Decision |

7. **Work pause.** A pause is a written notice, not a silent slowdown. State
   the overdue amount (in the private email only), the clause, what is
   paused, and what restarts work. Timelines extend by the pause.
8. **Record receipts.** On payment: record date, amount, bank reference, TDS
   deducted and certificate expected, and for foreign payments the inward
   remittance advice (FIRA) or e-BRC reference. Transfer the tax set-aside
   the same week ([finance](README.md)).
9. **Collaborators paid on time.** Pay collaborator invoices per their
   agreement, independent of client delays unless the agreement says
   otherwise. Late client payment is the studio's problem.

## Outputs

Vault: invoice schedule, invoice records, receipts, reminder log. Accounting
tool: formal invoices. Nothing in the repository.

## Quality gate

- [ ] Invoice schedule created at signature.
- [ ] Deposit cleared before kickoff.
- [ ] Each invoice raised on its trigger day and approved by the founder.
- [ ] Invoice carries every must-have field ([tax basics](india-tax-basics.md#invoice-must-haves)).
- [ ] Reminders sent on schedule and logged.
- [ ] Final files released only after the final invoice is paid.
- [ ] Receipt recorded and tax set-aside transferred within a week.

## Metrics

Days sales outstanding, share of invoices paid by due date, overdue
receivables, invoices raised on trigger day. Definitions in the
[scorecard](../scorecard.md).

## Failure modes

- Starting work before the deposit clears "to keep momentum".
- Invoicing at month-end instead of on the trigger; the client's cycle adds weeks.
- Releasing master files before final payment.
- Reminders that apologise; late payment becomes normal.
- Forgetting TDS certificates, then paying tax twice in effect.

## Related

[Master services agreement](../legal/master-services-agreement.md) ·
[Indian tax basics](india-tax-basics.md) · [Finance](README.md) ·
[Commercial rules](../pricing/commercial-rules.md)
