---
title: "Implementation and validation report"
type: guide
status: experimental
owner: founder
last_reviewed: 2026-10-31
review_every_days: 180
---

# Implementation and validation report

Historical source validation record, 31 October 2026. The commands and results below describe the pre-migration study; they are not claims that browser checks were rerun in this repository. The canonical skill now lives in `skills/3w-motion-teardown/` at the repository root, and repository licences govern the migrated publication.

## Delivered

- Installable motion-teardown skill with eight stages, nine on-demand references,
  routing/recovery, separate ownership, progress ledgers and resume policy.
- Fourteen generalised v2 templates, including a TypeScript build contract.
- Three draft-2020-12 schemas, three Oryzo examples and an offline validator.
- Six requested capture/instrumentation commands, shared helpers, a pinned local
  Playwright dependency/lockfile, usage guide and reproducible self-checks.
- Landing page with the approved media slots, credits, study/rights explanation,
  MIT code licence, CC BY 4.0 documentation declaration and third-party NOTICE.

## Checks actually run

Commands below are relative to the repo root. Browser runs used system Chrome
155.0.8059.85, Node 26.11.1 and playwright-core 1.64.1 already present in the
study checkout. FFmpeg was available. The dependency lockfile was generated
with `npm install --package-lock-only --ignore-scripts --no-audit --no-fund` in
scripts/. No new global install was made.

| Check | Command / scenario | Actual result |
| --- | --- | --- |
| JavaScript syntax | `node --check` on all nine .mjs/.js files | Passed |
| CLI routing | `--help` on all five executable commands | Passed |
| Unit checks | `node agent-system/scripts/self-test.mjs` | Range boundaries, invalid arguments, follower fitting/non-fit cases, SSIM identity/difference, flat Sobel and dark-frame warning passed |
| Schema validation | `uv run --with jsonschema python agent-system/scripts/validate-schemas.py` | Three schemas and examples passed; ID/reference/window/ownership checks and three invalid-instance rejection cases passed |
| Contract type check | Existing TypeScript compiler, `--noEmit --skipLibCheck --strict --lib ES2020,DOM agent-system/templates/contract-template.ts` | Passed |
| Required live smoke | `node agent-system/scripts/capture-steps.mjs --url https://example.com --out agent-system/scripts/_checks/example --viewport 1440x900 --selector body --round-trip` | Two settled captures, forward/reverse at y=0, 15 DOM elements, no console errors; page has no scroll range at this viewport |
| Browser integration | `node agent-system/scripts/self-test.mjs --browser` | Six settled fixture captures at y=0/150/300 in both directions; requested positions and computed transform checked; no console errors |
| WebGL hooks | Fixture creates a WebGL2 context, two original trivial shaders and a linked program | Context and shader/program pairing observed; captured JSON excludes shader source |
| Mirror replay | Browser self-test records the fixture, stops its HTTP server, then replays with offline route fulfil | Document loaded from mirror with network source unavailable |
| Input capture | Browser self-test calls scroll-physics.mjs on the fixture | Wheel moved 100 px; PageDown moved 860 px at the command's 1440×900 viewport. Instant wheel response correctly had no follower fit; key response yielded a candidate fit |
| No-movement handling | scroll-physics.mjs against example.com, wheel100 and PageDown, 600 ms traces | Both reported no-observable-movement; no smoothing constant invented |
| Image decoding | Browser self-test, FFmpeg decode and transparent PNG | Identity scores passed; transparent pixels decode onto white |
| Frame matching | frame-match.mjs on three fixture images and the paired step folder | Each matched its own step with luminance SSIM 1.0 |
| Video extraction | A one-second synthetic fixture MP4, frame-match.mjs --fps 2 | Two frames, timestamps 0 and 0.5 s, both matched the source step; lossy-video score approximately 0.9999 |
| Comparison sheets | compare.mjs on the fixture forward/reverse folders | Three pairs: structure=1.0, luminance=1.0; one PNG sheet generated |
| Rendered inspection | Viewed the example.com PNG and the generated fixture comparison sheet | Captured content and sheet labels/pair alignment visible; no claim about a rebuilt app's design |
| Link/resource checks | Markdown local-link scan, skill relative resource paths, placeholder checks | Only missing link is the intentional media/v01-side-by-side.mp4 slot; all 14 templates contain placeholders; skill resources resolve |
| Scope and rights review | Reviewed authored paths, subprocess argument handling, mirror URL/checksum/path validation and public source exclusions | No captured Lusion code, shader dumps, models or textures copied; no credentials or personal machine paths in authored publication files |

The alpha regression test initially caught an RGB→YUV overlay conversion that
made white RGB 253. The decoder now keeps overlay processing in RGB; the full
browser self-test passed after the fix. Comparison also refuses unsettled or
unreachable per-step metadata rather than scoring those rows as valid states.

Runtime artifacts live under scripts/_checks/ and are ignored by its .gitignore.
They are local verification evidence, not part of the public material.

## Open items and limits

- `media/v01-side-by-side.mp4` remains an intentional slot awaiting the supplied
  recordings. Other editorial/media paths are owned by the parallel writers.
- This pass did not recapture live Oryzo, benchmark a rebuilt app, or verify the
  original site's custom 3D channels with the new tools. The required live smoke
  and original local fixture were used instead. Worker-owned canvases and
  unexposed custom animation clocks remain explicit instrumentation limits.
- Scoring aligns with media/fidelity/score.py on 480×300 greyscale, Sobel SSIM
  and luminance SSIM parameters. FFmpeg and Pillow resampling are not
  bit-identical; JSON and usage docs record the difference. Keep one backend
  per comparison series and inspect native-size anchors.
- The watch skill's upstream URL was not supplied or verified, so the landing
  credits the installed skill by name without inventing a repository link.
  The dependency itself is not bundled; installation uses the reader's existing
  skill collection. REA is linked to its documented upstream.

## Authored file tree

The following tree excludes local _checks/ artifacts and other owners' paths.

```text
publish/motion-teardown/
  README.md
  agent-system/README.md
  agent-system/VALIDATION.md
  agent-system/schemas/README.md
  agent-system/schemas/effects.schema.json
  agent-system/schemas/examples/effects.example.json
  agent-system/schemas/examples/motion-spec.example.json
  agent-system/schemas/examples/scroll-map.example.json
  agent-system/schemas/motion-spec.schema.json
  agent-system/schemas/scroll-map.schema.json
  agent-system/scripts/.gitignore
  agent-system/scripts/README.md
  agent-system/scripts/capture-steps.mjs
  agent-system/scripts/compare.mjs
  agent-system/scripts/frame-match.mjs
  agent-system/scripts/hooks.js
  agent-system/scripts/image-metrics.mjs
  agent-system/scripts/lib.mjs
  agent-system/scripts/mirror.mjs
  agent-system/scripts/package-lock.json
  agent-system/scripts/package.json
  agent-system/scripts/scroll-physics.mjs
  agent-system/scripts/self-test.mjs
  agent-system/scripts/validate-schemas.py
  skills/3w-motion-teardown/SKILL.md
  skills/3w-motion-teardown/references/01-watch.md
  skills/3w-motion-teardown/references/02-map.md
  skills/3w-motion-teardown/references/03-teardown.md
  skills/3w-motion-teardown/references/04-reconcile.md
  skills/3w-motion-teardown/references/05-spec.md
  skills/3w-motion-teardown/references/06-assets.md
  skills/3w-motion-teardown/references/07-parallel-build.md
  skills/3w-motion-teardown/references/08-compare.md
  skills/3w-motion-teardown/references/routing.md
  agent-system/templates/agent-a-static.md
  agent-system/templates/agent-b-runtime.md
  agent-system/templates/agent-c-tokens.md
  agent-system/templates/build-agent-dom.md
  agent-system/templates/build-agent-gl.md
  agent-system/templates/build-agent-images.md
  agent-system/templates/build-spec-template.md
  agent-system/templates/contract-template.ts
  agent-system/templates/motion-plan-template.md
  agent-system/templates/qa-brief.md
  agent-system/templates/re-report-template.md
  agent-system/templates/reconcile-checklist.md
  agent-system/templates/resume-note.md
  agent-system/templates/teardown-prompt.md
```

51 authored files, including this report.
