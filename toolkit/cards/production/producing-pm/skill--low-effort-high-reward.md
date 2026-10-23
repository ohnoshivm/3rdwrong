---
title: Low-Effort-High-Reward
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:low-effort-high-reward
department: production
sub_department: producing-pm
job: project-planning
role: specialist
trigger: "When triaging a concrete studio or client backlog against effort and reward."
kind: skill
availability: codex
distribution: manual
source: /Users/hustle/.agents/skills/low-effort-high-reward/SKILL.md
invoke: "low-effort-high-reward skill"
pairs_with: [agency:project-management-project-shepherd, openai-templates:artifact-template-project-tracker]
---
# Low-Effort-High-Reward

The 3RDWRONG tool for {job.replace("-"," ")} — specialist when When triaging a concrete studio or client backlog against effort and reward.

## What it does

- Helps triage a concrete backlog against effort and reward.
- Makes candidate quick wins visible for discussion.
- Effort and reward estimates remain assumptions unless evidenced.

## When to use

- When triaging a concrete studio or client backlog against effort and reward.

## When not to use

- Not a substitute for approved strategy, human decisions or independent review. Use the appropriate job lead before activating a specialist.

## Inputs it needs

- Approved brief and decision to support.
- Source material, scope and constraints relevant to the tool; identify gaps rather than fill them.

## How to run it

1. Invoke with `low-effort-high-reward skill`; confirm availability and required setup in the host.
2. Supply the inputs above and request the source-defined workflow and output.
3. Review evidence, assumptions and limitations with a separate person or agent.
4. File only anonymised, rights-cleared material in the public studio repository.

```text
Use low-effort-high-reward skill. Job: project-planning. Project: {project}. Decision: {decision}. Inputs: {source links or files}. Constraints: {scope, timing, access}. Follow the tool’s documented workflow only. Mark claims Documented, Interpretation, Hypothesis or Unknown; identify gaps. Return the source-defined output and a concise next step. Do not invent findings or capabilities.
```

## What good output looks like

- A usable project planning deliverable that follows the tool source and answers the stated decision.
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
