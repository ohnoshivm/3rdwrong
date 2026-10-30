---
title: "Stage 3: Teardown"
type: guide
status: experimental
owner: founder
last_reviewed: 2026-10-31
review_every_days: 180
---

# Stage 3: Teardown

**Purpose.** Work out *how* each effect is made, from the code, from measurement and from tokens, using three agents at once on separate files.

**Case.** The teardown of oryzo.ai (by [Lusion](https://oryzo.ai)) ran as three agents on DeepSeek V4.1 Flash (the free tier through OpenCode), launched at 21:23 and 21:24 on 30 October:

- **A** read the shipped code (no browser).
- **B** captured runtime behaviour: scroll physics, a screenshot every 90 px, the intro, hover.
- **C** collected tokens, the network inventory, mobile behaviour and performance.

A finished at 21:47, C at 21:55. B's connection dropped at about 22:13, at the very end; its files were already complete: 101 screenshots, scroll physics, intro and interaction data.

## Inputs → outputs

| In | Out (one owner per file) |
| --- | --- |
| Stage 1 frames and effect list; stage 2 scope, mirror, rig, inventory | **A:** `notes/A-code.md`, `notes/A-bundle.pretty.js`, `inventory/libraries.json`, `shaders/README.md` |
| | **B:** `captures/desktop/step-*.jpg`, `captures/scroll-steps.json`, `captures/B-*.json`, `captures/intro.json`, `captures/interactions.json`, `inventory/scroll-map.json`, `inventory/effects.json`, `notes/B-runtime.md` |
| | **C:** `inventory/network.json`, `inventory/tokens.json`, `inventory/perf.json`, `notes/C-tokens.md`, `captures/mobile/*` |
| | One append-only ledger, `RE-LEDGER.md`, and each agent's notes file as its own ledger |

## Steps (pipeline v2)

1. **Start all three agents together, at minute one.** In v1 one agent ran from about 20:05 and we split only when the founder said "speed up" at 21:22. The split took the work from stuck to finished in about 50 minutes.
2. **Give agent A the head start that matters: the gate.** Ask A to write the loader and boot conditions first, in the first 10 minutes, at the top of its notes, with the exact action a script needs. Agent B checks that file every few minutes. (In our case A found the preloader's strict gate and wrote the answer at the top of `A-code.md`.)
3. **Read the code before measuring.** B's measurements should be designed from A's formulas: you know which scalar to sample, which ranges to step through, which uniform to read. Where A has not written yet, B starts with what does not depend on code (the rig, the physics probes).
4. **Give every agent a scope, a file list it alone may write, a time budget and the evidence tags.** Our budgets: A about 45 minutes, B about 60, C about 45. Tell them to append as they go.
5. **Capture scroll-stepped state.** B steps through the scope with scripted `scrollTo` (every 90 px, 101 steps for our 8,100 px), waits for settle, and at each step saves a screenshot, a row of internal scroll value, and the style and 3D state of every animated element. Then it scrolls back up the same steps and diffs: **scrubbed** (state is a function of scroll) or **triggered** (time-based)?
6. **Measure physics, don't guess.** One wheel event of known size, sampled every frame for 2.5 seconds, tells you the easing. Fit it.
7. **Stop and write.** Each agent ends with a final message: status, files, the ten most important findings with numbers, an answered, partial or unresolved table for the effect list, unknowns and blockers.

## The evidence to collect

**A (code):** libraries and versions; where scroll is handled; the formula behind each effect; the order of render passes; renderer settings; model and texture formats; the line number of each finding in the pretty-printed copy. Short excerpts only, into a notes file.

**B (runtime):**

- scroll model (native or virtual), the follower constants, per-event wheel clamp;
- for every step: position, element rects, computed transform, opacity, filter, plus 3D object state or uniforms;
- scrubbed or triggered, per effect, with the scroll ranges in px and in section progress `r`;
- the intro: element order and timings in the first 6 seconds at 60 fps;
- hover: what changes (bones, uniforms, DOM) and what does not.

**C (tokens, network, mobile, performance):**

- every text element's family, weight, size, line height, tracking, colour; the palette; the grid; z-order;
- the full network list with sizes;
- mobile (390×844): what is simplified;
- a DevTools trace: frame time, long tasks, main-thread against GPU, LCP, CLS, and any adaptive quality.

Every number carries a tag: `[code]`, `[measured]` or `[inferred]`, with what would confirm the inferred ones.

## What the three found

Enough to rebuild the section. A few headlines, all from FACTS and the report: one scroll scalar per section with every effect a `fit()` of it; smoothing done once in the scroll engine (wheel coefficient 12 in code, about 7 measured for the wheel); a hero that is a 2D composite, not 3D; a 36-bone GPU-skinned hand played between 3,056 and 4,950 px of scroll; an edge glow driven by scroll. Performance: 60 fps locked on an M3, CLS 0, LCP 6.5 to 7.2 s because the preloader gates it.

## Common traps

- **A browser-first single agent.** *Ours: about 50 minutes stuck behind the preloader while the answer sat in the code.* Read code first; run the agents in parallel.
- **Agents overwriting each other.** One owner per file. We told each agent which files it alone could write, and none collided.
- **Contention.** B and C ran Chrome at the same time, so their frame rates are floors. The notes say so.
- **A stream that drops.** B's connection was lost at the very end. Because it appended findings as it went, we read the files, found them complete, and did not rerun anything. Check the disk before you relaunch.
- **Printing big data into the conversation.** It exhausts the context. Write JSON to files; read ranges.
- **Out-of-scope code.** Tell A to ignore code that serves only later sections, or it will report a table and splats that are not in your hero.
- **A mangled paste.** When we pasted the instrumentation snippet into a prompt, Markdown turned `__THREE_DEVTOOLS__` into bold text. Paste code in fenced blocks and as plain text.

## Done when

- [ ] A, B and C each wrote their files and a final report with an answered, partial or unresolved table.
- [ ] Every effect in the stage 1 list has a status.
- [ ] The scroll-stepped capture covers the whole scope, with screenshots and state rows on disk.
- [ ] Scrubbed or triggered is decided for each effect.
- [ ] Unknowns are listed, not hidden.
- [ ] Nothing captured from the site is staged for publication.

## Tools

| Tool | Use |
| --- | --- |
| `reverse-engineer-anything` skill (REA) | A's bundle analysis; module tracing; network capture; event-listener inspection; script export |
| Playwright (`playwright-core`, headed Chrome) | B's and C's captures ([capture-steps.mjs](../agent-system/scripts/capture-steps.mjs)); the init-script hooks ([hooks.js](../agent-system/scripts/hooks.js), [deep dive](../tracks/dev/deep-dives/capturing-scenes-and-shaders.md)) |
| ffmpeg | Comparing a reference frame with step screenshots cheaply |
| Executors | Free-tier DeepSeek worked for all three; see [routing](../tracks/ai-builder/routing-and-fallbacks.md) |

Templates: [teardown-prompt.md](../agent-system/templates/teardown-prompt.md), [agent-a-static.md](../agent-system/templates/agent-a-static.md), [agent-b-runtime.md](../agent-system/templates/agent-b-runtime.md), [agent-c-tokens.md](../agent-system/templates/agent-c-tokens.md). Prompt: [prompt-pack, stage 3](../tracks/ai-builder/prompt-pack.md#stage-3-teardown). Next: [stage 4, Reconcile](04-reconcile.md).
