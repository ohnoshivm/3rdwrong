---
title: Master Of Media
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:master-of-media
department: operations
sub_department: planning-workflow
job: delivery-discipline
role: specialist
trigger: "Use when the approved work needs this capability: Find dormant ChatCut, audio, voice, transcription, video generation, image generation and media production skills when making or editing creative media"
kind: skill
availability: claude
distribution: manual
source: /Users/hustle/.claude/skills/master-of-media/SKILL.md
invoke: "/master-of-media"
pairs_with: []
---
# Master Of Media

Find dormant ChatCut, audio, voice, transcription, video generation, image generation and media production skills when making or editing creative media at 3RDWRONG as a specialist when the stated trigger applies.

## What it does

- Find dormant ChatCut, audio, voice, transcription, video generation, image generation and media production skills when making or editing creative media
- Follow the tool’s documented workflow and return its stated output.
- Follow the tool’s documented workflow and return its stated output.

## When to use

- Use when the approved work needs this capability: Find dormant ChatCut, audio, voice, transcription, video generation, image generation and media production skills when making or editing creative media
- Use in the relevant studio planning or delivery moment, with the brief and required evidence available.

## When not to use

- When the request falls outside its documented capability; choose a tool whose registry job matches the need.
- To treat generated analysis as client evidence or approval; label interpretation and unknowns.

## Inputs it needs

- The request, context and relevant project artefacts.
- Any constraints, decision owner and desired output format required by the tool’s own instructions.

## How to run it

1. Confirm the tool is installed or available in the active agent environment.
2. Invoke `/master-of-media` in Claude Code or Codex and provide the project context.
3. Review the output against the source instructions; a person other than the maker checks consequential work.

```text
Use /master-of-media for this 3RDWRONG task: {brief}. Context and source artefacts: {links/files}. Constraints: {constraints}. Return the documented output, separate evidence from interpretation, and mark unknowns rather than guessing.
```

## What good output looks like

- Addresses the stated task and produces the documented output for this tool.
- Makes assumptions and missing evidence visible; does not claim results the inputs cannot support.

## Quality checks

- [ ] The output follows the tool’s own instructions and requested scope.
- [ ] Evidence, interpretation, hypothesis and unknowns are distinguished where relevant.
- [ ] A reviewer other than the maker checks material decisions before client sign-off.

## Pairs with

- Registry pairs: Not documented; use only when their hand-off matches the project need.

## Limits and cautions

- Find dormant ChatCut, audio, voice, transcription, video generation, image generation and media production skills when making or editing creative media is the documented scope; other capabilities are Not documented.
- Distribution is `manual`; fetch/manual tools may require installation or sign-in before use.
- Keep client data out of the public repository. Do not present a maker’s output as independent QA.
