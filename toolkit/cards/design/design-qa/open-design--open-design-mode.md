---
title: Open Design Mode
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: open-design:open-design-mode
department: design
sub_department: design-qa
job: visual-qa-browser
role: specialist
trigger: "when inspecting an existing interface and making evidence-based design changes"
kind: plugin-skill
availability: codex
distribution: vendor
source: toolkit/vendor/plugin-openai-curated-remote-open-design-0.5.2/skills/open-design-mode
invoke: "Open Design MCP: collect_brief, then the workflow calls with its pluginWorkflowId"
pairs_with: [skill:ceos-visual-audit, skill:reviewing-interface-quality, design-steward:verify]
---
# Open Design Mode

Open Design Mode is a 3RDWRONG tool for creating and refining websites, slides, prototypes and design systems through the local Open Design MCP; its registry placement is disputed by its source.

## What it does

- Creates and refines websites, slides, prototypes and design systems through the local Open Design MCP.
- Uses Open Design Cloud by default; Local Codex and secure BYOK require the user to select that mode.
- Starts one attributed brief workflow with the exact external context and carries its server-issued workflow ID through the run.
- Does not silently switch execution mode after authentication, transport, quota or generation failures.

## When to use

- when inspecting an existing interface and making evidence-based design changes. The source instead describes artifact creation/refinement; use it only when the requested work is to create or continue an artifact, and use a QA tool for inspection.

## When not to use

- Do not use it to audit or verify a rendered interface; use `skill:ceos-visual-audit` or `agent:visual-qa-engineer`. The source is for creating or refining an artifact.

## Inputs it needs

- A confirmed artifact brief, output type, execution mode and the locally registered Open Design MCP.
- The MCP’s server-issued `pluginWorkflowId`; preserve it through login, project selection, generation and delivery.

## How to run it

1. Resolve the requested execution mode before collecting the brief; Cloud is default, Local Codex/BYOK require explicit selection.
2. Call `collect_brief` once with the required external context and locale; preserve its workflow ID.
3. Pass the same ID to every follow-up call and keep the selected mode for the whole generation.
4. On a mode failure, report it and ask before switching; do not repeat the brief call to replace its workflow.

```text
Use the Open Design MCP to create or refine {{artifact}} from this brief: {{approved scope and constraints}}. Execution mode: {{Open Design Cloud | Local Codex | secure BYOK}}. Keep one attributed workflow and preserve its returned workflow ID through delivery. Do not change execution mode without explicit user choice.
```

## What good output looks like

- Brief collection occurs once with the exact external context and a normalized locale.
- The same server-issued workflow ID is used for all later steps.
- The selected execution mode remains consistent through generation and delivery.

## Quality checks

- [ ] MCP registration and runtime are available; no remote MCP or guessed localhost endpoint is substituted.
- [ ] Mode, external context, locale and workflow ID are preserved.
- [ ] Failures do not trigger a silent mode switch or duplicate brief request.

## Pairs with

- Pair with `skill:ceos-visual-audit` or `agent:visual-qa-engineer` after the artifact is rendered; those tools inspect the result against its intended design.

## Limits and cautions

- Registry places this under `visual-qa-browser`, but the source describes artifact creation/refinement; it is not a visual QA tool.
- Keep client data out of the public repository under D-0021. Honor rights and the selected provider’s account/data terms.
- Requires the locally registered `open-design` MCP and an installed Open Design runtime. Cloud, Local Codex and BYOK use distinct accounts/modes; never switch modes without explicit user choice. Availability records source presence, not authentication or connectivity.
