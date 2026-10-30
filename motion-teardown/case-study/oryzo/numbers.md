---
title: "Every number we measured, with its source"
type: guide
status: experimental
owner: founder
last_reviewed: 2026-10-31
review_every_days: 180
---

# Every number we measured, with its source

Scope: oryzo.ai by Lusion, `#hero` and `#ai`, scroll 0 → 8,100 px at a 1440×900 viewport, measured 30 October 2026, plus our rebuild (Oryzo Red).

## Kinds of evidence

- **code**: read from oryzo.ai's shipped JavaScript.
- **measured**: read from the live page or our build.
- **session**: recorded in the session transcript.

## Source keys

- **F**: our facts sheet for this guide.
- **R**: the reverse-engineering report.
- **S**: the build spec.
- **C**: agent C's notes.
- **GL**: the WebGL agent's QA report.
- **T**: the session transcript.

These are private working files. Numbers are facts we observed. Lusion's code is not reproduced here.

## The recording and the session

| Number | Value | Kind | Source |
| --- | --- | --- | --- |
| Recording length | 12 s | session | F |
| Recording size and rate | 2508×1306 px, 60 fps | session | F |
| Frames extracted locally | 36, at 3 fps | session | F, T |
| Key frames saved | 12 | session | F, T |
| Frames that map cleanly to capture steps | 3 (0.00, 0.33, 0.67 s → steps 0, 3, 10) | measured | R §1 |
| Effects in the first plan | 10 (E1–E10) | session | F |
| Agent briefs written | 11 | session | T, `prompts/` |
| Length of the reverse-engineering brief | about 1,400 words | session | `prompts/02` |
| Questions asked of the founder before the build | 4, in one prompt | session | F, T |
| Session length, recording → zip | 6 h (19:29 → 01:29 IST) | session | F, T |
| Reverse engineering, request → report | about 3 h (20:05 → 23:01), roughly 1 h lost | session | T, F |
| Rebuild, request → localhost | 1 h 47 min (23:34 → 01:21) | session | T |
| Single-agent preloader stall | about 50 min | session | F, T |
| Agent A, launch → report | 24 min (21:23 → 21:47) | session | T |
| Time-boxes given to agents A, B, C | 45, 60, 45 min | session | `prompts/05–07` |
| DOM agent at max effort, launch → first file | about 40 min | session | F, T |
| Metered or pay-as-you-go spend | none | session | F |
| Token counts | not recorded | — | F |

## Engine and libraries

| Number | Value | Kind | Source |
| --- | --- | --- | --- |
| three.js revision | r178, "modified by Lusion" | code | F, R §3 |
| WebGL version | 2 | code | F |
| Device pixel ratio cap | 1.5 (`min(1.5, devicePixelRatio)`) | code | F, R §3 |
| Maximum pixel count | 2560×1440 | code | R §3 |
| GSAP SplitText version | 3.14.2 (the only GSAP code present) | code | F, R §3 |
| App bundle | 1 bundle, 1,097,812 bytes raw, 0 source maps | code | F, R §2 |
| Bundle, pretty-printed | 47,643 lines | measured | R §2 |
| Shader programs dumped | 19 of about 25 (38 GLSL files) | measured | R §2, T |
| Post chain | AA → bokeh (off) → edge glow → bloom → final grade → smudge (off) → card blur | code | F |
| Bloom levels and blur widths | 5; σ 3, 5, 7, 9, 11 | code | F |

## Scroll

| Number | Value | Kind | Source |
| --- | --- | --- | --- |
| Wheel ease coefficient | 12 | code | F |
| Wheel follower, measured | c ≈ 6.8–7.2 per second | measured | F |
| Keyboard follower, measured | c = 12.0 per second | measured | F |
| Wheel clamp per event | 200 px | code, measured | F |
| Arrow keys | ±100 px | code | F |
| Page Up / Page Down | ±1 viewport | code | F |
| Position rounding | whole pixels | code | F |
| Section scalar | `r = 1 + (scrollY − sectionTop) / viewportHeight` | code | F |
| Paragraph reveal rate | about 45 px of scroll per character | measured | R §6 E5 |

## Layout and windows (1440×900)

| Effect | Range (px) | Kind | Source |
| --- | --- | --- | --- |
| `#hero` | 0 → 900 | code, measured | F |
| `#ai` | 900 → 8,100 (8 viewport heights, pinned) | code, measured | F |
| Hero exit | 0 → 450 | code = measured | F, R §5 |
| "ISN'T JUST A COASTER." | in 450 → 1,125; out 2,475 → 3,150 | code ≈ measured | F, R §5 |
| Coaster and camera path | 0 → 4,950 | code | F |
| Hand animation, frames 71 → 115 | 3,056 → 4,950 | code = measured | F, R §5 |
| "Powered by AI*" | in 3,150 → 4,500 | code ≈ measured | F |
| Caption | in 4,050 → 4,950 | code ≈ measured | F |
| "Try to hover hand" | in 4,950 → 5,400 | code = measured | F |
| Edge glow | on 4,950 → 5,400; off 6,750 → 7,200 | code = measured | F |
| Hand fade-out | 7,200 → 8,100 | code = measured | F |
| Captured screenshots | 101, one every 90 px | measured | F, R §5 |

## Text

| Number | Value | Kind | Source |
| --- | --- | --- | --- |
| Stagger start | about 0.3 × normalised index | code | F |
| Stagger window width | 0.4–0.6 | code | F |
| "Powered by AI*" letter slide | 0.25 ex | code | F |
| "Powered by AI*" letter blur | 12.3 px → 0 (0.1 em at 123 px type) | code = measured | F, R §6 E7 |
| `#ai-title` type size | 123 px / 110.7 px line height | measured | R §10 |

## Hero desk and blur

| Number | Value | Kind | Source |
| --- | --- | --- | --- |
| Base photo | 3,296×1,460 px | code | F |
| Prop sprites | 7 (pen, pencil, eraser, cutter, paperclips ×3) | code | F |
| Cells per prop strip | 4 (3 light angles + height map) | code | F |
| Blur curve | proportional to mask³ | code | F |
| Tint mix | 0.8, towards olive | code | F |
| Zoom-out on exit | 5% | code | F |

## Coaster, camera and hand

| Number | Value | Kind | Source |
| --- | --- | --- | --- |
| Camera path | 116 frames | code, measured | R §6 E2, C |
| Coaster mesh | 2,306 vertices, 67,252 bytes | measured | R §6 E2, C |
| Hand bones | 36 (GPU texture skinning) | code | F |
| Hand mesh | 8,441 vertices, 381,334 bytes | measured | R §6 E8, C |
| Hand animation file | 41,812 bytes | measured | C |
| Hand frames played by scroll | 71 → 115 | code | F |
| Finger bands | 4 horizontal mouse-height bands, spring-driven | code | F |
| Edge glow pulse | every 2 s, from the scrollbar position | code, measured | F |

## Weight and performance of the original (M3)

| Number | Value | Kind | Source |
| --- | --- | --- | --- |
| Frame rate | 60 fps locked | measured | F |
| Frame time | p50 16.6 ms, p99 17.5 ms | measured | R §12 |
| CLS | 0 | measured | F |
| LCP | 6.5–7.2 s (gated by the preloader) | measured | F |
| In-scope media | about 2.06 MB, plus the bundle | measured | F, R §11 |
| Agent C's first in-scope estimate, before reconciliation | about 10.9 MB (included a later scene's splats and models) | measured | T (agent C report) |
| Preloader stall point in automation | about 53% | measured | R §2 |
| Boot time with the local mirror | 6–9.5 s | measured | R §2 |
| Mobile renderer pixel ratio | 1.5 | measured | R §13 |

Agent C ran Chrome alongside agent B, so its frame-rate figures are a floor.

## The rebuild (Oryzo Red)

| Number | Value | Kind | Source |
| --- | --- | --- | --- |
| Images generated | 27 | measured | F, T |
| Props generated | 7, each with alpha and height maps | measured | F |
| Original files reused privately | 5 geometry/animation + 6 textures | measured | F |
| Functional tests (GL) | 20/20 pass | measured | F, GL |
| Required screenshots (GL) | 24 (12 positions × 2 widths) | measured | T |
| Frame rate, M3 sweeps | 60 fps average; p95 17.2–17.4 ms | measured | F, GL |
| Shader warm-up before ready | about 250 ms | measured | F |
| First-use stall it removed | 913 ms | measured | F, GL |
| `stage.ready` deadline | settles within 10 s with missing files | measured | F |
| Acceptance scroll positions | 12: y = 0, 270, 900, 1,530, 2,250, 3,060, 3,600, 4,320, 5,130, 6,000, 7,200, 8,100 | spec | S §8 |
| Production JavaScript | about 556 KB minified, one chunk | measured | F |
| Share zip | 4.6 MB, 92 files | measured | F, T |
| Local dev server | 127.0.0.1:5180 | session | F, T |

## Palette (original → rebuild)

| Role | Original | Rebuild | Source |
| --- | --- | --- | --- |
| Cream | `#ffedd7` | `#fff6f4` | F |
| Ink | `#100904` | `#140304` | F |
| Accent | `#dc5000` | `#e3141b` | F |
| `#ai` background | `#4c3e37` | `#5a0c12` | F |
| Glow colours | 4-colour gradient | `#ffd6dc #ff3b3b #ffffff #ff7a8a` | F |
