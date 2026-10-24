---
name: awesome-design-md
description: Use when you need a DESIGN.md reference to study a brand or product visual system; it is inspiration only, never a source to copy into client work.
metadata:
  type: skill
  status: reference
  owner: founder
  last_reviewed: 2026-10-24
---

# Awesome DESIGN.md (reference wrapper)

## Purpose

Point agents at a pinned reference library of 84 DESIGN.md analyses of brand and product websites (MIT, upstream <https://github.com/voltagent/awesome-design-md>, commit `3b605329240ce735b510037cca322f1831fdd7f8`) so they can study how a visual system is organised. The library is fetched at install time to `~/.3rdwrong/fetch/pack-voltagent-awesome-design-md-mit/design-md/<brand>/DESIGN.md`. It is not vendored in this repository.

## When to use

- A design-system pattern needs a concrete external reference (type scale, spacing, colour roles, radii, motion timing).
- Comparing token approaches across several reference systems before writing the studio's own DESIGN.md.

## When not to use

- Copying a brand's system, layouts, assets or copy into any studio or client output.
- Brand identity decisions: use the approved strategy and identity-craft skills.
- When the library is not fetched: report it as unavailable.

## Inputs

- The brand or product to study, and the question the study must answer.
- The fetched library at its pinned commit.

## Dependencies

- `skills/3w-taste-graph/SKILL.md` for any creative-output task.
- The toolkit fetch step that places the library at the path above.

## Procedure

1. Confirm the library exists at the fetch path. If not, stop and report it.
2. Open only the one `<brand>/DESIGN.md` that answers the question.
3. Write findings as principles, each labelled Documented or Interpretation, and state what does not transfer.

## Evidence requirements

- Every claim about a reference names its file.
- Values are described as principles, not copied as a ready-made system.

## Output

Principles with source file names and evidence labels, and a note of what is not transferable to 3RDWRONG work.

## Quality checks

- [ ] No layout, asset, copy or brand identity copied.
- [ ] Only the named brand file was read.
- [ ] The taste graph pack was loaded for creative output.

## Failure conditions

- The library is missing, or the study would require copying a brand's system.
- The output presents a third-party analysis as established fact about the brand.

## Human review

A reviewer other than the author checks that the findings are principles, not copies, before they inform a client direction.

## Example

Question: how does a reference system set its type scale? Output: a short principle list citing the one brand file read, with each point labelled Documented or Interpretation.
