---
title: Stillsoil pipeline demonstrations
type: guide
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# Stillsoil pipeline demonstrations

**Documented:** two end-to-end CLI demonstrations reuse existing fictional
Stillsoil outputs byte-for-byte. Both are `demo: true`. **Interpretation:**
they illustrate the earlier pipeline format; current behaviour is covered by
the CLI regression suite. **Unknown:** real output quality,
independent judge agreement, human approval and delivery readiness.

The implementation agent (`gpt-6.1-sol`) assigned these illustrative values to
exercise weighting and report formatting. This was **not an independent
quality assessment**. Historical maker model is `historical-unknown`; no human
spot-check is recorded. The model difference field does not prove historical
maker/judge separation, so the demonstrations cannot enter lead evidence.

## Sources and attribution

- Synthesis: [existing output](../projects/examples/stillsoil-atelier/discovery-synthesis.md),
  attributed to `3w-brand-discovery` version 0.2.0 by the
  [existing skill evaluation](../projects/examples/stillsoil-atelier/brand-discovery-evaluation.md).
  Output SHA-256: `fd456d8a61dc03d82f5a59af80d3c8261f69fe63989ea72ae2bfee569ea12311`.
- Critique: [existing output](../projects/examples/stillsoil-atelier/identity-system-critique.md),
  attributed to `3w-identity-system-critic` version 0.2.0 by the
  [existing skill evaluation](../projects/examples/stillsoil-atelier/identity-system-critic-evaluation.md).
  Output SHA-256: `5703afefb6c5bd3ab66fbe23ab2de42f068db886ef67e99a3246689e5273581a`.

Those source documents establish within-repository skill provenance, not the
historical model, runtime settings or independently measured quality. No
challenger output was invented. A single candidate is permitted only because
these are pipeline demonstrations; a live bake-off needs multiple candidates.

## Stored records

These are archived historical examples, excluded from active run validation
and leaderboard ingestion. They predate committed case authority and have no
valid case commit reference. Their original files are preserved unchanged;
they cannot be resumed or scored with the current runner. Prepare a fresh run
after the demo cases have been committed by the parent integrator. No case
commit, evaluation or checker clearance has been invented for this migration.

Synthesis run: `evals/archive/pre-case-authority/runs/demos/evidence-synthesis/demo-stillsoil-synthesis-demo/`.
[Result](archive/pre-case-authority/results/demos/evidence-synthesis/demo-stillsoil-synthesis-demo.yaml): criterion
values 4, 4, 3, 4 under weights 0.35, 0.30, 0.20, 0.15 produce **3.80 / 5**.
This is an example score, not a judgement of the source output.

Critique run: `evals/archive/pre-case-authority/runs/demos/concept-critique/demo-stillsoil-critique-demo/`.
[Result](archive/pre-case-authority/results/demos/concept-critique/demo-stillsoil-critique-demo.yaml): four illustrative
4s produce **4.00 / 5**, meeting the arithmetic pass condition only. This is
not a quality pass, approval or readiness decision.

Each run contains the frozen case, numbered input snapshots, slot A output,
operator-only `run.yaml`, `judge-packet.txt` and `demo-scores.yaml`. The packet
has no candidate tool ID or maker-model field; a content-screening review
remains necessary in any live blind test. The stored verdict field is an
example of the protocol format, with pipeline-only meaning declared in both
the run and every scoring rationale.

## Commands exercised

The implementation originally executed this sequence for each of the two jobs.
These historical commands predate class-specific storage and the separate
blinding-check gate. The stored runs have since been migrated to the paths
above, retaining their original artefacts and scores. Migration added class
ledgers and hashes; it did not rerun or independently clear these packets.
Use the current [operating guide](README.md) for a new run:

```sh
uv run python scripts/eval_run.py prepare \
  evals/cases/strategy/evidence-synthesis/discovery-synthesis.yaml \
  --candidates skill:3w-brand-discovery --demo --run-id stillsoil-synthesis-demo
uv run python scripts/eval_run.py record \
  evals/runs/evidence-synthesis/stillsoil-synthesis-demo --slot A \
  --output projects/examples/stillsoil-atelier/discovery-synthesis.md \
  --maker-model historical-unknown
uv run python scripts/eval_run.py judge-packet \
  evals/runs/evidence-synthesis/stillsoil-synthesis-demo
uv run python scripts/eval_run.py score \
  evals/runs/evidence-synthesis/stillsoil-synthesis-demo \
  --judge-model gpt-6.1-sol \
  --scores evals/runs/evidence-synthesis/stillsoil-synthesis-demo/demo-scores.yaml
uv run python scripts/eval_run.py reveal \
  evals/runs/evidence-synthesis/stillsoil-synthesis-demo
uv run python scripts/eval_report.py
```

For the critique, the corresponding case is
`evals/cases/design/concept-critique/text-only-route.yaml`, tool
`skill:3w-identity-system-critic`, output
`projects/examples/stillsoil-atelier/identity-system-critique.md`, and run
`evals/runs/concept-critique/stillsoil-critique-demo`.

To repeat with the current committed-case format,
choose a new `--run-id` and point subsequent commands to the new run. Create
its demonstration score file after inspecting the emitted packet. Live runs
must use actual maker provenance, a genuinely different judge model and an
actual human spot-check before the report treats scores as quality evidence.
