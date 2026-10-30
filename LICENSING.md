# Licensing

This repository has separate licences because executable tooling, original creative knowledge, third-party sources, brand rights, and client work have different owners and permissions.

## Code

The validator, tests, schemas, and GitHub configuration are licensed under the [MIT License](LICENSE). The MIT licence applies to code and repository tooling in `scripts/`, `tests/`, `schemas/`, and `.github/`, plus `motion-teardown/agent-system/scripts/`, `motion-teardown/agent-system/schemas/`, `motion-teardown/tracks/dev/tests/`, the scripts under `motion-teardown/media/`, and `motion-teardown/export/build_exports.py`.

## Original documentation and creative material

Original documentation, methods, templates, skills, and other original written material are licensed under [Creative Commons Attribution 4.0 International](LICENSE-DOCS) (CC BY 4.0). Give attribution to 3RDWRONG, name the work, link to the source where practical, link to the licence, and describe material changes. An attribution can follow this form:

```text
3RDWRONG, “{{work title}}”, {{source link}}, licensed under CC BY 4.0. Changes: {{brief description}}.
```

The [licensing-model decision](studio/decisions/0009-licensing-model.md) records this founder-approved choice.

## Upstream Agency Agents

The files in `.claude/agents/` are upstream Agency Agents material licensed under MIT, not CC BY 4.0. Their original copyright and complete MIT licence are reproduced in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md); [the agent lock](agents/agency-agents.lock.json) records provenance and file hashes. Preserve the upstream notice when reusing these files.

## Third-party toolkit

`toolkit/vendor/` holds third-party skills, agents and plugin material copied unmodified from their published sources. Each vendored package keeps its own licence: its original `LICENSE`, `NOTICE` or `COPYRIGHT` files stay in place, its `PROVENANCE.yaml` records the upstream source, pinned reference, SPDX identifier and a SHA-256 for every file, and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md#third-party-toolkit) lists every package with links to those exact notice files. The copies in `toolkit/plugins/` carry the same licences, with the notices copied into each plugin.

The repository's MIT licence (code) and CC BY 4.0 licence (documentation) do not apply to `toolkit/vendor/**` or to the third-party copies in `toolkit/plugins/**`. They do apply to the toolkit scripts in `scripts/`, the generated plans and metadata in `toolkit/`, and the studio's own `3w-*` skills. Packages that `scripts/install.sh` clones at install time are not redistributed here; their own licences govern those checkouts.

## Third-party and excluded material

Third-party material linked to or quoted for commentary remains under its owners' rights and terms. A citation does not relicense it. No third-party images are committed as repository assets.

The name **3RDWRONG**, and any future logos or brand assets, are not licensed by MIT or CC BY 4.0. Trademark and brand rights are reserved.

Everything committed to this knowledge base is public and open source under its applicable licence. The founding blueprint and studio pricing hypotheses are included by explicit founder approval ([D-0017](studio/decisions/0017-fully-open-repository.md)); third-party quotations and cited sources retain their original rights.

Client personal data, third-party contracts, credentials and NDA-bound assets must never be committed or licensed through this repository. Choose a non-public store before the first client or interview data exists, and follow the [publication rules](docs/public-private-boundary.md). Client work and other third-party assets require specific rights clearance; the founder's approval does not relicense someone else's work.
