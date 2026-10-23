---
title: Chatcut Widget Forms
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:chatcut-widget-forms
department: media
sub_department: film-motion-graphics
job: media-tool-access
role: specialist
trigger: "Use for the matching ChatCut support or input task."
kind: skill
availability: both
distribution: manual
source: /Users/hustle/.agents/skills/chatcut-widget-forms/SKILL.md
invoke: "Claude Code/Codex skill `chatcut-widget-forms`"
pairs_with: [chatcut-desktop:widget-forms]
---
# Chatcut Widget Forms

The studio's specialist for media-tool-access; activate when Use for the matching ChatCut support or input task

## What it does

- Choose the interaction protocol from the active host, not from whether the
- Write `<choices/>` and `<widget>...</widget>` directly in the assistant
- Use `<choices/>` only for one text-only decision. Use `<widget>` for
- Do not call `ask_followup_questions`, discover `visualize`, or call

## When to use

- Use for the matching ChatCut support or input task.

## When not to use

- When the task does not match its documented scope, use the job lead or ask the producer to route it.

## Inputs it needs

- Approved brief, intended audience and output format.
- Source assets and rights/consent status where relevant.
- Relevant production environment and constraints stated by the tool file.

## How to run it

1. Read the source file at `/Users/hustle/.agents/skills/chatcut-widget-forms/SKILL.md` and confirm its prerequisites.
2. Invoke Claude Code/Codex skill `chatcut-widget-forms` in the supported host.
3. Supply only approved inputs; review the result against the brief.

```text
Use Claude Code/Codex skill `chatcut-widget-forms` for the media-tool-access task. Brief: {{approved brief}}. Inputs: {{source assets and constraints}}. Return only work supported by the tool instructions, state unknowns, and flag anything that needs human review.
```

## What good output looks like

- Output addresses the supplied brief and requested format.
- Unsupported claims, missing inputs and unresolved rights are identified.

## Quality checks

- [ ] Reviewer other than the maker checks the result against the brief.
- [ ] Claims and provenance are traceable; unknowns are explicit.
- [ ] Accessibility, rights and delivery requirements are checked where applicable.

## Pairs with

- `chatcut-desktop:widget-forms`

## Limits and cautions

- Source: `/Users/hustle/.agents/skills/chatcut-widget-forms/SKILL.md`. Verify documented prerequisites and scope before relying on output.
- Distribution and runtime availability are not guaranteed by this card.
- Follow studio rules: maker ≠ checker; motion only when concept-led; honour reduced motion/accessibility; no client data in public repo.
