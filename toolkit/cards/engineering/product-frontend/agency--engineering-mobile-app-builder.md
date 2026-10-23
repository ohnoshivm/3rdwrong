---
title: Mobile App Builder
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:engineering-mobile-app-builder
department: engineering
sub_department: product-frontend
job: ui-implementation
role: specialist
trigger: "Use for tasks involving Specialized mobile application developer with expertise in native iOS/Android development and cross-platform frameworks."
kind: upstream-agent
availability: claude-managed
distribution: vendor
source: .claude/agents/engineering-mobile-app-builder.md
invoke: "Claude Code agent: Mobile App Builder Agent"
pairs_with: [agency:engineering-frontend-developer, skill:mobile-native]
---
# Mobile App Builder

Mobile App Builder is the studio's specialist for `ui-implementation`; use it when the registry trigger below applies.

## What it does

- Builds native iOS/Android and cross-platform applications
- Implements mobile architecture, UI and platform integrations
- Works within mobile app delivery and release context

## When to use

- Use for tasks involving Specialized mobile application developer with expertise in native iOS/Android development and cross-platform frameworks.
- When the requested deliverable is native/cross-platform mobile
- Phase 02 Architecture through implementation and release planning

## When not to use

- For mobile browser behaviour use `skill:mobile-native`
- For web UI use `agency:engineering-frontend-developer`
- Do not use to approve its own work; assign a separate checker.

## Inputs it needs

- Target platforms and native capabilities
- Design, framework, device and release constraints
- Existing code and platform test environment

## How to run it

1. Confirm the task matches the job and, for a specialist, the registry trigger.
2. Invoke `Claude Code agent: Mobile App Builder Agent` and provide the approved brief, artefacts, constraints and source context.
3. Ask for the documented deliverable; inspect assumptions and verification before handoff.

```text
Use `agency:engineering-mobile-app-builder` for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform/version: {links and versions}. Constraints: {accessibility, performance, delivery}. Work within the documented scope and registry trigger. Label evidence Documented, Interpretation, Hypothesis or Unknown; return the requested artefact, assumptions, limitations, verification actually performed and a concrete next action.
```

## What good output looks like

- Platform-aware app plan and implementation
- Platform-specific verification and gaps

## Quality checks

- [ ] Work matches the approved brief and the maker is not its checker.
- [ ] Claims are supported by source or supplied evidence; label uncertainty explicitly.
- [ ] Responsive behaviour, accessibility and performance are checked where they apply.
- [ ] Verification lists only commands, tests or browser checks actually run.

## Pairs with

- `agency:engineering-frontend-developer` — coordinate the artefacts and handoff at the relevant stage.
- `skill:mobile-native` — coordinate the artefacts and handoff at the relevant stage.

## Limits and cautions

- Do not infer iOS/Android parity
- keep credentials and client data out of public repo
- Keep client data and credentials out of the public repository (D-0021); check licence and distribution prerequisites, including installation or sign-in when required.
