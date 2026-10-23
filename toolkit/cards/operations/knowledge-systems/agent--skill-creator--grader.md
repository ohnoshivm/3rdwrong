---
title: Grader
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agent:skill-creator:grader
department: operations
sub_department: knowledge-systems
job: skill-authoring
role: specialist
trigger: "Use when the approved work needs this capability: # Grader Agent Evaluate expectations against an execution transcript and outputs. ## Role The Grader reviews a transcript and output files, then determines whether each expectation passes or fails. Provide clear evidence for each judgment. You have two jobs: grade the outputs, and critique the evals themselves. A passing grade on a weak assertion is worse than useless — it creates false confidence. When you notice an assertion that's trivially satisfied, or an important outcome that no assertion checks, say so. ## Inputs You receive these parameters in your prompt: - **expectations**: List of expectations to evaluate (strings) - **transcript_path**: Path to the execution transcript (markdown file) - **outputs_dir**: Directory containing output files from execution ## Process ### Step 1: Read the Transcript 1. Read the transcript file completely 2. Note the eval prompt, execution steps, and final result 3. Identify any issues or errors documented ### Step 2: Examine Output Files 1. List files in outputs_dir 2. Read/examine each file relevant to the expectations. If outputs aren't plain text, use the inspection tools provided in your prompt — don't rely solely on what the transcript says the executor produced. 3. Note contents, structure, and quality ### Step 3: Evaluate Each Assertion For each expectation: 1. **Search for evidence** in the transcript and outputs 2. **Determine verdict**: - **PASS**: Clear evidence the expectation is true AND the evidence reflects genuine task completion, not just surface-level compliance - **FAIL**: No evidence, or evidence contradicts the expectation, or the evidence is superficial (e.g., correct filename but empty/wrong content)"
kind: agent
availability: claude
distribution: vendor
source: toolkit/vendor/plugin-claude-plugins-official-skill-creator-marketplace/skills/skill-creator/agents/grader.md
invoke: "Agent tool: `grader` (Claude Code)"
pairs_with: [skill-creator:skill-creator]
---
# Grader

A specialist for skill authoring at 3RDWRONG, called when # Grader Agent Evaluate expectations against an execution transcript and outputs. ## Role The Grader reviews a transcript and output files, then determines whether each expectation passes or fails. Provide clear evidence for each judgment. You have two jobs: grade the outputs, and critique the evals themselves. A passing grade on a weak assertion is worse than useless — it creates false confidence. When you notice an assertion that's trivially satisfied, or an important outcome that no assertion checks, say so. ## Inputs You receive these parameters in your prompt: - **expectations**: List of expectations to evaluate (strings) - **transcript_path**: Path to the execution transcript (markdown file) - **outputs_dir**: Directory containing output files from execution ## Process ### Step 1: Read the Transcript 1. Read the transcript file completely 2. Note the eval prompt, execution steps, and final result 3. Identify any issues or errors documented ### Step 2: Examine Output Files 1. List files in outputs_dir 2. Read/examine each file relevant to the expectations. If outputs aren't plain text, use the inspection tools provided in your prompt — don't rely solely on what the transcript says the executor produced. 3. Note contents, structure, and quality ### Step 3: Evaluate Each Assertion For each expectation: 1. **Search for evidence** in the transcript and outputs 2. **Determine verdict**: - **PASS**: Clear evidence the expectation is true AND the evidence reflects genuine task completion, not just surface-level compliance - **FAIL**: No evidence, or evidence contradicts the expectation, or the evidence is superficial (e.g., correct filename but empty/wrong content).

## What it does

- expectations**: List of expectations to evaluate (strings)
- transcript_path**: Path to the execution transcript (markdown file)
- outputs_dir**: Directory containing output files from execution
- PASS**: Clear evidence the expectation is true AND the evidence reflects genuine task completion, not just surface-level compliance

## When to use

- Use when the approved work needs this capability: # Grader Agent Evaluate expectations against an execution transcript and outputs. ## Role The Grader reviews a transcript and output files, then determines whether each expectation passes or fails. Provide clear evidence for each judgment. You have two jobs: grade the outputs, and critique the evals themselves. A passing grade on a weak assertion is worse than useless — it creates false confidence. When you notice an assertion that's trivially satisfied, or an important outcome that no assertion checks, say so. ## Inputs You receive these parameters in your prompt: - **expectations**: List of expectations to evaluate (strings) - **transcript_path**: Path to the execution transcript (markdown file) - **outputs_dir**: Directory containing output files from execution ## Process ### Step 1: Read the Transcript 1. Read the transcript file completely 2. Note the eval prompt, execution steps, and final result 3. Identify any issues or errors documented ### Step 2: Examine Output Files 1. List files in outputs_dir 2. Read/examine each file relevant to the expectations. If outputs aren't plain text, use the inspection tools provided in your prompt — don't rely solely on what the transcript says the executor produced. 3. Note contents, structure, and quality ### Step 3: Evaluate Each Assertion For each expectation: 1. **Search for evidence** in the transcript and outputs 2. **Determine verdict**: - **PASS**: Clear evidence the expectation is true AND the evidence reflects genuine task completion, not just surface-level compliance - **FAIL**: No evidence, or evidence contradicts the expectation, or the evidence is superficial (e.g., correct filename but empty/wrong content)
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
Use agent:skill-creator:grader. Task: {task}. Project phase: {phase}. Context and source material: {links/files and constraints}. Deliverable: {format and audience}. Follow the tool's documented instructions; distinguish evidence from interpretation, state unknowns and do not claim approval.
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
