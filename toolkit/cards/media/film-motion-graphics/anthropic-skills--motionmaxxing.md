---
title: Motionmaxxing
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: anthropic-skills:motionmaxxing
department: media
sub_department: film-motion-graphics
job: brand-film
role: lead
trigger: ""
kind: plugin-skill
availability: both
distribution: manual
source: /Users/hustle/.claude/skills/synced/88e7af4e-a2cf-4b40-8488-91a856697e04_aa2d1473-adba-46ff-9558-93fbf2ea6240/motionmaxxing/SKILL.md
invoke: "Claude Code/Codex skill `motionmaxxing`"
pairs_with: []
---
# Motionmaxxing

The studio's lead tool for brand-film: use it for the documented workflow in media production.

## What it does

- **Format:** 1920x1080, 30 fps, with sound. Length follows the idea: most launch films run 15-30 s; a single moment 3-7 s.
- **Ground:** from the brand and built as a world (capture plate, material, light). Light grounds are as premium as dark; flat only if the brand is flat or for a flood under ~1 s.

## When to use

- At the point in a studio engagement when `brand-film` is required.
- Use after Design direction and required inputs are agreed; keep the human accountable for creative decisions.

## When not to use

- When the task does not match its documented scope, use the job lead or ask the producer to route it.

## Inputs it needs

- Approved brief, intended audience and output format.
- Source assets and rights/consent status where relevant.
- Relevant production environment and constraints stated by the tool file.

## How to run it

1. Read the source file at `/Users/hustle/.claude/skills/synced/88e7af4e-a2cf-4b40-8488-91a856697e04_aa2d1473-adba-46ff-9558-93fbf2ea6240/motionmaxxing/SKILL.md` and confirm its prerequisites.
2. Invoke Claude Code/Codex skill `motionmaxxing` in the supported host.
3. Supply only approved inputs; review the result against the brief.

```text
Use Claude Code/Codex skill `motionmaxxing` for the brand-film task. Brief: {{approved brief}}. Inputs: {{source assets and constraints}}. Return only work supported by the tool instructions, state unknowns, and flag anything that needs human review.
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

- Source: `/Users/hustle/.claude/skills/synced/88e7af4e-a2cf-4b40-8488-91a856697e04_aa2d1473-adba-46ff-9558-93fbf2ea6240/motionmaxxing/SKILL.md`. Verify documented prerequisites and scope before relying on output.
- Distribution and runtime availability are not guaranteed by this card.
- Follow studio rules: maker ≠ checker; motion only when concept-led; honour reduced motion/accessibility; no client data in public repo.
