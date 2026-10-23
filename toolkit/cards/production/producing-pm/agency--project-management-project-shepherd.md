---
title: Project Shepherd
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:project-management-project-shepherd
department: production
sub_department: producing-pm
job: resource-coordination
role: lead
trigger: ""
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/project-management-project-shepherd.md
invoke: "Agent tool: Project Shepherd"
pairs_with: [openai-templates:artifact-template-project-tracker]
---
# Project Shepherd

The 3RDWRONG tool for {job.replace("-"," ")} — lead.

## What it does

- Coordinates scoped work across people, timelines, risks and communications.
- Keeps work moving against approved scope and dependencies.
- Surfaces delivery risks for a human decision.

## When to use

- At approved resource coordination hand-off, before the studio commits or ships the work.
- When the project record needs a consistent production method.

## When not to use

- Not a substitute for approved strategy, human decisions or independent review. Use the appropriate job lead before activating a specialist.

## Inputs it needs

- Approved brief and decision to support.
- Source material, scope and constraints relevant to the tool; identify gaps rather than fill them.

## How to run it

1. Invoke with `Agent tool: Project Shepherd`; confirm availability and required setup in the host.
2. Supply the inputs above and request the source-defined workflow and output.
3. Review evidence, assumptions and limitations with a separate person or agent.
4. File only anonymised, rights-cleared material in the public studio repository.

```text
Use Agent tool: Project Shepherd. Job: resource-coordination. Project: {project}. Decision: {decision}. Inputs: {source links or files}. Constraints: {scope, timing, access}. Follow the tool’s documented workflow only. Mark claims Documented, Interpretation, Hypothesis or Unknown; identify gaps. Return the source-defined output and a concise next step. Do not invent findings or capabilities.
```

## What good output looks like

- A usable resource coordination deliverable that follows the tool source and answers the stated decision.
- Inputs, evidence, assumptions and unresolved questions remain traceable.

## Quality checks

- [ ] A reviewer other than the maker checks the deliverable.
- [ ] Claims and unknowns are traceable to supplied sources.
- [ ] Scope and human decision ownership are clear.

## Pairs with

- Upstream: `openai-templates:artifact-template-project-tracker` — supplies or frames relevant context.

## Limits and cautions

- Source limitations: do not claim capabilities, outcomes or invocation details absent from the tool file.
- Keep client data and personal information outside the public repository.
- This tool cannot approve its own work; use a separate checker and retain human decisions.
