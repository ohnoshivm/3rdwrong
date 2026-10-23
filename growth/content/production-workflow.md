---
title: Content production workflow
type: method
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# Content production workflow

**Proposed.** From idea to measured piece: idea → brief → reference pack →
produce → review → publish → measure, plus the repurposing ladder and the
content calendar.

## Purpose

Make every published piece deliberate and reviewed, and get the most value
from each project without lowering the bar.

## When it applies

Every piece of studio content in the [content system](README.md).

## Roles

| Role | Department | Responsibility |
| --- | --- | --- |
| Content lead | Marketing — content-social | Ideas backlog, briefs, calendar, publishing, measurement |
| Producer | Media; Design or Engineering for craft material | Produces visuals, motion, film, captures |
| Reviewer | Design or Engineering lead; Marketing — studio-brand-voice | Craft accuracy; voice and editorial quality |
| **Founder** | Sign-off | Approves before publishing |

## Inputs

Ideas backlog; cleared project material; the [Taste Graph](../../skills/3w-taste-graph/SKILL.md); the
[content pillars](README.md#content-pillars).

## Steps

1. **Idea.** Add to the backlog with pillar, channel and the one thing the
   reader should take away. Good sources: questions from discovery calls
   (anonymised), decisions made in projects, critique sessions, rejected
   routes, build problems solved.
2. **Brief.** Render the `content-brief` bundle to
   `growth/content/briefs/<date>-<slug>.md`: pillar, channel, audience,
   takeaway, evidence and sources, clearance status, format, references,
   due date, owner.
3. **Reference pack.** Load [3w-taste-graph](../../skills/3w-taste-graph/SKILL.md)
   and run `uv run scripts/taste_graph.py pack "<brief>"` for this format.
   State which principles you will apply and which don'ts you will avoid.
   Record the references used; extract principles rather than copying layouts,
   assets, copy or distinctive sequences. If the pack is unavailable, stop and
   report the gap; never fabricate a pack.
4. **Produce.** Make the piece at the channel's native format. Write alt text
   and captions as you go.
5. **Review.** Craft lead checks accuracy; voice reviewer checks clarity and
   the [voice constraints](README.md#voice-placeholder-pending-d-0012); a
   clearance check confirms no identifying client detail. Founder approves.
6. **Publish** on the calendar date. Link back to the journal or case study
   where useful. Respond to comments within a working day
   ([inbound handling](inbound.md)).
7. **Measure** after 7 and 30 days in the monthly content log: reach,
   meaningful replies, saves or shares, profile visits, enquiries. Note one
   learning per piece.

### Repurposing ladder: one project, many assets

Start at the top only when the project is cleared for publication (see
[case studies](../proof/case-studies.md)). Each rung is a separate brief.

| Rung | Asset | Channel | Typical source material |
| --- | --- | --- | --- |
| 1 | Full case study | Journal / studio site | The whole story |
| 2 | Behance project | Behance | Case-study visuals and captions |
| 3 | Award submission | Award platforms (digital work) | Live site, case-study film |
| 4 | Founder essay on the key decision | Journal, LinkedIn long post | Strategy and selected-idea sections |
| 5 | System breakdown carousel | Instagram, LinkedIn | Identity rules and applications |
| 6 | Motion or interaction clip | Instagram, X, Dribbble | Screen recordings, motion studies |
| 7 | Build note | X, journal | An engineering problem and its solution |
| 8 | Process post: rejected route and why | LinkedIn, Instagram | Alternative territories |
| 9 | Talk or community share | Events, communities | Any of the above |

Uncleared projects can still feed rungs 4, 7 and 8 when the lesson is
generalised and nothing identifies the client; the founder decides.

### Content calendar

Keep a single calendar (a table in the monthly content log or the studio's
planning tool, per [business/tooling.md](../../business/tooling.md)). Plan a month ahead and fix one week
ahead.

| Column | Meaning |
| --- | --- |
| Week | ISO week |
| Pillar | One of the four pillars; aim for at least three pillars a month |
| Channel | Primary channel |
| Piece | Working title |
| Brief | Link to the brief |
| Owner | Department and person |
| Status | idea, briefed, in production, in review, scheduled, published |
| Result | 30-day note |

Fictional example row: `2026-W45 | Identity systems | Instagram | "One rule,
ten applications" (self-initiated) | brief link | Marketing | in review | —`.

## Outputs

Briefs in the repository; published pieces; the monthly content log.

## Quality gate

- [ ] Brief exists and states the takeaway.
- [ ] Reference pack recorded; no imitation.
- [ ] Craft, voice and clearance reviews done; founder approved.
- [ ] Alt text and captions present.
- [ ] 30-day result recorded.

## Metrics

Pieces published against plan; pillar balance; engagement quality; enquiries
attributed to content ([growth metrics](../metrics.md)).

## Failure modes

- Skipping the brief, so the piece has no point.
- Repurposing by copy-paste instead of rewriting for the channel.
- Publishing project material ahead of clearance.
- Never looking at results, or chasing reach over enquiries.

## Related

- [Content system](README.md)
- [Case studies](../proof/case-studies.md)
- [Taste practice](../../methods/taste-practice.md)
