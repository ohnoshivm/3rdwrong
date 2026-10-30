---
title: "8. Compare: measure the same state"
type: guide
status: experimental
owner: founder
last_reviewed: 2026-10-31
review_every_days: 180
---

# 8. Compare: measure the same state

Drive reference and rebuild with identical viewport, DPR, direction, scroll
coordinates, elapsed-time policy and pointer. For a redesign, write down
intentional differences before interpreting an image score. Capture the built
artifact as well as development mode. Inspect desktop, tablet and mobile.

Use `compare.mjs` for sheets and per-step windowed luminance SSIM. If a case
study supplies a scorer under media/fidelity, use its declared preprocessing
and metric, retaining its identity in the report. Do not compare numbers from
different pipelines. SSIM is a structural indicator, not a percentage of craft
or a proof of causal fidelity. Dark or low-detail frames can score misleadingly.

Inspect native-size anchors and the worst candidates. Check typography, masks,
composition, scroll windows, object/camera pose, glow gates and property curves.
Record each defect, owner, evidence, fix and recheck. Run keyboard/focus,
contrast, reduced-motion, console and missing-asset checks. Measure performance
on a named device/GPU with contention noted; hook overhead invalidates clean
performance claims. Do not optimise without a measured issue.

Exit: actual build/test results, rendered screenshots, exercised interactions,
comparison method, unresolved limits and a rights review. Exclude mirror,
bundles, shader dumps, cookies, personal paths and private archives from public
output. Caption reference frames “{{REFERENCE_SITE}} by {{REFERENCE_CREATOR}}”.
Never call an unrun check passed; say `not verified`.
