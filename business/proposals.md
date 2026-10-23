---
title: Proposals
type: method
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# Proposals

**Proposed.** How 3RDWRONG turns a discovery conversation into a signed
engagement: L3 Propose and L4 Contract & deposit.

## Purpose

Win the right work at the right price by showing the client that the studio
understood their problem better than anyone else they spoke to, then making
the decision easy.

## When it applies

After L2 Discover & scope confirms a qualified opportunity: a real problem, a
decision-maker in the conversation, a timeline and a budget that can reach
at least Option A. If any of those is missing, return to Growth's
qualification rather than writing a proposal.

## Roles

| Role | Department | Responsibility |
| --- | --- | --- |
| Proposal lead | Sales — proposals-pitches | Writes the proposal, books the presentation, runs follow-up |
| Pricing lead | Sales — pricing-deal-desk | Estimate, calculator, options ([pricing method](pricing/README.md)) |
| Strategy | Strategy — positioning | Problem framing and outcomes |
| Craft leads | Design, Engineering | Approach by stage, feasibility, risks |
| **Founder** | Sign-off | Approves proposal and price; presents live |

## Inputs

Discovery notes (vault), the offer page, the approved estimate and options,
relevant anonymised work to show, the client's decision process and date.

## Steps

1. **Day 0 — discovery ends.** Confirm in writing what you heard: problem,
   outcomes, constraints, decision process, and the date you will present.
   Book the presentation before leaving the call.
2. **Days 1–2 — draft.** Render the [proposal bundle](../templates/bundles/proposal/)
   to `projects/<codename>/proposal.md`. Write the problem in the client's
   words, three outcomes with observable signals, the approach by offer
   stage, and the options. Run the pricing method in parallel.
3. **Day 3 — price and review.** Founder approves options and investment
   (vault). A second reader checks the proposal against discovery notes:
   would the client recognise their problem in paragraph one?
4. **Day 4 — prepare the live presentation.** A short deck or the proposal
   page itself: problem, outcomes, approach, options, investment, next steps.
   Prepare answers to the three likeliest objections.
5. **By day 5 — present live.** Video or in person, with the decision-maker.
   Walk through the problem first and confirm it before showing options.
   Present investment live from the vault sheet; recommend Option B and say
   why. Ask which option fits and what would stop them deciding this week.
   Send the written proposal and investment sheet within an hour after.
   Never email a PDF as the first contact with the price.
6. **Follow up.** Day 2 after presenting: answer open questions. Day 5:
   short check-in on the decision. Day 10: final follow-up offering to hold
   the start window until the proposal's validity date. Then close it as
   lost or parked; stop chasing.
7. **On yes — L4.** Render the [SOW bundle](../templates/bundles/sow/) from
   the chosen option, send it with the
   [master services agreement](legal/master-services-agreement.md), issue the
   deposit invoice on signature ([invoicing](finance/invoicing-and-collections.md))
   and schedule kickoff for after the deposit clears. File signed copies in
   the vault `contracts/` folder.
8. **Win/loss review.** Within a week of every decision, record in the vault:
   outcome, option chosen, price position, decisive reason in the client's
   words, competing alternative, what to change. Review all entries monthly
   in the business review.

## Outputs

- Repository: anonymised `proposal.md` and `sow.md` under `projects/<codename>/`.
- Vault: investment sheet, signed MSA and SOW, deposit invoice, win/loss entry.

## Quality gate

- [ ] Discovery to presentation within five working days.
- [ ] Problem stated in the client's words and confirmed live before options.
- [ ] Three options differing by scope; one recommended with a reason.
- [ ] Calculator verdicts GO, or REVIEW with founder reason.
- [ ] Every assumption and exclusion explicit; strategy and visual sign-offs separate.
- [ ] Public files carry the codename only and no amounts.
- [ ] Presented live to the decision-maker; follow-up dates in the calendar.
- [ ] Win/loss entry recorded within a week of the decision.

## Metrics

Discovery-to-presentation days, proposal win rate, win rate by option, average
time to decision, share of proposals presented live. See the [scorecard](scorecard.md).

## Failure modes

- Writing before qualifying; proposals become free consulting.
- A long document about the studio instead of the client's problem.
- Emailing the price without a conversation; silence follows.
- Chasing indefinitely instead of closing the loop on day 10.
- Starting work on a verbal yes before signature and deposit.

## Related

[Pricing method](pricing/README.md) · [Commercial rules](pricing/commercial-rules.md) ·
[Legal templates](legal/README.md) · [Client acquisition](client-acquisition.md)
(L0–L2, Growth) · [Engagement operations](engagement-operations.md) (L5 onwards, Delivery)
