---
title: "6. Assets: make the replacements usable"
type: guide
status: experimental
owner: founder
last_reviewed: 2026-10-31
review_every_days: 180
---

# 6. Assets: make the replacements usable

Use `build-agent-images.md`. Check the requested generation tool exists first;
return `NO_IMAGE_TOOL` for that lane if absent. Do not substitute code drawings
or charge a new API without authorisation. Record the prompt and tool used.

For each asset specify path, exact dimensions, aspect, orientation, camera,
light direction, palette, alpha, colour space, map meaning and licence/source.
Remove ambiguity between an atlas and a single sprite. Derived maps must name
their recipe and limits: blurred alpha is an approximation, not measured depth.

View every generated result. Validate dimensions, genuine alpha in corners,
object opacity, no unwanted cast shadow, and greyscale maps. Regenerate failures.
Store a manifest and deterministic map recipe. Do not take original models,
textures, animation data or fonts into a public build without an independent
licence. Never link the private mirror from a public app.

Exit: manifest with provenance, verified files and known substitutions. Until
then use correctly sized, explicitly temporary placeholders with error handling.
