"""Snapshot generation must detect drift and preserve plugin containment."""
from __future__ import annotations
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / 'scripts/toolkit_build.py'


class BuildTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.repo = Path(self.tmp.name)
        (self.repo / 'toolkit/sources').mkdir(parents=True)
        p = self.repo / 'toolkit/vendor/demo/skills/hello'
        p.mkdir(parents=True)
        (p / 'SKILL.md').write_text('---\nname: hello\ndescription: Hello\n---\n# Hello\n')
        import hashlib
        digest = hashlib.sha256((p / 'SKILL.md').read_bytes()).hexdigest()
        import yaml
        (p.parent.parent / 'PROVENANCE.yaml').write_text(yaml.safe_dump({'package': 'demo', 'licence': 'MIT', 'files': {'skills/hello/SKILL.md': {'sha256': digest}}, 'notices': []}))
        package = {'id': 'demo', 'class': 'VENDOR', 'licence': 'MIT', 'upstream_url': 'https://example.com/demo', 'tool_ids': ['skill:hello'], 'tool_count': 1, 'notices': [], 'reason': 'permissive'}
        (self.repo / 'toolkit/sources/packages.json').write_text(json.dumps({'packages': [package]}))
        (self.repo / 'toolkit/sources/materials.json').write_text(json.dumps({'skill:hello': {'package': 'demo', 'source': 'toolkit/vendor/demo/skills/hello', 'kind': 'skill'}}))
        (self.repo / 'toolkit/sources/registry.json').write_text(json.dumps({'tools': [{'id': 'skill:hello', 'aliases': ['skill:hello'], 'department': 'design', 'role': 'lead'}]}))

    def run_build(self, *args):
        return subprocess.run([sys.executable, str(BUILD), '--repo', str(self.repo), *args], text=True, capture_output=True)

    def test_check_is_read_only_and_detects_tampered_vendor_file(self):
        built = self.run_build()
        self.assertEqual(built.returncode, 0, built.stderr)
        self.assertEqual(self.run_build('--check').returncode, 0)
        lock = self.repo / 'toolkit/toolkit.lock.json'
        before = lock.read_bytes()
        (self.repo / 'toolkit/vendor/demo/skills/hello/SKILL.md').write_text('tampered')
        self.assertNotEqual(self.run_build('--check').returncode, 0)
        self.assertNotEqual(self.run_build().returncode, 0)
        self.assertEqual(lock.read_bytes(), before)

    def test_plugins_contain_real_copies_and_only_active_items(self):
        self.assertEqual(self.run_build().returncode, 0)
        p = self.repo / 'toolkit/plugins/3rdwrong-design/skills/3w-skill-hello/SKILL.md'
        self.assertTrue(p.is_file())
        self.assertFalse(p.is_symlink())
        registry = self.repo / 'toolkit/sources/registry.json'
        d = json.loads(registry.read_text());d['tools'][0]['role'] = 'parked';registry.write_text(json.dumps(d))
        self.assertNotEqual(self.run_build('--check').returncode, 0)
        self.assertEqual(self.run_build().returncode, 0)
        self.assertFalse(p.exists())

    def test_extra_vendor_file_is_not_silently_blessed(self):
        self.assertEqual(self.run_build().returncode, 0)
        (self.repo / 'toolkit/vendor/demo/unreviewed.txt').write_text('unreviewed')
        result = self.run_build()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('unreviewed', result.stdout + result.stderr)

    def test_stale_plugin_directory_is_reported_then_removed(self):
        self.assertEqual(self.run_build().returncode, 0)
        stale = self.repo / 'toolkit/plugins/3rdwrong-business/skills'
        stale.mkdir(parents=True)
        result = self.run_build('--check')
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('3rdwrong-business', result.stdout)
        self.assertEqual(self.run_build().returncode, 0)
        self.assertFalse(stale.parent.exists())
        self.assertEqual(self.run_build('--check').returncode, 0)

    def test_reviewed_line_extends_only_to_identical_plugin_copy(self):
        import hashlib
        entry = {'path': 'toolkit/vendor/demo/skills/hello/SKILL.md', 'line_sha256': hashlib.sha256(b'# Hello').hexdigest(), 'label': 'email address', 'reason': 'test'}
        (self.repo / 'toolkit/sources/secret-allowlist.json').write_text(json.dumps({'entries': [entry]}))
        self.assertEqual(self.run_build().returncode, 0)
        paths = [e['path'] for e in json.loads((self.repo / 'toolkit/secret-allowlist.json').read_text())['entries']]
        self.assertEqual(sorted(paths), ['toolkit/plugins/3rdwrong-design/skills/3w-skill-hello/SKILL.md', entry['path']])
        entry.pop('reason')
        (self.repo / 'toolkit/sources/secret-allowlist.json').write_text(json.dumps({'entries': [entry]}))
        self.assertNotEqual(self.run_build().returncode, 0)

    def test_notice_section_is_generated_between_markers_and_keeps_prefix(self):
        notices = self.repo / 'THIRD_PARTY_NOTICES.md'
        notices.write_text('# Third-party notices\n\n## Agency Agents\n\nKeep me.\n')
        self.assertEqual(self.run_build().returncode, 0)
        text = notices.read_text()
        self.assertTrue(text.startswith('# Third-party notices\n\n## Agency Agents\n\nKeep me.\n'))
        self.assertIn('| `demo` | MIT | <https://example.com/demo> |', text)
        self.assertEqual(self.run_build('--check').returncode, 0)
        notices.write_text(text.replace('MIT', 'GPL'))
        self.assertNotEqual(self.run_build('--check').returncode, 0)


if __name__ == '__main__':
    unittest.main()
