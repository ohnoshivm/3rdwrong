---
title: Outbound department
type: guide
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# Outbound department

Find suitable prospects and open conversations through research, sequences and partnerships.

Status: proposed registry routing. Source review does not establish live tool performance, licence clearance, runtime connectivity or founder approval.

20 tools; 7 lead, 6 specialist, 7 bench, 0 parked, 0 excluded; 13 active / 7 library.

## Sub-departments → jobs → leads

### prospecting-research

| Job | Lead(s) |
| --- | --- |
| `prospect-discovery` | `skill:prospecting` |
| `account-research` | `sales:sales-company-research` |
| `prospect-qualification` | **gap** — No reviewed tool justifies default ownership of this complete job; existing narrow references/specialists do not establish a lead method. |

### outreach-sequences

| Job | Lead(s) |
| --- | --- |
| `sequence-design` | `agency:sales-outbound-strategist` |
| `outreach-copy` | `agency:sales-outreach` |
| `reply-triage` | **gap** — No reviewed tool justifies default ownership of this complete job; existing narrow references/specialists do not establish a lead method. |

### partnerships-referrals

| Job | Lead(s) |
| --- | --- |
| `creator-partnerships` | `skill:influencer-marketing` |
| `referral-programmes` | `skill:referrals` |
| `partner-outreach` | `skill:outreach-manager` |

## Specialists with activation triggers

| Tool | Job | Trigger |
| --- | --- | --- |
| `agency:sales-offer-lead-gen-strategist` | `prospecting-research/prospect-discovery` | Use for outbound/prospecting-research/prospect-discovery when the brief specifically requires: Top-of-funnel architect who designs irresistible offers and lead magnets that attract qualified buyers at scale . |
| `sales:enrich-company-and-contact-data` | `prospecting-research/account-research` | When the studio explicitly needs prospect/contact discovery and enrichment. |
| `skill:brief-generator` | `partnerships-referrals/creator-partnerships` | Use only when the named content, channel, lifecycle, or campaign task is explicitly in the approved marketing scope. |
| `skill:cold-email` | `outreach-sequences/sequence-design` | Use for outbound/outreach-sequences/sequence-design when the brief specifically requires: Write and run B2B cold outbound that gets replies, from cold emails and follow-ups to sending setup, LinkedIn, multichannel cadences, and reply handling . |
| `skill:cold-outbound-sequencer` | `outreach-sequences/sequence-design` | Use for outbound/outreach-sequences/sequence-design when the brief specifically requires: Use when the user asks to "build a B2B cold-outbound sequence", "design reply-triage branching", "plan a domain warmup / sending throttle", or "make my outbound CAN-SPAM / opt-in compliant"; produces a multi-step outbound sequence with reply-triage branches (positive / objection / referral / not-now / opt-out), a warmup + send-throttle ramp schedule, jurisdiction opt-in/CAN-SPAM guardrails (guidance, not legal advice), and a SEND S-dimension read . |
| `skill:trend-spotter` | `partnerships-referrals/creator-partnerships` | Use for the named audit, measurement, compliance, or reporting task when its evidence and data source are available. |

## Bench and parked summary

- **bench: 7.** `skill:advocacy-program-designer`, `skill:audience-mapper`, `skill:competitor-tracker`, `skill:creator-content-auditor`, `skill:fit-scorer`, `skill:influencer-discovery`, `skill:social-selling-planner`
- **parked: 0.** None.
- **excluded: 0.** None.

Individual reasons and activation requirements are in the [canonical registry](../../toolkit/sources/registry.json). Library means callable by explicit name after review; it is not loaded by default.

## Gaps

- `prospecting-research/prospect-qualification` — No reviewed tool justifies default ownership of this complete job; existing narrow references/specialists do not establish a lead method.
- `outreach-sequences/reply-triage` — No reviewed tool justifies default ownership of this complete job; existing narrow references/specialists do not establish a lead method.

## Counts by sub-department and role

| Sub-department | Lead | Specialist | Bench | Parked | Excluded | Active | Library | Total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| prospecting-research | 2 | 2 | 1 | 0 | 0 | 4 | 1 | 5 |
| outreach-sequences | 2 | 2 | 0 | 0 | 0 | 4 | 0 | 4 |
| partnerships-referrals | 3 | 2 | 6 | 0 | 0 | 5 | 6 | 11 |

## Operating contract

Use the job lead first and a specialist only on its trigger. Maker and checker must be separate people/agent instances; a reviewer never approves its own department alone. Proposed `load: active` is the desired loading policy, while the source inventory records installation presence. No physical activation was performed.

Design and Engineering prototype together early; the handoff names artefacts, constraints, budgets and evidence rather than creating a wall. Human judgement and founder approval remain separate from tool routing.
