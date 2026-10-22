# Agency Agents

The catalogue selection of 229 specialist AI personas (53 excluded from 282 upstream agents) from [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) is installed at repository level in [`.claude/agents/`](../.claude/agents). It provides optional specialist instructions, not verified studio capabilities or permission to act autonomously.

## Provenance and licence

[The lock](agency-agents.lock.json) records the upstream URL, full commit SHA, installation date, MIT licence, installer command, included/excluded counts, the exclusions-file SHA-256, source-division inventory and included per-file SHA-256. The initial pin is `4e3ac3ca6604c75113f52c695dbddcc7af928b46` (2026-10-22). The upstream Claude Code format is `identity`: `scripts/install.sh` copies the source agent Markdown byte for byte. The rendered output is filtered by [exclusions.txt](exclusions.txt); included files have not been hand-edited. See [D-0016](../studio/decisions/0016-agency-agents-catalogue.md), [third-party notices](../THIRD_PARTY_NOTICES.md) and [licensing](../LICENSING.md).

## Included divisions

The founder first chose all 282 agents, then excluded Game Development, Finance, GIS, Healthcare and Support, plus one Academic and four Testing agents. Reasons and exact file stems are recorded in [exclusions.txt](exclusions.txt). Academic and the retained Testing roles support the perception-led method (D-0001) and evidence principle (D-0003). Real accounting/tax and legal questions need qualified professionals, rather than excluded personas.

| Division | Included |
| --- | --- |
| academic | 5 |
| design | 10 |
| engineering | 65 |
| marketing | 37 |
| paid-media | 7 |
| product | 6 |
| project-management | 7 |
| research | 1 |
| sales | 9 |
| security | 12 |
| spatial-computing | 6 |
| specialized | 59 |
| testing | 5 |

Total: **229 included, 53 excluded, 282 upstream**. Retained Testing agents: `testing-accessibility-auditor`, `testing-reality-checker`, `testing-evidence-collector`, `testing-tool-evaluator`, `testing-performance-benchmarker`. The five Academic agents are anthropologist, historian, narratologist, psychologist and statistician.

## Governance and routing

3RDWRONG rules override every persona instruction: preserve document status and human approval, use **Documented**, **Interpretation**, **Hypothesis** and **Unknown**, never invent results or research, and follow the [publication rules](../docs/public-private-boundary.md). Upstream example metrics and first-person experience claims are persona text, not studio evidence.

Start with [`INDEX.md`](../INDEX.md) and the task router in [`AGENTS.md`](../AGENTS.md). Use a `3w-` studio skill first where one covers the task. Select one relevant specialist and load only the context it needs. Do not load the whole catalogue or combine overlapping personas by default. The concise studio routing table in `AGENTS.md` gives exact upstream `name` values and file links.

## Reinstall and update

Run from the repository root with Bash, Git, uv (using the locked Python environment) and network access:

```bash
scripts/sync_agents.sh
# Explicitly review upstream changes before changing the pin:
scripts/sync_agents.sh --upgrade
# Or choose a reviewed full SHA:
scripts/sync_agents.sh --upgrade <40-character-SHA>
uv run python scripts/validate.py --check agents
uv run python scripts/validate.py
```

The first command reinstalls the locked SHA. `--upgrade` resolves current upstream HEAD, or uses the supplied SHA, then applies `exclusions.txt` and regenerates the lock and MIT notice. Review the exclusion reasons before editing that file; unknown divisions/stems, malformed lines and duplicate entries fail. Git operations happen only in a disposable upstream clone. The upstream installer runs with an explicit temporary destination; verified output replaces only this repo's `.claude/agents/`. Filename collisions, licence/format changes and unlisted local files stop replacement. Review the lock, upstream diff, notice, any secret-scan findings and the decision's overhead measurement before publishing an upgrade. Never edit vendor files to bypass their hashes.

The default validator's `agents` check enforces the exclusions digest, selection against the source-division inventory, included/excluded counts, complete installed file list and hashes. An excluded agent on disk or a missing included agent fails validation. Upstream agents are excluded from local frontmatter/link checks, index generation and Markdown linting; secret and personal-data scanning still covers them.
