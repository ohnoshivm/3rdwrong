---
title: Senior Project Manager
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:project-manager-senior
department: production
sub_department: producing-pm
job: project-planning
role: specialist
trigger: "Use when the approved work needs this capability: Converts specs to tasks and remembers previous projects. Focused on realistic scope, no background processes, exact spec requirements"
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/project-manager-senior.md
invoke: "Agent tool: Senior Project Manager"
pairs_with: [agency:project-management-project-shepherd, openai-templates:artifact-template-project-tracker]
---
# Senior Project Manager

The 3RDWRONG tool for {job.replace("-"," ")} — specialist when Use when the approved work needs this capability: Converts specs to tasks and remembers previous projects. Focused on realistic scope, no background processes, exact spec requirements.

## What it does

- Converts specifications into tasks and supports realistic scope.
- Uses prior project context when it is supplied.
- Runs without background processes, as specified in its source.

## When to use

- Use when the approved work needs this capability: Converts specs to tasks and remembers previous projects. Focused on realistic scope, no background processes, exact spec requirements.

## When not to use

- Not a substitute for approved strategy, human decisions or independent review. Use the appropriate job lead before activating a specialist.

## Inputs it needs

- Approved brief and decision to support.
- Source material, scope and constraints relevant to the tool; identify gaps rather than fill them.

## How to run it

1. Invoke with `Agent tool: Senior Project Manager`; confirm availability and required setup in the host.
2. Supply the inputs above and request the source-defined workflow and output.
3. Review evidence, assumptions and limitations with a separate person or agent.
4. File only anonymised, rights-cleared material in the public studio repository.

```text
Use Agent tool: Senior Project Manager. Job: project-planning. Project: {project}. Decision: {decision}. Inputs: {source links or files}. Constraints: {scope, timing, access}. Follow the tool’s documented workflow only. Mark claims Documented, Interpretation, Hypothesis or Unknown; identify gaps. Return the source-defined output and a concise next step. Do not invent findings or capabilities.
```

## What good output looks like

- A usable project planning deliverable that follows the tool source and answers the stated decision.
- Inputs, evidence, assumptions and unresolved questions remain traceable.

## Quality checks

- [ ] A reviewer other than the maker checks the deliverable.
- [ ] Claims and unknowns are traceable to supplied sources.
- [ ] Scope and human decision ownership are clear.

## Pairs with

- Upstream: `agency:project-management-project-shepherd` — supplies or frames relevant context.
- Downstream/check: `openai-templates:artifact-template-project-tracker` — develops or independently checks the hand-off.

## Limits and cautions

- Source limitations: do not claim capabilities, outcomes or invocation details absent from the tool file.
- Keep client data and personal information outside the public repository.
- This tool cannot approve its own work; use a separate checker and retain human decisions.
