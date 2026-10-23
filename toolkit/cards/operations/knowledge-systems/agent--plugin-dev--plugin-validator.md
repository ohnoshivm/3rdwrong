---
title: Plugin Validator
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agent:plugin-dev:plugin-validator
department: operations
sub_department: knowledge-systems
job: skill-authoring
role: specialist
trigger: "Use when the approved work needs this capability: Use this agent when the user asks to \"validate my plugin\", \"check plugin structure\", \"verify plugin is correct\", \"validate plugin.json\", \"check plugin files\", or mentions plugin validation. Also trigger proactively after user creates or modifies plugin components. Examples: <example> Context: User finished creating a new plugin user: \"I've created my first plugin with commands and hooks\" assistant: \"Great! Let me validate the plugin structure.\" <commentary> Plugin created, proactively validate to catch issues early. </commentary> assistant: \"I'll use the plugin-validator agent to check the plugin.\" </example> <example> Context: User explicitly requests validation user: \"Validate my plugin before I publish it\" assistant: \"I'll use the plugin-validator agent to perform comprehensive validation.\" <commentary> Explicit validation request triggers the agent. </commentary> </example> <example> Context: User modified plugin.json user: \"I've updated the plugin manifest\" assistant: \"Let me validate the changes.\" <commentary> Manifest modified, validate to ensure correctness. </commentary> assistant: \"I'll use the plugin-validator agent to check the manifest.\" </example>"
kind: agent
availability: claude
distribution: vendor
source: toolkit/vendor/plugin-claude-plugins-official-plugin-dev-marketplace/agents/plugin-validator.md
invoke: "Agent tool: `plugin-validator` (Claude Code)"
pairs_with: [skill-creator:skill-creator]
---
# Plugin Validator

A specialist for skill authoring at 3RDWRONG, called when Use this agent when the user asks to "validate my plugin", "check plugin structure", "verify plugin is correct", "validate plugin.json", "check plugin files", or mentions plugin validation. Also trigger proactively after user creates or modifies plugin components. Examples: <example> Context: User finished creating a new plugin user: "I've created my first plugin with commands and hooks" assistant: "Great! Let me validate the plugin structure." <commentary> Plugin created, proactively validate to catch issues early. </commentary> assistant: "I'll use the plugin-validator agent to check the plugin." </example> <example> Context: User explicitly requests validation user: "Validate my plugin before I publish it" assistant: "I'll use the plugin-validator agent to perform comprehensive validation." <commentary> Explicit validation request triggers the agent. </commentary> </example> <example> Context: User modified plugin.json user: "I've updated the plugin manifest" assistant: "Let me validate the changes." <commentary> Manifest modified, validate to ensure correctness. </commentary> assistant: "I'll use the plugin-validator agent to check the manifest." </example>.

## What it does

- Check for `.claude-plugin/plugin.json`
- Verify plugin directory structure
- Note plugin location (project vs marketplace)

## When to use

- Use when the approved work needs this capability: Use this agent when the user asks to "validate my plugin", "check plugin structure", "verify plugin is correct", "validate plugin.json", "check plugin files", or mentions plugin validation. Also trigger proactively after user creates or modifies plugin components. Examples: <example> Context: User finished creating a new plugin user: "I've created my first plugin with commands and hooks" assistant: "Great! Let me validate the plugin structure." <commentary> Plugin created, proactively validate to catch issues early. </commentary> assistant: "I'll use the plugin-validator agent to check the plugin." </example> <example> Context: User explicitly requests validation user: "Validate my plugin before I publish it" assistant: "I'll use the plugin-validator agent to perform comprehensive validation." <commentary> Explicit validation request triggers the agent. </commentary> </example> <example> Context: User modified plugin.json user: "I've updated the plugin manifest" assistant: "Let me validate the changes." <commentary> Manifest modified, validate to ensure correctness. </commentary> assistant: "I'll use the plugin-validator agent to check the manifest." </example>
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
Use agent:plugin-dev:plugin-validator. Task: {task}. Project phase: {phase}. Context and source material: {links/files and constraints}. Deliverable: {format and audience}. Follow the tool's documented instructions; distinguish evidence from interpretation, state unknowns and do not claim approval.
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
