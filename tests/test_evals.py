"""Real CLI and validator contracts for the Quality Lab."""
from __future__ import annotations

import copy
from contextlib import redirect_stderr, redirect_stdout
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
from datetime import date
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[1]


def case_data():
    return {
        'schema_version': 1, 'status': 'proposed', 'id': 'sample', 'class': 'evidence',
        'department': 'design', 'job': 'concept-critique',
        'brief': 'Critique the fictional label against the supplied evidence.',
        'inputs': ['brief.md'], 'required_output_format': 'Markdown findings and next action.',
        'rubric': [
            {'id': 'fit', 'criterion': 'Strategy fit', 'weight': 0.6,
             'anchors': {i: f'{i} concrete fit findings with a source and action' for i in range(1, 6)}},
            {'id': 'evidence', 'criterion': 'Evidence boundaries', 'weight': 0.4,
             'anchors': {i: f'{i} sourced claims distinguished from unknowns' for i in range(1, 6)}}],
        'pass_bar': 4.0, 'disqualifiers': [{'id': 'fabrication', 'description': 'Invented research.'}],
        'judge_instructions': 'Use Documented, Interpretation, Hypothesis or Unknown; never approve.',
    }


class EvalTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        (self.root / 'brief.md').write_text('Synthetic brief.\n')
        (self.root / 'toolkit/sources').mkdir(parents=True)
        (self.root / 'toolkit/sources/registry.json').write_text(json.dumps({'tools': [
            {'id': 'tool:lead', 'department': 'design', 'job': 'concept-critique', 'role': 'lead'},
            {'id': 'tool:other', 'department': 'design', 'job': 'concept-critique', 'role': 'specialist'},
        ]}))
        (self.root / 'schemas').mkdir()
        # The repository schema, consumed by the same validator as the CLI.
        schema = REPO / 'schemas/eval-case.json'
        if schema.exists():
            (self.root / 'schemas/eval-case.json').write_bytes(schema.read_bytes())
        self.case = self.root / 'evals/cases/design/concept-critique/sample.yaml'
        self.case.parent.mkdir(parents=True)
        self.write(self.case, case_data())
        self.output = self.root / 'output.txt'
        self.output.write_text('Documented: fictional sample. Unknown: real audience response.\n')
        # Fake only the read-only Git transport: no commits, index writes or
        # temporary Git repositories. Blobs and ancestry are frozen per event.
        self.commits = {}
        self.history_order = []
        self.history = patch('scripts.eval_provenance.git', side_effect=self.git_read)
        self.history.start()
        self.addCleanup(self.history.stop)
        transport = patch('scripts.eval_run.git', side_effect=self.git_read)
        transport.start()
        self.addCleanup(transport.stop)

    def commit_fixture(self):
        revision = f'{len(self.commits) + 1:040x}'
        files = {p.relative_to(self.root).as_posix(): p.read_bytes()
                 for p in self.root.rglob('*') if p.is_file()}
        self.commits[revision] = files
        self.history_order.insert(0, revision)
        return revision

    def git_read(self, root, *args):
        from scripts.eval_core import EvalError
        command = args[0]
        if command == 'rev-parse':
            return str(root).encode() if args[-1] == '--show-toplevel' else b'false'
        if command == 'merge-base':
            if args[-2] not in self.history_order:
                raise EvalError('not an ancestor of HEAD')
            return b''
        if command == 'log':
            relative = args[-1]
            revisions = [c for c in self.history_order if relative in self.commits[c]]
            if '-1' in args:
                revisions = revisions[:1]
            return '\n'.join(revisions).encode()
        if command == 'ls-tree':
            return b'blob' if args[-1] in self.commits.get(args[1], {}) else b''
        if command == 'show':
            revision, relative = args[1].split(':', 1)
            try:
                return self.commits[revision][relative]
            except KeyError as exc:
                raise EvalError('committed blob unavailable') from exc
        raise AssertionError(args)

    def anchor(self, run):
        # Run manifests are deliberately not an authority or a commit gate.
        pass

    def write(self, path, data):
        path.write_text(yaml.safe_dump(data, sort_keys=False))

    def cli(self, *args, ok=True):
        from scripts.eval_run import main
        if args[0] == 'prepare' and not self.history_order:
            self.commit_fixture()
        stdout, stderr = io.StringIO(), io.StringIO()
        with redirect_stdout(stdout), redirect_stderr(stderr):
            code = main(['--root', str(self.root), *map(str, args)])
        result = subprocess.CompletedProcess(args, code, stdout.getvalue(), stderr.getvalue())
        if ok:
            self.assertEqual(result.returncode, 0, result.stderr)
        else:
            self.assertNotEqual(result.returncode, 0, result.stdout)
            self.assertNotIn('Traceback', result.stderr)
        return result

    def prepare(self, demo=False):
        case = self.case
        if demo:
            case = self.case.with_name('demo-sample.yaml')
            data = case_data()
            data.update(id='demo-sample', **{'class': 'demo'})
            self.write(case, data)
        args = ['prepare', case, '--candidates', 'tool:lead', 'tool:other', '--run-id', 'test-run']
        if demo:
            args += ['--demo']
        run = Path(self.cli(*args).stdout.strip())
        self.anchor(run)
        self.anchor(run)
        for slot in ('A', 'B'):
            self.cli('record', run, '--slot', slot, '--output', self.output, '--maker-model', 'gpt-4.1')
        self.cli('check-blinding', run, '--checker-model', 'claude-opus-4-1', '--notes', 'Checked identities and signatures in both sanitised outputs.')
        return run

    def scores(self, run, **changes):
        data = {'slots': {slot: {
            'criteria': {'fit': {'score': 5, 'evidence': 'Documented: output paragraph 1.'},
                         'evidence': {'score': 3, 'evidence': 'Unknown: audience response, paragraph 1.'}},
            'disqualifiers': [], 'verdict': 'Promising but structurally unresolved',
            'next_action': 'Designer: obtain an actual label before formal critique.',
        } for slot in ('A', 'B')},
            'human_spot_check': {'reviewer': 'human reviewer', 'reviewed_on': '2026-10-23',
                                 'findings': 'Checked evidence citations and score anchors.'}}
        data.update(changes)
        path = run / 'scores.yaml'
        self.write(path, data)
        return path

    def test_candidate_identity_is_scrubbed_before_judge_packet(self):
        self.output.write_text(
            'I am tool:lead, an OpenAI GPT-4.1 agent. Generated by Claude / Anthropic.\n'
            'Signed: agent:creative-auditor and skill:3w-identity-system-critic.\n'
            'As an AI language model, my assessment follows.\n'
            'Model credits: Opus, Sonnet, Haiku.\n'
            'Documented: retain this useful finding. Unknown: real audience response.\n')
        run = self.prepare()
        packet = self.cli('judge-packet', run).stdout.casefold()
        for identity in ('tool:lead', 'tool:other', 'openai', 'gpt-4.1', 'claude', 'anthropic',
                         'agent:creative-auditor', 'skill:3w-identity-system-critic', 'i am', 'as an ai', 'opus', 'sonnet', 'haiku'):
            self.assertNotIn(identity, packet)
        self.assertIn('retain this useful finding', packet)

    def test_aliases_cannot_bypass_maker_judge_separation(self):
        run = self.prepare()
        for alias in ('openai/gpt-4.1', 'gpt-4.1-2025-04-14', 'azure/openai/gpt-4.1',
                      'GPT-4.1', 'unresolved-judge-alias'):
            self.cli('score', run, '--judge-model', alias, '--scores', self.scores(run), ok=False)
        self.assertFalse((self.root / 'evals/results').exists())

    def test_compact_unicode_and_separator_identities_are_blinded(self):
        from scripts.eval_blind import check_blind, sanitise
        run = {'candidates': {'A': {
            'tool_id': 'skill:3w-identity-system-critic',
            'registry_snapshot': {'name': 'Identity System Critic'},
        }}}
        for identity in ('IdentitySystemCritic', '3w_identity_system_critic',
                         '```IdentitySystemCritic```', 'ＩｄｅｎｔｉｔｙＳｙｓｔｅｍＣｒｉｔｉｃ',
                         'Identity\u200bSystem\u2060Critic', 'C l a u d e',
                         'c-l-a-u-d-e', 'cl4ude', 'O p e n A I'):
            with self.subTest(identity=identity):
                content = f'Made by {identity}.\nDocumented: retain this finding.'
                with self.assertRaises(ValueError):
                    check_blind(content, run)
                scrubbed = sanitise(content, run)
                self.assertNotIn(identity, scrubbed)
                self.assertIn('retain this finding', scrubbed)
                check_blind(scrubbed, run)
        # Production registry entries often have only an ID, without a display
        # name. Omitting the studio prefix must not expose that identity either.
        run['candidates']['A']['registry_snapshot'] = {}
        with self.assertRaises(ValueError):
            check_blind('Made by IdentitySystemCritic.', run)
        self.assertNotIn('IdentitySystemCritic', sanitise('Made by IdentitySystemCritic.', run))

    def test_common_words_survive_without_model_context(self):
        from scripts.eval_blind import check_blind, sanitise
        run = {'candidates': {}}
        content = ('A haiku about the Opus painting, in sonnet form.\n'
                   'The Gemini constellation, a medieval codex and a llama appear.\n'
                   'Discuss meta analysis; three sonnets and two haiku follow.\n')
        self.assertEqual(sanitise(content, run), content)
        check_blind(content, run)
        for identity in ('Anthropic Opus', 'Opus 4.1', 'Sonnet-4-5', 'Haiku model',
                         'Google Gemini', 'Gemini-2.5-Pro', 'OpenAI Codex', 'Codex agent',
                         'Model credits: Opus, Sonnet, Haiku.'):
            with self.subTest(identity=identity):
                with self.assertRaises(ValueError):
                    check_blind(identity, run)
                self.assertNotEqual(sanitise(identity, run).strip(), identity)

    def test_ambiguous_model_before_provider_is_fully_redacted(self):
        from scripts.eval_blind import check_blind, sanitise
        for identity in ('Opus / Anthropic', 'Codex by OpenAI', 'Gemini from Google'):
            with self.subTest(identity=identity):
                scrubbed = sanitise(identity, {'candidates': {}})
                self.assertNotIn(identity.split()[0], scrubbed)
                check_blind(scrubbed, {'candidates': {}})

    def test_roster_signatures_are_blinded_even_when_not_candidates(self):
        path = self.root / 'toolkit/sources/registry.json'
        data = json.loads(path.read_text())
        data['tools'].append({'id': 'agent:visual-designer', 'department': 'design',
                              'job': 'concept-critique', 'role': 'specialist'})
        path.write_text(json.dumps(data))
        agents = self.root / '.claude/agents'
        agents.mkdir(parents=True)
        (agents / 'design-brand-guardian.md').write_text('---\nname: Brand Guardian\n---\n')
        self.output.write_text('Made by VisualDesigner and Brand_Guardian.\nDocumented: retain findings.\n')
        run = self.prepare()
        packet = self.cli('judge-packet', run).stdout
        self.assertNotIn('VisualDesigner', packet)
        self.assertNotIn('Brand_Guardian', packet)
        self.assertIn('retain findings', packet)

    def test_compact_candidate_in_frozen_input_blocks_clearance(self):
        path = self.root / 'toolkit/sources/registry.json'
        data = json.loads(path.read_text())
        data['tools'][0]['name'] = 'Identity System Critic'
        path.write_text(json.dumps(data))
        (self.root / 'brief.md').write_text('Made by IdentitySystemCritic.\n')
        run = Path(self.cli('prepare', self.case, '--candidates', 'tool:lead', 'tool:other').stdout.strip())
        for slot in ('A', 'B'):
            self.cli('record', run, '--slot', slot, '--output', self.output, '--maker-model', 'gpt-4.1')
        self.cli('check-blinding', run, '--checker-model', 'claude-opus-4-1', '--notes', 'Checked.', ok=False)
        self.cli('judge-packet', run, ok=False)

    def test_model_family_separation_spans_versions_and_tiers(self):
        from scripts.eval_core import canonical_model
        for first, second in (('gpt-4.1', 'OpenAI/GPT-6.1-sol'),
                              ('claude-opus-4-1', 'anthropic/claude-sonnet-4-5'),
                              ('claude-3-5-haiku', 'claude-opus-4-1'),
                              ('gemini-2.5-pro', 'google/gemini-3.1-flash')):
            with self.subTest(first=first, second=second):
                self.assertEqual(canonical_model(first), canonical_model(second))

    def test_coordinated_creation_and_run_edits_cannot_reclassify_demo(self):
        from scripts.eval_core import EvalError, digest
        from scripts.eval_report import build_report
        from scripts.oscheck.evals import check_evals
        run = self.prepare(demo=True)
        # Exact round-two bypass: change both manifests and all dependent hashes.
        creation_path = run / 'creation.yaml'
        creation = yaml.safe_load(creation_path.read_text())
        creation['demo'] = False
        creation['score_meaning'] = 'Rubric evidence; human approval remains separate.'
        self.write(creation_path, creation)
        run_path = run / 'run.yaml'
        metadata = yaml.safe_load(run_path.read_text())
        metadata.update(demo=False, score_meaning=creation['score_meaning'],
                        creation_sha256=digest(creation_path.read_bytes()))
        self.write(run_path, metadata)
        (run / 'run.sha256').write_text(digest(run_path.read_bytes()))
        scores = self.scores(run)
        self.cli('check-blinding', run, '--checker-model', 'claude-opus-4-1',
                 '--notes', 'Checked the changed packet.', ok=False)
        self.cli('score', run, '--judge-model', 'claude-opus-4-1', '--scores', scores, ok=False)
        self.assertTrue(check_evals(self.root, {}), 'repository validation must reject relabelling')
        # A forged result and result hash cannot restore leaderboard eligibility.
        result = {**metadata, 'scores': yaml.safe_load(scores.read_text())['slots']}
        destination = self.root / 'evals/results' / 'evidence' / metadata['job'] / (metadata['run_id'] + '.yaml')
        destination.parent.mkdir(parents=True)
        self.write(destination, result)
        (run / 'result.sha256').write_text(digest(destination.read_bytes()))
        with self.assertRaises(EvalError):
            build_report(self.root)

    def test_demo_class_and_candidate_metadata_cannot_change_before_scoring(self):
        run = self.prepare(demo=True)
        path = run / 'run.yaml'
        original = yaml.safe_load(path.read_text())
        mutations = []
        for key, value in [('demo', False), ('score_meaning', 'Quality evidence')]:
            data = copy.deepcopy(original)
            data[key] = value
            mutations.append(data)
        data = copy.deepcopy(original)
        data['candidates']['A']['maker_model'] = 'gemini-2.5-pro'
        mutations.append(data)
        data = copy.deepcopy(original)
        data['candidates']['A']['tool_id'] = 'tool:other' if data['candidates']['A']['tool_id'] == 'tool:lead' else 'tool:lead'
        mutations.append(data)
        for data in mutations:
            self.write(path, data)
            self.cli('score', run, '--judge-model', 'claude-opus-4-1', '--scores', self.scores(run), ok=False)
            self.cli('judge-packet', run, ok=False)
        self.assertFalse((self.root / 'evals/results').exists())

    def test_leaderboard_rejects_reclassified_demo_result(self):
        from scripts.eval_report import build_report
        from scripts.eval_core import EvalError
        run = self.prepare(demo=True)
        self.cli('score', run, '--judge-model', 'claude-opus-4-1', '--scores', self.scores(run))
        path = self.root / 'evals/results/demos/concept-critique/demo-test-run.yaml'
        result = yaml.safe_load(path.read_text())
        result['demo'] = False
        self.write(path, result)
        with self.assertRaises(EvalError):
            build_report(self.root)

    def test_packet_and_score_require_separate_blinding_clearance(self):
        run = Path(self.cli('prepare', self.case, '--candidates', 'tool:lead', 'tool:other', '--run-id', 'uncleared').stdout.strip())
        self.anchor(run)
        for slot in ('A', 'B'):
            self.cli('record', run, '--slot', slot, '--output', self.output, '--maker-model', 'gpt-4.1')
        self.cli('judge-packet', run, ok=False)
        self.assertNotIn('fictional sample', (run / 'judge-packet.txt').read_text())
        self.cli('score', run, '--judge-model', 'claude-opus-4-1', '--scores', self.scores(run), ok=False)
        self.cli('check-blinding', run, '--checker-model', 'openai/gpt-4.1-2025-04-14', '--notes', 'Checked.', ok=False)
        self.cli('check-blinding', run, '--checker-model', 'claude-opus-4-1', '--notes', 'Checked signatures and identities.')
        self.assertIn('fictional sample', self.cli('judge-packet', run).stdout)

    def test_identity_leaks_in_frozen_inputs_block_clearance(self):
        (self.root / 'brief.md').write_text('Maker identity: tool:lead, OpenAI GPT-4.1.\n')
        run = Path(self.cli('prepare', self.case, '--candidates', 'tool:lead', 'tool:other', '--run-id', 'leaked').stdout.strip())
        self.anchor(run)
        for slot in ('A', 'B'):
            self.cli('record', run, '--slot', slot, '--output', self.output, '--maker-model', 'gpt-4.1')
        self.cli('check-blinding', run, '--checker-model', 'claude-opus-4-1', '--notes', 'Checked.', ok=False)
        self.cli('judge-packet', run, ok=False)

    def test_canonical_model_families_and_unresolved_aliases(self):
        from scripts.eval_core import canonical_model, EvalError
        for value in ('anthropic/claude-opus-4-1-20250805', 'claude-opus-4.1', 'bedrock/anthropic/claude-opus-4-1'):
            self.assertEqual(canonical_model(value), 'anthropic/claude')
        for value in ('openai/gpt-4.1-2025-04-14', 'azure/gpt-4.1-mini', 'GPT-4.1'):
            self.assertEqual(canonical_model(value), 'openai/gpt')
        for value in ('my-deployment', 'latest', 'vendor/model-v1', 'unknown', 'claude-opus-latest'):
            with self.subTest(value=value), self.assertRaises(EvalError):
                canonical_model(value)
        self.assertEqual(canonical_model('historical-unknown', demo=True), 'unknown')

    def test_creation_class_is_checked_even_if_mutated_run_is_rehashed(self):
        from scripts.eval_core import digest
        run = self.prepare(demo=True)
        path = run / 'run.yaml'
        data = yaml.safe_load(path.read_text())
        data['demo'] = False
        self.write(path, data)
        (run / 'run.sha256').write_text(digest(path.read_bytes()))
        self.cli('score', run, '--judge-model', 'claude-opus-4-1', '--scores', self.scores(run), ok=False)

    def test_non_demo_without_creation_provenance_cannot_enter_leaderboard(self):
        from scripts.eval_report import build_report
        from scripts.eval_core import EvalError
        run = self.prepare()
        self.cli('score', run, '--judge-model', 'claude-opus-4-1', '--scores', self.scores(run))
        path = self.root / 'evals/results/evidence/concept-critique/evidence-test-run.yaml'
        result = yaml.safe_load(path.read_text())
        del result['creation_sha256']
        self.write(path, result)
        with self.assertRaises(EvalError):
            build_report(self.root)

    def test_edited_judge_packet_cannot_be_scored(self):
        run = self.prepare()
        with (run / 'judge-packet.txt').open('a') as packet:
            packet.write('Changed after checker clearance.\n')
        self.cli('score', run, '--judge-model', 'claude-opus-4-1', '--scores', self.scores(run), ok=False)

    def test_full_cycle_freezes_inputs_blinds_and_calculates_weighted_score(self):
        run = self.prepare()
        packet = self.cli('judge-packet', run).stdout
        self.assertIn('Documented: fictional sample', packet)
        for private in ('tool:lead', 'tool:other', 'gpt-4.1', 'output.txt', str(self.root)):
            self.assertNotIn(private, packet)
        (self.root / 'brief.md').write_text('CHANGED after preparation')
        self.assertNotIn('CHANGED', self.cli('judge-packet', run).stdout)
        self.cli('score', run, '--judge-model', 'claude-opus-4-1', '--scores', self.scores(run))
        result = yaml.safe_load((self.root / 'evals/results/evidence/concept-critique/evidence-test-run.yaml').read_text())
        self.assertAlmostEqual(result['scores']['A']['weighted_score'], 4.2)
        self.assertTrue(result['scores']['A']['passes'])
        from scripts.oscheck.evals import check_evals
        self.assertEqual(check_evals(self.root, {}), [])
        self.assertIn('tool:lead', self.cli('reveal', run).stdout)
        self.cli('record', run, '--slot', 'A', '--output', self.output, '--maker-model', 'new', ok=False)
        self.cli('score', run, '--judge-model', 'claude-opus-4-1', '--scores', self.scores(run), ok=False)

    def test_same_maker_or_missing_output_cannot_be_judged(self):
        run = self.prepare()
        self.cli('score', run, '--judge-model', 'gpt-4.1', '--scores', self.scores(run), ok=False)
        self.cli('prepare', self.case, '--candidates', 'tool:lead', 'tool:other', '--run-id', 'empty')
        empty = run.with_name('evidence-empty')
        self.cli('judge-packet', empty, ok=False)
        self.cli('score', empty, '--judge-model', 'claude-opus-4-1', '--scores', self.scores(run), ok=False)

    def test_invalid_score_contracts_do_not_write_results(self):
        run = self.prepare()
        original = yaml.safe_load(self.scores(run).read_text())
        variants = []
        for value in (0, 6, True, 4.5, '5'):
            data = copy.deepcopy(original)
            data['slots']['A']['criteria']['fit']['score'] = value
            variants.append(data)
        for mutation in ('missing-slot', 'extra-criterion', 'empty-evidence', 'bad-verdict', 'bad-disqualifier'):
            data = copy.deepcopy(original)
            if mutation == 'missing-slot':
                del data['slots']['B']
            elif mutation == 'extra-criterion':
                data['slots']['A']['criteria']['extra'] = {'score': 5, 'evidence': 'Documented: x'}
            elif mutation == 'empty-evidence':
                data['slots']['A']['criteria']['fit']['evidence'] = ''
            elif mutation == 'bad-verdict':
                data['slots']['A']['verdict'] = 'approved'
            else:
                data['slots']['A']['disqualifiers'] = ['not-in-case']
            variants.append(data)
        for data in variants:
            with self.subTest(data=data):
                self.write(run / 'bad.yaml', data)
                self.cli('score', run, '--judge-model', 'claude-opus-4-1', '--scores', run / 'bad.yaml', ok=False)
        self.assertFalse((self.root / 'evals/results').exists())

    def test_disqualifier_overrides_high_score(self):
        run = self.prepare()
        path = self.scores(run)
        data = yaml.safe_load(path.read_text())
        data['slots']['A']['disqualifiers'] = ['fabrication']
        self.write(path, data)
        self.cli('score', run, '--judge-model', 'claude-opus-4-1', '--scores', path)
        result = yaml.safe_load((self.root / 'evals/results/evidence/concept-critique/evidence-test-run.yaml').read_text())
        self.assertFalse(result['scores']['A']['passes'])

    def test_prepare_rejects_unknown_duplicate_and_unsafe_identifiers(self):
        for candidates in (['missing'], ['tool:lead', 'tool:lead'], ['tool:lead']):
            self.cli('prepare', self.case, '--candidates', *candidates, ok=False)
        for run_id in ('../escape', '/tmp/escape', 'bad/name'):
            self.cli('prepare', self.case, '--candidates', 'tool:lead', 'tool:other', '--run-id', run_id, ok=False)
        run = self.prepare()
        self.cli('record', run, '--slot', '../escape', '--output', self.output, '--maker-model', 'x', ok=False)
        self.cli('prepare', self.case, '--candidates', 'tool:lead', 'tool:other', '--run-id', 'test-run', ok=False)

    def test_case_validation_rejects_bad_anchors_weights_paths_and_job(self):
        from scripts.oscheck.evals import check_evals
        config = {'evals': {'case_schema': 'schemas/eval-case.json'}}
        self.assertEqual(check_evals(self.root, config), [])
        for mutation in ('anchors', 'weights', 'escape', 'missing', 'symlink', 'job', 'status', 'nan'):
            data = case_data()
            if mutation == 'anchors':
                del data['rubric'][0]['anchors'][5]
            elif mutation == 'weights':
                data['rubric'][0]['weight'] = 0.8
            elif mutation in ('escape', 'missing', 'symlink'):
                data['inputs'] = [{'escape': '../outside.md', 'missing': 'absent.md', 'symlink': 'link.md'}[mutation]]
                (self.root / 'link.md').unlink(missing_ok=True)
                (self.root / 'link.md').symlink_to('/etc/hosts')
            elif mutation == 'job':
                data['job'] = 'wrong'
            elif mutation == 'status':
                data['status'] = 'approved'
            else:
                data['rubric'][0]['weight'] = float('nan')
            self.write(self.case, data)
            with self.subTest(mutation=mutation):
                self.assertTrue(check_evals(self.root, config))

    def test_exact_pass_bar_is_independent_of_criterion_order(self):
        data = case_data()
        data['rubric'] = [
            {'id': key, 'criterion': key, 'weight': weight,
             'anchors': {i: f'{i} evidence-backed findings' for i in range(1, 6)}}
            for key, weight in [('fit', 0.35), ('evidence', 0.30), ('craft', 0.20), ('scope', 0.15)]
        ]
        self.write(self.case, data)
        run = self.prepare()
        path = self.scores(run)
        scores = yaml.safe_load(path.read_text())
        for slot, order in [('A', ['fit', 'evidence', 'craft', 'scope']),
                            ('B', ['scope', 'craft', 'evidence', 'fit'])]:
            scores['slots'][slot]['criteria'] = {
                key: {'score': 4, 'evidence': 'Documented: slot response, paragraph 1.'} for key in order}
        self.write(path, scores)
        self.cli('score', run, '--judge-model', 'claude-opus-4-1', '--scores', path)
        result = yaml.safe_load((self.root / 'evals/results/evidence/concept-critique/evidence-test-run.yaml').read_text())
        for slot in ('A', 'B'):
            self.assertEqual(result['scores'][slot]['weighted_score'], 4.0)
            self.assertTrue(result['scores'][slot]['passes'])

    def test_tampered_snapshots_and_early_reveal_are_rejected(self):
        run = self.prepare()
        self.cli('reveal', run, ok=False)
        (run / 'inputs/01.txt').write_text('tampered')
        self.cli('judge-packet', run, ok=False)
        (run / 'inputs/01.txt').write_text('Synthetic brief.\n')
        (run / 'slots/A.txt').write_text('tampered output')
        self.cli('score', run, '--judge-model', 'claude-opus-4-1', '--scores', self.scores(run), ok=False)

    def test_yaml_duplicates_malformed_scores_and_pending_human_review(self):
        from scripts.eval_report import build_report
        run = self.prepare()
        path = run / 'invalid.yaml'
        path.write_text('slots: {}\nslots: {}\n')
        self.cli('score', run, '--judge-model', 'claude-opus-4-1', '--scores', path, ok=False)
        path.write_text('slots: [\n')
        self.cli('score', run, '--judge-model', 'claude-opus-4-1', '--scores', path, ok=False)
        path = self.scores(run)
        data = yaml.safe_load(path.read_text())
        del data['human_spot_check']
        self.write(path, data)
        self.cli('score', run, '--judge-model', 'claude-opus-4-1', '--scores', path)
        report = build_report(self.root)
        self.assertIn('excluded from lead evidence', report)
        self.assertIn('No eligible quality evidence', report)
        from scripts.eval_report import main
        with redirect_stdout(io.StringIO()):
            self.assertEqual(main(['--root', str(self.root)]), 0)
        self.assertTrue((self.root / 'evals/LEADERBOARD.md').is_file())

    def test_run_directory_symlink_cannot_write_outside_repository(self):
        with tempfile.TemporaryDirectory() as outside:
            (self.root / 'evals/runs').symlink_to(outside, target_is_directory=True)
            self.cli('prepare', self.case, '--candidates', 'tool:lead', 'tool:other', ok=False)
            self.assertEqual(list(Path(outside).iterdir()), [])

    def test_report_separates_demo_flags_disagreement_and_ages_results(self):
        from scripts.eval_report import build_report
        run = self.prepare(demo=True)
        self.cli('score', run, '--judge-model', 'claude-opus-4-1', '--scores', self.scores(run))
        report = build_report(self.root, date(2027, 2, 1))
        self.assertIn('Pipeline demonstrations', report)
        self.assertIn('No eligible quality evidence', report)
        # Separate quality run; do not reclassify the demonstration.
        quality = Path(self.cli('prepare', self.case, '--candidates', 'tool:lead', 'tool:other', '--run-id', 'quality-run').stdout.strip())
        self.anchor(quality)
        for slot in ('A', 'B'):
            self.cli('record', quality, '--slot', slot, '--output', self.output, '--maker-model', 'gpt-4.1')
        self.cli('check-blinding', quality, '--checker-model', 'claude-opus-4-1', '--notes', 'Checked both outputs.')
        scores = self.scores(quality)
        submission = yaml.safe_load(scores.read_text())
        metadata = yaml.safe_load((quality / 'run.yaml').read_text())
        incumbent = next(s for s, c in metadata['candidates'].items() if c['tool_id'] == 'tool:lead')
        for criterion in submission['slots'][incumbent]['criteria'].values():
            criterion['score'] = 2
        self.write(scores, submission)
        self.cli('score', quality, '--judge-model', 'claude-opus-4-1', '--scores', scores)
        report = build_report(self.root, date(2027, 2, 1))
        self.assertIn('DISAGREEMENT', report)
        self.assertIn('RETEST', report)
        self.assertIn('tool:other', report)


if __name__ == '__main__':
    unittest.main()
