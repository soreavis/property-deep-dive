#!/usr/bin/env python3
"""Unit tests for scripts/check-playbooks.py. Run: python3 scripts/check-playbooks-test.py"""

from __future__ import annotations

import datetime
import importlib.util
import unittest
from pathlib import Path

_spec = importlib.util.spec_from_file_location("check_playbooks", Path(__file__).parent / "check-playbooks.py")
CP = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(CP)
TODAY = datetime.date(2026, 11, 3)


def errs(line: str) -> list[str]:
    return CP.line_errors(line, TODAY)


class ProcessNotes(unittest.TestCase):
    def test_fetch_log_wording_fails(self):
        for line in ("site returns HTTP 403 to non-browser clients", "read through Tavily after curl 403s",
                     "bot-walled", "the site sent empty replies to automated requests", "returned 404"):
            self.assertTrue(errs(line), line)

    def test_reader_facing_wording_passes(self):
        for line in ("could not be read for verification on 2026-11-03 — check it directly",
                     "archived copy of 14 Jul 2026", "M.Of. 403 of 11 May 2023", "403 households"):
            self.assertEqual(errs(line), [], line)


class StaleData(unittest.TestCase):
    def test_old_year_needs_suffix(self):
        self.assertTrue(errs("rate 3 % (2023 data, source X)"))
        self.assertEqual(errs("rate 3 % (2023 data, source X) — rates/figures may have changed since"), [])

    def test_recent_year_passes(self):
        self.assertEqual(errs("rate 3 % (2025 data, source X)"), [])


class Arithmetic(unittest.TestCase):
    def test_correct_results_pass(self):
        for line in ("(computed: 2.25% × £300k + 3.50% × £200k = £6,750 + £7,000 = £13,750)",
                     "(computed: €40,000 ÷ 7% ≈ €571k)", "(computed, 21% × 1.09 = 22.89%)",
                     "(computed: 11 + 21 + 12 = 44 %)", "at most ¥0.5 M × 70 % × 1.4 % = ¥4,900/yr (computed)",
                     "500–999 266 / 760 = 35.0 % (computed)", "(computed: 2% × £250,000 + 5.5% × £100,000 = 3% × £350,000)"):
            self.assertEqual(errs(line), [], line)

    def test_wrong_results_fail(self):
        for line in ("(computed: €40,000 ÷ 7% = €480k)", "(computed: 120 × 12 = 1,500)",
                     "(computed: 2.25% × £300k = £6,750 + £7,000 = £14,000)"):
            self.assertTrue(any(e.startswith("arithmetic") for e in errs(line)), line)

    def test_labels_and_bases_are_not_sums(self):
        for line in ("index 2025 = 100 (computed)", "at €250,000 ≈ 2.2 % effective (computed)",
                     "no marker on this line: 2 × 2 = 5"):
            self.assertEqual(errs(line), [], line)


PLAYBOOK = """# X
## Section: `--price`
a
## Section: `--tax`
b
## Section: `--traffic`
c
## Status

✅ fast-changing sections re-verified as of 2026-10-23.

### Per-section verification (overrides playbook-level date)

| Section | Last verified | Verifier | Notes |
|---|---|---|---|
| `--price` | 2026-10-23 | pass | n |
{tax}
"""


class Restamp(unittest.TestCase):
    def test_complete_table_passes(self):
        self.assertEqual(CP.restamp_errors(PLAYBOOK.format(tax="| `--tax` | 2026-10-23 | pass | n |")), [])

    def test_a_subsection_row_does_not_cover_the_section(self):
        self.assertTrue(CP.restamp_errors(PLAYBOOK.format(tax="| `--tax` › Rates | 2026-10-23 | pass | n |")))

    def test_an_open_objection_rejects_the_stamp_however_complete_the_table(self):
        text = PLAYBOOK.format(tax="| `--tax` | 2026-10-23 | pass | n |")
        self.assertTrue(CP.restamp_errors(text, ("tax",)))

    def test_missing_or_older_section_fails(self):
        self.assertTrue(CP.restamp_errors(PLAYBOOK.format(tax="")))
        self.assertTrue(CP.restamp_errors(PLAYBOOK.format(tax="| `--tax` | 2026-04-25 | pass | n |")))

    def test_no_restamp_claim_is_not_checked(self):
        self.assertEqual(CP.restamp_errors(PLAYBOOK.replace("re-verified as of", "populated").format(tax="")), [])


if __name__ == "__main__":
    unittest.main()
