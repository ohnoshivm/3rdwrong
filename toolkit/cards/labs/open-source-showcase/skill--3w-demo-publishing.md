---
title: Demo publishing
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:3w-demo-publishing
department: labs
sub_department: open-source-showcase
job: demo-publishing
role: lead
trigger: ""
kind: repo-skill
availability: repo
distribution: repo
source: skills/3w-demo-publishing/SKILL.md
invoke: "3w-demo-publishing skill"
pairs_with: [skill:publish-project-to-github, agency:specialized-developer-advocate, skill:3w-engine-validation]
---
# Demo publishing

The studio's lead tool for demo publishing: the pre-release gate for Labs demos and public repositories. Proposed lead; the registry change is pending.

## What it does

- Searches code, history, assets and captures for client material or personal data.
- Checks the outbound licence under D-0009 and every dependency and asset licence.
- Records AI use and checks the D-0023 budget, reduced motion and accessibility basics.
- Produces a publication record for a non-maker reviewer and founder approval.

## When to use

- An effect study, benchmark or validated kit is proposed for a public demo page or repository.
- Before `skill:publish-project-to-github` packages anything.

## When not to use

- Client launches or case studies.
- Deciding whether the work is good enough — a founder decision.

## Inputs it needs

- Demo or repository, version and intended public location.
- Source study, benchmark or validation record.
- List of third-party libraries, fonts, images, models and datasets.
- AI tools used.

## How to run it

1. Collect the inputs; keep client and prospect details in the vault.
2. Run the skill and return its exact output structure.
3. Have someone other than the maker review the result.
4. File the output where the skill says; act on blockers first.

```text
Use the 3w-demo-publishing skill for {{demo}} going to {{public location}}. Inputs: {{repo path}}, {{source record}}, third-party list {{…}}, AI use {{…}}. Return the demo publication record; do not publish.
```

## What good output looks like

- Every check row has evidence; unknown provenance or licence blocks.
- A README stating question, technique, measured cost, limits, licence and credits.

## Quality checks

- [ ] No client identifier anywhere, including history.
- [ ] Third-party items allow public redistribution.
- [ ] AI use disclosed.
- [ ] Founder approval recorded before release.

## Pairs with

- Upstream: `skill:3w-effect-study`, `skill:3w-labs-benchmark`, `skill:3w-engine-validation`.
- Downstream: `skill:publish-project-to-github` (packaging), `agency:specialized-developer-advocate` (community).

## Limits and cautions

- Not legal advice; licence compatibility questions go to an adviser.
- D-0009 licensing remains pending founder confirmation where stated.
- Publishing cannot be undone reliably.
