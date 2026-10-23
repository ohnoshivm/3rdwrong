---
title: Influencer Marketing
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:influencer-marketing
department: outbound
sub_department: partnerships-referrals
job: creator-partnerships
role: lead
trigger: ""
kind: skill
availability: codex
distribution: manual
source: /Users/hustle/.codex/skills/influencer-marketing/SKILL.md
invoke: "Claude Code skill: influencer-marketing; Codex skill: influencer-marketing."
pairs_with: [skill:brief-generator, skill:trend-spotter]
---
# Influencer Marketing

The studio lead for `creator-partnerships`: use this tool to handle creator partnerships work with a source-grounded draft for human review.

## What it does

- Influencer & Creator Marketing.
- The Influencer ↔ Ambassador Spectrum.
- 1. Finding & Vetting Partners.
- **Engagement rate**, not follower count (a rough floor: ~1–3% is healthy on IG/TikTok at scale; higher for nano). Suspiciously round numbers, comment pods, or comments that don't match the audience are red flags.
- **Telegram channels** show no likes-based engagement; the signal is the view counter under each post. Divide the median views of week-old posts by subscribers and compare with channels of the same size (median about 8% at 10K–20K subscribers, about 4% above 1M). For the full Telegram checklist (topic and language baselines, ad networks, channel age) and per-view pricing, see references/telegram-channels.md (upstream reference `references/telegram-channels.md`).

## When to use

- Start with this lead for the `creator-partnerships` job in outbound/partnerships-referrals.
- Use when the studio needs creator partnerships during a live opportunity or internal commercial decision.

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
Use skill:influencer-marketing for creator partnerships at 3RDWRONG. Scope: {{approved scope}}. Inputs: {{private source references or redacted facts}}. Return a concise, source-grounded draft for human review. Mark unsupported items Unknown; do not invent facts, approvals, outcomes or claims.
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
- skill:trend-spotter

Use the lead for routing and hand off only the relevant, reviewed artefact; keep human approval with the founder.

## Limits and cautions

- The tool source is a prompt/instruction file; this card does not establish live connectivity, performance, or approval.
- Distribution is `manual`; verify installation or sign-in requirements before relying on runtime access.

- Outbound is 20 personalised, hand-written first messages per week; do not automate or batch-send. Check consent, suppression and opt-out rules before any contact. Keep prospect names, contact details, notes and other personal data out of this public repository.
- Separate sourced facts from interpretation and label evidence Documented, Interpretation, Hypothesis or Unknown. A maker cannot be the sole checker; the founder retains approval.
