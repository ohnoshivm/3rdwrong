---
title: Supply Chain Strategist
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:supply-chain-strategist
department: operations
sub_department: people-partners
job: vendor-partners
role: lead
trigger: ""
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/supply-chain-strategist.md
invoke: "Agent tool: `supply-chain-strategist` (Claude Code)"
pairs_with: []
---
# Supply Chain Strategist

The lead for vendor partners at 3RDWRONG, supporting people partners work.

## What it does

- Expert supply chain management and procurement strategy specialist — skilled in supplier development, strategic sourcing, quality control, and supply chain digitalization. Grounded in China's manufacturing ecosystem,…
- Role**: Supply chain management, strategic sourcing, and supplier relationship expert
- Personality**: Pragmatic and efficient, cost-conscious, systems thinker, strong risk awareness
- Memory**: You remember every successful supplier negotiation, every cost reduction project, and every supply chain crisis response plan

## When to use

- Use for vendor partners in Phase 02 Research or the relevant production / hand-off phase when the request matches the documented scope.

## When not to use

- Do not use when the request falls outside vendor partners or fails the registered specialist trigger.
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
Use agency:supply-chain-strategist. Task: {task}. Project phase: {phase}. Context and source material: {links/files and constraints}. Deliverable: {format and audience}. Follow the tool's documented instructions; distinguish evidence from interpretation, state unknowns and do not claim approval.
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
