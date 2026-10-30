---
title: "Fidelity method"
type: guide
status: experimental
owner: founder
last_reviewed: 2026-10-31
review_every_days: 180
---

# Fidelity method

We compare 101 paired screenshots: the original at scroll positions 0, 90, …, 9,000 px, and the rebuild at the same positions. Both are reduced to 480 × 300 pixels before scoring. This keeps the comparison focused on the viewport composition rather than on different capture resolutions.

## Primary: structure

Each screenshot is converted to grayscale, then a Sobel filter measures the strength of light-to-dark edges: object outlines, text strokes and boundaries between scene elements. We calculate SSIM between those gradient images. SSIM compares local patterns instead of demanding that every pixel have the same value, so the primary score is less sensitive to the crimson/white palette swap than a direct pixel comparison.

This is still a strict visual comparison, not a semantic one. A different typeface changes letter shapes and therefore edge structure; different copy or text placement also lowers the score. A low score is not hidden or re-labelled as a pass.

## Secondary: luminance

We also calculate SSIM on the grayscale screenshots before edge detection. It gives a broad comparison of brightness and layout. Grayscale removes hue, but not brightness: a red region and a green region can still become different grey values. Treat this as context, not a colour-neutral score.

## Sections and limits

Per-section means use the requested ranges: hero 0–450, ai-pre 450–3,150, title + hand 3,150–4,950, glow hold 4,950–7,200, fade 7,200–8,100, and out of scope 8,100–9,000 px. The ranges are start-inclusive and end-exclusive, except the final range includes 9,000 px. Since samples are 90 px apart, a boundary belongs to the section starting at that boundary.

The rebuild deliberately changes the original colours and Halyard Display typeface to Oryzo Red and Albert Sans. Some text-layer details also differ. The 8,100–9,000 px tail is outside the rebuilt hero/first-scroll scope, so its low values are expected and remain visible in the overall mean. SSIM cannot tell whether differences were intentional, cannot identify objects, and does not establish source-code or behavioural equivalence.

## Capture robustness and hero result

Before each frame is saved, the capture checks that `window.scrollY` equals the requested position and that the app's debug HUD reports the same smoothed scroll position. It also waits for that state to remain stable across animation frames; below y = 450, it verifies that `#hero` intersects the viewport. The y = 0 capture uses a fresh page load with `history.scrollRestoration = 'manual'` set before application scripts run, waits for the preloader, and retries up to three times. A failed guard aborts the run instead of preserving a suspect image.

The corrected hero mean rises from 0.341487 structure / 0.356035 luminance to 0.365768 / 0.382450. It remains below the other in-scope sections for real visual reasons: the rebuild uses a different desk composition with newly GPT-generated props and wood, Albert Sans instead of Halyard Display, and different copy positions. The corrected y = 0 frame fixes the capture error; it does not make those design differences disappear. Overall means move from 0.788654 / 0.707781 to 0.781892 / 0.703095 after recapturing the complete series on the approved snapshot.

`fidelity.json` records every step and the section/overall means and is preserved byte-for-byte from the source publication. The GitHub rebuild JPEGs are downscaled to 960 px wide at quality 80 for delivery; these compressed files are not the original measurement inputs. Original-site captures and full-resolution private study inputs are not included.

`score.py` accepts explicit private `--originals`, `--rebuilds` and `--out` paths. Use the full-resolution capture pairs to reproduce the historical measurement; rescoring compressed delivery JPEGs can change the values. Write new measurements outside this repository. The companion `generate-figures.mjs` reads the preserved values to draw `f08-fidelity.png`.

```sh
uv run --with numpy --with pillow --with scikit-image python motion-teardown/media/fidelity/score.py \
  --originals /private-study/originals --rebuilds /private-study/rebuilds \
  --out /private-study/fidelity.json
```
