---
title: 08 Performance & launch readiness
type: method
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# 08 Performance & launch readiness

## Purpose

Prove the build meets its budgets and is safe to launch: measured
performance, security, SEO, analytics and consent, and a rehearsed go-live and
rollback plan.

## Roles and sign-off

- **Engineering** (platform-performance, engineering-qa-security,
  deployment-and-release): measurements, security review, deployment plan.
- **Design:** confirms optimisations did not degrade craft.
- **Production:** launch plan, client communications, go/no-go meeting.
- **Sign-off:** founder and `C1` approve launch at a go/no-go review (gate
  DX-08).

## Inputs

- DX-07 pass; budgets from DX-04; production hosting and domain access through
  the vault process.

## Steps

1. Measure every key template on the reference mid-range mobile profile and
   desktop: LCP, CLS, Total Blocking Time as a lab proxy for responsiveness,
   JavaScript and transfer weight, frame time for scenes.
2. Fix budget breaches or record founder-approved exceptions under D-0023.
   Compare the built dependency/renderer stack and fallbacks with
   `stack-decision.md`; [D-0025](../../studio/decisions/0025-creative-technology-selection-policy.md)
   does not waive the performance budget. Field p75 remains Unknown until measured.
3. Review security: headers, dependency audit, form and input handling, no
   exposed secrets, least-privilege access.
4. Check SEO, metadata, social cards, sitemap, robots rules and redirects from
   any old URLs.
5. Check analytics and consent against the agreed privacy approach.
6. Write the launch plan: timing, DNS and caching, owner per step, smoke tests,
   rollback trigger and procedure.
7. Run the [launch-readiness checklist](../quality/launch-readiness-checklist.md)
   and hold the go/no-go review.

## Outputs

- Performance report with budgets against measurements; security review;
  launch plan with rollback; completed launch-readiness checklist.

## Quality gate

- [ ] Every budget met on the reference device, or exceptions approved.
- [ ] Security review complete; no high-severity finding open.
- [ ] Redirects, metadata, analytics and consent verified on staging.
- [ ] Rollback rehearsed or verified.
- [ ] Go/no-go decision logged with approvers.

## Evidence required

Measurement output with device, network profile and date; dependency audit
output; header check; launch-readiness checklist; go/no-go record. Field data
is **not verified** before launch; name who measures it afterwards.

## Failure modes

- Lab scores on a fast laptop presented as user experience.
- Launching on a Friday or before a holiday without support cover.
- No rollback plan because "it is only a website".
- Analytics firing before consent where consent is required.

## Related

[07 QA](07-qa.md) · [09 Launch & handover](09-launch-and-handover.md) ·
[Web standards](../quality/web-standards.md)
