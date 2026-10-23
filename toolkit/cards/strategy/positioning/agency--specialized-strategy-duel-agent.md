---
title: Strategy Duel Agent
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:specialized-strategy-duel-agent
department: strategy
sub_department: positioning
job: positioning-proof
role: specialist
trigger: "Stress-test a positioning by arguing both sides; treat simulated scores as hypotheses and verify factual claims independently."
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/specialized-strategy-duel-agent.md
invoke: "Agent tool: Strategy Duel Agent"
pairs_with: [skill:positioning-mapper, skill:positioning-truth-tracer]
---
# Strategy Duel Agent

The 3RDWRONG tool for {job.replace("-"," ")} — specialist when Stress-test a positioning by arguing both sides; treat simulated scores as hypotheses and verify factual claims independently.

## What it does

- Argues both sides of a positioning to expose trade-offs.
- Produces simulated arguments or scores as hypotheses.
- Requires independent evidence checks for factual claims.

## When to use

- Stress-test a positioning by arguing both sides; treat simulated scores as hypotheses and verify factual claims independently.
- Use evidence to move from observed cue → interpretation → intended identity meaning; keep each step distinguishable.
- If based on 5–8 interviews, record hypotheses for later testing, never audience facts or prevalence.

## When not to use

- Not a substitute for approved strategy, human decisions or independent review. For evidence collection use `skill:3w-brand-discovery` or `skill:ux-research` where appropriate.

## Inputs it needs

- Approved brief and decision to support.
- Source material, scope and constraints relevant to the tool; identify gaps rather than fill them.
- For perception work, identify the cue, context and intended identity question; separate observation from interpretation.

## How to run it

1. Invoke with `Agent tool: Strategy Duel Agent`; confirm availability and required setup in the host.
2. Supply the inputs above and request the source-defined workflow and output.
3. Review evidence, assumptions and limitations with a separate person or agent.
4. File only anonymised, rights-cleared material in the public studio repository.

```text
Use Agent tool: Strategy Duel Agent. Job: positioning-proof. Project: {project}. Decision: {decision}. Inputs: {source links or files}. Constraints: {scope, timing, access}. Follow the tool’s documented workflow only. Mark claims Documented, Interpretation, Hypothesis or Unknown; identify gaps. Return the source-defined output and a concise next step. Do not invent findings or capabilities.
```

## What good output looks like

- A usable positioning proof deliverable that follows the tool source and answers the stated decision.
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

- Upstream: `skill:positioning-mapper` — supplies or frames relevant context.
- Downstream/check: `skill:positioning-truth-tracer` — develops or independently checks the hand-off.

## Limits and cautions

- Source limitations: do not claim capabilities, outcomes or invocation details absent from the tool file.
- Label evidence **Documented**, **Interpretation**, **Hypothesis** or **Unknown**; perception cues are not identity meaning until interpreted.
- Five to eight interviews generate hypotheses, not facts; do not claim representativeness or prevalence.
- Keep client data and personal information outside the public repository.
- This tool cannot approve its own work; use a separate checker and retain human decisions.
