from __future__ import annotations

import io
import json
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from test_cards import CardFixture
from scripts.build_handbook import build_handbook, main as handbook_main
from scripts.oscheck.cards import check_handbook
from scripts.oscheck.frontmatter import check_frontmatter
from scripts.oscheck.links import check_links


class BuildHandbookTests(CardFixture):
    def test_index_has_all_active_tools_canonical_ids_and_pending_nulls(self):
        self.card(identity='old:lead')
        outputs = build_handbook(self.root)
        rows = json.loads(outputs['toolkit/cards/index.json'])['tools']
        self.assertEqual([r['id'] for r in rows], ['skill:lead', 'skill:expert'])
        self.assertEqual(rows[0], dict(id='skill:lead', department='design', sub_department='direction',
            job='art-direction', role='lead', trigger='', invoke='demo skill', availability='both',
            distribution='vendor', card='toolkit/cards/design/direction/old--lead.md',
            summary='A studio tool for a precise job.'))
        self.assertIsNone(rows[1]['card'])
        self.assertIsNone(rows[1]['invoke'])
        self.assertIsNone(rows[1]['availability'])
        self.assertEqual(rows[1]['distribution'], 'vendor')
        self.assertEqual(rows[1]['summary'], 'Card pending.')

    def test_handbook_groups_jobs_and_includes_links_triggers_library_reasons_and_coverage(self):
        self.card()
        self.card(1)
        outputs = build_handbook(self.root)
        design = outputs['handbook/design.md']
        self.assertIn('## Direction', design)
        self.assertIn('### Art direction', design)
        self.assertIn('../toolkit/cards/design/direction/skill--lead.md', design)
        self.assertIn('A studio tool for a precise job.', design)
        self.assertIn('Overlaps \\| lead.', design)
        self.assertIn('Needs review.', design)
        self.assertIn('A release needs checking.', outputs['handbook/engineering.md'])
        self.assertIn('100.0%', outputs['handbook/README.md'])
        self.assertIn('read only', outputs['handbook/README.md'].lower())

    def test_pending_cards_and_missing_lead_are_visible(self):
        outputs = build_handbook(self.root)
        self.assertIn('card pending', outputs['handbook/design.md'])
        self.assertIn('No lead is assigned', outputs['handbook/engineering.md'])
        self.assertIn('0.0%', outputs['handbook/README.md'])

    def test_generation_is_deterministic_across_registry_order_and_multiline_summary(self):
        self.card(body='A precise tool\nfor studio work. Extra sentence.\n')
        first = build_handbook(self.root)
        self.put('toolkit/sources/registry.json', json.dumps({'tools': list(reversed(self.tools))}))
        self.assertEqual(first, build_handbook(self.root))
        self.assertEqual(json.loads(first['toolkit/cards/index.json'])['tools'][0]['summary'], 'A precise tool for studio work.')

    def test_generated_markdown_has_valid_metadata_and_local_links(self):
        self.card()
        for name, text in build_handbook(self.root).items():
            self.put(name, text)
        for name in ("docs/tool-cards.md", "studio/departments/design.md", "studio/departments/engineering.md"):
            self.put(name, "---\ntitle: Guide\ntype: guide\nstatus: proposed\nowner: founder\nlast_reviewed: 2026-10-23\n---\n\n# Guide\n")
        issues = check_frontmatter(self.root, self.config) + check_links(self.root, self.config)
        self.assertEqual([i.render() for i in issues], [])

    def test_cli_writes_then_check_detects_changed_missing_and_obsolete_outputs(self):
        self.card()
        with patch('scripts.build_handbook.ROOT', self.root), redirect_stdout(io.StringIO()):
            self.assertEqual(handbook_main(['--check']), 1)
            self.assertEqual(handbook_main([]), 0)
            self.assertEqual(handbook_main(['--check']), 0)
            self.assertEqual(check_handbook(self.root, self.config), [])
            self.card(body='A changed summary.\n')
            self.assertEqual(handbook_main(['--check']), 1)
            self.assertTrue(check_handbook(self.root, self.config))
            self.assertEqual(handbook_main([]), 0)
            (self.root / 'handbook/design.md').unlink()
            self.assertEqual(handbook_main(['--check']), 1)
            self.assertEqual(handbook_main([]), 0)
            self.put('handbook/obsolete.md', 'Stale output.\n')
            self.assertEqual(handbook_main(['--check']), 1)
            self.assertEqual(handbook_main([]), 0)
            self.assertFalse((self.root / 'handbook/obsolete.md').exists())

    def test_invalid_card_prevents_generation_with_readable_error(self):
        self.card(changes={'job': 'wrong'})
        with patch('scripts.build_handbook.ROOT', self.root), redirect_stdout(io.StringIO()) as out:
            self.assertEqual(handbook_main([]), 1)
        self.assertIn('registry value', out.getvalue())
        self.assertFalse((self.root / 'handbook').exists())


if __name__ == '__main__':
    unittest.main()
