---
title: Figma Spec
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: figma:figma-spec
department: design
sub_department: identity-craft
job: handover-specs
role: specialist
trigger: "A Figma file/workspace exists or is explicitly requested, and the task requires spec. Load this prerequisite only for its corresponding Figma operation."
kind: plugin-skill
availability: both
distribution: fetch
source: /Users/hustle/.claude/plugins/cache/claude-plugins-official/figma/2.2.157/skills/figma-spec/SKILL.md
invoke: "Skill name: figma:figma-spec"
pairs_with: [design:design-handoff, agency:engineering-technical-writer, design-steward:brief]
---
# Figma Spec

The Figma Spec is a specialist for handover specifications in 3RDWRONG’s identity-craft work.

## What it does

- This skill is required to create, read, edit, review, or comment on Figma specs. You must read it when working on a PRD, brief, RFC or any kind of document in either a standalone Figma spec or a Figma spec embedded in a Figma Design or Figjam file.
- Use **`getContent`** with the same `specNodeId` before edits and to verify writes; DON'T rely on screenshots.
- Default to multiplayer-safe, surgical **`editContent`**.
- Use destructive **`setContent`** only for an empty first draft or an explicit whole-document replacement.

## When to use

- A Figma file/workspace exists or is explicitly requested, and the task requires spec. Load this prerequisite only for its corresponding Figma operation.
- In practice: use it at Phase 06 Handoff when that specific operation is in the approved scope.

## When not to use

- When the approved direction, source artefact or required inputs are missing; ask for them before proceeding.
- For a request outside this scope, start with the job lead `design:design-handoff` and use another specialist only when its trigger applies.

## Inputs it needs

- Approved direction or source material appropriate to this task.
- The exact artefact, context, constraints and requested decision.
- A supplied Figma file/workspace and a working connection where the requested operation requires one.

## How to run it

1. Collect the approved design artefact, implementation constraints and known decisions.
2. Create the scoped handoff with explicit acceptance criteria and evidence locations.
3. Return open decisions and route implementation questions to the named owner.

```text
Load skill `figma:figma-spec`. Approved direction: {{link and status}}. Job: handover-specs. Bounded scope: {{task}}. Source artefact: {{link or files}}. Context, audience and constraints: {{details}}. Return the documented deliverable, identify evidence and unknowns, and state checks not performed.
```

## What good output looks like

- It addresses the bounded request and names its source artefacts.
- Documented facts, interpretation, hypotheses and unknowns are separated.
- A next owner can act on the deliverable without mistaking it for approval.

## Quality checks

- [ ] An independent reviewer checks the result against the supplied brief and actual artefact.
- [ ] Source-backed claims are distinguishable from Interpretation, Hypothesis and Unknown.
- [ ] The handoff names open issues and next owner; no tool output is treated as approval.

## Pairs with

- `design:design-handoff` — share the approved direction and relevant artefact; return findings for this tool’s next step.
- `agency:engineering-technical-writer` — share the approved direction and relevant artefact; return findings for this tool’s next step.
- `design-steward:brief` — share the approved direction and relevant artefact; return findings for this tool’s next step.

## Limits and cautions

- Distribution is fetch; confirm installation, sign-in and applicable licence limits before use.
- The source describes instructions, not proven runtime quality or live connectivity; confirm setup before claiming an operation ran.
- Maker ≠ checker. Human identity, cultural, optical, material and production judgement remains with the designer; the founder decides.
- Label evidence Documented, Interpretation, Hypothesis or Unknown. Do not claim audience response without observed research.
- Follow D-0006, accessibility and reduced-motion requirements; use motion only when the concept needs it.
- Keep client data out of the public repository (D-0021).
