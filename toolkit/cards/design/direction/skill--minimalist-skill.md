---
title: Minimalist Skill
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:minimalist-skill
department: design
sub_department: direction
job: inspiration-taste
role: specialist
trigger: "When the approved scope specifically requires exploring or applying the aesthetic system described by this skill."
kind: skill
availability: both
distribution: manual
source: /Users/hustle/.config/opencode/skills/minimalist-skill/SKILL.md
invoke: "/minimalist-skill skill"
pairs_with: [skill:ceos-art-direction, skill:dieter-rams-principles, ui-ux-pro-max:ui-ux-pro-max]
---

# Minimalist Skill

A specialist aesthetic system for minimal digital interfaces and visual exploration. For 3RDWRONG, use this specialist when the registry trigger applies: “When the approved scope specifically requires exploring or applying the aesthetic system described by this skill.”

## What it does

- Defines an opinionated web-interface style with typography, palette, component and motion prescriptions.
- Provides responsive and performance directives.
- Includes an execution protocol and pre-output checklist.
- Specific studio-specific validation: Not documented in the inspected opening 120 lines.

## When to use

- When the approved scope specifically requires exploring or applying the aesthetic system described by this skill.
- Use only when the minimalist direction answers the project brief.

## When not to use

- As a default for every project or to replace the studio’s art-direction lead.
- For independent accessibility or visual QA; use the appropriate reviewer.

## Inputs it needs

- Approved concept and content, plus constraints on stack, brand assets and audience.
- A real use case to decide what should be removed and what must remain.

## How to run it

1. Invoke `/minimalist-skill` in Claude Code or Codex.
2. Select only rules that support the approved concept; challenge unsupported prescriptions.
3. Inspect responsive states, content completeness, keyboard use and reduced motion.

```text
Use /minimalist-skill skill. Task: {specific decision or output}. Context: {approved strategy, source links, version and constraints}. Return the documented format, label evidence and unknowns, and stop where required inputs or approval are missing.
```

## What good output looks like

- Every remaining element supports the project’s purpose.
- The interface stays clear and usable at phone size and without motion.

## Quality checks

- [ ] The output answers the registry job and, for a specialist, the exact trigger.
- [ ] Every factual claim comes from supplied evidence or the tool’s documented method.
- [ ] An independent reviewer checks the output; the maker does not approve their own work.
- [ ] Accessibility, reduced motion and responsive behaviour are checked where relevant.

## Pairs with

- `skill:ceos-art-direction` — upstream context or hand-off.
- `skill:dieter-rams-principles` — downstream review or delivery.
- `ui-ux-pro-max:ui-ux-pro-max` — downstream review or delivery.

## Limits and cautions

- The skill is prescriptive; do not follow rules that conflict with brand or accessibility.
- Do not apply the studio’s rejected own-identity visual tropes.
- Use as an aesthetic reference, not evidence of audience preference.
- Manual distribution: installation, account access or sign-in may be required before invocation; verify availability in the target host.
