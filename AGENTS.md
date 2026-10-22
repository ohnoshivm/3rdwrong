# Agent instructions

3RDWRONGS OS is the public working knowledge base for a founder-led identity studio. It holds reviewed strategy, methods, research, templates, and experimental AI skills.

It is not a client archive: client information, personal data, credentials, and confidential material stay outside this repository.

## Retrieval first

Read [`INDEX.md`](INDEX.md) first to locate current knowledge. Then read the closest route below and only its named files; do not load the repository wholesale.

## Source order

When sources conflict, use this order and flag the conflict for a human:

1. `studio/decisions/` — the decision log wins over other pages.
2. `studio/` — current studio strategy and operating facts.
3. `methods/` — proposed and reviewed ways of working.
4. `intelligence/` — source-based research and design references.
5. `templates/` — reusable starting points, never evidence by themselves.

## Status and evidence rules

- `approved` means a named human has approved the material and the record includes `approved_by` and `approved_on`. Agents never promote material to `approved`.
- `proposed` means awaiting human review; `hypothesis` means plausible and untested; `experimental` means being evaluated; `rejected` means a human rejected it; `superseded` points to its replacement; `reference` records source material without adopting it as policy.
- Never invent clients, results, approvals, research findings, quotations, or statistics.
- Label evidence exactly: **Documented**, **Interpretation**, **Hypothesis**, or **Unknown**. Cite sources for documented claims and keep interpretation distinct from observation.
- 3RDWRONGS' visual identity is not approved. A rejected exploration used black backgrounds, heavy grotesk typography, and neon accents. Do not reuse that direction as guidance.
- Everything committed here is public and open source. Never commit personal data, third-party contracts, credentials or NDA-bound assets. Choose a non-public store before collecting client or interview data; follow the [publication rules](docs/public-private-boundary.md). Studio pricing hypotheses and the founding source are public, with their evidence/status limits intact.

## Context router

Read the `INDEX.md` entry first, then open the minimum files listed for the task.

| Task | Minimum files to read |
| --- | --- |
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

## Inspiration and references

When a task involves gathering inspiration or visual/interactive references, use the `taste/` folder: start at `taste/README.md`, then `taste/swipe-file.md`, `taste/discovery-sources.md`, `taste/award-site-teardowns.md` and `taste/studio-websites.md`. Cite the specific source page used.

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

Follow [Publication rules](docs/public-private-boundary.md) and [D-0017](studio/decisions/0017-fully-open-repository.md). Before collecting client or interview data, choose a non-public store; publish only non-identifying, aggregated, rights-cleared learning. Retain secret and personal-data scans, including on upstream agents.

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
