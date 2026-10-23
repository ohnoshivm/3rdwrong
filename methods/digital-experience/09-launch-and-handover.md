---
title: 09 Launch & handover
type: method
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# 09 Launch & handover

## Purpose

Release the site, verify it live, and transfer everything the client needs to
own and run it without the studio.

## Roles and sign-off

- **Engineering** (deployment-and-release): release, live verification,
  documentation.
- **Design:** usage and content guidance.
- **Production** (handover-retention): handover pack, walkthrough, acceptance
  and receipt records.
- **Sign-off:** `C1` confirms final acceptance and, separately, receipt and
  access (gate DX-09; lifecycle L7 exit).

## Inputs

- DX-08 launch approval and launch plan.

## Steps

1. Release per the launch plan; run smoke tests on production at three widths.
2. Verify live: redirects, metadata, analytics and consent, forms, CMS
   publishing, security headers, certificate.
3. Monitor errors and Core Web Vitals reporting during the first days.
4. Deliver the digital handover pack from
   [handover and care](../handover-and-care.md#digital-handover-pack).
5. Train the client's editors on the CMS with their own content.
6. Transfer ownership of accounts, domains and repositories as contracted;
   record locations in the vault.
7. Record final acceptance and receipt in `decisions.md` and `handover.md`;
   start the warranty period.

## Outputs

- Live site; handover pack; training record; acceptance and receipt records.

## Quality gate

- [ ] Live smoke tests pass at three widths.
- [ ] Every handover pack item delivered and opened by the client.
- [ ] Ownership and access transferred as contracted.
- [ ] Acceptance and receipt recorded separately.

## Evidence required

Live screenshots (vault), smoke-test notes, handover checklist, training
record, acceptance record with version.

## Failure modes

- Treating deployment as handover.
- Editors trained on dummy content who cannot publish real pages.
- Studio-owned accounts left as the only owner of client infrastructure.

## Related

[08 Performance & launch readiness](08-performance-and-launch-readiness.md) ·
[10 Care & iteration](10-care-and-iteration.md) ·
[Handover and care](../handover-and-care.md)
