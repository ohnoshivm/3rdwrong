---
title: Cultural Intelligence Strategist
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:specialized-cultural-intelligence-strategist
department: strategy
sub_department: culture-behaviour
job: cultural-systems
role: lead
trigger: ""
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/specialized-cultural-intelligence-strategist.md
invoke: "Agent tool: Cultural Intelligence Strategist"
pairs_with: [skill:3w-brand-discovery, skill:ux-research-methods]
---
# Cultural Intelligence Strategist

The 3RDWRONG tool for {job.replace("-"," ")} — lead.

## What it does

- Provides cultural intelligence and originality audit expertise.
- Interprets the cultural question within the approved scope.
- Calls for local or informed review where the source requires it.

## When to use

- Phase 01 Discovery, as the lead for cultural systems.
- Phase 03 Strategy, as the lead for cultural systems.
- Use evidence to move from observed cue → interpretation → intended identity meaning; keep each step distinguishable.
- If based on 5–8 interviews, record hypotheses for later testing, never audience facts or prevalence.

## When not to use

- Not a substitute for approved strategy, human decisions or independent review. For evidence collection use `skill:3w-brand-discovery` or `skill:ux-research` where appropriate.

## Inputs it needs

- Approved brief and decision to support.
- Source material, scope and constraints relevant to the tool; identify gaps rather than fill them.
- For perception work, identify the cue, context and intended identity question; separate observation from interpretation.

## How to run it

1. Invoke with `Agent tool: Cultural Intelligence Strategist`; confirm availability and required setup in the host.
2. Supply the inputs above and request the source-defined workflow and output.
3. Review evidence, assumptions and limitations with a separate person or agent.
4. File only anonymised, rights-cleared material in the public studio repository.

```text
Use Agent tool: Cultural Intelligence Strategist. Job: cultural-systems. Project: {project}. Decision: {decision}. Inputs: {source links or files}. Constraints: {scope, timing, access}. Follow the tool’s documented workflow only. Mark claims Documented, Interpretation, Hypothesis or Unknown; identify gaps. Return the source-defined output and a concise next step. Do not invent findings or capabilities.
```

## What good output looks like

- A usable cultural systems deliverable that follows the tool source and answers the stated decision.
- Inputs, evidence, assumptions and unresolved questions remain traceable.
- Perception is stated as cue → interpretation → intended identity meaning, with evidence status visible.
- A 5–8 interview sample yields testable hypotheses only, not audience facts.

## Quality checks

- [ ] A reviewer other than the maker checks the deliverable.
- [ ] Claims and unknowns are traceable to supplied sources.
- [ ] Scope and human decision ownership are clear.
- [ ] Interpretation is not presented as observation or established audience fact.
- [ ] Small-sample interviews are reported as hypotheses, not prevalence.

## Pairs with

- Upstream: `skill:3w-brand-discovery` — supplies or frames relevant context.
- Downstream/check: `skill:ux-research-methods` — develops or independently checks the hand-off.

## Limits and cautions

- Source limitations: do not claim capabilities, outcomes or invocation details absent from the tool file.
- Label evidence **Documented**, **Interpretation**, **Hypothesis** or **Unknown**; perception cues are not identity meaning until interpreted.
- Five to eight interviews generate hypotheses, not facts; do not claim representativeness or prevalence.
- Keep client data and personal information outside the public repository.
- This tool cannot approve its own work; use a separate checker and retain human decisions.
