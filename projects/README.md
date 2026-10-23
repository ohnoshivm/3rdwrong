# Projects

Project records are grouped by their relationship to real work:

- `<codename>/` holds a **cleared** client project: one whose contract permits
  anonymised publication. Records use the codename only; client names, people,
  contacts, domains, money and client files live in the private vault
  ([D-0021](../studio/decisions/0021-client-work-public-anonymised.md)).
  Projects that are not cleared live entirely in the vault and never appear
  here.
- `internal/` holds the studio's own work. It is never represented as client
  work.
- `speculative/` is for self-initiated studies of a real brief or category.
  Label the work speculative; do not imply client participation or validation.
  Create this directory only when a project exists.
- `examples/` contains explicitly fictional material used to exercise methods
  and skills. Every file in a fictional project carries the same fiction
  banner. [Stillsoil Atelier](examples/README.md) is the worked example.

## Starting a client project

Projects run on the [client lifecycle](../methods/lifecycle.md). At L4
Contract & deposit, once the contract is signed:

1. Create the vault once per machine: `bin/3w vault init`.
2. Create the workspace with the offer's bundle:
   `bin/3w new project-identity --cleared` or
   `bin/3w new project-digital --cleared` when the contract permits anonymised
   publication; otherwise use `--private`, which renders the whole workspace
   into the vault. Pass `--codename two-words` or let the CLI generate one.
3. Record the real client under the codename in the vault's `clients.yaml`.
4. Install the local pre-commit guard once per clone: `bin/3w hooks install`.
5. Regenerate `INDEX.md` (`uv run python scripts/build_index.py`) and run
   `bin/3w check` before every commit.

## Workspace layout

| Path | Contents |
| --- | --- |
| `README.md` | Offer, current stage, clearance and the gate log |
| `brief.md` | Anonymised brief and success criteria |
| `decisions.md` | Decisions and approvals log |
| `risks.md` | Risk and issue log |
| `status/` | Weekly status reports, one file per week |
| `feedback.md` | Consolidated feedback rounds |
| `qa/` | QA and acceptance evidence as text; screenshots stay in the vault |
| `handover.md` | Handover record, warranty and care |
| `retro.md` | Retrospective, lessons and publication clearance |

Only `.md`, `.yaml`, `.yml` and `.json` files are allowed under `projects/`;
the validator's anonymity check rejects anything else, along with emails,
phone numbers, currency amounts and Indian identifiers. Day-to-day rules are in
[project operations](../business/engagement-operations.md); publication rules
are in the [publication rules](../docs/public-private-boundary.md).
