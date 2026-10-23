---
title: Customer Success Manager
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:customer-success-manager
department: production
sub_department: handover-retention
job: client-success
role: lead
trigger: ""
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/customer-success-manager.md
invoke: "Agent tool: Customer Success Manager"
pairs_with: [skill:writing-release-notes]
---
# Customer Success Manager

The 3RDWRONG tool for {job.replace("-"," ")} — lead.

## What it does

- Supports customer-success work including account health and retention.
- Uses supplied account context to structure follow-up and success planning.
- Human owner retains renewal and commercial decisions.

## When to use

- At approved client success hand-off, before the studio commits or ships the work.
- When the project record needs a consistent production method.

## When not to use

- Not a substitute for approved strategy, human decisions or independent review. Use the appropriate job lead before activating a specialist.

## Inputs it needs

- Approved brief and decision to support.
- Source material, scope and constraints relevant to the tool; identify gaps rather than fill them.

## How to run it

1. Invoke with `Agent tool: Customer Success Manager`; confirm availability and required setup in the host.
2. Supply the inputs above and request the source-defined workflow and output.
3. Review evidence, assumptions and limitations with a separate person or agent.
4. File only anonymised, rights-cleared material in the public studio repository.

```text
Use Agent tool: Customer Success Manager. Job: client-success. Project: {project}. Decision: {decision}. Inputs: {source links or files}. Constraints: {scope, timing, access}. Follow the tool’s documented workflow only. Mark claims Documented, Interpretation, Hypothesis or Unknown; identify gaps. Return the source-defined output and a concise next step. Do not invent findings or capabilities.
```

## What good output looks like

- A usable client success deliverable that follows the tool source and answers the stated decision.
- Inputs, evidence, assumptions and unresolved questions remain traceable.

## Quality checks

- [ ] A reviewer other than the maker checks the deliverable.
- [ ] Claims and unknowns are traceable to supplied sources.
- [ ] Scope and human decision ownership are clear.

## Pairs with

- Upstream: `skill:writing-release-notes` — supplies or frames relevant context.

## Limits and cautions

- Source limitations: do not claim capabilities, outcomes or invocation details absent from the tool file.
- Keep client data and personal information outside the public repository.
- This tool cannot approve its own work; use a separate checker and retain human decisions.
