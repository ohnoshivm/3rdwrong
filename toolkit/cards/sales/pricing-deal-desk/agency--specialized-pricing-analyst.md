---
title: Specialized Pricing Analyst
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:specialized-pricing-analyst
department: sales
sub_department: pricing-deal-desk
job: pricing-models
role: lead
trigger: ""
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/specialized-pricing-analyst.md
invoke: "Claude Code Agent tool: Specialized Pricing Analyst; Codex: Specialized Pricing Analyst agent."
pairs_with: [skill:pricing, skill:pricing-packaging-planner]
---
# Specialized Pricing Analyst

The studio lead for `pricing-models`: use this tool to handle pricing models work with a source-grounded draft for human review.

## What it does

- Pricing Analyst Agent.
- **Price optimization**: Develop pricing strategies that maximize revenue per unit while maintaining competitive position.
- **Margin protection**: Identify and eliminate margin leakage from unnecessary discounts, poor packaging, or cost creep.
- **Market intelligence**: Build and maintain competitive pricing intelligence for informed positioning.
- **Packaging strategy**: Design product tiers and bundles that capture willingness-to-pay across segments.

## When to use

- Start with this lead for the `pricing-models` job in sales/pricing-deal-desk.
- Use when the studio needs pricing models during a live opportunity or internal commercial decision.

## When not to use

- Outside `pricing-models`; route to the matching job lead when another job owns the work.
- Do not use it to approve its own work or make an unapproved commercial commitment.

## Inputs it needs

- Approved scope, intended decision and the minimum relevant source material.
- The target, account, call, pricing context or pipeline data required by this job; redact or keep personal data in a private store.

## How to run it

1. Confirm the job, trigger and desired output; provide only approved, necessary inputs.
2. Invoke the tool with the prompt below and request evidence labels where claims or recommendations are made.
3. Review the draft against the source material; route decisions, external actions and approvals to the responsible human.

```text
Use agency:specialized-pricing-analyst for pricing models at 3RDWRONG. Scope: {{approved scope}}. Inputs: {{private source references or redacted facts}}. Return a concise, source-grounded draft for human review. Mark unsupported items Unknown; do not invent facts, approvals, outcomes or claims.
```

## What good output looks like

- Answers the stated `pricing-models` question with a clearly scoped result.
- Distinguishes documented inputs from interpretation and unknowns; gives a practical next step.
- Contains no unsupported claim, invented result or unapproved commitment.

## Quality checks

- [ ] A separate reviewer checked the output against the supplied evidence.
- [ ] Scope and assumptions are visible; unknowns are stated rather than filled in.
- [ ] No sensitive client or prospect information entered the public repository.

## Pairs with

- skill:pricing
- skill:pricing-packaging-planner

Use the lead for routing and hand off only the relevant, reviewed artefact; keep human approval with the founder.

## Limits and cautions

- The tool source is a prompt/instruction file; this card does not establish live connectivity, performance, or approval.
- Distribution is `vendor`; verify installation or sign-in requirements before relying on runtime access.

- Keep client and prospect personal data out of this public repository; use an approved private store.
- Separate sourced facts from interpretation and label evidence Documented, Interpretation, Hypothesis or Unknown. A maker cannot be the sole checker; the founder retains approval.
