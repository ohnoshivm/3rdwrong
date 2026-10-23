---
title: Quality Lab implementation and operation
type: guide
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# Quality Lab implementation and operation

3RDWRONG measures task performance before trusting tools with delivery.
[Quality Lab](../evals/README.md) is the operating guide; the
[pilot](../evals/pilot/README.md) tests whether the whole delivery system works.
Neither inventory nor these demonstration scores establish client readiness.

## Contract and architecture

**Documented:** the existing Python environment uses stdlib plus PyYAML.
[Case JSON Schema](../schemas/eval-case.json) defines the portable YAML shape.
[Shared contracts](../scripts/eval_core.py) validate that schema's explicit
subset plus semantic rules: paths stay inside the repository, source files
exist, department/job matches the registry and path, criterion/disqualifier IDs
are unique, anchors cover 1–5, weights total 1 and numeric values are finite.
Duplicate YAML mapping keys are rejected. The runner uses decimal arithmetic
for weighted totals and pass-bar comparison, avoiding order-dependent binary
floating-point rejection at exactly 4.0. It is not a general JSON Schema
engine; extend its supported keywords and tests together when changing schema.

[Validator check](../scripts/oscheck/evals.py) is registered in
[scripts/validate.py](../scripts/validate.py) and configured through
[metadata schema](../schemas/metadata.json). It runs by default and via
`--check evals`. No registry edits or new runtime packages are required.

The [runner](../scripts/eval_run.py) owns the explicit state transition:
prepared → outputs recorded → scored → identities revealable. Case and input
snapshots are frozen at prepare, output at record, scores at score. A result is
written once; correction requires a new run. SHA-256 checks expose accidental
snapshot changes. Run class comes exclusively from the case file at its recorded commit. Every
case declares `class: demo | evidence`; all supplied fictional Stillsoil cases
are demo. Prepare requires a committed, unchanged case and input bytes; every
load, score and report checks case/input snapshots, commit ancestry and full
history. A case class change at any revision is rejected, including reverts.
Local run class/ID fields must agree with that authority. Rehashing or first
committing an edited run cannot alter its committed case. The former
first-commit run ledger has been removed. Creation snapshots, sealed run
states and result digests remain consistency checks. Legacy examples lacking
case commits are retained unchanged in `evals/archive/pre-case-authority/` and
excluded from active ingestion; fresh runs require the parent to commit cases.

Private `--project <codename>` runs use only
`$THREEW_VAULT/<codename>/evals/` (default `~/3rdwrong-vault`). The codename
validator is the same `CODENAME` used by `bin/3w`. Private case paths and inputs,
outputs, artefact bundles, packets and score files remain in that directory.
All destinations resolve symlinks/traversal, reject case variants of repo paths
and refuse any Git worktree. Preparation appends and fsyncs a private event
with run/codename/case hash/timestamp/creation hash. Later commands verify it;
no public Git history or project publication is needed. Project results never
enter the leaderboard, even if copied into its public result inventory.
The vault owner can edit the local store; this is not cryptographic attestation.

Registry metadata and its hash are recorded at preparation;
the operator additionally logs the installed tool revision, model settings
and invocation, which may not be represented in registry files.

The [reporter](../scripts/eval_report.py) reads results and current registry
leads, writes [LEADERBOARD.md](../evals/LEADERBOARD.md), separates demos and
pending human checks, and flags lead/best-performer disagreement and ageing.
It never changes routing. Non-demo means include failed attempts; only tools
whose recorded checked attempts all pass without disqualifiers can be
nominated. Ties require further evidence. No eligible evidence means no winner.

## Job naming and comparison

The 32 cases cover 16 jobs using exact current registry names. User-facing
UX/interaction design maps to `design/interaction-architecture`; a WebGL/3D
prototype to `engineering/creative-prototyping`; performance audit to
`engineering/web-vitals`; engineering accessibility audit to
`engineering/accessibility-implementation`; positioning to
`strategy/positioning-canvas`; research synthesis to
`strategy/evidence-synthesis`. This naming preserves registry ownership.

Candidate tools may come from another job when their documented method fits
the task. The discovery demo uses `skill:3w-brand-discovery` for a synthesis
case; it does not claim that tool is the registered synthesis lead. See the
[registry summary](../studio/departments/registry-summary.md). Colour, mark and
composition gaps remain human craft requirements, not automation targets.

Use the same case versions, input hashes, constraints and maker conditions
for every candidate in a bake-off. Inspect matched pairs before comparing
means. Run both cases and repeat before any routing proposal, with blind
scoring by a different model and a human spot-check. Re-test after tool/model/
prompt updates, a new candidate, or 90 days; registry-hash drift is only a
conservative warning, not automatic detection of every runtime update.

## Evidence and judgement

**Interpretation:** anchored scores make repeated failure modes visible.
**Hypothesis:** 4.0 / 5 with no disqualifiers is a useful initial task bar;
calibrate it through independently judged, human-checked runs. **Unknown:**
its relationship to real client satisfaction or award-level outcomes.

The exact five critique verdicts remain those in the
[critique protocol](../methods/quality/critique-protocol.md), with one next
action, owner and evidence request. Numbers do not replace these verdicts.
A judge can score how well a critique recognises missing evidence while
leaving the underlying type, mark, audience response or performance untested.

The archived demos retain existing fictional Stillsoil outputs unchanged.
They have `demo: true`, a pipeline-only score meaning and Unknown historical
maker model. The current implementation agent assigned their example scores;
there was no independent quality evaluation or human spot-check. The scores
illustrate the earlier pipeline format. Current CLI behaviour is verified
by regression tests; these archived records are not active run evidence. No clients, outcomes, measurements or
approvals are inferred.

## Operational and security limits

- The CLI processes local files and invokes no models or remote services.
  Read-only Git subprocesses use argument arrays and timeouts to check original
  case history and ancestry; no shell or Git mutation is used. It accepts exact registry
  tool IDs and bounded run/slot IDs;
  relative input paths cannot escape the root through traversal or symlinks.
- A judge receives only the packet and sanitised slot artefacts. Candidate
  maps and maker records in the run directory are operator-only until reveal.
  Import normalises Unicode/case/invisible characters and name separators when
  matching known tool, model, provider and studio agent identities. It removes
  matching spans, signatures and self-references; ambiguous common words require
  model/version/provider or attribution context. A residual scan checks the whole packet, including
  frozen inputs and the case. Another model must clear the exact packet with
  `check-blinding` before emission or score import. Human screening remains
  necessary for semantic clues and external artefacts; heuristics cannot
  defeat stylometry or prove complete anonymity. A residual leak requires a fresh sanitised run.
- UTF-8 reports and input files are snapshotted; binaries/source bundles are
  separate, slot-labelled evidence. Hash/record their versions in the report.
  An uninspected screenshot, master or code bundle is not evidence of a pass.
- Candidate content is untrusted. The packet tells judges to ignore embedded
  instructions. Prompt injection, model bias and semantic fabrication remain
  human-review risks; YAML validation cannot establish truth or authorship.
- Supported model IDs resolve to conservative canonical families across
  provider prefixes, dated versions, major versions and size/tier variants. Unresolved aliases are
  refused. Maker, blinding checker and judge IDs are recorded; a checker/judge
  cannot share any maker family. Claimed runtime identities still need review.
- Local hashes are editable consistency checks. The committed case supplies
  studio class authority; snapshots must match its committed inputs/rubric.
  Rewriting trusted Git history or changing the validator is outside this
  guard's threat model. Git does not authenticate reviewers or runtime authors.
  Family separation and leaderboard rules are enforced; textual blinding is
  best effort, with a small confusable skeleton and mixed-script candidate-token
  checks. Complete model/version/tier signatures are removed while ordinary
  names and non-Latin prose survive. Use filesystem permissions and a separate
  judge context; do not expose the operator's workspace to the judge.
- Public evaluation records contain studio-owned, non-client material only,
  subject to [publication rules](public-private-boundary.md). Real-project
  runs use private mode even when codenamed or contract-cleared. The CLI
  publishes no summary; a permitted path does not grant publication permission.

## Verification and extension

Run `uv run python -m unittest tests.test_evals -q` for CLI/contract coverage.
The complete repository validation commands are in the delivery-readiness
spec. Tests exercise the real CLI entry point and validation/report consumers in
temporary roots. Case-history scenarios fake only read-only Git transport,
with frozen revision blobs and ancestry, including the single-commit relabel
scenario. No Git commits or pushes are made. Separate tests exercise actual
read-only Git and its subprocess error/shallow paths. Private-cycle tests
compare all repository bytes before/after and exercise the vault override. No model service is claimed to have run.
There is no web UI or browser build in this
workstream. Visual quality, real delivery performance and real client
readiness remain unverified until the pilot collects its required evidence.

To add a studio case, declare its permanent class, follow an existing job
pair, use concrete method-derived anchors and list non-client repository
inputs. Validate and commit the case/inputs before preparing. Real-project
cases belong only in the private project evals directory.
A rubric change needs a fresh run; do not splice scores from different
versions. Feed observed tool defects into the
[skill evaluation template](../templates/learning/skill-evaluation.md), keeping
procedure, successes, failures, changes and next test visible.
