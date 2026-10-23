---
title: React View Transitions
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:vercel-react-view-transitions
department: engineering
sub_department: product-frontend
job: frontend-architecture
role: specialist
trigger: "Use for tasks involving Guide for implementing smooth, native-feeling animations using React's View Transition API (`<ViewTransition>` component, `addTransitionType`, and CSS view transition pseudo-elements)."
kind: skill
availability: both
distribution: manual
source: /Users/hustle/.config/opencode/skills/vercel-react-view-transitions/SKILL.md
invoke: "vercel-react-view-transitions skill"
pairs_with: [agent:frontend-architect, skill:building-accessible-interfaces]
---
# React View Transitions

React View Transitions is the studio's specialist for `frontend-architecture`; use it when the registry trigger below applies.

## What it does

- Implements browser-native React View Transition patterns
- Uses shared elements, suspense, lists, state and route patterns
- Chooses transitions to express continuity or hierarchy and documents support

## When to use

- Use for tasks involving Guide for implementing smooth, native-feeling animations using React's View Transition API (`<ViewTransition>` component, `addTransitionType`, and CSS view transition pseudo-elements).
- When approved React interface needs meaningful state/route transitions
- Phase 05

## When not to use

- For other motion systems use project standard
- No animation without clear purpose
- Do not use to approve its own work; assign a separate checker.

## Inputs it needs

- React/Next version and state/routes
- Transition intent and target browsers
- Reduced-motion/fallback needs

## How to run it

1. Confirm the task matches the job and, for a specialist, the registry trigger.
2. Invoke `vercel-react-view-transitions skill` and provide the approved brief, artefacts, constraints and source context.
3. Ask for the documented deliverable; inspect assumptions and verification before handoff.

```text
Use `skill:vercel-react-view-transitions` for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform/version: {links and versions}. Constraints: {accessibility, performance, delivery}. Work within the documented scope and registry trigger. Label evidence Documented, Interpretation, Hypothesis or Unknown; return the requested artefact, assumptions, limitations, verification actually performed and a concrete next action.
```

## What good output looks like

- Transition communicates relationship
- Unsupported browsers degrade
- reduced motion honoured

## Quality checks

- [ ] Work matches the approved brief and the maker is not its checker.
- [ ] Claims are supported by source or supplied evidence; label uncertainty explicitly.
- [ ] Responsive behaviour, accessibility and performance are checked where they apply.
- [ ] Verification lists only commands, tests or browser checks actually run.

## Pairs with

- `agent:frontend-architect` — coordinate the artefacts and handoff at the relevant stage.
- `skill:building-accessible-interfaces` — coordinate the artefacts and handoff at the relevant stage.

## Limits and cautions

- Without Next source says React canary needed
- check versions and do not stack engines
- Keep client data and credentials out of the public repository (D-0021); check licence and distribution prerequisites, including installation or sign-in when required.
