---
title: Gstack Ios Fix
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:gstack-ios-fix
department: operations
sub_department: planning-workflow
job: delivery-discipline
role: specialist
trigger: "Use when the approved work needs this capability: Autonomous iOS bug fixer. Takes a bug found by /ios-qa, reads the source, writes the fix, rebuilds, redeploys, and verifies the fix on the real device. Closes the loop: find bug → fix bug → confirm fix — zero human intervention. Captures the pre-bug state snapshot as a regression test fixture, so"
kind: skill
availability: both
distribution: fetch
source: /Users/hustle/.config/opencode/skills/gstack-ios-fix/SKILL.md
invoke: "/gstack-ios-fix"
pairs_with: []
---
# Gstack Ios Fix

Autonomous iOS bug fixer. Takes a bug found by /ios-qa, reads the source, writes the fix, rebuilds, redeploys, and verifies the fix on the real device. Closes the loop: find bug → fix bug → confirm fix — zero human intervention. Captures th at 3RDWRONG as a specialist when the stated trigger applies.

## What it does

- Autonomous iOS bug fixer.
- Takes a bug found by /ios-qa, reads the source, writes the fix, rebuilds, redeploys, and verifies the fix on the real device.
- Closes the loop: find bug → fix bug → confirm fix — zero human intervention.

## When to use

- Use when the approved work needs this capability: Autonomous iOS bug fixer. Takes a bug found by /ios-qa, reads the source, writes the fix, rebuilds, redeploys, and verifies the fix on the real device. Closes the loop: find bug → fix bug → confirm fix — zero human intervention. Captures the pre-bug state snapshot as a regression test fixture, so
- Use in the relevant studio planning or delivery moment, with the brief and required evidence available.

## When not to use

- When the request falls outside its documented capability; choose a tool whose registry job matches the need.
- To treat generated analysis as client evidence or approval; label interpretation and unknowns.

## Inputs it needs

- The request, context and relevant project artefacts.
- Any constraints, decision owner and desired output format required by the tool’s own instructions.

## How to run it

1. Confirm the tool is installed or available in the active agent environment.
2. Invoke `/gstack-ios-fix` in Claude Code or Codex and provide the project context.
3. Review the output against the source instructions; a person other than the maker checks consequential work.

```text
Use /gstack-ios-fix for this 3RDWRONG task: {brief}. Context and source artefacts: {links/files}. Constraints: {constraints}. Return the documented output, separate evidence from interpretation, and mark unknowns rather than guessing.
```

## What good output looks like

- Addresses the stated task and produces the documented output for this tool.
- Makes assumptions and missing evidence visible; does not claim results the inputs cannot support.

## Quality checks

- [ ] The output follows the tool’s own instructions and requested scope.
- [ ] Evidence, interpretation, hypothesis and unknowns are distinguished where relevant.
- [ ] A reviewer other than the maker checks material decisions before client sign-off.

## Pairs with

- Registry pairs: Not documented; use only when their hand-off matches the project need.

## Limits and cautions

- Autonomous iOS bug fixer. Takes a bug found by /ios-qa, reads the source, writes the fix, rebuilds, redeploys, and verifies the fix on the real device. Closes the loop: find bug → fix bug → confirm fix — zero human intervention. Captures the pre-bug state snapshot as a regression test fixture, so th is the documented scope; other capabilities are Not documented.
- Distribution is `fetch`; fetch/manual tools may require installation or sign-in before use.
- Keep client data out of the public repository. Do not present a maker’s output as independent QA.
