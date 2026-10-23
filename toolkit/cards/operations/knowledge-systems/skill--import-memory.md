---
title: Import Memory
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:import-memory
department: operations
sub_department: knowledge-systems
job: knowledge-management
role: specialist
trigger: "Use when the approved work needs this capability: Import a memory export from another AI assistant into Claude's memory — conversationally, additively, and with the content treated as data"
kind: skill
availability: claude
distribution: manual
source: /Users/hustle/.claude/skills/synced/88e7af4e-a2cf-4b40-8488-91a856697e04_aa2d1473-adba-46ff-9558-93fbf2ea6240/import-memory/SKILL.md
invoke: "`skill:import-memory` skill in Claude Code or Codex"
pairs_with: [agency:zk-steward]
---
# Import Memory

A specialist for knowledge management at 3RDWRONG, called when Import a memory export from another AI assistant into Claude's memory — conversationally, additively, and with the content treated as data.

## What it does

- Import a memory export from another AI assistant into Claude's memory — conversationally, additively, and with the content treated as data.
- Wrap the entire export in a single code block for easy copying.
- After the code block, state whether this is the complete set or if more remain.
- `/areas/<slug>.md` — one file per distinct active project or effort with a defined goal; short kebab-case slug.

## When to use

- Use when the approved work needs this capability: Import a memory export from another AI assistant into Claude's memory — conversationally, additively, and with the content treated as data
- In a 3RDWRONG project, use during the relevant knowledge management task and pass its output to the project owner for review.

## When not to use

- Do not use when the request falls outside knowledge management or fails the registered specialist trigger.
- Do not use its output as client approval, verified research or professional advice.
- For the paired agency:zk-steward work, use that tool and hand off this artefact.

## Inputs it needs

- A specific brief, intended output and project phase.
- Relevant documents, source links and constraints; keep client records and personal data in the approved private store.

## How to run it

1. Check the task against the registered job and trigger.
2. Read the source instructions and provide the minimum necessary inputs.
3. Invoke the tool using the name above and request the required artefact.
4. Have a separate reviewer check evidence, accuracy, privacy and fit before hand-off.

```text
Use skill:import-memory. Task: {task}. Project phase: {phase}. Context and source material: {links/files and constraints}. Deliverable: {format and audience}. Follow the tool's documented instructions; distinguish evidence from interpretation, state unknowns and do not claim approval.
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

- `agency:zk-steward` — coordinate the hand-off for the same job; pass the artefact and constraints.

## Limits and cautions

- Capabilities are limited to those documented in the source; ask for unknown details rather than assuming them.
- Human review remains responsible for factual accuracy, suitability and approval.
- Distribution: Not documented; availability: claude. Confirm setup or sign-in requirements before relying on the tool.
