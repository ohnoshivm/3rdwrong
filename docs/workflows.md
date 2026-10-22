---
title: Working workflows
type: guide
status: proposed
owner: founder
last_reviewed: 2026-10-22
---

# Working workflows

Use issues to frame work, branches and pull requests for substantive changes, and status metadata to show what remains uncertain. Use `type:*` labels for the work and `status:*` labels for its review state. Add `privacy-review` when a change contains sanitised project learning or could reveal sensitive context.

## 1. Add an agency study

Open a `type: research` issue with the agency's public source links and a specific question. Read `intelligence/README.md` and `templates/research/agency-study.md`. In a branch such as `research/studio-name`, create the study with `uv run python scripts/new_doc.py templates/research/agency-study.md intelligence/agencies/studio-name.md --title "Studio Name: agency study"`. Cite sources, distinguish observation from interpretation, keep it at `reference`, run the validator, and open a pull request.

## 2. Add a design reference

Open a `type: reference` issue with a direct link to the public work. Read `intelligence/README.md`, `templates/research/visual-system-analysis.md`, and the relevant category-code skill. Describe only observable details first. In a `reference/short-desc` branch, use `uv run python scripts/new_doc.py templates/research/visual-system-analysis.md intelligence/projects/work-name.md --title "Work Name: visual system analysis"`. Keep it a reference study, check source and image rights, then submit a pull request.

## 3. Start an identity project

Open a `type: project` issue and read `methods/identity-engagement/README.md`, `templates/projects/project-readme.md`, and `skills/brand-discovery/SKILL.md`. Create a private working branch or approved private workspace for client details; only add a sanitised public index when it is safe. Use `uv run python scripts/new_doc.py templates/projects/project-readme.md projects/examples/project-name/README.md --title "Project name"` for a cleared example. Keep delivery checkpoints proposed until approved by a human.

## 4. Update approved strategy

Open a `type: decision` issue before changing a strategic fact. Read `studio/decisions/README.md`, `docs/knowledge-governance.md`, and the affected strategy page. Add the next contiguous decision record with the required sections and status `proposed`; link it from the decision index. A founder reviews and records `approved_by`, `approved_on`, and the decision status in the pull request. Run the validator and do not publish the change as approved before that review.

## 5. Propose a method

Open a `type: method` issue describing the need, steps, evidence, limits, and human review. Read `methods/README.md`, `methods/learning-loop.md`, and `templates/learning/method-improvement.md`. Work in a `method/short-desc` branch, keep the document `proposed`, update the canonical method page, validate, and submit a pull request.

## 6. Improve a skill

Open a `type: skill` issue with a reproducible example and evaluation plan. Read the skill, `templates/learning/skill-evaluation.md`, and `docs/ai-integration.md`. Keep the skill `experimental`, update its evaluation record, run the validator and unit tests, and ask a human to review the observed behaviour and risks in a pull request.

## 7. Record an experiment outcome

Open a `type: experiment` issue before running the test. Read `experiments/README.md` and `templates/learning/experiment.md`. Record the question, hypothesis, method, measure, observations, and limits. Use `status: hypothesis` for an untested claim and a proposed or experimental status for the record according to its state. Do not invent or overstate results. Work in an `experiment/short-desc` branch and submit the outcome and next learning as a pull request.

## 8. Review a design decision

Open a `type: docs` issue or a `type: decision` issue for the item under review. Read `skills/identity-system-critic/SKILL.md` and `methods/quality/critique-protocol.md`. In a `review/short-desc` branch, use the design-critique template to separate documented brief requirements, observable details, interpretation, and hypotheses. Link the decision or identity-system spec under review, state what remains unknown, and submit the critique as a pull request without changing the decision's status.

## 9. Capture post-project lessons

Before writing, remove names, assets, quotations, and identifying details unless written permission covers this publication. Read `methods/learning-loop.md`, `templates/learning/retrospective.md`, and `docs/public-private-boundary.md`. Open a `type: project` issue with `privacy-review`, use a `project/short-desc` branch, record only the generalised learning and its limits, then submit a pull request for human privacy review.

## 10. Retrieve context from Claude Code

At the repository root, run `claude`. Prompt: “Read `INDEX.md` first, then the route for the task I describe in `AGENTS.md`, and only those files. Summarise the current status and evidence before drafting anything.” Provide the specific source or task input, ask for links and evidence labels, and review its proposed changes. Use an `ai/context-retrieval` branch, run `uv run python scripts/validate.py`, and submit a pull request.

## 11. Capture a quick note and weekly triage

For a public-safe observation or link, add `inbox/YYYY-MM-DD-short-title.md` in the GitHub web editor or a short-lived branch. Read [`inbox/README.md`](../inbox/README.md) and [`docs/public-private-boundary.md`](public-private-boundary.md). Add only `title`, ISO `captured`, `type: inbox`, and `status: proposed` frontmatter; keep personal, client, confidential, and commercial material in the private system. During weekly triage, turn each useful note into a study, principle, experiment, decision, or method change and remove the inbox copy, or delete it if it has no lasting value. Use a pull request for substantive changes and run the validator after regenerating `INDEX.md`.

## No-code path

For a small correction or sourced note, use GitHub's web editor, select **Propose changes**, and create a pull request. Issues can frame research, experiments, methods, and lessons without local tooling. Code, validator changes, skill symlinks, and workflow edits need a local checkout so the required checks can run.
