---
title: Case-study pipeline
type: method
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# Case-study pipeline

**Proposed.** From L9 close-out to a published, distributed, anonymised case
study: clearance check → interview → story → visuals → publish → distribute.

## Purpose

Show how the studio thinks and what it delivered, truthfully and with the
client's permission, in a form buyers can learn from.

## When it applies

At L9 for every client project, and for self-initiated or fictional portfolio
projects (labelled as such, clearance step skipped).

## Roles

| Role | Department | Responsibility |
| --- | --- | --- |
| Writer | Marketing — pr-awards | Interview, story, publication, distribution |
| Visuals | Media; Design and Engineering | Images, film, interaction captures, technical notes |
| Clearance | Production — handover-retention | Checks the contract clause and permissions |
| Craft review | Design and Engineering leads | Accuracy of every craft and technical claim |
| **Founder** | Sign-off | Publication decision |

## Inputs

The contract's publication clause and clearance (vault); retrospective;
project decisions, routes and QA records; the client's feedback; project files.

## Steps

1. **Clearance check (D-0021).** Confirm the contract permits publication
   ("cleared") and what it covers: anonymised only, or named with separate
   written permission; embargo date; assets excluded. If not cleared, stop:
   keep the material in the vault and record "parked: not cleared". If the
   client has not launched, wait for the launch date.
2. **Interview (30 minutes, optional).** With the client's agreement, ask:
   the situation before, why they chose to act, what changed in use, what
   they would tell a peer. Record answers in the vault; quotations are
   testimonials and follow the [testimonial process](testimonials.md).
3. **Story.** Render the `case-study` bundle with `--cleared` to
   `projects/<codename>/case-study.md`. Tell it as decisions: challenge,
   insight, alternatives, selected idea, system, applications,
   implementation evidence, outcomes or stated hypotheses, learning. Describe
   the client by sector and stage, never by name, unless written permission
   to name them exists.
4. **Visuals.** Brief Media with a shot list: system overview, rules in use,
   applications in context, motion or interaction captures, one honest
   "before" only if the client agrees. Remove anything identifying from
   anonymised cases (logos, names, addresses, people, distinctive products).
5. **Review.** Craft leads check accuracy; a second reader checks for
   identifying combinations; the anonymity guard (the Delivery engine's
   `3w check`) passes; the founder approves. If the case names the client,
   send the client the final draft for factual review.
6. **Publish** on the studio site or journal first; then Behance.
7. **Distribute** through the [repurposing ladder](../content/production-workflow.md#repurposing-ladder-one-project-many-assets)
   and, for digital work, consider an [award entry](awards.md). Share the
   published link with the client.

## Outputs

`projects/<codename>/case-study.md` (anonymised, public); full-resolution
assets and any named version in the vault until named publication is permitted.

## Quality gate

- [ ] Clearance recorded; scope of permission respected; embargo passed.
- [ ] No name, person, contact, money or identifying combination in an
      anonymised case.
- [ ] Every outcome evidenced or labelled **Hypothesis**; no causation implied.
- [ ] Self-initiated or fictional work labelled at the top.
- [ ] Craft claims checked; accessibility of the published page checked.
- [ ] Founder approved.

## Metrics

Share of cleared projects with a published case study; days from L7
acceptance to publication; enquiries citing a case study.

## Failure modes

- Writing the case study months later, when details are lost — start at L9.
- Anonymising the name but leaving identifying details.
- A gallery with no decisions.
- Claiming results the client has not measured.

## Related

- [Proof engine](README.md)
- [Case-study template](../../templates/case-studies/case-study.md) (the
  single-file reference structure)
- [Portfolio strategy](../../studio/portfolio-strategy.md)
- [Publication rules](../../docs/public-private-boundary.md)
