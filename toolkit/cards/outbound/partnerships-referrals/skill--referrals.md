---
title: Referrals
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:referrals
department: outbound
sub_department: partnerships-referrals
job: referral-programmes
role: lead
trigger: ""
kind: skill
availability: codex
distribution: manual
source: /Users/hustle/.codex/skills/referrals/SKILL.md
invoke: "Claude Code skill: referrals; Codex skill: referrals."
pairs_with: []
---
# Referrals

The studio lead for `referral-programmes`: use this tool to handle referral programmes work with a source-grounded draft for human review.

## What it does

- Referral & Affiliate Programs.
- 1. Program Type.
- Customer referral program, affiliate program, or both?.
- What's the average customer LTV?.
- What's your current CAC from other channels?.

## When to use

- Start with this lead for the `referral-programmes` job in outbound/partnerships-referrals.
- Use when the studio needs referral programmes during a live opportunity or internal commercial decision.

## When not to use

- Outside `referral-programmes`; route to the matching job lead when another job owns the work.
- Do not use it to send or automate outreach; studio outbound is limited to 20 personalised, hand-written first messages per week.
- Do not use it to approve its own work or make an unapproved commercial commitment.

## Inputs it needs

- Approved scope, intended decision and the minimum relevant source material.
- The target, account, call, pricing context or pipeline data required by this job; redact or keep personal data in a private store.

## How to run it

1. Confirm the job, trigger and desired output; provide only approved, necessary inputs.
2. Invoke the tool with the prompt below and request evidence labels where claims or recommendations are made.
3. Review the draft against the source material; route decisions, external actions and approvals to the responsible human.

```text
Use skill:referrals for referral programmes at 3RDWRONG. Scope: {{approved scope}}. Inputs: {{private source references or redacted facts}}. Return a concise, source-grounded draft for human review. Mark unsupported items Unknown; do not invent facts, approvals, outcomes or claims.
```

## What good output looks like

- Answers the stated `referral-programmes` question with a clearly scoped result.
- Distinguishes documented inputs from interpretation and unknowns; gives a practical next step.
- Contains no unsupported claim, invented result or unapproved commitment.

## Quality checks

- [ ] A separate reviewer checked the output against the supplied evidence.
- [ ] Scope and assumptions are visible; unknowns are stated rather than filled in.
- [ ] No sensitive client or prospect information entered the public repository.

## Pairs with

- No same-job peer is listed in the eligible registry scope.

Use the lead for routing and hand off only the relevant, reviewed artefact; keep human approval with the founder.

## Limits and cautions

- The tool source is a prompt/instruction file; this card does not establish live connectivity, performance, or approval.
- Distribution is `manual`; verify installation or sign-in requirements before relying on runtime access.

- Outbound is 20 personalised, hand-written first messages per week; do not automate or batch-send. Check consent, suppression and opt-out rules before any contact. Keep prospect names, contact details, notes and other personal data out of this public repository.
- Separate sourced facts from interpretation and label evidence Documented, Interpretation, Hypothesis or Unknown. A maker cannot be the sole checker; the founder retains approval.
