---
title: Organizational Psychologist
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:organizational-psychologist
department: operations
sub_department: people-partners
job: team-development
role: lead
trigger: ""
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/organizational-psychologist.md
invoke: "Agent tool: `organizational-psychologist` (Claude Code)"
pairs_with: []
---
# Organizational Psychologist

The lead for team development at 3RDWRONG, supporting people partners work.

## What it does

- Applied organizational psychologist who diagnoses team dynamics, psychological safety, burnout risk, and culture health — using evidence-based frameworks to help leaders build high-performing, resilient, and…
- Distinguishes symptom from cause: "Attrition is the symptom. Let's check the Job Demands-Resources balance before we assume it's pay."
- Cites the evidence plainly, without lecturing: "Edmondson's data is clear here — punishing the messenger is the fastest way to kill the early-warning signals you most need."
- Comfortable saying "that intervention will backfire" and explaining why a sequence (e.g., trust before conflict) can't be skipped.

## When to use

- Use for team development in Phase 02 Research or the relevant production / hand-off phase when the request matches the documented scope.

## When not to use

- Do not use when the request falls outside team development or fails the registered specialist trigger.
- Do not use its output as client approval, verified research or professional advice.

## Inputs it needs

- A bounded task brief, relevant context, constraints and expected deliverable.
- Only provide files and information needed for the task.

## How to run it

1. Check the task against the registered job and trigger.
2. Read the source instructions and provide the minimum necessary inputs.
3. Invoke the tool using the name above and request the required artefact.
4. Have a separate reviewer check evidence, accuracy, privacy and fit before hand-off.

```text
Use agency:organizational-psychologist. Task: {task}. Project phase: {phase}. Context and source material: {links/files and constraints}. Deliverable: {format and audience}. Follow the tool's documented instructions; distinguish evidence from interpretation, state unknowns and do not claim approval.
```

## What good output looks like

- The deliverable addresses the requested task and follows the source-documented workflow.
- Facts, assumptions and unknowns are distinguishable; no capability is implied beyond the source.

## Quality checks

- [ ] The task fits the registry job and any specialist trigger.
- [ ] A reviewer other than the maker checked the output and source evidence.
- [ ] Assumptions and unknowns are visible; unsupported claims are removed.
- [ ] No client-confidential data or personal information entered the public repository.

## Pairs with

- No paired tool is registered for this job in the assigned scope.

## Limits and cautions

- Capabilities are limited to those documented in the source; ask for unknown details rather than assuming them.
- Human review remains responsible for factual accuracy, suitability and approval.
- Distribution: vendor; availability: repo. Confirm setup or sign-in requirements before relying on the tool.
