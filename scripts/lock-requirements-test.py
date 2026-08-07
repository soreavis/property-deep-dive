#!/usr/bin/env python3
"""Unit tests for lock-requirements.py. Run: python3 scripts/lock-requirements-test.py

These are hermetic — they never reach the index. The job runs `--check` straight
after, which is the real end-to-end. What is guarded here is the one property that
broke main: the file handed to `uv pip compile` must already carry the current pins.
"""

import importlib.util
import subprocess
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
