---
title: Documents
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: documents:documents
department: operations
sub_department: knowledge-systems
job: document-production
role: lead
trigger: ""
kind: plugin-skill
availability: both
distribution: manual
source: /Users/hustle/.codex/plugins/cache/openai-primary-runtime/documents/26.1020.11127/skills/documents/SKILL.md
invoke: "`documents:documents` skill (Codex plugin; Claude availability: both)"
pairs_with: [anthropic-skills:docx, anthropic-skills:pdf]
---
# Documents

The lead for document production at 3RDWRONG, supporting knowledge systems work.

## What it does

- Create, edit, redline, and comment on `.docx`, Word, and Google Docs-targeted document artifacts inside the container, with a strict render-and-verify workflow. Use `render_docx.py` to generate page PNGs (and…
- For document creation and deterministic OOXML edits, it is still acceptable to use the bundled Python/OOXML helper scripts in this skill package when the JS surface is incomplete.
- Run any builder or helper file from a writable workspace or temp directory, not from the managed dependency directory itself.
- Run `render_docx.py` to produce `page-<N>.png` images (optionally also a PDF with `--emit_pdf`)

## When to use

- Use for document production in Phase 02 Research or the relevant production / hand-off phase when the request matches the documented scope.

## When not to use

- Do not use when the request falls outside document production or fails the registered specialist trigger.
- Do not use its output as client approval, verified research or professional advice.
- For the paired anthropic-skills:docx work, use that tool and hand off this artefact.

## Inputs it needs

- The named document type or template, its purpose, audience and required format.
- Relevant documents, source links and constraints; keep client records and personal data in the approved private store.

## How to run it

1. Check the task against the registered job and trigger.
2. Read the source instructions and provide the minimum necessary inputs.
3. Invoke the tool using the name above and request the required artefact.
4. Have a separate reviewer check evidence, accuracy, privacy and fit before hand-off.

```text
Use documents:documents. Task: {task}. Project phase: {phase}. Context and source material: {links/files and constraints}. Deliverable: {format and audience}. Follow the tool's documented instructions; distinguish evidence from interpretation, state unknowns and do not claim approval.
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

- `anthropic-skills:docx` — coordinate the hand-off for the same job; pass the artefact and constraints.
- `anthropic-skills:pdf` — coordinate the hand-off for the same job; pass the artefact and constraints.

## Limits and cautions

- Capabilities are limited to those documented in the source; ask for unknown details rather than assuming them.
- Human review remains responsible for factual accuracy, suitability and approval.
- Distribution: Not documented; availability: both. Confirm setup or sign-in requirements before relying on the tool.
