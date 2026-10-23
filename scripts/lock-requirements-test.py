#!/usr/bin/env python3
"""Unit tests for lock-requirements.py. Run: python3 scripts/lock-requirements-test.py

These are hermetic — they never reach the index. The job runs `--check` straight
after, which is the real end-to-end. What is guarded here is the one property that
broke main: the file handed to `uv pip compile` must already carry the current pins.
"""

import contextlib
import importlib.util
import io
import subprocess
import tempfile
import unittest
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    'lock_requirements', Path(__file__).resolve().parent / 'lock-requirements.py')
lr = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(lr)


class FakeCompile:
    """Stands in for `uv pip compile`, recording what the output file was seeded with."""

    def __init__(self):
        self.cmd: list[str] = []
        self.seed: str | None = None

    def __call__(self, cmd, **kwargs):
        self.cmd = cmd
        out = Path(cmd[cmd.index('-o') + 1])
        self.seed = out.read_text(encoding='utf-8') if out.exists() else None
        out.write_text('compiled==1.0\n', encoding='utf-8')
        return subprocess.CompletedProcess(cmd, 0, '', '')


class TestSeeding(unittest.TestCase):
    def setUp(self):
        self.fake = FakeCompile()
        self._real = lr.subprocess.run
        lr.subprocess.run = self.fake

    def tearDown(self):
        lr.subprocess.run = self._real

    def test_existing_pins_are_handed_to_uv(self):
        # The regression: with an empty output file uv re-resolves every range in
        # requirements.in against whatever the index serves today, so an upstream
        # release inside the range fails --check on a tree nobody touched.
        lr.compile_body()
        self.assertIsNotNone(self.fake.seed, 'output file was not seeded with the lock')
        self.assertIn('pypdf==', self.fake.seed)
        self.assertNotIn('--upgrade', self.fake.cmd)

    def test_upgrade_drops_the_seed_and_asks_for_bumps(self):
        lr.compile_body(upgrade=True)
        self.assertIsNone(self.fake.seed, '--upgrade must not preserve the old pins')
        self.assertIn('--upgrade', self.fake.cmd)

    def test_resolution_is_pinned_to_the_runner(self):
        # Resolving against the local interpreter/platform would make the lock differ
        # per machine, which fails --check for whoever is not on the CI runner.
        lr.compile_body()
        for flag, value in (('--python-version', lr.PYTHON_VERSION),
                            ('--python-platform', lr.PLATFORM)):
            self.assertIn(flag, self.fake.cmd)
            self.assertEqual(self.fake.cmd[self.fake.cmd.index(flag) + 1], value)
        self.assertIn('--generate-hashes', self.fake.cmd)
        self.assertIn('--no-header', self.fake.cmd)

    def test_resolution_never_builds_sdists(self):
        # The Dependabot relock job resolves with a push token in reach, so a
        # package's setup.py must never run.
        lr.compile_body()
        self.assertIn('--no-build', self.fake.cmd)

    def test_base_pins_fill_in_packages_the_lock_lacks(self):
        # Dependabot's lock drops typing-extensions; without main's pin as a preference
        # uv takes its newest release, an unannounced bump inside the Dependabot PR.
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp) / 'base.txt'
            base.write_text('pypdf==0.0.1 \\\n    --hash=sha256:aa\n'
                            'Not_In.Lock==1.2.3 \\\n    --hash=sha256:bb\n    # via x\n',
                            encoding='utf-8')
            lr.compile_body(base=base)
        self.assertTrue(self.fake.seed.startswith(lr.LOCK.read_text(encoding='utf-8').rstrip('\n')))
        self.assertIn('\nNot_In.Lock==1.2.3 \\\n    --hash=sha256:bb\n    # via x\n', self.fake.seed)
        self.assertNotIn('pypdf==0.0.1', self.fake.seed, 'a pin the lock already has must win')


class TestUpgradePackage(unittest.TestCase):
    def setUp(self):
        self.fake = FakeCompile()
        self._real = lr.subprocess.run, lr.LOCK
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        lr.subprocess.run = self.fake
        lr.LOCK = Path(tmp.name) / 'requirements.txt'
        lr.LOCK.write_text(self._real[1].read_text(encoding='utf-8'), encoding='utf-8')

    def tearDown(self):
        lr.subprocess.run, lr.LOCK = self._real

    def rejected(self, *argv):
        with self.assertRaises(SystemExit), contextlib.redirect_stderr(io.StringIO()):
            lr.main(list(argv))
        self.assertEqual(self.fake.cmd, [], 'uv ran despite the rejected arguments')

    def test_named_packages_are_lifted_on_top_of_the_seed(self):
        # The point of the option: a security bump moves one pin, not the whole lock.
        with contextlib.redirect_stdout(io.StringIO()):
            lr.main(['-P', 'aiohttp==3.14.4', '--upgrade-package', 'Typing_Extensions'])
        self.assertIn('pypdf==', self.fake.seed)
        self.assertNotIn('--upgrade', self.fake.cmd)
        flags = [self.fake.cmd[i + 1] for i, a in enumerate(self.fake.cmd) if a == '--upgrade-package']
        self.assertEqual(flags, ['aiohttp==3.14.4', 'Typing_Extensions'])

    def test_combinations_that_make_no_sense_are_refused(self):
        self.rejected('-P', 'aiohttp', '--upgrade')
        self.rejected('-P', 'aiohttp', '--check')

    def test_a_name_missing_from_the_lock_is_refused(self):
        # uv ignores an unknown -P silently, so a typo would pass as a successful bump.
        self.rejected('-P', 'aiohtp==3.14.4')

    def test_uv_failure_surfaces_its_reason(self):
        def fail(cmd, **kwargs):
            raise subprocess.CalledProcessError(1, cmd, stderr='No solution found')
        lr.subprocess.run = fail
        with self.assertRaises(SystemExit) as ctx:
            lr.compile_body(packages=['pypdf==7.0.0'])
        self.assertIn('No solution found', str(ctx.exception.code))


class TestHeader(unittest.TestCase):
    def test_header_survives_regeneration(self):
        # `uv pip compile -o requirements.txt` overwrites the instruction block; the
        # whole point of the wrapper is that it does not.
        header = lr.header_of(lr.LOCK)
        self.assertTrue(header.startswith('#'))
        self.assertIn('lock-requirements.py', header)
        self.assertNotIn('pypdf==', header)

    def test_header_stops_at_the_first_pin(self):
        tmp = Path(__file__).resolve().parent / '_header-probe.tmp'
        tmp.write_text('# one\n\n# two\naiohttp==3.14.3\n# not this\n', encoding='utf-8')
        try:
            self.assertEqual(lr.header_of(tmp), '# one\n\n# two')
        finally:
            tmp.unlink()


if __name__ == '__main__':
    unittest.main(verbosity=2)
