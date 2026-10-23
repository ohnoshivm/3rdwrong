---
title: Project Artifact
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: project-artifact:project-artifact
department: operations
sub_department: knowledge-systems
job: documentation
role: specialist
trigger: "Use when the approved work needs this capability: Generate and publish a project status artifact — an opinionated, tabbed status page for a project too big for one update (overview & success criteria, the workstream sequence, next steps, plus background, plan, risks & open questions, and decisions/FAQ when they earn a tab) — published with the built-in Artifact tool to a default-private claude.ai page the user can share with teammates. Use when a piece of work spans several workstreams and you want a shareable overview kept current. Each artifact is backed by a small per-project config in the plugin data dir, so refreshing it re-gathers live state, redeploys the same URL, and reports only the delta. For software projects whose workstreams are PRs, also read swe.md (the X.Y PR-numbering convention; pulling PR state with gh/git; a per-PR detail block). Needs the built-in Artifact tool (claude.ai login). Not for single-PR changes or public docs"
kind: plugin-skill
availability: claude
distribution: vendor
source: toolkit/vendor/plugin-claude-plugins-official-project-artifact-marketplace/skills/project-artifact/SKILL.md
invoke: "`project-artifact:project-artifact` skill (Codex plugin; Claude availability: claude)"
pairs_with: [skill:gstack-document-generate]
---
# Project Artifact

A specialist for documentation at 3RDWRONG, called when Generate and publish a project status artifact — an opinionated, tabbed status page for a project too big for one update (overview & success criteria, the workstream sequence, next steps, plus background, plan, risks & open questions, and decisions/FAQ when they earn a tab) — published with the built-in Artifact tool to a default-private claude.ai page the user can share with teammates. Use when a piece of work spans several workstreams and you want a shareable overview kept current. Each artifact is backed by a small per-project config in the plugin data dir, so refreshing it re-gathers live state, redeploys the same URL, and reports only the delta. For software projects whose workstreams are PRs, also read swe.md (the X.Y PR-numbering convention; pulling PR state with gh/git; a per-PR detail block). Needs the built-in Artifact tool (claude.ai login). Not for single-PR changes or public docs.

## What it does

- Generate and publish a project status artifact — an opinionated, tabbed status page for a project too big for one update (overview & success criteria, the workstream sequence, next steps, plus background, plan, risks…
- Project** — name, slug, one-line description, the audience the page is written for.
- Artifact** — `url` (written after the first publish; every later publish passes it),
- Sources** — where live state comes from: repos with the `gh` query parameters

## When to use

- Use when the approved work needs this capability: Generate and publish a project status artifact — an opinionated, tabbed status page for a project too big for one update (overview & success criteria, the workstream sequence, next steps, plus background, plan, risks & open questions, and decisions/FAQ when they earn a tab) — published with the built-in Artifact tool to a default-private claude.ai page the user can share with teammates. Use when a piece of work spans several workstreams and you want a shareable overview kept current. Each artifact is backed by a small per-project config in the plugin data dir, so refreshing it re-gathers live state, redeploys the same URL, and reports only the delta. For software projects whose workstreams are PRs, also read swe.md (the X.Y PR-numbering convention; pulling PR state with gh/git; a per-PR detail block). Needs the built-in Artifact tool (claude.ai login). Not for single-PR changes or public docs
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
Use project-artifact:project-artifact. Task: {task}. Project phase: {phase}. Context and source material: {links/files and constraints}. Deliverable: {format and audience}. Follow the tool's documented instructions; distinguish evidence from interpretation, state unknowns and do not claim approval.
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
