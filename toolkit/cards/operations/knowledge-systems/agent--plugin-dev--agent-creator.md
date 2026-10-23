---
title: Agent Creator
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agent:plugin-dev:agent-creator
department: operations
sub_department: knowledge-systems
job: skill-authoring
role: specialist
trigger: "Use when the approved work needs this capability: Use this agent when the user asks to \"create an agent\", \"generate an agent\", \"build a new agent\", \"make me an agent that...\", or describes agent functionality they need. Trigger when user wants to create autonomous agents for plugins. Examples: <example> Context: User wants to create a code review agent user: \"Create an agent that reviews code for quality issues\" assistant: \"I'll use the agent-creator agent to generate the agent configuration.\" <commentary> User requesting new agent creation, trigger agent-creator to generate it. </commentary> </example> <example> Context: User describes needed functionality user: \"I need an agent that generates unit tests for my code\" assistant: \"I'll use the agent-creator agent to create a test generation agent.\" <commentary> User describes agent need, trigger agent-creator to build it. </commentary> </example> <example> Context: User wants to add agent to plugin user: \"Add an agent to my plugin that validates configurations\" assistant: \"I'll use the agent-creator agent to generate a configuration validator agent.\" <commentary> Plugin development with agent addition, trigger agent-creator. </commentary> </example>"
kind: agent
availability: claude
distribution: vendor
source: toolkit/vendor/plugin-claude-plugins-official-plugin-dev-marketplace/agents/agent-creator.md
invoke: "Agent tool: `agent-creator` (Claude Code)"
pairs_with: [skill-creator:skill-creator]
---
# Agent Creator

A specialist for skill authoring at 3RDWRONG, called when Use this agent when the user asks to "create an agent", "generate an agent", "build a new agent", "make me an agent that...", or describes agent functionality they need. Trigger when user wants to create autonomous agents for plugins. Examples: <example> Context: User wants to create a code review agent user: "Create an agent that reviews code for quality issues" assistant: "I'll use the agent-creator agent to generate the agent configuration." <commentary> User requesting new agent creation, trigger agent-creator to generate it. </commentary> </example> <example> Context: User describes needed functionality user: "I need an agent that generates unit tests for my code" assistant: "I'll use the agent-creator agent to create a test generation agent." <commentary> User describes agent need, trigger agent-creator to build it. </commentary> </example> <example> Context: User wants to add agent to plugin user: "Add an agent to my plugin that validates configurations" assistant: "I'll use the agent-creator agent to generate a configuration validator agent." <commentary> Plugin development with agent addition, trigger agent-creator. </commentary> </example>.

## What it does

- Establishes clear behavioral boundaries and operational parameters
- Provides specific methodologies and best practices for task execution
- Anticipates edge cases and provides guidance for handling them

## When to use

- Use when the approved work needs this capability: Use this agent when the user asks to "create an agent", "generate an agent", "build a new agent", "make me an agent that...", or describes agent functionality they need. Trigger when user wants to create autonomous agents for plugins. Examples: <example> Context: User wants to create a code review agent user: "Create an agent that reviews code for quality issues" assistant: "I'll use the agent-creator agent to generate the agent configuration." <commentary> User requesting new agent creation, trigger agent-creator to generate it. </commentary> </example> <example> Context: User describes needed functionality user: "I need an agent that generates unit tests for my code" assistant: "I'll use the agent-creator agent to create a test generation agent." <commentary> User describes agent need, trigger agent-creator to build it. </commentary> </example> <example> Context: User wants to add agent to plugin user: "Add an agent to my plugin that validates configurations" assistant: "I'll use the agent-creator agent to generate a configuration validator agent." <commentary> Plugin development with agent addition, trigger agent-creator. </commentary> </example>
- In a 3RDWRONG project, use during the relevant skill authoring task and pass its output to the project owner for review.

## When not to use

- Do not use when the request falls outside skill authoring or fails the registered specialist trigger.
- Do not use its output as client approval, verified research or professional advice.
- For the paired skill-creator:skill-creator work, use that tool and hand off this artefact.

## Inputs it needs

- A bounded task brief, relevant context, constraints and expected deliverable.
- Only provide files and information needed for the task.

## How to run it

1. Check the task against the registered job and trigger.
2. Read the source instructions and provide the minimum necessary inputs.
3. Invoke the tool using the name above and request the required artefact.
4. Have a separate reviewer check evidence, accuracy, privacy and fit before hand-off.

```text
Use agent:plugin-dev:agent-creator. Task: {task}. Project phase: {phase}. Context and source material: {links/files and constraints}. Deliverable: {format and audience}. Follow the tool's documented instructions; distinguish evidence from interpretation, state unknowns and do not claim approval.
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

- `skill-creator:skill-creator` — coordinate the hand-off for the same job; pass the artefact and constraints.

## Limits and cautions

- Capabilities are limited to those documented in the source; ask for unknown details rather than assuming them.
- Human review remains responsible for factual accuracy, suitability and approval.
- Distribution: vendor; availability: claude. Confirm setup or sign-in requirements before relying on the tool.
