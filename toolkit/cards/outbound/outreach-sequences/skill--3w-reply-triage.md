---
title: Reply triage
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:3w-reply-triage
department: outbound
sub_department: outreach-sequences
job: reply-triage
role: lead
trigger: ""
kind: repo-skill
availability: repo
distribution: repo
source: skills/3w-reply-triage/SKILL.md
invoke: "3w-reply-triage skill"
pairs_with: [skill:3w-prospect-qualification, agency:sales-outreach, skill:engagement-inbox-manager]
---
# Reply triage

The studio's lead tool for reply triage: every outbound reply classified, answered within a working day, opt-outs honoured the same day. Proposed lead; the registry change is pending.

## What it does

- Stops the sequence at the first reply.
- Classifies into one of six classes from the outbound reply table.
- Drafts a short reply for a human to send and creates L0 leads for positive replies.
- Updates the suppression list and monthly counts; watches stop signals.

## When to use

- Whenever a reply to studio outbound arrives, and at the start of each working day.

## When not to use

- Inbound enquiries.
- Social comments and DMs — `skill:engagement-inbox-manager`.
- Auto-sending.

## Inputs it needs

- Reply, original message and sequence state.
- Suppression list.
- Qualification record.

## How to run it

1. Collect the inputs; keep client and prospect details in the vault.
2. Run the skill and return its exact output structure.
3. Have someone other than the maker review the result.
4. File the output where the skill says; act on blockers first.

```text
Use the 3w-reply-triage skill on today's outbound replies: {{vault link}}. Stop each sequence, classify, draft replies for me to send, and return the triage table with suppression updates.
```

## What good output looks like

- Each reply has one class, an action and a dated next step.
- Opt-outs added the same day.

## Quality checks

- [ ] Response within one working day.
- [ ] Positive replies became L0 leads with source `outbound`.
- [ ] No names or contacts in the public repo.

## Pairs with

- Upstream: `skill:3w-prospect-qualification`, `agency:sales-outreach`.
- Downstream: the pipeline (L0 lead) and the founder for stop signals.

## Limits and cautions

- Experimental skill; a person sends every reply.
- Legal complaints and deletion requests escalate to the founder after the request is honoured.
