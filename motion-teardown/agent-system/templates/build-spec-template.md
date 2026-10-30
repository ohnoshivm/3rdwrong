---
title: "{{PROJECT_NAME}}: build spec"
type: template
status: experimental
owner: founder
last_reviewed: 2026-10-31
review_every_days: 180
template_for: guide
---

# {{PROJECT_NAME}}: build spec

Evidence report: {{RE_REPORT_PATH}}. Version {{SPEC_VERSION}}. Scope {{SCOPE}}.
Reference {{REFERENCE_URL}} by {{REFERENCE_CREATOR}}. Implementation is original.

## Decisions already made

{{SCOPE_ART_DIRECTION_STACK_ASSET_RIGHTS_BUDGET_AND_APPROVAL_STATE}}
Visual concept: {{CONCEPT}}. Type hierarchy: {{TYPE_SCALE}}. Colour roles:
{{PALETTE}}. Layout, material/light, motion, interaction and responsive rules:
{{DESIGN_RULES}}. Define spacing, radii, shadows, durations/easings as tokens.

## Architecture and ownership (freeze before workers start)

{{STATE_FLOW_ONE_SCROLL_ONE_LOOP_AND_DEPENDENCY_VERSIONS}}

| Owner | Sole writable paths | First checkpoint |
| --- | --- | --- |
| Director / integration | {{SCAFFOLD_CONTRACT_MANIFEST_ENTRY_PATHS}} | Contract and runnable slice |
| DOM | {{DOM_PATHS}} | {{DOM_CHECKPOINT}} |
| GL | {{GL_PATHS}} | {{GL_CHECKPOINT}} |
| IMG | {{IMAGE_PATHS}} | {{IMAGE_CHECKPOINT}} |
| QA | {{QA_PATHS}} | First slice, concurrent with build |

Contract: {{CONTRACT_PATH}}, version {{CONTRACT_VERSION}}, created by director.
Consumers may propose changes; only the owner edits. Never create it yourself
while waiting. State fields, units, axes, scalar formula, timing origins,
readiness deadline {{READY_TIMEOUT_MS}} and disposal follow the contract.

## Motion and assets

{{MOTION_SPEC_PATH}} defines each effect from reconciled facts; {{ASSET_MANIFEST}}
defines exact dimensions, alpha, maps, provenance and fallbacks. Intentional
changes from reference: {{INTENTIONAL_CHANGES}}. Unknowns accepted: {{LIMITS}}.
Images and models must be original or independently licensed for public use.

## Acceptance and hand-off

Prototype {{REPRESENTATIVE_SLICE}} first. Verify production build {{BUILD_COMMAND}},
logic tests {{TEST_COMMAND}}, then run the built artifact {{SERVE_COMMAND}}.
At {{VIEWPORTS_DPR}} capture {{POSITIONS}} in both directions with pointer/time
policy {{CAPTURE_POLICY}}. Inspect type, pose, masks, glow gates and console.
Exercise {{INTERACTIONS}}, keyboard, reduced motion, resize, missing asset and
GL failure. Performance budget {{BUDGET}} on {{DEVICE_GPU}}; measure first.
QA logs {{QA_LEDGER}} while owners fix findings. Effort high for routine code.
Use resume-note.md on route change; stop stale retries. Release: {{RELEASE_SCOPE}}.
