---
title: Shader Gen
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: chatcut-desktop:shader-gen
department: media
sub_department: film-motion-graphics
job: video-effects
role: lead
trigger: ""
kind: skill
availability: both
distribution: fetch
source: /Users/hustle/.claude/skills-library/master-of-20261021/media/chatcut-shader-gen/SKILL.md
invoke: "Claude Code/Codex skill `shader-gen`"
pairs_with: []
---
# Shader Gen

The studio's lead tool for video-effects: use it for the documented workflow in media production.

## What it does

- **Inline**: pass `targetItemId`; the effect covers the whole item and follows it when it moves or resizes.
- **Block effect**: pass `trackId` + `startFrame` + `durationFrames` for an absolute timeline range.
- assetId` is the LUT effect asset's real id. There is no literal `"lut"` assetId, and no LUT binding nested inside `propertyOverrides`.
- propertyOverrides` carries only `intensity` (0–1, default 1). The `.cube` binding lives on the asset, not on the effect item.

## When to use

- At the point in a studio engagement when `video-effects` is required.
- Use after Design direction and required inputs are agreed; keep the human accountable for creative decisions.

## When not to use

- When the task does not match its documented scope, use the job lead or ask the producer to route it.

## Inputs it needs

- Approved brief, intended audience and output format.
- Source assets and rights/consent status where relevant.
- Relevant production environment and constraints stated by the tool file.

## How to run it

1. Read the source file at `/Users/hustle/.claude/skills-library/master-of-20261021/media/chatcut-shader-gen/SKILL.md` and confirm its prerequisites.
2. Invoke Claude Code/Codex skill `shader-gen` in the supported host.
3. Supply only approved inputs; review the result against the brief.

```text
Use Claude Code/Codex skill `shader-gen` for the video-effects task. Brief: {{approved brief}}. Inputs: {{source assets and constraints}}. Return only work supported by the tool instructions, state unknowns, and flag anything that needs human review.
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

- Source: `/Users/hustle/.claude/skills-library/master-of-20261021/media/chatcut-shader-gen/SKILL.md`. Verify documented prerequisites and scope before relying on output.
- Fetch/manual distribution may require installation or sign-in.
- Follow studio rules: maker ≠ checker; motion only when concept-led; honour reduced motion/accessibility; no client data in public repo.
