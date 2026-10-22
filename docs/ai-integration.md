---
title: AI integration
type: guide
status: proposed
owner: founder
last_reviewed: 2026-10-22
---

# AI integration

AI tools help retrieve, structure, compare, and critique public studio knowledge. They do not establish facts, make final creative choices, or approve policy.

## Loading context

Start with the generated [`INDEX.md`](../INDEX.md) to locate relevant documents, then follow the closest task in [`AGENTS.md`](../AGENTS.md) and read only the named files. Check frontmatter, headings, and status first. Never load `intelligence/` wholesale; follow one index link at a time and read the sources needed for the question.

Claude Code imports `AGENTS.md` through [`CLAUDE.md`](../CLAUDE.md). Skills are discovered through `.claude/skills` symlinks to `skills/`. Other tools can use the same skill files as explicit instructions.

## Skill format

Each `skills/<name>/SKILL.md` uses Agent Skills frontmatter with a folder-matching `name`, a concise `description`, and `metadata` for type, status, owner, and review date; an optional `version` must be a string. Its body contains twelve H2 sections in the order checked by the validator. See [`schemas/metadata.json`](../schemas/metadata.json) for the canonical section names.

To add or improve a skill, keep its status `experimental`, add the matching symlink, and evaluate it using [`templates/learning/skill-evaluation.md`](../templates/learning/skill-evaluation.md). Record the task, input, expected evidence, observed failure modes, and required human review.

## Token economy

- Route to a narrow task and load the minimum source files.
- Inspect frontmatter and headings before full bodies.
- Follow a specific source or intelligence index entry; do not ingest whole libraries by default.
- Ask for a concrete output and return citations or paths that let a human verify it.
- Keep generated drafts short enough to review and preserve uncertainty explicitly.

## Source verification and anti-fabrication

Use public primary sources where possible. Verify that a source supports the specific claim and record access dates for research. Mark each material claim Documented, Interpretation, Hypothesis, or Unknown. Never invent clients, results, approvals, research findings, quotations, or statistics. The company facts in the founding brief are the only approved company facts until a human records a change.

Do not send private client materials to a tool unless the studio has approved that tool and use. Never put client names, assets, personal data, contracts, internal margins, or unreleased work in this repository. Read the [public-private boundary](public-private-boundary.md) before using examples.

## AI and human responsibility

This operating split is adapted from Founding Blueprint v1.0, 22 October 2026 (private archive). Reuse the existing multi-model AI environment; do not build another routing system. Write skills in Markdown first; add code only when it improves output or removes repeated work.

| Work | AI contribution | Human responsibility |
| --- | --- | --- |
| Research | Find candidate sources, organise evidence, and draft cited summaries. | Choose the question, verify sources, and judge what the evidence supports. |
| Strategy | Compare evidence and prepare options with assumptions visible. | Set objectives, choose direction, and approve strategic policy. |
| Concepts | Expand possible routes and make alternatives easier to compare. | Lead art direction, judge originality, and select the concept. |
| Production | Prepare drafts and reduce repetitive production work. | Own craft, technical quality, rights, accessibility, and final release. |
| Critique | Check work against criteria and surface gaps or contradictions. | Weigh context, taste, audience fit, and commercial suitability; decide the next action. |
| Delivery | Organise files, documentation, and handover checks. | Make commitments, confirm acceptance, and release client work. |

## Adding a skill

1. Open an issue describing the task, example, evaluation plan, and privacy check.
2. Create a short-lived branch, add `skills/<name>/SKILL.md`, and link `.claude/skills/<name>` to `../../skills/<name>`.
3. Keep status `experimental`; use all required H2 sections and state evidence and failure conditions.
4. Evaluate with the skill-evaluation template, then run `uv run python scripts/validate.py` and the unit tests.
5. Submit a pull request for human review. A passing evaluation does not make the skill approved policy.

Regenerate the retrieval index after changing frontmatter documents with `uv run python scripts/build_index.py`; use `uv run python scripts/build_index.py --check` to verify it without writing.
