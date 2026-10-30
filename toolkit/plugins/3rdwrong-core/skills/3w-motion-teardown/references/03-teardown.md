---
title: "3. Teardown: three independent evidence lanes"
type: guide
status: experimental
owner: founder
last_reviewed: 2026-10-31
review_every_days: 180
---

# 3. Teardown: three independent evidence lanes

Read reverse-engineer-anything and its JavaScript/runtime references. Discover
available tools; use summary-first analysis with retained evidence IDs. If its
recovery path fails, document the fallback and use local source searches and
Playwright. Do not claim a static trace observed execution.

Assign templates `agent-a-static.md`, `agent-b-runtime.md`, `agent-c-tokens.md`
from the start. Each worker owns separate notes, inventory files and a ledger.
A reads loader, scroll and renderer code first, sharing the loading finding
without editing B's files. B records requests and prepares hooks in parallel;
C records tokens and verifies which assets belong to which section.

Private mirror: `mirror.mjs --mode record`, then `--mode replay` or capture
with `--mirror`. Record only public GET responses in declared origins. Review
failures and missing assets. Replay does not fetch files the recording never
received. Never invent a response, remove a gate, or mistake an overlay hidden
with CSS for a running app. If unavailable assets prevent boot, record partial
results and move to other evidence. Bound loader waits; do not retry forever.

Capture: inject `hooks.js` before scripts, retain exact original URL identity,
then `capture-steps.mjs` with `window.scrollTo`. Capture both directions with
the same element identities. Save requested/actual y, settle status, screenshots,
computed styles and observable world transforms, cameras, bones and uniforms.
An empty devtools channel is an instrumentation limit, not proof of no 3D.
Raw shader strings remain in memory by default; never publish dumps.

Measure wheel and keys separately with trusted browser input. For pointer
claims, park at a fixed y: still pointer, recorded sweep, still pointer again;
then repeat at a different y. Sample after a reload for intro timing. Isolate
time, pointer and scroll as competing drivers. Keep idle time channels out of
the settle signature using an explicitly logged exclusion when necessary.

Exit: A/B/C answered/partial/unresolved tables, local evidence and ledgers.
