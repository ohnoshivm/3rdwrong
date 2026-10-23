from __future__ import annotations

import datetime as dt
import importlib.util
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("taste_graph", ROOT / "scripts" / "taste_graph.py")
tg = importlib.util.module_from_spec(SPEC)
sys.modules["taste_graph"] = tg
SPEC.loader.exec_module(tg)

PNG = b"\x89PNG\r\n\x1a\n" + b"\x00" * 64


class UrlTests(unittest.TestCase):
    def test_normalize_strips_tracking_www_fragment_and_trailing_slash(self):
        self.assertEqual(tg.normalize_url("HTTP://www.Example.com/work/?utm_source=x&b=2&a=1#top"),
                         "https://example.com/work?a=1&b=2")
        self.assertEqual(tg.normalize_url("https://example.com"), "https://example.com/")
        self.assertEqual(tg.normalize_url("https://example.com/?s=search"), "https://example.com/?s=search")

    def test_normalize_social_urls(self):
        for url in ("https://youtu.be/abc123XYZ_-?si=foo", "https://www.youtube.com/watch?v=abc123XYZ_-&t=30",
                    "https://m.youtube.com/shorts/abc123XYZ_-"):
            self.assertEqual(tg.normalize_url(url), "https://youtube.com/watch?v=abc123XYZ_-")
        self.assertEqual(tg.normalize_url("https://twitter.com/Someone/status/123?s=20"),
                         tg.normalize_url("https://x.com/someone/status/123"))

    def test_only_http_urls(self):
        for bad in ("file:///etc/passwd", "javascript:alert(1)", "ftp://example.com/x", "notaurl"):
            with self.assertRaises(tg.TasteError):
                tg.normalize_url(bad)

    def test_detect_kind_and_method(self):
        cases = {
            "https://www.youtube.com/watch?v=abc": ("thumbnail", "youtube"),
            "https://youtube.com/shorts/abc": ("short_video", "youtube"),
            "https://x.com/a/status/1": ("tweet", "twitter"),
            "https://www.tiktok.com/@a/video/1": ("tiktok", "tiktok"),
            "https://www.instagram.com/reel/abc/": ("reel", "walled"),
            "https://www.linkedin.com/posts/abc": ("linkedin_post", "walled"),
            "https://cdn.example.com/logo.PNG": ("other", "image"),
            "https://lusion.co/": ("landing_page", "web"),
        }
        for url, expected in cases.items():
            self.assertEqual(tg.detect(url), expected, url)

    def test_kind_hints_and_tsquery(self):
        self.assertEqual(tg.kind_hints("landing page hero for a design-engineering studio"), {"landing_page", "website"})
        self.assertIn("thumbnail", tg.kind_hints("YouTube thumbnail for a launch video"))
        self.assertEqual(tg.kind_hints("quarterly finance report"), set())
        self.assertEqual(tg.tsquery_text("Hero, hero & design-engineering"), "hero or design-engineering")

    def test_slugify(self):
        self.assertEqual(tg.slugify("We Are Büro"), "we-are-buro")
        self.assertEqual(tg.slugify("KOKUYO — Curiosity is Life"), "kokuyo-curiosity-is-life")
        self.assertEqual(tg.slugify("!!!"), "untitled")


class InboxTests(unittest.TestCase):
    def test_parse_inbox_line(self):
        self.assertEqual(tg.parse_inbox_line("https://a.com | great hero | landing page"),
                         {"url": "https://a.com", "note": "great hero", "kind": "landing_page"})
        self.assertEqual(tg.parse_inbox_line("- https://a.com"), {"url": "https://a.com", "note": "", "kind": ""})
        self.assertEqual(tg.parse_inbox_line("https://a.com | n | nonsense")["kind"], "")
        self.assertEqual(tg.parse_inbox_line("https://a.com | n # error 2026-10-23: boom")["note"], "n")
        for line in ("", "# Taste inbox", "see https://a.com", "javascript:alert(1) | x"):
            self.assertIsNone(tg.parse_inbox_line(line))


class GuardTests(unittest.TestCase):
    def test_inside_git_worktree(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp) / "repo"
            (repo / ".git").mkdir(parents=True)
            self.assertEqual(tg.inside_git_worktree(repo / "not" / "yet" / "created"), repo)
            self.assertIsNone(tg.inside_git_worktree(Path(tmp) / "elsewhere"))

    def test_data_home_refuses_repository(self):
        with mock.patch.dict(os.environ, {"TASTE_GRAPH_HOME": str(ROOT / "captures")}):
            with self.assertRaises(tg.TasteError):
                tg.data_home()
        self.assertFalse((ROOT / "captures").exists())

    def test_repository_graph_folder_holds_no_captures(self):
        allowed = {".sql", ".yaml", ".md"}
        found = [p for p in (ROOT / "taste" / "graph").rglob("*") if p.is_file() and p.suffix not in allowed]
        self.assertEqual(found, [])


class SeedTests(unittest.TestCase):
    def setUp(self):
        self.text = (ROOT / "taste" / "graph" / "seed.yaml").read_text(encoding="utf-8")
        self.seed = tg.parse_seed(self.text)

    def test_matches_pyyaml_when_available(self):
        try:
            import yaml
        except ImportError:
            self.skipTest("PyYAML not installed")
        self.assertEqual(self.seed, yaml.safe_load(self.text))

    def test_seed_is_consistent(self):
        nodes = self.seed["nodes"]
        refs = {f"{n['type']}:{n.get('slug') or tg.slugify(n['title'])}" for n in nodes}
        self.assertEqual(len(refs), len(nodes), "duplicate type:slug in seed")
        for node in nodes:
            self.assertIn(node["type"], tg.NODE_TYPES)
            if node.get("url"):
                self.assertTrue(node["url"].startswith("https://"), node["url"])
            if node.get("kind"):
                self.assertIn(node["kind"], tg.KINDS)
        for edge in self.seed["edges"]:
            self.assertIn(edge["src"], refs)
            self.assertIn(edge["dst"], refs)
            self.assertIn(edge["rel"], tg.RELS)
        swipe = [n for n in nodes if set(n.get("tags", [])) & {"tier-1", "tier-2", "tier-3"}]
        self.assertEqual(len(swipe), 37, "every swipe-file entry is seeded")


def fixture_pack(images: int = 5, do_items: int = 6) -> dict:
    asset = {"id": 1, "title": "Example", "url": "https://example.com/", "kind": "website",
             "why": "word " * 50, "image": "/tmp/x-desktop.png"}
    return {
        "brief": "landing page hero", "kinds": [], "matched": 3,
        "do": [{"id": i, "title": f"Principle {i}", "why": "because " * 60, "exemplars": [asset] * 3}
               for i in range(do_items)],
        "dont": [{"id": 99, "title": "Filler copy", "why": "generic claims", "examples": [asset]}],
        "study": [asset] * 5,
        "signals": {"tone": [("dry wit", 2)], "audience": [], "industry": []},
        "images": [f"/tmp/{i}.png" for i in range(images)],
    }


class RenderTests(unittest.TestCase):
    def test_render_contains_sections_and_guard(self):
        text = tg.render_pack(fixture_pack())
        for heading in ("## Do", "## Don't", "## Open these images", "## Signals"):
            self.assertIn(heading, text)
        self.assertTrue(text.rstrip().endswith(f"> {tg.GUARD}"))
        images = text.split("## Open these images", 1)[1].split(">", 1)[0]
        self.assertEqual(images.count("- `"), 3)
        self.assertIn("- Tone: dry wit (2)", text)

    def test_render_respects_word_budget_and_is_deterministic(self):
        pack = fixture_pack(do_items=12)
        text = tg.render_pack(pack)
        self.assertLessEqual(len(text.split()), 900)
        self.assertEqual(text, tg.render_pack(pack))

    def test_render_empty_graph(self):
        text = tg.render_pack({"brief": "x", "kinds": [], "matched": 0, "do": [], "dont": [], "study": [],
                               "signals": {}, "images": []})
        self.assertIn("No curated principles yet.", text)
        self.assertIn(tg.GUARD, text)


def _postgres_available() -> str | None:
    try:
        import psycopg
        from psycopg.conninfo import make_conninfo
    except ImportError:
        return None
    try:
        psycopg.connect(make_conninfo(tg.dsn(), dbname="postgres"), connect_timeout=3).close()
    except psycopg.OperationalError:
        return None
    return make_conninfo(tg.dsn(), dbname=f"taste_graph_test_{os.getpid()}")


TEST_DSN = _postgres_available()


def fake_capture(url, method, full_page=False):
    if "fail" in url:
        raise tg.TasteError("simulated capture failure")
    return tg.Capture(title=f"Page {url[-6:]}", content="captured headline", media=[(PNG, "desktop", ".png")],
                      props={"headline": "captured headline"})


@unittest.skipUnless(TEST_DSN, "psycopg or PostgreSQL unavailable")
class DatabaseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.home = Path(cls.tmp.name) / "home"
        cls.env = mock.patch.dict(os.environ, {"TASTE_GRAPH_HOME": str(cls.home), "TASTE_GRAPH_DSN": TEST_DSN})
        cls.env.start()
        tg.ensure_database(TEST_DSN)
        cls.conn = tg.connect(TEST_DSN)
        tg.migrate(cls.conn)
        tg.load_seed(cls.conn)

    @classmethod
    def tearDownClass(cls):
        import psycopg
        from psycopg import sql
        from psycopg.conninfo import conninfo_to_dict, make_conninfo
        cls.conn.close()
        with psycopg.connect(make_conninfo(TEST_DSN, dbname="postgres"), autocommit=True) as admin:
            for name in (conninfo_to_dict(TEST_DSN)["dbname"], conninfo_to_dict(TEST_DSN)["dbname"] + "_restore"):
                admin.execute(sql.SQL("DROP DATABASE IF EXISTS {} WITH (FORCE)").format(sql.Identifier(name)))
        cls.env.stop()
        cls.tmp.cleanup()

    def test_01_init_is_idempotent(self):
        before = tg.counts(self.conn)
        self.assertEqual(tg.migrate(self.conn), [])
        self.assertEqual(tg.load_seed(self.conn), {"nodes": 0, "edges": 0})
        self.assertEqual(tg.counts(self.conn), before)
        self.assertGreaterEqual(before["nodes"]["principle"], 8)

    def test_02_add_file_capture_links_and_media(self):
        shot = Path(self.tmp.name) / "shot.png"
        shot.write_bytes(PNG)
        home = tg.data_home()
        node, created = tg.add_reference(
            self.conn, home, files=[str(shot)], title="Studio hero study", kind="landing_page", verdict="exemplar",
            why="Oversized serif headline carries the whole hero; one idea, lots of space.", tags=["hero", "serif"],
            patterns=["Oversized serif hero", "principle:Type-led design"], tone="confident", score=5,
            status="curated", by="founder")
        self.assertTrue(created)
        stored = home / node["media"][0]["path"]
        self.assertTrue(stored.exists())
        self.assertRegex(stored.name, r"^[0-9a-f-]{36}-file1\.png$")
        self.assertEqual(node["media"][0]["sha256"], __import__("hashlib").sha256(PNG).hexdigest())
        rels = {(r["rel"], r["type"], r["slug"]) for r in self.conn.execute(
            "SELECT e.rel, n.type, n.slug FROM edge e JOIN node n ON n.id = e.dst WHERE e.src = %s", (node["id"],))}
        self.assertIn(("exemplifies", "pattern", "oversized-serif-hero"), rels)
        self.assertIn(("exemplifies", "principle", "type-led-design"), rels)
        self.assertIn(("has_tone", "tone", "confident"), rels)

    def test_03_governance_and_url_dedupe(self):
        home = tg.data_home()
        with self.assertRaises(tg.TasteError):
            tg.add_reference(self.conn, home, url="https://example.org/a", status="curated", by="agent",
                             capture_fn=fake_capture)
        first, created = tg.add_reference(self.conn, home, url="https://www.example.org/page/?utm_source=x",
                                          why="first", capture_fn=fake_capture)
        again, created_again = tg.add_reference(self.conn, home, url="https://example.org/page#hero", why="second",
                                                tags=["extra"], capture_fn=fake_capture)
        self.assertTrue(created)
        self.assertFalse(created_again)
        self.assertEqual(first["id"], again["id"])
        self.assertEqual((again["body"], again["status"], again["captured_by"]), ("first", "inbox", "agent"))
        self.assertTrue(again["props"]["notes"][-1].endswith(": second"))
        self.assertEqual(len(again["media"]), 1, "existing media is not recaptured")
        curated = tg.find_node(self.conn, "asset:bunq-labs")
        updated, _ = tg.add_reference(self.conn, home, url="https://bunqlabs.com", why="agent opinion", verdict="anti_pattern",
                                      capture_fn=fake_capture)
        self.assertEqual((updated["body"], updated["verdict"], updated["status"]),
                         (curated["body"], curated["verdict"], "curated"), "agents never overwrite curated analysis")
        self.assertRegex(updated["props"]["notes"][-1], r"^agent \d{4}-\d{2}-\d{2}: agent opinion$")

    def test_04_link_and_ingest(self):
        tg.link(self.conn, tg.find_node(self.conn, "asset:studio-hero-study")["id"], "for",
                tg.ensure_node(self.conn, "audience:Founders", "audience")["id"])
        with self.assertRaises(tg.TasteError):
            tg.link(self.conn, 1, "likes", 2)
        inbox = Path(self.tmp.name) / "inbox.md"
        inbox.write_text("# Taste inbox\n\nhttps://ingest.example/one | strong hero | landing page\n"
                         "https://ingest.example/fail | broken\nhttps://ingest.example/two\n", encoding="utf-8")
        result = tg.ingest(self.conn, tg.data_home(), inbox, capture_fn=fake_capture, today=dt.date(2026, 10, 23))
        self.assertEqual(result, {"captured": 2, "failed": 1})
        text = inbox.read_text(encoding="utf-8")
        top, _, processed = text.partition("## Processed 2026-10-23")
        self.assertIn("https://ingest.example/fail | broken # error 2026-10-23: simulated capture failure", top)
        self.assertNotIn("ingest.example/one", top)
        self.assertIn("- https://ingest.example/one | strong hero | landing page → #", processed)
        one = tg.find_node(self.conn, "https://ingest.example/one")
        self.assertEqual((one["status"], one["kind"], one["body"]), ("inbox", "landing_page", "strong hero"))
        # A second run processes nothing new and keeps the failure in place.
        tg.ingest(self.conn, tg.data_home(), inbox, capture_fn=fake_capture, today=dt.date(2026, 10, 23))
        self.assertEqual(inbox.read_text(encoding="utf-8").count("ingest.example/one"), 1)

    def test_05_pack_do_dont_and_usage(self):
        home = tg.data_home()
        bad = Path(self.tmp.name) / "bad.png"
        bad.write_bytes(PNG + b"bad")
        tg.add_reference(self.conn, home, files=[str(bad)], title="Template hero with gradient blob",
                         kind="landing_page", verdict="anti_pattern", why="Gradient blob and three cards: says nothing.",
                         patterns=["pattern:Random gradient soup"], violates=["Fewer, stronger decisions"],
                         status="curated", by="founder")
        brief = "landing page hero for a design-engineering studio"
        pack = tg.build_pack(self.conn, home, brief)
        self.assertEqual(pack, tg.build_pack(self.conn, home, brief), "pack is deterministic")
        do_titles = [item["title"] for item in pack["do"]]
        self.assertIn("Oversized serif hero", do_titles)
        hero = next(i for i in pack["do"] if i["title"] == "Oversized serif hero")
        self.assertEqual(hero["exemplars"][0]["title"], "Studio hero study")
        dont_titles = [item["title"] for item in pack["dont"]]
        self.assertIn("Random gradient soup", dont_titles)
        self.assertIn("Ignoring “Fewer, stronger decisions”", dont_titles)
        self.assertNotIn("Page ple/one", str(pack), "inbox items stay out unless included")
        self.assertIn(("confident", 1), pack["signals"]["tone"])
        self.assertLessEqual(len(pack["images"]), 3)
        text = tg.render_pack(pack)
        self.assertLessEqual(len(text.split()), 900)
        self.assertIn(tg.GUARD, text)
        self.assertTrue(tg.build_pack(self.conn, home, brief, include_inbox=True)["matched"] >= pack["matched"])
        used = tg.record_usage(self.conn, pack, "demo-project")
        project = tg.find_node(self.conn, "project:demo-project")
        n = self.conn.execute("SELECT count(*) AS n FROM edge WHERE rel = 'used_in' AND dst = %s", (project["id"],)).fetchone()["n"]
        self.assertEqual(n, used)

    def test_06_backup_and_restore(self):
        try:
            pg_restore = tg.pg_bin("pg_restore")
            tg.pg_bin("pg_dump")
        except tg.TasteError:
            self.skipTest("pg_dump/pg_restore unavailable")
        import psycopg
        from psycopg.conninfo import make_conninfo, conninfo_to_dict
        target = tg.backup(tg.data_home(), keep=2, conninfo=TEST_DSN)
        self.assertTrue(target.exists())
        restore_dsn = make_conninfo(TEST_DSN, dbname=conninfo_to_dict(TEST_DSN)["dbname"] + "_restore")
        tg.ensure_database(restore_dsn)
        subprocess.run([pg_restore, "--no-owner", f"--dbname={restore_dsn}", str(target)], check=True,
                       capture_output=True)
        with psycopg.connect(restore_dsn, row_factory=__import__("psycopg.rows").rows.dict_row) as restored:
            self.assertEqual(tg.counts(restored), tg.counts(self.conn))


if __name__ == "__main__":
    unittest.main()
