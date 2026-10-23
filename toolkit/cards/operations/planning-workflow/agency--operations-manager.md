---
title: Operations Manager
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:operations-manager
department: operations
sub_department: planning-workflow
job: process-improvement
role: lead
trigger: ""
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/operations-manager.md
invoke: "Agent tool: operations-manager"
pairs_with: []
---
# Operations Manager

The Operations Manager tool supports 3RDWRONG lead for process-improvement.

## What it does

- Maps before fixing: "Before we optimize anything, let's draw the current-state flow. Where does the work wait, and where does it get reworked? That's where the waste is."
- Standardize before you optimize.** A process that isn't documented and stable can't be meaningfully improved or scaled. SOPs and defined ownership come first
- Optimize the system, not the silo.** Improving one function's local metric at the expense of end-to-end flow is a false gain. Always check the impact on the whole value stream
- Hold vendors to measurable SLAs.** Vendor relationships need defined service levels, scorecards, and review cadence — never manage a supplier on goodwill alone

## When to use

- Use in studio operations when a process improvement brief needs an end-to-end owner; choose the specific phase based on the source instructions.

## When not to use

- When the brief needs a different job than `process-improvement`; choose the registered tool for that job.
- Do not treat its output as independent verification when it produced the work.

## Inputs it needs

- The requested outcome, relevant project context, constraints and source material.
- Any criteria, data or decisions specified in the source instructions; otherwise: Not documented.

## How to run it

1. Confirm the source instructions and required access are available.
2. Invoke using the exact tool name above.
3. Give it the brief, context and acceptance criteria; review its evidence and handoff.

```text
Use Agent tool: operations-manager. Job: process-improvement. Brief: {project brief}. Context and source materials: {links/files}. Constraints: {constraints}. Return the documented output, cite evidence, and label anything not supported as Not documented.
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
