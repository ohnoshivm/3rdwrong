---
name: 3w-taste-graph
description: Load a reference pack (what to do, what not to do, with exemplars) from the local Taste Graph before any creative-output task, and capture or analyse references into it. Use before landing pages, UI, branding, thumbnails, copy, social posts, ads, video or decks, and whenever the founder shares a link or screenshot to save.
metadata:
  type: skill
  status: experimental
  owner: founder
  last_reviewed: 2026-10-23
  version: 0.1.0
---
# 3w-taste-graph

## Purpose

Make the studio's taste memory part of every creative task. The Taste Graph is a local PostgreSQL graph of curated references, the patterns and principles they exemplify, and the anti-patterns they warn against. A **reference pack** turns it into a short brief of principles to apply and mistakes to avoid. It informs judgement; it does not replace it, and it never licenses copying.

## When to use

- **Before any creative-output task**: landing page, website section, UI component, branding or identity, YouTube thumbnail, copy or headlines, social post (X, LinkedIn, TikTok, Reels), ad, email, video, deck.
- **When the founder shares a link or screenshot to save.**
- **For an optional daily capture run** when a scheduled task asks for one.

## When not to use

Do not use for non-creative work (backend, data, ops). Do not use the graph as evidence of effectiveness, audience response or market fact: it records taste judgements. Do not run captures behind a login, with cookies or credentials, or around paywalls and anti-bot measures.

## Inputs

- The creative brief in one sentence, plus the output kind when known (`landing_page`, `thumbnail`, `copy`, `tweet`, `reel` …).
- For a capture: a public URL and/or local screenshots, the verdict (`exemplar`, `anti_pattern` or `mixed`) and the analysis.
- A running local database (`TASTE_GRAPH_DSN`, default `postgresql:///taste_graph`). If it is unreachable, say so and continue without a pack; never invent one.

## Dependencies

[Taste Graph guide](../../taste/graph/README.md) for setup and commands; [taste references](../../taste/README.md) and [discovery sources](../../taste/discovery-sources.md) for the source lists; [D-0020](../../studio/decisions/0020-taste-graph.md) for the governing decision. The CLI is `uv run scripts/taste_graph.py`; web captures use `playwright-cli`. No paid service is required.

## Procedure

### A. Before a creative-output task

1. Run `uv run scripts/taste_graph.py pack "<brief>" [--kind <kind>] [--project <slug>]`. Add `--project` when the work is a named deliverable, so the graph records which references informed it.
2. Read the pack. Open at most the images it lists under "Open these images".
3. State in 2–4 lines which principles you will apply and which don'ts you will avoid, then do the work. Re-check the output against those lines before handing it over.

### B. When the founder shares a reference to save

1. Analyse it (procedure C), then run `add <url>` or `add --file <screenshot> --title "…"` with `--kind`, `--verdict`, `--why "<analysis>"`, `--pattern "<pattern>"` (repeatable; `principle:` or `technique:` prefixes allowed), `--violates "<principle>"` for anti-patterns, and `--brand`, `--creator`, `--platform`, `--tone`, `--tags` when known.
2. Add `--by founder --status curated` only when the founder explicitly says so in this conversation. Otherwise it enters as `inbox`.
3. Report the node id and stored media paths. If capture warns that the screenshot looks blank, or the site is behind a login, ask the founder for screenshots (`--file`) and the copy (`--text`).

### C. How to analyse a reference

Answer in 3–6 sentences for `--why`:

- What makes it work, naming the lever: hierarchy, typography, composition, colour, motion, copy structure, the hook or first two seconds, the CTA.
- The transferable **principle**, phrased so it applies to a different brand and format.
- What **not** to copy: the recognisable layout, asset, line or identity element that belongs to its owner.

For an anti-pattern, name the principle it violates and why it fails.

### D. Daily capture run (optional scheduled task)

1. Browse the sources in [discovery sources](../../taste/discovery-sources.md) and [Award Site Teardowns](../../taste/award-site-teardowns.md).
2. Pick at most 10 genuinely excellent new items across kinds; skip anything already in the graph (`search`, or `show <url>`).
3. Capture each with an analysis as `inbox` (the default). Never pass `--status curated` and never run `update --status curated`.
4. Report what was captured, with ids, for the founder's weekly curation.

### E. Privacy and rights

Captured media and third-party text are private reference material. They stay in `TASTE_GRAPH_HOME` (outside any repository) and the local database; never paste them into the repository, an issue, a deliverable or a public channel. The repository holds only code, schema, docs and the seed of public URLs and studio notes.

## Evidence requirements

A pack reports the founder's curated taste judgements; treat them as **Interpretation**, not evidence of performance. Analyses you write are **Interpretation** until the founder curates them. Facts about a reference's maker, awards or results need a cited source; otherwise leave them out.

## Output

Before creative work, a short statement in this form, followed by the work itself:

```markdown
Taste pack: "<brief>" (<N> references)
Applying: <principle>, <principle>, <principle>.
Avoiding: <anti-pattern>, <anti-pattern>.
```

After a capture: `added|updated #<id> asset:<slug> [<status>]`, media paths, and any warning.

## Quality checks

- The pack was run with the actual brief, not a generic query, and no more than its listed images were opened.
- The applied principles are visible in the work; the avoided don'ts are absent from it.
- Every capture has an analysis naming a lever, a transferable principle and what not to copy.
- Agent captures are `inbox`; nothing was curated without the founder's explicit instruction.
- No captured image or third-party text left the data home or database.

## Failure conditions

Stop and report when the database is unreachable, a capture needs a login, the founder has not confirmed the rights to use a supplied file, or a request would copy a reference's layout, assets, copy or identity. Do not fabricate a pack, an analysis of a page you could not see, or a curation decision.

## Human review

The founder curates: weekly, they review `list --status inbox`, set verdicts and scores, and promote with `update <id> --status curated` or archive. The founder judges originality of every output that used a pack. This skill never approves work.

## Example

**Fictional example.** Brief: "LinkedIn post announcing a new identity project". `pack "LinkedIn post announcing an identity project" --kind linkedin_post` returns Do: *One idea per section*, *Plain-sentence hero*; Don't: *Filler copy*. The agent writes: "Applying: one idea, a plain first line, specific detail. Avoiding: filler claims." The post opens with one concrete observation about the project rather than "We're thrilled to announce".
