---
title: Creative Director
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agent:creative-director
department: design
sub_department: direction
job: concept-direction
role: lead
trigger: ""
kind: agent
availability: claude
distribution: vendor
source: toolkit/vendor/pack-founder-local-agents/agents/creative-director.md
invoke: "creative-director agent in the Agent tool"
pairs_with: [skill:3w-creative-direction, agent:ui-ux-architect, agent:visual-designer, agent:frontend-architect]
---

# Creative Director

The visual concept and art-direction lead for a project, with aesthetic authority during refinement. For 3RDWRONG, this is the lead tool for concept direction.

## What it does

- Owns research and art direction, then checks whether the built result matches the direction.
- Returns one Art Direction Document covering concept, type, colour roles, composition, material, motion, interaction, responsive principles, reference principles and clichés to avoid.
- Writes the concept before opening references and extracts mechanisms rather than looks.
- Routes only the needed work to named design and engineering agents.

## When to use

- Phase 03 Strategy to Phase 04 Concept, when an approved brief needs its visual direction and constraints.
- During refinement, to compare a rendered page against the Art Direction Document.

## When not to use

- Implementation, motion or performance ownership; use `agent:frontend-architect`, `agent:motion-director` or `agent:performance-engineer`.
- Brand identity route selection under the 3RDWRONG identity method; use `skill:3w-creative-direction` as the identity gate.

## Inputs it needs

- Goal, audience, brand assets, page inventory, hard constraints and any site to beat or replace.
- The approved strategy and reference sources where applicable.

## How to run it

1. Open the `creative-director` agent in Claude Code with the brief and constraints.
2. Ask for one Art Direction Document in the source’s ten-part hand-off shape.
3. Compare the build against it using rendered evidence; record “visual QA: unverified” if no responsive screenshots were inspected.

```text
Use creative-director agent in the Agent tool. Task: {specific decision or output}. Context: {approved strategy, source links, version and constraints}. Return the documented format, label evidence and unknowns, and stop where required inputs or approval are missing.
```

## What good output looks like

- A single clear concept and concrete rules that a builder can apply.
- References carry principles and explicit never-copy boundaries.

## Quality checks

- [ ] The output answers the registry job and, for a specialist, the exact trigger.
- [ ] Every factual claim comes from supplied evidence or the tool’s documented method.
- [ ] An independent reviewer checks the output; the maker does not approve their own work.
- [ ] Accessibility, reduced motion and responsive behaviour are checked where relevant.

## Pairs with

- `skill:3w-creative-direction` — upstream context or hand-off.
- `agent:ui-ux-architect` — downstream review or delivery.
- `agent:visual-designer` — downstream review or delivery.
- `agent:frontend-architect` — downstream review or delivery.

## Limits and cautions

- Read-only: the agent does not edit files or run shell commands.
- Maker and checker must remain separate.
- The source requires screenshot evidence before claiming visual verification; respect reduced motion and accessibility.
