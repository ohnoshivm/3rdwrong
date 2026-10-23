---
title: Industrial Brutalist UI
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:brutalist-skill
department: design
sub_department: direction
job: inspiration-taste
role: specialist
trigger: "When the approved scope specifically requires exploring or applying the aesthetic system described by this skill."
kind: skill
availability: both
distribution: manual
source: /Users/hustle/.config/opencode/skills/brutalist-skill/SKILL.md
invoke: "/industrial-brutalist-ui skill"
pairs_with: [skill:ceos-art-direction, ui-ux-pro-max:ui-ux-pro-max, agent:visual-qa-engineer]
---

# Industrial Brutalist UI

A specialist aesthetic system for deliberately industrial, brutalist digital interfaces. For 3RDWRONG, use this specialist when the registry trigger applies: “When the approved scope specifically requires exploring or applying the aesthetic system described by this skill.”

## What it does

- Offers two distinct territories: Swiss industrial print or tactical telemetry/CRT.
- Defines strict typography, colour, grid and component rules for those territories.
- Specifies interface techniques such as hard grids, square corners and optional analog texture.
- Describes an implementation and review checklist for responsive layouts and interface details.

## When to use

- When the approved scope specifically requires exploring or applying the aesthetic system described by this skill.
- Only for a client direction where an industrial/brutalist territory is explicitly approved.

## When not to use

- 3RDWRONG’s own identity, which has rejected black backgrounds, heavy grotesk and neon under D-0006.
- A general visual direction; use `skill:ceos-art-direction` or `skill:3w-creative-direction`.

## Inputs it needs

- Approved brief that explicitly calls for the brutalist system.
- Content, required interface functions, accessibility and responsive constraints.

## How to run it

1. Invoke `/industrial-brutalist-ui` in Claude Code or Codex.
2. Select one of the two archetypes and state the choice before design work.
3. Check accessibility, responsive behaviour and the client’s own system independently.

```text
Use /industrial-brutalist-ui skill. Task: {specific decision or output}. Context: {approved strategy, source links, version and constraints}. Return the documented format, label evidence and unknowns, and stop where required inputs or approval are missing.
```

## What good output looks like

- One coherent archetype is used rather than mixing the two.
- A deliberate client-approved direction is evident; functional and accessibility checks remain separate.

## Quality checks

- [ ] The output answers the registry job and, for a specialist, the exact trigger.
- [ ] Every factual claim comes from supplied evidence or the tool’s documented method.
- [ ] An independent reviewer checks the output; the maker does not approve their own work.
- [ ] Accessibility, reduced motion and responsive behaviour are checked where relevant.

## Pairs with

- `skill:ceos-art-direction` — upstream context or hand-off.
- `ui-ux-pro-max:ui-ux-pro-max` — downstream review or delivery.
- `agent:visual-qa-engineer` — downstream review or delivery.

## Limits and cautions

- The source mandates highly restrictive stylistic choices; apply only when the brief warrants them.
- Do not apply its dark, heavy or neon options to 3RDWRONG’s own identity.
- It is an aesthetic method, not evidence of audience response or production readiness.
- Manual distribution: installation, account access or sign-in may be required before invocation; verify availability in the target host.
