---
title: "Failure routing and resume"
type: guide
status: experimental
owner: founder
last_reviewed: 2026-10-31
review_every_days: 180
---

# Failure routing and resume

| Failure | Next action | Preserve |
| --- | --- | --- |
| Quota or allowance | Record error; use an already authorised available provider. Ask only if cost/model choice is new | Completed files and the next bounded task |
| DNS / transport loss | Inspect disk and ledger; one changed-input retry if justified; resume on authorised route | Evidence IDs, partial captures, failed command |
| Video engine unavailable | Follow watch's engine-switch/privacy rules; offer local frames | Engine/error, original media identity |
| Loader never completes | Read code and failed request list; replay successful local assets; stop bounded wait if still incomplete | Missing URLs, loader state, partial evidence |
| No real GPU | Record software renderer; use static analysis and available captures | Renderer string; visuals/performance unverified |
| REA missing | Follow its recovery once; use source searches and Playwright | Tool availability and weaker evidence boundary |
| Image tool absent | Return NO_IMAGE_TOOL; keep other lanes on sized placeholders | Manifest and generation brief |
| Port binding denied | Use an already permitted local preview or report blocker; obey host access policy | Build result, exact error, command |
| Slow reasoning / no file progress | Narrow checkpoint and use high for routine code; replace only with authorisation | Read/complete/remaining lists |
| Replaced worker still retrying | Cancel stale retry through the host before replacement writes | Single-writer ownership |

Write one resume note per worker with template `resume-note.md`. Include the
root using portable paths, owner, contract version, commands and results,
complete/partial/missing files, outstanding questions, next action and stopped
worker identity. Never embed credentials, account names or full user paths.
On resumption verify existing files; do not scaffold over completed work.
