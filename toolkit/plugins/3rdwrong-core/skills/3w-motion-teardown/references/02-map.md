---
title: "2. Map: give each observation a coordinate"
type: guide
status: experimental
owner: founder
last_reviewed: 2026-10-31
review_every_days: 180
---

# 2. Map: give each observation a coordinate

Use the teardown brief and motion-plan template. Bound the study by named
sections; a brief look past the end may establish the boundary, not broaden it.
Define desktop, tablet and mobile viewports with DPR and device/GPU mode.

Create an effect ID per mechanism, a section list, provisional scroll ranges
and a recording-time-to-state table. Mark all video-only numbers `inferred`.
Do not assume a library, asset format, timeline object or monotonic recording.
Distinguish input, logical progress, actual native scroll and rendered state.

Use `schemas/scroll-map.schema.json` for the reconciled map. Coordinates must
name their unit: CSS px, viewport heights, section scalar or seconds. Preserve
reference viewport and section top with each conversion. A scalar may exceed
one; normalised effect progress alone is clamped to [0,1].

Exit: questions for A/B/C, owned output paths, capture range and acceptance
positions. Share read-only evidence paths, never concurrent write access.
