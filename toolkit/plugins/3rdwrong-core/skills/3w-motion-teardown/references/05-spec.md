---
title: "5. Spec: freeze the interface before splitting the build"
type: guide
status: experimental
owner: founder
last_reviewed: 2026-10-31
review_every_days: 180
---

# 5. Spec: freeze the interface before splitting the build

Use `build-spec-template.md`, `contract-template.ts` and the motion-spec schema.
Ask the human only when a decision cannot be recovered: scope, art direction,
rights/budget and target stack. Present mutually exclusive choices in one short
multiple-choice request, honour existing decisions, and continue independent
work. Do not ask them to choose routine implementation details.

Record the smallest architecture: one scroll engine, one frame loop, state
flow, renderer boundary, asset routes and dependency versions already present.
Separate observed behaviour from deliberate design choices. Define tokens,
responsive rules, reduced motion, fallback visuals and measurable budgets.

The director creates and owns the contract before launching workers. Other
agents may read it and propose a change; they never recreate or edit it while
waiting. Specify units, time origin, scalar formula, pointer axes, rect space,
readiness timeout, error state, disposal and resize. Reserve each file to one
owner, including package manifest, contract and integration entry point.

Exit: approved decisions where needed, typed contract, asset manifest, ownership,
match positions, failure scenarios and verification commands. Build workers can
start against placeholders while the asset lane finishes; the manifest is fixed.
