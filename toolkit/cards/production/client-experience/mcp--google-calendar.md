---
title: Google Calendar
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: mcp:google-calendar
department: production
sub_department: client-experience
job: meeting-cadence
role: specialist
trigger: "Use when the approved work needs this capability: Configured MCP server: google calendar. Transport details and credentials are not inventoried"
kind: mcp
availability: mcp
distribution: manual
source: /Users/hustle/.claude/plugins/synced/88e7af4e-a2cf-4b40-8488-91a856697e04_aa2d1473-adba-46ff-9558-93fbf2ea6240/2da0c8d9-1e96-4394-b0f4-3249613186f8/.mcp.json
invoke: "MCP server: google-calendar (operation names not documented)"
pairs_with: [agency:project-management-project-shepherd, openai-templates:artifact-template-project-tracker]
---
# Google Calendar

The 3RDWRONG tool for {job.replace("-"," ")} — specialist when Use when the approved work needs this capability: Configured MCP server: google calendar. Transport details and credentials are not inventoried.

## What it does

- Configured Google Calendar MCP server is listed in the source inventory.
- Tool actions and transport details are not documented in the source material.
- Connectivity and available operations are not verified.

## When to use

- Use when the approved work needs this capability: Configured MCP server: google calendar. Transport details and credentials are not inventoried.

## When not to use

- Not a substitute for approved strategy, human decisions or independent review. Use the appropriate job lead before activating a specialist.

## Inputs it needs

- Approved brief and decision to support.
- Source material, scope and constraints relevant to the tool; identify gaps rather than fill them.

## How to run it

1. Invoke with `MCP server: google-calendar (operation names not documented)`; confirm availability and required setup in the host.
2. Supply the inputs above and request the source-defined workflow and output.
3. Review evidence, assumptions and limitations with a separate person or agent.
4. File only anonymised, rights-cleared material in the public studio repository.

```text
Use MCP server: google-calendar (operation names not documented). Job: meeting-cadence. Project: {project}. Decision: {decision}. Inputs: {source links or files}. Constraints: {scope, timing, access}. Follow the tool’s documented workflow only. Mark claims Documented, Interpretation, Hypothesis or Unknown; identify gaps. Return the source-defined output and a concise next step. Do not invent findings or capabilities.
```

## What good output looks like

- A usable meeting cadence deliverable that follows the tool source and answers the stated decision.
- Inputs, evidence, assumptions and unresolved questions remain traceable.

## Quality checks

- [ ] A reviewer other than the maker checks the deliverable.
- [ ] Claims and unknowns are traceable to supplied sources.
- [ ] Scope and human decision ownership are clear.

## Pairs with

- Upstream: `agency:project-management-project-shepherd` — supplies or frames relevant context.
- Downstream/check: `openai-templates:artifact-template-project-tracker` — develops or independently checks the hand-off.

## Limits and cautions

- Source limitations: do not claim capabilities, outcomes or invocation details absent from the tool file.
- Distribution or connection requires setup or sign-in; the inventory does not verify live connectivity.
- Keep client data and personal information outside the public repository.
- This tool cannot approve its own work; use a separate checker and retain human decisions.
