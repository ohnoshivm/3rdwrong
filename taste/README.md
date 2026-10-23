# Taste references

**TASTE REFERENCE ONLY.** This folder holds curated references that calibrate the studio's aesthetic and
experiential bar. The founder selected the references on 2026-10-22; selection is not approval of a
method, visual direction or client deliverable.

[D-0002](../studio/decisions/0002-identity-system-scope.md) continues to govern the offer: comprehensive
websites and complex 3D experiences are excluded from the standard identity engagement. 3RDWRONGS is a
brand identity studio. Admiration for immersive studio websites does not imply that it sells them.

## How it fits

- [Swipe file](swipe-file.md) is the founder's three-tier master list.
- [Inspiration discovery sources](discovery-sources.md) verifies discovery sources and gives use guidance.
- [Award Site Teardowns](award-site-teardowns.md) is the primary resource for structured award-site analysis.
- [Studio websites](studio-websites.md) is the curated, source-checked original-site benchmark list, with limits and browser prompts.
- [Taste practice](../methods/taste-practice.md) supplies the proposed weekly analysis and original-application loop.
- [Intelligence](../intelligence/README.md) holds deeper evidence-graded studies, transferable questions and exercises.
- [Research queue](../intelligence/research-queue.md) prioritises Buttermax, Unseen Studio and fromanother for deep study.

## Own-identity guardrail

**Interpretation** — Studying a reference must not become imitation. Many of these sites share a recognisable
“awards-site” vocabulary: immersive entry scenes, large type, loaders, pointer effects and dramatic transitions.
Collecting them without critique could produce another familiar creative-agency aesthetic.

**Documented** — [D-0006](../studio/decisions/0006-rejected-own-identity-direction.md) rejects the exploration
combining black backgrounds, heavy grotesk typography and neon accents because it was conventional.
These references do not reopen that direction or approve an identity for 3RDWRONGS.

Extract a principle, explain its context, then make an original application with different formal decisions.
Do not copy layouts, copy, characters, imagery, objects, brand identities or distinctive interaction sequences.

## Add a reference

1. Record the studio/site name, canonical HTTPS link, source title and access date. Strip tracking parameters;
   do not use image-proxy or favicon URLs as sources.
2. Open the primary site and relevant creator/award account. Verify attribution, location, dates and technical
   claims individually; record failed access or changes with the date. Treat AI research notes as leads.
3. Include what to study, concrete browser questions, a transferable identity-studio lesson and unknowns.
   Distinguish a historical version from the current website.
4. Label claims **Documented**, **Interpretation**, **Hypothesis** or **Unknown**. Cite documented claims;
   call unsupported details unverified or omit them. A source's self-report is not independent measurement.
5. Store notes and links only: no images, downloaded assets, copied site code or third-party design files.
   A reference confers no permission to reproduce its work.
6. For a new research document, use frontmatter with `type: research`, `status: reference`, `owner: founder`,
   `last_reviewed`, `review_every_days` and `sources` entries containing `title`, `url` and `accessed`.
   Link it below, rebuild `INDEX.md` and run the repository validator and Markdown lint.

## Taste Graph

The [Taste Graph](graph/README.md) turns these lists into a local PostgreSQL knowledge graph of references, patterns, principles and anti-patterns ([D-0020](../studio/decisions/0020-taste-graph.md)). Agents load a reference pack from it through the [`3w-taste-graph`](../skills/3w-taste-graph/SKILL.md) skill before any creative-output task. Captured media and third-party text stay on the founder's machine, never in this repository.

## File index

| File | Purpose |
| --- | --- |
| [Swipe file](swipe-file.md) | Founder's three-tier master list and pick-list of website references. |
| [Inspiration discovery sources](discovery-sources.md) | Discovery-source verification and use guidance. |
| [Award Site Teardowns](award-site-teardowns.md) | Primary taste resource for structured award-site analysis; complements the original-site benchmarks and browser prompts in studio-websites.md. |
| [Studio websites](studio-websites.md) | Six primary benchmarks, four further references, two provisional Indian leads, source checks and deep-study priorities. |
