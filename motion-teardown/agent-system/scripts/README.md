---
title: "Capture a motion system at known scroll positions"
type: guide
status: experimental
owner: founder
last_reviewed: 2026-10-31
review_every_days: 180
---

# Capture a motion system at known scroll positions

Original Node tools, MIT © 2026 3RDWRONG. Use public pages you may inspect.
Captured third-party material stays in a private local study directory; it is
not covered by this repo's licences. Do not commit a mirror, bundle or shader
capture. Scripts never need your logged-in browser, cookies or API keys.

## Runtime

Use Node 20+, system Google Chrome and `playwright-core`. From this folder:

```sh
npm install
node capture-steps.mjs --help
npm test
```

The dependency is pinned to the version tested for this edition. No global
installation is required. `PLAYWRIGHT_CORE_PATH` may point to an existing folder
containing `node_modules/playwright-core`. `--executable`
selects a Chromium binary if the system Chrome channel is absent; no browser is
downloaded automatically. Use `--headed` for a real-GPU capture when headless
renders differently. Record the renderer in the output, including SwiftShader.

Frame matching and comparison need FFmpeg on PATH. Optional schema validation:
`uv run --with jsonschema python validate-schemas.py` (an isolated environment).
`npm run test:browser` exercises a local fixture with real Chrome and FFmpeg.

## Common browser flags

| Flag | Meaning |
| --- | --- |
| `--url URL` | Public http(s) target without embedded credentials |
| `--out DIR` | New/local output location; choose separate folders for concurrent runs |
| `--viewport 1440x900 --dpr 1` | CSS viewport and capture DPR |
| `--selector CSS` | Repeat for each root; capture includes descendants, including split text |
| `--headed` / `--executable PATH` | Browser visibility / Chromium executable |
| `--timeout 15000` | Navigation/action timeout in ms |
| `--boot-ms 1000` | Declared warm-up, **not** an assertion that a loader has finished |
| `--ready-selector CSS` | Assert a visible readiness marker, bounded by timeout |
| `--mirror DIR --offline` | Fulfil known URLs from local files; abort all misses in offline mode |
| `--reduced-motion` | Emulate prefers-reduced-motion: reduce |

Use one folder per run; files with the same names are replaced. Do not point
`--out` at valuable existing files. Browser contexts are fresh, service workers
are blocked so routes are observable, and TLS validation remains enabled.

## Record successful assets, then replay at the original origin

```sh
node mirror.mjs --mode record --url https://example.com \
  --out ./private-study/mirror --observe-ms 3000
node mirror.mjs --mode replay --url https://example.com \
  --mirror ./private-study/mirror --offline --out ./private-study/replay
```

The first pass records the request list (type, status, initiator, encoded
transfer and available decoded sizes) and saves successful GET response bodies
from the target origin. Add repeatable `--origin https://cdn.example` entries
for explicitly scoped asset hosts. `--scroll-end PX --step 450` triggers normal
scroll requests inside the declared scope; it is not a crawler. `--max-bytes`
limits accepted bodies (default 20 MiB; a headerless body must first be read).

`mirror.json` maps exact URLs, including query strings, to content-addressed
blobs. Replay uses Playwright route fulfil at those same URLs and preserves
relevant content/CORS/CSP headers. It does not start a server, rewrite code,
invent missing responses or repair a broken app. Checksums and contained paths
are verified. Only HTTP 200 GET responses are mirrored; redirects follow their
normal live route unless the initial URL already has a recorded body. Range
responses, streams, workers and non-GET requests are outside this replay model.
`--offline` exposes missing dependencies instead of silently fetching them.

A failed original request remains failed. Read loading code and the request
list; record what is missing. Never hide a preloader and call that a successful
boot. Record and replay are separate passes. Keep waits bounded and continue
independent analysis if readiness cannot be established.

## Capture screenshots, computed styles and observable 3D state

```sh
node capture-steps.mjs --url https://example.com --out ./private-study/steps \
  --viewport 1440x900 --step 90 --selector body --round-trip
# For your target, specify the scoped end and roots, and a real readiness marker
node capture-steps.mjs --url https://your-reference.example \
  --out ./private-study/reference --start 0 --end 5400 --step 90 \
  --selector '#hero' --selector '#first-section' \
  --ready-selector '.app-ready' --mirror ./private-study/mirror --offline
```

`window.scrollTo` requests each coordinate. Each row records requested/actual y,
settled state, screenshot and JSON paths. All selected elements get stable IDs
for both directions, even when no style is currently animated. Disconnected
nodes are flagged; rerun after responsive re-splitting to establish new IDs.
Computed styles include transform, opacity, filter, clipping, visibility, colour,
font and rect. Captures use PNG and retain the full declared viewport at DPR.
The final position is included even when the step does not divide the range.
The current document height must support the range; a short page has one step.

`capture.json` is checkpointed after every step. Each direction has
`step-0000.png` plus `step-0000.json`. Exit 2 means a requested state did not
settle/reach its target; these rows are retained, never labelled good captures.
`--settle-ms 3000` bounds waiting. A state must stay unchanged for 300 ms within
0.001 numeric precision and reach the target within 1 px. Idle uniforms can
keep it changing: use explicit repeatable `--ignore-uniform u_time` flags only
for diagnosed time channels. Ignored names affect settling; final JSON still
contains them. DOM idle motion can also time out: report it rather than delete
it from the page. Do not use settles as performance measurements.

`hooks.js` runs before page scripts: three.js devtools observation plus WebGL
context, shader/program pairing and draw-call hooks. It observes render calls
to find cameras and scenes. Output includes world transforms, material uniforms,
lights, bones and clip metadata when exposed. A missing observation channel
means **unknown**, not no 3D. Custom animation playback time cannot be recovered
without an exposed channel. Worker-owned canvases are not covered. Shader text
is held in bounded browser memory for private inspection and omitted from JSON.
Heartbeat draw counts include post passes and are instrumentation estimates;
use an uninstrumented trace for performance.

## Fit wheel and keyboard response separately

```sh
node scroll-physics.mjs --url https://example.com --out ./private-study/physics \
  --wheel 100,300 --key PageDown --key ArrowDown --selector body
```

Uses trusted Playwright input and rAF samples. `--start` chooses an initial y;
`--duration-ms 2600` bounds each trace. A first-order exponential candidate is
fit in seconds after input onset, with RMSE. No movement, an unsettled endpoint
or an instantaneous jump has no valid follower fit. A transformed wrapper is
logged but is not mistaken for native scroll. A fit is evidence for a model,
not proof of the source implementation or its exact input friction.

## Find candidate video-frame matches

```sh
node frame-match.mjs --video ./reference.mp4 \
  --steps ./private-study/reference/forward --out ./private-study/matches --fps 1
# Or supply timestamped frames already extracted by watch
node frame-match.mjs --frames ./reference-frames \
  --steps ./private-study/reference/forward --out ./private-study/matches
```

Requires exactly one of `--video` / `--frames`. FFmpeg exports at most 1,000
resampled frames and records their presentation timestamps; supplied image
folders have unknown timestamps rather than invented times. `--top 3` retains
alternatives. Matching is independent for every frame, so a recording can move
backwards. `--start-y` and `--step` infer legacy filename coordinates only when
per-step JSON is absent. This assumption is recorded.

**Dark frames and low-resolution similarity can give a confident wrong match.**
We warn on dark/low-detail images and small top-score gaps. Inspect native-size
anchor frames and compare property curves before classifying a driver. The
Oryzo study's 32×20 greyscale matches were not reliable causal evidence.

## Compare matching scroll steps

```sh
node compare.mjs --reference ./private-study/reference/forward \
  --candidate ./private-study/rebuild/forward --out ./private-study/compare \
  --caption 'Reference site by its creator / our original study'
```

Pairs numeric `step-N` identities (three/four digit padding may differ), reports
missing/extra candidates, rejects unsettled/unreachable rows, and rejects unequal actual y when both metadata files
exist. For legacy JPEGs, supply `--start-y` / `--step`. It writes comparison.json
and side-by-side PNG sheets, `--sheet-rows 4` pairs per sheet. Original inputs
remain untouched. Credit reference material in captions before sharing.

The metric follows `media/fidelity/score.py`: 480×300 greyscale, primary Sobel
gradient magnitude SSIM (`structure`) and secondary luminance SSIM (`luminance`).
Both use 7×7 uniform windows, sample covariance, K1=.01/K2=.03, cropped borders;
the edge data range is the pair's maximum gradient. The Node pipeline uses
FFmpeg Lanczos instead of Pillow Lanczos, so results are **not bit-identical**
to the case figure. JSON records these details. Do not mix scorer backends in
one series. Alpha is composited onto white; captures should be opaque.

A score is not a percentage of fidelity. Palette changes can reduce luminance
similarity while silhouette remains close. Dark holds can exaggerate similarity.
Native-size inspection and measured animation curves remain necessary. Sheets
are browser-rendered report artifacts, not visual verification of a rebuilt app.
