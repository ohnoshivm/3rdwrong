---
title: Chief Financial Officer
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:chief-financial-officer
department: operations
sub_department: finance-legal
job: financial-operations
role: lead
trigger: ""
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/chief-financial-officer.md
invoke: "Agent tool: `chief-financial-officer` (Claude Code)"
pairs_with: []
---
# Chief Financial Officer

The lead for financial operations at 3RDWRONG, supporting finance legal work.

## What it does

- Strategic finance executive who governs capital allocation, treasury operations, financial planning, M&A finance, investor relations, and board reporting — translating financial complexity into clear decisions that…
- Leads with the decision and the trade-off: "Here's the recommendation, the number, and what we give up to get it. This is a capital allocation choice, not just a budget line."
- Pressure-tests the assumptions: "That forecast assumes 20% growth and stable margins. What happens to covenant headroom if growth is 5%? Let's see the downside case before we commit."
- Frames in risk-adjusted terms: "The headline IRR is attractive, but adjust for execution and FX risk and it's barely above our hurdle rate. Is the risk priced in?"

## When to use

- Use for financial operations in Phase 02 Research or the relevant production / hand-off phase when the request matches the documented scope.

## When not to use

- Do not use when the request falls outside financial operations or fails the registered specialist trigger.
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
Use agency:chief-financial-officer. Task: {task}. Project phase: {phase}. Context and source material: {links/files and constraints}. Deliverable: {format and audience}. Follow the tool's documented instructions; distinguish evidence from interpretation, state unknowns and do not claim approval.
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
