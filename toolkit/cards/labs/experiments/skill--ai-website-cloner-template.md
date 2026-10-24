---
title: Website deconstruction (clone-website)
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-24
tool_id: skill:ai-website-cloner-template
department: labs
sub_department: experiments
job: effect-studies
role: specialist
trigger: "Use when deconstructing a reference website (cloning, replication or reverse engineering, including animated pages) for study only; never ship cloned layouts, assets or code in client work."
kind: skill
availability: both
distribution: fetch
source: ~/.3rdwrong/fetch/pack-jcodesmore-ai-website-cloner-template-mit/.agents/skills/clone-website (pinned ee3f5a2f31fd549b9593fa4f7cf6d2955ee593bb)
invoke: "clone-website skill (Labs study only)"
pairs_with: [skill:3w-effect-study, skill:3w-taste-graph, skill:gsap-scrolltrigger]
---
# Website deconstruction (clone-website)

A Labs-only skill for deconstructing a reference website into its structure, behaviour and motion, so the studio can study how an effect is built. It is for study only. Never ship cloned layouts, assets or code in client work.

## What it does

- Maps a reference page: sections, routes, responsive behaviour and interactions.
- Observes the page at desktop and mobile widths, including scroll-driven and pinned scenes.
- Reads declared values (computed styles, variables, library options) rather than guessing from one rendering.
- Writes a source-to-local route map and a compact page brief for study notes.

## When to use

- A non-client effect study in Labs (for example, understanding a scroll-driven scene before writing an original version).
- Measuring frame, asset and motion budgets of a reference, to inform a Labs prototype.
- Teaching the studio how a published effect is built, with the source credited.

## When not to use

- Client work, of any kind, including "matching a reference" for a client. Never ship cloned layouts, assets or code (AGENTS.md; D-0021).
- Copying a brand's assets, copy or identity into any studio output.
- Any site whose owner has not given permission for study use.

## Inputs it needs

- A reference URL, and a written study question with no client attached.
- Confirmation that the study is non-client and the output stays in Labs.

## How to run it

1. Record the study question and confirm it is non-client.
2. Observe the reference and write the page brief; do not download production bundles for reuse.
3. Build an original Labs prototype from the observed principles, not from the source code.

```text
Use the clone-website skill for study only. Reference: {url}. Study question: {question}. Non-client. Produce the structure and motion observations as principles with Documented or Interpretation labels. Do not output or reuse the source code, images or copy. No output leaves Labs.
```

## What good output looks like

- A written study of structure, motion and budgets, with the reference credited.
- Principles that an original prototype can use, and an explicit statement that no source code or assets were reused.

## Quality checks

- [ ] The study is non-client and the output stays in Labs.
- [ ] No cloned layout, asset or code appears in any studio or client output.
- [ ] Reduced-motion behaviour noted for any motion observed.

## Pairs with

- `skill:3w-effect-study`: the Labs effect-study route.
- `skill:3w-taste-graph`: references and anti-patterns.
- `skill:gsap-scrolltrigger`: how an original scroll scene would be built.

## Limits and cautions

- MIT licence on the template repository. The upstream template is a full Next.js app; only the `clone-website` skill folder is installed.
- The skill is built for cloning. Its default purpose conflicts with studio policy, so it is installed for study only.
- Copying a live site may breach its terms; do not download or redistribute the site.
