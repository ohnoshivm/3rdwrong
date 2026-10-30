---
title: "7. Parallel build: own files, share state"
type: guide
status: experimental
owner: founder
last_reviewed: 2026-10-31
review_every_days: 180
---

# 7. Parallel build: own files, share state

Use DOM, GL and image briefs. Routine code uses reasoning effort `high`, not
`max`; specialised problems can be escalated when there is a concrete need.
No worker changes another owner's files, contract or dependencies. Contract
changes return to the director, who versions the interface and updates consumers.

DOM owns scroll integration, scalar calculation, semantic content and styles.
GL consumes immutable per-frame state and owns its renderer, scenes and shaders.
IMG owns only manifest-listed assets and generation recipes. The director owns
scaffold and integration unless explicitly assigned elsewhere before launch.
One loop calls both sides; never add smoothing to every effect.

Get the first representative slice running early. Start QA with `qa-brief.md`
at that point while workers continue. QA logs defects to its own files and sends
evidence to owners. It exercises reverse scroll, pointer isolation, resized
layout, reduced motion, keyboard, missing assets and a renderer failure.

Readiness must settle within the specified deadline on success or failure.
Use asset error handlers, bounded waits and a DOM fallback. Save milestones
and exact commands in each ledger; use resume-note.md before any hand-off.
Exit: production build, functional tests, integrated checkpoints, QA defects.
