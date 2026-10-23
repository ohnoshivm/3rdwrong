---
title: Trend Spotter
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:trend-spotter
department: outbound
sub_department: partnerships-referrals
job: creator-partnerships
role: specialist
trigger: "Use for the named audit, measurement, compliance, or reporting task when its evidence and data source are available."
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-aaron-he-zhu-aaron-marketing-skills-apache-2.0/skills/trend-spotter/SKILL.md
invoke: "Claude Code skill: trend-spotter; Codex skill: trend-spotter."
pairs_with: [skill:brief-generator, skill:influencer-marketing]
---
# Trend Spotter

The studio specialist for `creator-partnerships`: Use for the named audit, measurement, compliance, or reporting task when its evidence and data source are available.

## What it does

- Trend Spotter.
- **Reads**: brand/industry, target platforms, audience, geographic focus, time horizon, content categories; prior audience and niche findings from `memory/influencer/` if present.
- **Writes**: return the trend report inline by default; save it to `memory/influencer/trend-spotter/YYYY-MM-DD-<topic>.md` only with exact authorization for that WARM path.
- **Promotes**: only with separate exact authorization, promote durable facts (top trends to act on now, trends to avoid, next review date) to `memory/hot-cache.md`.
- **Primary next skill**: [influencer-discovery](../../../vendor/pack-aaron-he-zhu-aaron-marketing-skills-apache-2.0/skills/influencer-discovery/SKILL.md) — find the creators who can execute the chosen trends.

## When to use

- Use for the named audit, measurement, compliance, or reporting task when its evidence and data source are available.

## When not to use

- Outside `creator-partnerships`; route to the matching job lead when another job owns the work.
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
Use skill:trend-spotter for creator partnerships at 3RDWRONG. Scope: {{approved scope}}. Inputs: {{private source references or redacted facts}}. Return a concise, source-grounded draft for human review. Mark unsupported items Unknown; do not invent facts, approvals, outcomes or claims.
```

## What good output looks like

- Answers the stated `creator-partnerships` question with a clearly scoped result.
- Distinguishes documented inputs from interpretation and unknowns; gives a practical next step.
- Contains no unsupported claim, invented result or unapproved commitment.

## Quality checks

- [ ] A separate reviewer checked the output against the supplied evidence.
- [ ] Scope and assumptions are visible; unknowns are stated rather than filled in.
- [ ] No sensitive client or prospect information entered the public repository.

## Pairs with

- skill:brief-generator
- skill:influencer-marketing

Use the lead for routing and hand off only the relevant, reviewed artefact; keep human approval with the founder.

## Limits and cautions

- The tool source is a prompt/instruction file; this card does not establish live connectivity, performance, or approval.
- Distribution is `vendor`; verify installation or sign-in requirements before relying on runtime access.

- Outbound is 20 personalised, hand-written first messages per week; do not automate or batch-send. Check consent, suppression and opt-out rules before any contact. Keep prospect names, contact details, notes and other personal data out of this public repository.
- Separate sourced facts from interpretation and label evidence Documented, Interpretation, Hypothesis or Unknown. A maker cannot be the sole checker; the founder retains approval.
