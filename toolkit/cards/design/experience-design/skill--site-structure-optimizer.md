---
title: Site Structure Optimizer
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:site-structure-optimizer
department: design
sub_department: experience-design
job: interaction-architecture
role: specialist
trigger: "Use only when the named content, channel, lifecycle, or campaign task is explicitly in the approved marketing scope."
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-aaron-he-zhu-aaron-marketing-skills-apache-2.0/skills/site-structure-optimizer
invoke: "site-structure-optimizer skill"
pairs_with: [skill:designing-user-experience, skill:ceos-interaction-architecture]
---
# Site Structure Optimizer

The experience-design specialist for `interaction-architecture` is Site Structure Optimizer (trigger: “Use only when the named content, channel, lifecycle, or campaign task is explicitly in the approved marketing scope”), which plans website information architecture or improves internal links within an existing site.

## What it does

- Supports architecture and linking modes.
- designs hierarchy, navigation, URL patterns and topic clusters.
- analyses link graphs and orphan pages.

## When to use

- Use only for a specifically approved site hierarchy, navigation, URL taxonomy or internal-link task. Use Phase 04 Information Architecture before route build.
- Use only when the named content, channel, lifecycle, or campaign task is explicitly in the approved marketing scope.

## When not to use

- Use `skill:designing-user-experience` for user journeys or `skill:ceos-interaction-architecture` for interaction behaviour.
- Do not use it to approve its own work; have an independent reviewer check the artefact.

## Inputs it needs

- Approved site goals, page inventory, content relationships and existing URL/link data.
- Versioned approved brief/strategy and source links; mark draft material as formative.

## How to run it

1. Confirm the trigger, stage and source material; keep client data in the approved private store.
2. Run it using the invocation above and provide the required inputs.
3. Check the output against the quality checks; hand unresolved decisions to the named human owner.

```text
Use site-structure-optimizer skill. Studio phase: {phase}. Project: {project}. Approved goal/strategy: {goal and source}. Scope: {screen, flow or interaction}. Inputs/evidence: {links and versions}. Constraints: {platform, accessibility, motion, privacy}. Produce hierarchy is understandable, orphan handling is stated and link recommendations map to real pages. Keep documented facts separate from interpretation and hypothesis; list unknowns and the next human decision.
```

## What good output looks like

- A sitemap or prioritised internal-link plan with structure score and handoff summary.
- Evidence claims are labelled Documented, Interpretation, Hypothesis or Unknown as applicable.
- The output names open questions, owner and next action.

## Quality checks

- [ ] An independent checker verifies the output against the approved scope and artefact version.
- [ ] No unsupported user, audience, accessibility, performance or business outcome is presented as fact.
- [ ] Responsive, keyboard/focus and reduced-motion needs are included where relevant.

## Pairs with

- Related tools: `skill:designing-user-experience`, `skill:ceos-interaction-architecture`. Use the relevant method or specialist to complete the handoff.
- Engineering owns implementation, general testing, performance and security; Design owns experience intent and craft.

## Limits and cautions

- Registry trigger mentions marketing scope despite design placement; source is an SEO/marketing skill. Do not use for external backlinks, XML sitemap or indexation issues.
- Respect the tool distribution: vendor copies are repo snapshots; fetch/manual sources need their stated install or sign-in.
- Client data, personal data and credentials stay out of the public repository.
- Motion is purposeful and honours reduced motion; avoid the rejected own-identity vocabulary in D-0006.
