"""Round-three public/private and textual-blinding regressions."""
import io
import os
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from scripts.eval_blind import check_blind, sanitise
from scripts.eval_run import main
from tests import test_evals


class BlindingRound3Tests(unittest.TestCase):
    metadata = {'candidates': {'A': {'tool_id': 'skill:3w-identity-system-critic',
                              'registry_snapshot': {'name': 'Identity System Critic'}}}}

    def test_confusable_identity_is_scrubbed_and_raw_clearance_refused(self):
        for identity in ('Identіty System Critic', 'ΙdentitySystemCritic', 'Identitу_System_Critic'):
            with self.subTest(identity=identity):
                with self.assertRaises(ValueError):
                    check_blind(identity, self.metadata)
                self.assertEqual(sanitise(identity, self.metadata), '[identity redacted]\n')

    def test_mixed_script_near_candidate_tokens_refuse_clearance(self):
        content = 'Identitғ Criti҄c and Systeғ are signatures.\n'
        with self.assertRaises(ValueError):
            check_blind(content, self.metadata)
        check_blind(sanitise(content, self.metadata), self.metadata)

    def test_non_latin_prose_and_person_claude_survive(self):
        content = 'Claude is my colleague.\nΚαλημέρα κόσμε. Добрый день. नमस्ते दुनिया.\n'
        self.assertEqual(sanitise(content, self.metadata), content)
        check_blind(content, self.metadata)

    def test_complete_model_signatures_leave_no_suffix(self):
        for signature in ('Gemini 2.5 Pro', 'GPT-4.1', 'GPT-6.1 Sol',
                          'Claude Opus 5.5', 'Haiku 5.5', 'OpenAI GPT-4.1 Sol'):
            with self.subTest(signature=signature):
                self.assertEqual(sanitise(signature, {'candidates': {}}), '[identity redacted]\n')
                with self.assertRaises(ValueError):
                    check_blind(signature, {'candidates': {}})


class PreparationRound3Tests(unittest.TestCase):
    def test_uncommitted_evidence_case_cannot_prepare(self):
        fixture = test_evals.EvalTests()
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        stdout, stderr = io.StringIO(), io.StringIO()
        with redirect_stdout(stdout), redirect_stderr(stderr):
            code = main(['--root', str(fixture.root), 'prepare', str(fixture.case),
                         '--candidates', 'tool:lead', 'tool:other'])
        self.assertEqual(code, 1)
        self.assertIn('committed case', stderr.getvalue())

    def test_project_mode_writes_only_to_override_vault(self):
        fixture = test_evals.EvalTests()
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        with tempfile.TemporaryDirectory() as temp:
            vault = Path(temp).resolve()
            case = vault / 'quiet-harbour/evals/cases/design/concept-critique/sample.yaml'
            case.parent.mkdir(parents=True)
            case.write_bytes(fixture.case.read_bytes())
            (vault / 'quiet-harbour/evals/brief.md').write_text('Private synthetic input.\n')
            stdout, stderr = io.StringIO(), io.StringIO()
            with patch.dict(os.environ, {'THREEW_VAULT': str(vault)}), redirect_stdout(stdout), redirect_stderr(stderr):
                code = main(['--root', str(fixture.root), 'prepare', str(case), '--project', 'quiet-harbour',
                             '--candidates', 'tool:lead', 'tool:other', '--run-id', 'private-test'])
            self.assertEqual(code, 0, stderr.getvalue())
            self.assertTrue(Path(stdout.getvalue().strip()).is_relative_to(vault))
            self.assertFalse((fixture.root / 'evals/runs').exists())


class CaseAuthorityTests(unittest.TestCase):
    def setUp(self):
        self.fixture = test_evals.EvalTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)

    def test_precommit_demo_relabel_move_rehash_and_single_commit_is_refused(self):
        import yaml
        from scripts.eval_core import digest, EvalError
        from scripts.eval_report import build_report
        from scripts.oscheck.evals import check_evals
        fixture = self.fixture
        demo = fixture.prepare(demo=True)
        evidence = fixture.root / 'evals/runs/evidence/concept-critique/evidence-relabeled'
        evidence.parent.mkdir(parents=True)
        demo.rename(evidence)
        for name in ('creation.yaml', 'run.yaml'):
            data = yaml.safe_load((evidence / name).read_text())
            data.update(run_id='evidence-relabeled', demo=False, **{'class': 'evidence'})
            data['score_meaning'] = 'Rubric evidence; human approval remains separate.'
            if name == 'run.yaml':
                data['creation_sha256'] = digest((evidence / 'creation.yaml').read_bytes())
            fixture.write(evidence / name, data)
        (evidence / 'run.sha256').write_text(digest((evidence / 'run.yaml').read_bytes()))
        # First-ever commit of the edited run; the case already existed as demo.
        fixture.commit_fixture()
        result = fixture.cli('score', evidence, '--judge-model', 'claude-opus-4-1',
                             '--scores', fixture.scores(evidence), ok=False)
        self.assertIn('derived case', result.stderr)
        fixture.cli('check-blinding', evidence, '--checker-model', 'claude-opus-4-1', '--notes', 'Checked.', ok=False)
        self.assertTrue(check_evals(fixture.root, {}))
        # Fabricating a result alongside it cannot make the reporter trust it.
        forged = fixture.root / 'evals/results/evidence/concept-critique/evidence-relabeled.yaml'
        forged.parent.mkdir(parents=True)
        forged.write_bytes((evidence / 'run.yaml').read_bytes())
        with self.assertRaises(EvalError):
            build_report(fixture.root)

    def test_case_class_changes_even_if_reverted_or_run_points_at_new_commit_are_refused(self):
        import yaml
        fixture = self.fixture
        run = fixture.prepare(demo=True)
        path = fixture.root / yaml.safe_load((run / 'run.yaml').read_text())['case_path']
        data = yaml.safe_load(path.read_text())
        data['class'] = 'evidence'
        fixture.write(path, data)
        fixture.commit_fixture()
        fixture.cli('score', run, '--judge-model', 'claude-opus-4-1', '--scores', fixture.scores(run), ok=False)
        data['class'] = 'demo'
        fixture.write(path, data)
        fixture.commit_fixture()
        result = fixture.cli('judge-packet', run, ok=False)
        self.assertIn('case class changed', result.stderr)
        fixture.cli('prepare', path, '--demo', '--candidates', 'tool:lead', ok=False)

    def test_uncommitted_inputs_and_case_are_refused_before_any_write(self):
        fixture = self.fixture
        fixture.commit_fixture()
        (fixture.root / 'brief.md').write_text('Uncommitted input.\n')
        fixture.cli('prepare', fixture.case, '--candidates', 'tool:lead', 'tool:other', ok=False)
        self.assertFalse((fixture.root / 'evals/runs').exists())
        (fixture.root / 'brief.md').write_text('Synthetic brief.\n')
        fixture.case.write_text(fixture.case.read_text() + '\n')
        fixture.cli('prepare', fixture.case, '--candidates', 'tool:lead', 'tool:other', ok=False)
        self.assertFalse((fixture.root / 'evals/runs').exists())

    def test_rehashing_input_and_manifests_still_checks_committed_bytes(self):
        import yaml
        from scripts.eval_core import digest
        fixture = self.fixture
        run = fixture.prepare()
        (run / 'inputs/01.txt').write_text('Forged replacement.\n')
        for name in ('creation.yaml', 'run.yaml'):
            data = yaml.safe_load((run / name).read_text())
            data['inputs'][0]['sha256'] = digest((run / 'inputs/01.txt').read_bytes())
            if name == 'run.yaml':
                data['creation_sha256'] = digest((run / 'creation.yaml').read_bytes())
            fixture.write(run / name, data)
        (run / 'run.sha256').write_text(digest((run / 'run.yaml').read_bytes()))
        result = fixture.cli('score', run, '--judge-model', 'claude-opus-4-1', '--scores', fixture.scores(run), ok=False)
        self.assertIn('committed case inputs', result.stderr)

    def test_missing_shallow_unreachable_history_refuses_score_and_leaderboard(self):
        from scripts.eval_core import EvalError
        from scripts.eval_report import build_report
        fixture = self.fixture
        run = fixture.prepare()
        fixture.cli('score', run, '--judge-model', 'claude-opus-4-1', '--scores', fixture.scores(run))
        for failure in ('missing', 'shallow', 'unreachable'):
            def transport(root, *args):
                if failure == 'missing' or (failure == 'unreachable' and args[0] == 'merge-base'):
                    raise EvalError('committed case history unavailable')
                if failure == 'shallow' and args[-1] == '--is-shallow-repository':
                    return b'true'
                return fixture.git_read(root, *args)
            with self.subTest(failure=failure), patch('scripts.eval_provenance.git', side_effect=transport):
                fixture.cli('reveal', run, ok=False)
                with self.assertRaises(EvalError):
                    build_report(fixture.root)

    def test_demo_flag_cannot_downgrade_evidence_case(self):
        fixture = self.fixture
        fixture.cli('prepare', fixture.case, '--demo', '--candidates', 'tool:lead', 'tool:other', ok=False)
        self.assertFalse((fixture.root / 'evals/runs').exists())


class PrivateStorageTests(unittest.TestCase):
    def setUp(self):
        import yaml
        self.fixture = test_evals.EvalTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.vault = Path(self.temp.name).resolve()
        env = patch.dict(os.environ, {'THREEW_VAULT': str(self.vault)})
        env.start()
        self.addCleanup(env.stop)
        self.base = self.vault / 'quiet-harbour/evals'
        self.case = self.base / 'cases/design/concept-critique/sample.yaml'
        self.case.parent.mkdir(parents=True)
        self.case.write_bytes(self.fixture.case.read_bytes())
        (self.base / 'brief.md').write_text('Private synthetic input.\n')
        self.output = self.base / 'maker.txt'
        self.output.write_text('Documented: private synthetic finding.\n')

    def prepare(self, run_id='private-test'):
        return Path(self.fixture.cli('prepare', self.case, '--project', 'quiet-harbour',
                                    '--candidates', 'tool:lead', 'tool:other', '--run-id', run_id).stdout.strip())

    def test_full_private_cycle_scores_bundles_and_append_only_events(self):
        import json
        from scripts.eval_report import build_report
        fixture = self.fixture
        before = {p.relative_to(fixture.root).as_posix(): p.read_bytes()
                  for p in fixture.root.rglob('*') if p.is_file()}
        run = self.prepare()
        events = self.base / 'preparations.jsonl'
        original = events.read_bytes()
        first = json.loads(original)
        self.assertEqual(first['run_id'], 'project-private-test')
        self.assertEqual(first['codename'], 'quiet-harbour')
        self.assertTrue(first['timestamp'])
        self.assertEqual(len(first['case_sha256']), 64)
        bundle = self.base / 'bundle'
        bundle.mkdir()
        (bundle / 'proof.txt').write_text('Private synthetic artefact.\n')
        for slot in ('A', 'B'):
            fixture.cli('record', run, '--slot', slot, '--output', self.output,
                        '--maker-model', 'gpt-4.1', '--artefacts', bundle)
        fixture.cli('check-blinding', run, '--checker-model', 'claude-opus-4-1', '--notes', 'Checked private packet.')
        fixture.cli('score', run, '--judge-model', 'claude-opus-4-1', '--scores', fixture.scores(run))
        fixture.cli('reveal', run)
        self.assertTrue((self.base / 'results/project/concept-critique/project-private-test.yaml').is_file())
        self.assertEqual((run / 'artefacts/A/proof.txt').read_text(), 'Private synthetic artefact.\n')
        self.prepare('second-private')
        self.assertTrue(events.read_bytes().startswith(original))
        self.assertEqual(len(events.read_text().splitlines()), 2)
        report = build_report(fixture.root)
        self.assertNotIn('private-test', report)
        self.assertNotIn('private synthetic', report)
        self.assertEqual(before, {p.relative_to(fixture.root).as_posix(): p.read_bytes()
                                 for p in fixture.root.rglob('*') if p.is_file()})

    def test_in_repo_vault_traversal_case_variant_and_symlink_are_refused(self):
        fixture = self.fixture
        link = self.vault / 'repo-link'
        link.symlink_to(fixture.root, target_is_directory=True)
        for vault in (fixture.root / 'private', fixture.root / 'projects/../private',
                      Path(str(fixture.root).upper()) / 'private', link / 'private'):
            with self.subTest(vault=vault), patch.dict(os.environ, {'THREEW_VAULT': str(vault)}):
                fixture.cli('prepare', self.case, '--project', 'quiet-harbour',
                            '--candidates', 'tool:lead', 'tool:other', ok=False)
        self.assertFalse((fixture.root / 'private').exists())

    def test_nested_private_output_symlink_into_repo_is_refused(self):
        fixture = self.fixture
        run = self.prepare()
        (run / 'slots').symlink_to(fixture.root, target_is_directory=True)
        fixture.cli('record', run, '--slot', 'A', '--output', self.output, '--maker-model', 'gpt-4.1', ok=False)
        self.assertFalse((fixture.root / 'A.txt').exists())

    def test_private_case_inputs_cannot_escape_to_repository(self):
        import yaml
        data = yaml.safe_load(self.case.read_text())
        data['inputs'] = ['public-link.md']
        self.fixture.write(self.case, data)
        (self.base / 'public-link.md').symlink_to(self.fixture.root / 'brief.md')
        self.fixture.cli('prepare', self.case, '--project', 'quiet-harbour',
                         '--candidates', 'tool:lead', 'tool:other', ok=False)
        self.assertFalse((self.base / 'runs').exists())

    def test_private_bundle_symlinks_and_tampered_bundle_are_refused(self):
        fixture = self.fixture
        run = self.prepare()
        bundle = self.base / 'bundle'
        bundle.mkdir()
        (bundle / 'link.txt').symlink_to(fixture.root / 'brief.md')
        fixture.cli('record', run, '--slot', 'A', '--output', self.output,
                    '--maker-model', 'gpt-4.1', '--artefacts', bundle, ok=False)
        self.assertFalse((run / 'slots/A.txt').exists())
        (bundle / 'link.txt').unlink()
        (bundle / 'proof.txt').write_text('Original proof.\n')
        fixture.cli('record', run, '--slot', 'A', '--output', self.output,
                    '--maker-model', 'gpt-4.1', '--artefacts', bundle)
        (run / 'artefacts/A/proof.txt').write_text('Edited proof.\n')
        fixture.cli('judge-packet', run, ok=False)

    def test_real_subprocess_private_prepare_uses_override(self):
        import subprocess
        import sys
        result = subprocess.run([sys.executable, str(test_evals.REPO / 'scripts/eval_run.py'),
                                 '--root', str(self.fixture.root), 'prepare', str(self.case),
                                 '--project', 'quiet-harbour', '--candidates', 'tool:lead', 'tool:other'],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(Path(result.stdout.strip()).is_relative_to(self.base))
        self.assertFalse((self.fixture.root / 'evals/runs').exists())

    def test_codename_rule_and_public_case_source_are_refused(self):
        fixture = self.fixture
        for codename in ('', 'quiet', 'Quiet-Harbour', 'quiet-123', '../quiet-harbour', 'a-b-c'):
            fixture.cli('prepare', self.case, '--project', codename,
                        '--candidates', 'tool:lead', 'tool:other', ok=False)
        for codename in ('', 'quiet-harbour'):
            fixture.cli('prepare', fixture.case, '--project', codename,
                        '--candidates', 'tool:lead', 'tool:other', ok=False)

    def test_missing_anchor_and_copied_project_result_cannot_enter_leaderboard(self):
        from scripts.eval_report import verified_result
        from scripts.eval_core import EvalError
        fixture = self.fixture
        run = self.prepare()
        copied = fixture.root / 'evals/results/evidence/concept-critique/project-private-test.yaml'
        copied.parent.mkdir(parents=True)
        copied.write_bytes((run / 'run.yaml').read_bytes())
        with self.assertRaises(EvalError):
            verified_result(fixture.root, copied)
        (self.base / 'preparations.jsonl').unlink()
        fixture.cli('record', run, '--slot', 'A', '--output', self.output, '--maker-model', 'gpt-4.1', ok=False)


class GitTransportTests(unittest.TestCase):
    def test_real_read_only_history_and_failed_git_commands(self):
        import subprocess
        from scripts.eval_provenance import complete_history, git
        from scripts.eval_core import EvalError
        complete_history(test_evals.REPO)
        self.assertIn(b'[project]', git(test_evals.REPO, 'show', 'HEAD:pyproject.toml'))
        for failure in (OSError('missing Git'), subprocess.TimeoutExpired('git', 15)):
            with self.subTest(failure=failure), patch('scripts.eval_provenance.subprocess.run', side_effect=failure):
                with self.assertRaises(EvalError):
                    complete_history(test_evals.REPO)
        with patch('scripts.eval_provenance.subprocess.run', return_value=subprocess.CompletedProcess([], 128, b'', b'missing')):
            with self.assertRaises(EvalError):
                git(test_evals.REPO, 'show', 'missing:case.yaml')

    def test_shallow_and_unknown_history_states_fail_closed(self):
        from scripts.eval_provenance import complete_history
        from scripts.eval_core import EvalError
        for state in (b'true', b'unknown', b''):
            def transport(root, *args):
                return str(root).encode() if args[-1] == '--show-toplevel' else state
            with self.subTest(state=state), patch('scripts.eval_provenance.git', side_effect=transport):
                with self.assertRaises(EvalError):
                    complete_history(test_evals.REPO)
