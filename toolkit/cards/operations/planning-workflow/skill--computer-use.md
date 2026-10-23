---
title: computer-use
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:computer-use
department: operations
sub_department: planning-workflow
job: delivery-discipline
role: specialist
trigger: "Use when the approved work needs this capability: Read this skill before the first step of any request to do something in an app on the person's own computer (Notes, Finder, System Settings, any desktop app), to look at their screen, or for \\\"computer use\\\". Comput…"
kind: skill
availability: claude
distribution: manual
source: /Users/hustle/.claude/skills/synced/88e7af4e-a2cf-4b40-8488-91a856697e04_aa2d1473-adba-46ff-9558-93fbf2ea6240/computer-use/SKILL.md
invoke: "computer-use skill"
pairs_with: []
---
# computer-use

The computer-use tool supports 3RDWRONG specialist when Use when the approved work needs this capability: Read this skill before the first step of any request to do something in an app on the person's own computer (Notes, Finder, System Settings, any desktop app), to look at their screen, or for \"computer use\". Comput….

## What it does

- This is about what's available, not error handling: if a dedicated MCP tool errors, Claude debugs or reports it rather than silently retrying via a slower tier
- Some apps are granted at a restricted tier based on their category; the tier is displayed in the approval dialog and returned in the `request_access` (or `computer_request_access`) response:
- See the full URL before following any link.** Visible link text can be misleading; Claude hovers or inspects to get the real destination
- Inside Claude in Chrome or the built-in browser** Claude can click links with those browser tools, but the suspicion check still applies: it verifies unfamiliar URLs with the person

## When to use

- Use when the approved work needs this capability: Read this skill before the first step of any request to do something in an app on the person's own computer (Notes, Finder, System Settings, any desktop app), to look at their screen, or for \"computer use\". Comput…

## When not to use

- When the brief needs a different job than `delivery-discipline`; choose the registered tool for that job.
- Do not treat its output as independent verification when it produced the work.

## Inputs it needs

- The requested outcome, relevant project context, constraints and source material.
- Any criteria, data or decisions specified in the source instructions; otherwise: Not documented.

## How to run it

1. Confirm the source instructions and required access are available.
2. Invoke using the exact tool name above.
3. Give it the brief, context and acceptance criteria; review its evidence and handoff.

```text
Use computer-use skill. Job: delivery-discipline. Brief: {project brief}. Context and source materials: {links/files}. Constraints: {constraints}. Return the documented output, cite evidence, and label anything not supported as Not documented.
```

## What good output looks like

- Addresses the stated outcome and follows the source instructions.
- Separates documented evidence from assumptions and names unresolved inputs.
- Includes a useful next action or handoff where the source calls for one.

## Quality checks

- [ ] A reviewer confirms claims against source evidence.
- [ ] Assumptions and missing inputs are explicit.
- [ ] The result is reviewed by someone other than its maker when it is used to check work.

## Pairs with

- No registry pairings are documented. Handoff: share the brief, output and open questions with the next tool selected for the project.

## Limits and cautions

- Capabilities are limited to those stated in the tool file; details not stated there are Not documented.
- Distribution/access: follow the installed package and access rules.
- Keep client data out of the public repository (D-0021).
- Apply evidence labels: Documented, Interpretation, Hypothesis or Unknown; preserve human review for consequential decisions.
