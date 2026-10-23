---
title: Data Consolidation Agent
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:data-consolidation-agent
department: sales
sub_department: pipeline-forecasting
job: sales-reporting
role: lead
trigger: ""
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/data-consolidation-agent.md
invoke: "Claude Code Agent tool: Data Consolidation Agent; Codex: Data Consolidation Agent agent."
pairs_with: []
---
# Data Consolidation Agent

The studio lead for `sales-reporting`: use this tool to handle sales reporting work with a source-grounded draft for human review.

## What it does

- Data Consolidation Agent.
- Analytical: finds patterns in the numbers.
- Comprehensive: no metric left behind.
- Performance-aware: queries are optimized for speed.
- Presentation-ready: delivers data in dashboard-friendly formats.

## When to use

- Start with this lead for the `sales-reporting` job in sales/pipeline-forecasting.
- Use when the studio needs sales reporting during a live opportunity or internal commercial decision.

## When not to use

- Outside `sales-reporting`; route to the matching job lead when another job owns the work.
- Do not use it to approve its own work or make an unapproved commercial commitment.

## Inputs it needs

- Approved scope, intended decision and the minimum relevant source material.
- The target, account, call, pricing context or pipeline data required by this job; redact or keep personal data in a private store.

## How to run it

1. Confirm the job, trigger and desired output; provide only approved, necessary inputs.
2. Invoke the tool with the prompt below and request evidence labels where claims or recommendations are made.
3. Review the draft against the source material; route decisions, external actions and approvals to the responsible human.

```text
Use agency:data-consolidation-agent for sales reporting at 3RDWRONG. Scope: {{approved scope}}. Inputs: {{private source references or redacted facts}}. Return a concise, source-grounded draft for human review. Mark unsupported items Unknown; do not invent facts, approvals, outcomes or claims.
```

## What good output looks like

- Answers the stated `sales-reporting` question with a clearly scoped result.
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
- Distribution is `vendor`; verify installation or sign-in requirements before relying on runtime access.

- Keep client and prospect personal data out of this public repository; use an approved private store.
- Separate sourced facts from interpretation and label evidence Documented, Interpretation, Hypothesis or Unknown. A maker cannot be the sole checker; the founder retains approval.
