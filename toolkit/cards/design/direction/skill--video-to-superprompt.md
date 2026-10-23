---
title: Video to Superprompt
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:video-to-superprompt
department: design
sub_department: direction
job: inspiration-taste
role: specialist
trigger: "When the approved scope specifically requires analyzing a reference video for its design and interaction principles."
kind: skill
availability: both
distribution: fetch
source: /Users/hustle/.agents/skills/video-to-superprompt/SKILL.md
invoke: "/video-to-superprompt skill"
pairs_with: [skill:daily-ui-inspiration-capture, skill:ceos-creative-direction, skill:taste-skill]
---

# Video to Superprompt

A specialist for turning an accessible reference video into a detailed build or inspiration prompt. For 3RDWRONG, use this specialist when the registry trigger applies: “When the approved scope specifically requires analyzing a reference video for its design and interaction principles.”

## What it does

- Locates and technically inspects a video, including duration, dimensions, frame rate, codec and file size.
- Analyses story, layout, motion, visual design, rebuild mechanisms and accessibility/performance.
- Builds an asset map and writes a single paste-ready prompt by default.
- Checks that referenced assets exist or are clearly marked as placeholders.

## When to use

- When the approved scope specifically requires analyzing a reference video for its design and interaction principles.
- When a builder needs a detailed prompt grounded in an uploaded or accessible reference video.

## When not to use

- When no video or accessible source exists; the skill says to ask for a file or URL.
- For exact recreation without inspecting available source HTML/CSS/JS when it is connected to the video.

## Inputs it needs

- Local, uploaded, browser-visible or linked video.
- Whether the goal is exact recreation, inspired adaptation, article or implementation brief.

## How to run it

1. Invoke `/video-to-superprompt` in Codex.
2. Follow the technical inspection and layered analysis workflow in the skill.
3. Check each asset path/URL and label placeholders before handing over the prompt.

```text
Use /video-to-superprompt skill. Task: {specific decision or output}. Context: {approved strategy, source links, version and constraints}. Return the documented format, label evidence and unknowns, and stop where required inputs or approval are missing.
```

## What good output looks like

- The prompt preserves observed sequence, pacing and mechanisms without vague motion language.
- Mobile, reduced motion, accessibility and performance constraints are explicit.

## Quality checks

- [ ] The output answers the registry job and, for a specialist, the exact trigger.
- [ ] Every factual claim comes from supplied evidence or the tool’s documented method.
- [ ] An independent reviewer checks the output; the maker does not approve their own work.
- [ ] Accessibility, reduced motion and responsive behaviour are checked where relevant.

## Pairs with

- `skill:daily-ui-inspiration-capture` — upstream context or hand-off.
- `skill:ceos-creative-direction` — downstream review or delivery.
- `skill:taste-skill` — downstream review or delivery.

## Limits and cautions

- Codex skill; `ffprobe`/`ffmpeg` may be needed for local video analysis.
- Do not invent details when the video cannot be accessed.
- References are inspiration unless the user explicitly requests exact recreation and rights allow it.
- Fetch distribution: installation, account access or sign-in may be required before invocation; verify availability in the target host.
