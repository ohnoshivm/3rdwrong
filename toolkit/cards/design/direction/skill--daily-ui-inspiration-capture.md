---
title: Daily UI Inspiration Capture
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:daily-ui-inspiration-capture
department: design
sub_department: direction
job: inspiration-taste
role: specialist
trigger: "When the approved scope specifically requires packaging a dated set of interface inspiration references."
kind: skill
availability: both
distribution: fetch
source: /Users/hustle/.agents/skills/daily-ui-inspiration-capture/SKILL.md
invoke: "/daily-ui-inspiration-capture skill"
pairs_with: [skill:taste-skill, skill:design-analysis, skill:video-to-superprompt]
---

# Daily UI Inspiration Capture

A workflow specialist for packaging dated UI inspiration references with local evidence and prompts. For 3RDWRONG, use this specialist when the registry trigger applies: “When the approved scope specifically requires packaging a dated set of interface inspiration references.”

## What it does

- Creates a dated article bundle rather than a screenshot dump.
- Selects exactly five final references and checks previous manifests for duplicate titles and URLs.
- Captures stills, videos, full-page screenshots, section crops and motion frames where possible.
- Includes concrete visual and motion notes, a builder prompt and a JSON manifest.

## When to use

- When the approved scope specifically requires packaging a dated set of interface inspiration references.
- When a repeatable daily capture bundle is requested for a named project.

## When not to use

- A one-off design analysis or critique; use `skill:design-analysis` or `skill:dieter-rams-principles`.
- When the task does not need a dated bundle with local media.

## Inputs it needs

- Project/workspace and current runbook; prior capture manifests.
- Browser-visible reference candidates and capture tools.

## How to run it

1. Invoke `/daily-ui-inspiration-capture` in Codex.
2. Follow the current project runbook; select five non-duplicate references.
3. Package the article, evidence and manifest; state blocked captures and fallback reasons.

```text
Use /daily-ui-inspiration-capture skill. Task: {specific decision or output}. Context: {approved strategy, source links, version and constraints}. Return the documented format, label evidence and unknowns, and stop where required inputs or approval are missing.
```

## What good output looks like

- Exactly five final references, deduped against earlier manifests.
- Full-page and contiguous section evidence are present where captured; fallback reasons are explicit.

## Quality checks

- [ ] The output answers the registry job and, for a specialist, the exact trigger.
- [ ] Every factual claim comes from supplied evidence or the tool’s documented method.
- [ ] An independent reviewer checks the output; the maker does not approve their own work.
- [ ] Accessibility, reduced motion and responsive behaviour are checked where relevant.

## Pairs with

- `skill:taste-skill` — upstream context or hand-off.
- `skill:design-analysis` — downstream review or delivery.
- `skill:video-to-superprompt` — downstream review or delivery.

## Limits and cautions

- Source requires browser capture in the Codex in-app browser, not Chrome.
- It may require network access; do not claim captures or videos that were not made.
- Never copy the reference design; keep client information outside the public repo.
- Fetch distribution: installation, account access or sign-in may be required before invocation; verify availability in the target host.
