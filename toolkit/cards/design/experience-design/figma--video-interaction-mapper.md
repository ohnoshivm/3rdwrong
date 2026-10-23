---
title: Video Interaction Mapper
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: figma:video-interaction-mapper
department: design
sub_department: experience-design
job: interaction-architecture
role: specialist
trigger: "A Figma file/workspace exists or is explicitly requested, and the task requires video interaction mapper. Load this prerequisite only for its corresponding Figma operation."
kind: plugin-skill
availability: claude
distribution: fetch
source: /Users/hustle/.claude/plugins/cache/claude-plugins-official/figma/2.2.120/workflow-skills/video-interaction-mapper/SKILL.md
invoke: "video-interaction-mapper skill (Claude Code plugin `figma`)"
pairs_with: [skill:ux-storyboard, skill:designing-user-experience]
---
# Video Interaction Mapper

The experience-design specialist for `interaction-architecture` is Video Interaction Mapper (trigger: “A Figma file/workspace exists or is explicitly requested, and the task requires video interaction mapper. Load this prerequisite only for its corresponding Figma operation”), which turns a ui recording into a static annotated figma storyboard of key interaction states.

## What it does

- Extracts key frames and scene changes.
- records visible state transitions and inferred triggers.
- places screenshots, markers and annotations in Figma.

## When to use

- Use when a Figma file/workspace exists or is requested and a UI recording needs mapping into interaction states.
- A Figma file/workspace exists or is explicitly requested, and the task requires video interaction mapper. Load this prerequisite only for its corresponding Figma operation.

## When not to use

- Use `skill:ux-storyboard` for a storyboard without a supplied recording, or `skill:designing-user-experience` for interaction architecture.
- Do not use it to approve its own work; have an independent reviewer check the artefact.

## Inputs it needs

- Local .mp4/.mov/.webm/.avi, ffmpeg/ffprobe, Python Pillow, Figma Design file and required Figma MCP tools.
- Versioned approved brief/strategy and source links; mark draft material as formative.

## How to run it

1. Confirm the trigger, stage and source material; keep client data in the approved private store.
2. Run it using the invocation above and provide the required inputs.
3. Check the output against the quality checks; hand unresolved decisions to the named human owner.

```text
Use video-interaction-mapper skill (Claude Code plugin `figma`). Studio phase: {phase}. Project: {project}. Approved goal/strategy: {goal and source}. Scope: {screen, flow or interaction}. Inputs/evidence: {links and versions}. Constraints: {platform, accessibility, motion, privacy}. Produce key moments are traceable to frames; uncertain causes/targets are explicitly marked; annotation text avoids unsupported claims. Keep documented facts separate from interpretation and hypothesis; list unknowns and the next human decision.
```

## What good output looks like

- A Figma Design storyboard with key moments, concise labels and uncertainty marked for inferred triggers.
- Evidence claims are labelled Documented, Interpretation, Hypothesis or Unknown as applicable.
- The output names open questions, owner and next action.

## Quality checks

- [ ] An independent checker verifies the output against the approved scope and artefact version.
- [ ] No unsupported user, audience, accessibility, performance or business outcome is presented as fact.
- [ ] Responsive, keyboard/focus and reduced-motion needs are included where relevant.

## Pairs with

- Related tools: `skill:ux-storyboard`, `skill:designing-user-experience`. Use the relevant method or specialist to complete the handoff.
- Engineering owns implementation, general testing, performance and security; Design owns experience intent and craft.

## Limits and cautions

- Fetch installation/sign-in and working ffmpeg, ffprobe, Pillow and Figma MCP are prerequisites. Use only Figma Design files, not FigJam or Slides.
- Respect the tool distribution: vendor copies are repo snapshots; fetch/manual sources need their stated install or sign-in.
- Client data, personal data and credentials stay out of the public repository.
- Motion is purposeful and honours reduced motion; avoid the rejected own-identity vocabulary in D-0006.
