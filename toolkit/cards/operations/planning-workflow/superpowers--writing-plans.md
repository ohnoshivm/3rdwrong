---
title: Writing Plans
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: superpowers:writing-plans
department: operations
sub_department: planning-workflow
job: project-planning
role: lead
trigger: ""
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/plugin-account-synced-superpowers-marketplace/skills/writing-plans
invoke: "/writing-plans"
pairs_with: []
---
# Writing Plans

Use when you have a spec or requirements for a multi-step task, before touching code at 3RDWRONG as a specialist when the stated trigger applies.

## What it does

- Use when you have a spec or requirements for a multi-step task, before touching code
- Follows the scope and sequence documented in its source instructions.
- Produces the output described by the source; unsupported capabilities are Not documented.

## When to use

-
- Use at the matching studio moment when the brief, artefacts and decision context are ready.

## When not to use

- When the request falls outside the source description; select a tool whose registry job fits.
- To replace independent review or treat interpretation as client evidence.

## Inputs it needs

- The task brief and relevant source artefacts.
- Constraints, decision owner and output format required by its instructions.

## How to run it

1. Check the skill is available in the active Claude Code or Codex environment.
2. Invoke `/writing-plans` with the task context and relevant artefacts.
3. Check the result against the source instructions and have a separate reviewer check consequential claims.

```text
Use /writing-plans for this 3RDWRONG task: {brief}. Context and artefacts: {links/files}. Constraints: {constraints}. Follow the tool's documented instructions; distinguish evidence from interpretation and mark unknowns.
```

## What good output looks like

- Completes the documented task and follows its output requirements.
- Makes assumptions and missing evidence visible.

## Quality checks

- [ ] Output follows the source instructions and stays within scope.
- [ ] Evidence, interpretation, hypothesis and unknowns are distinguished where relevant.
- [ ] A reviewer other than the maker checks material decisions before sign-off.

## Pairs with

- Registry pairs: Not documented; use when their hand-off fits.

## Limits and cautions

- Documented scope: Use when you have a spec or requirements for a multi-step task, before touching code. Other capabilities are Not documented.
- Distribution is `vendor`; fetch/manual tools may need installation or sign-in.
- Keep client data out of the public repository.
