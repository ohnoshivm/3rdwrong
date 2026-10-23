---
title: Quality Lab
type: guide
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# Quality Lab

Test quality before a client sees it. This is 3RDWRONG's proposed internal
measurement system for studio work and the tools used to produce it.
Inventory, installation, source review and a registry lead label are not
performance evidence. A successful evaluation is not client approval.

**Documented:** the [department registry summary](../studio/departments/registry-summary.md)
records current jobs, leads and human craft gaps. The
[critique protocol](../methods/quality/critique-protocol.md) requires written
verdicts, evidence labels and next actions. **Interpretation:** repeatable
bake-offs can expose stronger candidates and weaknesses before delivery.
**Unknown:** which tools will perform best on real studio work; the committed
runs below are demonstrations only.

## Choose leads by evidence

1. Choose a job and both of its cases. Include the current registry lead(s)
   and credible challengers, using exact registry IDs. Where no lead exists,
   retain the human craft owner; an AI score cannot fill that role.
2. Freeze the same brief, input files, output contract, time allowance, model
   settings and rubric for all candidates. Record tool revision, maker model,
   prompt, runtime settings and elapsed time in the operator log. Run each
   candidate independently without showing competitors' work.
3. Use randomised letter slots. Import strips model/provider names, tool IDs,
   known signatures and self-identification from candidate text. Preserve any
   permitted unsanitised original privately. A separate checker reviews the
   sanitised outputs and runs `check-blinding`; a residual-identity scan and
   packet hash bind that clearance to the exact text. Until clearance, packet
   emission and scoring are refused. Give a judge only `judge-packet.txt` and
   any separately screened, slot-labelled artefact bundle. Do not give the run
   directory, source output names, candidate map, registry snapshot or maker log.
4. Use a different canonical model family from **every** maker. Use the best available model
   at direction/critique gates: Opus, with the `agent:ceo` trigger for flagship
   and own-identity work, as specified in the studio rules. The CLI records
   original model IDs and canonical families, rejecting family reuse across
   provider prefixes, dated versions and supported aliases. Unresolved IDs
   are refused; extend the reviewed resolver before using a new family. It
   does not invoke a model, prove its identity or enforce model availability.
   All supported GPT/Codex versions share `openai/gpt`; all supported Claude
   tiers/versions share `anthropic/claude`; all supported Gemini versions share
   `google/gemini`; supported o-series models share `openai/o`. Changing a tier,
   version, date or routing prefix cannot establish independence.
5. The judge scores every criterion against the concrete 1–5 anchors and
   cites slot/section evidence. Numeric scores measure task performance;
   they never average away a disqualifier, replace critique or approve craft.
6. A human spot-checks the source evidence, all disqualifiers and gate-critical
   findings, plus at least one scored criterion per slot. Record reviewer,
   date and findings in the score file. The judge must not fabricate this
   record. Without it a non-demo run remains provisional on the leaderboard.
7. Freeze scores, then reveal slots. Compare paired cases, failure patterns,
   time and human findings; repeat disputed results with another independent
   judge. Use at least both cases and two bake-offs before proposing a lead
   change. This minimum is a **Hypothesis** calibration rule, not statistical
   proof. Review sample breadth, model bias and repeatability explicitly.
8. Submit a documented routing proposal to the registry owner and founder.
   Never edit the registry automatically. Human-led typography, colour, mark
   and composition decisions remain human-led even if AI assistance scores well.

Re-test a lead after a **tool, model, prompt or material workflow update**,
when a **new credible candidate** becomes available, and at **90 days** after
its last evaluation. Run both job cases again with the incumbent and the new
or changed candidates. Suspend claims of current evidence until completed.
The report flags ageing runs and registry changes; runtime updates/new tools
outside the registry require the operator's re-test log. No script can infer
unrecorded updates.

## Cases and scores

[Case schema](../schemas/eval-case.json) describes
`evals/cases/<department>/<job>/<case-id>.yaml`. There are two cases per job. Every case declares `class: demo | evidence`.
All 32 supplied Stillsoil exercises are `demo`; fictional-brand exercises can
never nominate a registry lead. Evidence requires a separately authored studio
case with fixed, source-grounded anchors and non-client inputs. Its class must
be present in its first commit and remain unchanged throughout history.
Each includes a bounded brief, existing repository inputs, output contract,
four criteria with five concrete anchors each, positive weights totalling 1,
pass bar, disqualifiers and judge instructions. Validate with:

```sh
uv run python scripts/validate.py --check evals
```

The weighted score is `sum(criterion score × weight)` on a **1–5** scale.
The proposed case pass bar is **4.0 / 5** with **zero disqualifiers**.
A score of 4.5 with fabrication fails. Passing a research plan does not mean
the underlying design, product or delivery passed its gate.

Every scored response also includes exactly one written verdict:

- **Strong enough to advance**
- **Promising but structurally unresolved**
- **Technically sound but conceptually weak**
- **Distinctive but commercially inappropriate**
- **Rejected, with explicit reasons**

Use **Documented**, **Interpretation**, **Hypothesis**, **Unknown** exactly.
Unavailable review modes are **Not testable**. Findings use the protocol's
**Blocker**, **Major**, **Minor**, **Observation** severities. The human records
approval separately, with version and date. In a formative review no strategy
or visual approval is implied.

## Run the pipeline

All paths below are repository-relative. The CLI uses this checkout by
default; `--root PATH` before the subcommand supports another repository root.
Candidate IDs must exist in its registry. Commit the public studio case and
its inputs before preparation; all case revisions must declare the same class.
This uncommitted implementation cannot prepare its new cases until the parent
integrator commits them. The runner never commits for you. Evidence bake-offs require at least
two candidates; only demonstrations may have one.

```sh
uv run python scripts/eval_run.py prepare \
  evals/cases/design/concept-critique/text-only-route.yaml \
  --candidates skill:3w-identity-system-critic agent:creative-auditor --demo
# Prints evals/runs/demos/concept-critique/demo-<run-id> as an absolute path.
# Set RUN to that printed path. Produce each output independently first.
uv run python scripts/eval_run.py record "$RUN" --slot A \
  --output path/to/sanitised-report.md --maker-model openai/gpt-4.1
uv run python scripts/eval_run.py record "$RUN" --slot B \
  --output path/to/second-report.md --maker-model google/gemini-2.5-pro
# After a separate checker has reviewed both sanitised slot reports:
uv run python scripts/eval_run.py check-blinding "$RUN" \
  --checker-model anthropic/claude-opus-4-1 \
  --notes "Record the checker's actual identity and signature findings here."
uv run python scripts/eval_run.py judge-packet "$RUN"
# Case authority is the pre-existing commit recorded by prepare.
# Have the run and actual evidence reviewed; the runner grants no approval.
# Full Git history must be available; shallow history is refused.
# Send only the emitted blinded packet and screened slot artefacts to the judge.
# Have the human add their actual spot-check, then import its YAML score file.
uv run python scripts/eval_run.py score "$RUN" \
  --judge-model anthropic/claude-opus-4-1 --scores path/to/scores.yaml
uv run python scripts/eval_run.py reveal "$RUN"
uv run python scripts/eval_report.py
```

`prepare` records the case ID, the full commit SHA of its case revision, the
case snapshot and the exact bytes/hashes of inputs at that commit. It refuses
uncommitted cases or inputs. The commit must be an ancestor of HEAD, full
history must be available, and the case's class must never have changed since
its first commit (including a change followed by a revert). Missing Git,
shallow clones, missing blobs and history/ancestry errors fail closed.

At every command and at leaderboard ingestion, class is read from the case
file at that recorded commit. `demo`, `class`, `case_id`, namespace and ID
prefixes in run/result files are informational consistency fields; disagreement
with the committed case fails validation. Demo IDs use `demo-` and
`evals/runs/demos/<job>/`; evidence IDs use `evidence-` and
`evals/runs/evidence/<job>/`. Results use matching paths under `evals/results/`.
The input inventory and each snapshot hash must equal that case's committed
inputs. The frozen rubric/case bytes must also match. A run uses the recorded
revision even if subsequent inputs change; changing a rubric needs a new run.

Editing every local manifest and hash, moving/renaming a demo, then committing
those edited run files once cannot make evidence: its case at the recorded
commit still says demo. Changing the case's class is rejected by its history.
Pointing at a different case instead makes this a run of that other case,
which must satisfy that case's committed inputs and rubric. Git history is the
studio case authority; no first-commit run ledger competes with it. The old
`evals/provenance/` ledger mechanism has been removed. Trust assumes reviewed
studio case commits; rewriting trusted history or the validator is outside
this guard's scope. Git cannot authenticate a reviewer or prove authorship.

`creation.yaml`, run seals, slot hashes and result digests remain local
consistency checks. `record` accepts one non-empty UTF-8 report per slot,
sanitises it and records its hash, original maker ID and canonical family.
`--artefacts DIR` copies a separately screened source bundle into
`artefacts/<slot>/` and records each file hash. Bundles cannot contain symlinks
or special files. A judge must actually inspect the required artefacts;
missing review modes are Not testable. Scored runs cannot be rescored and
reveal is available only after score import. Corrections require a new run.

The two legacy Stillsoil examples have no committed case reference. Their
original files are preserved under `evals/archive/pre-case-authority/`, outside
active run/result ingestion. They are historical illustrations only, cannot be
resumed, and supply no leaderboard scores. Prepare fresh demos after their
cases have been committed; no commit or re-evaluation is fabricated here.

## Private project runs

Real-project material uses `--project <codename>`. The codename follows
`bin/3w`: exactly two lowercase letter-only words joined by a hyphen (use
neutral words with no identifying meaning). The complete project evaluation
workspace is `~/3rdwrong-vault/<codename>/evals/`, or
`$THREEW_VAULT/<codename>/evals/`. Set the override consistently for all commands.
Place the private case at `evals/cases/<department>/<job>/<id>.yaml` under the
project root; its `inputs` are relative to the private `evals/` directory.
Private case validation uses the repository's schema/registry but writes no
project data there. Private cases do not require public Git commits.

```sh
# Set PRIVATE_EVALS to the existing private project evals directory.
uv run python scripts/eval_run.py prepare \
  "$PRIVATE_EVALS/cases/design/concept-critique/project-check.yaml" \
  --project quiet-harbour \
  --candidates skill:3w-identity-system-critic agent:creative-auditor
# Set RUN to the printed absolute vault path. All other commands are the same:
uv run python scripts/eval_run.py record "$RUN" --slot A \
  --output "$PRIVATE_EVALS/maker-a.md" --maker-model openai/gpt-4.1 \
  --artefacts "$PRIVATE_EVALS/screened-bundle-a"
# Record all slots, run the independent blinding check, then score privately:
uv run python scripts/eval_run.py score "$RUN" \
  --judge-model anthropic/claude-opus-4-1 --scores "$PRIVATE_EVALS/scores.yaml"
```

All case inputs, imported reports, screened artefact bundles, snapshots, slots,
judge packets, scores and results stay within that project's private `evals/`.
The runner resolves symlinks and `..`, rejects case variants of the public
repository path and rejects any Git-worktree vault. Nested run symlinks are
also refused before writing. Project IDs use `project-`; storage uses
`evals/runs/project/` and `evals/results/project/` in the vault. `--root` only
selects the studio repository; it is never a privacy mode.

Preparation appends a record to private `evals/preparations.jsonl` containing
run ID, codename, case hash, timestamp and creation hash. An append-only file
write, lock and fsync preserve previous records; IDs cannot be reused. Later
commands require the matching event. This is a local audit trail, not a
signature or protection from the vault owner editing/deleting the store.
Project runs are always excluded from the leaderboard, which scans only
repository studio results and refuses copied project records. There is no
public-summary publication command; no project material is copied to the repo.

Textual blinding is **best effort** and cannot defeat stylometry or every
semantic clue. Matching uses Unicode NFKC and case-folding, strips invisible
characters, collapses name separators/spacing and recognises common digit
substitutions, plus a small Greek/Cyrillic confusable skeleton. Mixed-script
candidate-like tokens refuse checker clearance. It covers known providers, model families, candidate identities
and the snapshotted studio agent roster. Ambiguous words such as haiku, opus,
sonnet, gemini and codex require model/version/provider or attribution context;
ordinary poetry, manuscript prose and names such as “Claude is my colleague”
survive. Complete model/version/tier signatures are removed together, including
Gemini 2.5 Pro, GPT-6.1 Sol, Claude Opus 5.5 and Haiku 5.5. Normalised matching removes
identified spans while preserving surrounding prose. Human/checker screening
of meaning and external artefacts remains necessary. The enforced guarantees
are recorded maker/judge family separation and the provenance/leaderboard rules,
not proof of complete anonymity or runtime authorship.

A score file has exactly all slots and rubric IDs, with no extras:

```yaml
slots:
  A:
    criteria:
      four-modes:
        score: 4
        evidence: 'Documented: slot A / Findings covers the four modes.'
      findings-actions:
        score: 4
        evidence: 'Interpretation: slot A / Findings links consequence and owner.'
      verdict-gate:
        score: 4
        evidence: 'Documented: slot A / Summary and Next design action.'
      evidence-boundary:
        score: 4
        evidence: 'Unknown: formal craft remains untested in slot A.'
    disqualifiers: []
    verdict: Promising but structurally unresolved
    next_action: 'Designer: supply sketches and real-size tests for formal review.'
  # Add B and every other prepared slot using the same criterion IDs.
# Only the human adds this after actually checking the evidence:
human_spot_check:
  reviewer: named reviewer or role
  reviewed_on: '2026-10-23'
  findings: 'State the evidence actually checked and any score disagreements.'
```

The CLI checks structure, ranges, weights, evidence-label presence and known
disqualifier IDs. It cannot verify the truth of citations, detect fabricated
approval, semantically identify the rejected look, or authenticate a human.
Those checks require the independent judge and human review.

## Read results responsibly

Results live at `evals/results/evidence/<job>/<run-id>.yaml` for evidence, or
`evals/results/demos/<job>/<run-id>.yaml` for demos. They retain the frozen
case, inputs/output hashes, slot/tool mapping, maker and judge models,
criterion scores and evidence, written verdict, next action and human review.
The matching `evals/runs/<class>/<job>/<run-id>/` retains input and output text.
Keep both and the committed case/input history to reconstruct a studio run.
Private project results use the vault paths above and never enter this report.
See [implementation notes](../docs/quality-lab.md).

[Leaderboard](LEADERBOARD.md) groups by department/job. It shows the current
registry lead versus best eligible performer, mean weighted score, runs and
last run, plus **DISAGREEMENT**, **TIE** and **RETEST** flags. Per-tool rows
retain failed attempts in the mean; a tool with any disqualified or failed
run is not eligible for nomination. These conservative rules are proposed.
Means across different briefs or revisions are descriptive only: inspect
paired case/version coverage before choosing a lead. Do not infer that a
single high score establishes general superiority. Registry gaps stay visible.

[Committed Stillsoil demos](demonstrations.md) cover `evidence-synthesis` and `concept-critique`.
Their `demo: true` scores were assigned solely to exercise the pipeline and
are **not quality verdicts, independent blind evaluations or approvals**.
Historical maker model provenance is Unknown. Their archive is excluded from active report ingestion and all quality means
and nominations. No real lead has been validated by these demos.

## Pilot and learning

Use [Pilot Delivery Dry-Run](pilot/README.md) to rehearse a complete Identity
System and Digital Experience with stage scores, time, defects and human
gates. Its readiness index requires actual delivery evidence; these two demos
do not satisfy it. Feed defects into the existing
[skill evaluation](../templates/learning/skill-evaluation.md),
[learning loop](../methods/learning-loop.md) and method-improvement process.

Only studio-owned, public-safe and rights-cleared test material belongs here. Follow
[D-0021](../studio/decisions/0021-client-work-public-anonymised.md) and
[publication rules](../docs/public-private-boundary.md); real client outputs,
identifying combinations, account details and confidential binaries stay in
the private project mode above. Public studio cases require a separate review
for non-identifying, studio-owned content before committing.
