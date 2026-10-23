---
title: optimize-web-animations
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:optimize-web-animations
department: engineering
sub_department: platform-performance
job: animation-runtime
role: lead
trigger: ""
kind: skill
availability: both
distribution: fetch
source: /Users/hustle/.agents/skills/optimize-web-animations/SKILL.md
invoke: "optimize-web-animations skill"
pairs_with: []
---
# optimize-web-animations

Profile, audit, and optimize frontend page performance with emphasis on animation work, memory-leak risks, long-session slowdowns, CSS animations, canvas/WebGL requestAnimationFrame loops, marquees, skeletons, GSAP/Three/Matter effects, timers, listeners, and observers. Use when the user asks to make animations performant, pause offscreen animations, look for memory leaks, profile pages that slow the computer over time, fix janky scrolling, reduce CPU/GPU use, or repeat the "only play in view" optimization on React/Vite/Next/frontend pages using Codex Browser.

## What it does

- Profile, audit, and optimize frontend page performance with emphasis on animation work, memory-leak risks, long-session slowdowns, CSS animations, canvas/WebGL requestAnimationFrame loops, marquees, skeletons, GSAP/Three/Matter effects, timers, listeners, and observers. Use when the user asks to make animations performant, pause offscreen animations, look for memory leaks, profile pages that slow the computer over time, fix janky scrolling, reduce CPU/GPU use, or repeat the "only play in view" optimization on React/Vite/Next/frontend pages using Codex Browser.
- Read `AGENTS.md` or local instructions.
- Find page components, animation hooks, CSS keyframes, `requestAnimationFrame`, `setInterval`, `setTimeout`, canvas/WebGL/physics components, media elements, GSAP timelines/tweens, and existing visibility utilities.
- Search effect cleanup for event listeners, observers, RAF loops, intervals, timers, external scripts, media streams, WebGL textures/materials/geometries/renderers, and async work that can complete after unmount.

## When to use

- Phase 05 Build, when measured evidence shows a need for animation runtime work.
- Before changing production behaviour, with scope, baseline and decision owner stated.

## When not to use

- When the task is outside `animation-runtime` or its stated trigger; route to the appropriate job lead.
- To approve its own work; use an independent checker.

## Inputs it needs

- The approved scope, relevant repository or system context, and decision requested.
- Baseline evidence, constraints, and acceptance criteria relevant to the task.
- Access and environment details only when required; keep client data outside the public repository.

## How to run it

1. Confirm the brief matches `animation-runtime` and the trigger above.
2. Provide the inputs and ask for findings tied to the supplied evidence.
3. Review the output independently; implement only approved changes and record before/after evidence.

```text
Use optimize-web-animations skill. Task: {specific task}. Context: {repository/system and approved scope}. Evidence available: {baseline, traces, logs, or constraints}. Return documented capabilities and limits, identify unknowns, and give a proposed next action with evidence. Do not claim unmeasured results.
```

## What good output looks like

- Recommendations map to the stated task and cite supplied evidence.
- Unknowns, assumptions and risks are explicit.
- Any performance or reliability claim has a comparable baseline and follow-up measure.

## Quality checks

- [ ] The work matches the registry job and trigger.
- [ ] Claims trace to supplied evidence; unknowns are labelled.
- [ ] An independent reviewer checks the result.

## Pairs with

- Upstream: the relevant project owner.
- Downstream: an independent reviewer and the relevant delivery or QA owner; hand off findings, evidence and unresolved risks.

## Limits and cautions

- The source describes a role or workflow; it does not prove live system access, successful execution or performance outcomes.
- Keep maker and checker separate; label evidence **Documented**, **Interpretation**, **Hypothesis** or **Unknown**.
- Protect client data; do not place confidential or identifying material in this public repository.
