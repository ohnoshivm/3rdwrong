---
title: Mark exploration
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:3w-mark-exploration
department: design
sub_department: identity-craft
job: mark-logo
role: lead
trigger: ""
kind: repo-skill
availability: repo
distribution: repo
source: skills/3w-mark-exploration/SKILL.md
invoke: "3w-mark-exploration skill"
pairs_with: [skill:3w-category-code-audit, skill:3w-creative-direction, skill:3w-identity-system-critic, skill:3w-typography-system, skill:3w-colour-system]
---
# Mark exploration

The studio's lead tool for mark and logo work: from an idea written without visual adjectives to a tested, production-ready vector family.

## What it does

- Requires the mark's idea in words before form, and at least three conceptually distinct routes.
- Gives a sketch-to-vector workflow and a construction and optical-correction checklist (overshoot, optical centre, stroke contrast, counters, apertures, spacing).
- Sets size and medium tests: 16, 24, 32, 48 px, favicon, app icon, print minimum in mm, emboss, foil and embroidery where in scope.
- Specifies one-colour and reverse versions, clear space and minimum sizes from tests.
- Checks distinctiveness against the category audit and flags registrability cautions; trademark clearance stays a legal step.

## When to use

- Phase 05 Identity, after the founder chooses a concept route.
- Phase 07 Validation, to re-run size and medium tests on final artwork.
- Formative exploration during Phase 04, if accepted and labelled formative.

## When not to use

- Before any route exists, or to restyle an approved mark without a brief.
- To produce a finished logo with an image model.
- To judge registrability — that needs a qualified trademark professional.

## Inputs it needs

- Chosen route and idea statement; strategy status.
- Brand name, scripts, mark type in scope and brand architecture.
- Category audit (`skill:3w-category-code-audit`) and any Taste Graph never-copy list.
- Application set, media and vendor constraints.

## How to run it

1. Collect the inputs above in one folder or message; state whether the route is chosen or the run is formative.
2. Run the skill; a human designer makes every form decision it records.
3. Hand the output to someone other than the maker for review.
4. File the output in the project folder; nothing it produces is an approval.

```text
Use the 3w-mark-exploration skill for {{project}}. Route: {{link, chosen or formative}}. Name and scripts: {{…}}. Category audit: {{link or none}}. Applications and media: {{list with sizes}}. Return the skill's exact output structure; mark untested items Unknown; do not approve or clear anything.
```

## What good output looks like

- An adjective-free idea, three routes that differ in organising idea, and rejected routes with reasons.
- Every size and medium test recorded as run with evidence, unverified or out of scope.
- A clear decision on what represents the brand below the master's minimum size.
- Distinctiveness cited or Unknown; registrability as cautions plus the legal step.

## Quality checks

- [ ] Idea stated before form, without visual adjectives.
- [ ] Routes are different ideas, not style variants; none uses the D-0006 rejected look.
- [ ] Size renders and physical tests exist or are marked unverified.
- [ ] Reverse versions were optically checked.
- [ ] No registrability verdict; reviewer is not the maker.

## Pairs with

- Upstream: `skill:3w-creative-direction` (route), `skill:3w-category-code-audit` (category sample).
- Alongside: `skill:3w-typography-system` (stroke contrast, kerning), `skill:3w-colour-system` (versions).
- Downstream: `skill:3w-identity-system-critic` before the founder chooses.

## Limits and cautions

- Experimental; one fictional run so far (Stillsoil Atelier) with no drawn artwork.
- AI may explore and check; the founder or design lead draws and decides. AI-derived forms in finals need the client's written consent (D-0023).
- Never copy, trace or closely adapt an existing mark.
