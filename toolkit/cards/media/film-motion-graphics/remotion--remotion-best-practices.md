---
title: Remotion Best Practices
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: remotion:remotion-best-practices
department: media
sub_department: film-motion-graphics
job: programmatic-video
role: lead
trigger: ""
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/plugin-openai-curated-remote-remotion-4.0.534/skills/remotion-best-practices
invoke: "Claude Code/Codex skill `remotion-best-practices`"
pairs_with: []
---
# Remotion Best Practices

The studio's lead tool for programmatic-video: use it for the documented workflow in media production.

## What it does

- Users may make edits in the code outside of the conversation.
- If you detect a surprising change made in the meanwhile, don't overwrite it, assume it was intentional or ask for confirmation.
- If the user asks to make, create, or build a new video or composition, load [Create a new Remotion video](../../../vendor/pack-remotion-dev-remotion-mit/skills/remotion-best-practices/remotion-create/REFERENCE.md), whether or not a Remotion project already exists.

## When to use

- At the point in a studio engagement when `programmatic-video` is required.
- Use after Design direction and required inputs are agreed; keep the human accountable for creative decisions.

## When not to use

- When the task does not match its documented scope, use the job lead or ask the producer to route it.

## Inputs it needs

- Approved brief, intended audience and output format.
- Source assets and rights/consent status where relevant.
- Relevant production environment and constraints stated by the tool file.

## How to run it

1. Read the source file at `toolkit/vendor/plugin-openai-curated-remote-remotion-4.0.534/skills/remotion-best-practices` and confirm its prerequisites.
2. Invoke Claude Code/Codex skill `remotion-best-practices` in the supported host.
3. Supply only approved inputs; review the result against the brief.

```text
Use Claude Code/Codex skill `remotion-best-practices` for the programmatic-video task. Brief: {{approved brief}}. Inputs: {{source assets and constraints}}. Return only work supported by the tool instructions, state unknowns, and flag anything that needs human review.
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

- Source: `toolkit/vendor/plugin-openai-curated-remote-remotion-4.0.534/skills/remotion-best-practices`. Verify documented prerequisites and scope before relying on output.
- Distribution and runtime availability are not guaranteed by this card.
- Follow studio rules: maker ≠ checker; motion only when concept-led; honour reduced motion/accessibility; no client data in public repo.
