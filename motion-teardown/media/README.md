---
title: Motion Teardown media and provenance
type: guide
status: experimental
owner: founder
last_reviewed: 2026-10-31
review_every_days: 180
---

# Motion Teardown media and provenance

The GitHub edition includes our rebuild renders, generated imagery and authored diagrams and prompt cards. Original-site screenshots, reference frames, the original prop atlas, raw models, source code and shader dumps are excluded. Side-by-side comparisons with the original appear in the Substack edition; see the live site at [https://oryzo.ai](https://oryzo.ai).

Rebuild render credit: the hand and coaster geometry come from oryzo.ai by Lusion, recoloured. This credit applies to every file in `rebuild-steps/`, `hand-sequence/`, the article rebuild images, f01, f07 and f10. These are our rendered pixels; the underlying geometry is not distributed or relicensed. See [Licensing](../../LICENSING.md) and [third-party notices](../../THIRD_PARTY_NOTICES.md).

[CAPTIONS.md](CAPTIONS.md) supplies figure captions and alt text. [image-audit.json](image-audit.json) lists every retained image, its provenance, SHA-256 and the inspection result. All copied images were visually inspected in labelled contact sheets, with the generated-assets sheet and replaced figures also inspected individually. The audit concerns screenshot pixels, not a transfer of rights in depicted geometry or marks.

## Reproducing the public figures

Use Node 20+, Chrome and the existing `playwright-core` dependency described in the [capture-tools guide](../agent-system/scripts/README.md). No private source-workspace path is discovered automatically.

```sh
node motion-teardown/media/generate-figures.mjs
```

The default command draws f01 (our hero), f06 (our generated props), f07 (our rebuild at eight positions) and f08 (the preserved fidelity measurements). Individual figure identifiers can be supplied as arguments. The seven-prop panel in `generated-props.png` is cropped from the generated-only right-hand panel of the supplied f06; it contains no original atlas pixels. f11 retains the supplied generated-assets sheet, including its generated video thumbnail. `FIGURE_FONT` optionally names a licensed local font; the default uses Arial. `CHROME_PATH` optionally selects a Chrome executable.

The other diagrams and cards are retained from the supplied publication. `cards/render-cards.mjs` requires `REBUILD_ASSET_ROOT` pointing to the creator's own generated images; those separate source images are not included. `article/copy-images.sh` copies only the two included rebuild frames.

## Capture and measurement limits

The 101 `rebuild-steps/step-000.jpg` through `step-100.jpg` images are 960 px wide at JPEG quality 80. The six hand captures and two article frames are compressed copies of our renders. PNGs use an optimised 256-colour palette; measured mean absolute channel error was below 2/255 for every PNG compared with its unquantised input. No new pixels from the reference site were introduced.

`capture-report.json` describes the historical source capture on an Apple M3; it is not a new browser or performance result. `capture-rebuild.mjs` requires a separately running rebuild and writes full-resolution captures, so optimise new captures before committing them. The rebuilt application is not included here.

[fidelity/fidelity.json](fidelity/fidelity.json) is preserved byte-for-byte. Its score inputs were the private full-resolution captures; downscaled delivery images are not identical measurement inputs. See the [fidelity method](fidelity/method.md) before rescoring. The original-site capture set is deliberately absent.
