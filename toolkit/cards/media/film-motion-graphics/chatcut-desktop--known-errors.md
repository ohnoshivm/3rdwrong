---
title: Known Errors
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: chatcut-desktop:known-errors
department: media
sub_department: film-motion-graphics
job: video-editing
role: specialist
trigger: "Use for the named production workflow when its format or host matches the brief."
kind: plugin-skill
availability: both
distribution: fetch
source: /Users/hustle/.codex/plugins/cache/openai-curated-remote/chatcut-desktop/1.10.14/skills/known-errors/SKILL.md
invoke: "Claude Code/Codex skill `known-errors`"
pairs_with: [chatcut-desktop:chatcut-plugin-basics]
---
# Known Errors

The studio's specialist for video-editing; activate when Use for the named production workflow when its format or host matches the brief

## What it does

- On locked-track or stale-id failures, refresh the affected timeline scope and retry only with current ids and state.
- On validation errors, change only the rejected field or transaction shape; preserve unrelated project state.
- Hosted plugin surfaces use the `asset-import` adapter and `import_media`; do not substitute backend-only `push_asset` or `download_media` calls when they are absent.
- If media conversion fails, use the helper's structured retry when provided. Otherwise explain the unsupported source and ask for a compatible replacement; do not repeat the same failing editor import path.

## When to use

- Use for the named production workflow when its format or host matches the brief.

## When not to use

- When the task does not match its documented scope, use the job lead or ask the producer to route it.

## Inputs it needs

- Approved brief, intended audience and output format.
- Source assets and rights/consent status where relevant.
- Relevant production environment and constraints stated by the tool file.

## How to run it

1. Read the source file at `/Users/hustle/.codex/plugins/cache/openai-curated-remote/chatcut-desktop/1.10.14/skills/known-errors/SKILL.md` and confirm its prerequisites.
2. Invoke Claude Code/Codex skill `known-errors` in the supported host.
3. Supply only approved inputs; review the result against the brief.

```text
Use Claude Code/Codex skill `known-errors` for the video-editing task. Brief: {{approved brief}}. Inputs: {{source assets and constraints}}. Return only work supported by the tool instructions, state unknowns, and flag anything that needs human review.
```

## What good output looks like

- Output addresses the supplied brief and requested format.
- Unsupported claims, missing inputs and unresolved rights are identified.

## Quality checks

- [ ] Reviewer other than the maker checks the result against the brief.
- [ ] Claims and provenance are traceable; unknowns are explicit.
- [ ] Accessibility, rights and delivery requirements are checked where applicable.

## Pairs with

- `chatcut-desktop:chatcut-plugin-basics`

## Limits and cautions

- Source: `/Users/hustle/.codex/plugins/cache/openai-curated-remote/chatcut-desktop/1.10.14/skills/known-errors/SKILL.md`. Verify documented prerequisites and scope before relying on output.
- Fetch/manual distribution may require installation or sign-in.
- Follow studio rules: maker ≠ checker; motion only when concept-led; honour reduced motion/accessibility; no client data in public repo.
