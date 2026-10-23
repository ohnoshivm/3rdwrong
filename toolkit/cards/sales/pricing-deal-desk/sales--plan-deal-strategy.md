---
title: Plan Deal Strategy
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: sales:plan-deal-strategy
department: sales
sub_department: pricing-deal-desk
job: deal-strategy
role: specialist
trigger: "For an active studio opportunity with a defined buyer, scope, and decision process."
kind: plugin-skill
availability: codex
distribution: manual
source: /Users/hustle/.codex/plugins/cache/openai-curated-remote/sales/1.1.3/skills/plan-deal-strategy/SKILL.md
invoke: "Claude Code skill: plan-deal-strategy; Codex skill: plan-deal-strategy."
pairs_with: [agency:sales-deal-strategist]
---
# Plan Deal Strategy

The studio specialist for `deal-strategy`: For an active studio opportunity with a defined buyer, scope, and decision process.

## What it does

- Plan Deal Strategy.
- Context-Gathering Intake.
- Common Skill Instructions.
- Key Dependency Categories.
- [Blocking] ~~CRM for authoritative account and opportunity identity, stage, amount, close date, owner, contacts, and recent activity. It blocks the default active-deal strategy path unless sufficiently grounded deal truth is already in context.

## When to use

- For an active studio opportunity with a defined buyer, scope, and decision process.

## When not to use

- Outside `deal-strategy`; route to the matching job lead when another job owns the work.
- Do not use it to approve its own work or make an unapproved commercial commitment.

## Inputs it needs

- Approved scope, intended decision and the minimum relevant source material.
- The target, account, call, pricing context or pipeline data required by this job; redact or keep personal data in a private store.

## How to run it

1. Confirm the job, trigger and desired output; provide only approved, necessary inputs.
2. Invoke the tool with the prompt below and request evidence labels where claims or recommendations are made.
3. Review the draft against the source material; route decisions, external actions and approvals to the responsible human.

```text
Use sales:plan-deal-strategy for deal strategy at 3RDWRONG. Scope: {{approved scope}}. Inputs: {{private source references or redacted facts}}. Return a concise, source-grounded draft for human review. Mark unsupported items Unknown; do not invent facts, approvals, outcomes or claims.
```

## What good output looks like

- Answers the stated `deal-strategy` question with a clearly scoped result.
- Distinguishes documented inputs from interpretation and unknowns; gives a practical next step.
- Contains no unsupported claim, invented result or unapproved commitment.

## Quality checks

- [ ] A separate reviewer checked the output against the supplied evidence.
- [ ] Scope and assumptions are visible; unknowns are stated rather than filled in.
- [ ] No sensitive client or prospect information entered the public repository.

## Pairs with

- agency:sales-deal-strategist

Use the lead for routing and hand off only the relevant, reviewed artefact; keep human approval with the founder.

## Limits and cautions

- The tool source is a prompt/instruction file; this card does not establish live connectivity, performance, or approval.
- Distribution is `manual`; verify installation or sign-in requirements before relying on runtime access.

- Keep client and prospect personal data out of this public repository; use an approved private store.
- Separate sourced facts from interpretation and label evidence Documented, Interpretation, Hypothesis or Unknown. A maker cannot be the sole checker; the founder retains approval.
