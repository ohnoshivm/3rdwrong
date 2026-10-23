---
title: Imagegen
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:imagegen
department: media
sub_department: image-photo-direction
job: brand-image-assets
role: lead
trigger: ""
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/standalone-imagegen-4a41c3fc/skills/imagegen
invoke: "Claude Code/Codex skill `imagegen`"
pairs_with: []
---
# Imagegen

The studio's lead tool for brand-image-assets: use it for the documented workflow in media production.

## What it does

- **Default built-in tool mode (preferred):** built-in `image_gen` tool for image generation, editing, and transparent-image requests. Does not require `OPENAI_API_KEY`.
- **Fallback CLI mode:** `scripts/image_gen.py` CLI. Use when the user explicitly asks for or confirms the CLI/API/model path. Requires `OPENAI_API_KEY`.
- Use the built-in `image_gen` tool by default for normal image generation and editing requests.
- Do not switch to CLI fallback for ordinary quality, size, or file-path control.

## When to use

- At the point in a studio engagement when `brand-image-assets` is required.
- Use after Design direction and required inputs are agreed; keep the human accountable for creative decisions.

## When not to use

- When the task does not match its documented scope, use the job lead or ask the producer to route it.

## Inputs it needs

- Approved brief, intended audience and output format.
- Source assets and rights/consent status where relevant.
- Relevant production environment and constraints stated by the tool file.

## How to run it

1. Read the source file at `toolkit/vendor/standalone-imagegen-4a41c3fc/skills/imagegen` and confirm its prerequisites.
2. Invoke Claude Code/Codex skill `imagegen` in the supported host.
3. Supply only approved inputs; review the result against the brief.

```text
Use Claude Code/Codex skill `imagegen` for the brand-image-assets task. Brief: {{approved brief}}. Inputs: {{source assets and constraints}}. Return only work supported by the tool instructions, state unknowns, and flag anything that needs human review.
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

- Source: `toolkit/vendor/standalone-imagegen-4a41c3fc/skills/imagegen`. Verify documented prerequisites and scope before relying on output.
- Distribution and runtime availability are not guaranteed by this card.
- Follow studio rules: maker ≠ checker; motion only when concept-led; honour reduced motion/accessibility; no client data in public repo.
- The studio discloses AI use in its process; AI-generated material in final deliverables requires the client's written consent (D-0023).
- Check rights, likeness and source permissions before use.
- Do not send client data in prompts to third-party services without permission.
