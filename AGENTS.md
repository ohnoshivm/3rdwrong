# Agent instructions

3RDWRONG OS is the public working knowledge base for a founder-led design-engineering studio with brand identity at the core and digital experience as the second pillar. It holds reviewed strategy, methods, research, templates, and experimental AI skills.

It is not a client archive: client information, personal data, credentials, and confidential material stay outside this repository.

## Retrieval first

Read [`INDEX.md`](INDEX.md) first to locate current knowledge. Then read the closest route below and only its named files; do not load the repository wholesale.

## Using the toolkit

To choose a tool for a task, read [toolkit/cards/index.json](toolkit/cards/index.json), filter by department and job, then open **only the chosen card** and follow its “How to run it” section. Start with the lead; load a specialist only when its trigger applies. Bench and parked tools require an explicit request. Humans can browse [handbook/README.md](handbook/README.md); a pending card is not evidence of readiness.

## Source order

When sources conflict, use this order and flag the conflict for a human:

1. `studio/decisions/` — the decision log wins over other pages; approved D-0018 supersedes D-0001/D-0002, and approved D-0019 governs organisation/loading, D-0020 governs Taste Graph reference packs, and D-0021 governs anonymised client records, D-0022 sets the studio name 3RDWRONG, and D-0023/D-0024 set commercial, delivery and growth defaults, and D-0025 adopts Creative Technology selection and stack records; related proposals and hypotheses retain their statuses.
2. `studio/` — current studio strategy and operating facts.
3. `methods/` — proposed and reviewed ways of working.
4. `intelligence/` — source-based research and design references.
5. `templates/` — reusable starting points, never evidence by themselves.

## Status and evidence rules

- `approved` means a named human has approved the material and the record includes `approved_by` and `approved_on`. Agents never promote material to `approved`.
- `proposed` means awaiting human review; `hypothesis` means plausible and untested; `experimental` means being evaluated; `rejected` means a human rejected it; `superseded` points to its replacement; `reference` records source material without adopting it as policy.
- Never invent clients, results, approvals, research findings, quotations, or statistics.
- Label evidence exactly: **Documented**, **Interpretation**, **Hypothesis**, or **Unknown**. Cite sources for documented claims and keep interpretation distinct from observation.
- 3RDWRONG's visual identity is not approved. A rejected exploration used black backgrounds, heavy grotesk typography, and neon accents. Do not reuse that direction as guidance.
- Everything committed here is public and open source. Never commit personal data, third-party contracts, credentials or NDA-bound assets. Choose a non-public store before collecting client or interview data; follow the [publication rules](docs/public-private-boundary.md). Historical studio pricing hypotheses and the founding source remain public under D-0017, with their evidence/status limits intact. Never add operating rates, prices, deal values, invoices or cash to the repo; `scripts/pricing.py` reads vault inputs and only prints. Keep its output private.

## Department and toolkit loading

Follow [D-0019](studio/decisions/0019-organisation-and-loading-policy.md) and the [eleven-department index](studio/departments/README.md): Craft (Design, Engineering, Labs), Delivery (Strategy, Production, Media), Growth (Marketing, Advertising, Outbound, Sales), Studio (Operations). Read the job lead first and specialists only on their triggers. Bench and parked entries stay in the library; tool inventory is not proof of quality or connectivity.

[toolkit/sources/registry.json](toolkit/sources/registry.json) is the current routing source. VENDOR snapshots live in `toolkit/vendor/`; FETCH uses [pinned commits](toolkit/fetch.yaml); MANUAL setup lives in [toolkit/manual.md](toolkit/manual.md). The v1 Design YAML is legacy scanner input only. See the [registry summary](studio/departments/registry-summary.md), [Third-party toolkit licensing](LICENSING.md#third-party-toolkit) and [notices](THIRD_PARTY_NOTICES.md).

Use `scripts/install.sh --profile full --tools both` after reviewing the [installation guide](README.md#one-command-install). Profiles are `full|design-engineering|growth|studio|minimal`; tools are `claude|codex|both`. Preview with `--dry-run`; `--skip-fetch` omits network fetches; `--uninstall` removes unchanged installer-owned entries. `TOOLKIT_FETCH_TIMEOUT` controls fetch timeout. Skills link to `~/.claude/skills/` or `~/.agents/skills/`, agents to `~/.claude/agents/`, and library entries to `~/.claude/skills-library/3rdwrong/`, without overwriting user folders.

The [Claude marketplace](.claude-plugin/marketplace.json) has 12 plugins. Register with `/plugin marketplace add ohnoshivm/3rdwrong#system/v0.3-departments`, then `/plugin install 3rdwrong-core@3rdwrong` or a named department plugin such as `/plugin install 3rdwrong-engineering@3rdwrong`. See the README for shell equivalents and the [verified command reference](https://code.claude.com/docs/en/discover-plugins). Installation does not approve routing or verify connected services.

## Context router

Read the `INDEX.md` entry first, then open the minimum files listed for the task.

| Task | Minimum files to read |
| --- | --- |
| Choose a technology stack or effect technique | `methods/creative-technology/selection-policy.md`, `methods/creative-technology/selection-matrix.md` |
| Record a stack decision | `templates/bundles/project-digital/workspace/stack-decision.md.tmpl` |
| Choose a tool for a job | `toolkit/cards/index.json`, `handbook/<department>.md` |
| Qualify a lead or run discovery | `growth/sales/README.md`, `growth/sales/qualification.md`, `growth/sales/discovery-call.md` |
| Plan content | `growth/content/README.md`, `growth/content/production-workflow.md`, `taste/README.md`, `skills/3w-taste-graph/SKILL.md` |
| Outreach | `growth/outbound/README.md`, `growth/outbound/compliance.md`, `studio/initial-icp.md` |
| Case study, testimonial or award | `growth/proof/README.md`, `growth/proof/case-studies.md`, `growth/proof/testimonials.md`, `growth/proof/awards.md` |
| Growth metrics | `growth/metrics.md`, `growth/sales/pipeline.md`, `business/scorecard.md` |
| Run a client project | `methods/lifecycle.md`, `business/engagement-operations.md`, `docs/public-private-boundary.md` |
| Deliver a website | `methods/digital-experience/README.md`, `methods/quality/web-standards.md` |
| Check a website build against the studio budget | `docs/web-qa-harness.md`, `methods/digital-experience/qa-budget.yaml`, `methods/digital-experience/07-qa.md` |
| Create a workspace or vault record | `templates/bundles/README.md`, `docs/public-private-boundary.md` |
| Run a project stage | `methods/playbooks/README.md`, then the stage's playbook: `methods/playbooks/client-lifecycle.md` (L0–L9), `methods/playbooks/identity-system.md` or `methods/playbooks/digital-experience.md` (L6), plus the method file it links |
| Hand work to another department | `methods/handoffs/README.md`, the matching contract in `methods/handoffs/`, `studio/departments/heads.md` |
| Launch and hand over | `methods/quality/launch-readiness-checklist.md`, `methods/handover-and-care.md` |
| Price an opportunity | `business/pricing/README.md`, `business/pricing/estimation-guide.md`, `business/pricing/rates-and-estimates.md`, `business/pricing/commercial-rules.md` |
| Write a proposal or SOW | `business/proposals.md`, `templates/bundles/README.md`, `templates/bundles/proposal/bundle.yaml`, `templates/bundles/sow/bundle.yaml` |
| Contracts and IP | `business/legal/README.md`, `business/legal/master-services-agreement.md`, `business/legal/ip-and-licensing.md` |
| Invoice and tax | `business/finance/README.md`, `business/finance/invoicing-and-collections.md`, `business/finance/india-tax-basics.md` |
| Founder review session | `business/review-queue.md`, `scripts/review_queue.py` |
| Creative work references | `skills/3w-taste-graph/SKILL.md`, `taste/graph/README.md` |
| Plan a portfolio project | `studio/portfolio-strategy.md`, `templates/projects/project-readme.md`, `docs/public-private-boundary.md` |
| Run a Brand Direction Sprint | `studio/brand-direction-sprint.md`, `studio/positioning.md`, `studio/initial-icp.md` |
| Start a client identity project | `methods/identity-engagement/README.md`, `templates/projects/project-readme.md`, `skills/3w-brand-discovery/SKILL.md` |
| Perception research (perception-to-identity map) | `methods/perception-to-identity-map.md`, `skills/3w-brand-discovery/SKILL.md` |
| Weekly taste practice | `methods/taste-practice.md`, `methods/learning-loop.md` |
| Calibrate taste / study reference websites | `taste/swipe-file.md`, `taste/discovery-sources.md`, `taste/award-site-teardowns.md`, `taste/studio-websites.md`, `methods/taste-practice.md` |
| Capture a quick note | `inbox/README.md`, `docs/public-private-boundary.md` |
| Add an agency study | `intelligence/README.md`, `templates/research/agency-study.md` |
| Add a design reference | `intelligence/README.md`, `templates/research/visual-system-analysis.md`, `skills/3w-category-code-audit/SKILL.md` |
| Update strategy | `studio/decisions/README.md`, `docs/knowledge-governance.md`, the affected `studio/` page |
| Propose a method | `methods/README.md`, `methods/learning-loop.md`, `templates/learning/method-improvement.md` |
| Improve a skill | the relevant `skills/*/SKILL.md`, `templates/learning/skill-evaluation.md`, `docs/ai-integration.md` |
| Record an experiment outcome | `experiments/README.md`, `templates/learning/experiment.md`, `docs/workflows.md` |
| Critique a design | `skills/3w-identity-system-critic/SKILL.md`, `methods/quality/critique-protocol.md` |
| Capture project lessons | `methods/learning-loop.md`, `templates/learning/retrospective.md`, `docs/public-private-boundary.md` |
| Retrieve context in Claude Code | `INDEX.md`, this file, then the closest task route above |

## Creative reference packs and client records

Before **any creative-output task**, load `skills/3w-taste-graph/SKILL.md` and a reference pack with `uv run scripts/taste_graph.py pack "<brief>"`. State which principles you will apply and which don'ts you will avoid. Treat references as inspiration: never copy layouts, assets, copy or brand identity. If PostgreSQL or the pack is unavailable, stop and report as the skill requires; never claim a pack was loaded when it was not. Read the specific sources needed, not the whole graph. Captured media, third-party text and database backups stay outside Git.

D-0021: client work is public and anonymised **only when cleared by contract**. Use codenames and roles only, never client names, people, contacts, domains, money or client files. Otherwise render the whole workspace into the vault with `--private`. Run `bin/3w check` before committing project records, including the vault deny-list when available. Human review must also check identifying combinations. Never write rates, prices, deal values, invoices or cash into the repo; the pricing CLI reads vault inputs and only prints. Never paste its output here.

## AI and human responsibility

The operating split below is adapted from Founding Blueprint v1.0, 22 October 2026 ([founding source archive](studio/archive/founding-blueprint-v1.0.md)). Reuse the existing multi-model AI environment; do not build another routing system. Write skills in Markdown first; add code only when it improves output or removes repeated work.

| Work | AI contribution | Human responsibility |
| --- | --- | --- |
| Research | Find candidate sources, organise evidence, and draft cited summaries. | Choose the question, verify sources, and judge what the evidence supports. |
| Strategy | Compare evidence and prepare options with assumptions visible. | Set objectives, choose direction, and approve strategic policy. |
| Concepts | Expand possible routes and make alternatives easier to compare. | Lead art direction, judge originality, and select the concept. |
| Production | Prepare drafts and reduce repetitive production work. | Own craft, technical quality, rights, accessibility, and final release. |
| Critique | Check work against criteria and surface gaps or contradictions. | Weigh context, taste, audience fit, and commercial suitability; decide the next action. |
| Delivery | Organise files, documentation, and handover checks. | Make commitments, confirm acceptance, and release client work. |

## Skill selection

| Skill | Use for |
| --- | --- |
| `3w-taste-graph` | Load principles, exemplars and anti-patterns before every creative-output task. |
| `3w-brand-discovery` | Gather and organise evidence for an identity project. |
| `3w-category-code-audit` | Identify and test category conventions and opportunities. |
| `3w-creative-direction` | Turn an approved strategy into a proposed creative direction. |
| `3w-identity-system-critic` | Review identity work against a stated brief and evidence. |
| `3w-brand-consistency-qa` | Check applications against an identity system specification. |

## Token and verification rules

- Read the route entry, then frontmatter and headings before loading long pages.
- Never load `intelligence/` wholesale. Follow a specific index link and read only sources needed for the question.
- Read `INDEX.md` before retrieving context, then run `uv run python scripts/validate.py` before proposing a pull request. Run the unit tests when changing validator or tool code.
- Keep claims traceable to sources and show uncertainty instead of filling gaps.

## Publication rules

Follow [Publication rules](docs/public-private-boundary.md), [D-0017](studio/decisions/0017-fully-open-repository.md) and [D-0021](studio/decisions/0021-client-work-public-anonymised.md). Before collecting client or interview data, choose a non-public store; publish only non-identifying, aggregated, rights-cleared learning. Retain secret and personal-data scans, including on upstream agents.

## Agency agents

The upstream catalogue minus [founder exclusions](agents/exclusions.txt) (229 included, 53 excluded) is repo-local in `.claude/agents/`; [provenance and updates](agents/README.md) are locked and validated. 3RDWRONG status rules, evidence labels, no invented results, and publication rules override every persona. Start with the `3w-` skill where available, then select only the relevant specialist below (exact upstream `name` values).

| Studio work | Studio skill first | Upstream specialist |
| --- | --- | --- |
| Brand foundations and consistency | `3w-creative-direction`, `3w-brand-consistency-qa` | [Brand Guardian](.claude/agents/design-brand-guardian.md) |
| Discovery and buyer research | `3w-brand-discovery` | [UX Researcher](.claude/agents/design-ux-researcher.md) |
| Category and market signals | `3w-category-code-audit` | [Trend Researcher](.claude/agents/product-trend-researcher.md) |
| Sourced research synthesis | `3w-brand-discovery` when in discovery | [Research Synthesist](.claude/agents/research-synthesist.md) |
| Interview and critique feedback | `3w-brand-discovery`, `3w-identity-system-critic` | [Feedback Synthesizer](.claude/agents/product-feedback-synthesizer.md) |
| Concept and case-study narrative | `3w-creative-direction` | [Visual Storyteller](.claude/agents/design-visual-storyteller.md) |
| Inclusive visual review | `3w-identity-system-critic` | [Inclusive Visuals Specialist](.claude/agents/design-inclusive-visuals-specialist.md) |
| Final digital craft review | `3w-brand-consistency-qa` | [UI Finish-Gate Reviewer](.claude/agents/design-ui-finish-gate-reviewer.md) |
