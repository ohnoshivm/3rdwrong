---
title: UX Architect
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:design-ux-architect
department: design
sub_department: experience-design
job: interaction-architecture
role: specialist
trigger: "When the approved scope specifically requires interaction architecture expertise."
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/design-ux-architect.md
invoke: "Claude Code Agent tool: UX Architect"
pairs_with: [skill:designing-user-experience, agent:ui-ux-architect, skill:ceos-interaction-architecture]
---
# UX Architect

The experience-design specialist for `interaction-architecture` is UX Architect (trigger: “When the approved scope specifically requires interaction architecture expertise”), which turns a product brief into implementable ux and technical foundations for interface structure.

## What it does

- Defines information architecture and content hierarchy.
- proposes CSS/layout systems and responsive rules.
- specifies component boundaries and interaction patterns.

## When to use

- Use when an approved digital scope needs an interaction architecture handoff. Use Phase 04 Concept to settle journeys and structure before screen design.
- When the approved scope specifically requires interaction architecture expertise.

## When not to use

- Use `skill:designing-user-experience` for broader UX method, or `agent:ui-ux-architect` for studio-owned flow and state contracts.
- Do not use it to approve its own work; have an independent reviewer check the artefact.

## Inputs it needs

- Approved goals, content inventory, platform constraints, existing design language.
- Versioned approved brief/strategy and source links; mark draft material as formative.

## How to run it

1. Confirm the trigger, stage and source material; keep client data in the approved private store.
2. Run it using the invocation above and provide the required inputs.
3. Check the output against the quality checks; hand unresolved decisions to the named human owner.

```text
Use Claude Code Agent tool: UX Architect. Studio phase: {phase}. Project: {project}. Approved goal/strategy: {goal and source}. Scope: {screen, flow or interaction}. Inputs/evidence: {links and versions}. Constraints: {platform, accessibility, motion, privacy}. Produce a buildable route/flow map, component and state inventory, responsive strategy and unresolved questions. Keep documented facts separate from interpretation and hypothesis; list unknowns and the next human decision.
```

## What good output looks like

- A structured UX and implementation foundation with explicit dependencies and open decisions.
- Evidence claims are labelled Documented, Interpretation, Hypothesis or Unknown as applicable.
- The output names open questions, owner and next action.

## Quality checks

- [ ] An independent checker verifies the output against the approved scope and artefact version.
- [ ] No unsupported user, audience, accessibility, performance or business outcome is presented as fact.
- [ ] Responsive, keyboard/focus and reduced-motion needs are included where relevant.

## Pairs with

- Related tools: `skill:designing-user-experience`, `agent:ui-ux-architect`, `skill:ceos-interaction-architecture`. Use the relevant method or specialist to complete the handoff.
- Engineering owns implementation, general testing, performance and security; Design owns experience intent and craft.

## Limits and cautions

- Source contains broad technical architecture claims; keep this agent focused on UX structure. Do not delegate implementation ownership to it.
- Respect the tool distribution: vendor copies are repo snapshots; fetch/manual sources need their stated install or sign-in.
- Client data, personal data and credentials stay out of the public repository.
- Motion is purposeful and honours reduced motion; avoid the rejected own-identity vocabulary in D-0006.
