---
title: Pdf
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: anthropic-skills:pdf
department: operations
sub_department: knowledge-systems
job: document-production
role: specialist
trigger: "Use when the approved work needs this capability: Use this skill whenever the user wants to do anything with PDF files. This includes reading or extracting text/tables from PDFs, combining or merging multiple PDFs into one, splitting PDFs apart, rotating pages, add…"
kind: plugin-skill
availability: claude-managed
distribution: manual
source: /Users/hustle/.claude/skills/synced/88e7af4e-a2cf-4b40-8488-91a856697e04_aa2d1473-adba-46ff-9558-93fbf2ea6240/pdf/SKILL.md
invoke: "`anthropic-skills:pdf` skill (Codex plugin; Claude availability: claude-managed)"
pairs_with: [documents:documents]
---
# Pdf

A specialist for document production at 3RDWRONG, called when Use this skill whenever the user wants to do anything with PDF files. This includes reading or extracting text/tables from PDFs, combining or merging multiple PDFs into one, splitting PDFs apart, rotating pages, add….

## What it does

- Use this skill whenever the user wants to do anything with PDF files. This includes reading or extracting text/tables from PDFs, combining or merging multiple PDFs into one, splitting PDFs apart, rotating pages,…
- Addresses pdf processing guide as a documented part of its workflow.
- Addresses quick start as a documented part of its workflow.

## When to use

- Use when the approved work needs this capability: Use this skill whenever the user wants to do anything with PDF files. This includes reading or extracting text/tables from PDFs, combining or merging multiple PDFs into one, splitting PDFs apart, rotating pages, add…
- In a 3RDWRONG project, use during the relevant document production task and pass its output to the project owner for review.

## When not to use

- Do not use when the request falls outside document production or fails the registered specialist trigger.
- Do not use its output as client approval, verified research or professional advice.
- For the paired documents:documents work, use that tool and hand off this artefact.

## Inputs it needs

- The named document type or template, its purpose, audience and required format.
- Relevant documents, source links and constraints; keep client records and personal data in the approved private store.

## How to run it

1. Check the task against the registered job and trigger.
2. Read the source instructions and provide the minimum necessary inputs.
3. Invoke the tool using the name above and request the required artefact.
4. Have a separate reviewer check evidence, accuracy, privacy and fit before hand-off.

```text
Use anthropic-skills:pdf. Task: {task}. Project phase: {phase}. Context and source material: {links/files and constraints}. Deliverable: {format and audience}. Follow the tool's documented instructions; distinguish evidence from interpretation, state unknowns and do not claim approval.
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

- `documents:documents` — coordinate the hand-off for the same job; pass the artefact and constraints.

## Limits and cautions

- Capabilities are limited to those documented in the source; ask for unknown details rather than assuming them.
- Human review remains responsible for factual accuracy, suitability and approval.
- Distribution: manual; availability: claude-managed. Confirm setup or sign-in requirements before relying on the tool.
