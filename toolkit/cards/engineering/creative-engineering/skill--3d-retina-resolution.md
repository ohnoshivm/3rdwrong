---
title: 3D Retina Resolution
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:3d-retina-resolution
department: engineering
sub_department: creative-engineering
job: realtime-3d
role: specialist
trigger: "Use for engineering/creative-engineering/realtime-3d when the brief specifically requires: Render a 3D canvas sharply on Retina and HiDPI displays, including explicit 200 percent resolution, synchronized renderer and post-processing sizes, correct pointer coordinates, and measured quality fallbacks ."
kind: skill
availability: claude
distribution: manual
source: /Users/hustle/.claude/skills/3d-retina-resolution/SKILL.md
invoke: "3d-retina-resolution skill"
pairs_with: [agent:3d-webgl-engineer, skill:3d-falling-leaves, skill:3d-high-poly-models]
---
# 3D Retina Resolution

3D Retina Resolution is the specialist when Use for engineering/creative-engineering/realtime-3d when the brief specifically requires: Render a 3D canvas sharply on Retina and HiDPI displays, including explicit 200 percent resolution, synchronized renderer and post-processing sizes, correct pointer coordinates, and measured quality fallbacks . at 3RDWRONG.

## What it does

- Render a 3D canvas sharply on Retina and HiDPI displays, including explicit 200 percent resolution, synchronized renderer and post-processing sizes, correct pointer coordinates, and measured quality fallbacks. Use for blurry WebGL output, 2x rendering, high-resolution previews, and display-density changes
- Organises the method around choose the scale deliberately
- Fixed 200%: effective pixel ratio is 2, independent of device pixel ratio. This is the default when the user explicitly requests 200%
- Automatic Retina, capped at 2×: effective ratio is Math.min(window.devicePixelRatio || 1, 2). This can render at 1× on an ordinary display; label it Auto rather than claiming it always renders at 200%
- Relative to native resolution: multiply native DPR only when the user explicitly wants that meaning. Native 2× multiplied by another 2 becomes 4× per dimension, or sixteen times the CSS pixel count

## When to use

- Use for engineering/creative-engineering/realtime-3d when the brief specifically requires: Render a 3D canvas sharply on Retina and HiDPI displays, including explicit 200 percent resolution, synchronized renderer and post-processing sizes, correct pointer coordinates, and measured quality fallbacks .

## When not to use

- When the approved brief does not call for realtime 3d; use the smallest relevant implementation method.
- To independently approve its own work; use a separate reviewer and the relevant QA tool.
- When required inputs or platform prerequisites are missing; clarify them before implementation.

## Inputs it needs

- Approved brief, intended audience, success criteria and project status.
- Relevant design, code, platform, device and integration context named by the source.
- Constraints and reference artefacts; mark unsupported assumptions Unknown.

## How to run it

1. Check that the brief matches the registry trigger and the source's documented scope.
2. Provide the inputs and constraints above; load or invoke `skill:3d-retina-resolution`.
3. Review the output against the quality checks and pass it to an independent checker.

```text
Use skill:3d-retina-resolution for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform: {links and versions}. Constraints: {performance, accessibility, delivery}. Work only within the source's documented scope. Label evidence Documented, Interpretation, Hypothesis or Unknown; return findings, assumptions, limitations and a concrete next action.
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

- `agent:3d-webgl-engineer`: coordinate inputs and hand off the reviewed result.
- `skill:3d-falling-leaves`: coordinate inputs and hand off the reviewed result.
- `skill:3d-high-poly-models`: coordinate inputs and hand off the reviewed result.

## Limits and cautions

- Distribution is manual; install or sign in as required before use.
- Do not use beyond the documented scope; if a capability or outcome is absent from the source, treat it as Not documented.
- Keep client data out of the public repository (D-0021); apply maker ≠ checker and label evidence as Documented, Interpretation, Hypothesis or Unknown.
- Treat GPU work as a measured budget: record frame time, draw calls, memory and device tier; reduce quality or disable the effect on constrained devices. Exact numeric budget: Not documented unless the source specifies one.
- Provide a non-WebGL/static fallback and honour prefers-reduced-motion; keep motion purposeful and preserve usable content when animation is off.
