---
title: Agency MCP
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: mcp:agency-mcp
department: marketing
sub_department: content-social
job: content-writing
role: specialist
trigger: "Use only when the named content, channel, lifecycle, or campaign task is explicitly in the approved marketing scope."
kind: mcp
availability: mcp
distribution: manual
source: /Users/hustle/.claude/plugins/synced/88e7af4e-a2cf-4b40-8488-91a856697e04_aa2d1473-adba-46ff-9558-93fbf2ea6240/32b58f4f-b004-46d1-8ac7-ec83653a20c6/.mcp.json
invoke: "MCP server `agency-mcp` (inspect the connected tool list before use)"
pairs_with: [skill:content-quality-auditor]
---
# Agency MCP

Agency MCP is a specialist for content-writing at 3RDWRONG, used when this trigger applies: Use only when the named content, channel, lifecycle, or campaign task is explicitly in the approved marketing scope.

## What it does

- Configures an HTTP MCP server named `agency-mcp`.
- Points the server configuration to the documented MCP endpoint.
- The configuration file does not describe the server's available tools or their behaviour.

## When to use

- Use only when the named content, channel, lifecycle, or campaign task is explicitly in the approved marketing scope.
- During approved studio content work for LinkedIn, Instagram, the studio journal or portfolio channels (Behance, Dribbble and X).

## When not to use

- Do not use for an unapproved campaign or to publish/schedule directly; the founder must approve every post.
- When the task belongs to another job, use its lead (`skill:content-writer`) or the more appropriate tool instead.

## Inputs it needs

- The approved brief, audience, objective, channel and desired deliverable.
- Relevant source material and evidence; mark unsupported claims Unknown or `[needs source]`.

## How to run it

1. Confirm the task is in the approved studio scope and gather the inputs above.
2. Invoke the tool in Claude Code or Codex using the command/agent/server shown above.
3. Review its output against the source material; hand it to a separate reviewer.
4. For any post or scheduled item, keep it in draft until the founder approves publication.

```text
Use MCP server `agency-mcp` (inspect the connected tool list before use) for this approved 3RDWRONG task: {task}. Context and source material: {links/files}. Target audience: {audience}. Desired output: {deliverable}. Label evidence as Documented, Interpretation, Hypothesis or Unknown where relevant. Do not publish or schedule anything; return a reviewable draft and list open questions.
```

## What good output looks like

- Directly addresses the approved brief and names assumptions or missing evidence.
- Gives a usable, reviewable deliverable with source links where claims require support.

## Quality checks

- [ ] A reviewer other than the maker checks claims, fit and completeness.
- [ ] Client or personal information is excluded from the public repository.
- [ ] Publication or scheduling remains blocked until founder approval.

## Pairs with

- `skill:content-quality-auditor` — receives the relevant draft, evidence or audit hand-off for its documented remit.

## Limits and cautions

- Capabilities and output depend on the tool’s source instructions and supplied inputs; do not infer undocumented features.
- Apply licence and installation/sign-in requirements for this distribution; availability does not prove a service is connected.
- Keep evidence labels distinct and separate maker from checker.
