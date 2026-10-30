---
title: "Routing and fallbacks: which model for what, and what to do when one fails"
type: guide
status: experimental
owner: founder
last_reviewed: 2026-10-31
review_every_days: 180
---

# Routing and fallbacks: which model for what, and what to do when one fails

Our rule of thumb: one strong model directs and decides; cheaper, faster models implement approved decisions; every role has a written fallback before the work starts. On the night of 30 October we met a Claude usage limit, a video-model overload, a provider quota, a DNS error, a free-tier limit and a dropped stream. Every one was recoverable because the work was on disk and the next step was obvious. In v1 we improvised the fallbacks. In v2 you write them down first.

## Who did what in the oryzo.ai case

Times in IST. See the [playbook](../../playbook/README.md) for the stages.

| Role | Model or tool | Work |
| --- | --- | --- |
| Director | Claude Opus 5.5 (in T3 Code, over the Claude Code harness) | Watched the frames, planned, wrote every brief and the spec, reconciled findings, ran QA and packaging |
| Video | `watch` skill: Gemini 3.7 Flash (failed with 503), then local ffmpeg frames | Turned the recording into evidence |
| Reverse engineering, agents A, B, C | `reverse-engineer-anything` skill and REA MCP; Playwright with headed Chrome; DeepSeek V4.1 Flash on the free tier through OpenCode | Static bundle analysis, runtime capture, tokens |
| Images | GPT-6 Luna with built-in image generation | 27 files |
| DOM build | DeepSeek (scaffold), then GPT-6 Luna at max effort | Scroll engine port, text choreography, layout, preloader, mobile, reduced motion |
| GL build | GPT-6.1 Sol at high effort | Renderer, model loader, hero composite, camera scrub, GPU-skinned hand, post chain |
| Infrastructure | T3 Code (multi-provider orchestration), OpenCode, Codex, Vite, three.js, GSAP SplitText, ffmpeg, Python with Pillow | |

**Spend.** No metered or pay-as-you-go spend. The work ran on existing subscriptions (Claude, ChatGPT, a TokenHarbor pass that ran out) and free tiers (OpenCode DeepSeek, a Gemini key). We did not record exact token counts, so we make no claim about them.

## Routing principles

1. **The strongest model directs; it does not execute.** It plans, writes briefs, decides, reconciles, reviews. Using it to type code spends the scarcest thing you have.
2. **Executors implement decisions that are already made.** An executor that reopens a design decision is a brief that left one open.
3. **Free and subscription capacity first.** No pay-as-you-go without the human's approval. Our TokenHarbor run failed instantly because its pass allowance was used up; pay-as-you-go had been deliberately left off, and we moved to the free tier instead of turning it on.
4. **Match the model to the job:**
   - substantial implementation, from a spec: a coding-tuned executor at `high`;
   - complex multi-file work and recovery from a failed attempt: a stronger model;
   - images: whatever has a built-in image tool, on a subscription;
   - extraction, formatting, bulk or mechanical edits: the cheapest executor that can do it;
   - taste, strategy, reconciliation: the director.
5. **One accountable executor per task**, and never two agents editing the same files.
6. **Verify with deterministic checks before asking another model** (types, build, tests, screenshots).

## Effort levels

Effort is a time and cost dial, and it is not monotonic with quality.

| Level | Use it for | What we saw |
| --- | --- | --- |
| low | Mechanical work: renames, saving files, linking a skill | The frame-saving and skill-linking task went to a DeepSeek agent in one short brief. We did not record its effort setting |
| medium | Generation with a clear spec | The image agent at medium finished in about 10 minutes |
| high | **The default for implementation** | The GL agent at high produced 20/20 tests and a 60 fps average by about 00:45 |
| max | A named hard problem, not a default | The DOM agent at max took about 40 minutes before writing its first file |

If an agent has been silent for a long time, ask what its first file is. A long silence at maximum effort is often planning, not progress. Calibrate on the first run and write the result into your routing table.

## The fallback table

Written as: what happened, what we did, what to pre-write.

| Failure | What we did | Pre-write in v2 |
| --- | --- | --- |
| **Claude usage limit** (the first attempt had hit a 5-hour limit) | Waited for the reset; the founder said "continue" and the session resumed | Keep every brief and ledger on disk so any agent can continue. If you have a second account, route subagents to it |
| **Video model overload** (Gemini 503 at about 19:40) | Extracted 36 frames locally with ffmpeg at 3 fps and read them directly | Make local frames the default; treat the video model as a bonus |
| **Provider allowance used up** (TokenHarbor, at about 20:07) | Relaunched on the free OpenCode DeepSeek | List providers in order and switch without discussion |
| **Transient DNS error** (OpenCode, `opencode.ai` not found, after partial work) | Resumed from disk with a resume note at 20:25 | A retry once, then a resume note, not a rerun |
| **Free-tier limit** (DeepSeek, after scaffolding the DOM) | Relaunched the DOM agent on GPT-6 Luna at max effort on a second ChatGPT account, with a resume note; cancelled the stale automatic retry | Name the fallback model and effort per role in advance |
| **Stream lost** (agent B, at about 22:13, very end of its run) | Read its files: complete (101 screenshots, scroll physics, intro, interactions). Did not rerun | Check the disk first; ask for appended output so a crash costs nothing |
| **Effort too high** (DOM at max, 40 minutes to a first file) | Learned: use `high` for routine code | Set the effort per brief |
| **Stalled automation** (the preloader, about 50 minutes) | Split into parallel agents; read the code first; mirror and `scrollTo` | The stage 2 rig, before any capture |
| **Sandbox blocked a local port** (00:56, "show it to me in localhost") | Ran the dev server outside the sandbox at 127.0.0.1:5180 | Know which environment may bind ports, and ask once if it needs approval |
| **Markdown mangled pasted code** (`__THREE_DEVTOOLS__` turned bold) | Fixed it before sending | Fenced code, plain text |

### A note on duplicates

When a provider's limit lifts, its queue may automatically resume the old task, and you will have two agents doing one job. **Cancel the original before relaunching elsewhere.** We did, for the DOM agent.

## A routing table to fill in before you start

| Role | First choice | Second | Third | Effort | Time to first file (expected) |
| --- | --- | --- | --- | --- | --- |
| Director | {{ }} | {{ }} | {{ }} | | n/a |
| Video | `watch` with {{video model}} | local ffmpeg frames | | low | |
| Teardown A, B, C | {{free coding model}} | {{subscription coding model}} | {{stronger model}} | high | |
| Images | {{model with an image tool}} | {{another}} | the human, with prompts | medium | |
| DOM build | {{ }} | {{ }} | {{ }} | high | |
| GL build | {{ }} | {{ }} | {{ }} | high | |
| QA | the director | {{ }} | | medium | |

Rules for the table: a fallback must be able to *start from the ledger*, a fallback must not need money you did not approve, and the last column is filled in after the first run.

## Resume notes

A resume note is the first block of the next agent's brief (template: [resume-note.md](../../agent-system/templates/resume-note.md)). Four lines:

```text
RESUME NOTE: a previous {{role}} agent stopped because {{reason}}.
Already done; keep it and do not redo it: {{files and facts}}.
NOT done: {{files and tasks}}.
Do not change: {{contracts, decisions}}.
```

What made ours work: the "done" list named files, not feelings ("package.json with node_modules installed; tsconfig.json; `src/contract.ts` with the exact spec content; the symlink; fonts"). The "not done" list named the rest.

## Progress ledgers

A ledger is a plain file the agent appends to, never rewrites:

```text
## 00:41 milestone: hand skinning renders
- done: bone textures, vertex shader, frames 71-115
- verified: screenshot qa/gl-1440-4320.png matches step 48
- next: finger bands
- blocked: none
```

One per agent: `RE-LEDGER.md`, `qa/GL-LOG.md`, `qa/DOM-LOG.md` in our case. The director reads the last entry, not the whole file. The ledger is also what turns a failure into a ten-second resume.

## When the director itself is the one that stops

If the director's session ends, a new director needs: the spec, the report, the ledgers, the routing table and the list of open questions. Keep those in the repository, not in one conversation.
