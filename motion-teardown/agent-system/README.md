---
title: "Give an agent an evidence trail, then a build contract"
type: guide
status: experimental
owner: founder
last_reviewed: 2026-10-31
review_every_days: 180
---

# Give an agent an evidence trail, then a build contract

This folder is the machine-usable part of Motion Teardown. It is designed for Claude Code, Codex and OpenCode. The skill coordinates eight stages and loads detailed instructions only when needed.

## Canonical skill

The skill lives at [skills/3w-motion-teardown](../../skills/3w-motion-teardown/SKILL.md), with its stage references alongside. This folder holds the templates, schemas and scripts; it contains no duplicate skill. The repository registers Claude discovery through `.claude/skills/3w-motion-teardown`. For other hosts, link the canonical directory without overwriting an existing skill, and keep this repository checkout in place so its publication resources resolve.

Install `watch` and `reverse-engineer-anything` / REA separately from their upstreams or your existing skill collection. Read their installed SKILL.md before using them; capabilities and video privacy choices belong to those skills. See the credits in the [repo README](../README.md). No API key is required for local frames and Playwright captures.

## Invoke

```text
Use 3w-motion-teardown to study {{URL}}, from {{START_SECTION}} through
{{END_SECTION}}. Recording: {{VIDEO_PATH_OR_NONE}}.
Write local evidence to {{STUDY_DIR}}. Build target: {{PROJECT_DIR_OR_NONE}}.
Public output must use original code and licensed or generated assets.
```

Replace every `{{PLACEHOLDER}}` in the [templates](templates/) before assigning a worker. The [skill](../../skills/3w-motion-teardown/SKILL.md) is the entry point. [Schemas](schemas/README.md) define the hand-off formats; [scripts](scripts/README.md) produce raw capture evidence, which must be reconciled before it becomes a spec.

## Routing is a capability choice

| Work | Default | Recovery |
| --- | --- | --- |
| Video | Installed watch skill with its configured engine | If a cloud engine fails, report it and ask before switching engines; local frames are an explicit option |
| Static code | REA + source searches; separate worker A | Follow REA recovery once; use local bundle searches if unavailable and record the limit |
| Runtime | Worker B, Playwright and real browser | Mirror known successful assets, then replay; record unresolved loads rather than wait indefinitely |
| Tokens and inventory | Worker C with its own browser context | Read available computed styles while runtime work continues |
| DOM / GL build | Separate owners, routine reasoning effort `high` | Resume from disk on an available, authorised provider; do not silently change a user-selected model |
| Images | A worker with the requested image tool | Stop the image lane with `NO_IMAGE_TOOL`; sized placeholders unblock other lanes |
| QA | Separate observer while build proceeds | Use existing checkpoints and log defects; do not edit another worker's files |

Keep a progress ledger per worker and a [resume note](templates/resume-note.md). Inspect files after a connection loss before rerunning work. Cancel stale retries when replacing a worker. If parallel workers are unavailable, perform the lanes sequentially with the same ownership and evidence boundaries; report the change. The skill is a workflow, not a guarantee of quotas, tools or GPU access.
