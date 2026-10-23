---
title: Account Strategist
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:sales-account-strategist
department: production
sub_department: handover-retention
job: client-success
role: specialist
trigger: "Use for production/handover-retention/client-success when the brief specifically requires: Expert post-sale account strategist specializing in land-and-expand execution, stakeholder mapping, QBR facilitation, and net revenue retention ."
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/sales-account-strategist.md
invoke: "Agent tool: Account Strategist"
pairs_with: [agency:customer-success-manager, skill:writing-release-notes]
---
# Account Strategist

The 3RDWRONG tool for {job.replace("-"," ")} — specialist when Use for production/handover-retention/client-success when the brief specifically requires: Expert post-sale account strategist specializing in land-and-expand execution, stakeholder mapping, QBR facilitation, and net revenue retention .

## What it does

- Supports post-sale account strategy, stakeholder mapping and QBR preparation.
- Frames retention and expansion opportunities from supplied account evidence.
- A new expansion deal remains a Sales responsibility.

## When to use

- Use for production/handover-retention/client-success when the brief specifically requires: Expert post-sale account strategist specializing in land-and-expand execution, stakeholder mapping, QBR facilitation, and net revenue retention .

## When not to use

- Not a substitute for approved strategy, human decisions or independent review. Use the appropriate job lead before activating a specialist.

## Inputs it needs

- Approved brief and decision to support.
- Source material, scope and constraints relevant to the tool; identify gaps rather than fill them.

## How to run it

1. Invoke with `Agent tool: Account Strategist`; confirm availability and required setup in the host.
2. Supply the inputs above and request the source-defined workflow and output.
3. Review evidence, assumptions and limitations with a separate person or agent.
4. File only anonymised, rights-cleared material in the public studio repository.

```text
Use Agent tool: Account Strategist. Job: client-success. Project: {project}. Decision: {decision}. Inputs: {source links or files}. Constraints: {scope, timing, access}. Follow the tool’s documented workflow only. Mark claims Documented, Interpretation, Hypothesis or Unknown; identify gaps. Return the source-defined output and a concise next step. Do not invent findings or capabilities.
```

## What good output looks like

- A usable client success deliverable that follows the tool source and answers the stated decision.
- Inputs, evidence, assumptions and unresolved questions remain traceable.

## Quality checks

- [ ] A reviewer other than the maker checks the deliverable.
- [ ] Claims and unknowns are traceable to supplied sources.
- [ ] Scope and human decision ownership are clear.

## Pairs with

- Upstream: `agency:customer-success-manager` — supplies or frames relevant context.
- Downstream/check: `skill:writing-release-notes` — develops or independently checks the hand-off.

## Limits and cautions

- Source limitations: do not claim capabilities, outcomes or invocation details absent from the tool file.
- Keep client data and personal information outside the public repository.
- This tool cannot approve its own work; use a separate checker and retain human decisions.
