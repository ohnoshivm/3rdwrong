# /// script
# requires-python = ">=3.12"
# dependencies = ["psycopg[binary]>=3"]
# ///
"""3RDWRONG Taste Graph: a local PostgreSQL knowledge graph of references.

Run with `uv run scripts/taste_graph.py <command>`. See taste/graph/README.md.

Captured media and third-party text are private reference material. They live in
TASTE_GRAPH_HOME (default ~/.3rdwrong/taste) and the database, never in a git work tree.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import html
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
import uuid
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
GRAPH_DIR = ROOT / "taste" / "graph"
DEFAULT_DSN = "postgresql:///taste_graph"
PG_PREFIXES = ("/opt/homebrew/opt/postgresql@17/bin", "/usr/local/opt/postgresql@17/bin")
PLAYWRIGHT_CLI = "/opt/homebrew/bin/playwright-cli"
USER_AGENT = "3rdwrong-taste-graph/1 (local reference capture)"
MAX_DOWNLOAD = 25 * 1024 * 1024
BLANK_PNG_BYTES = 20_000  # a 1440x900 PNG this small is almost always a flat loader screen
TIMEOUT = 20
PAGE_SETTLE_SECONDS = (8.0, 3.0)  # first viewport waits out loaders; resize only re-lays out
GUARD = "Use these as principles. Never copy layouts, assets, copy or brand identity."

NODE_TYPES = ("asset", "brand", "creator", "platform", "pattern", "principle",
              "technique", "tone", "audience", "industry", "project")
KINDS = ("landing_page", "website", "ui_component", "thumbnail", "brand_asset", "copy", "tweet",
         "linkedin_post", "tiktok", "reel", "short_video", "ad", "email", "other")
VERDICTS = ("exemplar", "anti_pattern", "mixed")
STATUSES = ("inbox", "curated", "archived")
RELS = ("exemplifies", "violates", "by", "on", "for", "has_tone", "related", "contrasts", "used_in")
NODE_COLUMNS = ("type", "slug", "title", "body", "url", "kind", "verdict", "score", "tags")

TRACKING_PARAMS = {"fbclid", "gclid", "dclid", "msclkid", "igshid", "igsh", "mc_cid", "mc_eid",
                   "ref_src", "ref_url", "_hsenc", "_hsmi", "yclid"}
SOCIAL_HOSTS = ("youtube.com", "youtu.be", "x.com", "twitter.com", "instagram.com", "tiktok.com", "linkedin.com")
SOCIAL_TRACKING = {"si", "s", "t", "feature", "is_from_webapp", "sender_device", "rcm"}
IMAGE_TYPES = {"image/png": ".png", "image/jpeg": ".jpg", "image/webp": ".webp",
               "image/gif": ".gif", "image/avif": ".avif"}
FILE_EXTS = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".avif", ".heic", ".mp4", ".mov", ".webm", ".pdf"}
WALLED_HOSTS = ("instagram.com", "linkedin.com", "facebook.com", "threads.net", "threads.com")
PLATFORM_NAMES = {"youtube": "YouTube", "twitter": "X", "tiktok": "TikTok",
                  "instagram.com": "Instagram", "linkedin.com": "LinkedIn",
                  "facebook.com": "Facebook", "threads.net": "Threads", "threads.com": "Threads"}
KIND_HINTS = (
    (("landing", "hero", "homepage", "home page"), ("landing_page", "website")),
    (("website", "site", "web", "portfolio"), ("website", "landing_page")),
    (("ui", "ux", "component", "button", "nav", "navigation", "form", "dashboard", "interface"), ("ui_component",)),
    (("thumbnail", "youtube"), ("thumbnail",)),
    (("brand", "branding", "logo", "identity", "wordmark"), ("brand_asset",)),
    (("copy", "headline", "headlines", "tagline", "copywriting", "slogan"), ("copy",)),
    (("tweet", "twitter", "thread"), ("tweet",)),
    (("linkedin",), ("linkedin_post",)),
    (("tiktok",), ("tiktok",)),
    (("reel", "reels", "instagram"), ("reel",)),
    (("video", "short", "shorts"), ("short_video", "reel", "tiktok")),
    (("ad", "ads", "advert", "advertising", "campaign"), ("ad",)),
    (("email", "newsletter"), ("email",)),
)


class TasteError(Exception):
    """A user-facing failure: printed without a traceback."""


# ---------------------------------------------------------------- pure helpers


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:80].strip("-") or "untitled"


def check_url(url: str) -> str:
    url = url.strip()
    parts = urllib.parse.urlsplit(url)
    if parts.scheme not in ("http", "https") or not parts.hostname:
        raise TasteError(f"only http(s) URLs are accepted: {url!r}")
    return url


def youtube_id(url: str) -> str | None:
    parts = urllib.parse.urlsplit(url)
    host = (parts.hostname or "").removeprefix("www.").removeprefix("m.")
    if host == "youtu.be":
        return parts.path.strip("/").split("/")[0] or None
    if host in ("youtube.com", "music.youtube.com"):
        if parts.path == "/watch":
            return (urllib.parse.parse_qs(parts.query).get("v") or [None])[0]
        match = re.match(r"^/(?:shorts|embed|live)/([\w-]+)", parts.path)
        return match.group(1) if match else None
    return None


def _keep_param(host: str, key: str) -> bool:
    key = key.lower()
    if key.startswith("utm_") or key in TRACKING_PARAMS:
        return False
    return not (key in SOCIAL_TRACKING and any(host == h or host.endswith("." + h) for h in SOCIAL_HOSTS))


def normalize_url(url: str) -> str:
    """Canonical key for duplicate detection: same content, same key."""
    url = check_url(url)
    if vid := youtube_id(url):
        return f"https://youtube.com/watch?v={vid}"
    parts = urllib.parse.urlsplit(url)
    host = (parts.hostname or "").lower().removeprefix("www.").removeprefix("mobile.")
    path = re.sub(r"/{2,}", "/", parts.path or "/")
    if host in ("twitter.com", "x.com"):
        match = re.match(r"^/([^/]+)/status/(\d+)", path)
        return f"https://x.com/{match.group(1).lower()}/status/{match.group(2)}" if match else f"https://x.com{path.rstrip('/').lower()}"
    if len(path) > 1:
        path = path.rstrip("/")
    query = sorted(
        (key, value)
        for key, value in urllib.parse.parse_qsl(parts.query, keep_blank_values=True)
        if _keep_param(host, key)
    )
    port = f":{parts.port}" if parts.port and parts.port not in (80, 443) else ""
    return urllib.parse.urlunsplit(("https", host + port, path, urllib.parse.urlencode(query), ""))


def clean_url(url: str) -> str:
    """The URL as stored for humans: tracking parameters and fragments removed."""
    parts = urllib.parse.urlsplit(check_url(url))
    host = (parts.hostname or "").lower().removeprefix("www.")
    query = [(k, v) for k, v in urllib.parse.parse_qsl(parts.query, keep_blank_values=True) if _keep_param(host, k)]
    return urllib.parse.urlunsplit((parts.scheme, parts.netloc, parts.path or "/", urllib.parse.urlencode(query), ""))


def detect(url: str) -> tuple[str, str]:
    """Return (default kind, capture method) for a URL."""
    parts = urllib.parse.urlsplit(url)
    host = (parts.hostname or "").lower().removeprefix("www.")
    path = parts.path.lower()
    if youtube_id(url):
        return ("short_video" if "/shorts/" in path else "thumbnail"), "youtube"
    if host in ("x.com", "twitter.com", "mobile.twitter.com"):
        return "tweet", "twitter"
    if host.endswith("tiktok.com"):
        return "tiktok", "tiktok"
    if os.path.splitext(path)[1] in (".png", ".jpg", ".jpeg", ".webp", ".gif", ".avif"):
        return "other", "image"
    for walled in WALLED_HOSTS:
        if host == walled or host.endswith("." + walled):
            if walled == "instagram.com":
                return ("reel" if re.match(r"^/reels?/", path) else "other"), "walled"
            if walled == "linkedin.com":
                return "linkedin_post", "walled"
            return "other", "walled"
    return "landing_page", "web"


def kind_hints(brief: str) -> set[str]:
    lowered = brief.lower()
    words = set(re.findall(r"[a-z]+", lowered))
    hinted: set[str] = set()
    for keywords, kinds in KIND_HINTS:
        if any(k in lowered if " " in k else k in words for k in keywords):
            hinted.update(kinds)
    return hinted


def tsquery_text(brief: str) -> str:
    """OR the brief's words so websearch_to_tsquery ranks partial matches instead of requiring all."""
    words = re.findall(r"[\w][\w-]*", brief.lower())
    return " or ".join(dict.fromkeys(words))


def parse_inbox_line(line: str) -> dict[str, str] | None:
    """`URL | optional note | optional kind`; a previous error note is ignored. None if not a capture line."""
    line = re.split(r"\s+# error \d{4}-\d{2}-\d{2}:", line, maxsplit=1)[0].strip()
    if line.startswith(("- ", "* ")):
        line = line[2:].strip()
    fields = [part.strip() for part in line.split("|")]
    if not fields or not re.match(r"^https?://\S+$", fields[0]):
        return None
    note = fields[1] if len(fields) > 1 else ""
    kind = fields[2].lower().replace(" ", "_").replace("-", "_") if len(fields) > 2 else ""
    return {"url": fields[0], "note": note, "kind": kind if kind in KINDS else ""}


def inside_git_worktree(path: Path) -> Path | None:
    """Return the work-tree root containing path (existing or not), else None."""
    path = Path(os.path.abspath(os.path.expanduser(str(path))))
    for candidate in (path, *path.parents):
        if (candidate / ".git").exists():
            return candidate
    return None


def truncate_words(text: str, limit: int) -> str:
    words = text.split()
    return text.strip() if len(words) <= limit else " ".join(words[:limit]).rstrip(".,;:") + "…"


def parse_seed(text: str) -> dict[str, Any]:
    """Parse the seed file's YAML subset (top-level keys, sequences of flat mappings, quoted or
    plain scalars, flow lists). Keeps the CLI to a single dependency; tests compare with PyYAML."""
    data: dict[str, Any] = {}
    sequence: list | None = None
    item: dict | None = None

    def scalar(raw: str) -> Any:
        raw = raw.strip()
        if raw.startswith('"'):
            return json.loads(raw)
        if raw.startswith("'"):
            return raw[1:-1].replace("''", "'")
        if raw.startswith("["):
            if not raw.endswith("]"):
                raise ValueError(f"unterminated flow list: {raw}")
            inner = raw[1:-1].strip()
            return [v.strip() for v in next(csv.reader([inner], skipinitialspace=True))] if inner else []
        if re.fullmatch(r"-?\d+", raw):
            return int(raw)
        return raw

    def pair(target: dict, text_: str, lineno: int) -> None:
        key, sep, rest = text_.partition(":")
        if not sep or not re.fullmatch(r"[a-z_]+", key) or not rest.startswith(" "):
            raise ValueError(f"seed line {lineno}: expected 'key: value'")
        target[key] = scalar(rest)

    for lineno, raw in enumerate(text.splitlines(), start=1):
        stripped = raw.strip()
        if not stripped or stripped.startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip(" "))
        if indent == 0:
            key, sep, rest = stripped.partition(":")
            if not sep:
                raise ValueError(f"seed line {lineno}: expected a top-level key")
            if rest.strip():
                data[key] = scalar(rest)
                sequence = None
            else:
                sequence = data[key] = []
            item = None
        elif stripped.startswith("- ") and sequence is not None:
            item = {}
            sequence.append(item)
            pair(item, stripped[2:], lineno)
        elif item is not None:
            pair(item, stripped, lineno)
        else:
            raise ValueError(f"seed line {lineno}: unsupported structure")
    return data


# ---------------------------------------------------------------- pack rendering (pure)


def render_pack(pack: dict[str, Any], word_budget: int = 900) -> str:
    """Render a pack built by build_pack (or a fixture) as compact markdown."""
    for why_words, exemplars, study in ((35, 3, True), (20, 2, True), (14, 1, False), (8, 1, False)):
        text = _render(pack, why_words, exemplars, study)
        if len(text.split()) <= word_budget:
            return text
    return text


def _ref_line(asset: dict[str, Any]) -> str:
    bits = [f"[{asset['title']}]({asset['url']})" if asset.get("url") else asset["title"]]
    if asset.get("kind"):
        bits.append(asset["kind"].replace("_", " "))
    if asset.get("image"):
        bits.append(f"`{asset['image']}`")
    return " · ".join(bits)


def _render(pack: dict[str, Any], why_words: int, max_exemplars: int, show_study: bool) -> str:
    out = [f"# Reference pack: {pack['brief']}", ""]
    out.append(f"{pack['matched']} matching references from the 3RDWRONG Taste Graph"
               + (f" (kinds: {', '.join(pack['kinds'])})." if pack.get("kinds") else "."))
    out += ["", "## Do", ""]
    for item in pack["do"]:
        why = truncate_words(item.get("why") or "", why_words)
        out.append(f"- **{item['title']}**" + (f": {why}" if why else ""))
        for asset in item.get("exemplars", [])[:max_exemplars]:
            out.append(f"  - e.g. {_ref_line(asset)}")
    if not pack["do"]:
        out.append("- No curated principles yet.")
    out += ["", "## Don't", ""]
    for item in pack["dont"]:
        why = truncate_words(item.get("why") or "", why_words)
        out.append(f"- **{item['title']}**" + (f": {why}" if why else ""))
        for asset in item.get("examples", [])[:1]:
            out.append(f"  - seen in {_ref_line(asset)}")
    if not pack["dont"]:
        out.append("- No curated anti-patterns yet.")
    if show_study and pack.get("study"):
        out += ["", "## Study", ""]
        for asset in pack["study"]:
            why = truncate_words(asset.get("why") or "", why_words)
            out.append(f"- {_ref_line(asset)}" + (f": {why}" if why else ""))
    signals = pack.get("signals") or {}
    if any(signals.values()):
        out += ["", "## Signals", ""]
        for label in ("tone", "audience", "industry"):
            if signals.get(label):
                out.append(f"- {label.title()}: " + ", ".join(f"{name} ({count})" for name, count in signals[label]))
    if pack.get("images"):
        out += ["", "## Open these images", ""]
        out += [f"- `{path}`" for path in pack["images"][:3]]
    out += ["", f"> {GUARD}", ""]
    return "\n".join(out)


# ---------------------------------------------------------------- environment


def dsn() -> str:
    return os.environ.get("TASTE_GRAPH_DSN", DEFAULT_DSN)


def data_home(create: bool = True) -> Path:
    home = Path(os.path.expanduser(os.environ.get("TASTE_GRAPH_HOME", "~/.3rdwrong/taste"))).resolve()
    if repo := inside_git_worktree(home):
        raise TasteError(f"refusing data home {home}: it is inside the git work tree {repo}. "
                         "Captures are private and must never be committed; set TASTE_GRAPH_HOME outside any repository.")
    if create:
        for sub in ("media", "backups"):
            (home / sub).mkdir(parents=True, exist_ok=True)
    return home


def inbox_path(home: Path) -> Path:
    return Path(os.path.expanduser(os.environ.get("TASTE_GRAPH_INBOX", str(home / "inbox.md"))))


def pg_bin(name: str) -> str:
    for prefix in PG_PREFIXES:
        candidate = Path(prefix) / name
        if candidate.exists():
            return str(candidate)
    if found := shutil.which(name):
        return found
    raise TasteError(f"{name} not found; install PostgreSQL 17 with `brew install postgresql@17`")


def connect(conninfo: str | None = None):
    try:
        import psycopg
        from psycopg.rows import dict_row
    except ImportError as exc:  # pragma: no cover - uv installs it from the inline metadata
        raise TasteError("psycopg is missing; run with `uv run scripts/taste_graph.py`") from exc
    try:
        return psycopg.connect(conninfo or dsn(), row_factory=dict_row, connect_timeout=5)
    except psycopg.OperationalError as exc:
        raise TasteError(f"cannot connect to {conninfo or dsn()}: {str(exc).strip()}. "
                         "Is it running? `brew services start postgresql@17`, then `init`.") from exc


def ensure_database(conninfo: str) -> bool:
    import psycopg
    from psycopg import sql
    from psycopg.conninfo import conninfo_to_dict, make_conninfo

    name = conninfo_to_dict(conninfo).get("dbname") or os.environ.get("USER", "")
    try:
        psycopg.connect(conninfo, connect_timeout=5).close()
        return False
    except psycopg.OperationalError as exc:
        if "does not exist" not in str(exc):
            raise TasteError(f"cannot connect to {conninfo}: {str(exc).strip()}") from exc
    with psycopg.connect(make_conninfo(conninfo, dbname="postgres"), autocommit=True, connect_timeout=5) as admin:
        admin.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(name)))
    return True


def migrate(conn) -> list[str]:
    conn.execute("CREATE TABLE IF NOT EXISTS schema_migrations "
                 "(version text PRIMARY KEY, applied_at timestamptz NOT NULL DEFAULT now())")
    done = {row["version"] for row in conn.execute("SELECT version FROM schema_migrations")}
    applied = []
    for path in sorted((GRAPH_DIR / "migrations").glob("*.sql")):
        version = path.stem
        if version in done:
            continue
        with conn.transaction():
            conn.execute(path.read_text(encoding="utf-8"))
            conn.execute("INSERT INTO schema_migrations (version) VALUES (%s)", (version,))
        applied.append(version)
    conn.commit()
    return applied


# ---------------------------------------------------------------- graph operations


def jsonb(value: Any):
    from psycopg.types.json import Jsonb

    return Jsonb(value)


def find_node(conn, ref: str | int, default_type: str | None = None) -> dict | None:
    ref = str(ref).strip()
    if ref.isdigit():
        return conn.execute("SELECT * FROM node WHERE id = %s", (int(ref),)).fetchone()
    node_type, sep, name = ref.partition(":")
    if sep and node_type in NODE_TYPES and not name.startswith("//"):
        return conn.execute("SELECT * FROM node WHERE type = %s AND slug = %s", (node_type, slugify(name))).fetchone()
    if ref.startswith(("http://", "https://")):
        return conn.execute("SELECT * FROM node WHERE type = 'asset' AND url_norm = %s", (normalize_url(ref),)).fetchone()
    rows = conn.execute(
        "SELECT * FROM node WHERE slug = %s AND (%s::text IS NULL OR type = %s) ORDER BY type",
        (slugify(ref), default_type, default_type)).fetchall()
    if len(rows) > 1:
        raise TasteError(f"'{ref}' is ambiguous: " + ", ".join(f"{r['type']}:{r['slug']}" for r in rows))
    return rows[0] if rows else None


def ensure_node(conn, ref: str, default_type: str, status: str = "inbox", captured_by: str = "agent",
                verdict: str | None = None) -> dict:
    """Find a node by reference or create a non-asset node from 'type:Title' or 'Title'."""
    if node := find_node(conn, ref, None if ":" in ref else default_type):
        return node
    node_type, sep, title = ref.partition(":")
    if not sep or node_type not in NODE_TYPES:
        node_type, title = default_type, ref
    title = title.strip()
    if node_type == "asset" or not title or ref.strip().isdigit():
        raise TasteError(f"node not found: {ref}")
    return conn.execute(
        "INSERT INTO node (type, slug, title, status, captured_by, verdict) VALUES (%s, %s, %s, %s, %s, %s) "
        "ON CONFLICT (type, slug) DO UPDATE SET title = node.title RETURNING *",
        (node_type, slugify(title), title, status, captured_by, verdict)).fetchone()


def link(conn, src: int, rel: str, dst: int, note: str = "") -> None:
    if rel not in RELS:
        raise TasteError(f"unknown rel '{rel}'; use one of {', '.join(RELS)}")
    if src == dst:
        raise TasteError("a node cannot link to itself")
    conn.execute("INSERT INTO edge (src, rel, dst, note) VALUES (%s, %s, %s, %s) "
                 "ON CONFLICT (src, rel, dst) DO UPDATE SET note = CASE WHEN excluded.note <> '' "
                 "THEN excluded.note ELSE edge.note END", (src, rel, dst, note))


def unique_slug(conn, node_type: str, title: str) -> str:
    base = slugify(title)
    slug, n = base, 2
    while conn.execute("SELECT 1 FROM node WHERE type = %s AND slug = %s", (node_type, slug)).fetchone():
        slug, n = f"{base}-{n}", n + 1
    return slug


def load_seed(conn, path: Path = GRAPH_DIR / "seed.yaml") -> dict[str, int]:
    seed = parse_seed(path.read_text(encoding="utf-8"))
    added = {"nodes": 0, "edges": 0}
    for entry in seed.get("nodes", []):
        node_type, title = entry["type"], entry["title"]
        props = {k: v for k, v in entry.items() if k not in NODE_COLUMNS}
        url = clean_url(entry["url"]) if entry.get("url") else None
        row = conn.execute(
            "INSERT INTO node (type, slug, title, body, url, url_norm, kind, verdict, score, tags, props, status, captured_by) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 'curated', 'founder') ON CONFLICT DO NOTHING RETURNING id",
            (node_type, entry.get("slug") or slugify(title), title, entry.get("body", ""), url,
             normalize_url(url) if url and node_type == "asset" else None, entry.get("kind"),
             entry.get("verdict"), entry.get("score"), entry.get("tags", []), jsonb(props))).fetchone()
        added["nodes"] += row is not None
    for entry in seed.get("edges", []):
        src, dst = find_node(conn, entry["src"]), find_node(conn, entry["dst"])
        if not src or not dst:
            raise TasteError(f"seed edge references a missing node: {entry}")
        cur = conn.execute("INSERT INTO edge (src, rel, dst, note) VALUES (%s, %s, %s, %s) ON CONFLICT DO NOTHING",
                           (src["id"], entry["rel"], dst["id"], entry.get("note", "")))
        added["edges"] += cur.rowcount
    conn.commit()
    return added


def counts(conn) -> dict[str, Any]:
    nodes = {r["type"]: r["n"] for r in conn.execute("SELECT type, count(*) AS n FROM node GROUP BY type ORDER BY type")}
    status = {r["status"]: r["n"] for r in conn.execute("SELECT status, count(*) AS n FROM node GROUP BY status ORDER BY status")}
    kinds = {r["kind"]: r["n"] for r in conn.execute(
        "SELECT kind, count(*) AS n FROM node WHERE type = 'asset' GROUP BY kind ORDER BY kind")}
    rels = {r["rel"]: r["n"] for r in conn.execute("SELECT rel, count(*) AS n FROM edge GROUP BY rel ORDER BY rel")}
    return {"nodes": nodes, "node_total": sum(nodes.values()), "status": status, "asset_kinds": kinds,
            "edges": rels, "edge_total": sum(rels.values())}


# ---------------------------------------------------------------- capture


class _HttpOnlyRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        if urllib.parse.urlsplit(newurl).scheme not in ("http", "https"):
            raise TasteError(f"refusing redirect to non-http URL: {newurl}")
        return super().redirect_request(req, fp, code, msg, headers, newurl)


_OPENER = urllib.request.build_opener(_HttpOnlyRedirect)  # no cookie processor: never sends cookies


def http_get(url: str, max_bytes: int = MAX_DOWNLOAD) -> tuple[bytes, str]:
    request = urllib.request.Request(check_url(url), headers={"User-Agent": USER_AGENT})
    try:
        with _OPENER.open(request, timeout=TIMEOUT) as response:
            declared = int(response.headers.get("Content-Length") or 0)
            if declared > max_bytes:
                raise TasteError(f"download larger than {max_bytes // 1048576} MB: {url}")
            data = response.read(max_bytes + 1)
            if len(data) > max_bytes:
                raise TasteError(f"download larger than {max_bytes // 1048576} MB: {url}")
            return data, response.headers.get_content_type()
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        raise TasteError(f"fetch failed for {url}: {exc}") from exc


def http_json(url: str) -> dict:
    data, _ = http_get(url, max_bytes=1024 * 1024)
    try:
        return json.loads(data)
    except ValueError as exc:
        raise TasteError(f"unexpected non-JSON response from {url}") from exc


@dataclass
class Capture:
    title: str = ""
    content: str = ""
    media: list[tuple[bytes, str, str]] = field(default_factory=list)  # (data, variant, ext)
    props: dict[str, Any] = field(default_factory=dict)
    creator: str = ""
    platform: str = ""


def store_media(home: Path, captured: list[tuple[bytes, str, str]]) -> list[dict]:
    """Write media under media/YYYY/MM/<uuid>-<variant>.<ext>; names never come from URLs."""
    if not captured:
        return []
    today = dt.date.today()
    folder = home / "media" / f"{today:%Y}" / f"{today:%m}"
    folder.mkdir(parents=True, exist_ok=True)
    uid = uuid.uuid4()
    stored = []
    for data, variant, ext in captured:
        path = folder / f"{uid}-{variant}{ext}"
        path.write_bytes(data)
        stored.append({"path": str(path.relative_to(home)), "variant": variant,
                       "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)})
    return stored


def capture_image(url: str) -> Capture:
    data, content_type = http_get(url)
    if content_type not in IMAGE_TYPES:
        raise TasteError(f"not a supported image ({content_type}): {url}")
    return Capture(media=[(data, "image", IMAGE_TYPES[content_type])])


def _thumbnail(url: str, variant: str = "thumbnail") -> tuple[bytes, str, str]:
    data, content_type = http_get(url)
    if content_type not in IMAGE_TYPES:
        raise TasteError(f"thumbnail is not an image ({content_type})")
    return data, variant, IMAGE_TYPES[content_type]


def capture_youtube(url: str) -> Capture:
    vid = youtube_id(url)
    meta = http_json("https://www.youtube.com/oembed?" + urllib.parse.urlencode({"url": url, "format": "json"}))
    thumb = None
    for name in ("maxresdefault", "hqdefault"):
        try:
            thumb = _thumbnail(f"https://i.ytimg.com/vi/{vid}/{name}.jpg")
            break
        except TasteError:
            continue
    if thumb is None:
        raise TasteError(f"no public thumbnail found for {url}")
    return Capture(title=meta.get("title", ""), content=meta.get("title", ""), media=[thumb],
                   props={"author_url": meta.get("author_url", ""), "video_id": vid},
                   creator=meta.get("author_name", ""), platform="YouTube")


def oembed_text(markup: str) -> str:
    paragraph = re.search(r"<p[^>]*>(.*?)</p>", markup, re.S)
    text = re.sub(r"<br\s*/?>", "\n", paragraph.group(1) if paragraph else markup)
    return html.unescape(re.sub(r"<[^>]+>", "", text)).strip()


def capture_twitter(url: str) -> Capture:
    meta = http_json("https://publish.twitter.com/oembed?" + urllib.parse.urlencode(
        {"url": url, "omit_script": "1", "dnt": "true"}))
    text = oembed_text(meta.get("html", ""))
    author = meta.get("author_name", "")
    return Capture(title=f"{author}: {truncate_words(text, 10)}" if author else truncate_words(text, 12),
                   content=text, props={"author_url": meta.get("author_url", "")}, creator=author, platform="X")


def capture_tiktok(url: str) -> Capture:
    meta = http_json("https://www.tiktok.com/oembed?" + urllib.parse.urlencode({"url": url}))
    media = []
    if meta.get("thumbnail_url"):
        try:
            media.append(_thumbnail(meta["thumbnail_url"]))
        except TasteError:
            pass
    author = meta.get("author_name", "")
    return Capture(title=meta.get("title") or f"TikTok by {author}", content=meta.get("title", ""), media=media,
                   props={"author_url": meta.get("author_url", "")}, creator=author, platform="TikTok")


PAGE_META_JS = """() => {
  const meta = (n) => document.querySelector(`meta[name="${n}"],meta[property="${n}"]`)?.content || '';
  const h = document.querySelector('h1') || document.querySelector('h2');
  return JSON.stringify({title: document.title || '', description: meta('description') || meta('og:description'),
    og_image: meta('og:image'), headline: (h?.textContent || '').replace(/\\s+/g, ' ').trim().slice(0, 300)});
}"""


def capture_web(url: str, full_page: bool = False, mobile: bool = True) -> Capture:
    """Screenshot a public page with playwright-cli (fresh in-memory profile: no cookies, no login)."""
    cli = PLAYWRIGHT_CLI if Path(PLAYWRIGHT_CLI).exists() else shutil.which("playwright-cli")
    if not cli:
        raise TasteError("playwright-cli not found; install it or pass --file screenshots")
    session = f"tg-{os.getpid()}-{uuid.uuid4().hex[:6]}"
    capture = Capture()
    with tempfile.TemporaryDirectory(prefix="taste-capture-") as work:
        def pw(*args: str, timeout: int = 90) -> subprocess.CompletedProcess:
            return subprocess.run([cli, f"-s={session}", *args], cwd=work, capture_output=True,
                                  text=True, timeout=timeout, check=False)
        try:
            opened = pw("open", url, timeout=120)
            if opened.returncode:
                raise TasteError(f"browser could not open {url}: {(opened.stderr or opened.stdout).strip()[-300:]}")
            viewports = [("desktop", 1440, 900)] + ([("mobile", 390, 844)] if mobile else [])
            for variant, width, height in viewports:
                pw("resize", str(width), str(height))
                time.sleep(PAGE_SETTLE_SECONDS[variant != "desktop"])
                shot = Path(work) / f"{variant}.png"
                pw("screenshot", f"--filename={shot}", *(["--full-page"] if full_page else []), timeout=120)
                if not shot.exists() or shot.stat().st_size == 0:
                    raise TasteError(f"screenshot failed for {url} at {width}x{height}")
                capture.media.append((shot.read_bytes(), variant, ".png"))
                if variant == "desktop" and shot.stat().st_size < BLANK_PNG_BYTES:
                    capture.props["capture_warning"] = "desktop screenshot looks blank (intro or loader?); add --file screenshots"
                if variant == "desktop":
                    result = pw("--raw", "eval", PAGE_META_JS)
                    try:
                        meta = json.loads(result.stdout.strip())
                        meta = json.loads(meta) if isinstance(meta, str) else meta
                    except ValueError:
                        meta = {}
                    capture.title = meta.get("title", "")
                    capture.content = "\n".join(filter(None, (meta.get("headline", ""), meta.get("description", ""))))
                    capture.props = {k: meta[k] for k in ("description", "og_image", "headline") if meta.get(k)}
        except subprocess.TimeoutExpired as exc:
            raise TasteError(f"browser timed out capturing {url}") from exc
        finally:
            try:
                pw("close", timeout=30)
            except subprocess.TimeoutExpired:
                pass
    return capture


def capture_url(url: str, method: str, full_page: bool = False) -> Capture:
    if method == "youtube":
        return capture_youtube(url)
    if method == "twitter":
        return capture_twitter(url)
    if method == "tiktok":
        return capture_tiktok(url)
    if method == "image":
        return capture_image(url)
    if method == "walled":
        capture = capture_web(url, full_page=False, mobile=False)  # best effort: public view only
        host = (urllib.parse.urlsplit(url).hostname or "").removeprefix("www.")
        capture.platform = next((name for key, name in PLATFORM_NAMES.items() if host.endswith(key)), "")
        return capture
    return capture_web(url, full_page=full_page)


def read_files(paths: list[str]) -> list[tuple[bytes, str, str]]:
    media = []
    for n, raw in enumerate(paths, start=1):
        path = Path(raw).expanduser()
        if not path.is_file():
            raise TasteError(f"file not found: {raw}")
        ext = path.suffix.lower()
        media.append((path.read_bytes(), f"file{n}", ".jpg" if ext == ".jpeg" else ext if ext in FILE_EXTS else ".bin"))
    return media


# ---------------------------------------------------------------- add / ingest


def add_reference(conn, home: Path, *, url: str | None = None, files: list[str] | None = None,
                  kind: str | None = None, verdict: str | None = None, why: str = "", title: str = "",
                  tags: list[str] | None = None, brand: str = "", creator: str = "", platform: str = "",
                  patterns: list[str] | None = None, violates: list[str] | None = None, tone: str = "",
                  score: int | None = None, text: str = "", status: str = "inbox", by: str = "agent",
                  full_page: bool = False, capture_fn=capture_url) -> tuple[dict, bool]:
    """Capture and upsert one asset. Returns (node, created)."""
    if status not in ("inbox", "curated"):
        raise TasteError("new captures enter as inbox or curated")
    if status == "curated" and by != "founder":
        raise TasteError("only the founder curates: agent captures enter as status=inbox")
    if not url and not files:
        raise TasteError("give a URL or at least one --file")
    url = clean_url(url) if url else None
    norm = normalize_url(url) if url else None
    detected_kind, method = detect(url) if url else ("other", "file")
    existing = conn.execute("SELECT * FROM node WHERE type = 'asset' AND url_norm = %s", (norm,)).fetchone() if norm else None

    capture = Capture()
    if url and not (existing and existing["media"]):
        try:
            capture = capture_fn(url, method, full_page)
        except TasteError:
            if not files and not text:
                raise
            capture = Capture()  # walled or failed page: rely on supplied files/text
    capture.media.extend(read_files(files or []))
    if not existing and not capture.media and not capture.content and not text:
        hint = " This site needs login: pass --file screenshots and --text." if method == "walled" else ""
        raise TasteError(f"capture produced no media or text for {url or files}.{hint}")
    media = store_media(home, capture.media)
    content = text or capture.content
    explicit_title = title
    title = title or capture.title or (urllib.parse.urlsplit(url).hostname if url else Path(files[0]).stem)

    if existing:
        props = dict(capture.props)
        if why and existing["body"]:
            # Re-adding never overwrites existing analysis (edit it with `update --why`); keep the note alongside.
            props["notes"] = [*existing["props"].get("notes", []), f"{by} {dt.date.today()}: {why}"]
            why = ""
        if existing["status"] == "curated" and by != "founder":
            kind, verdict, score, explicit_title = None, None, None, ""  # only the founder edits curated items
        node = conn.execute(
            "UPDATE node SET title = CASE WHEN %(title_given)s THEN %(title)s ELSE title END, "
            "body = CASE WHEN %(why)s <> '' THEN %(why)s ELSE body END, "
            "kind = coalesce(%(kind)s, kind), verdict = coalesce(%(verdict)s, verdict), score = coalesce(%(score)s, score), "
            "status = CASE WHEN %(promote)s THEN 'curated' ELSE status END, "
            "content = CASE WHEN %(content)s <> '' THEN %(content)s ELSE content END, "
            "media = media || %(media)s, tags = ARRAY(SELECT DISTINCT unnest(tags || %(tags)s::text[]) ORDER BY 1), "
            "props = props || %(props)s WHERE id = %(id)s RETURNING *",
            {"title_given": bool(explicit_title), "title": explicit_title,
             "why": why, "kind": kind, "verdict": verdict, "score": score, "promote": status == "curated",
             "content": content, "media": jsonb(media), "tags": sorted(set(tags or [])),
             "props": jsonb(props), "id": existing["id"]}).fetchone()
        created = False
    else:
        node = conn.execute(
            "INSERT INTO node (type, slug, title, body, url, url_norm, kind, verdict, score, status, captured_by, "
            "media, content, tags, props) VALUES ('asset', %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING *",
            (unique_slug(conn, "asset", title), title, why, url, norm, kind or detected_kind, verdict or "exemplar",
             score, status, by, jsonb(media), content, sorted(set(tags or [])), jsonb(capture.props))).fetchone()
        created = True

    def attach(ref: str, default_type: str, rel: str, node_verdict: str | None = None) -> None:
        target = ensure_node(conn, ref, default_type, status=status, captured_by=by, verdict=node_verdict)
        link(conn, node["id"], rel, target["id"])

    pattern_verdict = "anti_pattern" if node["verdict"] == "anti_pattern" else "exemplar"
    for ref in patterns or []:
        attach(ref, "pattern", "exemplifies", pattern_verdict)
    for ref in violates or []:
        attach(ref, "principle", "violates", "exemplar")
    for ref, default_type, rel in ((brand, "brand", "by"), (creator or capture.creator, "creator", "by"),
                                   (platform or capture.platform, "platform", "on"), (tone, "tone", "has_tone")):
        if ref:
            attach(ref, default_type, rel)
    conn.commit()
    return node, created


def ingest(conn, home: Path, path: Path, capture_fn=capture_url, today: dt.date | None = None) -> dict[str, int]:
    """Capture every `URL | note | kind` line; move successes to a dated Processed section."""
    if not path.exists():
        raise TasteError(f"inbox not found: {path}")
    today = today or dt.date.today()
    lines = path.read_text(encoding="utf-8").splitlines()
    heading = f"## Processed {today:%Y-%m-%d}"
    try:
        first_processed = next(i for i, line in enumerate(lines) if line.startswith("## Processed "))
    except StopIteration:
        first_processed = len(lines)
    pending, done, result = [], [], {"captured": 0, "failed": 0}
    for i, line in enumerate(lines):
        entry = parse_inbox_line(line) if i < first_processed else None
        if entry is None:
            pending.append(line)
            continue
        try:
            node, _ = add_reference(conn, home, url=entry["url"], why=entry["note"], kind=entry["kind"] or None,
                                    status="inbox", by="founder", capture_fn=capture_fn)
            done.append(f"- {line.split(' # error ')[0].strip()} → #{node['id']}")
            result["captured"] += 1
        except TasteError as exc:
            conn.rollback()
            clean = re.split(r"\s+# error \d{4}-\d{2}-\d{2}:", line)[0].rstrip()
            pending.append(f"{clean} # error {today:%Y-%m-%d}: {str(exc).splitlines()[0][:200]}")
            result["failed"] += 1
    if done:
        last_heading = next((line for line in reversed(pending) if line.startswith("## ")), None)
        while pending and not pending[-1].strip():
            pending.pop()
        pending += done if last_heading == heading else ["", heading, "", *done]
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text("\n".join(pending).rstrip("\n") + "\n", encoding="utf-8")
    os.replace(tmp, path)
    return result


# ---------------------------------------------------------------- pack


PACK_SQL = """
WITH q AS (SELECT websearch_to_tsquery('english', %(tsq)s) AS tsq)
SELECT n.id, n.slug, n.title, n.url, n.kind, n.verdict, n.score, n.body, n.media,
       ts_rank_cd(n.search, q.tsq) AS fts,
       similarity(n.title || ' ' || tg_tags(n.tags), %(brief)s) AS trg,
       coalesce((SELECT max(ts_rank_cd(p.search, q.tsq)) FROM edge e JOIN node p ON p.id = e.dst
                 WHERE e.src = n.id AND e.rel IN ('exemplifies', 'violates', 'has_tone', 'for')), 0) AS link_fts
FROM node n, q
WHERE n.type = 'asset' AND n.status = ANY(%(statuses)s)
  AND (%(kinds)s::text[] IS NULL OR n.kind = ANY(%(kinds)s))
"""


def _rank_assets(rows: list[dict], hinted: set[str]) -> list[dict]:
    ranked = []
    for row in rows:
        trg = row["trg"] if row["trg"] >= 0.1 else 0.0
        relevance = row["fts"] + 0.5 * row["link_fts"] + 0.5 * trg + (0.3 if row["kind"] in hinted else 0.0)
        ranked.append({**row, "relevance": relevance, "rank": relevance + 0.2 * (row["score"] or 3) / 5})
    ranked.sort(key=lambda r: (-r["rank"], r["id"]))
    relevant = [r for r in ranked if r["relevance"] > 0]
    return relevant or ranked


def _asset_ref(home: Path, row: dict) -> dict:
    image = ""
    for item in sorted(row["media"] or [], key=lambda m: m.get("variant") != "desktop"):
        if Path(item.get("path", "")).suffix.lower() in (".png", ".jpg", ".webp", ".gif", ".avif"):
            image = str(home / item["path"])
            break
    return {"id": row["id"], "title": row["title"], "url": row["url"], "kind": row["kind"],
            "why": row["body"], "image": image}


def build_pack(conn, home: Path, brief: str, kinds: list[str] | None = None, limit: int = 8,
               include_inbox: bool = False) -> dict[str, Any]:
    statuses = ["curated", "inbox"] if include_inbox else ["curated"]
    params = {"tsq": tsquery_text(brief), "brief": brief, "statuses": statuses, "kinds": kinds or None}
    rows = conn.execute(PACK_SQL, params).fetchall()
    hinted = set(kinds or []) or kind_hints(brief)
    do_assets = _rank_assets([r for r in rows if r["verdict"] != "anti_pattern"], hinted)[:limit]
    dont_assets = _rank_assets([r for r in rows if r["verdict"] == "anti_pattern"], hinted)[:max(2, limit // 2)]
    by_id = {r["id"]: r for r in do_assets + dont_assets}
    order = {r["id"]: i for i, r in enumerate(do_assets + dont_assets)}

    edges = conn.execute(
        "SELECT e.src, e.rel, p.id, p.type, p.slug, p.title, p.body, p.verdict FROM edge e JOIN node p ON p.id = e.dst "
        "WHERE e.src = ANY(%s) AND p.status <> 'archived' ORDER BY e.src, p.slug",
        ([*by_id],)).fetchall()
    do_items: dict[int, dict] = {}
    dont_items: dict[int, dict] = {}
    signals: dict[str, dict[str, int]] = {"tone": {}, "audience": {}, "industry": {}}
    for e in edges:
        asset = by_id[e["src"]]
        if e["type"] in signals:
            signals[e["type"]][e["title"]] = signals[e["type"]].get(e["title"], 0) + 1
            continue
        if e["type"] not in ("pattern", "principle", "technique"):
            continue
        is_dont = e["rel"] == "violates" or e["verdict"] == "anti_pattern" or asset["verdict"] == "anti_pattern"
        if e["rel"] not in ("exemplifies", "violates"):
            continue
        bucket = dont_items if is_dont else do_items
        title = f"Ignoring “{e['title']}”" if e["rel"] == "violates" and e["verdict"] != "anti_pattern" else e["title"]
        item = bucket.setdefault(e["id"], {"id": e["id"], "title": title, "why": e["body"], "assets": [], "weight": 0.0})
        item["assets"].append(asset)
        item["weight"] += asset["rank"]

    def fill(bucket: dict[int, dict], anti: bool, cap: int = 6) -> list[dict]:
        items = sorted(bucket.values(), key=lambda i: (-i["weight"], i["title"]))[:cap]
        if len(items) < cap:
            extra = conn.execute(
                "WITH q AS (SELECT websearch_to_tsquery('english', %s) AS tsq) "
                "SELECT id, title, body, ts_rank_cd(search, q.tsq) AS fts FROM node, q "
                "WHERE type IN ('pattern', 'principle', 'technique') AND status = 'curated' "
                "AND (coalesce(verdict, '') = 'anti_pattern') = %s AND NOT (id = ANY(%s)) "
                "ORDER BY fts DESC, coalesce(score, 3) DESC, id LIMIT %s",  # ties keep seed order
                (params["tsq"], anti, [*bucket], cap - len(items))).fetchall()
            items += [{"id": r["id"], "title": r["title"], "why": r["body"], "assets": []} for r in extra]
        return items

    do_list = fill(do_items, anti=False)
    dont_list = fill(dont_items, anti=True)
    shown = set()
    pack_do, pack_dont = [], []
    for item in do_list:
        assets = sorted(item["assets"], key=lambda a: order[a["id"]])[:3]
        shown.update(a["id"] for a in assets)
        pack_do.append({"id": item["id"], "title": item["title"], "why": item["why"],
                        "exemplars": [_asset_ref(home, a) for a in assets]})
    for item in dont_list:
        assets = sorted(item["assets"], key=lambda a: order[a["id"]])[:1]
        shown.update(a["id"] for a in assets)
        pack_dont.append({"id": item["id"], "title": item["title"], "why": item["why"],
                          "examples": [_asset_ref(home, a) for a in assets]})
    study = [_asset_ref(home, a) for a in do_assets if a["id"] not in shown][:5]
    images = []
    for asset in do_assets:
        ref = _asset_ref(home, asset)
        if ref["image"] and Path(ref["image"]).exists():
            images.append(ref["image"])
    return {
        "brief": brief, "kinds": kinds or [], "matched": len(do_assets) + len(dont_assets),
        "do": pack_do, "dont": pack_dont, "study": study, "images": images[:3],
        "signals": {k: sorted(v.items(), key=lambda kv: (-kv[1], kv[0])) for k, v in signals.items()},
        "asset_ids": sorted(by_id), "node_ids": sorted(i["id"] for i in pack_do + pack_dont),
    }


def record_usage(conn, pack: dict, project: str) -> int:
    node = ensure_node(conn, f"project:{project}", "project")
    used = [*pack["asset_ids"], *pack["node_ids"]]
    for node_id in used:
        link(conn, node_id, "used_in", node["id"], pack["brief"][:200])
    conn.commit()
    return len(used)


# ---------------------------------------------------------------- commands


def _print_rows(rows: list[dict], columns: tuple[str, ...]) -> None:
    for row in rows:
        print("  ".join(str(row.get(c) if row.get(c) is not None else "-") for c in columns))


def cmd_init(args) -> None:
    home = data_home()
    conninfo = dsn()
    created = ensure_database(conninfo)
    with connect() as conn:
        version = conn.execute("SHOW server_version").fetchone()["server_version"]
        applied = migrate(conn)
        seeded = load_seed(conn) if args.seed else None
        report = counts(conn)
    playwright = PLAYWRIGHT_CLI if Path(PLAYWRIGHT_CLI).exists() else shutil.which("playwright-cli")
    print(f"postgres: reachable (server {version}) · database {'created' if created else 'exists'} · {conninfo}")
    print(f"migrations applied now: {', '.join(applied) or 'none (up to date)'}")
    if seeded is not None:
        print(f"seed: {seeded['nodes']} nodes and {seeded['edges']} edges added (existing entries left untouched)")
    print(f"playwright-cli: {playwright or 'MISSING (web screenshots unavailable; use --file)'}")
    print(f"data home: {home} · inbox: {inbox_path(home)}")
    print(f"nodes: {report['node_total']} {json.dumps(report['nodes'])}")
    print(f"edges: {report['edge_total']} {json.dumps(report['edges'])}")


def cmd_add(args) -> None:
    home = data_home()
    with connect() as conn:
        node, created = add_reference(
            conn, home, url=args.url, files=args.file, kind=args.kind, verdict=args.verdict, why=args.why or "",
            title=args.title or "", tags=_split(args.tags), brand=args.brand or "", creator=args.creator or "",
            platform=args.platform or "", patterns=args.pattern, violates=args.violates, tone=args.tone or "",
            score=args.score, text=args.text or "", status=args.status, by=args.by, full_page=args.full_page)
    print(f"{'added' if created else 'updated'} #{node['id']} asset:{node['slug']} [{node['status']}] {node['title']}")
    for item in node["media"]:
        print(f"  media: {home / item['path']}")
    if warning := node["props"].get("capture_warning"):
        print(f"  warning: {warning}")


def cmd_ingest(args) -> None:
    home = data_home()
    path = Path(args.inbox).expanduser() if args.inbox else inbox_path(home)
    with connect() as conn:
        result = ingest(conn, home, path)
    print(f"ingested {path}: {result['captured']} captured (status inbox), {result['failed']} failed (left in place)")


def cmd_list(args) -> None:
    with connect() as conn:
        rows = conn.execute(
            "SELECT id, status, kind, verdict, score, slug, title, url FROM node WHERE type = %(type)s "
            "AND (%(status)s::text IS NULL OR status = %(status)s) AND (%(kind)s::text IS NULL OR kind = %(kind)s) "
            "AND (%(since)s::date IS NULL OR created_at >= %(since)s::date) ORDER BY created_at DESC, id DESC LIMIT %(limit)s",
            {"type": args.type, "status": args.status, "kind": args.kind, "since": args.since, "limit": args.limit}).fetchall()
    _print_rows(rows, ("id", "status", "kind", "verdict", "score", "slug", "url"))
    print(f"{len(rows)} {args.type} node(s)")


def cmd_show(args) -> None:
    home = data_home(create=False)
    with connect() as conn:
        node = find_node(conn, args.ref)
        if not node:
            raise TasteError(f"node not found: {args.ref}")
        out_edges = conn.execute("SELECT e.rel, e.note, n.id, n.type, n.slug, n.title FROM edge e JOIN node n ON n.id = e.dst "
                                 "WHERE e.src = %s ORDER BY e.rel, n.slug", (node["id"],)).fetchall()
        in_edges = conn.execute("SELECT e.rel, e.note, n.id, n.type, n.slug, n.title FROM edge e JOIN node n ON n.id = e.src "
                                "WHERE e.dst = %s ORDER BY e.rel, n.slug", (node["id"],)).fetchall()
    print(f"#{node['id']} {node['type']}:{node['slug']} — {node['title']}")
    for key in ("url", "kind", "verdict", "score", "status", "captured_by", "tags", "created_at"):
        if node.get(key) not in (None, "", []):
            print(f"  {key}: {node[key]}")
    if node["body"]:
        print(f"  why: {node['body']}")
    if node["content"]:
        print(f"  captured text (private): {truncate_words(node['content'], 60)}")
    for item in node["media"]:
        print(f"  media [{item['variant']}]: {home / item['path']}")
    for edge in out_edges:
        print(f"  → {edge['rel']} #{edge['id']} {edge['type']}:{edge['slug']}" + (f" ({edge['note']})" if edge["note"] else ""))
    for edge in in_edges:
        print(f"  ← {edge['rel']} #{edge['id']} {edge['type']}:{edge['slug']}" + (f" ({edge['note']})" if edge["note"] else ""))


def cmd_search(args) -> None:
    with connect() as conn:
        rows = conn.execute(
            "WITH q AS (SELECT websearch_to_tsquery('english', %(tsq)s) AS tsq) "
            "SELECT id, type, slug, status, title, ts_rank_cd(search, q.tsq) + 0.5 * similarity(title || ' ' || tg_tags(tags), %(q)s) AS r "
            "FROM node, q WHERE search @@ q.tsq OR similarity(title || ' ' || tg_tags(tags), %(q)s) >= 0.2 "
            "ORDER BY r DESC, id LIMIT %(limit)s", {"tsq": tsquery_text(args.query), "q": args.query, "limit": args.limit}).fetchall()
    for row in rows:
        print(f"#{row['id']}  {row['type']}:{row['slug']}  [{row['status']}]  {row['title']}")
    print(f"{len(rows)} result(s)")


def cmd_update(args) -> None:
    changes = {k: v for k, v in (("verdict", args.verdict), ("body", args.why), ("score", args.score),
                                  ("status", args.status), ("kind", args.kind), ("title", args.title)) if v is not None}
    if args.tags is not None:
        changes["tags"] = sorted(set(_split(args.tags)))
    if not changes:
        raise TasteError("nothing to update")
    with connect() as conn:
        node = find_node(conn, args.ref)
        if not node:
            raise TasteError(f"node not found: {args.ref}")
        if "kind" in changes and node["type"] != "asset":
            raise TasteError("only assets have a kind")
        from psycopg import sql
        query = sql.SQL("UPDATE node SET {} WHERE id = %s RETURNING *").format(
            sql.SQL(", ").join(sql.SQL("{} = %s").format(sql.Identifier(k)) for k in changes))
        node = conn.execute(query, (*changes.values(), node["id"])).fetchone()
    print(f"updated #{node['id']} {node['type']}:{node['slug']} [{node['status']}] {', '.join(changes)}")


def cmd_link(args) -> None:
    with connect() as conn:
        src = find_node(conn, args.src)
        if not src:
            raise TasteError(f"source node not found: {args.src}")
        dst = ensure_node(conn, args.dst, "pattern")
        link(conn, src["id"], args.rel, dst["id"], args.note or "")
        conn.commit()
    print(f"linked #{src['id']} {src['type']}:{src['slug']} -{args.rel}-> #{dst['id']} {dst['type']}:{dst['slug']}")


def cmd_pack(args) -> None:
    home = data_home(create=False)
    for kind in args.kind or []:
        if kind not in KINDS:
            raise TasteError(f"unknown kind '{kind}'")
    with connect() as conn:
        pack = build_pack(conn, home, args.brief, args.kind, args.limit, args.include_inbox)
        if args.project:
            pack["recorded_used_in"] = record_usage(conn, pack, args.project)
    print(json.dumps(pack, indent=2, ensure_ascii=False) if args.format == "json" else render_pack(pack))


def cmd_stats(args) -> None:
    home = data_home(create=False)
    with connect() as conn:
        report = counts(conn)
    files = [p for p in (home / "media").rglob("*") if p.is_file()] if (home / "media").exists() else []
    report["media_files"] = len(files)
    report["media_mb"] = round(sum(p.stat().st_size for p in files) / 1048576, 1)
    print(json.dumps(report, indent=2))


def backup(home: Path, keep: int, conninfo: str | None = None) -> Path:
    folder = home / "backups"
    folder.mkdir(parents=True, exist_ok=True)
    target = folder / f"taste_graph-{dt.datetime.now():%Y%m%d-%H%M%S}.dump"
    result = subprocess.run([pg_bin("pg_dump"), "-Fc", f"--dbname={conninfo or dsn()}", "-f", str(target)],
                            capture_output=True, text=True, timeout=600, check=False)
    if result.returncode:
        target.unlink(missing_ok=True)
        raise TasteError(f"pg_dump failed: {result.stderr.strip()}")
    for old in sorted(folder.glob("taste_graph-*.dump"))[:-keep] if keep > 0 else []:
        old.unlink()
    return target


def cmd_backup(args) -> None:
    target = backup(data_home(), args.keep)
    print(f"backup written: {target} ({target.stat().st_size} bytes); keeping the newest {args.keep}")


def _split(value: str | None) -> list[str]:
    return [t.strip() for t in (value or "").split(",") if t.strip()]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="taste_graph", description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("init", help="create the database, apply migrations, optionally seed")
    p.add_argument("--seed", action="store_true", help="load taste/graph/seed.yaml (adds missing entries only)")
    p.set_defaults(func=cmd_init)

    p = sub.add_parser("add", help="capture a reference by URL and/or files")
    p.add_argument("url", nargs="?")
    p.add_argument("--file", action="append", help="local screenshot/file; repeatable")
    p.add_argument("--kind", choices=KINDS)
    p.add_argument("--verdict", choices=VERDICTS)
    p.add_argument("--why", help="the studio's analysis: what works and the transferable principle")
    p.add_argument("--title")
    p.add_argument("--tags", help="comma-separated")
    p.add_argument("--brand")
    p.add_argument("--creator")
    p.add_argument("--platform")
    p.add_argument("--pattern", action="append", help="pattern it exemplifies ('principle:X' or 'technique:X' allowed); repeatable")
    p.add_argument("--violates", action="append", help="principle it violates; repeatable")
    p.add_argument("--tone")
    p.add_argument("--score", type=int, choices=range(1, 6))
    p.add_argument("--text", help="captured copy (private; stays in the local database)")
    p.add_argument("--status", choices=("inbox", "curated"), default="inbox")
    p.add_argument("--by", choices=("founder", "agent"), default="agent")
    p.add_argument("--full-page", action="store_true")
    p.set_defaults(func=cmd_add)

    p = sub.add_parser("ingest", help="capture every line of the inbox file as status=inbox")
    p.add_argument("--inbox")
    p.set_defaults(func=cmd_ingest)

    p = sub.add_parser("list", help="list nodes")
    p.add_argument("--type", choices=NODE_TYPES, default="asset")
    p.add_argument("--status", choices=STATUSES)
    p.add_argument("--kind", choices=KINDS)
    p.add_argument("--since", type=dt.date.fromisoformat, help="YYYY-MM-DD")
    p.add_argument("--limit", type=int, default=50)
    p.set_defaults(func=cmd_list)

    p = sub.add_parser("show", help="show a node and its neighbours")
    p.add_argument("ref", help="id, type:slug, slug or URL")
    p.set_defaults(func=cmd_show)

    p = sub.add_parser("search", help="full-text and fuzzy search across all nodes")
    p.add_argument("query")
    p.add_argument("--limit", type=int, default=20)
    p.set_defaults(func=cmd_search)

    p = sub.add_parser("update", help="change a node's verdict, analysis, score, status, tags or kind")
    p.add_argument("ref")
    p.add_argument("--verdict", choices=VERDICTS)
    p.add_argument("--why")
    p.add_argument("--score", type=int, choices=range(1, 6))
    p.add_argument("--status", choices=STATUSES)
    p.add_argument("--tags", help="comma-separated; replaces existing tags")
    p.add_argument("--kind", choices=KINDS)
    p.add_argument("--title")
    p.set_defaults(func=cmd_update)

    p = sub.add_parser("link", help="add an edge; dst may be 'pattern:Title' to auto-create")
    p.add_argument("src")
    p.add_argument("rel", choices=RELS)
    p.add_argument("dst")
    p.add_argument("--note")
    p.set_defaults(func=cmd_link)

    p = sub.add_parser("pack", help="render a reference pack for a creative brief")
    p.add_argument("brief")
    p.add_argument("--kind", action="append", help="restrict to asset kind; repeatable")
    p.add_argument("--limit", type=int, default=8)
    p.add_argument("--project", help="record used_in edges to this project slug")
    p.add_argument("--include-inbox", action="store_true")
    p.add_argument("--format", choices=("md", "json"), default="md")
    p.set_defaults(func=cmd_pack)

    p = sub.add_parser("stats", help="counts by type, status, kind and relation")
    p.set_defaults(func=cmd_stats)

    p = sub.add_parser("backup", help="pg_dump -Fc into the data home's backups/, rotated")
    p.add_argument("--keep", type=int, default=14)
    p.set_defaults(func=cmd_backup)

    args = parser.parse_args(argv)
    try:
        args.func(args)
    except TasteError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
