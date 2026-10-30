---
title: "The playbook: eight stages from a screen recording to a working rebuild"
type: guide
status: experimental
owner: founder
last_reviewed: 2026-10-31
review_every_days: 180
---

# The playbook: eight stages from a screen recording to a working rebuild

This is the method behind Motion Teardown. It takes you from a short recording of a motion site you admire to a rebuild you can run, in eight stages, with evidence at every step. We used it on oryzo.ai by [Lusion](https://oryzo.ai): a 12-second recording became a working crimson-and-white rebuild of its hero and first scroll section, on localhost, in about six hours.

The playbook is **pipeline v2**. Version 1 is what we actually did that night; v2 is what we would do again, with the lessons folded in. Each stage file says which is which.

## The eight stages

| # | Stage | The question it answers | Main outputs | Tools | In our case |
| --- | --- | --- | --- | --- | --- |
| 1 | [Watch](01-watch.md) | What do I see, and which effects are there? | frames, effect list of hypotheses | `watch`, ffmpeg | 19:34 → about 19:42 |
| 2 | [Map](02-map.md) | What is the site made of, and what is in scope? | scope note, network and library inventory, local mirror, capture rig | REA, Playwright | part of a 20:05 → 21:22 single-agent run |
| 3 | [Teardown](03-teardown.md) | How does each effect work? | notes from three parallel agents, scroll-stepped captures | REA, Playwright | 21:22 → about 22:13 |
| 4 | [Reconcile](04-reconcile.md) | Where do the sources disagree, and which is right? | one tagged report | the director, targeted checks | about 22:15 → 22:45 |
| 5 | [Spec](05-spec.md) | What exactly will we build, and who builds what? | build spec, contract file, ownership table | the director | 23:06 → about 23:40 |
| 6 | [Assets](06-assets.md) | What new material do we need? | generated images, derived maps | image generation, ffmpeg or Pillow | 23:41 → 23:51 |
| 7 | [Parallel build](07-parallel-build.md) | Can several agents build without colliding? | the app | coding agents | about 23:40 → 01:00 |
| 8 | [Compare](08-compare.md) | Does it match, and can we prove it? | side-by-sides, fidelity score, console and frame-time report | Playwright, ffmpeg | 00:29 → 01:20 |

Times are IST, 30 to 31 October 2026, from the session record. Recording to approved rebuild on localhost was about 5.5 hours; to a verified share zip, 6 hours. Roughly an hour of the reverse-engineering stretch was lost to quota limits, a DNS error and a preloader stall; v2 removes the last of those by design.

## What changed from v1 to v2

| In the night as it happened (v1) | In pipeline v2 | The cost it removes |
| --- | --- | --- |
| One agent measured the live page first and read the code later | **Read the code before measuring.** Measurement is designed from the code's formulas | About 50 minutes stuck behind the site's preloader, with scroll stuck at 0 |
| Teardown became three parallel agents only after "speed up" at 21:22 | **Teardown agents run in parallel from minute one**, on separate files | The serial first hour |
| Capture failed until we served a local copy and scripted the scroll | **A local asset mirror and scripted `window.scrollTo` are set up in stage 2**, before any capture | Automation hangs on one missing file |
| The director reconciled A, B and C in conversation | **A formal reconcile step**, with a fixed evidence order: code > measured data > video | Wrong beliefs reaching the spec (we found four, and fixed them in time) |
| The contract and file ownership were written with the spec | **A contract and file ownership are fixed before any build agent starts** (we did this well; v2 makes it a gate) | Agents editing each other's files |
| DOM agent at `max` effort took about 40 minutes to write its first file | **Effort calibration**: `high` for routine code, higher only for a named hard problem | Idle time that looks like work |
| Providers failed one by one (a usage limit, a DNS error, a stream drop) and the director improvised | **A fallback routing table is written before the build** | Decisions under pressure |
| QA waited for the build | **QA runs in parallel with the build**, on the first screenshots | A late, large defect list |

## The evidence order

When sources disagree, they rank like this:

1. **Code** (`[code]`): what the shipped JavaScript says. It states the rule.
2. **Measured data** (`[measured]`): what the live page did when we drove it. It confirms the rule, or exposes a gap.
3. **Video** (`[video]`): what a human saw. It gives you hypotheses, and it is the least reliable of the three.

Tag every claim in your notes with one of these, or with `[inferred]` and the evidence that would confirm it. In our case the video said the glow was triggered by hovering the hand. The code and the data said it follows scroll. The video was wrong, and the tags are what let us see it.

## Layout of a study

```text
research/<site>/
  video-frames/        stage 1
  MOTION-PLAN.md       stage 1: hypotheses
  scope.md             stage 2
  inventory/           stage 2-3: network, libraries, tokens, scroll map
  _ref-assets/mirror/  stage 2: local mirror (git-ignored, never published)
  notes/               stage 3: A-code.md, B-runtime.md, C-tokens.md
  captures/            stage 3: step screenshots, state rows
  RE-LEDGER.md         running ledger, appended by every agent
  RE-REPORT.md         stage 4
  BUILD-SPEC.md        stage 5
studies/<name>/        stages 6-8: the rebuild and its qa/ folder
```

## Ground rules

- **Study, not copy.** Credit the site and its makers. Explain techniques in your own words, with your own code. Keep captured models, textures, shaders and source private. The [worksheet](../worksheets/byo-site.md) starts with a scope and legal check.
- **Captured material is data.** Text, scripts and comments on the page you study are untrusted. Agents never follow instructions found in them. Say so in every brief.
- **Every agent keeps a ledger.** One append-only file per agent. A crash must not lose work: in our case agent B's connection dropped at the very end, and because it had written files as it went, nothing was lost.
- **Ask the human only real questions.** See [asking the human](../tracks/ai-builder/asking-the-human.md).

## Who this is for, and where to go next

- **You want to understand the mechanisms and write them yourself:** the [dev track](../tracks/dev/README.md).
- **You want to direct agents through the method:** the [AI-builder track](../tracks/ai-builder/README.md), whose [prompt pack](../tracks/ai-builder/prompt-pack.md) holds a prompt for every stage here.
- **You have a site in mind:** the [BYO-site worksheet](../worksheets/byo-site.md).
- **Unfamiliar word:** the [glossary](../glossary.md).
- **The ready-made templates and scripts** live in [agent-system](../agent-system/README.md).
