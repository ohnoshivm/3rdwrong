---
title: Voice
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: chatcut-desktop:voice
department: media
sub_department: sound-voice
job: voice-and-sound
role: lead
trigger: ""
kind: skill
availability: both
distribution: fetch
source: /Users/hustle/.agents/skills/chatcut-voice/SKILL.md
invoke: "Claude Code/Codex skill `voice`"
pairs_with: []
---
# Voice

The studio's lead tool for voice-and-sound: use it for the documented workflow in media production.

## What it does

- Generate voiceover/narration from text
- Create text-to-speech audio for videos
- Add, replace, or redo narration/voiceover for an existing video, timeline,
- Keep existing narration/voiceover aligned after trimming, speeding up, slowing

## When to use

- At the point in a studio engagement when `voice-and-sound` is required.
- Use after Design direction and required inputs are agreed; keep the human accountable for creative decisions.

## When not to use

- When the task does not match its documented scope, use the job lead or ask the producer to route it.

## Inputs it needs

- Approved brief, intended audience and output format.
- Source assets and rights/consent status where relevant.
- Relevant production environment and constraints stated by the tool file.

## How to run it

1. Read the source file at `/Users/hustle/.agents/skills/chatcut-voice/SKILL.md` and confirm its prerequisites.
2. Invoke Claude Code/Codex skill `voice` in the supported host.
3. Supply only approved inputs; review the result against the brief.

```text
Use Claude Code/Codex skill `voice` for the voice-and-sound task. Brief: {{approved brief}}. Inputs: {{source assets and constraints}}. Return only work supported by the tool instructions, state unknowns, and flag anything that needs human review.
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

- Source: `/Users/hustle/.agents/skills/chatcut-voice/SKILL.md`. Verify documented prerequisites and scope before relying on output.
- Fetch/manual distribution may require installation or sign-in.
- Follow studio rules: maker ≠ checker; motion only when concept-led; honour reduced motion/accessibility; no client data in public repo.
- Client consent is required for AI-generated material in final deliverables (studio contract default).
- Check rights, likeness and source permissions before use.
- Do not send client data in prompts to third-party services without permission.
