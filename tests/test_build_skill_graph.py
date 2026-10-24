from __future__ import annotations

import json
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.build_skill_graph import GRAPH, build, stale_outputs
from scripts.oscheck.common import markdown_files

WIKILINK = re.compile(r'\[\[([^\]|]+)(?:\|[^\]]*)?\]\]')


def dei_tools() -> list[dict]:
    registry = json.loads((ROOT / 'toolkit/sources/registry.json').read_text(encoding='utf-8'))['tools']
    return [t for t in registry if t['department'] in ('design', 'engineering')]


class BuildSkillGraphTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.notes = build(ROOT)

    def test_note_counts_match_registry(self) -> None:
        tools = dei_tools()
        active = [t for t in tools if t['role'] in ('lead', 'specialist')]
        jobs = {(t['department'], t['job']) for t in tools}
        skill_notes = [p for p in self.notes if p.startswith(f'{GRAPH}/skills/')]
        job_notes = [p for p in self.notes if p.startswith(f'{GRAPH}/jobs/')]
        self.assertEqual(len(skill_notes), len(active))
        self.assertEqual(len(job_notes), len(jobs))
        self.assertEqual(len(self.notes), len(active) + len(jobs) + 4)

    def test_hub_and_department_notes_exist(self) -> None:
        for name in ('README', 'Design', 'Engineering', 'Workflow'):
            self.assertIn(f'{GRAPH}/{name}.md', self.notes)
        hub = self.notes[f'{GRAPH}/README.md']
        self.assertIn('[[skill-graph/Design|Design]]', hub)
        self.assertIn('[[skill-graph/Engineering|Engineering]]', hub)

    def test_frontmatter_is_repo_valid(self) -> None:
        for path, text in self.notes.items():
            with self.subTest(path=path):
                self.assertTrue(text.startswith('---\n'))
                self.assertRegex(text, r'\ntype: (skill|guide)\n')
                self.assertIn('\nstatus: proposed\n', text)
                self.assertIn('\nowner: founder\n', text)
                self.assertRegex(text, r'\nlast_reviewed: \d{4}-\d{2}-\d{2}\n')

    def test_every_wikilink_resolves(self) -> None:
        graph_bases = {Path(p).stem.lower() for p in self.notes}
        vault_bases = {p.stem.lower() for p in markdown_files(ROOT)}
        for path, text in self.notes.items():
            for target in WIKILINK.findall(text):
                with self.subTest(note=path, target=target):
                    if '/' in target:
                        self.assertTrue((ROOT / f'{target}.md').is_file(), target)
                    else:
                        self.assertIn(target.lower(), graph_bases | vault_bases, target)

    def test_build_is_deterministic(self) -> None:
        self.assertEqual(build(ROOT), self.notes)

    def test_committed_graph_is_current(self) -> None:
        self.assertEqual(stale_outputs(ROOT), [])

    def test_extra_note_makes_check_fail(self) -> None:
        extra = ROOT / GRAPH / '_stale-probe.md'
        extra.write_text('---\ntitle: probe\n---\n', encoding='utf-8')
        try:
            issues = stale_outputs(ROOT)
        finally:
            extra.unlink()
        self.assertTrue(any('_stale-probe.md' in issue for issue in issues))

    def test_specialist_clauses_drop_use_when_prefix(self) -> None:
        for path, text in self.notes.items():
            if '/jobs/' in path:
                self.assertNotIn('pick this instead when Use when', text)


if __name__ == '__main__':
    unittest.main()
