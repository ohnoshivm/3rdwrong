---
title: Cut Weight
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: design-steward:cut-weight
department: operations
sub_department: knowledge-systems
job: documentation
role: specialist
trigger: "Use when the approved work needs this capability: Sanitize repositories and project folders by removing development residue: superseded plans, completed audits, duplicate docs, plugin output, scratch files, and disposable artifacts. Read project intent, resolve consequential ambiguities through a brief grouped conversation, archive locally, and repair surviving guidance. Use for repository bloat, folder cleanup, or audit-only reviews. Operational code is protected; feature retirement is separate work"
kind: plugin-skill
availability: claude
distribution: vendor
source: toolkit/vendor/plugin-account-synced-design-steward-marketplace/components/cut-weight/skills/cut-weight/SKILL.md
invoke: "`design-steward:cut-weight` skill (Codex plugin; Claude availability: claude)"
pairs_with: [skill:gstack-document-generate]
---
# Cut Weight

A specialist for documentation at 3RDWRONG, called when Sanitize repositories and project folders by removing development residue: superseded plans, completed audits, duplicate docs, plugin output, scratch files, and disposable artifacts. Read project intent, resolve consequential ambiguities through a brief grouped conversation, archive locally, and repair surviving guidance. Use for repository bloat, folder cleanup, or audit-only reviews. Operational code is protected; feature retirement is separate work.

## What it does

- Sanitize repositories and project folders by removing development residue: superseded plans, completed audits, duplicate docs, plugin output, scratch files, and disposable artifacts. Read project intent, resolve…
- audit**: inventory, interpretation, proposed groups and unresolved questions.
- cleanup** (default for action requests): establish the shared understanding,
- aggressive**: the same scope with more decisive removal of proven residue.

## When to use

- Use when the approved work needs this capability: Sanitize repositories and project folders by removing development residue: superseded plans, completed audits, duplicate docs, plugin output, scratch files, and disposable artifacts. Read project intent, resolve consequential ambiguities through a brief grouped conversation, archive locally, and repair surviving guidance. Use for repository bloat, folder cleanup, or audit-only reviews. Operational code is protected; feature retirement is separate work
- In a 3RDWRONG project, use during the relevant documentation task and pass its output to the project owner for review.

## When not to use

- Do not use when the request falls outside documentation or fails the registered specialist trigger.
- Do not use its output as client approval, verified research or professional advice.
- For the paired skill:gstack-document-generate work, use that tool and hand off this artefact.

## Inputs it needs

- A specific brief, intended output and project phase.
- Relevant documents, source links and constraints; keep client records and personal data in the approved private store.

## How to run it

1. Check the task against the registered job and trigger.
2. Read the source instructions and provide the minimum necessary inputs.
3. Invoke the tool using the name above and request the required artefact.
4. Have a separate reviewer check evidence, accuracy, privacy and fit before hand-off.

```text
Use design-steward:cut-weight. Task: {task}. Project phase: {phase}. Context and source material: {links/files and constraints}. Deliverable: {format and audience}. Follow the tool's documented instructions; distinguish evidence from interpretation, state unknowns and do not claim approval.
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

- `skill:gstack-document-generate` — coordinate the hand-off for the same job; pass the artefact and constraints.

## Limits and cautions

- Capabilities are limited to those documented in the source; ask for unknown details rather than assuming them.
- Human review remains responsible for factual accuracy, suitability and approval.
- Distribution: vendor; availability: claude. Confirm setup or sign-in requirements before relying on the tool.
