from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from scripts.validate import CHECKS
from scripts.oscheck import agents as agents_module


class AgentsCheckTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.directory = self.root / '.claude' / 'agents'
        self.directory.mkdir(parents=True)
        self.agent = self.directory / 'example.md'
        self.agent.write_text('# Original upstream agent\n', encoding='utf-8')
        self.lock_path = self.root / 'agents' / 'agency-agents.lock.json'
        self.lock_path.parent.mkdir()
        self.exclusions = self.root / 'agents' / 'exclusions.txt'
        self.exclusions.write_text('division:support  # unrelated support roles\n', encoding='utf-8')
        self.lock = {
            'upstream': 'https://github.com/msitarzewski/agency-agents',
            'commit': 'a' * 40,
            'date': '2026-10-22',
            'licence': 'MIT',
            'install_method': 'upstream Claude Code installer (identity format)',
            'install_command': 'bash scripts/install.sh --tool claude-code --no-interactive --path <repo>/.claude/agents',
            'agent_count': 1,
            'included_count': 1,
            'excluded_count': 1,
            'upstream_agent_count': 2,
            'exclusions_sha256': hashlib.sha256(self.exclusions.read_bytes()).hexdigest(),
            'catalogue': {'example': 'design', 'excluded-example': 'support'},
            'division_counts': {'design': 1},
            'files': {'.claude/agents/example.md': hashlib.sha256(self.agent.read_bytes()).hexdigest()},
        }
        self.write_lock()

    def write_lock(self) -> None:
        self.lock_path.write_text(json.dumps(self.lock), encoding='utf-8')

    def check(self):
        self.assertIn('agents', CHECKS, 'the default validator must check the agent lock')
        return CHECKS['agents'](self.root, {})

    def test_exclusions_parse_comments_and_specific_agents(self) -> None:
        self.assertTrue(hasattr(agents_module, 'parse_exclusions'), 'exclusions must have a shared strict parser')
        parsed = agents_module.parse_exclusions('# Founder exclusions\n\ndivision:support  # unrelated\nagent:example  # weakest fit\n')
        self.assertEqual(parsed, [('division', 'support'), ('agent', 'example')])

    def test_exclusions_reject_invalid_missing_reason_duplicate_and_unknown_entries(self) -> None:
        self.assertTrue(hasattr(agents_module, 'parse_exclusions'), 'exclusions must have a shared strict parser')
        for text in ('support', 'division:support', 'agent:../escape  # unsafe',
                     'agent:example  # reason\nagent:example  # duplicate'):
            with self.subTest(text=text), self.assertRaises(ValueError):
                agents_module.parse_exclusions(text)
        self.exclusions.write_text('agent:unknown  # typo\n')
        self.lock['exclusions_sha256'] = hashlib.sha256(self.exclusions.read_bytes()).hexdigest()
        self.write_lock()
        self.assertTrue(any('unknown' in issue.message for issue in self.check()))

    def test_changed_exclusions_require_regeneration(self) -> None:
        self.exclusions.write_text('agent:example  # new founder choice\n')
        self.assertTrue(any('exclusions' in issue.message for issue in self.check()))

    def test_excluded_agent_present_is_rejected_even_if_added_to_lock(self) -> None:
        excluded = self.directory / 'excluded-example.md'
        excluded.write_text('# Excluded\n')
        self.lock['files']['.claude/agents/excluded-example.md'] = hashlib.sha256(excluded.read_bytes()).hexdigest()
        self.lock['agent_count'] = 2
        self.write_lock()
        self.assertTrue(any('excluded' in issue.message for issue in self.check()))

    def test_matching_catalogue_passes(self) -> None:
        self.assertEqual(self.check(), [])

    def test_tampering_is_rejected(self) -> None:
        self.agent.write_text('# Changed persona\n', encoding='utf-8')
        self.assertTrue(any('hash' in issue.message for issue in self.check()))

    def test_missing_and_unlisted_files_are_rejected(self) -> None:
        self.agent.unlink()
        extra = self.directory / 'unlisted.txt'
        extra.write_text('Unexpected file\n', encoding='utf-8')
        issues = self.check()
        self.assertTrue(any(issue.path.endswith('example.md') and 'missing' in issue.message for issue in issues))
        self.assertTrue(any(issue.path.endswith('unlisted.txt') and 'unlisted' in issue.message for issue in issues))

    def test_count_mismatch_is_rejected(self) -> None:
        self.lock['agent_count'] = 2
        self.write_lock()
        self.assertTrue(any('count' in issue.message for issue in self.check()))

    def test_invalid_or_missing_lock_returns_issues(self) -> None:
        for contents in ('{', '[]', '{}'):
            with self.subTest(contents=contents):
                self.lock_path.write_text(contents, encoding='utf-8')
                self.assertTrue(self.check())
        self.lock_path.unlink()
        self.assertTrue(self.check())

    def test_lock_rejects_unsafe_paths_and_invalid_hashes(self) -> None:
        self.lock['files'] = {'../outside.md': 'not-a-hash'}
        self.write_lock()
        issues = self.check()
        self.assertTrue(any('path' in issue.message for issue in issues))
        self.assertTrue(any('sha256' in issue.message for issue in issues))

    def test_symlink_agent_is_rejected_even_when_bytes_match(self) -> None:
        target = self.root / 'outside.md'
        target.write_bytes(self.agent.read_bytes())
        self.agent.unlink()
        self.agent.symlink_to(target)
        self.assertTrue(any('symlink' in issue.message for issue in self.check()))


if __name__ == '__main__':
    unittest.main()
