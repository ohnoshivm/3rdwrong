---
title: Engine validation
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:3w-engine-validation
department: labs
sub_department: house-engine
job: engine-validation
role: lead
trigger: ""
kind: repo-skill
availability: repo
distribution: repo
source: skills/3w-engine-validation/SKILL.md
invoke: "3w-engine-validation skill"
pairs_with: [skill:web-technique-to-skill, skill:3w-effect-study, skill:3w-labs-benchmark]
---
# Engine validation

The studio's lead tool for engine validation: the Labs gate a house-engine kit passes before projects may use it. Registered job lead; the skill remains experimental.

## What it does

- Checks API and README, dependency and asset licences.
- Runs the D-0023 budget on the reference phone and desktop (five runs, medians).
- Forces low pixel ratio, throttled CPU, WebGL off and reduced motion.
- Checks keyboard, focus, text alternatives and the browser matrix; installs the kit from its README only.
- Returns one verdict: validated, validated with conditions, or not validated.

## When to use

- A kit from an adopted effect study or `skill:web-technique-to-skill` is proposed for the house engine.
- A validated kit's dependencies or API change.

## When not to use

- To approve a client site — use the launch-readiness checklist.
- To compare options — use `skill:3w-labs-benchmark`.
- To judge creative fit for a project.

## Inputs it needs

- Kit path, version, API and README.
- Source technique card or benchmark.
- A neutral demo page.
- Dependency list with licences.

## How to run it

1. Collect the inputs; keep client and prospect details in the vault.
2. Run the skill and return its exact output structure.
3. Have someone other than the maker review the result.
4. File the output where the skill says; act on blockers first.

```text
Use the 3w-engine-validation skill on {{kit}} v{{version}} at {{path}}. You did not build this kit. Run every check, record device, tool and run count, and return the validation record with one verdict.
```

## What good output looks like

- Every check row has evidence or is marked not tested.
- Conditions of use specific enough to enforce in a project.
- A re-validation trigger.

## Quality checks

- [ ] Validator is not the kit's maker.
- [ ] Reduced-motion and no-WebGL states observed.
- [ ] All licences listed.
- [ ] Budget figures have device, tool and run count.

## Pairs with

- Upstream: `skill:3w-effect-study`, `skill:web-technique-to-skill`, `skill:3w-labs-benchmark`.
- Downstream: project use, recorded in the project's `decisions.md`.

## Limits and cautions

- Lab measurements only; a kit has no field data.
- Experimental skill; the Engineering lead accepts the verdict and the founder approves additions to the house engine.
