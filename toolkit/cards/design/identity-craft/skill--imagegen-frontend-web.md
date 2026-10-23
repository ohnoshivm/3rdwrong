---
title: Imagegen Frontend Web
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:imagegen-frontend-web
department: design
sub_department: identity-craft
job: image-generation-direction
role: specialist
trigger: "When the approved scope specifically requires generating website or mobile screen design references."
kind: skill
availability: both
distribution: manual
source: /Users/hustle/.config/opencode/skills/imagegen-frontend-web/SKILL.md
invoke: "Skill name: skill:imagegen-frontend-web"
pairs_with: [anthropic-skills:gpt-image-2-director, agency:design-image-prompt-engineer, agency:design-inclusive-visuals-specialist]
---
# Imagegen Frontend Web

The Imagegen Frontend Web is a specialist for image-generation direction in 3RDWRONG’s identity-craft work.

## What it does

- Elite frontend image-direction skill for generating premium, conversion-aware website design references. CRITICAL OUTPUT RULE — generate ONE separate horizontal image FOR EVERY section. A landing page with 8 sections produces 8 images. Never compress multiple sections into one image. Enforces composition variety (not always left-text / right-image), background-image freedom, varied CTAs, varied hero scales (giant / mid / mini minimalist), narrative concept spine, second-read moments, and a single consistent palette across all images. Optimized for landing pages, marketing sites, and product comps that developers or coding models can accurately recreate.
- 1 section requested -> 1 image.
- 4 sections requested -> 4 images.
- 8 sections requested -> 8 images.

## When to use

- When the approved scope specifically requires generating website or mobile screen design references.
- In practice: use it at Phase 04 Concept or asset production when that specific operation is in the approved scope.

## When not to use

- When the approved direction, source artefact or required inputs are missing; ask for them before proceeding.
- For a request outside this scope, start with the job lead `anthropic-skills:gpt-image-2-director` and use another specialist only when its trigger applies.

## Inputs it needs

- Approved direction or source material appropriate to this task.
- The exact artefact, context, constraints and requested decision.
- Approved concept, intended use, aspect ratio and representation/rights constraints.

## How to run it

1. Start from the approved concept, intended use and representation constraints.
2. Prepare the source-defined image direction or prompt for the named generation workflow.
3. Review the output against the brief and mark generated or unverified elements clearly.

```text
Load skill `skill:imagegen-frontend-web`. Approved direction: {{link and status}}. Job: image-generation-direction. Bounded scope: {{task}}. Source artefact: {{link or files}}. Context, audience and constraints: {{details}}. Return the documented deliverable, identify evidence and unknowns, and state checks not performed.
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

- `anthropic-skills:gpt-image-2-director` — share the approved direction and relevant artefact; return findings for this tool’s next step.
- `agency:design-image-prompt-engineer` — share the approved direction and relevant artefact; return findings for this tool’s next step.
- `agency:design-inclusive-visuals-specialist` — share the approved direction and relevant artefact; return findings for this tool’s next step.

## Limits and cautions

- Distribution is manual; confirm installation, sign-in and applicable licence limits before use.
- The source describes instructions, not proven runtime quality or live connectivity; confirm setup before claiming an operation ran.
- Maker ≠ checker. Human identity, cultural, optical, material and production judgement remains with the designer; the founder decides.
- Label evidence Documented, Interpretation, Hypothesis or Unknown. Do not claim audience response without observed research.
- Follow D-0006, accessibility and reduced-motion requirements; use motion only when the concept needs it.
- Keep client data out of the public repository (D-0021).
