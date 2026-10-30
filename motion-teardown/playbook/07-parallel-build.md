---
title: "Stage 7: Parallel build"
type: guide
status: experimental
owner: founder
last_reviewed: 2026-10-31
review_every_days: 180
---

# Stage 7: Parallel build

**Purpose.** Build the DOM layer and the WebGL layer at the same time, with the image agent running beside them, so that three agents write code for an hour without stepping on each other. The enabling pieces are the contract, file ownership, failure behaviour written into the spec, and QA running alongside.

**Case.** The rebuild of oryzo.ai (by [Lusion](https://oryzo.ai)) ran from about 23:40 on 30 October. Three agents launched at once: IMG (GPT-6 Luna, medium), DOM (DeepSeek free, high) and GL (GPT-6.1 Sol, high). The stack: Vite, TypeScript, vanilla three.js and GSAP SplitText.

## Inputs → outputs

| In | Out |
| --- | --- |
| `BUILD-SPEC.md`, `src/contract.ts` | The app in `studies/<name>/` |
| The research folder (report, notes, captures) | `qa/DOM-LOG.md` and `qa/GL-LOG.md`: progress ledgers |
| An agent per owner, each with a brief | Screenshots in `qa/`, a build, a completion report per agent |

## Steps (pipeline v2)

1. **Write one brief per agent** with the seven parts: Objective · Context · Files · Constraints · Implementation · Acceptance · Output. See [directing agents](../tracks/ai-builder/directing-agents.md). Templates: [build-agent-dom.md](../agent-system/templates/build-agent-dom.md), [build-agent-gl.md](../agent-system/templates/build-agent-gl.md), [build-agent-images.md](../agent-system/templates/build-agent-images.md).
2. **Fix the ownership table and say what each agent must not touch.** Ours: DOM owns the scaffold, `src/core`, `src/dom`, `src/styles` and `public/fonts`; GL owns `src/gl` and the symlink to the study mirror; IMG owns `public/gen` and `scripts/gen`. No path has two owners.
3. **Make the first minutes unblock the others.** The DOM brief's first job, "within your first few minutes", is to scaffold the project, install the dependencies, create `src/contract.ts` with exactly the spec text and link the study assets, because the GL agent cannot start without them and never edits `package.json`.
4. **Choose the effort level per agent, not per project.** `high` for substantial code. We put the DOM agent's second run at `max` and it took about 40 minutes to write its first file. Use `max` only for a named hard problem.
5. **Set the routing and the fallbacks before launching**, not during. See [routing and fallbacks](../tracks/ai-builder/routing-and-fallbacks.md).
6. **Require a progress ledger.** Each agent appends to its own log after every milestone, so a crash loses nothing and a replacement can resume.
7. **Run QA in parallel.** When the first screenshots land, start reviewing them against the originals instead of waiting for the final report (see [stage 8](08-compare.md)).
8. **Review the completion reports** with deterministic checks first (build, types, tests, screenshots), before asking another model's opinion.

## Evidence to collect

- Each agent's completion report: status, files, build result, screenshots with mismatch notes, console output, open items.
- The ledgers, with timestamps.
- Build output; the GL agent's functional test count (ours: 20 of 20); frame-time sweeps (ours: averaged 60 fps on the M3, p95 17.2 to 17.4 ms).
- The shader warm-up result: about 250 ms before `ready`, removing a 913 ms first-use spike.
- `stage.ready` settling within 10 seconds, even with files missing.

## What happened, in order

| Time (IST) | Event |
| --- | --- |
| ~23:40 | Spec written; IMG, DOM and GL briefed |
| ~23:50 | The DOM agent hit the free DeepSeek usage limit after scaffolding |
| 23:51 | IMG finished: 27 files |
| ~23:52 | DOM relaunched on GPT-6 Luna at max effort, on a second ChatGPT account, with a resume note listing what was done; the stale automatic retry on the first provider was cancelled |
| 00:29 | Founder: "speed up" (lightly edited). Claude reviewed the GL screenshots in parallel rather than waiting; the founder accepted the strong red glow as it was |
| ~00:45 | GL finished: 20/20 functional tests, 60 fps average |
| 00:56 | Founder: "show it to me in localhost". The sandbox blocked local port binding; the dev server ran outside it, at 127.0.0.1:5180 |
| ~01:00 | The rebuild was on localhost; approved at 01:20 |

## Common traps

- **Quota in the middle.** *Ours: the DOM agent ran out of its free tier right after scaffolding.* The resume note let the next agent skip all finished work (package, config, contract, symlink, fonts) and pick up the rest. See [routing](../tracks/ai-builder/routing-and-fallbacks.md).
- **The duplicate that arrives later.** When a provider's limit lifts, a queued auto-retry can resume the old task and duplicate the new one. Cancel the original before you relaunch elsewhere. We did.
- **Effort that looks like progress.** Forty minutes of thinking before the first file is a cost. Calibrate.
- **A contract edit in the middle.** The contract was never changed after launch. Resist the urge to "just add a field".
- **Hidden hangs.** The spec's rule that `stage.ready` settles within 10 seconds, with placeholders, is what let GL be developed while images were still being made.
- **Sandboxed servers.** If the agent's environment blocks local ports, run the dev server where it is allowed, and say so in the report.

## Done when

- [ ] Each agent's build passes and its completion report is in.
- [ ] No agent edited a file it does not own (check the diff by path).
- [ ] The contract is byte-for-byte the spec's text.
- [ ] `stage.ready` settles in 10 seconds with a file deliberately missing.
- [ ] The app runs on localhost with a clean console.
- [ ] QA findings from the parallel review are fixed or accepted by the human.

## Tools

| Tool | Use |
| --- | --- |
| Coding agents | DeepSeek V4.1 Flash first for code; GPT-6.1 Sol for the multi-file GL work; GPT-6 Luna for the DOM and images |
| Vite, TypeScript, three.js, GSAP SplitText | The stack |
| Playwright | The agents' own screenshot checks |
| Image generation | The IMG agent ([stage 6](06-assets.md)) |

Resume template: [resume-note.md](../agent-system/templates/resume-note.md). Prompt: [prompt-pack, stage 7](../tracks/ai-builder/prompt-pack.md#stage-7-parallel-build). Next: [stage 8, Compare](08-compare.md).
