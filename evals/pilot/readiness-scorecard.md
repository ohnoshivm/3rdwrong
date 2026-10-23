---
title: Studio Delivery Quality Index
type: method
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# Studio Delivery Quality Index

**Hypothesis:** a complete rehearsal with an index of **80 / 100** or above,
**every stage at least 4.0 / 5**, and all hard gates satisfied is a useful
proposed bar for founder review of readiness for a first real client.
It is not proof of awards, market success or future client satisfaction.

Use [scorecard.yaml](scorecard.yaml) and the [stage crosswalk](stage-matrix.md).
Identity stages total 50% and Digital Experience stages total 50%. Higher-risk
identity craft, prototype, build and QA stages carry more weight. These are
proposed calibration weights; only the founder can adopt or revise them.
Change them before a run, record the version and never tune them after seeing
scores to manufacture a pass.

For each job, calculate its case score as the weighted mean of criterion
scores, on 1–5. A stage score is the arithmetic mean of all mapped applicable
job scores; retain each job and criterion result. For stage weights `w` that
sum to 100 and stage scores `s` on 1–5:

```text
Studio Delivery Quality Index = sum(w × s / 5)
```

For example, a complete synthetic scorecard with every stage at 4 would yield
80. This is an arithmetic example only, not a pilot result. Missing stages
are **not scored**, never zero-filled, omitted or renormalised. If any
required stage/rubric/evidence is absent, the index is **not calculable** and
the delivery is **not ready**. The two archived pipeline demonstrations never
enter the index: they contain no completed stage delivery. A fictional pilot
needs actual stage work and independent human-checked rehearsal scores; those
cases retain `class: demo` and never enter studio leaderboard evidence.

## Hard gates alongside the index

- Every one of I01–I09 and DX01–DX10 has a versioned output, actual elapsed
  time, independently judged rubric scores (fictional Stillsoil cases remain demo) and a recorded human
  spot-check. Every job score is at least its 4.0 pass bar.
- No disqualifier, unresolved Blocker or unresolved Major remains. Minor
  exceptions name a human owner, reason and closure plan. Observations are not
  counted as defects without a reason. A high mean cannot cancel these rules.
- Strategy, concept, visual-system, art-direction, prototype, launch and
  delivery decisions are actually recorded by the human decision-maker, with
  dates/versions and rehearsal-only scope. Approval and receipt are separate.
- Identity proof includes actual-size applications, original editable/vector
  masters, typography/script coverage, colour/contrast/production conditions,
  rights and an opened asset library. Untested in-scope production constraints
  prevent a production-ready claim.
- Digital evidence includes a passing production build and meaningful tests,
  actual three-width/browser/interaction inspection, clean console,
  accessibility and complete reduced-motion/static fallback checks.
- D-0023's lab/transfer/frame/fallback tests pass on a named mid-range mobile
  profile. Mobile field p75 LCP/INP/CLS remain explicitly not verified until
  field data exists; a human accepts the collection plan and owner. Never
  replace INP with TBT or invent p75 evidence from synthetic or lab samples.
  A looser budget requires the founder's written exception and prevents an
  unqualified claim of meeting the default budget.
- Security, dependency/rights/AI-final consent rehearsal, launch rollback,
  acceptance/receipt, ownership, 30-day warranty simulation, care choice and
  access-removal checks are complete using the delivery/launch checklists.

## Decision record

Record index, all individual job/stage scores, hard-gate results, open defects,
uncertainties and next action in the run log. The independent reviewer may
recommend advancing; the founder records the actual readiness decision.
The exact [critique verdict](../../methods/quality/critique-protocol.md) remains
separate from this operational decision.

**Unknown:** the current index. The committed scorecard has null scores and
no executed stages. No claim of client readiness is supported by it.
Calibrate weights and the pass bar after the first fully evidenced pilot,
retaining failed runs and their lessons. Re-run affected stages after any
material method/tool change; do not reuse a stale score for new output.
