---
title: "The briefs: every prompt from the Oryzo session"
type: guide
status: experimental
owner: founder
last_reviewed: 2026-10-31
review_every_days: 180
---

# The briefs: every prompt from the Oryzo session

These are the eleven briefs the director model (Claude Opus 5.5, in T3 Code) sent to agents during the study of [oryzo.ai](https://oryzo.ai) by Lusion on 30 October 2026, plus the founder's own key messages. Times are IST. The article explains what each part of a brief was for: see [ARTICLE.md §5](../../../ARTICLE.md).

## What was changed from the originals

The brief text is verbatim except for these substitutions:

- absolute project paths are written as `<project>/…`, and home-directory paths as `~/…`;
- the temporary folder for video frames is written as `<temporary-session>/`;
- the provider instance id of the second ChatGPT account is written as `codex (ChatGPT account 2)`, and the first as `codex (ChatGPT account 1)`;
- an npm package specifier that had already been redacted upstream appears as `<rea-cli-package>`.

The founder's messages in [`founder-prompts.md`](founder-prompts.md) are lightly edited for spelling, with profanity removed, and marked as such.

## Index

| # | Brief | Sent | Model and effort | What happened |
| --- | --- | --- | --- | --- |
| 01 | [Link watch skill + save Oryzo frames](01-link-watch-skill-save-oryzo-frames.md) | 19:40 | DeepSeek V4.1 Flash (free, OpenCode), low | Done; 12 key frames saved under descriptive names |
| 02 | [Reverse engineer oryzo.ai hero + 2 sections](02-reverse-engineer-oryzo-ai-hero-2-sections.md) | 20:11 | DeepSeek V4.1 Flash 1017 (TokenHarbor), high | Failed instantly: pass allowance used up |
| 03 | [… (free DS)](03-reverse-engineer-oryzo-ai-hero-2-sections-free-ds.md) | 20:12 | DeepSeek V4.1 Flash (free), high | Same brief with stricter context rules; died on a DNS error after partial work |
| 04 | [… (DS, resume)](04-reverse-engineer-oryzo-ai-hero-2-sections-ds-resume.md) | 20:27 | DeepSeek V4.1 Flash (free), high | Resumed from disk; stalled about 50 minutes behind the preloader; stopped at 21:23 |
| 05 | [Agent A: bundle code analysis](05-oryzo-re-a-bundle-code-analysis.md) | 21:23 | DeepSeek V4.1 Flash (free), high | Done at 21:47; found the preloader gate and the formulas |
| 06 | [Agent B: runtime scroll capture](06-oryzo-re-b-runtime-scroll-capture.md) | 21:24 | DeepSeek V4.1 Flash (free), high | Stream lost at 22:13; files complete (101 screenshots) |
| 07 | [Agent C: tokens, network, mobile, perf](07-oryzo-re-c-tokens-network-mobile-perf.md) | 21:24 | DeepSeek V4.1 Flash (free), high | Done at 21:55 |
| 08 | [IMG: GPT image generation](08-oryzo-red-img-gpt-image-generation.md) | 23:41 | GPT-6 Luna, medium | Done; 27 files |
| 09 | [DOM: scaffold, scroll, text choreography](09-oryzo-red-dom-scaffold-scroll-text-choreography.md) | 23:41 | DeepSeek V4.1 Flash (free), high | Hit the free usage limit after scaffolding |
| 10 | [GL: renderer, scenes, hand, post](10-oryzo-red-gl-renderer-scenes-hand-post.md) | 23:41 | GPT-6.1 Sol, high | Done; 20/20 functional tests, 60 fps average on an M3 |
| 11 | [DOM (resume on Luna)](11-oryzo-red-dom-resume-on-luna.md) | 23:52 | GPT-6 Luna, max (second ChatGPT account) | Took about 40 minutes before writing its first file |
| — | [Founder's key messages](founder-prompts.md) | 19:34–01:41 | — | Scope, speed, taste and approval |
| — | [Image-generation prompts](image-prompts.md) | 23:41–23:53 | written by GPT-6 Luna for GPT image generation | The 12 prompts behind the 27 generated files |

## How to read them

- **02 → 03 → 04** show one brief adapting to three conditions: a paid route, a smaller context window, and a crash. Diff them to see what a resume note adds.
- **05, 06, 07** show one job split three ways by evidence type, with a written dependency between A and B.
- **08, 09, 10** show three build agents sharing one spec and one contract file, each owning its own folders.
- **09 → 11** show a relaunch on a different model that keeps the first agent's work ("Already done… NOT done").

A note on scope: these briefs were written for a private study, and several of them refer to Lusion's downloaded assets in a git-ignored folder. The repository does not include or link those assets, the captured shaders, or Lusion's code.
