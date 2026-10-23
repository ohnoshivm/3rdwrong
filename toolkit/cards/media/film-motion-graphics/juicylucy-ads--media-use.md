---
title: Media Use
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: juicylucy-ads:media-use
department: media
sub_department: film-motion-graphics
job: asset-research
role: lead
trigger: ""
kind: plugin-skill
availability: both
distribution: manual
source: /Users/hustle/.codex/plugins/cache/openai-curated-remote/juicylucy-ads/0.27.0/skills/media-use/SKILL.md
invoke: "Claude Code/Codex skill `media-use`"
pairs_with: []
---
# Media Use

The studio's lead tool for asset-research: use it for the documented workflow in media production.

## What it does

- The media OS for HyperFrames: resolve · generate · operate · remember — every media type, one skill, zero context noise.
- First run: install and sign in to the `heygen` CLI (the free-usage path), then verify with `~/.juicylucy/bin/hyperframes media-use resolve --doctor`. Setup and providers: `references/setup-providers.md`.
- ~/.juicylucy/bin/hyperframes media-use resolve --type <type> --intent "<description>" --project <dir>

## When to use

- At the point in a studio engagement when `asset-research` is required.
- Use after Design direction and required inputs are agreed; keep the human accountable for creative decisions.

## When not to use

- When the task does not match its documented scope, use the job lead or ask the producer to route it.

## Inputs it needs

- Approved brief, intended audience and output format.
- Source assets and rights/consent status where relevant.
- Relevant production environment and constraints stated by the tool file.

## How to run it

1. Read the source file at `/Users/hustle/.codex/plugins/cache/openai-curated-remote/juicylucy-ads/0.27.0/skills/media-use/SKILL.md` and confirm its prerequisites.
2. Invoke Claude Code/Codex skill `media-use` in the supported host.
3. Supply only approved inputs; review the result against the brief.

```text
Use Claude Code/Codex skill `media-use` for the asset-research task. Brief: {{approved brief}}. Inputs: {{source assets and constraints}}. Return only work supported by the tool instructions, state unknowns, and flag anything that needs human review.
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

- Source: `/Users/hustle/.codex/plugins/cache/openai-curated-remote/juicylucy-ads/0.27.0/skills/media-use/SKILL.md`. Verify documented prerequisites and scope before relying on output.
- Distribution and runtime availability are not guaranteed by this card.
- Follow studio rules: maker ≠ checker; motion only when concept-led; honour reduced motion/accessibility; no client data in public repo.
