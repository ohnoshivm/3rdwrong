---
title: "Tests for the dev-track code"
type: guide
status: experimental
owner: founder
last_reviewed: 2026-10-31
review_every_days: 180
---

# Tests for the dev-track code

These are the tests we ran against the lab and deep-dive snippets before publishing them. They are working files, kept as they were run, with absolute paths replaced by relative ones.

## What is here

| File | What it checks | Needs |
| --- | --- | --- |
| `node-l1.mjs` | `fit`, easings, section maths, the scroll model (frame-rate independence, the 200 px wheel clamp), stagger windows | Node 20+ |
| `node-l2.mjs` | the baked-clip sampler | Node 20+ |
| `node-l3.mjs` | bone pose maths, the spring, band weights, the gaussian kernel, frame statistics | Node 20+ |
| `node-dd.mjs` | the mesh container's round trip and error bound; the resilient loader (success, failure, synchronous throw, a hung item, the total deadline) | Node 20+ |
| `browser-l1.mjs` | L1's whole page: letters at set scroll positions, reversibility, the wheel path | Chrome, `playwright-core`, a built `page-l1/` |
| `browser-l2.mjs`, `browser-l2m.mjs` | L2's stage: pixel statistics inside and outside the glass; the combined L1 + L2 page at four scroll positions | as above, `page-l2/`, `page-l2m/` |
| `browser-l3.mjs` | L3's shaders: skinning against known poses, finger lift, edge glow, grade, bright-pass and blur, the three.js wiring | as above, `page-l3/` |
| `t-cap.mjs`, `run-capture.mjs`, `capture-init.js` | the capture hook against a small three.js page | as above, `page-cap/` |
| `run-compare.mjs` | the step-comparison script from the deep dives | Chrome, `playwright-core`, ffmpeg |
| `fixture.js` | a small input for the call scanner | — |
| `extract.mjs` | pulls every fenced block that starts with `// lab/<file>` out of the Markdown into `lab/` | Node 20+ |

The `node-*.mjs` files are self-contained bundles (the snippets plus the assertions), so they run as they are:

```sh
node node-l1.mjs && node node-l2.mjs && node node-l3.mjs && node node-dd.mjs
```

## Running the browser tests

The browser tests load small pages from `page-*/index.html`, which expect a bundled `main.js` beside them. We do not ship the bundles (one of them inlines all of three.js). Rebuild them from the Markdown:

```sh
cd motion-teardown/tracks/dev/tests
npm i playwright-core three esbuild
node extract.mjs ../*.md ../deep-dives/*.md      # writes the snippets into lab/
npx esbuild lab/main.ts      --bundle --outfile=page-l1/main.js
npx esbuild lab/l2-entry.ts  --bundle --outfile=page-l2/main.js
npx esbuild lab/main-l2.ts   --bundle --outfile=page-l2m/main.js
npx esbuild lab/l3-entry.ts  --bundle --outfile=page-l3/main.js
npx esbuild lab/cap-entry.ts --bundle --outfile=page-cap/main.js
node browser-l1.mjs && node browser-l2.mjs && node browser-l3.mjs && node t-cap.mjs
```

`lab/cap-entry.ts`, `lab/l2-entry.ts` and `lab/l3-entry.ts` are test entry points that are not in the Markdown; the rest of `lab/` comes from `extract.mjs`. The scripts launch the installed Chrome (`channel: 'chrome'`); change the launch options if you use another browser.

## Results and limits

When we published, the four Node suites passed from this folder. The browser suites passed in headless Chrome on an Apple M3 when Writer B ran them; we have not re-run them from this folder. What was not tested is listed in [the dev track README](../README.md#how-the-code-was-tested).
