---
title: "Oryzo Red · IMG: GPT image generation"
type: guide
status: experimental
owner: founder
last_reviewed: 2026-10-31
review_every_days: 180
---

# Oryzo Red · IMG: GPT image generation

- Sent: 10-30 23:41 IST
- Provider: codex (ChatGPT account 1)
- Model: gpt-6-luna
- Options: {"reasoningEffort": "medium"}
- Mode: async · Role: design

## Brief (verbatim)

````text
Objective: generate the 2D image assets for a private local web study ("Oryzo Red", a crimson + white recolour of a product site hero) using YOUR built-in image generation tool (GPT image model). Then post-process the images into exact sizes and maps.

FIRST: check that you have an image generation tool. If you do not, STOP immediately and reply "NO_IMAGE_TOOL" with what you have. Do not substitute SVG/canvas/code-drawn fakes and do not call any paid API.

Output folder: <project>/studies/oryzo-red/public/gen/ (create it). Scripts you write go in <project>/studies/oryzo-red/scripts/gen/. Write ONLY in those two folders. Another agent is building the app in the same project; do not touch package.json, src/ or anything else. No git commits. For post-processing use ffmpeg (installed) or a python3 script with Pillow if it is available (`python3 -c "import PIL"`). If neither works for alpha handling, use `uv run --with pillow`.

Art direction shared by all images:
- Photoreal studio product photography, crisp detail, physically plausible.
- Camera: strictly top-down orthographic (looking straight down at a desk).
- Key light: soft daylight from the upper left, gentle falloff.
- Palette: crimson red (#c8102e to #e3141b), warm white (#fff6f4), small neutral metal greys. No other hues.
- No text except where specified. No logos of real brands.

Images (exact final file names and sizes):
1. desk.jpg: top-down surface of a white-washed light oak desk, fine straight grain running horizontally, a subtle warm bounce, no objects, no object shadows. Landscape. Generate as wide as the tool allows, then upscale with lanczos to exactly 3296×1460 (crop to that aspect). Quality 90.
2. Props. Each is ONE object lying vertically (long axis vertical, top of the object at the top of the image), on a FULLY TRANSPARENT background, no cast shadow, filling the frame height with a small margin. Generate as a portrait PNG with transparency, trim to the object, then scale to fit and centre on a transparent canvas of exactly the size given:
   - pencil.png 192×1980: hexagonal wooden pencil, glossy white lacquer body with a small red lettering band (no readable brand), brushed silver ferrule with a red eraser at the BOTTOM, sharpened natural-wood tip with a graphite point at the TOP.
   - pen.png 204×1440: slim ballpoint pen, crimson matte barrel, white cap and clip, silver tip pointing up.
   - cutter.png 288×1536: snap-off utility knife, glossy crimson plastic body, white slider grip with chevron ridges, brushed steel blade segments showing at the top, dark grey rubber end cap at the bottom.
   - eraser.png 270×420: rectangular white vinyl eraser, half covered by a crimson paper sleeve, slightly worn corners.
   - paperclip1.png, paperclip2.png, paperclip3.png, each 150×351: a standard double-loop paperclip, vertical. Clip 1 is crimson vinyl-coated, clip 2 is white vinyl-coated, clip 3 is bare polished steel.
3. gobo_b.png and gobo_c.png, each 512×512, 8-bit grayscale: soft dappled leaf shadows (as if sunlight passes through foliage onto a flat surface), white = light and black = shadow, high-contrast but soft-edged. Two different foliage patterns. Tileable if possible.
4. coaster_diff.jpg 1024×1024: seamless top-down texture of fine-grain agglomerated cork dyed crimson red, natural granule variation, even lighting (it is an albedo map, so no strong shading). Make it tile.
5. video_thumb.jpg 640×360: a candid studio still of a friendly presenter (fictional adult, neutral smart-casual white shirt) holding up a small round red cork coaster toward the camera, in front of a deep crimson backdrop. Large clean white sans-serif wordmark "ORYZO" behind them, partially occluded by their shoulder. Soft cinematic light, shallow depth of field.

Derived maps (a script in scripts/gen/, deterministic and re-runnable): for every prop write <name>_alpha.png (8-bit grayscale from the alpha channel) and <name>_height.png (the alpha blurred with a Gaussian radius of about 6% of the image width, normalised 0–1, 8-bit grayscale). Also write coaster_height.jpg (1024², the coaster_diff luminance with contrast stretched).

Acceptance:
- Every file listed exists with the exact pixel size given.
- Prop PNGs have real transparency: the corners are alpha 0 and the object is opaque.
- Gobos are single-channel grayscale.
- Look at each output once yourself and regenerate any that are clearly off-brief (wrong colours, object not vertical, background not transparent, visible text where none was asked).

Output: a completion report with status, a table of files (name, size in px, bytes), which images were regenerated and why, the prompts actually used, and blockers.
````
