---
title: Pilot Delivery Dry-Run
type: method
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# Pilot Delivery Dry-Run

Rehearse a complete Identity System and Digital Experience on the fictional
[Stillsoil brief](../../projects/examples/stillsoil-atelier/brief.md) before
a first real client. Test the delivery system: people, tool routing, craft,
QA, gates and handover. This document is a protocol, not a completed pilot.

**Documented:** existing Stillsoil files contain a discovery synthesis and a
formative critique of one text route, without approved strategy, artwork,
production proofs or a digital build. **Unknown:** end-to-end delivery
quality, elapsed delivery time, real audience response and client readiness.
The [two pipeline demos](../LEADERBOARD.md) do not resolve these unknowns.

## Authority, scope and prerequisites

Read `methods/playbooks/identity-system.md`,
`methods/playbooks/digital-experience.md` and `methods/playbooks/client-lifecycle.md`.
These three playbooks land in the same release as Quality Lab, from the parallel
playbook workstream; merge them together before executing this pilot. They are
integration dependencies, not deliverables of this worktree. Before starting, reconcile their stages/gates with the
[stage matrix](stage-matrix.md), record the playbook versions and escalate
conflicts to the parent integrator/founder. Their release copies were read only on 2026-10-23 to align all 19 names and
gate requirements in the scorecard; no pilot execution is claimed. Recheck
these mappings against the integrated versions before execution. The existing
[identity phases](../../methods/identity-engagement/README.md) and
[digital stages](../../methods/digital-experience/README.md) supply the current
19-stage crosswalk; no stage may disappear during integration.

The original brief excludes a full website redesign. The pilot operator must
record a **fictional rehearsal scope extension** before execution: a complete
identity with label, line sheet and responsive product-finding experience,
plus a sandbox digital release, fallback, handover and care simulation.
Synthetic dimensions in [digital-stress.yaml](../fixtures/digital-stress.yaml)
are evaluation constraints, not vendor specifications. No real brand,
participant, client approval, order or product benefit is created by this
extension. Mark additional language, regulatory and production inputs Unknown
until supplied; never invent regulated label text or research.

Assign actual operator roles: human art/craft owner; Strategy, Design and
Engineering makers; independent checker using another model; Production/time
logger; human gate decision-maker. Use the best available critique model and
the flagship `agent:ceo` trigger under studio rules. A maker cannot be their
own checker. Humans lead type, mark, colour, composition and final judgement.
Use fictional role codes in public logs; private identities and artefacts stay
outside Git where required by [publication rules](../../docs/public-private-boundary.md).

Before creative production, load `skills/3w-taste-graph/SKILL.md` and the
reference pack required by [AGENTS.md](../../AGENTS.md); record principles and
no-copy boundaries. If its prerequisites are unavailable, log that blocker.
This protocol and the existing-output pipeline demos create no new identity
or website and are not a substitute for that creative-production prerequisite.

## Execute every stage

1. Copy the [run log](run-log-template.md) to a new public-safe pilot record;
   keep the raw creative assets and any sensitive information in the agreed
   private/sandbox store. Copy [scorecard.yaml](scorecard.yaml) for this run.
   Record versions, source hashes, actual roles and the fictional extension.
2. Follow I01–I09 and DX01–DX10 in [stage-matrix.md](stage-matrix.md), reading
   the corresponding method and integrated playbook at each stage. Gather the
   required inputs before work. Strategy approval is a hard prerequisite for
   concept development; visual approval is a separate decision.
3. Start a real clock for each maker, checker, revision and gate activity.
   Log UTC start/end, active minutes, wait minutes, rework minutes, tool/model
   settings, deliverable version and evidence location. Never estimate time
   retrospectively as a measurement; label estimates Hypothesis.
4. Produce original stage deliverables, including real editable artwork and
   runnable code where required. Use the smallest representative browser
   prototype before building the full experience. Omit gratuitous 3D; if a
   scene is justified, test target hardware and its full static alternative.
5. Apply every mapped job rubric to the stage output. Freeze a stage-specific
   proposed eval case if its inputs differ from the supplied bake-off case.
   Run the [blinded pipeline](../README.md) with an independent judge and human
   spot-check. For single-delivery pilot scoring, compare two independently
   made candidates/revisions under the same brief; use a new run for each
   revision. Stillsoil uses committed `class: demo` cases; their human-checked scores
   support rehearsal learning only and never leaderboard evidence. A real
   project uses `--project <codename>` and private stage cases, never repo
   snapshots. Neither workflow can promote a fictional exercise into studio
   evidence by changing a run flag.
6. Record criterion scores, sources, disqualifiers, one exact written critique
   verdict, and the next action/owner/evidence. Mark uninspectable modes Not
   testable. Record the stage aggregate and its underlying job scores; never
   hide a weak job in the index. A plan may be well scored while its delivery
   evidence gate remains blocked.
7. Log each defect using the protocol's exact **Blocker**, **Major**, **Minor**
   or **Observation** severity, with affected version/application, source,
   consequence, owner, fix, retest and closure evidence. Blocker stops the
   gate. Major is resolved before sign-off; any method-permitted exception
   needs a named human record, and an unresolved Major still prevents this
   pilot's readiness declaration.
8. The human decision-maker records **advance**, **hold** or **rework** with
   date, version, actual evidence and rationale. This operational gate decision
   is separate from the exact written critique verdict. Route selection,
   strategy, visual sign-off, launch and receipt remain separate. Record all
   rehearsal decisions as rehearsal-only, never real client consent.
9. Fix defects and repeat independent review until the gate is supported.
   Honour D-0023's two consolidated feedback rounds per phase; a further round
   triggers a simulated scope/change decision and is logged as rework, not
   hidden from time. Never erase failed versions or bypass approval by score.
10. At I08/DX09 open the delivery pack, verify formats/rights/access, rehearse
    acceptance separately from receipt, and perform a sandbox release and
    rollback. At DX10 simulate a warranty defect and verify the response,
    monitoring, care choice and access removal. State that this is a
    simulation: it does not prove that a real 30-day warranty elapsed.
11. Compute the [Studio Delivery Quality Index](readiness-scorecard.md) only
    when every required stage has evidence. Hold if hard gates fail. Close
    with lessons and changes using the
    [skill evaluation template](../../templates/learning/skill-evaluation.md)
    and [learning loop](../../methods/learning-loop.md). Set the next test and
    re-test owner/date. Only the founder can accept readiness for a first client.

## Required delivery evidence

Identity: signed rehearsal strategy, compared ideas, human-reviewed type,
colour, mark and composition, original vector/editable masters, actual-size
application tests, supported scripts, rights register, guidelines and opened
export index. Use [identity system testing](../../methods/quality/identity-system-testing.md)
and the [final-delivery checklist](../../methods/quality/final-delivery-checklist.md).
No mock-up is a production proof; vendor evidence absent from a simulated
condition stays unverified and may block the agreed production scope.

Digital: production build and tests; browser inspection at desktop, tablet and
mobile with screenshots and exercised flows; clean console; keyboard/focus,
zoom/reflow, contrast and assistive-technology coverage; reduced-motion and
WebGL-unavailable paths; security/rights/dependency checks; measured transfer,
LCP/CLS lab proxies and frame traces on the named target profile; sandbox
release, rollback and ownership handover. Complete
[web QA](../../methods/quality/web-qa-checklist.md) and
[launch readiness](../../methods/quality/launch-readiness-checklist.md).

D-0023 requires mobile p75 LCP ≤ 2.0 s, INP ≤ 200 ms, CLS ≤ 0.1,
≤ 2 MB before first interaction, 60 fps on a mid-range phone and a complete
reduced-motion fallback. Prelaunch lab results are proxies; field p75,
especially INP, stays **not verified** until real field evidence exists.
Record a field-measurement owner and plan, accepted by the human gate. TBT is
not INP. Synthetic fixture values never become measurements.

Disclose AI process use and rehearse the written-consent check for AI finals;
only an actual client can consent to real final deliverables. Rehearse the
30-day defect warranty, care boundary and account/access removal without
inventing a client, signature, elapsed service period or live production URL.

## Starting state

All 19 stages are **not-run**, with null scores and time in the scorecard.
The pilot is **not ready for a first real client** on this record. The two
existing-output demos prove pipeline mechanics only. Executing this protocol
requires the integrated playbooks, actual craft and engineering work,
independent review and human gates; none is asserted as completed here.
