---
title: Gstack Document Generate
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:gstack-document-generate
department: operations
sub_department: knowledge-systems
job: documentation
role: lead
trigger: ""
kind: skill
availability: both
distribution: fetch
source: /Users/hustle/creative-engineering-os/library/skills/document-generate/SKILL.md
invoke: "`skill:gstack-document-generate` skill in Claude Code or Codex"
pairs_with: [design-steward:cut-weight, project-artifact:project-artifact]
---
# Gstack Document Generate

The lead for documentation at 3RDWRONG, supporting knowledge systems work.

## What it does

- Then branch on `SESSION_KIND` (echoed by the preamble; empty/absent ⇒ `interactive`):
- `spawned` → defer to the **Spawned session** block: auto-choose the recommended option. Never prose, never BLOCKED.
- `unattended` → auto-choose the recommended option; a consent, unrecommended question or approval gate becomes a pending gate item (Unattended session block).

## When to use

- Use for documentation in Phase 02 Research or the relevant production / hand-off phase when the request matches the documented scope.

## When not to use

- Do not use when the request falls outside documentation or fails the registered specialist trigger.
- Do not use its output as client approval, verified research or professional advice.
- For the paired design-steward:cut-weight work, use that tool and hand off this artefact.

## Inputs it needs

- A specific brief, intended output and project phase.
- Relevant documents, source links and constraints; keep client records and personal data in the approved private store.

## How to run it

1. Check the task against the registered job and trigger.
2. Read the source instructions and provide the minimum necessary inputs.
3. Invoke the tool using the name above and request the required artefact.
4. Have a separate reviewer check evidence, accuracy, privacy and fit before hand-off.

```text
Use skill:gstack-document-generate. Task: {task}. Project phase: {phase}. Context and source material: {links/files and constraints}. Deliverable: {format and audience}. Follow the tool's documented instructions; distinguish evidence from interpretation, state unknowns and do not claim approval.
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

- `design-steward:cut-weight` — coordinate the hand-off for the same job; pass the artefact and constraints.
- `project-artifact:project-artifact` — coordinate the hand-off for the same job; pass the artefact and constraints.

## Limits and cautions

- Capabilities are limited to those documented in the source; ask for unknown details rather than assuming them.
- Human review remains responsible for factual accuracy, suitability and approval.
- Distribution: fetch; availability: both. Confirm setup or sign-in requirements before relying on the tool.
