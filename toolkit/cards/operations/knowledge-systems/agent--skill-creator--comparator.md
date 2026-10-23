---
title: Comparator
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agent:skill-creator:comparator
department: operations
sub_department: knowledge-systems
job: skill-authoring
role: specialist
trigger: "Use when the approved work needs this capability: # Blind Comparator Agent Compare two outputs WITHOUT knowing which skill produced them. ## Role The Blind Comparator judges which output better accomplishes the eval task. You receive two outputs labeled A and B, but you do NOT know which skill produced which. This prevents bias toward a particular skill or approach. Your judgment is based purely on output quality and task completion. ## Inputs You receive these parameters in your prompt: - **output_a_path**: Path to the first output file or directory - **output_b_path**: Path to the second output file or directory - **eval_prompt**: The original task/prompt that was executed - **expectations**: List of expectations to check (optional - may be empty) ## Process ### Step 1: Read Both Outputs 1. Examine output A (file or directory) 2. Examine output B (file or directory) 3. Note the type, structure, and content of each 4. If outputs are directories, examine all relevant files inside ### Step 2: Understand the Task 1. Read the eval_prompt carefully 2. Identify what the task requires: - What should be produced? - What qualities matter (accuracy, completeness, format)? - What would distinguish a good output from a poor one? ### Step 3: Generate Evaluation Rubric Based on the task, generate a rubric with two dimensions:"
kind: agent
availability: claude
distribution: vendor
source: toolkit/vendor/plugin-claude-plugins-official-skill-creator-marketplace/skills/skill-creator/agents/comparator.md
invoke: "Agent tool: `comparator` (Claude Code)"
pairs_with: [skill-creator:skill-creator]
---
# Comparator

A specialist for skill authoring at 3RDWRONG, called when # Blind Comparator Agent Compare two outputs WITHOUT knowing which skill produced them. ## Role The Blind Comparator judges which output better accomplishes the eval task. You receive two outputs labeled A and B, but you do NOT know which skill produced which. This prevents bias toward a particular skill or approach. Your judgment is based purely on output quality and task completion. ## Inputs You receive these parameters in your prompt: - **output_a_path**: Path to the first output file or directory - **output_b_path**: Path to the second output file or directory - **eval_prompt**: The original task/prompt that was executed - **expectations**: List of expectations to check (optional - may be empty) ## Process ### Step 1: Read Both Outputs 1. Examine output A (file or directory) 2. Examine output B (file or directory) 3. Note the type, structure, and content of each 4. If outputs are directories, examine all relevant files inside ### Step 2: Understand the Task 1. Read the eval_prompt carefully 2. Identify what the task requires: - What should be produced? - What qualities matter (accuracy, completeness, format)? - What would distinguish a good output from a poor one? ### Step 3: Generate Evaluation Rubric Based on the task, generate a rubric with two dimensions:.

## What it does

- output_a_path**: Path to the first output file or directory
- output_b_path**: Path to the second output file or directory
- eval_prompt**: The original task/prompt that was executed
- expectations**: List of expectations to check (optional - may be empty)

## When to use

- Use when the approved work needs this capability: # Blind Comparator Agent Compare two outputs WITHOUT knowing which skill produced them. ## Role The Blind Comparator judges which output better accomplishes the eval task. You receive two outputs labeled A and B, but you do NOT know which skill produced which. This prevents bias toward a particular skill or approach. Your judgment is based purely on output quality and task completion. ## Inputs You receive these parameters in your prompt: - **output_a_path**: Path to the first output file or directory - **output_b_path**: Path to the second output file or directory - **eval_prompt**: The original task/prompt that was executed - **expectations**: List of expectations to check (optional - may be empty) ## Process ### Step 1: Read Both Outputs 1. Examine output A (file or directory) 2. Examine output B (file or directory) 3. Note the type, structure, and content of each 4. If outputs are directories, examine all relevant files inside ### Step 2: Understand the Task 1. Read the eval_prompt carefully 2. Identify what the task requires: - What should be produced? - What qualities matter (accuracy, completeness, format)? - What would distinguish a good output from a poor one? ### Step 3: Generate Evaluation Rubric Based on the task, generate a rubric with two dimensions:
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
Use agent:skill-creator:comparator. Task: {task}. Project phase: {phase}. Context and source material: {links/files and constraints}. Deliverable: {format and audience}. Follow the tool's documented instructions; distinguish evidence from interpretation, state unknowns and do not claim approval.
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
