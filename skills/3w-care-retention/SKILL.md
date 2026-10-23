---
name: 3w-care-retention
description: Run the 3RDWRONG retention programme for past and current clients — warranty closure, care-plan proposals, scheduled care reviews, re-engagement check-ins and once-only testimonial and referral asks — following the studio's handover-and-care method. Use from L7 handover through L8 care and L9 close-out; do not use to sell unrequested work, extend warranty informally or contact clients who asked not to be contacted.
metadata:
  type: skill
  status: experimental
  owner: founder
  last_reviewed: 2026-10-23
  version: 0.1.0
---
# 3w-care-retention

## Purpose

Keep good clients well served after launch so that further work, referrals and proof come from real value — not from pressure. This skill applies [handover and care](../../methods/handover-and-care.md); it does not replace it.

## When to use

- At L7 handover, to schedule the warranty and the care conversation.
- At warranty end (30 days by default, D-0023), to close the warranty and propose or confirm a care plan.
- On each care-plan review date, and at a planned check-in after an engagement ends.

## When not to use

Do not use for live client service during a project (`agency:customer-service`) or retainer health scoring (`agency:customer-success-manager`). Do not use for prices; care-plan prices come from the Business engine and stay in the vault. Do not contact anyone who has asked not to hear from the studio.

## Inputs

- The project's `handover.md`, decisions log, warranty terms and any care plan (from the project workspace or vault).
- Care log, field measurement record and open issues.
- Client contact preferences and any earlier testimonial or referral answer.

## Dependencies

[Tool card](../../toolkit/cards/production/handover-retention/skill--3w-care-retention.md) records routing, invocation and independent checks.

Read [handover and care](../../methods/handover-and-care.md), [10 Care and iteration](../../methods/digital-experience/10-care-and-iteration.md), the [lifecycle](../../methods/lifecycle.md) L7–L9 stages, [testimonials](../../growth/proof/testimonials.md), [partnerships and referrals](../../growth/partnerships-and-referrals.md#referral-asks-l9) and [D-0023](../../studio/decisions/0023-commercial-and-delivery-defaults.md).

## Procedure

1. **Calendar.** At handover, set dates for warranty end, the care conversation (a week before warranty end) and, if no care plan, a check-in three to six months later (Hypothesis cadence; recalibrate after five clients). Dates live in the vault.
2. **Warranty closure.** Triage open issues as warranty defect, change or care work, per the method. Confirm closure in writing.
3. **Care proposal.** If the work needs ongoing support, draft a plan using the care-plan elements table (term, monitoring, maintenance, support, iteration, reporting, exclusions, access). Leave prices to the Business engine. If no plan is agreed, run offboarding and access removal.
4. **Care review** (each plan period). Summarise incidents, measurements against budgets, updates applied and evidence-based recommendations. Recommend only what evidence supports.
5. **Check-in** (no plan). One short, useful message: how the work is holding up and one observation or offer of help. No sales sequence.
6. **Proof and referrals.** Ask for a testimonial and a referral once each, only after the client has accepted the work and said it went well. Record answers; never ask twice.
7. **Record.** Log every contact, decision and answer in the vault; publish nothing identifying (D-0021).

## Evidence requirements

Care reviews cite measurements with tool and date; recommendations name the evidence behind them. Client sentiment is quoted from their own words, not inferred.

## Output

```markdown
# Care and retention: {{codename}}

**Stage:** {{warranty | care plan | ended}} · **Next date:** {{date, purpose}}

## Warranty
{{open issues by type; closure date}}

## Care plan
{{proposed | active | declined}} — elements: term, monitoring, maintenance, support, iteration, reporting, exclusions, access

## Review or check-in notes
## Asks
- Testimonial: {{not asked | asked date | answer}}
- Referral: {{not asked | asked date | answer}}

## Access status
```

## Quality checks

- Warranty is not used as an unlimited change budget.
- Each care recommendation cites evidence.
- Testimonial and referral are asked at most once each.
- Studio access is either justified by a plan or removed.
- No client identity or price appears in the public repository.

## Failure conditions

Stop when the handover record or warranty terms are missing; reconstruct them with Production first. Stop contact immediately when a client declines further contact.

## Human review

The founder approves care scope and any warranty exception. The client approves care work and any testimonial text.

## Example

**Fictional example.** Thirty days after a fictional site launch, two issues remain: one is a defect (fixed under warranty), one is a new page (change control). The client declines a care plan; offboarding removes studio access, and a check-in is set for four months later. At close-out the founder asks once for a testimonial; the client agrees and approves the exact text.
