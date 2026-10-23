# 3RDWRONG Creative Operating System

3RDWRONG is an emerging independent design-engineering studio: **brand identity at the core, digital experience as the second pillar, perception-led by method.** Living identity remains a capability. See the approved direction in [D-0018](studio/decisions/0018-design-engineering-studio.md).

The repository is [`ohnoshivm/3rdwrong`](https://github.com/ohnoshivm/3rdwrong), with local home `~/3rdwrong`. Everything committed here is public and open source under the applicable licences, including the [founding blueprint](studio/archive/founding-blueprint-v1.0.md) and [unvalidated pricing hypotheses](studio/pricing.md). See [D-0017](studio/decisions/0017-fully-open-repository.md).

This repository is the studio's version-controlled second brain: a public operating knowledge base that connects strategy, repeatable methods, source-based design research, working templates, and experimental AI skills so learning can compound across projects without replacing human creative judgement. [`INDEX.md`](INDEX.md) maps the frontmatter documents; [`inbox/`](inbox/README.md) is for quick public-safe capture before weekly triage.

## Contents

| Area | Purpose |
| --- | --- |
| [`INDEX.md`](INDEX.md) | Generated retrieval index for frontmatter documents, grouped by area. |
| [`handbook/`](handbook/README.md) | Generated tool handbook for humans and routing index for agents. |
| [`inbox/`](inbox/README.md) | Rough public-safe notes and links awaiting weekly triage. |
| [`studio/`](studio/README.md) | Positioning, offer, philosophy, roadmap, and decision records. |
| [`methods/`](methods/README.md) | Proposed ways of working, quality checks, and learning loop. |
| [`intelligence/`](intelligence/README.md) | Cited agency, project, visual-system, and research studies. |
| [`taste/`](taste/README.md) | Curated aesthetic and experiential references only; no policy or offer change. |
| [`templates/`](templates/README.md) | Reusable project, research, learning, strategy, and critique documents. |
| [`skills/`](skills/README.md) | Six `3w-` experimental AI workflows with evidence and human-review requirements. |
| [`agents/`](agents/README.md) | Upstream Agency Agents catalogue minus founder exclusions, provenance, lock and repo-level update instructions. |
| [`projects/`](projects/README.md) | Codenamed, contract-cleared anonymised project records and internal exploration. |
| [`experiments/`](experiments/README.md) | Small, explicit tests of creative and operating hypotheses. |
| [`growth/`](growth/README.md) | Sales, content, outbound, proof and acquisition metrics; identities and money stay in the vault. |
| [`business/`](business/README.md) | Pricing, proposals, legal/finance methods, operations and founder reviews. |
| [`docs/`](docs/architecture.md) | Governance, onboarding, workflows, maintenance, and publication rules. |
| [`scripts/validate.py`](scripts/validate.py) and [`schemas/metadata.json`](schemas/metadata.json) | Repository checks and their single source of truth. |
| [`.github/`](.github/workflows/validate.yml) | Contribution workflow, labels, repository ownership, and CI. |

## Start here

- Retrieval index: [INDEX.md](INDEX.md).
- Human onboarding: [Getting started](docs/getting-started.md).
- How knowledge is reviewed: [Knowledge governance](docs/knowledge-governance.md).
- How agents should load context: [AI integration](docs/ai-integration.md) and [agent instructions](AGENTS.md).
- How to contribute: [Contributing](CONTRIBUTING.md).
- What may be published: [Publication rules](docs/public-private-boundary.md).

## Departments and toolkit

The [department index](studio/departments/README.md) groups eleven departments: **Craft** (Design, Engineering, Labs), **Delivery** (Strategy, Production, Media), **Growth** (Marketing, Advertising, Outbound, Sales), and **Studio** (Operations). Leads and specialists are active; bench and parked tools stay in the library under D-0019. The [registry summary](studio/departments/registry-summary.md) records job leads and honest gaps.

The portable toolkit has three distribution paths: **VENDOR** in `toolkit/vendor/` for redistributable snapshots, **FETCH** in [toolkit/fetch.yaml](toolkit/fetch.yaml) at pinned commits, and **MANUAL** in [toolkit/manual.md](toolkit/manual.md) for account setup or unresolved rights. See [coverage](toolkit/coverage.json), [LICENSING — Third-party toolkit](LICENSING.md#third-party-toolkit) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

### One-command install

From a clone of this repository:

```bash
scripts/install.sh --profile full --tools both
scripts/install.sh --profile design-engineering --tools codex --dry-run
scripts/install.sh --profile minimal --tools claude --skip-fetch
scripts/install.sh --uninstall
```

Profiles: `full` (all departments), `design-engineering` (Craft), `growth` (Growth), `studio` (Delivery and Operations), `minimal` (core `3w-` skills only). Core skills accompany every profile. `--tools claude|codex|both` chooses hosts; `--dry-run` previews changes, `--skip-fetch` skips network packages, and `--uninstall` removes only unchanged installer-owned entries. `TOOLKIT_FETCH_TIMEOUT` sets the per-fetch timeout in seconds (default 1800).

Active skills link into `~/.claude/skills/` and/or `~/.agents/skills/`; Claude agents link into `~/.claude/agents/`. Library tools and Codex agent references use `~/.claude/skills-library/3rdwrong/`. Fetches and ownership records live under `~/.3rdwrong/`; configuration templates are written only when absent. Names are prefixed `3w-`. Existing user files or folders are never overwritten; conflicts are reported. Keep the clone in place while its links are installed.

### Claude Code marketplace

[.claude-plugin/marketplace.json](.claude-plugin/marketplace.json) exposes 12 plugins: one per department plus `3rdwrong-core`. Choose the department you need. In Claude Code, register the release branch and install a plugin:

```text
/plugin marketplace add ohnoshivm/3rdwrong#system/v0.3-departments
/plugin install 3rdwrong-design@3rdwrong
/plugin install 3rdwrong-core@3rdwrong
```

Shell equivalents are `claude plugin marketplace add ohnoshivm/3rdwrong#system/v0.3-departments` and `claude plugin install 3rdwrong-design@3rdwrong`. These forms were checked against the [current Claude Code plugin documentation](https://code.claude.com/docs/en/discover-plugins) on 2026-10-23. After PR A lands, the unpinned `ohnoshivm/3rdwrong` source uses the default branch. Fetch/manual tools still need the setup described above; marketplace entries do not grant accounts or licences.

## Using with Claude Code

1. Open Claude Code at the repository root so it can read `AGENTS.md` and the task router.
2. Have it read `INDEX.md` first, then follow the closest task route in `AGENTS.md`. Claude Code can discover the six `3w-` skills through `.claude/skills` and the 229-agent catalogue (53 founder exclusions) through `.claude/agents`; route to studio skills first.
3. Review every proposed change and keep speculative material in its correct status.

Example prompts:

- “Read the route for starting a client identity project and prepare a proposed discovery brief from the files I provide. Do not invent research findings.”
- “Use the 3w-identity-system-critic skill to critique this supplied design. Separate documented evidence, interpretation, hypothesis, and unknowns.”
- “Review this agency's public work using the agency-study template. Link each observation to a source and keep the study at reference status.”

## Taste Graph

The [Taste Graph](taste/graph/README.md) is local PostgreSQL reference memory: public-source seeds, curated examples, principles and anti-patterns. Before creative work, use [3w-taste-graph](skills/3w-taste-graph/SKILL.md) and `uv run scripts/taste_graph.py pack "<brief>"`; state the principles and don'ts you will apply. Media and database backups stay outside this repo. Setup, capture and curation are in the guide ([D-0020](studio/decisions/0020-taste-graph.md)).

## Delivery engine

The [lifecycle](methods/lifecycle.md) connects discovery, scope, contract, production, QA, launch and care. [Digital Experience](methods/digital-experience/README.md) includes web standards, measured quality and launch gates; [handover and care](methods/handover-and-care.md) carries the work after release. [D-0021](studio/decisions/0021-client-work-public-anonymised.md) permits codenamed public records only when the contract clears them; names, people, contacts, domains, money and client files stay in the private vault.

[bin/3w](bin/3w) renders [bundles](templates/bundles/README.md) and checks publication:

```bash
bin/3w new project-digital --cleared --codename quiet-harbour
# Or --private to create the whole workspace in an existing private vault.
bin/3w check
```

Choose `THREEW_VAULT` outside all Git worktrees and run `bin/3w vault init` before creating private records. Only run these creation commands when you intend to create a workspace.

## Business engine

The [business guide](business/README.md) covers pricing, proposals/SOWs, legal/IP, invoicing/tax, collaborators and operating rhythm. `uv run python scripts/pricing.py "$THREEW_VAULT/<codename>/finance/estimate.yaml"` reads private rates and an estimate and prints a private pricing check. Never paste monetary output into this repo. `uv run python scripts/review_queue.py --limit 8` prints the founder's next proposed/hypothesis documents to review. Methods and commercial defaults remain proposed.

## Growth engine

The [Growth engine](growth/README.md) connects [qualification and discovery](growth/sales/README.md), [content production](growth/content/README.md), [outbound](growth/outbound/README.md), [proof](growth/proof/README.md) and [metrics](growth/metrics.md). It feeds qualified opportunities into the Business engine and turns cleared delivery evidence into case studies, testimonials, referrals and award decisions. Prospect identities, outreach records, discovery notes and money stay in the vault. [Client acquisition](business/client-acquisition.md) is the short route into these methods.

## Validation

Install the locked Python dependency and run the repository validator:

```bash
uv sync --locked
uv run python scripts/build_index.py
uv run python scripts/validate.py
```

To include warning-only review-cadence checks, add `--stale`. Run the unit tests after changing validator or maintenance-tool code:

```bash
uv run python -m unittest discover -s tests -q
```

## Who can use it

The OS is for the founder, collaborators, researchers, designers, and AI tools working with the studio's public knowledge. AI can help retrieve, organise, compare, and critique material; people retain responsibility for evidence, creative judgement, privacy, and approval.

## Complete and experimental

The repository foundation, governance rules, validation tools, and entry-point documentation are in place. [D-0018](studio/decisions/0018-design-engineering-studio.md) records the approved design-engineering direction; [D-0019](studio/decisions/0019-organisation-and-loading-policy.md) records the approved organisation and loading policy. The original operating philosophy remains recorded. Positioning wording, offer details, delivery workflows and the 12-month roadmap remain proposed; department guides and the portable registry are integrated, with routing and capability evaluations still proposed.

The studio's own visual identity is still in exploration and is not approved. The skills are experimental. The ICP and existing pricing remain hypotheses and need review for D-0018; Digital Experience pricing is to be set by founder. The ambition to become a leading studio within 6–12 months is an ambition, not current standing or validated market evidence. Statuses on individual documents show what is ready for use and what still needs review.

## Open source and protected material

Code and original written material have separate licences; third-party material, the 3RDWRONG name and future brand assets, and client work are treated separately. Read [Licensing](LICENSING.md) and the [publication rules](docs/public-private-boundary.md) before reusing or publishing material.

## Next priorities

The current sequence of studio priorities is in the [roadmap](studio/roadmap.md).
