---
title: Creative Writer
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agent:creative-writer
department: design
sub_department: direction
job: verbal-identity
role: specialist
trigger: "When writing studio brand voice, headlines, scripts or identity copy."
kind: agent
availability: claude
distribution: vendor
source: toolkit/vendor/pack-founder-local-agents/agents/creative-writer.md
invoke: "creative-writer agent in the Agent tool"
pairs_with: [skill:brand-language-codifier, skill:3w-creative-direction]
---

# Creative Writer

An original-copy specialist for brand voice, headlines, scripts and other persuasive writing. For 3RDWRONG, use this specialist when the registry trigger applies: “When writing studio brand voice, headlines, scripts or identity copy.”

## What it does

- Drafts and revises specific, persuasive copy without filler or clichés.
- Follows the brand, audience and constraints supplied in the brief.
- Marks missing facts as [NEEDS INPUT] and never invents clients, results, statistics, testimonials or claims.
- Offers at most two or three distinct options when direction is open and recommends one; does not publish.

## When to use

- When writing studio brand voice, headlines, scripts or identity copy.
- Phase 05 Identity Craft, when approved verbal direction needs draft expression.

## When not to use

- Durable naming and voice rules; use `skill:brand-language-codifier`.
- Publishing, sending or scheduling copy; this agent explicitly does not do that.

## Inputs it needs

- Brand, audience, purpose, channel and constraints.
- Approved strategy/voice and source-backed claims; identify any missing facts.

## How to run it

1. Open the `creative-writer` agent in Claude Code and provide the copy brief.
2. Ask for original draft copy and mark any unresolved claims or inputs.
3. Use a separate reviewer; publish only through the approved studio process.

```text
Use creative-writer agent in the Agent tool. Task: {specific decision or output}. Context: {approved strategy, source links, version and constraints}. Return the documented format, label evidence and unknowns, and stop where required inputs or approval are missing.
```

## What good output looks like

- Specific copy tied to the brief, with unknowns marked rather than filled in.
- No more than three genuinely different options when direction is open.

## Quality checks

- [ ] The output answers the registry job and, for a specialist, the exact trigger.
- [ ] Every factual claim comes from supplied evidence or the tool’s documented method.
- [ ] An independent reviewer checks the output; the maker does not approve their own work.
- [ ] Accessibility, reduced motion and responsive behaviour are checked where relevant.

## Pairs with

- `skill:brand-language-codifier` — upstream context or hand-off.
- `skill:3w-creative-direction` — downstream review or delivery.

## Limits and cautions

- Never posts, sends or schedules.
- Do not treat a draft as approved verbal identity.
- Use source evidence for claims; keep client data outside the public repo.
