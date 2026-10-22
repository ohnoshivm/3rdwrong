# Templates

Templates are proposed starting points. Copy only the sections that fit the
work, replace every `{{placeholder}}`, and keep evidence labels and approvals
honest. Do not invent source material to complete a field.

## Studio and project

- [Client brief](briefs/client-brief.md)
- [Strategy on a page](strategies/strategy-on-a-page.md)
- [Project README](projects/project-readme.md)
- [Case study](case-studies/case-study.md)

## Identity and critique

- [Concept route](identity-systems/concept-route.md)
- [Identity system specification](identity-systems/identity-system-spec.md)
- [Design critique](critique/design-critique.md)

## Learning and evaluation

- [Research intake](learning/research-intake.md)
- [Creative experiment](learning/experiment.md)
- [Retrospective](learning/retrospective.md)
- [Method improvement proposal](learning/method-improvement.md)
- [Skill evaluation](learning/skill-evaluation.md)

## Research library templates

- [Agency study](research/agency-study.md)
- [Project study](research/project-study.md)
- [Psychology research](research/psychology-research.md)
- [Visual system analysis](research/visual-system-analysis.md)
- [Typography analysis](research/typography-analysis.md)
- [Motion system analysis](research/motion-system-analysis.md)
- [Design principle](research/design-principle.md)

## Create a document

If the repository helper is available, run:

```bash
uv run python scripts/new_doc.py <template> <dest>
```

Use the template path relative to the repository as `<template>` and the
intended output path as `<dest>`. The helper copies the file and may prefill
metadata; review the result and replace placeholders before committing.

Without code, open the template, copy its contents into a new file in the
correct project folder, update the frontmatter and title, replace every
placeholder, remove unused guidance comments and check all relative links.
