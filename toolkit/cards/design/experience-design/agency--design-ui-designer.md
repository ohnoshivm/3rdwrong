---
title: UI Designer
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:design-ui-designer
department: design
sub_department: experience-design
job: ui-design
role: specialist
trigger: "When the approved scope specifically requires composition layout expertise."
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/design-ui-designer.md
invoke: "Claude Code Agent tool: UI Designer"
pairs_with: [frontend-design:frontend-design, skill:designing-frontend-interfaces, agent:ui-ux-architect]
---
# UI Designer

The experience-design specialist for `ui-design` is UI Designer (trigger: “When the approved scope specifically requires composition layout expertise”), which designs interface systems, component libraries and polished screens that reflect the supplied brand.

## What it does

- Component and token systems.
- responsive screen and interaction prototypes.
- design handoff and component documentation.

## When to use

- Use when an approved scope needs visual composition and screen-level craft. Use Phase 05 Prototype when translating an approved concept and identity into screens.
- When the approved scope specifically requires composition layout expertise.

## When not to use

- Use `frontend-design:frontend-design` for original visual direction, or `vectorlab-ux-skills:page-patterns` for one missing page structure.
- Do not use it to approve its own work; have an independent reviewer check the artefact.

## Inputs it needs

- Brand direction, screen scope, design system or component constraints, target devices.
- Versioned approved brief/strategy and source links; mark draft material as formative.

## How to run it

1. Confirm the trigger, stage and source material; keep client data in the approved private store.
2. Run it using the invocation above and provide the required inputs.
3. Check the output against the quality checks; hand unresolved decisions to the named human owner.

```text
Use Claude Code Agent tool: UI Designer. Studio phase: {phase}. Project: {project}. Approved goal/strategy: {goal and source}. Scope: {screen, flow or interaction}. Inputs/evidence: {links and versions}. Constraints: {platform, accessibility, motion, privacy}. Produce a system grounded in the given brief, with documented components, responsive states and a developer-ready handoff. Keep documented facts separate from interpretation and hypothesis; list unknowns and the next human decision.
```

## What good output looks like

- A component and visual hierarchy specification, with responsive states and accessible behaviour stated.
- Evidence claims are labelled Documented, Interpretation, Hypothesis or Unknown as applicable.
- The output names open questions, owner and next action.

## Quality checks

- [ ] An independent checker verifies the output against the approved scope and artefact version.
- [ ] No unsupported user, audience, accessibility, performance or business outcome is presented as fact.
- [ ] Responsive, keyboard/focus and reduced-motion needs are included where relevant.

## Pairs with

- Related tools: `skill:frontend-design`, `skill:designing-frontend-interfaces`, `agent:ui-ux-architect`. Use the relevant method or specialist to complete the handoff.
- Engineering owns implementation, general testing, performance and security; Design owns experience intent and craft.

## Limits and cautions

- Treat its own example tokens as examples, not client values. Accessibility and performance requirements need independent verification.
- Respect the tool distribution: vendor copies are repo snapshots; fetch/manual sources need their stated install or sign-in.
- Client data, personal data and credentials stay out of the public repository.
- Motion is purposeful and honours reduced motion; avoid the rejected own-identity vocabulary in D-0006.
