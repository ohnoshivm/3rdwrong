---
title: Pipeline and follow-up
type: method
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# Pipeline and follow-up

**Proposed.** Pipeline stages with exact entry and exit definitions, starting
probability ranges, the private pipeline record and a follow-up cadence that
is persistent without being pushy.

## Purpose

Know at any moment which opportunities are real, what happens next on each,
and whether there is enough qualified work ahead — without guessing and
without chasing people who have said no.

## When it applies

From the first L0 record until an opportunity is won, lost or parked.

## Roles

| Role | Department | Responsibility |
| --- | --- | --- |
| Pipeline owner | Sales — pipeline-forecasting | Keeps every record current; runs the Friday update |
| Opportunity owner | Sales — discovery-qualification | Next action and follow-up on each opportunity |
| **Founder** | Sign-off | Reviews the pipeline weekly; approves stage moves into Proposal and Won |

## Inputs

Lead, qualification and discovery records; proposal and contract status from
the [Business engine](../../business/README.md).

## Steps

1. **Keep one record per opportunity** in the vault's `growth/pipeline.yaml`.
2. **Move stages only on the exit evidence** in the table below — never on
   feeling.
3. **Every open record has a next action and a date.** No date means the
   opportunity is not being worked.
4. **Friday update:** move stages, apply follow-ups due, close stale records,
   and copy anonymised counts into the weekly review.
5. **Monthly:** compute pipeline metrics from the vault
   ([growth metrics](../metrics.md)).

### Stages

Probabilities are **Hypothesis** starting ranges for weighting the pipeline,
not industry benchmarks. Replace them with the studio's own stage-to-win rates
once at least ten opportunities have closed from each stage.

| Stage | Lifecycle | Entry | Exit (to next stage) | Probability range |
| --- | --- | --- | --- | --- |
| 1 Lead | L0 | Record created with codename, source and need | Qualification conversation held and scored | 0–5% |
| 2 Qualified | L1 | Founder decision "pursue" | Discovery call held | 5–15% |
| 3 Discovery | L2 | Discovery call held | Client confirmed the written summary; feasibility confirmed | 15–30% |
| 4 Proposal | L3 | Proposal presented live to the decision-maker | Client chooses an option, or declines | 30–60% |
| 5 Contracting | L4 | Client verbally accepts an option | Contract signed and deposit received | 70–90% |
| Won | L4 exit | Contract signed and deposit received | Hands to Delivery (L5) | 100% |
| Lost | Any | Client declines, chooses another provider, or the studio declines | [Win/loss review](win-loss.md) filed | 0% |
| Not yet | Any | Real interest, but a named condition must change first | Condition met (re-enter at the earlier stage) or check-back date passes twice (close as lost) | Excluded from weighting |

### Private record format

The vault file holds names and values; this public example uses the fictional
client and placeholder numbers with no currency.

```yaml
# $THREEW_VAULT/growth/pipeline.yaml  (private; never commit)
- codename: stillsoil-atelier
  created: 2026-10-23
  source: referral-network
  offer: identity-system
  stage: 3-discovery
  qualification_score: 225
  value_band: 0          # deal value in the studio's currency, vault only
  decision_date: 2026-11-20
  next_action: send discovery summary
  next_action_date: 2026-10-24
  notes_path: stillsoil-atelier/private-notes/
```

### Follow-up cadence

Each follow-up must carry something useful — an answer, a relevant example, a
clarified option — or a simple, honest check-in. Never invent deadlines,
"last chance" offers or expiring discounts.

| Situation | Cadence | Stop when |
| --- | --- | --- |
| Inbound enquiry, no reply to your first answer | Day 3, then day 10 | Two follow-ups without reply → mark "not yet" with a 60-day check-back |
| Discovery summary sent, not confirmed | Day 2, then day 6 | Confirmed or corrected; otherwise ask whether priorities changed |
| Proposal presented, no decision | Day 2 (questions?), day 7 (anything to clarify for the decision-maker?), day 14 (close the loop: "I'll assume timing has moved — happy to pick this up when it suits") | Decision, or after day 14 → "not yet" or lost |
| "Not yet" | At the agreed check-back date, once | No reply → close as lost, no further contact unless they return |
| Explicit no or opt-out | None | Immediately: record the reason, stop all contact |

Outbound sequences have their own cadence in the [outbound system](../outbound/README.md).

## Outputs

The vault pipeline; weekly anonymised counts (leads, qualified, discovery,
proposals, won, lost) in the weekly review; monthly metrics.

## Quality gate

- [ ] Every open opportunity has a stage, next action and date.
- [ ] Stage moves match the exit evidence.
- [ ] No follow-up after an explicit no or opt-out.
- [ ] No deal value, name or contact outside the vault.

## Metrics

Pipeline coverage, sales-cycle length, stage-to-stage conversion, win rate —
definitions in [growth metrics](../metrics.md).

## Failure modes

- Zombie opportunities inflating coverage — close them.
- Probabilities treated as forecasts before the studio has its own data.
- Follow-ups that pressure ("only two slots left") instead of helping.
- Pipeline kept in a public issue tracker or spreadsheet link in the repo.

## Related

- [Sales system](README.md)
- [Win/loss review](win-loss.md)
- The [Business engine](../../business/README.md)'s scorecard ([business/scorecard.md](../../business/scorecard.md)) and operating
  rhythm ([business/operating-rhythm.md](../../business/operating-rhythm.md))
