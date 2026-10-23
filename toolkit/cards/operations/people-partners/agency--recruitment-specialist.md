---
title: Recruitment Specialist
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:recruitment-specialist
department: operations
sub_department: people-partners
job: recruitment-onboarding
role: lead
trigger: ""
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/recruitment-specialist.md
invoke: "Agent tool: `recruitment-specialist` (Claude Code)"
pairs_with: [agency:hr-onboarding]
---
# Recruitment Specialist

The lead for recruitment onboarding at 3RDWRONG, supporting people partners work.

## What it does

- Expert recruitment operations and talent acquisition specialist — skilled in China's major hiring platforms, talent assessment frameworks, and labor law compliance. Helps companies efficiently attract, screen, and…
- Role**: Recruitment operations, talent acquisition, and HR compliance expert
- Personality**: Goal-oriented, insightful, strong communicator, solid compliance awareness
- Memory**: You remember every successful recruiting strategy, channel performance metric, and talent profile pattern

## When to use

- Use for recruitment onboarding in Phase 02 Research or the relevant production / hand-off phase when the request matches the documented scope.

## When not to use

- Do not use when the request falls outside recruitment onboarding or fails the registered specialist trigger.
- Do not use its output as client approval, verified research or professional advice.
- For the paired agency:hr-onboarding work, use that tool and hand off this artefact.

## Inputs it needs

- A bounded task brief, relevant context, constraints and expected deliverable.
- Only provide files and information needed for the task.

## How to run it

1. Check the task against the registered job and trigger.
2. Read the source instructions and provide the minimum necessary inputs.
3. Invoke the tool using the name above and request the required artefact.
4. Have a separate reviewer check evidence, accuracy, privacy and fit before hand-off.

```text
Use agency:recruitment-specialist. Task: {task}. Project phase: {phase}. Context and source material: {links/files and constraints}. Deliverable: {format and audience}. Follow the tool's documented instructions; distinguish evidence from interpretation, state unknowns and do not claim approval.
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

- `agency:hr-onboarding` — coordinate the hand-off for the same job; pass the artefact and constraints.

## Limits and cautions

- Capabilities are limited to those documented in the source; ask for unknown details rather than assuming them.
- Human review remains responsible for factual accuracy, suitability and approval.
- Distribution: vendor; availability: repo. Confirm setup or sign-in requirements before relying on the tool.
