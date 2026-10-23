---
title: Growth engine
type: guide
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# Growth engine

How 3RDWRONG becomes known to the right people, starts the right
conversations, qualifies and wins clients, and turns finished work into proof.
**Proposed** for founder review; nothing here is approved policy until the
founder approves it.

The studio sells craft and judgement. Every growth method here protects that:
no spam, no fake urgency, no inflated claims, no invented results. A smaller,
better-qualified pipeline is the goal, not volume.

## The rule: public method, private names and money

Under D-0021 (founder decision, 2026-10-23), client work in this repository is
public and anonymised. Growth methods, templates and anonymised counts live
here. Prospect lists, the pipeline with names and deal values, outreach to
named people, discovery notes, testimonials before written permission, ad
budgets, award fees and every amount of money live in the private **vault**:
the folder named by `THREEW_VAULT`, default `~/3rdwrong-vault`.

```text
$THREEW_VAULT/
  clients.yaml                       codename -> client or prospect identity
  growth/
    pipeline.yaml                    every open and closed opportunity, with value
    accounts.yaml                    target-account list with research links
    outreach/<codename>.md           sequences to named people
    win-loss/<codename>-<date>.md    win/loss reviews
    testimonials/<codename>.md       quotations and written permissions
    budgets.yaml                     award fees, ad tests, partnership costs
  <codename>/private-notes/          discovery notes for that opportunity
```

Public files refer to prospects and clients by codename only. Examples use the
fictional client **Stillsoil Atelier** (codename `stillsoil-atelier`). See the
[publication rules](../docs/public-private-boundary.md).

## The engine

```text
positioning ──► proof ──► reach ──► conversations ──► proposals
 (studio/)     (proof/)   (content/,     (sales/: L0–L2)    (Business: L3–L4)
                          outbound/,
                          partnerships,
                          advertising)
       ▲                                                        │
       └────────────── L9: case study, testimonial, referral ◄──┘
```

1. **Positioning** says who the studio is for and what it does:
   [positioning](../studio/positioning.md), [initial ICP](../studio/initial-icp.md),
   the Identity System offer and the Digital Experience offer (D-0018). Growth
   does not change positioning; it reports evidence back to it.
2. **Proof** shows the studio can do it: case studies, testimonials, awards and
   the portfolio — [proof engine](proof/README.md).
3. **Reach** puts the proof in front of the ICP: [content](content/README.md),
   [outbound](outbound/README.md), [partnerships and referrals](partnerships-and-referrals.md)
   and, later, [advertising](advertising.md).
4. **Conversations** turn interest into qualified opportunities: the
   [sales system](sales/README.md), lifecycle stages L0–L2.
5. **Proposals** are the Business engine's L3 Propose and L4 Contract &
   deposit (business/proposals.md in the Business engine). Growth hands over a
   complete discovery record.

## Lifecycle stages served

The canonical client lifecycle (the Delivery engine's methods/lifecycle.md)
has ten stages. Growth owns four of them, fully or in part.

| Stage | Growth material | Exit gate (summary) |
| --- | --- | --- |
| L0 Lead | [Lead sources](sales/lead-sources.md), [inbound handling](content/inbound.md), [outbound](outbound/README.md) | Codename, source, one-line need and next action recorded in the vault pipeline |
| L1 Qualify | [Qualification](sales/qualification.md) | Scorecard complete, no unresolved disqualifier, founder decides pursue / not yet / decline |
| L2 Discover & scope | [Discovery call](sales/discovery-call.md), discovery-notes bundle | Problem, scope boundary, decision process, timing, budget band and risks confirmed; client confirms the summary in writing; Business hand-off pack complete |
| L9 Close-out (growth parts) | [Case studies](proof/case-studies.md), [testimonials](proof/testimonials.md), [referrals](partnerships-and-referrals.md), [awards](proof/awards.md) | Clearance checked; case study published or parked with a reason; testimonial and referral asked; award decision logged |

L3–L4 belong to the Business engine; the backbone and L5–L8 belong to the
Delivery engine.

## Who owns what

Departments follow D-0019. They are accountability structures, not headcount:
in a founder-led studio one person may hold several. The founder signs off
everything that leaves the studio under its name.

| Department (D-0019) | Sub-departments | Growth responsibility |
| --- | --- | --- |
| Marketing | studio-brand-voice, content-social, pr-awards, search-aeo | Content system, studio site and portfolio updates, case-study writing, awards, inbound first response |
| Advertising | paid-social, search-programmatic, ad-creative-measurement | Paid tests only when the gate in [advertising](advertising.md) is met |
| Outbound | prospecting-research, outreach-sequences, partnerships-referrals | Target accounts, research, outreach sequences, agency partnerships, referral asks |
| Sales | discovery-qualification, proposals-pitches, pricing-deal-desk, pipeline-forecasting | Qualification, discovery, pipeline, follow-up, win/loss, hand-off to L3 |
| Media (Delivery group) | film-motion-graphics, image-photo-direction, sound-voice | Produces visuals, motion and film for case studies and content |
| Design, Engineering (Craft group) | — | Review every public piece of work for craft accuracy; supply process material |

## Weekly growth rhythm

Feeds the Business engine's operating rhythm (business/operating-rhythm.md)
and scorecard (business/scorecard.md). Time boxes assume a founder doing
client work most of the week; protect craft blocks first.

| When | Time | What | Department |
| --- | --- | --- | --- |
| Monday plan | 15 minutes | Pick this week's outbound accounts (from the target list), content pieces to ship and follow-ups due | Sales, Outbound, Marketing |
| Daily | 15 minutes | Inbound and DM triage; reply to real enquiries within one working day | Marketing → Sales |
| Twice a week | 60 minutes | Outbound research and personalised messages for the week's accounts | Outbound |
| Weekly | One block | Produce and publish the week's content per the [calendar](content/production-workflow.md#content-calendar) | Marketing, Media |
| Friday review | 15 minutes, inside the weekly review | Update the vault pipeline; count leads, qualified conversations, proposals, wins and losses; note one learning | Sales |
| Monthly | 45 minutes, inside the business review | [Growth metrics](metrics.md), source attribution, win/loss themes, content performance, award calendar | Sales, Marketing |
| Quarterly | Inside the strategy review | ICP and channel evidence; which channels to keep, cut or test | Founder |

## Map of this folder

| Area | Documents |
| --- | --- |
| Sales | [sales system](sales/README.md): [lead sources](sales/lead-sources.md), [qualification](sales/qualification.md), [discovery call](sales/discovery-call.md), [pipeline and follow-up](sales/pipeline.md), [win/loss review](sales/win-loss.md) |
| Content | [content system](content/README.md), [production workflow](content/production-workflow.md), [inbound handling](content/inbound.md) |
| Outbound | [outbound system](outbound/README.md), [compliance basics](outbound/compliance.md) |
| Proof | [proof engine](proof/README.md), [case studies](proof/case-studies.md), [testimonials](proof/testimonials.md), [awards](proof/awards.md) |
| Other reach | [partnerships and referrals](partnerships-and-referrals.md), [advertising](advertising.md) |
| Measurement | [growth metrics](metrics.md) |

## Template bundles

| Bundle | Target | Stage |
| --- | --- | --- |
| [`discovery-notes`](../templates/bundles/discovery-notes/) | `{vault}/{codename}/private-notes/discovery-{date}.md` | L2 |
| [`outreach-sequence`](../templates/bundles/outreach-sequence/) | `{vault}/growth/outreach/{codename}.md` | L0 |
| [`win-loss`](../templates/bundles/win-loss/) | `{vault}/growth/win-loss/{codename}-{date}.md` | After L3 decision, or a loss at any stage |
| [`content-brief`](../templates/bundles/content-brief/) | `growth/content/briefs/{date}-{slug}.md` | Content workflow |
| [`case-study`](../templates/bundles/case-study/) | `projects/{codename}/case-study.md` (cleared projects only) | L9 |

Render them with the Delivery engine's `3w new <bundle>` command.

## Related

- [Client acquisition summary](../business/client-acquisition.md)
- [Portfolio strategy](../studio/portfolio-strategy.md)
- [Creative philosophy](../studio/creative-philosophy.md)
- [Taste references](../taste/README.md)
