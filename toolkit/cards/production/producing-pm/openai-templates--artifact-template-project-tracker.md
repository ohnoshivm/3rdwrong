---
title: Artifact-Template-Project-Tracker
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: openai-templates:artifact-template-project-tracker
department: production
sub_department: producing-pm
job: project-tracking
role: lead
trigger: ""
kind: plugin-skill
availability: codex
distribution: manual
source: /Users/hustle/.codex/plugins/cache/openai-curated-remote/openai-templates/0.1.1/skills/artifact-template-project-tracker/SKILL.md
invoke: "artifact-template-project-tracker skill"
pairs_with: [agency:project-management-project-shepherd]
---
# Artifact-Template-Project-Tracker

The 3RDWRONG tool for {job.replace("-"," ")} — lead.

## What it does

- Creates a project tracker using the named template and retained reference file.
- Use the template to organise project tracking information.
- Template-specific fields beyond its source are not documented.

## When to use

- At approved project tracking hand-off, before the studio commits or ships the work.
- When the project record needs a consistent production method.

## When not to use

- Not a substitute for approved strategy, human decisions or independent review. Use the appropriate job lead before activating a specialist.

## Inputs it needs

- Approved brief and decision to support.
- Source material, scope and constraints relevant to the tool; identify gaps rather than fill them.

## How to run it

1. Invoke with `artifact-template-project-tracker skill`; confirm availability and required setup in the host.
2. Supply the inputs above and request the source-defined workflow and output.
3. Review evidence, assumptions and limitations with a separate person or agent.
4. File only anonymised, rights-cleared material in the public studio repository.

```text
Use artifact-template-project-tracker skill. Job: project-tracking. Project: {project}. Decision: {decision}. Inputs: {source links or files}. Constraints: {scope, timing, access}. Follow the tool’s documented workflow only. Mark claims Documented, Interpretation, Hypothesis or Unknown; identify gaps. Return the source-defined output and a concise next step. Do not invent findings or capabilities.
```

## What good output looks like

- A usable project tracking deliverable that follows the tool source and answers the stated decision.
- Inputs, evidence, assumptions and unresolved questions remain traceable.

## Quality checks

- [ ] A reviewer other than the maker checks the deliverable.
- [ ] Claims and unknowns are traceable to supplied sources.
- [ ] Scope and human decision ownership are clear.

## Pairs with

- Upstream: `agency:project-management-project-shepherd` — supplies or frames relevant context.

## Limits and cautions

- Source limitations: do not claim capabilities, outcomes or invocation details absent from the tool file.
- Distribution or connection requires setup or sign-in; the inventory does not verify live connectivity.
- Keep client data and personal information outside the public repository.
- This tool cannot approve its own work; use a separate checker and retain human decisions.
