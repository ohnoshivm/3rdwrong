---
title: Figma Use
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: figma:figma-use
department: design
sub_department: identity-craft
job: composition-layout
role: specialist
trigger: "A Figma file/workspace exists or is explicitly requested, and the task requires use. Load this prerequisite only for its corresponding Figma operation."
kind: plugin-skill
availability: both
distribution: fetch
source: /Users/hustle/.claude/plugins/cache/claude-plugins-official/figma/2.2.120/skills-figquery/figma-use/SKILL.md
invoke: "Skill name: figma:figma-use"
pairs_with: [design-skills:design-elevation, figma:figma-create-new-file, mcp:stitch]
---
# Figma Use

The Figma Use is a specialist for composition and layout in 3RDWRONG’s identity-craft work.

## What it does

- **MANDATORY prerequisite** — you MUST invoke this skill BEFORE every `use_figma` tool call. NEVER call `use_figma` directly without loading this skill first. Skipping it causes common, hard-to-debug failures. Trigger whenever the user wants to perform a write action or a unique read action that requires JavaScript execution in the Figma file context — e.g. create/edit/delete nodes, set up variables or tokens, build components and variants, modify auto-layout or fills, bind variables to properties, or inspect file structure programmatically.
- **Create:** `$fig.autoLayout / .frame / .text / .rectangle / .ellipse / .polygon / .star / .line / .vector / .section / .component / .page` — all `(opts?, children?)`. Plan nodes are chainable.
- **Grouping/boolean:** `$fig.group / .union / .subtract / .intersect / .exclude / .variants` — all `(opts?, children?)`.
- **Things `$fig` genuinely doesn't expose:** `node.setRangeFontName(...)`, etc. — access via `planNode.node` (see references/fig-builder.md (upstream reference `references/fig-builder.md`)).

## When to use

- A Figma file/workspace exists or is explicitly requested, and the task requires use. Load this prerequisite only for its corresponding Figma operation.
- In practice: use it at Phase 04 Concept or Phase 05 Application when that specific operation is in the approved scope.

## When not to use

- When the approved direction, source artefact or required inputs are missing; ask for them before proceeding.
- For work outside this scope, route to `design-skills:design-elevation` for its related operation; do not use this tool as a general-purpose design lead.

## Inputs it needs

- Approved direction or source material appropriate to this task.
- The exact artefact, context, constraints and requested decision.
- A supplied Figma file/workspace and a working connection where the requested operation requires one.

## How to run it

1. Check the approved brief, source artefact and required prerequisites; record missing inputs.
2. Invoke the tool with the bounded request and supplied constraints.
3. Return its documented deliverable with evidence, unresolved points and a named next owner for independent review.

```text
Load skill `figma:figma-use`. Approved direction: {{link and status}}. Job: composition-layout. Bounded scope: {{task}}. Source artefact: {{link or files}}. Context, audience and constraints: {{details}}. Return the documented deliverable, identify evidence and unknowns, and state checks not performed.
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

- `design-skills:design-elevation` — share the approved direction and relevant artefact; return findings for this tool’s next step.
- `figma:figma-create-new-file` — share the approved direction and relevant artefact; return findings for this tool’s next step.
- `mcp:stitch` — share the approved direction and relevant artefact; return findings for this tool’s next step.

## Limits and cautions

- Distribution is fetch; confirm installation, sign-in and applicable licence limits before use.
- The source describes instructions, not proven runtime quality or live connectivity; confirm setup before claiming an operation ran.
- Maker ≠ checker. Human identity, cultural, optical, material and production judgement remains with the designer; the founder decides.
- Label evidence Documented, Interpretation, Hypothesis or Unknown. Do not claim audience response without observed research.
- Follow D-0006, accessibility and reduced-motion requirements; use motion only when the concept needs it.
- Keep client data out of the public repository (D-0021).
