---
title: gemini-intern
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:gemini-intern
department: operations
sub_department: planning-workflow
job: delivery-discipline
role: specialist
trigger: "Use when the approved work needs this capability: Offload small, command-verifiable tasks (test-gated fixes, small modules, unit tests, quote-checked extraction, one-folder mechanical edits) to free Gemini Flash interns in T3. Not for reviews, creative/copy, browser QA or multi-file work"
kind: skill
availability: both
distribution: manual
source: /Users/hustle/.claude/skills/gemini-intern/SKILL.md
invoke: "gemini-intern skill"
pairs_with: []
---
# gemini-intern

The gemini-intern tool supports 3RDWRONG specialist when Use when the approved work needs this capability: Offload small, command-verifiable tasks (test-gated fixes, small modules, unit tests, quote-checked extraction, one-folder mechanical edits) to free Gemini Flash interns in T3. Not for reviews, creative/copy, browser QA or multi-file work.

## What it does

- One command proves done:** tests, a JSON/quote check, or a diff rule
- Small:** one directory, about 3 files or fewer, under 10 minutes. No reviews, creative/brand/copy, browsers, servers, installs or multi-file refactors
- | 3 | On the completion notification: `bash grade.sh check <dir> -- <cmd>` | `PASS …` or `FAIL …` (+15 lines) |
- Tests first:** the failing test or check you write is the spec. Protect it with `snap`. Don't write a separate long prose spec

## When to use

- Use when the approved work needs this capability: Offload small, command-verifiable tasks (test-gated fixes, small modules, unit tests, quote-checked extraction, one-folder mechanical edits) to free Gemini Flash interns in T3. Not for reviews, creative/copy, browser QA or multi-file work

## When not to use

- When the brief needs a different job than `delivery-discipline`; choose the registered tool for that job.
- Do not treat its output as independent verification when it produced the work.

## Inputs it needs

- The requested outcome, relevant project context, constraints and source material.
- Any criteria, data or decisions specified in the source instructions; otherwise: Not documented.

## How to run it

1. Confirm the source instructions and required access are available.
2. Invoke using the exact tool name above.
3. Give it the brief, context and acceptance criteria; review its evidence and handoff.

```text
Use gemini-intern skill. Job: delivery-discipline. Brief: {project brief}. Context and source materials: {links/files}. Constraints: {constraints}. Return the documented output, cite evidence, and label anything not supported as Not documented.
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
