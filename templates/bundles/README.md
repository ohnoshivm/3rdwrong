---
title: Template bundles
type: guide
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 180
---

# Template bundles

A bundle is a folder of templates that `bin/3w new` renders together into a
working folder, such as a client project workspace. Bundles implement the
workspace model in [D-0021](../../studio/decisions/0021-client-work-public-anonymised.md)
and the [publication rules](../../docs/public-private-boundary.md).

## Available bundles

| Bundle | Renders | Use |
| --- | --- | --- |
| `project-identity` | `projects/{codename}/` | Identity System engagement, [identity engagement method](../../methods/identity-engagement/README.md) |
| `project-digital` | `projects/{codename}/` | Digital Experience engagement, [digital experience method](../../methods/digital-experience/README.md) |
| `proposal` | `projects/{codename}/proposal.md` | Public anonymised proposal; investment stays in vault |
| `sow` | `projects/{codename}/sow.md` | Public anonymised scope; signed contract stays in vault |
| `change-order` | `projects/{codename}/change-orders/{change_id}.md` | Public anonymised change record |
| `invoice` | `{vault}/{codename}/finance/invoices/` | Private invoice record |
| `finance-review` | `{vault}/finance/reviews/` | Private monthly review |
| `weekly-review` | `{vault}/reviews/weekly/` | Private weekly operating review |
| `rates` | `{vault}/rates.yaml` | Private pricing inputs |
| `estimate` | `{vault}/{codename}/finance/estimate.yaml` | Private opportunity estimate |
| `case-study` | `projects/{codename}/case-study.md` | Contract-cleared anonymised case study |
| `content-brief` | `growth/content/briefs/{date}-{slug}.md` | Public studio content brief |
| `discovery-notes` | `{vault}/{codename}/private-notes/discovery-{date}.md` | Private opportunity discovery |
| `outreach-sequence` | `{vault}/growth/outreach/{codename}.md` | Private personalised outreach |
| `win-loss` | `{vault}/growth/win-loss/{codename}-{date}.md` | Private opportunity review |

All client repository targets also support `--private`.

## Format

```text
templates/bundles/<bundle>/
  bundle.yaml              metadata and variables
  <name>.md.tmpl           a single-file template, or
  workspace/               a folder of *.tmpl files rendered together
    README.md.tmpl
    status/README.md.tmpl
```

`bundle.yaml` is ordinary YAML, read with PyYAML (the repository's declared
dependency):

```yaml
kind: project
description: Anonymised workspace for a Digital Experience engagement.
template: workspace/
target: projects/{codename}/
variables:
  - name: codename
    description: Two lowercase words joined by a hyphen.
    example: quiet-harbour
```

| Key | Required | Meaning |
| --- | --- | --- |
| `kind` | yes | What the bundle creates, e.g. `project`, `proposal`, `invoice`. `project` bundles create a client workspace |
| `description` | yes | One sentence shown to people choosing a bundle |
| `template` | yes | The single `.tmpl` file name, or a folder of `*.tmpl` files (searched recursively), relative to the bundle |
| `target` | yes | Output path pattern with `{variable}` placeholders. A target starting with `{vault}/` renders into the vault; anything else renders into the repository. A folder template, or a target ending in `/`, is a folder |
| `variables` | no | A list of `{name, description?, example}` that `--set` may fill; `example` is shown when a required value is missing |

Every template file carries a `.tmpl` suffix so repository checks and
markdownlint skip the unrendered source; rendering removes the suffix.
Rendered repository files must pass the validator, markdownlint and the
anonymity guard.

### Placeholders

Inside `.tmpl` files placeholders are `{{variable}}`; in `target` they are
`{variable}`. The CLI fills `{{codename}}` and `{{title}}` (codename in title
case) when a codename applies, `{{date}}` (today, ISO), `{{bundle}}`, and
`{{clearance}}` when `--cleared` or `--private` is given. `--set name=value`
fills any declared variable and overrides an automatic one. Any other
`{{placeholder}}` is left for a person to replace, as in the
[single-file templates](../README.md). Every `{variable}` in `target` must be
filled, and target values may not contain `/`, `\` or `..`.

## Command line

Run from the repository root. `bin/3w` uses the repository's `uv` environment
when available, otherwise `python3`.

| Command | Effect |
| --- | --- |
| `bin/3w new <bundle> --cleared [--codename quiet-harbour] [--set name=value]` | Renders a client record into the repository. Only for projects whose contract permits anonymised publication. A `project` bundle also creates the vault's private folders for the codename when the vault exists |
| `bin/3w new <bundle> --private [--codename quiet-harbour]` | Renders a repository-target client bundle into the vault instead: `projects/` is replaced by `<vault>/`, so a workspace lands in `<vault>/<codename>/` with `contracts/`, `finance/`, `files/` and `private-notes/` |
| `bin/3w new <vault-bundle> --codename quiet-harbour --set name=value` | Renders a `{vault}/` target, such as an invoice, into the vault; no clearance flag is needed |
| `bin/3w vault init` | Creates the vault (mode 700) with an empty `clients.yaml` that documents its structure; never overwrites an existing file |
| `bin/3w check` | Runs `scripts/validate.py`, then the anonymity guard with the vault deny-list when `clients.yaml` exists |
| `bin/3w check --staged` | Guards staged files only; used by the pre-commit hook |
| `bin/3w hooks install` | Installs a local pre-commit hook that runs `bin/3w check --staged`; refuses to replace a hook it did not write. Hooks are never committed |

Rules the CLI enforces:

- A repository target that contains `{codename}`, and every `project` bundle,
  needs `--cleared` or `--private`; there is no default. Vault targets reject
  `--cleared`; other repository targets reject both flags.
- Codenames are two lowercase words joined by a hyphen, supplied by `--codename` or `--set codename=two-words`. A `project` bundle
  generates one from a neutral built-in word list when it is omitted, checked
  against existing public and vault workspaces; other bundles require the
  client's existing codename.
- It refuses to overwrite: a `project` workspace that already exists on either
  side, or any output file that exists. Files are written with exclusive
  creation.
- The vault is `THREEW_VAULT` or `~/3rdwrong-vault`, must exist
  (`bin/3w vault init`) before anything renders into it, and must not be inside
  any git work tree.

After `new --cleared`, record the real client under the codename in the vault's
`clients.yaml`, regenerate `INDEX.md` with `uv run python scripts/build_index.py`
and run `bin/3w check` before committing.

## Adding a bundle

1. Create `templates/bundles/<bundle>/bundle.yaml` with the keys above.
2. Add the `.tmpl` file or folder. Repository outputs need valid frontmatter
   after rendering; write links relative to the rendered location.
3. Render it into a temporary root and vault in a test (see
   `tests/test_threew.py`) and check repository output with the validator's
   frontmatter check and the anonymity guard.
