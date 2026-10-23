---
title: Hr Onboarding
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:hr-onboarding
department: operations
sub_department: people-partners
job: recruitment-onboarding
role: specialist
trigger: "Use for operations/people-partners/recruitment-onboarding when the brief specifically requires: Comprehensive HR onboarding specialist for employee orientation, documentation management, compliance tracking, benefits enrollment, culture integration, and new hire support — delivering a seamless first-day-to-first-year experience that drives retention and productivity ."
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/hr-onboarding.md
invoke: "Agent tool: `hr-onboarding` (Claude Code)"
pairs_with: [agency:recruitment-specialist]
---
# Hr Onboarding

A specialist for recruitment onboarding at 3RDWRONG, called when Comprehensive HR onboarding specialist for employee orientation, documentation management, compliance tracking, benefits enrollment, culture integration, and new hire support — delivering a seamless first-day-to-first-year experience that drives retention and productivity.

## What it does

- Comprehensive HR onboarding specialist for employee orientation, documentation management, compliance tracking, benefits enrollment, culture integration, and new hire support — delivering a seamless…
- The new hire's name, role, department, start date, and manager
- Which onboarding steps have been completed and which are outstanding
- The company's specific onboarding workflow, policies, and culture

## When to use

- Use for operations/people-partners/recruitment-onboarding when the brief specifically requires: Comprehensive HR onboarding specialist for employee orientation, documentation management, compliance tracking, benefits enrollment, culture integration, and new hire support — delivering a seamless first-day-to-first-year experience that drives retention and productivity .
- In a 3RDWRONG project, use during the relevant recruitment onboarding task and pass its output to the project owner for review.

## When not to use

- Do not use when the request falls outside recruitment onboarding or fails the registered specialist trigger.
- Do not use its output as client approval, verified research or professional advice.
- For the paired agency:recruitment-specialist work, use that tool and hand off this artefact.

## Inputs it needs

- A bounded task brief, relevant context, constraints and expected deliverable.
- Only provide files and information needed for the task.

## How to run it

1. Check the task against the registered job and trigger.
2. Read the source instructions and provide the minimum necessary inputs.
3. Invoke the tool using the name above and request the required artefact.
4. Have a separate reviewer check evidence, accuracy, privacy and fit before hand-off.

```text
Use agency:hr-onboarding. Task: {task}. Project phase: {phase}. Context and source material: {links/files and constraints}. Deliverable: {format and audience}. Follow the tool's documented instructions; distinguish evidence from interpretation, state unknowns and do not claim approval.
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

- `agency:recruitment-specialist` — coordinate the hand-off for the same job; pass the artefact and constraints.

## Limits and cautions

- Capabilities are limited to those documented in the source; ask for unknown details rather than assuming them.
- Human review remains responsible for factual accuracy, suitability and approval.
- Distribution: vendor; availability: repo. Confirm setup or sign-in requirements before relying on the tool.
