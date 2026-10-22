# 3RDWRONGS Creative Operating System

3RDWRONGS is an emerging independent design and branding company with global ambitions. Its approved direction is: **“A brand identity studio first. A living identity specialist by capability. A perception-led consultancy by method.”**

The repository is [`ohnoshivm/3rdwrong`](https://github.com/ohnoshivm/3rdwrong), with local home `~/3rdwrong`. Everything committed here is public and open source under the applicable licences, including the [founding blueprint](studio/archive/founding-blueprint-v1.0.md) and [unvalidated pricing hypotheses](studio/pricing.md). See [D-0017](studio/decisions/0017-fully-open-repository.md).

This repository is the studio's version-controlled second brain: a public operating knowledge base that connects strategy, repeatable methods, source-based design research, working templates, and experimental AI skills so learning can compound across projects without replacing human creative judgement. [`INDEX.md`](INDEX.md) maps the frontmatter documents; [`inbox/`](inbox/README.md) is for quick public-safe capture before weekly triage.

## Contents

| Area | Purpose |
| --- | --- |
| [`INDEX.md`](INDEX.md) | Generated retrieval index for frontmatter documents, grouped by area. |
| [`inbox/`](inbox/README.md) | Rough public-safe notes and links awaiting weekly triage. |
| [`studio/`](studio/README.md) | Positioning, offer, philosophy, roadmap, and decision records. |
| [`methods/`](methods/README.md) | Proposed ways of working, quality checks, and learning loop. |
| [`intelligence/`](intelligence/README.md) | Cited agency, project, visual-system, and research studies. |
| [`taste/`](taste/README.md) | Curated aesthetic and experiential references only; no policy or offer change. |
| [`templates/`](templates/README.md) | Reusable project, research, learning, strategy, and critique documents. |
| [`skills/`](skills/README.md) | Five `3w-` experimental AI workflows with evidence and human-review requirements. |
| [`agents/`](agents/README.md) | Upstream Agency Agents catalogue minus founder exclusions, provenance, lock and repo-level update instructions. |
| [`projects/`](projects/README.md) | Internal identity exploration and sanitised examples. |
| [`experiments/`](experiments/README.md) | Small, explicit tests of creative and operating hypotheses. |
| [`business/`](business/engagement-operations.md) | Proposed engagement operations. |
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

## Using with Claude Code

1. Open Claude Code at the repository root so it can read `AGENTS.md` and the task router.
2. Have it read `INDEX.md` first, then follow the closest task route in `AGENTS.md`. Claude Code can discover the five `3w-` skills through `.claude/skills` and the 229-agent catalogue (53 founder exclusions) through `.claude/agents`; route to studio skills first.
3. Review every proposed change and keep speculative material in its correct status.

Example prompts:

- “Read the route for starting a client identity project and prepare a proposed discovery brief from the files I provide. Do not invent research findings.”
- “Use the 3w-identity-system-critic skill to critique this supplied design. Separate documented evidence, interpretation, hypothesis, and unknowns.”
- “Review this agency's public work using the agency-study template. Link each observation to a source and keep the study at reference status.”

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

The repository foundation, governance rules, validation tools, and entry-point documentation are in place. The approved positioning, flagship offer, and operating philosophy are recorded from the founding brief. Delivery workflow details remain proposed.

The studio's own visual identity is still in exploration and is not approved. The skills are experimental. The primary ICP and pricing range remain hypotheses; neither should be presented as validated market evidence. Statuses on individual documents show what is ready for use and what still needs review.

## Open source and protected material

Code and original written material have separate licences; third-party material, the 3RDWRONGS name and future brand assets, and client work are treated separately. Read [Licensing](LICENSING.md) and the [publication rules](docs/public-private-boundary.md) before reusing or publishing material.

## Next priorities

The current sequence of studio priorities is in the [roadmap](studio/roadmap.md).
