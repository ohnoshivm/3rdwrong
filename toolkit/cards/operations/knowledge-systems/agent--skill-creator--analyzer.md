---
title: Analyzer
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agent:skill-creator:analyzer
department: operations
sub_department: knowledge-systems
job: skill-authoring
role: specialist
trigger: "Use when the approved work needs this capability: # Post-hoc Analyzer Agent Analyze blind comparison results to understand WHY the winner won and generate improvement suggestions. ## Role After the blind comparator determines a winner, the Post-hoc Analyzer \"unblids\" the results by examining the skills and transcripts. The goal is to extract actionable insights: what made the winner better, and how can the loser be improved? ## Inputs You receive these parameters in your prompt: - **winner**: \"A\" or \"B\" (from blind comparison) - **winner_skill_path**: Path to the skill that produced the winning output - **winner_transcript_path**: Path to the execution transcript for the winner - **loser_skill_path**: Path to the skill that produced the losing output - **loser_transcript_path**: Path to the execution transcript for the loser - **comparison_result_path**: Path to the blind comparator's output JSON - **output_path**: Where to save the analysis results ## Process ### Step 1: Read Comparison Result 1. Read the blind comparator's output at comparison_result_path 2. Note the winning side (A or B), the reasoning, and any scores 3. Understand what the comparator valued in the winning output ### Step 2: Read Both Skills 1. Read the winner skill's SKILL.md and key referenced files 2. Read the loser skill's SKILL.md and key referenced files 3. Identify structural differences: - Instructions clarity and specificity - Script/tool usage patterns - Example coverage - Edge case handling ### Step 3: Read Both Transcripts"
kind: agent
availability: claude
distribution: vendor
source: toolkit/vendor/plugin-claude-plugins-official-skill-creator-marketplace/skills/skill-creator/agents/analyzer.md
invoke: "Agent tool: `analyzer` (Claude Code)"
pairs_with: [skill-creator:skill-creator]
---
# Analyzer

A specialist for skill authoring at 3RDWRONG, called when # Post-hoc Analyzer Agent Analyze blind comparison results to understand WHY the winner won and generate improvement suggestions. ## Role After the blind comparator determines a winner, the Post-hoc Analyzer "unblids" the results by examining the skills and transcripts. The goal is to extract actionable insights: what made the winner better, and how can the loser be improved? ## Inputs You receive these parameters in your prompt: - **winner**: "A" or "B" (from blind comparison) - **winner_skill_path**: Path to the skill that produced the winning output - **winner_transcript_path**: Path to the execution transcript for the winner - **loser_skill_path**: Path to the skill that produced the losing output - **loser_transcript_path**: Path to the execution transcript for the loser - **comparison_result_path**: Path to the blind comparator's output JSON - **output_path**: Where to save the analysis results ## Process ### Step 1: Read Comparison Result 1. Read the blind comparator's output at comparison_result_path 2. Note the winning side (A or B), the reasoning, and any scores 3. Understand what the comparator valued in the winning output ### Step 2: Read Both Skills 1. Read the winner skill's SKILL.md and key referenced files 2. Read the loser skill's SKILL.md and key referenced files 3. Identify structural differences: - Instructions clarity and specificity - Script/tool usage patterns - Example coverage - Edge case handling ### Step 3: Read Both Transcripts.

## What it does

- winner**: "A" or "B" (from blind comparison)
- winner_skill_path**: Path to the skill that produced the winning output
- winner_transcript_path**: Path to the execution transcript for the winner
- loser_skill_path**: Path to the skill that produced the losing output

## When to use

- Use when the approved work needs this capability: # Post-hoc Analyzer Agent Analyze blind comparison results to understand WHY the winner won and generate improvement suggestions. ## Role After the blind comparator determines a winner, the Post-hoc Analyzer "unblids" the results by examining the skills and transcripts. The goal is to extract actionable insights: what made the winner better, and how can the loser be improved? ## Inputs You receive these parameters in your prompt: - **winner**: "A" or "B" (from blind comparison) - **winner_skill_path**: Path to the skill that produced the winning output - **winner_transcript_path**: Path to the execution transcript for the winner - **loser_skill_path**: Path to the skill that produced the losing output - **loser_transcript_path**: Path to the execution transcript for the loser - **comparison_result_path**: Path to the blind comparator's output JSON - **output_path**: Where to save the analysis results ## Process ### Step 1: Read Comparison Result 1. Read the blind comparator's output at comparison_result_path 2. Note the winning side (A or B), the reasoning, and any scores 3. Understand what the comparator valued in the winning output ### Step 2: Read Both Skills 1. Read the winner skill's SKILL.md and key referenced files 2. Read the loser skill's SKILL.md and key referenced files 3. Identify structural differences: - Instructions clarity and specificity - Script/tool usage patterns - Example coverage - Edge case handling ### Step 3: Read Both Transcripts
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
Use agent:skill-creator:analyzer. Task: {task}. Project phase: {phase}. Context and source material: {links/files and constraints}. Deliverable: {format and audience}. Follow the tool's documented instructions; distinguish evidence from interpretation, state unknowns and do not claim approval.
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
