---
title: Chatcut Plugin Basics
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: chatcut-desktop:chatcut-plugin-basics
department: media
sub_department: film-motion-graphics
job: video-editing
role: lead
trigger: ""
kind: plugin-skill
availability: both
distribution: fetch
source: /Users/hustle/.codex/plugins/cache/openai-curated-remote/chatcut-desktop/1.10.14/skills/chatcut-plugin-basics/SKILL.md
invoke: "Claude Code/Codex skill `chatcut-plugin-basics`"
pairs_with: []
---
# Chatcut Plugin Basics

The studio's lead tool for video-editing: use it for the documented workflow in media production.

## What it does

- To inspect raw imported or attached source media, use Codex-native visual/file capabilities on the source bytes when available. Do not create a temporary timeline just to inspect source assets.
- "Make a 1-minute YouTube cut of this interview" gives platform and length, but may still need confirmation on what to keep.
- "Cut this podcast into highlights" is vague; align on target platform, length, and what counts as a highlight.
- "Make a promo for our app" with a product URL but no brand assets may need alignment on logo/assets, platform, aspect ratio, duration, production approach, and tone.

## When to use

- At the point in a studio engagement when `video-editing` is required.
- Use after Design direction and required inputs are agreed; keep the human accountable for creative decisions.

## When not to use

- When the task does not match its documented scope, use the job lead or ask the producer to route it.

## Inputs it needs

- Approved brief, intended audience and output format.
- Source assets and rights/consent status where relevant.
- Relevant production environment and constraints stated by the tool file.

## How to run it

1. Read the source file at `/Users/hustle/.codex/plugins/cache/openai-curated-remote/chatcut-desktop/1.10.14/skills/chatcut-plugin-basics/SKILL.md` and confirm its prerequisites.
2. Invoke Claude Code/Codex skill `chatcut-plugin-basics` in the supported host.
3. Supply only approved inputs; review the result against the brief.

```text
Use Claude Code/Codex skill `chatcut-plugin-basics` for the video-editing task. Brief: {{approved brief}}. Inputs: {{source assets and constraints}}. Return only work supported by the tool instructions, state unknowns, and flag anything that needs human review.
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

- Source: `/Users/hustle/.codex/plugins/cache/openai-curated-remote/chatcut-desktop/1.10.14/skills/chatcut-plugin-basics/SKILL.md`. Verify documented prerequisites and scope before relying on output.
- Fetch/manual distribution may require installation or sign-in.
- Follow studio rules: maker ≠ checker; motion only when concept-led; honour reduced motion/accessibility; no client data in public repo.
