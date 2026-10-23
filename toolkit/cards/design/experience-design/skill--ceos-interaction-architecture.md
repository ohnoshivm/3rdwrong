---
title: Interaction Architecture
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:ceos-interaction-architecture
department: design
sub_department: experience-design
job: interaction-architecture
role: specialist
trigger: "When the approved scope specifically requires defining navigation, user journeys, states, and input behavior for a website."
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-ohnoshivm-creative-engineering-os-mit/skills/ceos-interaction-architecture
invoke: "ceos-interaction-architecture skill"
pairs_with: [skill:designing-user-experience, agent:ui-ux-architect, design-skills:interaction-design]
---
# Interaction Architecture

The experience-design specialist for `interaction-architecture` is Interaction Architecture (trigger: “When the approved scope specifically requires defining navigation, user journeys, states, and input behavior for a website”), which defines an accessible interaction model for a website, from journeys and navigation through states and input behaviour.

## What it does

- Plans journeys and page actions.
- specifies input parity, keyboard/focus and scroll behaviour.
- uses explicit state machines for complex UI.
- includes verification criteria.

## When to use

- Use when the approved scope specifically requires defining navigation, user journeys, states, and input behavior for a website. Use Phase 04 Architecture before route and interaction implementation.
- When the approved scope specifically requires defining navigation, user journeys, states, and input behavior for a website.

## When not to use

- Use `skill:designing-user-experience` as UX lead or `vectorlab-ux-skills:forms` for form-specific patterns.
- Do not use it to approve its own work; have an independent reviewer check the artefact.

## Inputs it needs

- Approved concept, content inventory, art direction draft, conversion goal, input and accessibility constraints.
- Versioned approved brief/strategy and source links; mark draft material as formative.

## How to run it

1. Confirm the trigger, stage and source material; keep client data in the approved private store.
2. Run it using the invocation above and provide the required inputs.
3. Check the output against the quality checks; hand unresolved decisions to the named human owner.

```text
Use ceos-interaction-architecture skill. Studio phase: {phase}. Project: {project}. Approved goal/strategy: {goal and source}. Scope: {screen, flow or interaction}. Inputs/evidence: {links and versions}. Constraints: {platform, accessibility, motion, privacy}. Produce every key journey has a primary action, all inputs have a path, states and failures are specified and verifiable. Keep documented facts separate from interpretation and hypothesis; list unknowns and the next human decision.
```

## What good output looks like

- An interaction inventory and state model that can be checked across pointer, touch, keyboard and assistive technology.
- Evidence claims are labelled Documented, Interpretation, Hypothesis or Unknown as applicable.
- The output names open questions, owner and next action.

## Quality checks

- [ ] An independent checker verifies the output against the approved scope and artefact version.
- [ ] No unsupported user, audience, accessibility, performance or business outcome is presented as fact.
- [ ] Responsive, keyboard/focus and reduced-motion needs are included where relevant.

## Pairs with

- Related tools: `skill:designing-user-experience`, `agent:ui-ux-architect`, `design-skills:interaction-design`. Use the relevant method or specialist to complete the handoff.
- Engineering owns implementation, general testing, performance and security; Design owns experience intent and craft.

## Limits and cautions

- Source requires keyboard, screen-reader and touch checks. Keep native scrolling operable; motion respects reduced motion; independent engineering QA remains necessary.
- Respect the tool distribution: vendor copies are repo snapshots; fetch/manual sources need their stated install or sign-in.
- Client data, personal data and credentials stay out of the public repository.
- Motion is purposeful and honours reduced motion; avoid the rejected own-identity vocabulary in D-0006.
