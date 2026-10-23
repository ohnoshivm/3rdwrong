---
title: Figma Generate Diagram
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: figma:figma-generate-diagram
department: design
sub_department: identity-craft
job: presentation
role: specialist
trigger: "A Figma file/workspace exists or is explicitly requested, and the task requires generate diagram. Load this prerequisite only for its corresponding Figma operation."
kind: plugin-skill
availability: both
distribution: fetch
source: /Users/hustle/.claude/plugins/cache/claude-plugins-official/figma/2.2.120/skills-figquery/figma-generate-diagram/SKILL.md
invoke: "Skill name: figma:figma-generate-diagram"
pairs_with: [anthropic-skills:pptx, agency:design-visual-storyteller, agency:sales-proposal-strategist]
---
# Figma Generate Diagram

The Figma Generate Diagram is a specialist for presentation in 3RDWRONG’s identity-craft work.

## What it does

- MANDATORY prerequisite — load this skill BEFORE every `generate_diagram` tool call. NEVER call `generate_diagram` directly without loading this skill first. Trigger whenever the user asks to create, generate, draw, render, sketch, or build a diagram — flowchart, architecture diagram, sequence diagram, ERD or entity-relationship diagram, state diagram or state machine, gantt chart, or timeline. Also trigger when the user mentions Mermaid syntax or wants a system architecture, decision tree, dependency graph, API call flow, auth handshake, schema, or pipeline visualized in FigJam. Routes to type-specific guidance, sets universal Mermaid constraints, and tells you when to use a different diagram type or skip the tool entirely (mindmaps, pie charts, class diagrams, etc.).
- **Pie chart, mindmap, venn diagram, class diagram, journey, timeline, quadrant, C4, git graph, requirement diagram**.
- Change fonts on an existing diagram.
- Edit a diagram node-by-node after generation.

## When to use

- A Figma file/workspace exists or is explicitly requested, and the task requires generate diagram. Load this prerequisite only for its corresponding Figma operation.
- In practice: use it at Phase 05 Application when that specific operation is in the approved scope.

## When not to use

- When the approved direction, source artefact or required inputs are missing; ask for them before proceeding.
- For a request outside this scope, start with the job lead `anthropic-skills:pptx` and use another specialist only when its trigger applies.

## Inputs it needs

- Approved direction or source material appropriate to this task.
- The exact artefact, context, constraints and requested decision.
- A supplied Figma file/workspace and a working connection where the requested operation requires one.
- Verified content, data and brand assets; identify unverified claims.

## How to run it

1. Organise the approved content around the audience and purpose.
2. Use the tool for the requested document or presentation operation.
3. Check claims, hierarchy and brand fit; hand the file to an independent reviewer.

```text
Load skill `figma:figma-generate-diagram`. Approved direction: {{link and status}}. Job: presentation. Bounded scope: {{task}}. Source artefact: {{link or files}}. Context, audience and constraints: {{details}}. Return the documented deliverable, identify evidence and unknowns, and state checks not performed.
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

- `anthropic-skills:pptx` — share the approved direction and relevant artefact; return findings for this tool’s next step.
- `agency:design-visual-storyteller` — share the approved direction and relevant artefact; return findings for this tool’s next step.
- `agency:sales-proposal-strategist` — share the approved direction and relevant artefact; return findings for this tool’s next step.

## Limits and cautions

- Distribution is fetch; confirm installation, sign-in and applicable licence limits before use.
- The source describes instructions, not proven runtime quality or live connectivity; confirm setup before claiming an operation ran.
- Maker ≠ checker. Human identity, cultural, optical, material and production judgement remains with the designer; the founder decides.
- Label evidence Documented, Interpretation, Hypothesis or Unknown. Do not claim audience response without observed research.
- Follow D-0006, accessibility and reduced-motion requirements; use motion only when the concept needs it.
- Keep client data out of the public repository (D-0021).
