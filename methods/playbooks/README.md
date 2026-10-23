---
title: Delivery playbooks
type: guide
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# Delivery playbooks

How 3RDWRONG's eleven departments ([D-0019](../../studio/decisions/0019-organisation-and-loading-policy.md)) run one real project as one studio. The playbooks do not replace the methods: they say **who** does each phase or stage, **with which tool**, **who checks it**, **what file it lands in** and **what the founder decides**. The method files keep the actual steps and checks; read them alongside.

| Playbook | Covers | Method it operates |
| --- | --- | --- |
| [Client lifecycle](client-lifecycle.md) | L0 Lead → L9 Close-out & case study, across Outbound, Sales, Production, Strategy and Marketing | [Client lifecycle](../lifecycle.md) |
| [Identity system](identity-system.md) | The nine identity phases inside L6 | [Identity engagement](../identity-engagement/README.md) |
| [Digital experience](digital-experience.md) | The ten Digital Experience stages inside L6–L8, as a Design + Engineering pod | [Digital experience](../digital-experience/README.md) |
| [Handoffs](../handoffs/README.md) | Contracts and artefact checklists between departments | [Design handoffs](../../studio/departments/design.md#handoffs) |
| [Department heads](../../studio/departments/heads.md) | Head agent, job owners, reviewer pool, escalation and RACI per stage | [Department index](../../studio/departments/README.md) |

## How a project runs through the departments

1. **Growth finds and qualifies** (L0–L2). Outbound and Marketing bring the lead; Sales qualifies and scopes with Strategy, and Design and Engineering confirm feasibility.
2. **Sales and Operations commit** (L3–L4). Proposal, SOW, contract and deposit; the codename and clearance are recorded under [D-0021](../../studio/decisions/0021-client-work-public-anonymised.md).
3. **Production opens the project** (L5). Populate from the identity or digital project bundle using the [workspace rule](#workspace-and-evidence-discipline); Production owns the plan, gate log and status.
4. **The craft departments deliver** (L6). Strategy leads identity phases 01–03; Design leads 04–07 with Engineering from the first digital application; the Design + Engineering pod runs Digital Experience from stage 01. Media produces scoped assets under Design's direction.
5. **Production hands over and cares** (L7–L8), with Engineering for anything live.
6. **Production, Marketing and Operations close** (L9): retrospective, permission check, case study if cleared, final invoice.

Every move between departments uses a [handoff contract](../handoffs/README.md). A stage cannot start until the previous gate is logged in the project README's gate log ([format](../lifecycle.md#gate-log-format)).

## How to read a playbook entry

Each phase or stage has the same fields:

| Field | Meaning |
| --- | --- |
| Objective | One sentence; the method file holds the full purpose. |
| Owner | Department / sub-department that is responsible, and the **owner agent** that does or coordinates the work. |
| Reviewer | The **independent reviewer agent** that checks it. Never the maker, never the maker's own department alone. |
| Lead tools | Registry `id`s from [`toolkit/sources/registry.json`](../../toolkit/sources/registry.json), job lead first. Load a lead before any specialist. |
| Specialists | Registry `id` plus the trigger that justifies loading it. No trigger, no load. |
| Inputs / outputs | Exact workspace files from the project bundle, or the template that produces them. |
| Gate | Founder and client decisions. Strategy approval is always separate from visual or concept approval. |
| Evidence | What must exist before the gate is logged. Mock-ups do not prove production readiness. |
| Failure modes | The ways this phase usually goes wrong in practice; the method file lists more. |
| Duration | **Hypothesis** planning range only, never a commitment. Real dates are set at L5. |

**Documented** — The four craft and twelve gap-closing leads are integrated experimental skills, with routing and invocation in the [tool-card index](../../toolkit/cards/index.json) and source methods in the [skills guide](../../skills/README.md). Web QA is integrated: follow the [`docs/web-qa-harness.md`](../../docs/web-qa-harness.md) guide, [`scripts/web_qa.py`](../../scripts/web_qa.py) implementation, [browser probe](../../scripts/web_qa_browser.js) and [default budget](../digital-experience/qa-budget.yaml) for `bin/3w qa run <url>`. Quality Lab (`evals/`) remains under independent review; its code-formatted paths await integration. Check that the selected tool and its prerequisites are installed before use; routing is not quality evidence.

Read the job's lead instructions first. All proposed ownership and duration assignments in these playbooks are **Hypothesis** until tested; the linked methods and decisions are the **Documented** basis. Common failure modes are risks to test, not reports of client incidents.

## Model routing

The registry decides **which tool**; this table decides **which model** runs it. It mirrors the Design charter's "best model at every gate" rule ([Design quality rules](../../studio/departments/design.md#quality-rules-and-gates)).

| Work | Agent (registry id) | Model | Never use it for |
| --- | --- | --- | --- |
| Flagship concept, own-identity work, consequential critique | `agent:ceo` | Opus, max effort | Routine coding, formatting, research |
| Direction, art direction, critique | `agent:creative-director`; `agency:design-brand-guardian` for identity; `agent:creative-auditor` for rendered digital work | Opus | Building what they will later judge |
| Strategy, hard trade-offs, architecture diagnosis | `agent:strategic-architect` | Opus | Routine implementation |
| Copy where voice matters | `agent:creative-writer` | Opus | Publishing |
| Interface systems and typography execution | `agent:ui-ux-architect`, `agent:visual-designer` | Opus | Final craft decisions on type, mark, colour or composition (human-led) |
| Builds from an approved spec | GPT-6 Luna (primary) or GPT-6.1 Sol (complex) through T3 `delegate_task`; fallback `agent:implementer`, `agent:complex-engineer`, `agent:frontend-architect` | GPT-6 / Sonnet | Reopening approved creative intent |
| Motion and 3D implementation | `agent:motion-director`, `agent:3d-webgl-engineer` | Sonnet | Setting the motion concept (Design's job) |
| Browser QA and measurement | `agent:visual-qa-engineer`, `agent:performance-engineer` | Sonnet | Approving their own fixes |
| Structured lookups and enrichment | `agent:researcher` | Haiku | Interpreting evidence or choosing a direction |
| Repetitive, mechanical work | `agent:bulk-executor` | Haiku | Anything that needs judgement |

Discover current provider/model identifiers and options before routing; the model names above express intended capability, not guaranteed availability. Use one project coordinator, not an additional orchestration system. Existing project instructions choose the stage orchestrator; Operations' planning tools do not override it.

Respect each agent's actual permissions. `agent:creative-director`, `agent:ui-ux-architect`, `agent:strategic-architect` and `agent:ceo` return decisions/specifications; they do not write project files. Production assigns `agent:implementer` to persist their returned work without changing its meaning. `agent:creative-auditor` reviews rendered digital work with supplied captures; it is not a text-route or print critic. For those reviews use an independent `agency:design-brand-guardian` on Opus (or `agent:ceo` when its flagship/own-identity trigger applies) running `skill:3w-identity-system-critic`, with human craft review. If `agent:ceo` made the direction, choose the other reviewer. `agent:performance-engineer` measures and reports; builders make fixes. A reviewer who contributes a fix becomes a maker of that version and needs a new checker.

**Interpretation** — the cheaper the model, the more precise its brief must be. A cheap model that fails costs more than a strong model that succeeds. If the right model is unavailable, record the gap; never lower the gate (Design rule 8).

## Maker ≠ checker

- The agent instance that made an artefact never reviews it. Use a different agent, and for consequential gates a different model family or a human.
- A department never approves its own work alone ([D-0019](../../studio/decisions/0019-organisation-and-loading-policy.md)). Design work gets a Design QA pass **and** a pass from outside Design (Strategy for strategic fit, Engineering for implementation); Engineering work gets Engineering QA **and** a Design QA pass in the browser.
- Two passes on creative work: concept first, then form and implementation ([critique protocol](../quality/critique-protocol.md)). Nothing advances below "Strong enough to advance".
- Every handoff names maker, checker, artefact version, evidence, verdict, unknowns and next owner.

## Pre-client measurement and first-project readiness

Before a job's first client use, run both of its cases in `evals/cases/<department>/<job>/` using the blinded procedure in `evals/README.md`. The stage tables in the pillar playbooks map all 19 stages to the existing 16 job rubrics. Preserve tool/model/prompt versions, time allowance, input/output hashes, criterion scores, disqualifiers, written verdict and human spot-check. The proposed case bar is at least 4.0 / 5 with zero disqualifiers. A judge uses a different underlying model from every maker, sees only the blinded packet and screened artefacts, and never receives the candidate map. A score cannot replace a delivery gate or human craft judgement. Missing evidence is **Not testable**.

`evals/LEADERBOARD.md` contains demonstrations, not proven client readiness. For jobs with no case, record **Unknown: no Quality Lab case**, the independent review and the missing evaluation owner/date in `qa/README.md`; propose a bounded case rather than inventing a score. Re-test after tool/model/prompt/workflow changes, a credible new candidate, or 90 days. Lead changes require paired cases, at least two bake-offs and founder/registry-owner review; never auto-promote from a score.

**Before the first real client**, Production runs `evals/pilot/README.md` with its `stage-matrix.md`, `scorecard.yaml` and `readiness-scorecard.md`: all nine identity phases and ten digital stages, actual timings, original artefacts, independent non-demo scores and human gates. A complete proposed index of at least 80 / 100, every stage and mapped job at least 4.0 / 5, zero disqualifiers and no unresolved Blocker or Major supports founder review; it does not approve readiness. Missing stages prevent calculation. Record the fictional scope extension and simulated launch, receipt, warranty and care as rehearsal-only. No real consent or elapsed 30-day service is implied. The founder must explicitly accept readiness before client delivery begins; this documentation does not record a completed pilot.

## Workspace and evidence discipline

Use [the bundle sources](../../templates/bundles/README.md) for real filenames. `bin/3w new` creates files exclusively and refuses an existing project workspace. At L2–L4 private discovery, proposal and scope records may already create the codename folder. At L5, inspect both repository and vault first: when either target exists, populate only missing workspace files from `templates/bundles/project-identity/workspace/` or `templates/bundles/project-digital/workspace/`, rendering documented placeholders and fixing private-copy links. Retain existing records, dates and clearance. Do not delete or rename a real codename to make the CLI succeed. Run `bin/3w check` on public records. Use `new project-*` only for a genuinely new target.

For a combined engagement, keep one workspace and gate log with both I01–I09 and DX-01–DX-10. Extend its QA/handover sections from the other bundle's source templates; do not run a second project bundle over it. All short filenames in the playbooks are relative to `projects/<codename>/` for cleared projects, or `<vault>/<codename>/` for private ones. New method artefacts are explicitly distinguished from bundle-generated files. Private records use vault filenames rather than links from public pages.

## Founder gates

Only the founder (and the client decision-maker `C1` where marked) approves. Agents recommend; tools never mark anything approved.

| Gate | Founder decides | Client `C1` decides |
| --- | --- | --- |
| L1 | Pursue or decline | — |
| L2–L4 | Scope is deliverable; proposal may be sent; contract signed | Scope summary; proposal; contract and deposit |
| Identity 03 | Strategy is ready to present | **Strategy sign-off** (dated version) |
| Identity 04 | Route to recommend | Route for development |
| Identity 06 | System is ready to present | **Visual sign-off**, separate from strategy |
| DX-02, DX-03, DX-04, DX-08 | Concept, art direction, prototype and budgets, launch | Each, as marked in the [Digital Experience playbook](digital-experience.md) |
| L7–L9 | Release, care scope, retro actions, publication | Final acceptance; receipt and access (separately); case-study permission |

Human-led craft: type, mark, colour and composition decisions are made by a person. AI explores, prepares variations, tests and checks.

## Studio defaults every playbook applies

- [D-0023](../../studio/decisions/0023-commercial-and-delivery-defaults.md): 50 / 30 / 20 payment split; two consolidated feedback rounds per phase; 30-day warranty; AI use disclosed, AI-generated finals only with written client consent; the Digital Experience performance budget (mobile p75 LCP ≤ 2.0 s, INP ≤ 200 ms, CLS ≤ 0.1, ≤ 2 MB before first interaction, 60 fps target on a mid-range phone, complete reduced-motion fallback).
- [D-0024](../../studio/decisions/0024-growth-defaults.md): four content channels, 20 hand-written first messages a week, free award submissions only.
- [D-0021](../../studio/decisions/0021-client-work-public-anonymised.md): codenames and roles only in the repository; names, contacts, money, contracts and client files in the vault. Run `bin/3w check` before committing project records.
- [D-0006](../../studio/decisions/0006-rejected-own-identity-direction.md): the rejected look (black backgrounds, heavy grotesk, neon, familiar creative-agency aesthetics) is never a default.
- Before any creative-output task, load the [`3w-taste-graph`](../../skills/3w-taste-graph/SKILL.md) skill and a reference pack, as [AGENTS.md](../../AGENTS.md#creative-reference-packs-and-client-records) requires. Its registered id [`skill:3w-taste-graph`](../../toolkit/cards/design/direction/skill--3w-taste-graph.md) records the creative-output prerequisite without displacing the inspiration-taste lead.

## Related

- [Client lifecycle](../lifecycle.md) and [project operations](../../business/engagement-operations.md)
- [Registry summary](../../studio/departments/registry-summary.md) for every job and lead
- [Template bundles](../../templates/bundles/README.md) for workspace files
