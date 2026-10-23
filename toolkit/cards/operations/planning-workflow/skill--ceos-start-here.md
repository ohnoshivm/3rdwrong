---
title: ceos-start-here
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:ceos-start-here
department: operations
sub_department: planning-workflow
job: workflow-orchestration
role: specialist
trigger: "Use when the approved work needs this capability: Progressive entry point for the Creative Engineering OS. Explains the toolkit, maps website tasks to a specialist through the deterministic local router, and scales the CEOS workflow to FAST, STANDARD, or FLAGSHIP work. Use first when starting or res"
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-ohnoshivm-creative-engineering-os-mit/skills/ceos-start-here
invoke: "ceos-start-here skill"
pairs_with: []
---
# ceos-start-here

The ceos-start-here tool supports 3RDWRONG specialist when Use when the approved work needs this capability: Progressive entry point for the Creative Engineering OS. Explains the toolkit, maps website tasks to a specialist through the deterministic local router, and scales the CEOS workflow to FAST, STANDARD, or FLAGSHIP work. Use first when starting or res.

## What it does

- | `tooling/` | `visual-audit/capture.mjs` (screens + axe + console), `perf/frame-probe.mjs` | During review |
- Run the local router for one primary recommendation:
- python3 <toolkit>/scripts/ceos-route.py "Create a wireframe for the signup flow" --project
- require an existing React runtime; a framework override cannot bypass the package-metadata check

## When to use

- Use when the approved work needs this capability: Progressive entry point for the Creative Engineering OS. Explains the toolkit, maps website tasks to a specialist through the deterministic local router, and scales the CEOS workflow to FAST, STANDARD, or FLAGSHIP work. Use first when starting or res

## When not to use

- When the brief needs a different job than `workflow-orchestration`; choose the registered tool for that job.
- Do not treat its output as independent verification when it produced the work.

## Inputs it needs

- The requested outcome, relevant project context, constraints and source material.
- Any criteria, data or decisions specified in the source instructions; otherwise: Not documented.

## How to run it

1. Confirm the source instructions and required access are available.
2. Invoke using the exact tool name above.
3. Give it the brief, context and acceptance criteria; review its evidence and handoff.

```text
Use ceos-start-here skill. Job: workflow-orchestration. Brief: {project brief}. Context and source materials: {links/files}. Constraints: {constraints}. Return the documented output, cite evidence, and label anything not supported as Not documented.
```

## What good output looks like

- Addresses the stated outcome and follows the source instructions.
- Separates documented evidence from assumptions and names unresolved inputs.
- Includes a useful next action or handoff where the source calls for one.

## Quality checks

- [ ] A reviewer confirms claims against source evidence.
- [ ] Assumptions and missing inputs are explicit.
- [ ] The result is reviewed by someone other than its maker when it is used to check work.

## Pairs with

- No registry pairings are documented. Handoff: share the brief, output and open questions with the next tool selected for the project.

## Limits and cautions

- Capabilities are limited to those stated in the tool file; details not stated there are Not documented.
- Distribution/access: follow the installed package and access rules.
- Keep client data out of the public repository (D-0021).
- Apply evidence labels: Documented, Interpretation, Hypothesis or Unknown; preserve human review for consequential decisions.
