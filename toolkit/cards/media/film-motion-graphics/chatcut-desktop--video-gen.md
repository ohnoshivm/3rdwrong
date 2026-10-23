---
title: Video Gen
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: chatcut-desktop:video-gen
department: media
sub_department: film-motion-graphics
job: video-editing
role: specialist
trigger: "Use for the named production workflow when its format or host matches the brief."
kind: skill
availability: both
distribution: fetch
source: /Users/hustle/.agents/skills/chatcut-video-gen/SKILL.md
invoke: "Claude Code/Codex skill `video-gen`"
pairs_with: [chatcut-desktop:chatcut-plugin-basics]
---
# Video Gen

The studio's specialist for video-editing; activate when Use for the named production workflow when its format or host matches the brief

## What it does

- **User explicitly named a model** ("用 Kling", "use Kling", "用 Omni", "用 mini", "/kling") — switch, no need to re-ask.
- **User explicitly asks for MiniMax H3 or needs combined image/video/audio reference guidance with optional 2K output** — use `minimax-h3`.
- **User explicitly asks for MiniMax H3 Max or wants its highest-fidelity text/frame generation without multimodal references** — use `minimax-h3-max`.
- **Seedance clearly can't or won't do it well** — when you hit a known case where Seedance struggles, propose switching to `kling` and confirm before submitting.

## When to use

- Use for the named production workflow when its format or host matches the brief.

## When not to use

- When the task does not match its documented scope, use the job lead or ask the producer to route it.

## Inputs it needs

- Approved brief, intended audience and output format.
- Source assets and rights/consent status where relevant.
- Relevant production environment and constraints stated by the tool file.

## How to run it

1. Read the source file at `/Users/hustle/.agents/skills/chatcut-video-gen/SKILL.md` and confirm its prerequisites.
2. Invoke Claude Code/Codex skill `video-gen` in the supported host.
3. Supply only approved inputs; review the result against the brief.

```text
Use Claude Code/Codex skill `video-gen` for the video-editing task. Brief: {{approved brief}}. Inputs: {{source assets and constraints}}. Return only work supported by the tool instructions, state unknowns, and flag anything that needs human review.
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

- Source: `/Users/hustle/.agents/skills/chatcut-video-gen/SKILL.md`. Verify documented prerequisites and scope before relying on output.
- Fetch/manual distribution may require installation or sign-in.
- Follow studio rules: maker ≠ checker; motion only when concept-led; honour reduced motion/accessibility; no client data in public repo.
- The studio discloses AI use in its process; AI-generated material in final deliverables requires the client's written consent (D-0023).
- Check rights, likeness and source permissions before use.
- Do not send client data in prompts to third-party services without permission.
