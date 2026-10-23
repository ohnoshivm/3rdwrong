---
title: Customer Service
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:customer-service
department: production
sub_department: client-experience
job: client-service
role: lead
trigger: ""
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/customer-service.md
invoke: "Agent tool: Customer Service"
pairs_with: [agency:project-management-project-shepherd, openai-templates:artifact-template-project-tracker]
---
# Customer Service

The 3RDWRONG tool for {job.replace("-"," ")} — lead.

## What it does

- Supports customer service workflows and client communication.
- Use only for the service capability described by its agent instructions.
- Escalate policy decisions and commitments to the responsible human.

## When to use

- At approved client service hand-off, before the studio commits or ships the work.
- When the project record needs a consistent production method.

## When not to use

- Not a substitute for approved strategy, human decisions or independent review. Use the appropriate job lead before activating a specialist.

## Inputs it needs

- Approved brief and decision to support.
- Source material, scope and constraints relevant to the tool; identify gaps rather than fill them.

## How to run it

1. Invoke with `Agent tool: Customer Service`; confirm availability and required setup in the host.
2. Supply the inputs above and request the source-defined workflow and output.
3. Review evidence, assumptions and limitations with a separate person or agent.
4. File only anonymised, rights-cleared material in the public studio repository.

```text
Use Agent tool: Customer Service. Job: client-service. Project: {project}. Decision: {decision}. Inputs: {source links or files}. Constraints: {scope, timing, access}. Follow the tool’s documented workflow only. Mark claims Documented, Interpretation, Hypothesis or Unknown; identify gaps. Return the source-defined output and a concise next step. Do not invent findings or capabilities.
```

## What good output looks like

- A usable client service deliverable that follows the tool source and answers the stated decision.
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
