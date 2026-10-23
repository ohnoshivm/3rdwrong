---
title: Build Vesperfall Review Assets
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:build-vesperfall-review-assets
department: labs
sub_department: house-engine
job: asset-pipelines
role: lead
trigger: ""
kind: skill
availability: both
distribution: manual
source: /Users/hustle/.claude/skills-library/master-of-20261021/games/build-vesperfall-review-assets/SKILL.md
invoke: "Claude Code/Codex skill `build-vesperfall-review-assets`"
pairs_with: []
---
# Build Vesperfall Review Assets

The studio's lead tool for asset-pipelines: use it for the documented workflow in media production.

## What it does

- Locate shipped PNG, FBX, GLB, textures, runtime factories, and declared-but-missing paths.
- Prefer a shipped FBX/GLB when it is the actual runtime source.
- Use `$img2threejs` only when reconstructing from an image in code. Never relabel imported geometry as img2threejs.
- Do not claim a GLB or texture exists because code declares a future URL.

## When to use

- At the point in a studio engagement when `asset-pipelines` is required.
- Use after Design direction and required inputs are agreed; keep the human accountable for creative decisions.

## When not to use

- When the task does not match its documented scope, use the job lead or ask the producer to route it.

## Inputs it needs

- Approved brief, intended audience and output format.
- Source assets and rights/consent status where relevant.
- Relevant production environment and constraints stated by the tool file.

## How to run it

1. Read the source file at `/Users/hustle/.claude/skills-library/master-of-20261021/games/build-vesperfall-review-assets/SKILL.md` and confirm its prerequisites.
2. Invoke Claude Code/Codex skill `build-vesperfall-review-assets` in the supported host.
3. Supply only approved inputs; review the result against the brief.

```text
Use Claude Code/Codex skill `build-vesperfall-review-assets` for the asset-pipelines task. Brief: {{approved brief}}. Inputs: {{source assets and constraints}}. Return only work supported by the tool instructions, state unknowns, and flag anything that needs human review.
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

- Source: `/Users/hustle/.claude/skills-library/master-of-20261021/games/build-vesperfall-review-assets/SKILL.md`. Verify documented prerequisites and scope before relying on output.
- Distribution and runtime availability are not guaranteed by this card.
- Follow studio rules: maker ≠ checker; motion only when concept-led; honour reduced motion/accessibility; no client data in public repo.
