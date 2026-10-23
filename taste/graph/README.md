# Taste Graph

The swipe file as a local PostgreSQL knowledge graph. Every reference you save is linked to the patterns and principles it shows (or breaks), and every creative task an agent runs starts from a short **reference pack**: what to do, what not to do, with exemplars. Governed by [D-0020](../../studio/decisions/0020-taste-graph.md); agents use the [`3w-taste-graph`](../../skills/3w-taste-graph/SKILL.md) skill.

**Private by design.** Screenshots, thumbnails and captured third-party text stay on your Mac in `~/.3rdwrong/taste` and the local database. They never enter this repository: the CLI refuses a data folder inside any git work tree. This folder holds only the schema ([`migrations/`](migrations/0001_init.sql)), the seed of public URLs and studio notes ([`seed.yaml`](seed.yaml)) and this guide.

## For the founder

### Setup (5 minutes, once)

```bash
brew install postgresql@17
brew services start postgresql@17
cd ~/3rdwrong
uv run scripts/taste_graph.py init --seed
```

`init` creates the `taste_graph` database, applies the schema, loads the seed (the existing 37 swipe-file entries plus 16 research additions, studio benchmarks, discovery sources, 9 principles and 13 anti-patterns) and reports what it found. Running it again is safe: it only adds what is missing. Web screenshots use `playwright-cli`, which is already installed.

Optional settings (set them in your shell only if you want to change the defaults):

| Variable | Default | Purpose |
| --- | --- | --- |
| `TASTE_GRAPH_DSN` | `postgresql:///taste_graph` | Database connection |
| `TASTE_GRAPH_HOME` | `~/.3rdwrong/taste` | Media, backups and the default inbox |
| `TASTE_GRAPH_INBOX` | `$TASTE_GRAPH_HOME/inbox.md` | Inbox file read by `ingest` |

### The 2-minute daily habit

**On the desktop**, when something is excellent (or instructively bad):

```bash
uv run scripts/taste_graph.py add https://example.com/ --kind landing_page --verdict exemplar \
  --why "One plain sentence carries the hero; the type does the work." \
  --pattern "Plain-sentence hero" --pattern "principle:Type-led design" --tone plainspoken \
  --by founder --status curated
```

Web pages get desktop (1440×900) and mobile (390×844) screenshots plus title, description and headline. YouTube links get the public thumbnail; X and TikTok links get the post text through public oEmbed. Instagram, LinkedIn and anything behind a login only get a best-effort public screenshot, so save your own screenshot and pass it with `--file shot.png --text "the copy"`. Saving the same link again updates the entry instead of duplicating it and never overwrites your earlier analysis.

**On the phone**, append links to an inbox file in iCloud Drive with a Shortcut, then ingest them at the desk.

1. On the Mac, create the file once: `mkdir -p ~/Library/Mobile\ Documents/com~apple~CloudDocs/3rdwrong && touch ~/Library/Mobile\ Documents/com~apple~CloudDocs/3rdwrong/taste-inbox.md`.
2. On the iPhone, open **Shortcuts** › **+** and name the shortcut **Save to Taste**.
3. Tap the **ⓘ** (details) button, turn on **Show in Share Sheet**, and limit input types to **URLs**, **Safari web pages** and **Text**.
4. The first action reads **Receive URLs and Text from Share Sheet**; set **If there's no input** to **Get Clipboard**.
5. Add **Ask for Input**: type **Text**, prompt `Why is it good? (optional)`.
6. Add **Text** and enter: the **Shortcut Input** variable, a space, `|`, a space, then the **Provided Input** variable.
7. Add **Append to Text File**: choose the file **iCloud Drive › 3rdwrong › taste-inbox.md** and turn on **Make New Line**.
8. Share any link to **Save to Taste**. Each line looks like `URL | note`; you can add a third field for the kind, for example `URL | note | thumbnail`.

At the desk, point the CLI at that file once per session and ingest it:

```bash
export TASTE_GRAPH_INBOX=~/Library/Mobile\ Documents/com~apple~CloudDocs/3rdwrong/taste-inbox.md
uv run scripts/taste_graph.py ingest
```

Each captured line moves into a dated `## Processed YYYY-MM-DD` section with its node number, so nothing is lost. A line that fails stays where it was with `# error <date>: <reason>` appended; fix it or replace it with screenshots via `add --file`, and the next `ingest` retries it. Ingested items enter as `inbox`.

### Weekly curation (10 minutes)

```bash
uv run scripts/taste_graph.py list --status inbox
uv run scripts/taste_graph.py show 123
uv run scripts/taste_graph.py update 123 --verdict exemplar --score 5 --status curated --why "…"
uv run scripts/taste_graph.py link 123 exemplifies "pattern:Oversized serif hero"
uv run scripts/taste_graph.py update 124 --status archived
```

Only curated references reach a pack (agents can include the inbox explicitly). Agent captures always enter as `inbox`; promoting them is your call. If a capture warns that the screenshot looks blank, the site showed an intro or loader: take your own screenshot and add it with `--file`.

### Backup and restore

```bash
uv run scripts/taste_graph.py backup --keep 14
```

This writes `~/.3rdwrong/taste/backups/taste_graph-<timestamp>.dump` and keeps the newest 14. The dump covers the database only; include `~/.3rdwrong/taste` (media and backups) in Time Machine. To restore into a fresh database and check it:

```bash
PG=/opt/homebrew/opt/postgresql@17/bin
$PG/createdb taste_graph_restored
$PG/pg_restore --no-owner -d taste_graph_restored ~/.3rdwrong/taste/backups/taste_graph-<timestamp>.dump
TASTE_GRAPH_DSN=postgresql:///taste_graph_restored uv run scripts/taste_graph.py stats
```

To replace the live database, stop anything using it, then `$PG/dropdb taste_graph && $PG/createdb taste_graph` and run the same `pg_restore` against `taste_graph`.

## For agents

Follow the [`3w-taste-graph`](../../skills/3w-taste-graph/SKILL.md) skill. All commands run as `uv run scripts/taste_graph.py <command>`.

| Command | Use |
| --- | --- |
| `init [--seed]` | Create the database if missing, apply migrations, load the seed, report the environment |
| `add <url> \| --file <path>…` | Capture with `--kind --verdict --why --title --tags --brand --creator --platform --pattern… --violates… --tone --score --text --status --by --full-page` |
| `ingest [--inbox PATH]` | Capture every `URL \| note \| kind` line as `inbox` |
| `list [--type] [--status] [--kind] [--since]` | Recent nodes |
| `show <id\|type:slug\|slug\|url>` | One node, its media and neighbours |
| `search "<query>"` | Full-text and fuzzy search over all nodes |
| `update <id> …` | Verdict, analysis, score, status, tags, kind or title |
| `link <src> <rel> <dst>` | Add an edge; `dst` such as `pattern:Title` is created if missing |
| `pack "<brief>" [--kind …] [--limit N] [--project slug] [--include-inbox] [--format md\|json]` | The reference pack |
| `stats` / `backup [--keep N]` | Counts and rotated `pg_dump` backups |

**Pack.** Ranks curated assets against the brief by full text, title/tag similarity, kind and score, then follows the graph to the patterns and principles they exemplify and the principles that anti-pattern assets violate. Studio principles and anti-patterns fill the rest. The markdown (about 900 words at most) has Do, Don't, Study, Signals (tone, audience, industry) and up to three local images, and always ends with the originality guard. `--project` records `used_in` edges so you can later see which references informed which deliverable. Output is deterministic for the same data.

**Graph model.** Node types: asset, brand, creator, platform, pattern, principle, technique, tone, audience, industry, project. Asset kinds: landing_page, website, ui_component, thumbnail, brand_asset, copy, tweet, linkedin_post, tiktok, reel, short_video, ad, email, other. Edges: `exemplifies` (asset → pattern, principle or technique), `violates` (asset → principle), `by` (→ brand or creator), `on` (→ platform), `for` (→ audience or industry), `has_tone`, `related`, `contrasts` (pattern ↔ pattern or principle), `used_in` (→ project). Change the schema only by adding a numbered migration.

**Rules.** Public pages only: no login, cookies, stored credentials, paywall or anti-bot circumvention. Downloads are capped at 25 MB, media filenames are random UUIDs, and only `http(s)` URLs are accepted. Never copy captured media or text into the repository or a deliverable.

## Next steps (not built)

- **Local embeddings:** add `pgvector` and a local embedding model (no paid API) to rank by visual and semantic similarity as well as words.
- **Phone capture without the desk step:** a small local service or scheduled `ingest` so phone shares arrive in the graph automatically.
