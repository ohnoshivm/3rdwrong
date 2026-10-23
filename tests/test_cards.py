from __future__ import annotations

import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.oscheck.cards import check_cards
from scripts.validate import main as validate_main


SECTIONS = [
    'What it does', 'When to use', 'When not to use', 'Inputs it needs',
    'How to run it', 'What good output looks like', 'Quality checks',
    'Pairs with', 'Limits and cautions',
]


class CardFixture(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.tools = [
            dict(id='skill:lead', aliases=['old:lead'], department='design',
                 sub_department='direction', job='art-direction', role='lead',
                 trigger='', kind='skill', load='active', reason='Owns the job.'),
            dict(id='skill:expert', aliases=[], department='engineering',
                 sub_department='quality', job='testing', role='specialist',
                 trigger='A release needs checking.', kind='skill', load='active', reason='Checks releases.'),
            dict(id='skill:bench', aliases=[], department='design',
                 sub_department='direction', job='art-direction', role='bench',
                 trigger='', kind='skill', load='library', reason='Overlaps | lead.'),
            dict(id='skill:parked', aliases=[], department='design',
                 sub_department='direction', job='art-direction', role='parked',
                 trigger='', kind='skill', load='library', reason='Needs review.'),
        ]
        self.put('toolkit/sources/registry.json', json.dumps({'tools': self.tools}))
        self.put('toolkit/sources/materials.json', json.dumps({
            t['id']: {'distribution': 'vendor', 'source': 'toolkit/vendor/demo'} for t in self.tools
        }))
        self.config = json.loads((Path(__file__).resolve().parents[1] / 'schemas/metadata.json').read_text())

    def put(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding='utf-8')
        return path

    def card(self, index=0, *, identity=None, changes=None, sections=None, body=None, path=None):
        tool = self.tools[index]
        identity = identity or tool['id']
        data = dict(title='Demo tool', type='tool-card', status='proposed', owner='founder',
                    last_reviewed='2026-10-23', tool_id=identity,
                    department=tool['department'], sub_department=tool['sub_department'],
                    job=tool['job'], role=tool['role'], trigger=tool['trigger'], kind='skill',
                    availability='both', distribution='vendor', source='toolkit/vendor/demo',
                    invoke='demo skill', pairs_with=['old:lead'])
        data.update(changes or {})
        slug = identity.lower().replace(':', '--')
        path = path or f"toolkit/cards/{tool['department']}/{tool['sub_department']}/{slug}.md"
        text = '---\n' + yaml.safe_dump(data, sort_keys=False) + '---\n\n# Demo tool\n\n'
        text += body or 'A studio tool for a precise job. Another sentence is excluded.\n'
        text += ''.join(f'\n## {section}\n\nDocumented instructions.\n' for section in (sections or SECTIONS))
        return self.put(path, text)

    def errors(self):
        return [i for i in check_cards(self.root, self.config) if i.severity == 'error']


class CardsTests(CardFixture):
    def test_valid_card_and_alias_pair_are_accepted(self):
        self.card()
        self.assertEqual(self.errors(), [])

    def test_alias_card_covers_canonical_tool(self):
        self.card(identity='old:lead')
        issues = check_cards(self.root, self.config)
        self.assertFalse(any('design:' in i.message for i in issues))
        self.assertEqual(self.errors(), [])

    def test_unknown_tool_and_pair_are_errors(self):
        self.card(identity='skill:missing', changes={'pairs_with': ['missing:id']})
        messages = ' '.join(i.message for i in self.errors())
        self.assertIn('unknown tool_id', messages)
        self.assertIn('missing:id', messages)

    def test_registry_mismatches_include_registry_values(self):
        self.card(changes={k: 'wrong' for k in ('department', 'sub_department', 'job', 'role')})
        messages = ' '.join(i.message for i in self.errors())
        for value in ('design', 'direction', 'art-direction', 'lead'):
            self.assertIn(f"registry value is '{value}'", messages)

    def test_missing_and_malformed_frontmatter_fields_are_errors(self):
        path = self.card()
        path.write_text(path.read_text().replace('invoke: demo skill\n', '').replace('pairs_with:\n- old:lead', 'pairs_with: old:lead'))
        messages = ' '.join(i.message for i in self.errors())
        self.assertIn('invoke', messages)
        self.assertIn('pairs_with', messages)
        self.assertIn('list', messages)

    def test_invalid_metadata_is_reported_by_cards_check_alone(self):
        self.card(changes={'type': 'guide', 'last_reviewed': 'yesterday', 'status': 'imaginary', 'availability': ['both']})
        messages = ' '.join(i.message for i in self.errors())
        for value in ('tool-card', 'last_reviewed', 'status', 'availability'):
            self.assertIn(value, messages)

    def test_empty_lead_trigger_is_valid_but_specialist_requires_trigger(self):
        self.card()
        self.card(1, changes={'trigger': ''})
        self.assertTrue(any('trigger' in i.message for i in self.errors()))

    def test_wrong_path_and_slug_are_errors(self):
        self.card(path='toolkit/cards/design/wrong/Lead.md')
        self.assertTrue(any('toolkit/cards/design/direction/skill--lead.md' in i.message for i in self.errors()))

    def test_slug_replaces_punctuation_and_lowercases(self):
        self.tools[0]['id'] = 'Skill:Odd_Name.X'
        self.put('toolkit/sources/registry.json', json.dumps({'tools': self.tools}))
        self.card(path='toolkit/cards/design/direction/skill--odd-name-x.md')
        self.assertEqual(self.errors(), [])

    def test_required_sections_must_appear_once_and_in_order(self):
        for sections in (SECTIONS[1:], list(reversed(SECTIONS)), SECTIONS + [SECTIONS[0]]):
            with self.subTest(sections=sections):
                self.card(sections=sections)
                self.assertTrue(any('sections' in i.message for i in self.errors()))

    def test_headings_in_code_fences_do_not_count(self):
        self.card(body='A useful tool.\n\n```text\n# Example H1\n## When to use\n```\n')
        self.assertEqual(self.errors(), [])
        self.card(body='# Extra title\n')
        self.assertTrue(any('exactly one H1' in i.message for i in self.errors()))

    def test_over_90_lines_is_only_a_warning(self):
        self.card(body='A useful tool.\n' + '\n' * 91)
        self.assertEqual(self.errors(), [])
        self.assertTrue(any('90 lines' in i.message and i.severity == 'warning' for i in check_cards(self.root, self.config)))

    def test_bench_and_parked_cards_are_errors(self):
        self.card(2)
        self.card(3)
        messages = ' '.join(i.message for i in self.errors())
        self.assertIn('bench', messages)
        self.assertIn('parked', messages)

    def test_duplicate_alias_and_canonical_cards_are_errors(self):
        self.card()
        self.card(identity='old:lead')
        self.assertTrue(any('duplicate card' in i.message for i in self.errors()))

    def test_missing_cards_warn_once_per_department_and_strict_setting_errors(self):
        issues = check_cards(self.root, self.config)
        self.assertEqual(len(issues), 2)
        self.assertTrue(all(i.severity == 'warning' for i in issues))
        self.config['cards'] = {'strict_departments': ['design']}
        issues = check_cards(self.root, self.config)
        self.assertEqual(sum(i.severity == 'error' for i in issues), 1)
        self.assertTrue(any('skill:lead' in i.message for i in issues if i.severity == 'error'))

    def test_cli_strict_cards_flag_promotes_coverage(self):
        self.put('schemas/metadata.json', json.dumps(self.config))
        with patch('scripts.validate.ROOT', self.root), redirect_stdout(io.StringIO()):
            self.assertEqual(validate_main(['--check', 'cards']), 0)
            self.assertEqual(validate_main(['--check', 'cards', '--strict-cards']), 1)

    def test_malformed_yaml_is_an_issue_not_a_crash(self):
        self.put('toolkit/cards/design/direction/broken.md', '---\ntitle: [\n---\n')
        self.assertTrue(any('invalid YAML' in i.message for i in self.errors()))

    def test_registry_rejects_ambiguous_aliases_and_unsafe_output_paths(self):
        self.tools[1]['aliases'] = ['old:lead']
        self.put('toolkit/sources/registry.json', json.dumps({'tools': self.tools}))
        self.assertTrue(any('ambiguous registry alias' in i.message for i in self.errors()))
        self.tools[1]['aliases'] = []
        self.tools[0]['department'] = '../../outside'
        self.put('toolkit/sources/registry.json', json.dumps({'tools': self.tools}))
        self.assertTrue(any('department must be a slug' in i.message for i in self.errors()))

    def test_missing_registry_is_an_issue(self):
        (self.root / 'toolkit/sources/registry.json').unlink()
        self.assertTrue(any('registry' in i.message for i in self.errors()))


if __name__ == '__main__':
    unittest.main()
