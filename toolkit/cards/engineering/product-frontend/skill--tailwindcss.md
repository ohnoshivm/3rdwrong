---
title: Tailwind CSS
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:tailwindcss
department: engineering
sub_department: product-frontend
job: ui-implementation
role: specialist
trigger: "When the approved scope specifically requires use when the task specifically needs use when designing/implementing ui with tailwind css (layout, typography, responsive, theming, component patterns)."
kind: skill
availability: both
distribution: manual
source: /Users/hustle/.claude/skills-library/master-of-20261021/visual-design/tailwindcss/SKILL.md
invoke: "tailwindcss skill"
pairs_with: [skill:shadcn, agent:frontend-architect]
---
# Tailwind CSS

Tailwind CSS is the studio's specialist for `ui-implementation`; use it when the registry trigger below applies.

## What it does

- Guides utility patterns for layout, typography, responsive design and theming
- Covers state variants and component extraction
- Warns about content scanning and dynamic class construction

## When to use

- When the approved scope specifically requires use when the task specifically needs use when designing/implementing ui with tailwind css (layout, typography, responsive, theming, component patterns).
- When approved UI implementation uses Tailwind
- Phase 05

## When not to use

- For other styling systems follow project conventions
- For shadcn component workflows use `skill:shadcn`
- Do not use to approve its own work; assign a separate checker.

## Inputs it needs

- Tailwind version and build scan configuration
- Tokens and responsive states
- Component boundaries

## How to run it

1. Confirm the task matches the job and, for a specialist, the registry trigger.
2. Invoke `tailwindcss skill` and provide the approved brief, artefacts, constraints and source context.
3. Ask for the documented deliverable; inspect assumptions and verification before handoff.

```text
Use `skill:tailwindcss` for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform/version: {links and versions}. Constraints: {accessibility, performance, delivery}. Work within the documented scope and registry trigger. Label evidence Documented, Interpretation, Hypothesis or Unknown; return the requested artefact, assumptions, limitations, verification actually performed and a concrete next action.
```

## What good output looks like

- Consistent responsive utilities and generated CSS
- Repeated patterns extracted appropriately

## Quality checks

- [ ] Work matches the approved brief and the maker is not its checker.
- [ ] Claims are supported by source or supplied evidence; label uncertainty explicitly.
- [ ] Responsive behaviour, accessibility and performance are checked where they apply.
- [ ] Verification lists only commands, tests or browser checks actually run.

## Pairs with

- `skill:shadcn` — coordinate the artefacts and handoff at the relevant stage.
- `agent:frontend-architect` — coordinate the artefacts and handoff at the relevant stage.

## Limits and cautions

- Arbitrary values sparingly
- avoid oversized classes and verify content scanning
- Keep client data and credentials out of the public repository (D-0021); check licence and distribution prerequisites, including installation or sign-in when required.
