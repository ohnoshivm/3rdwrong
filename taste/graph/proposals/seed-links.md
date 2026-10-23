---
title: Proposed seed links for the Taste Graph
type: guide
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 30
---
# Proposed seed links for the Taste Graph

These are proposed links between seed website assets and existing principles and patterns. Nothing here is in the database yet. Each justification describes what the live page showed at 1440×900 and 390×844 across its first three screens on 2026-10-23. The sites are references for principles only: never copy their layouts, assets or copy.

**Batch 1 of 29:** Igloo Inc only. The other 28 sites will follow in later batches.

## How to approve

1. Tick the rows you accept here, or reply "approve all except …".
2. Set `approved: true` on the same rows in [`seed-links.yaml`](seed-links.yaml).
3. Dry run (prints the commands only):

   ```bash
   uv run --with pyyaml python -c 'import yaml,shlex; [print("uv run scripts/taste_graph.py link", r["asset"], r["rel"], shlex.quote(r["dst"]), "--note", shlex.quote(r["note"])) for r in yaml.safe_load(open("taste/graph/proposals/seed-links.yaml"))["links"] if r["approved"]]'
   ```

4. Apply: run the same command and pipe it to `sh`.

`exemplifies` with a `pattern:` target records an anti-pattern the site shows, and packs list it under Don't. Always keep the `principle:` or `pattern:` prefix: if you drop it, `link` creates a new pattern node instead of matching the existing one.

## igloo-inc

<https://www.igloo.inc/>

- [x] igloo-inc exemplifies principle:a-single-coherent-palette — every screen at both widths stays in one cool grey-to-white range; the only accent is light glowing from the igloo's block seams.
- [x] igloo-inc exemplifies principle:intentional-asymmetry — the wordmark and copyright stack sit top-left, a right-aligned monospace manifesto sits top-right, and the scroll and sound prompts sit bottom-left, framing a centred igloo.
- [x] igloo-inc exemplifies principle:motion-with-purpose — scrolling pulls the igloo apart into separate blocks tagged with numbered, line-connected labels, so the scroll itself acts out one company made of many brands (reduced-motion handling not checked).
- [x] igloo-inc exemplifies pattern:default-awards-site-vocabulary — (partial, anti-pattern) the first view is a bare ASCII progress loader on flat grey, followed by an immersive entry scene with a sound toggle, before any copy appears.

Approved by the founder on 2026-10-23 (all four).

## New pattern proposals

None yet. New patterns need several sites that share them, so they will come in later batches.
