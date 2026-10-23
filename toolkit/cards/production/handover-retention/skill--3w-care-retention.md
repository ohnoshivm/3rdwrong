---
title: Care and retention
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:3w-care-retention
department: production
sub_department: handover-retention
job: retention-programmes
role: lead
trigger: ""
kind: repo-skill
availability: repo
distribution: repo
source: skills/3w-care-retention/SKILL.md
invoke: "3w-care-retention skill"
pairs_with: [agency:customer-success-manager, skill:writing-release-notes, skill:3w-awards-submission]
---
# Care and retention

The studio's lead tool for retention programmes: warranty closure, care plans, care reviews, check-ins and once-only testimonial and referral asks. Registered job lead; the skill remains experimental.

## What it does

- Sets warranty, care-conversation and check-in dates at handover.
- Triages issues as warranty defect, change or care work.
- Drafts a care plan from the method's elements table (prices left to the Business engine).
- Runs care reviews from evidence and logs testimonial and referral asks once each.

## When to use

- L7 handover, warranty end (30 days, D-0023), each care-plan review, and a planned check-in after an engagement.

## When not to use

- Live project client service — `agency:customer-service`.
- Retainer health scoring — `agency:customer-success-manager`.
- Pricing, or contacting anyone who asked not to be contacted.

## Inputs it needs

- `handover.md`, decisions log, warranty terms, care plan.
- Care log and field measurements.
- Client contact preferences and earlier asks.

## How to run it

1. Collect the inputs; keep client and prospect details in the vault.
2. Run the skill and return its exact output structure.
3. Have someone other than the maker review the result.
4. File the output where the skill says; act on blockers first.

```text
Use the 3w-care-retention skill for {{codename}}, stage {{warranty end | care review | check-in}}. Inputs: {{handover.md, care log, measurements}}. Return the care and retention record with next dates; leave prices blank.
```

## What good output looks like

- Clear stage and next date.
- Recommendations each cite evidence.
- Ask log shows at most one testimonial and one referral ask.

## Quality checks

- [ ] Warranty not used as a change budget.
- [ ] Access justified or removed.
- [ ] No client identity or price in the public repo.

## Pairs with

- Upstream: `skill:writing-release-notes` (delivery handover).
- Neighbour: `agency:customer-success-manager` for retainers.
- Proof: testimonials feed case studies; `skill:3w-awards-submission` after close-out.

## Limits and cautions

- Experimental skill; cadence for check-ins is a Hypothesis.
- Founder approves care scope; client approves care work and testimonial text.
