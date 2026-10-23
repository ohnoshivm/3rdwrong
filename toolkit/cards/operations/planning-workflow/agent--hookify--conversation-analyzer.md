---
title: conversation-analyzer
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agent:hookify:conversation-analyzer
department: operations
sub_department: planning-workflow
job: delivery-discipline
role: specialist
trigger: "Use when the approved work needs this capability: Use this agent when analyzing conversation transcripts to find behaviors worth preventing with hooks. Typical triggers include the /hookify command being invoked without arguments, or the user explicitly asking to look back at the current conversation and surface mistakes that should be prevented in the future. See \"When to invoke\" in the agent body for worked scenarios"
kind: agent
availability: claude
distribution: vendor
source: toolkit/vendor/plugin-claude-plugins-official-hookify-marketplace/agents/conversation-analyzer.md
invoke: "Agent tool: conversation-analyzer"
pairs_with: []
---
# conversation-analyzer

The conversation-analyzer tool supports 3RDWRONG specialist when Use when the approved work needs this capability: Use this agent when analyzing conversation transcripts to find behaviors worth preventing with hooks. Typical triggers include the /hookify command being invoked without arguments, or the user explicitly asking to look back at the current conversation and surface mistakes that should be prevented in the future. See "When to invoke" in the agent body for worked scenarios.

## What it does

- You are a conversation analysis specialist that identifies problematic behaviors in Claude Code sessions that could be prevented with hooks
- Read and analyze user messages to find frustration signals
- Identify specific tool usage patterns that caused issues

- ### 2. Identify Tool Usage Patterns

## When to use

- Use when the approved work needs this capability: Use this agent when analyzing conversation transcripts to find behaviors worth preventing with hooks. Typical triggers include the /hookify command being invoked without arguments, or the user explicitly asking to look back at the current conversation and surface mistakes that should be prevented in the future. See "When to invoke" in the agent body for worked scenarios

## When not to use

- When the brief needs a different job than `delivery-discipline`; choose the registered tool for that job.
- Do not treat its output as independent verification when it produced the work.

## Inputs it needs

- The requested outcome, relevant project context, constraints and source material.
- Any criteria, data or decisions specified in the source instructions; otherwise: Not documented.

## How to run it

1. Confirm the source instructions and required access are available.
2. Invoke using the exact tool name above.
3. Give it the brief, context and acceptance criteria; review its evidence and handoff.

```text
Use Agent tool: conversation-analyzer. Job: delivery-discipline. Brief: {project brief}. Context and source materials: {links/files}. Constraints: {constraints}. Return the documented output, cite evidence, and label anything not supported as Not documented.
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
