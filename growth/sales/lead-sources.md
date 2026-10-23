---
title: Lead sources
type: method
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# Lead sources

**Proposed.** Lifecycle stage **L0 Lead**: where potential clients come from
and how every contact is captured the same way.

## Purpose

Capture every potential client consistently so that no real enquiry is lost,
and so the studio can learn which sources produce qualified, winnable work —
not just volume.

## When it applies

Any contact that could become paid work: an inbound enquiry, a reply to
outreach, a referral, a partner introduction, a conversation at an event, a
comment or DM that asks about working together.

## Roles

| Role | Department | Responsibility |
| --- | --- | --- |
| Capture | Whoever receives the contact (Marketing for inbound, Outbound for replies) | Records the lead within one working day |
| Owner | Sales — discovery-qualification | Assigns a codename, sets the next action, moves it to L1 |
| **Founder** | Sign-off | Reviews new leads in the Friday review |

## Inputs

The enquiry or reply itself; the source; any referrer (recorded privately).

## Steps

1. **Recognise a lead.** A contact is a lead when someone with a plausible
   business need asks about working together, or replies positively to
   outreach. A compliment, a job application or a vendor pitch is not a lead.
2. **Reply first.** Acknowledge a real enquiry within one working day, thank
   them, and propose a short call or ask one or two clarifying questions. Do
   not send a price list or a capability deck as the first reply.
3. **Assign a codename.** Two lowercase words joined by a hyphen, neutral and
   unrelated to the business (the [Delivery engine](../../methods/lifecycle.md)'s codename rules apply).
   Record the real identity against it in the vault's `clients.yaml`.
4. **Record in the vault pipeline** (`growth/pipeline.yaml`, format in
   [pipeline](pipeline.md)): codename, date, source (from the table below),
   referrer if any, offer interest (identity, digital experience, both,
   unclear), one-line need in the contact's own words, next action and date.
5. **Route.** Move to [L1 qualification](qualification.md) within two working
   days, or record why not (for example, spam or out of scope).

### Source taxonomy

Use exactly one primary source per lead so attribution stays comparable.

| Source code | Meaning | Feeds from |
| --- | --- | --- |
| `referral-client` | Introduced by a past or current client | [Referrals](../partnerships-and-referrals.md) |
| `referral-network` | Introduced by a peer, collaborator or friend | [Referrals](../partnerships-and-referrals.md) |
| `partner-agency` | Brought by an agency partner | [Partnerships](../partnerships-and-referrals.md) |
| `outbound` | Reply to studio outreach | [Outbound](../outbound/README.md) |
| `inbound-site` | Studio site or journal | [Content](../content/README.md) |
| `inbound-social` | Instagram, LinkedIn, X, Behance or Dribbble | [Inbound handling](../content/inbound.md) |
| `inbound-award` | Found the studio through an award or platform profile | [Awards](../proof/awards.md) |
| `event-community` | Talk, event or community | [Partnerships and communities](../partnerships-and-referrals.md) |
| `paid` | A paid placement or ad | [Advertising](../advertising.md) |
| `other` | Anything else; describe it in a note | — |

**Hypothesis** — for a new founder-led studio, referrals and the founder's
network are likely to produce the first qualified work, with content and
awards compounding more slowly. Test this with the studio's own attribution
data in [growth metrics](../metrics.md); do not plan around it as fact.

## Outputs

One pipeline record per lead in the vault. No public artefact.

## Quality gate

- [ ] Real enquiries acknowledged within one working day.
- [ ] Codename assigned; real name only in the vault.
- [ ] Exactly one source code recorded; referrer recorded privately.
- [ ] Need recorded in the contact's own words, not the studio's diagnosis.
- [ ] Next action and date set.

## Metrics

Leads by source, first-response time, lead-to-qualified rate by source
([growth metrics](../metrics.md)).

## Failure modes

- Enquiries sitting in DMs or inboxes without a record — triage daily.
- Treating every compliment as a lead, which inflates the funnel.
- Sending prices before understanding the problem.
- Recording names or contact details in a public file, issue or commit.

## Related

- [Qualification](qualification.md)
- [Inbound handling](../content/inbound.md)
- [Outbound system](../outbound/README.md)
