---
title: "Stage 4: Reconcile"
type: guide
status: experimental
owner: founder
last_reviewed: 2026-10-31
review_every_days: 180
---

# Stage 4: Reconcile

**Purpose.** Three agents and a video will disagree. This stage settles every disagreement with evidence and writes one report that the build can trust. It is the step most teams skip, and the one that stopped four wrong beliefs reaching our spec.

**Case.** From about 22:15 to 22:45 on 30 October, the director (Claude Opus 5.5) read A, B and C, checked the contested points against captured data, and wrote `RE-REPORT.md` for oryzo.ai (by [Lusion](https://oryzo.ai)).

## Inputs → outputs

| In | Out |
| --- | --- |
| `notes/A-code.md`, `B-runtime.md`, `C-tokens.md` | `RE-REPORT.md`: one reconciled report |
| `MOTION-PLAN.md` hypotheses, `captures/`, `inventory/` | A **corrections table**: earlier claim, corrected claim, evidence |
| | An **unknowns** list and an ordered rebuild checklist |

## The evidence order

**Code > measured data > video.** Code states the rule. Measured data confirms it. Video suggests it. When two sources differ, the higher one wins unless you can show it is out of scope (see the desk example below). The checklist template is [reconcile-checklist.md](../agent-system/templates/reconcile-checklist.md).

## Steps

1. **List every claim that more than one source touches.** Put them in a table: claim, source A, source B, source C, video.
2. **Mark the conflicts.** Any row where two sources disagree, or where a claim comes only from the video, needs a check.
3. **Resolve by the cheapest decisive check.** Usually that is plotting or grepping a number you already have: one channel from `scroll-steps.json` against scroll position, one formula against its measured curve, one network entry against the code that requests it.
4. **Check scope.** An asset in the network log is not necessarily in your section. Trace it to the code that uses it.
5. **Write the corrections table.** Earlier claim → corrected claim → the evidence. Show the table in the report; people learn from it.
6. **Mark each effect** *answered*, *partial* or *unresolved*, and list what would settle the partial ones.
7. **Keep the tags.** The report restates every fact as `[code]`, `[measured]` or `[inferred]`.
8. **Write the ordered rebuild checklist.** It feeds stage 5.

## The corrections we made

| Earlier claim | Source | What we found | Evidence that decided it |
| --- | --- | --- | --- |
| The glow is triggered by hovering the hand | Video, and our own first hypothesis | It is driven by scroll. It switches on between 4,950 and 5,400 px and off between 6,750 and 7,200 px. Hover moves only the fingers | The code, and the glow channel in B's captures |
| The desk is real 3D, with Gaussian splats | Agent C, from the network log | The splats and the 3D table belong to a later scene. The hero desk is a 2D composite: a 3,296×1,460 base photo plus seven prop sprites | The code that requests those assets |
| The hand's catch is a time-driven animation | Agent B | It is scrubbed: the hand's animation ratio rises linearly with scroll from 3,056 to 4,950 px. B's own data showed it; its frame matching (32×20 greyscale thumbnails of dark frames) was unreliable | B's captured channel against scroll |
| The reference video is linear | The video | It is not: the founder scrolled down, up and down again | Matching frames to steps; only three early frames mapped cleanly |

## Common traps

- **A confident wrong agent.** Two of the three agents were wrong on one point each, and neither flagged any doubt. The cure is not distrust, it is the order: code first, then data.
- **Believing the network log.** *Ours: C's "real 3D with splats".* A request is not a use. Trace the request to the code path and the section.
- **Weak instruments.** Frame matching on dark images with tiny thumbnails produced the "time-driven" error. When an instrument is crude, prefer a channel the page itself exposes.
- **Reconciling in conversation.** We did it live, and it worked, but it left no table. Write the table.
- **Silently dropping an unknown.** The wheel follower was about 7 per second measured against a coefficient of 12 in the code. The keys matched the code (12). We kept both numbers and listed the gap as an unknown to settle by side-by-side comparison in stage 8.

## Done when

- [ ] Every claim touched by two or more sources has a row, and every conflict a resolution with evidence.
- [ ] The corrections table is in the report.
- [ ] Every number is tagged, and every `[inferred]` states what would confirm it.
- [ ] Each effect is marked answered, partial or unresolved.
- [ ] The unknowns list exists, including licence and font issues found by agent C.
- [ ] The rebuild checklist is ordered, and the report's own scope matches `scope.md`.

## Tools

| Tool | Use |
| --- | --- |
| The director (the strongest model you have) | Reads all notes, designs the checks, writes the report |
| Small scripts | Plot or diff one channel; grep one number |
| `reverse-engineer-anything` skill (REA) | Re-open the code for a contested point |
| `ffmpeg` | Compare a reference frame with a step image |

Templates: [reconcile-checklist.md](../agent-system/templates/reconcile-checklist.md), [re-report-template.md](../agent-system/templates/re-report-template.md). Prompt: [prompt-pack, stage 4](../tracks/ai-builder/prompt-pack.md#stage-4-reconcile). Next: [stage 5, Spec](05-spec.md).
