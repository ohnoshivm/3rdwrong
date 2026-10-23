---
title: Alina Head of Website Department
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:alina-head-of-website-department
department: design
sub_department: direction
job: concept-direction
role: specialist
trigger: "When the approved scope specifically requires starting a studio site, identity touchpoint, or coordinated creative web project."
kind: skill
availability: codex
distribution: manual
source: /Users/hustle/.agents/skills/alina-head-of-website-department/SKILL.md
invoke: "/alina-head-of-website-department skill"
pairs_with: [agent:creative-director, skill:ceos-art-direction, agent:frontend-architect, agent:visual-qa-engineer]
---

# Alina Head of Website Department

A website-project coordinator for research, art direction, interface, implementation hand-off and evidence-based QA. For 3RDWRONG, use this specialist when the registry trigger applies: “When the approved scope specifically requires starting a studio site, identity touchpoint, or coordinated creative web project.”

## What it does

- Frames the objective, audience, action, constraints, references, assets and environment.
- Coordinates research, strategy/art direction, information architecture, design system, engineering, motion and QA.
- Requires evidence labels and says not to claim unrun builds, browser inspections or metrics.
- Requires scope, direction, files/behaviour, executed tests, defects and deployment state in its final output.

## When to use

- When the approved scope specifically requires starting a studio site, identity touchpoint, or coordinated creative web project.
- Use at project start or for a broad site redesign where a cross-discipline workflow is needed.

## When not to use

- A focused identity route decision; use `skill:3w-creative-direction`.
- A small, isolated UI question; select the relevant discipline tool instead.

## Inputs it needs

- Objective, audience, desired action and constraints.
- References, assets, stack and available execution/QA environment.

## How to run it

1. Invoke `/alina-head-of-website-department` in Codex.
2. Give the site brief and say which mode is authorised; default is partner mode per its file.
3. Review work against actual build and browser evidence; record unrun checks as NOT RUN.

```text
Use /alina-head-of-website-department skill. Task: {specific decision or output}. Context: {approved strategy, source links, version and constraints}. Return the documented format, label evidence and unknowns, and stop where required inputs or approval are missing.
```

## What good output looks like

- A coherent hand-off with real assets, responsive behaviour, accessibility and verification limits stated.
- No borrowed identity, fictional proof or claims about work that was not executed.

## Quality checks

- [ ] The output answers the registry job and, for a specialist, the exact trigger.
- [ ] Every factual claim comes from supplied evidence or the tool’s documented method.
- [ ] An independent reviewer checks the output; the maker does not approve their own work.
- [ ] Accessibility, reduced motion and responsive behaviour are checked where relevant.

## Pairs with

- `agent:creative-director` — upstream context or hand-off.
- `skill:ceos-art-direction` — downstream review or delivery.
- `agent:frontend-architect` — downstream review or delivery.
- `agent:visual-qa-engineer` — downstream review or delivery.

## Limits and cautions

- The skill’s partner mode may seek approval before substantial build; follow the user’s approved scope.
- No deployment, purchase or credential change without explicit authorisation.
- Client data stays outside the public repository.
- Manual distribution: installation, account access or sign-in may be required before invocation; verify availability in the target host.
