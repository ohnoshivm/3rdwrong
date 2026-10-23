---
title: Memory Management
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:memory-management
department: operations
sub_department: knowledge-systems
job: knowledge-management
role: specialist
trigger: "Use when the user asks to \"remember project context\", review saved findings, initialize runtime memory, archive stale work, reconcile notes, or erase a subject; manages authorized HOT/WARM/COLD working memory across all disciplines while preserving registry event ownership and privacy controls."
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-aaron-he-zhu-aaron-marketing-skills-apache-2.0/skills/memory-management/SKILL.md
invoke: "`skill:memory-management` skill in Claude Code or Codex"
pairs_with: [agency:zk-steward]
---
# Memory Management

A specialist for knowledge management at 3RDWRONG, called when Use when the user asks to "remember project context", review saved findings, initialize runtime memory, archive stale work, reconcile notes, or erase a subject; manages authorized HOT/WARM/COLD working memory across all disciplines while preserving registry event ownership and privacy controls.

## What it does

- Use when the user asks to "remember project context", review saved findings, initialize runtime memory, archive stale work, reconcile notes, or erase a subject; manages authorized HOT/WARM/COLD working memory across…
- `../../references/runtime-invocation.md`
- Save a dated WARM artifact only after permission. Include source refs, observation dates, assumptions, open loops, and the registry offsets read.
- Promote at most three lines to HOT when the user explicitly pins the conclusion. HOT contains a pointer and current summary, not raw evidence.

## When to use

- Use when the user asks to "remember project context", review saved findings, initialize runtime memory, archive stale work, reconcile notes, or erase a subject; manages authorized HOT/WARM/COLD working memory across all disciplines while preserving registry event ownership and privacy controls.
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
Use skill:memory-management. Task: {task}. Project phase: {phase}. Context and source material: {links/files and constraints}. Deliverable: {format and audience}. Follow the tool's documented instructions; distinguish evidence from interpretation, state unknowns and do not claim approval.
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
- Distribution: vendor; availability: both. Confirm setup or sign-in requirements before relying on the tool.
