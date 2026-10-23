---
title: Mobile Native
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:mobile-native
department: engineering
sub_department: product-frontend
job: ui-implementation
role: specialist
trigger: "When adapting a studio-owned web touchpoint for native-feeling mobile browser behavior."
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-emilkowalski-skills-mit/skills/mobile-native
invoke: "mobile-native skill"
pairs_with: [agency:engineering-mobile-app-builder, agency:engineering-frontend-developer]
---
# Mobile Native

Mobile Native is the studio's specialist for `ui-implementation`; use it when the registry trigger below applies.

## What it does

- Guides native-feeling mobile browser adaptation of studio web touchpoints
- Focuses on browser behaviour rather than native app implementation
- Uses approved web experience as basis

## When to use

- When adapting a studio-owned web touchpoint for native-feeling mobile browser behavior.
- When adapting a studio-owned web touchpoint for mobile browser behaviour

## When not to use

- For native apps use `agency:engineering-mobile-app-builder`
- For breakpoints only use frontend lead
- Do not use to approve its own work; assign a separate checker.

## Inputs it needs

- Existing touchpoint and mobile journey
- Devices/browsers and interactions
- Accessibility and responsive constraints

## How to run it

1. Confirm the task matches the job and, for a specialist, the registry trigger.
2. Invoke `mobile-native skill` and provide the approved brief, artefacts, constraints and source context.
3. Ask for the documented deliverable; inspect assumptions and verification before handoff.

```text
Use `skill:mobile-native` for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform/version: {links and versions}. Constraints: {accessibility, performance, delivery}. Work within the documented scope and registry trigger. Label evidence Documented, Interpretation, Hypothesis or Unknown; return the requested artefact, assumptions, limitations, verification actually performed and a concrete next action.
```

## What good output looks like

- Mobile web adaptation with appropriate interaction
- Device and assistive behaviour checked

## Quality checks

- [ ] Work matches the approved brief and the maker is not its checker.
- [ ] Claims are supported by source or supplied evidence; label uncertainty explicitly.
- [ ] Responsive behaviour, accessibility and performance are checked where they apply.
- [ ] Verification lists only commands, tests or browser checks actually run.

## Pairs with

- `agency:engineering-mobile-app-builder` — coordinate the artefacts and handoff at the relevant stage.
- `agency:engineering-frontend-developer` — coordinate the artefacts and handoff at the relevant stage.

## Limits and cautions

- Do not imply native-app capability
- retain approved identity and purposeful motion
- Keep client data and credentials out of the public repository (D-0021); check licence and distribution prerequisites, including installation or sign-in when required.
