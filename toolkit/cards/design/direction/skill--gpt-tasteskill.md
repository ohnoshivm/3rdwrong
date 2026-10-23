---
title: GPT Taste Skill
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:gpt-tasteskill
department: design
sub_department: direction
job: inspiration-taste
role: specialist
trigger: "When the approved scope specifically requires exploring or applying the aesthetic system described by this skill."
kind: skill
availability: both
distribution: manual
source: /Users/hustle/.config/opencode/skills/gpt-tasteskill/SKILL.md
invoke: "/gpt-taste skill"
pairs_with: [skill:ceos-art-direction, ui-ux-pro-max:ui-ux-pro-max, skill:motion]
---

# GPT Taste Skill

A web-interface style skill prescribing a highly opinionated layout, typography and GSAP motion system. For 3RDWRONG, use this specialist when the registry trigger applies: “When the approved scope specifically requires exploring or applying the aesthetic system described by this skill.”

## What it does

- Prescribes a pre-flight design plan, an AIDA page structure and wide hero headlines.
- Requires a selection process for hero, typography, components and motion patterns.
- Specifies GSAP scroll choreography and reduced-motion fallbacks.
- Includes explicit anti-patterns, content and implementation requirements.

## When to use

- When the approved scope specifically requires exploring or applying the aesthetic system described by this skill.
- Only when its prescriptive website approach is compatible with the approved concept and 3RDWRONG guardrails.

## When not to use

- As the general design lead or as unreviewed authority over studio identity; use `skill:3w-creative-direction` and `skill:ceos-art-direction`.
- When the AIDA/GSAP requirements conflict with a project’s actual content or accessibility needs.

## Inputs it needs

- Approved concept, actual project content and existing stack.
- Motion purpose, viewport requirements and reduced-motion expectations.

## How to run it

1. Invoke `/gpt-taste` in Claude Code or Codex.
2. State which rules are applicable and reject any conflict with the approved concept or studio guardrails.
3. Inspect responsive output and reduced-motion behaviour before acceptance.

```text
Use /gpt-taste skill. Task: {specific decision or output}. Context: {approved strategy, source links, version and constraints}. Return the documented format, label evidence and unknowns, and stop where required inputs or approval are missing.
```

## What good output looks like

- The UI is concept-led and responsive, and animation has an accessible static state.
- No arbitrary randomisation or prescribed pattern is mistaken for evidence of fit.

## Quality checks

- [ ] The output answers the registry job and, for a specialist, the exact trigger.
- [ ] Every factual claim comes from supplied evidence or the tool’s documented method.
- [ ] An independent reviewer checks the output; the maker does not approve their own work.
- [ ] Accessibility, reduced motion and responsive behaviour are checked where relevant.

## Pairs with

- `skill:ceos-art-direction` — upstream context or hand-off.
- `ui-ux-pro-max:ui-ux-pro-max` — downstream review or delivery.
- `skill:motion` — downstream review or delivery.

## Limits and cautions

- The skill contains strong prescriptive rules that may conflict with a brief; studio and accessibility guardrails take precedence.
- Do not add dependencies or motion without a clear purpose.
- Never use 3RDWRONG’s rejected own-identity look.
- Manual distribution: installation, account access or sign-in may be required before invocation; verify availability in the target host.
