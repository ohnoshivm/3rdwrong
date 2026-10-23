---
title: Google Slides
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: google-drive:google-slides
department: operations
sub_department: knowledge-systems
job: tool-integration
role: specialist
trigger: "Use when the approved work needs this capability: Route Google Slides authoring requests and derive a design system from a native template or reference deck. Use this skill when the user provides an existing native Google Slides deck as a template, reference, or prior-period source, or asks to edit, update, repair, restyle, or clean up an existing native Google Slides deck. Use the Presentations skill instead for net-new presentation creation when no existing native Google Slides deck must be followed"
kind: plugin-skill
availability: codex
distribution: vendor
source: toolkit/vendor/plugin-openai-curated-remote-google-drive-0.1.22/skills/google-slides/SKILL.md
invoke: "`google-drive:google-slides` skill (Codex plugin; Claude availability: codex)"
pairs_with: [agency:testing-tool-evaluator]
---
# Google Slides

A specialist for tool integration at 3RDWRONG, called when Route Google Slides authoring requests and derive a design system from a native template or reference deck. Use this skill when the user provides an existing native Google Slides deck as a template, reference, or prior-period source, or asks to edit, update, repair, restyle, or clean up an existing native Google Slides deck. Use the Presentations skill instead for net-new presentation creation when no existing native Google Slides deck must be followed.

## What it does

- Route Google Slides authoring requests and derive a design system from a native template or reference deck. Use this skill when the user provides an existing native Google Slides deck as a template, reference, or…
- Use `[@presentations](plugin://presentations@openai-primary-runtime)` to create a net-new presentation when no existing native Google Slides deck is the template or reference.
- Use this skill to create a presentation by following an existing native Google Slides template, reference deck, or prior-period deck.
- Use this skill to edit, update, repair, restyle, or clean up an existing native Google Slides deck.

## When to use

- Use when the approved work needs this capability: Route Google Slides authoring requests and derive a design system from a native template or reference deck. Use this skill when the user provides an existing native Google Slides deck as a template, reference, or prior-period source, or asks to edit, update, repair, restyle, or clean up an existing native Google Slides deck. Use the Presentations skill instead for net-new presentation creation when no existing native Google Slides deck must be followed
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
Use google-drive:google-slides. Task: {task}. Project phase: {phase}. Context and source material: {links/files and constraints}. Deliverable: {format and audience}. Follow the tool's documented instructions; distinguish evidence from interpretation, state unknowns and do not claim approval.
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
