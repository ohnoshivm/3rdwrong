---
title: Pricing method
type: method
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# Pricing method

**Proposed.** How 3RDWRONG turns a scoped opportunity into priced options the
founder approves. Prices are set by the value of the outcome to the client,
checked against cost so that no project loses money, and kept in the vault.

## Purpose

Charge for the decision and the outcome, not the hours, while proving with
arithmetic that every option clears the studio's margin and cash needs. One
repeatable method for every offer means prices can be compared, defended in a
live presentation and improved from win/loss evidence.

## When it applies

At L3 Propose, after L2 Discover & scope has produced an agreed problem,
outcomes and scope boundary. Also for change orders (L6), care plans (L8) and
any renewal. Never price before discovery: a number without scope is a guess
the client will hold you to.

## Roles

| Role | Department | Responsibility |
| --- | --- | --- |
| Pricing lead | Sales — pricing-deal-desk | Runs the estimate and calculator, drafts options |
| Craft leads | Design, Engineering, Strategy | Estimate hours for their stages and roles |
| Producer | Production — producing-pm | Checks timeline, dependencies and collaborator capacity |
| Finance | Operations — finance-legal | Checks cash, tax set-aside and payment schedule |
| **Founder** | Sign-off | Approves the value price, options and any exception |

In a founder-only week the founder holds every role; the steps still apply.

## Inputs

- Discovery output: problem, outcomes, decision-maker, constraints, scope boundary.
- The offer page: [Identity System](../../studio/identity-system-offer.md),
  [Brand Direction Sprint](../../studio/brand-direction-sprint.md), the
  [Digital Experience offer](../../studio/digital-experience-offer.md) or a care plan.
- The published ranges in [pricing hypotheses](../../studio/pricing.md) as a
  public sanity check only; they are unvalidated.
- Vault `rates.yaml` ([format](rates-and-estimates.md)) and a new estimate
  rendered from the estimate bundle.

## Steps

1. **Scope.** Write the deliverable list and exclusions in the client's
   language. Mark every unknown that could move effort by more than a day.
2. **Value.** Record in the vault what the outcome is worth to the client:
   the decision it unlocks, the cost of getting it wrong or late, what they
   would otherwise spend (hire, in-house time, a bigger agency), their stated
   budget and the strategic value to the studio (portfolio, segment, award
   potential). Label each point Documented, Interpretation, Hypothesis or
   Unknown. Value sets the ceiling; cost sets the floor.
3. **Estimate effort.** Fill hours by stage and role with the
   [estimation guide](estimation-guide.md). Add the risk buffer the guide's
   uncertainty table gives, plus pass-through expenses.
4. **Shape options.** Build good / better / best by **scope**, not by
   discounting the same work:
   - *Option A — core:* the smallest scope that solves the stated problem.
   - *Option B — recommended:* the scope the studio believes is right.
   - *Option C — extended:* B plus the next most valuable outcome (for
     example applications, motion, a prototype, a care plan).
   Each option gets a value price set by the founder within the value range.
5. **Check margin and cash.** Run
   [`uv run python scripts/pricing.py "$THREEW_VAULT/<codename>/finance/estimate.yaml"`](../../scripts/pricing.py).
   For each option the calculator prints cost, the floor price that meets
   target margin, the rate-card price, gross margin, effective hourly rate,
   payment schedule, tax set-aside and a verdict:
   - **GO** — margin at or above target and the first payment covers
     expenses plus first-stage collaborator cost.
   - **REVIEW** — margin between floor and target, or the cash check fails.
     The founder accepts with a written reason (strategic value, portfolio
     gap) or changes scope or schedule.
   - **NO-GO** — margin below floor. Cut scope or raise the price; never
     cut the estimate to make the number pass.
6. **Approve.** The founder reviews the three options, the verdicts and the
   value notes, then approves, edits or stops. Record the decision and reason
   in the vault estimate file.
7. **Present.** Present live per [proposals](../proposals.md). Investment lives
   in the vault investment sheet; the public proposal carries none.
8. **Learn.** After the decision, record won/lost, the option chosen and the
   reason in the win/loss log; after close-out compare estimated and actual
   hours per stage (see [scorecard](../scorecard.md)).

## Offer notes

| Offer | Value drivers | Effort shape | Price structure |
| --- | --- | --- | --- |
| Identity System | Launch or repositioning moment; cost of a weak identity across every touchpoint; years of use | Strategy-heavy front, concept and system craft, guidelines and handover | Fixed fee per option, milestone payments tied to strategy and visual sign-off |
| Digital Experience | Revenue or reputation the site carries; launch date; award ambition; maintenance burden | Prototype first, then build, QA and performance work; specialist roles (creative and frontend engineering, motion) | Fixed fee per phase; prototype can be sold as a paid first phase with a go/no-go before build |
| Brand Direction Sprint | Avoiding a wrong large commission; speed to a decision | Short, founder-led, 5–10 working days per the offer page | Single fixed fee, paid in full or mostly upfront; credit towards an Identity System is a founder decision |
| Care plan | Keeping the system or site correct, current and fast after launch | Reserved monthly hours, monitoring, small changes | Monthly or quarterly fee for a defined allowance with a minimum term; work beyond the allowance by change order |

The Digital Experience price is not set: the published pricing hypotheses
state that identity pricing is not a proxy for websites or 3D. Estimate from
the prototype and specialist needs before quoting.

## Outputs

- Vault: `<codename>/finance/estimate.yaml`, calculator output, value notes,
  founder decision, investment sheet.
- Repository: the anonymised proposal from the [proposal bundle](../../templates/bundles/proposal/).

## Quality gate

- [ ] Scope and exclusions agreed in discovery, written in the client's language.
- [ ] Value notes recorded with evidence labels.
- [ ] Every stage has hours by role; risk buffer matches the uncertainty table.
- [ ] Options differ by scope and outcome, not only price.
- [ ] Calculator run; every option GO, or REVIEW with a founder reason.
- [ ] Payment schedule front-loads enough to cover expenses and first-stage collaborators.
- [ ] Founder approval recorded in the vault.
- [ ] No amount in any repository file, commit, issue or pull request.

## Metrics

Win rate by option, average gross margin per project, effective hourly rate,
estimate accuracy (actual ÷ estimated hours per stage). Definitions in the
[scorecard](../scorecard.md).

## Failure modes

- Pricing from hours and calling it value; the client then negotiates hours.
- Options that are the same work at three prices: invites discounting.
- Shaving the estimate until the calculator says GO.
- Quoting on a call before running the method; the first number sticks.
- Ignoring collaborator cash timing: profitable on paper, short of cash in week two.
- Treating the published hypothesis ranges as a rate card.

## Related

- [Commercial rules](commercial-rules.md) — discounts, negotiation, rush, change pricing.
- [Rates and estimates format](rates-and-estimates.md).
- [Invoicing and collections](../finance/invoicing-and-collections.md).
