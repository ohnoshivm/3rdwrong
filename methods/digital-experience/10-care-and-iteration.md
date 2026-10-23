---
title: 10 Care & iteration
type: method
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# 10 Care & iteration

## Purpose

Fix defects during the warranty period, monitor the live site, and improve it
with measured iterations under a care plan, if one is agreed.

## Roles and sign-off

- **Production** (handover-retention, client-success): care channel, reports,
  care plan.
- **Engineering** (platform-performance): monitoring, fixes, updates.
- **Design:** iteration design and craft review.
- **Sign-off:** founder and `C1` close the warranty and agree or decline the
  care plan (gate DX-10; lifecycle L8 exit).

## Inputs

- Live site, handover record, warranty terms and any care plan.

## Steps

1. Triage reported issues: defect against acceptance (warranty), change
   (change control) or care-plan work.
2. Fix warranty defects within the agreed response times.
3. Review field Core Web Vitals once enough data exists and compare with
   budgets; record results.
4. Apply security and dependency updates under the care plan.
5. Propose iterations from evidence: analytics, field data, client goals.
6. At warranty end, confirm closure, remove access no longer needed and offer
   or confirm the care plan.

## Outputs

- Care log; field measurement record; iteration proposals; warranty closure
  record.

## Quality gate

- [ ] Every warranty defect fixed or dispositioned.
- [ ] Field data reviewed where available, or recorded as not verified.
- [ ] Access removed or justified under a care plan.

## Evidence required

Care log entries, measurement records with dates, closure record in
`decisions.md`.

## Failure modes

- Unlimited "small changes" absorbed as warranty.
- No monitoring, so the client reports breakages first.
- Dependencies left unpatched with no owner.

## Related

[09 Launch & handover](09-launch-and-handover.md) ·
[Handover and care](../handover-and-care.md) ·
[Learning loop](../learning-loop.md)
