---
title: Legal Document Review
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:legal-document-review
department: operations
sub_department: finance-legal
job: legal-contracts
role: lead
trigger: ""
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/legal-document-review.md
invoke: "Agent tool: `legal-document-review` (Claude Code)"
pairs_with: []
---
# Legal Document Review

The lead for legal contracts at 3RDWRONG, supporting finance legal work.

## What it does

- Comprehensive legal document review specialist for contracts, litigation documents, and real estate agreements — summarizing documents, flagging risk clauses, comparing contract versions, and checking compliance…
- The document type and jurisdiction being reviewed
- The client's role in the agreement (buyer/seller, licensor/licensee, landlord/tenant, plaintiff/defendant)
- Risk tolerance level specified by the reviewing attorney

## When to use

- Use for legal contracts in Phase 02 Research or the relevant production / hand-off phase when the request matches the documented scope.

## When not to use

- Do not use when the request falls outside legal contracts or fails the registered specialist trigger.
- Do not use its output as client approval, verified research or professional advice.

## Inputs it needs

- A bounded task brief, relevant context, constraints and expected deliverable.
- Only provide files and information needed for the task.

## How to run it

1. Check the task against the registered job and trigger.
2. Read the source instructions and provide the minimum necessary inputs.
3. Invoke the tool using the name above and request the required artefact.
4. Have a separate reviewer check evidence, accuracy, privacy and fit before hand-off.

```text
Use agency:legal-document-review. Task: {task}. Project phase: {phase}. Context and source material: {links/files and constraints}. Deliverable: {format and audience}. Follow the tool's documented instructions; distinguish evidence from interpretation, state unknowns and do not claim approval.
```

## What good output looks like

- The deliverable addresses the requested task and follows the source-documented workflow.
- Facts, assumptions and unknowns are distinguishable; no capability is implied beyond the source.

## Quality checks

- [ ] The task fits the registry job and any specialist trigger.
- [ ] A reviewer other than the maker checked the output and source evidence.
- [ ] Assumptions and unknowns are visible; unsupported claims are removed.
- [ ] No client-confidential data or personal information entered the public repository.

## Pairs with

- No paired tool is registered for this job in the assigned scope.

## Limits and cautions

- Capabilities are limited to those documented in the source; ask for unknown details rather than assuming them.
- Human review remains responsible for factual accuracy, suitability and approval.
- Distribution: vendor; availability: repo. Confirm setup or sign-in requirements before relying on the tool.
- Outputs need review by a chartered accountant or lawyer before use.
