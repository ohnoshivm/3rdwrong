---
title: High-End Visual Design
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:soft-skill
department: design
sub_department: direction
job: inspiration-taste
role: specialist
trigger: "When the approved scope specifically requires exploring or applying the aesthetic system described by this skill."
kind: skill
availability: both
distribution: manual
source: /Users/hustle/.config/opencode/skills/soft-skill/SKILL.md
invoke: "/high-end-visual-design skill"
pairs_with: [skill:ceos-art-direction, ui-ux-pro-max:ui-ux-pro-max, agent:visual-qa-engineer]
---

# High-End Visual Design

A strongly prescriptive premium-interface aesthetic system for layout, components and motion. For 3RDWRONG, use this specialist when the registry trigger applies: “When the approved scope specifically requires exploring or applying the aesthetic system described by this skill.”

## What it does

- Defines several visual and layout archetypes with mobile overrides.
- Prescribes nested card structures, CTA patterns, typography and spatial rhythm.
- Specifies motion choreography and performance rules.
- Includes a pre-output checklist for the prescribed style.

## When to use

- When the approved scope specifically requires exploring or applying the aesthetic system described by this skill.
- Only when its visual language is a fit for the client brief and reviewed by the art-direction lead.

## When not to use

- 3RDWRONG’s own identity: the file’s dark glass, heavy type and premium-agency prescriptions conflict with D-0006.
- As independent design QA or as the default look for client work.

## Inputs it needs

- Approved concept and existing brand system.
- Device, content and interaction constraints.

## How to run it

1. Invoke `/high-end-visual-design` in Claude Code or Codex.
2. State which archetype and rules are being used and which are rejected for fit.
3. Review the result independently for accessibility, responsive behaviour and reduced motion.

```text
Use /high-end-visual-design skill. Task: {specific decision or output}. Context: {approved strategy, source links, version and constraints}. Return the documented format, label evidence and unknowns, and stop where required inputs or approval are missing.
```

## What good output looks like

- Visual decisions have a project-specific reason and hold across phone and desktop.
- The build does not inherit generic premium styling without a concept rationale.

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

- Strongly prescriptive and potentially unsuitable; project concept takes precedence.
- Do not use its rejected own-identity tropes for 3RDWRONG.
- Motion must respect reduced motion; maker ≠ checker.
- Manual distribution: installation, account access or sign-in may be required before invocation; verify availability in the target host.
