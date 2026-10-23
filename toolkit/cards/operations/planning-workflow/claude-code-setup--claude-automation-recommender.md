---
title: claude-automation-recommender
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: claude-code-setup:claude-automation-recommender
department: operations
sub_department: planning-workflow
job: automation-operations
role: lead
trigger: ""
kind: plugin-skill
availability: claude
distribution: vendor
source: toolkit/vendor/plugin-claude-plugins-official-claude-code-setup-marketplace/skills/claude-automation-recommender
invoke: "claude-automation-recommender skill"
pairs_with: []
---
# claude-automation-recommender

The claude-automation-recommender tool supports 3RDWRONG lead for automation-operations.

## What it does

- Analyze codebase patterns to recommend tailored Claude Code automations across all extensibility options
- Recommend 1-2 of each type**: Don't overwhelm - surface the top 1-2 most valuable automations per category
- If user asks for a specific type**: Focus only on that type and provide more options (3-5 recommendations)
- Go beyond the reference lists**: The reference files contain common patterns, but use web search to find recommendations specific to the codebase's tools, frameworks, and libraries

## When to use

- Use in studio operations when a automation operations brief needs an end-to-end owner; choose the specific phase based on the source instructions.

## When not to use

- When the brief needs a different job than `automation-operations`; choose the registered tool for that job.
- Do not treat its output as independent verification when it produced the work.

## Inputs it needs

- The requested outcome, relevant project context, constraints and source material.
- Any criteria, data or decisions specified in the source instructions; otherwise: Not documented.

## How to run it

1. Confirm the source instructions and required access are available.
2. Invoke using the exact tool name above.
3. Give it the brief, context and acceptance criteria; review its evidence and handoff.

```text
Use claude-automation-recommender skill. Job: automation-operations. Brief: {project brief}. Context and source materials: {links/files}. Constraints: {constraints}. Return the documented output, cite evidence, and label anything not supported as Not documented.
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
