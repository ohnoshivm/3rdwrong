---
title: "Independent QA: {{PROJECT_NAME}}"
type: template
status: experimental
owner: founder
last_reviewed: 2026-10-31
review_every_days: 180
template_for: guide
---

# Independent QA: {{PROJECT_NAME}}

Read {{BUILD_SPEC}}, {{CONTRACT_PATH}}, {{REFERENCE_MAP}}, {{ASSET_MANIFEST}}
and {{BUILD_CHECKPOINTS}}. Own only {{QA_OUTPUT_PATHS}} and {{QA_LEDGER}}.
Start when {{FIRST_SLICE}} runs; continue alongside DOM/GL/IMG workers.
Report defects to owners; do not edit their files. No commits or publishing.

Run {{BUILD_COMMAND}}, {{TEST_COMMAND}}, and the production artifact with
{{SERVE_COMMAND}}. At {{VIEWPORTS_DPR}}, drive window.scrollTo through
{{POSITIONS}} in both directions. Log requested/actual y, settle, pointer and
elapsed-time policy; retain screenshots and console. Compare type, layout,
masks, object/camera/hand pose, blur and glow gating to {{REFERENCE_CAPTURES}}.
Use {{SCORER_AND_PREPROCESSING}} as a candidate aid; inspect dark frames and
native-size anchors manually. Palette/assets intentionally differ: {{DIFFERENCES}}.

Exercise {{POINTER_PATH}}, still-pointer controls, keyboard/focus, resize,
reduced motion, touch where available, blocked asset, timeout and renderer
failure. Verify readiness deadline {{READY_TIMEOUT_MS}} and DOM fallback.
Measure {{PERFORMANCE_SCENARIO}} on {{DEVICE_GPU}} with contention/overhead noted.

| Defect | Evidence | Owner | Severity | Repro | Fix / recheck |
| --- | --- | --- | --- | --- | --- |
| {{ID}} | {{CAPTURE_OR_TRACE}} | {{OWNER}} | {{SEVERITY}} | {{STEPS}} | {{STATE}} |

Final: checks actually run/results, inspected screenshots, open defects,
performance limits and rights exclusions. Unavailable checks say not verified.
