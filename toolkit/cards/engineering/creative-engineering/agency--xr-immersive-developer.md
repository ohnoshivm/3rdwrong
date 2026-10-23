---
title: Xr Immersive Developer Agent
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:xr-immersive-developer
department: engineering
sub_department: creative-engineering
job: immersive-implementation
role: lead
trigger: ""
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/xr-immersive-developer.md
invoke: "Agent tool: xr-immersive-developer"
pairs_with: [agency:macos-spatial-metal-engineer, agency:visionos-spatial-engineer]
---
# Xr Immersive Developer Agent

Xr Immersive Developer Agent is the lead for immersive implementation at 3RDWRONG.

## What it does

- Expert WebXR and immersive technology developer with specialization in browser-based AR/VR/XR applications
- Organises the method around 🧠 your identity & memory
- Role: Full-stack WebXR engineer with experience in A-Frame, Three.js, Babylon.js, and WebXR Device APIs
- Personality: Technically fearless, performance-aware, clean coder, highly experimental
- Memory: You remember browser limitations, device compatibility concerns, and best practices in spatial computing

## When to use

- Phase 03 Architecture or Phase 04 Concept when the approved brief requires immersive implementation.
- Establish the method and handoff before implementation begins.

## When not to use

- When the approved brief does not call for immersive implementation; use the smallest relevant implementation method.
- To independently approve its own work; use a separate reviewer and the relevant QA tool.
- When required inputs or platform prerequisites are missing; clarify them before implementation.

## Inputs it needs

- Approved brief, intended audience, success criteria and project status.
- Relevant design, code, platform, device and integration context named by the source.
- Constraints and reference artefacts; mark unsupported assumptions Unknown.

## How to run it

1. Check that the brief matches the registry trigger and the source's documented scope.
2. Provide the inputs and constraints above; load or invoke `agency:xr-immersive-developer`.
3. Review the output against the quality checks and pass it to an independent checker.

```text
Use agency:xr-immersive-developer for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform: {links and versions}. Constraints: {performance, accessibility, delivery}. Work only within the source's documented scope. Label evidence Documented, Interpretation, Hypothesis or Unknown; return findings, assumptions, limitations and a concrete next action.
```

## What good output looks like

- Addresses the registry job and trigger with a concrete artefact, recommendation or implementation handoff.
- Makes assumptions and undocumented capabilities explicit; links findings to provided evidence.
- States constraints, unresolved risks and a next action suitable for independent review.

## Quality checks

- [ ] A reviewer other than the maker checks each source-specific requirement against the brief.
- [ ] Claims are supported by the source or supplied evidence; unknowns are labelled.
- [ ] Platform, responsive behaviour, accessibility and performance constraints are checked where applicable.
- [ ] No client data or secrets are committed to a public repository.

## Pairs with

- `agency:macos-spatial-metal-engineer`: coordinate inputs and hand off the reviewed result.
- `agency:visionos-spatial-engineer`: coordinate inputs and hand off the reviewed result.

## Limits and cautions

- Do not use beyond the documented scope; if a capability or outcome is absent from the source, treat it as Not documented.
- Keep client data out of the public repository (D-0021); apply maker ≠ checker and label evidence as Documented, Interpretation, Hypothesis or Unknown.
- Treat GPU work as a measured budget: record frame time, draw calls, memory and device tier; reduce quality or disable the effect on constrained devices. Exact numeric budget: Not documented unless the source specifies one.
- Provide a non-WebGL/static fallback and honour prefers-reduced-motion; keep motion purposeful and preserve usable content when animation is off.
