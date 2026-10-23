---
name: 3w-labs-benchmark
description: Design and run a reproducible Labs research benchmark that compares techniques, libraries, models or workflows on a stated question, with fixed fixtures, repeated runs, recorded environments and evidence-labelled conclusions. Use to choose between options before house-engine or project use; do not use for a single project's release gate or to publish rankings as fact.
metadata:
  type: skill
  status: experimental
  owner: founder
  last_reviewed: 2026-10-23
  version: 0.1.0
---
# 3w-labs-benchmark

## Purpose

Answer a comparative question ("which of these is better for this use, at what cost?") with a protocol another person could rerun and get the same answer. Benchmarks feed Labs decisions; they are not marketing claims.

## When to use

Use when Labs or Engineering must choose between two or more options: rendering approaches, animation libraries, image formats, build tools, AI models or workflows for a studio task. Use before a choice is written into the house engine or a method.

## When not to use

Do not use as a project's performance gate; that is `skill:3w-engine-validation` for kits and the [launch-readiness checklist](../../methods/quality/launch-readiness-checklist.md) for sites. Do not benchmark a single option against nothing. Do not run vendor benchmark suites you have not read.

## Inputs

- The decision the benchmark informs and who makes it.
- Two or more options with versions and licences.
- A fixture: the smallest realistic task each option performs (a page, a scene, an image set, a prompt set).
- The metrics that matter to the decision and the threshold that would change it.

## Dependencies

Read the [experiment template](../../templates/learning/experiment.md), the [experiments guide](../../experiments/README.md) and, for web metrics, [web standards](../../methods/quality/web-standards.md). Statistical challenge may use `agency:academic-statistician`. No paid tool is required; a tool that cannot run is recorded as not run.

## Procedure

1. Write the decision, the question and a falsifiable hypothesis. Name the result that would change the decision before measuring.
2. Fix the fixture and inputs. Store them in `experiments/<benchmark>/` with provenance; no client material.
3. Record the environment once per machine: hardware, OS, browser or runtime, versions, network profile, power state.
4. Run each option at least five times per environment, alternating order. Warm-up runs are discarded and stated.
5. Report medians and spread (min, max or p5/p95). Do not average away outliers; explain them.
6. For quality metrics that need judgement (image fidelity, output usefulness), blind the options and use a written rubric scored by someone who did not build the fixture.
7. Compare against the stated threshold. Label the conclusion Documented (measured here), Interpretation, Hypothesis or Unknown.
8. State the limits: environments not tested, fixture bias, version drift. Set a re-run date when versions change.
9. File the result and link it from the method or kit it informs.

## Evidence requirements

Every number has an environment, version and run count. Vendor claims are quoted with source and date, never merged with own measurements. Model or tool comparisons record prompt, settings and date.

## Output

```markdown
# Benchmark: {{question}}

**Decision informed:** {{decision, owner}} · **Date:** {{date}} · **Status:** experimental
**Hypothesis:** {{…}} · **Decision threshold:** {{…}}

## Options
| Option | Version | Licence | Notes |
| --- | --- | --- | --- |

## Environment
{{hardware, OS, runtime, network, power}}

## Results (median, spread, n)
| Metric | Option A | Option B | Unit |
| --- | --- | --- | --- |

## Conclusion
{{label}} — {{answer to the question}}

## Limits and re-run trigger
```

## Quality checks

- The decision threshold was written before results.
- Fixtures and scripts are in the repo and rerunnable.
- Spread and run count are shown for every metric.
- Judged metrics were blinded and scored by a non-maker.
- No client data or identifying material is in the fixture.

## Failure conditions

Stop when options cannot be run on the same fixture, when versions are unknown, or when the question is not tied to a decision. Report "inconclusive" when spread overlaps the threshold.

## Human review

The decision owner reads the limits before acting. Founder approval is needed before a benchmark is published outside the repo.

## Example

**Fictional example.** Labs compares two image formats for a fictional gallery fixture of 24 photographs at three widths. Over seven runs on the reference phone, format B transfers 31 % less with no blinded quality loss on the rubric. Conclusion: Documented for this fixture; re-run when encoder versions change.
