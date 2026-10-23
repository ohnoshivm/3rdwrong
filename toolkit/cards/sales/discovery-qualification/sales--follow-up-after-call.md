---
title: Follow Up after Call
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: sales:follow-up-after-call
department: sales
sub_department: discovery-qualification
job: discovery-calls
role: specialist
trigger: "After a client or qualified prospect call when a draft follow-up is requested."
kind: plugin-skill
availability: codex
distribution: manual
source: /Users/hustle/.codex/plugins/cache/openai-curated-remote/sales/1.1.3/skills/follow-up-after-call/SKILL.md
invoke: "Claude Code skill: follow-up-after-call; Codex skill: follow-up-after-call."
pairs_with: [agency:sales-discovery-coach]
---
# Follow Up after Call

The studio specialist for `discovery-calls`: After a client or qualified prospect call when a draft follow-up is requested.

## What it does

- Follow Up After Call.
- Context-Gathering Intake.
- Common Skill Instructions.
- Key Dependency Categories.
- [Blocking] ~~Meeting Transcripts for the primary transcript, grounded notes, participant language, decisions, commitments, objections, and source links. It blocks the default live-source follow-up path; explicit grounded call evidence already in context satisfies the need.

## When to use

- After a client or qualified prospect call when a draft follow-up is requested.

## When not to use

- Outside `discovery-calls`; route to the matching job lead when another job owns the work.
- Do not use it to approve its own work or make an unapproved commercial commitment.

## Inputs it needs

- Approved scope, intended decision and the minimum relevant source material.
- The target, account, call, pricing context or pipeline data required by this job; redact or keep personal data in a private store.

## How to run it

1. Confirm the job, trigger and desired output; provide only approved, necessary inputs.
2. Invoke the tool with the prompt below and request evidence labels where claims or recommendations are made.
3. Review the draft against the source material; route decisions, external actions and approvals to the responsible human.

```text
Use sales:follow-up-after-call for discovery calls at 3RDWRONG. Scope: {{approved scope}}. Inputs: {{private source references or redacted facts}}. Return a concise, source-grounded draft for human review. Mark unsupported items Unknown; do not invent facts, approvals, outcomes or claims.
```

## What good output looks like

- Answers the stated `discovery-calls` question with a clearly scoped result.
- Distinguishes documented inputs from interpretation and unknowns; gives a practical next step.
- Contains no unsupported claim, invented result or unapproved commitment.

## Quality checks

- [ ] A separate reviewer checked the output against the supplied evidence.
- [ ] Scope and assumptions are visible; unknowns are stated rather than filled in.
- [ ] No sensitive client or prospect information entered the public repository.

## Pairs with

- agency:sales-discovery-coach

Use the lead for routing and hand off only the relevant, reviewed artefact; keep human approval with the founder.

## Limits and cautions

- The tool source is a prompt/instruction file; this card does not establish live connectivity, performance, or approval.
- Distribution is `manual`; verify installation or sign-in requirements before relying on runtime access.

- Keep client and prospect personal data out of this public repository; use an approved private store.
- Separate sourced facts from interpretation and label evidence Documented, Interpretation, Hypothesis or Unknown. A maker cannot be the sole checker; the founder retains approval.
