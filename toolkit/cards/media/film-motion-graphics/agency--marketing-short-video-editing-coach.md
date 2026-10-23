---
title: Marketing Short Video Editing Coach
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:marketing-short-video-editing-coach
department: media
sub_department: film-motion-graphics
job: short-form-editing
role: lead
trigger: ""
kind: upstream-agent
availability: claude
distribution: vendor
source: .claude/agents/marketing-short-video-editing-coach.md
invoke: "Claude Code Agent tool: `marketing-short-video-editing-coach`"
pairs_with: []
---
# Marketing Short Video Editing Coach

The studio's lead tool for short-form-editing: use it for the documented workflow in media production.

## What it does

- **Role**: Short-video editing technical coach and full post-production workflow specialist
- **Personality**: Technical perfectionist, aesthetically sharp, zero tolerance for visual flaws, patient but strict with sloppy deliverables
- **CapCut Pro (primary recommendation)**
- Use cases: Daily short-video output, lightweight commercial projects, team batch production

## When to use

- At the point in a studio engagement when `short-form-editing` is required.
- Use after Design direction and required inputs are agreed; keep the human accountable for creative decisions.

## When not to use

- When the task does not match its documented scope, use the job lead or ask the producer to route it.

## Inputs it needs

- Approved brief, intended audience and output format.
- Source assets and rights/consent status where relevant.
- Relevant production environment and constraints stated by the tool file.

## How to run it

1. Read the source file at `.claude/agents/marketing-short-video-editing-coach.md` and confirm its prerequisites.
2. Invoke Claude Code Agent tool: `marketing-short-video-editing-coach` in the supported host.
3. Supply only approved inputs; review the result against the brief.

```text
Use Claude Code Agent tool: `marketing-short-video-editing-coach` for the short-form-editing task. Brief: {{approved brief}}. Inputs: {{source assets and constraints}}. Return only work supported by the tool instructions, state unknowns, and flag anything that needs human review.
```

## What good output looks like

- Output addresses the supplied brief and requested format.
- Unsupported claims, missing inputs and unresolved rights are identified.

## Quality checks

- [ ] Reviewer other than the maker checks the result against the brief.
- [ ] Claims and provenance are traceable; unknowns are explicit.
- [ ] Accessibility, rights and delivery requirements are checked where applicable.

## Pairs with

- No same-job pair recorded in the registry; use the department lead for hand-off.

## Limits and cautions

- Source: `.claude/agents/marketing-short-video-editing-coach.md`. Verify documented prerequisites and scope before relying on output.
- Distribution and runtime availability are not guaranteed by this card.
- Follow studio rules: maker ≠ checker; motion only when concept-led; honour reduced motion/accessibility; no client data in public repo.
