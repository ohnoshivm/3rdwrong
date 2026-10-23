"""Installer contracts: conflict preservation, loading isolation, and owned cleanup."""
from __future__ import annotations
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
INSTALL = ROOT / 'scripts/toolkit_install.py'


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name)
        self.repo = self.base / 'repo'
        self.home = self.base / 'home'
        (self.repo / 'toolkit').mkdir(parents=True)
        self.home.mkdir()
        for name in ('active', 'bench'):
            p = self.repo / 'toolkit/vendor/demo/skills' / name
            p.mkdir(parents=True)
            (p / 'SKILL.md').write_text('---\nname: '+name+'\ndescription: Test\n---\n')
        self.plan = {'schema_version': 1, 'items': [
            {'id': 'skill:active', 'name': '3w-active', 'kind': 'skill', 'source': 'toolkit/vendor/demo/skills/active', 'package': 'demo', 'distribution': 'vendor', 'department': 'design', 'role': 'lead'},
            {'id': 'skill:bench', 'name': '3w-bench', 'kind': 'skill', 'source': 'toolkit/vendor/demo/skills/bench', 'package': 'demo', 'distribution': 'vendor', 'department': 'design', 'role': 'bench'}],
            'fetch': [], 'templates': {}, 'manual': []}
        self.write_plan()

    def write_plan(self):
        (self.repo / 'toolkit/install-plan.json').write_text(json.dumps(self.plan))

    def run_install(self, *args):
        env = dict(os.environ, HOME=str(self.home), PYTHONDONTWRITEBYTECODE='1')
        return subprocess.run([sys.executable, str(INSTALL), '--repo', str(self.repo), *args], env=env, text=True, capture_output=True)

    def test_active_and_bench_have_separate_discovery_paths(self):
        result = self.run_install('--tools', 'both')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue((self.home / '.claude/skills/3w-active').is_symlink())
        self.assertTrue((self.home / '.agents/skills/3w-active').is_symlink())
        self.assertTrue((self.home / '.claude/skills-library/3rdwrong/skills/3w-bench').is_symlink())
        self.assertFalse((self.home / '.claude/skills/3w-bench').exists())
        self.assertEqual(self.run_install('--tools', 'both').returncode, 0)
        self.assertEqual(len(list((self.home / '.claude/skills').iterdir())), 1)

    def test_conflict_survives_install_and_uninstall(self):
        conflict = self.home / '.claude/skills/3w-active'
        conflict.mkdir(parents=True)
        (conflict / 'mine').write_text('keep')
        result = self.run_install('--tools', 'both')
        self.assertIn('CONFLICT', result.stdout)
        self.assertEqual((conflict / 'mine').read_text(), 'keep')
        self.assertEqual(self.run_install('--uninstall').returncode, 0)
        self.assertEqual((conflict / 'mine').read_text(), 'keep')
        self.assertFalse((self.home / '.agents/skills/3w-active').exists())

    def test_dry_run_does_not_create_home_content(self):
        self.assertEqual(self.run_install('--dry-run').returncode, 0)
        self.assertEqual(list(self.home.iterdir()), [])

    def test_parent_symlink_cannot_redirect_writes_outside_home(self):
        outside = self.base / 'outside'
        outside.mkdir()
        (self.home / '.claude').symlink_to(outside, target_is_directory=True)
        result = self.run_install()
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(list(outside.iterdir()), [])

    def test_profile_filters_and_rejects_traversal_source(self):
        self.assertEqual(self.run_install('--profile', 'growth').returncode, 0)
        self.assertFalse((self.home / '.claude/skills/3w-active').exists())
        self.plan['items'][0]['source'] = '../../outside'
        self.write_plan()
        self.assertNotEqual(self.run_install().returncode, 0)

    def test_uninstall_preserves_user_replacement_and_modified_template(self):
        self.plan['templates'] = {'example.json': {'mcpServers': {}}}
        self.write_plan()
        self.assertEqual(self.run_install().returncode, 0)
        active = self.home / '.claude/skills/3w-active'
        active.unlink()
        active.mkdir()
        template = self.home / '.3rdwrong/mcp-templates/example.json'
        template.write_text('mine')
        self.assertEqual(self.run_install('--uninstall').returncode, 0)
        self.assertTrue(active.is_dir())
        self.assertEqual(template.read_text(), 'mine')

    def test_uninstall_restores_home_except_preexisting_folders(self):
        mine = self.home / '.claude/skills/mine'
        mine.mkdir(parents=True)
        self.plan['templates'] = {'example.json': {'mcpServers': {}}}
        self.write_plan()
        self.assertEqual(self.run_install('--tools', 'both').returncode, 0)
        self.assertEqual(self.run_install('--uninstall').returncode, 0)
        remaining = sorted(p.relative_to(self.home).as_posix() for p in self.home.rglob('*'))
        self.assertEqual(remaining, ['.claude', '.claude/skills', '.claude/skills/mine'])

    def test_skip_fetch_reports_without_network(self):
        self.plan['fetch'] = [{'id': 'pkg', 'commit': '0' * 40, 'upstream_url': 'https://github.com/example/pkg', 'component_only': False}]
        self.plan['items'].append({'id': 'skill:remote', 'name': '3w-remote', 'kind': 'skill', 'package': 'pkg', 'distribution': 'fetch', 'department': 'design', 'role': 'lead'})
        self.write_plan()
        result = self.run_install('--skip-fetch')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('SKIP FETCH pkg', result.stdout)
        self.assertFalse((self.home / '.3rdwrong/fetch').exists())
        self.assertFalse((self.home / '.claude/skills/3w-remote').exists())


if __name__ == '__main__':
    unittest.main()
