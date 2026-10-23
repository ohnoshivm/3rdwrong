---
title: Google Drive
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: google-drive:google-drive
department: operations
sub_department: knowledge-systems
job: tool-integration
role: specialist
trigger: "Use for operations/knowledge-systems/tool-integration when the brief specifically requires: Use connected Google Drive as the single entrypoint for Drive, Docs, Sheets, and Slides work ."
kind: plugin-skill
availability: codex
distribution: vendor
source: toolkit/vendor/plugin-openai-curated-remote-google-drive-0.1.22/skills/google-drive/SKILL.md
invoke: "`google-drive:google-drive` skill (Codex plugin; Claude availability: codex)"
pairs_with: [agency:testing-tool-evaluator]
---
# Google Drive

A specialist for tool integration at 3RDWRONG, called when Use connected Google Drive as the single entrypoint for Drive, Docs, Sheets, and Slides work.

## What it does

- Use connected Google Drive as the single entrypoint for Drive, Docs, Sheets, and Slides work. Use when the user wants to find, fetch, organize, share, export, copy, or delete Drive files, or summarize and edit Google…
- If the user did not provide an exact file URL or ID, use Google Drive search, recent files, folder listing, or metadata reads to identify the right file.
- If the request starts as "find X and then update it," do the Drive discovery step first instead of guessing the target.
- Drive, Docs, Sheets, or Slides comment creation, comment replies, comment resolution, or review-by-comments: use [google-drive-comments](../../../vendor/plugin-openai-curated-remote-google-drive-0.1.22/skills/google-drive-comments/SKILL.md).

## When to use

- Use for operations/knowledge-systems/tool-integration when the brief specifically requires: Use connected Google Drive as the single entrypoint for Drive, Docs, Sheets, and Slides work .
- In a 3RDWRONG project, use during the relevant tool integration task and pass its output to the project owner for review.

## When not to use

- Do not use when the request falls outside tool integration or fails the registered specialist trigger.
- Do not use its output as client approval, verified research or professional advice.
- For the paired agency:testing-tool-evaluator work, use that tool and hand off this artefact.

## Inputs it needs

- The named connected service and the requested read or change; confirm the correct account and file.
- Relevant documents, source links and constraints; keep client records and personal data in the approved private store.

## How to run it

1. Check the task against the registered job and trigger.
2. Read the source instructions and provide the minimum necessary inputs.
3. Invoke the tool using the name above and request the required artefact.
4. Have a separate reviewer check evidence, accuracy, privacy and fit before hand-off.

```text
Use google-drive:google-drive. Task: {task}. Project phase: {phase}. Context and source material: {links/files and constraints}. Deliverable: {format and audience}. Follow the tool's documented instructions; distinguish evidence from interpretation, state unknowns and do not claim approval.
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

- `agency:testing-tool-evaluator` — coordinate the hand-off for the same job; pass the artefact and constraints.

## Limits and cautions

- Capabilities are limited to those documented in the source; ask for unknown details rather than assuming them.
- Human review remains responsible for factual accuracy, suitability and approval.
- Distribution: vendor; availability: codex. Confirm setup or sign-in requirements before relying on the tool.
