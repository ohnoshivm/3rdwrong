---
title: "Handoff: delivery to marketing"
type: checklist
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# Handoff: delivery to marketing

After acceptance, Production hands Marketing what it needs to tell the project's story truthfully, within the client's permission. Happens at L9 ([case studies](../../growth/proof/case-studies.md), [testimonials](../../growth/proof/testimonials.md), [awards](../../growth/proof/awards.md)). If the project is not cleared, the handoff stops at the permission check and the material stays in the vault, recorded as "parked: not cleared".

- **From:** Production / handover-retention (clearance) with Design and Engineering (craft material).
- **To:** Marketing / pr-awards and content-social (writer: `agent:creative-writer` with `skill:content-writer`); Media for visuals under Design's direction.
- **Acceptance checker:** the founder for clearance; `skill:content-quality-auditor` run by an instance that did not write the piece; Design and Engineering leads for craft accuracy.

## Permissions checklist (first, always)

- [ ] Contract publication clause and clearance read from the vault: **cleared** or **private** ([D-0021](../../studio/decisions/0021-client-work-public-anonymised.md)).
- [ ] Scope of permission: anonymised only, or named with separate written permission (stored in the vault).
- [ ] Embargo: the client's public launch date has passed (D-0023 named portfolio use applies only after public launch).
- [ ] Assets excluded by the client, listed.
- [ ] Client approval of case-study wording where the client is named (D-0023).
- [ ] Testimonial quotations approved verbatim by the person quoted.

## Artefact checklist (sender)

- [ ] `retro.md` and the decision log, for the story of decisions: challenge, insight, alternatives, selected idea, system, applications, implementation evidence.
- [ ] Route records, including rejected routes and why (only what the permission covers).
- [ ] QA and measurement records that support any technical claim, labelled lab or field with dates.
- [ ] Approved finals and process material, with identifying elements listed for removal in anonymised cases (logos, names, addresses, people, distinctive products).
- [ ] Shot list inputs for Media: system overview, rules in use, applications in context, motion or interaction captures.
- [ ] Outcomes only where evidence and permission exist; otherwise record outcome as Unknown. A future outcome expectation may be labelled Hypothesis, never presented as a result.

## Acceptance checks (Marketing)

- [ ] Every claim traces to a record; no invented results or statistics.
- [ ] Repository records always use codenames and non-identifying descriptions. Separate written naming permission applies to an external portfolio/award entry only; it never authorises names or client files in this repository.
- [ ] `bin/3w check` passes and a second reader has checked identifying combinations.
- [ ] Award entries are free submissions only for now ([D-0024](../../studio/decisions/0024-growth-defaults.md)).
- [ ] [`skill:3w-awards-submission`](../../toolkit/cards/marketing/pr-awards/skill--3w-awards-submission.md) leads any award proposal: official criteria/deadline/fee verified, permission and credits settled, founder approves before submission. Marketing never infers award standing from a QA score.
- [ ] Media uses [`skill:3w-image-production`](../../toolkit/cards/media/image-photo-direction/skill--3w-image-production.md) for new case-study assets and an independent [`skill:3w-image-qa`](../../toolkit/cards/media/image-photo-direction/skill--3w-image-qa.md) check before publication. The permissions record covers the final crops, channels and AI use.

## Outputs

`bin/3w new case-study --cleared --codename <codename>` → `projects/<codename>/case-study.md`; testimonial record per the testimonial process; distribution per the [content workflow](../../growth/content/production-workflow.md). The founder approves publication.

## Return conditions

Return to Production when permission is unclear or the embargo has not passed; return to the craft leads when a claim lacks a record.

## Record

One handoff row in `decisions.md` ([format](README.md#handoff-record)).
