---
title: GPT Image 2 Director
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: anthropic-skills:gpt-image-2-director
department: design
sub_department: identity-craft
job: image-generation-direction
role: lead
trigger: ""
kind: plugin-skill
availability: claude-managed
distribution: manual
source: /Users/hustle/.claude/skills/synced/88e7af4e-a2cf-4b40-8488-91a856697e04_aa2d1473-adba-46ff-9558-93fbf2ea6240/gpt-image-2-director/SKILL.md
invoke: "Skill name: anthropic-skills:gpt-image-2-director"
pairs_with: [agency:design-image-prompt-engineer, agency:design-inclusive-visuals-specialist, creative-production:produce]
---
# GPT Image 2 Director

The GPT Image 2 Director is 3RDWRONG’s lead for image-generation-direction.

## What it does

- GPT Image 2.0 prompt director. Converts plain-text concepts into production-ready prompts for GPT Image 2.0, routing by output type — structured JSON (for UI mockups, infographics, landing pages, posters with dense layouts, character reference sheets, social media mockups, editorial/document layouts) vs. dense cinematic prose (for portraits, single-image cinematic scenes, editorial photography) vs. auto-derive meta-prompts (for concept posters, relationship diagrams, where the model should self-generate the entire composition from a single theme). Use this skill whenever the user asks for a GPT Image 2.0 prompt, says "make a GPT image prompt", mentions GPT-Image 2, gpt-image-2, or describes anything they want to generate with GPT Image 2.0 — posters, mockups, infographics, character sheets, editorial layouts, landing pages, or cinematic single images. Also trigger if the user pastes a rough concept and says "turn this into a GPT image prompt" or "prompt this for GPT Image 2".
- **Text rendering is best-in-class.** Multi-line paragraphs, mixed scripts (CJK + Latin), small UI labels, serif vs sans, numeric data in tables — all sharp and legible.
- **Design and UI mockups are its sweet spot.** Website landing pages, social feeds, magazine covers, infographics, exploded product diagrams, exam papers — things with real information density.
- `type` — one-line description of what this image is ("infographic poster", "landing page mockup", "exploded view diagram", "anime character reference sheet", "social media app interface mockup").

## When to use

- Phase 04 Concept or asset production, when the approved direction and the source artefact are ready for image generation direction.
- Use it to lead this job; keep the founder’s decision and an independent check separate from its output.

## When not to use

- When the approved direction, source artefact or required inputs are missing; ask for them before proceeding.
- For work outside this scope, route to `agency:design-image-prompt-engineer` for its related operation; do not use this tool as a general-purpose design lead.

## Inputs it needs

- Approved direction or source material appropriate to this task.
- The exact artefact, context, constraints and requested decision.
- Approved concept, intended use, aspect ratio and representation/rights constraints.

## How to run it

1. Start from the approved concept, intended use and representation constraints.
2. Prepare the source-defined image direction or prompt for the named generation workflow.
3. Review the output against the brief and mark generated or unverified elements clearly.

```text
Load skill `anthropic-skills:gpt-image-2-director`. Approved direction: {{link and status}}. Job: image-generation-direction. Bounded scope: {{task}}. Source artefact: {{link or files}}. Context, audience and constraints: {{details}}. Return the documented deliverable, identify evidence and unknowns, and state checks not performed.
```

## What good output looks like

- It addresses the bounded request and names its source artefacts.
- Documented facts, interpretation, hypotheses and unknowns are separated.
- A next owner can act on the deliverable without mistaking it for approval.

## Quality checks

- [ ] An independent reviewer checks the result against the supplied brief and actual artefact.
- [ ] Source-backed claims are distinguishable from Interpretation, Hypothesis and Unknown.
- [ ] The handoff names open issues and next owner; no tool output is treated as approval.
- [ ] Representation and rights concerns are reviewed by a human before use.

## Pairs with

- `agency:design-image-prompt-engineer` — share the approved direction and relevant artefact; return findings for this tool’s next step.
- `agency:design-inclusive-visuals-specialist` — share the approved direction and relevant artefact; return findings for this tool’s next step.
- `creative-production:produce` — share the approved direction and relevant artefact; return findings for this tool’s next step.

## Limits and cautions

- Distribution is manual; confirm installation, sign-in and applicable licence limits before use.
- The source describes instructions, not proven runtime quality or live connectivity; confirm setup before claiming an operation ran.
- Maker ≠ checker. Human identity, cultural, optical, material and production judgement remains with the designer; the founder decides.
- Label evidence Documented, Interpretation, Hypothesis or Unknown. Do not claim audience response without observed research.
- Follow D-0006, accessibility and reduced-motion requirements; use motion only when the concept needs it.
- Keep client data out of the public repository (D-0021).
