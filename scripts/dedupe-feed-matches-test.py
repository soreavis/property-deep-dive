#!/usr/bin/env python3
"""Unit tests for scripts/dedupe-feed-matches.py.

Each test pins one shape seen in the duplicate issues #302-#320.

Run: python3 scripts/dedupe-feed-matches-test.py
"""

from __future__ import annotations

import contextlib
import importlib.util
import io
import sys
import tempfile
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "dedupe_feed_matches", str(Path(__file__).parent / "dedupe-feed-matches.py")
)
dedupe = importlib.util.module_from_spec(spec)
sys.modules["dedupe_feed_matches"] = dedupe
spec.loader.exec_module(dedupe)

CJEU = (
    "- **[CJEU-PR]** 107/Thu Jul 16 00:00:00 CEST 2026 : null - Judgment in Case C-26/25\n"
    "  - Judgment on tenancy deposits\n"
    "  - <https://curia.europa.eu/jcms/upload/docs/cp260107en.pdf>\n"
)
EP = (
    "- **[EP-Adopted]** Housing crisis in the European Union\n"
    "  - <https://data.europarl.europa.eu/api/v2/adopted-texts/TA-10-2026-0234>\n"
)


def run(matches: str, reported: str) -> tuple[int, str]:
    """Run main() against two file bodies; return (exit_code, stdout)."""
    paths = []
    for body in (matches, reported):
        with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False, encoding="utf-8") as fh:
            fh.write(body)
            paths.append(fh.name)
    argv = sys.argv
    sys.argv = ["dedupe-feed-matches.py", "--matches", paths[0], "--reported", paths[1]]
    out = io.StringIO()
    try:
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(io.StringIO()):
            code = dedupe.main()
    finally:
        sys.argv = argv
    return code, out.getvalue()


class TestDedupe(unittest.TestCase):
    def test_item_reported_yesterday_is_dropped(self):
        # #302/#303/#304 were the same CJEU judgment on three consecutive polls.
        code, out = run(CJEU, f"Property-relevant items detected.\n\n{CJEU}")
        self.assertEqual(code, 0)
        self.assertEqual(out, "")

    def test_unreported_item_survives(self):
        code, out = run(EP, CJEU)
        self.assertEqual(code, 0)
        self.assertIn("Housing crisis", out)

    def test_snippet_lines_travel_with_their_block(self):
        code, out = run(CJEU, "")
        self.assertIn("Judgment on tenancy deposits", out)
        self.assertIn("<https://curia.europa.eu/jcms/upload/docs/cp260107en.pdf>", out)

    def test_linkless_item_dedupes_on_title(self):
        item = "- **[EC-Press]** Daily News 17 / 07 / 2026\n"
        code, out = run(item, item)
        self.assertEqual(out, "")

    def test_linkless_titles_are_not_conflated(self):
        code, out = run(
            "- **[EC-Press]** Daily News 18 / 07 / 2026\n",
            "- **[EC-Press]** Daily News 17 / 07 / 2026\n",
        )
        self.assertIn("18 / 07 / 2026", out)

    def test_no_prior_issues_keeps_everything(self):
        code, out = run(CJEU + EP, "")
        self.assertIn("C-26/25", out)
        self.assertIn("Housing crisis", out)

    def test_one_report_does_not_open_eleven_rows(self):
        # #375's exact shape: five sitting records and four votes carrying the
        # report reference, plus two debate records that omit it — 11 rows, 11
        # URLs, one file. The reference has to strip or the debates split off.
        base = "- **[EP-Procedures]** Housing crisis in the European Union"
        ref = " (A10-0025/2026 - Borja Giménez Larraz)"
        suffixes = [ref] * 5 + [f"{ref} (vote)"] * 4 + [" (debate)"] * 2
        run_matches = "".join(
            f"{base}{suffix}\n  - <https://data.europarl.europa.eu/api/v2/procedures/OTH-{i}>\n"
            for i, suffix in enumerate(suffixes)
        )
        code, out = run(run_matches, "")
        self.assertEqual(code, 0)
        self.assertEqual(out.count("Housing crisis"), 1)

    def test_distinct_reports_are_not_merged_by_the_reference_strip(self):
        code, out = run(
            "- **[EP-Procedures]** Public access to documents (A10-0011/2026 - Ostrihoňová)\n"
            "  - <https://data.europarl.europa.eu/api/v2/procedures/OTH-1>\n"
            "- **[EP-Procedures]** Copyright and generative AI (A10-0019/2026 - Voss)\n"
            "  - <https://data.europarl.europa.eu/api/v2/procedures/OTH-2>\n",
            "",
        )
        self.assertIn("Public access to documents", out)
        self.assertIn("Copyright and generative AI", out)

    def test_artefact_of_a_triaged_report_does_not_come_back(self):
        # A new sitting record under a new URL must not reopen a closed triage.
        code, out = run(
            "- **[EP-Procedures]** Housing crisis in the European Union (A10-0025/2026) (vote)\n"
            "  - <https://data.europarl.europa.eu/api/v2/procedures/OTH-999>\n",
            "- **[EP-Procedures]** Housing crisis in the European Union (A10-0025/2026)\n"
            "  - <https://data.europarl.europa.eu/api/v2/procedures/OTH-1>\n",
        )
        self.assertEqual(out, "")

    def test_opinion_and_judgment_in_one_case_stay_separate(self):
        # The qualifier strip must only ever take a trailing (vote)/(debate) —
        # a distinction carried in the title body is a distinct legal event.
        code, out = run(
            "- **[CJEU-PR]** Opinion in Case C-26/25\n  - <https://curia.europa.eu/a.pdf>\n"
            "- **[CJEU-PR]** Judgment in Case C-26/25\n  - <https://curia.europa.eu/b.pdf>\n",
            "",
        )
        self.assertIn("Opinion in Case C-26/25", out)
        self.assertIn("Judgment in Case C-26/25", out)


if __name__ == "__main__":
    unittest.main(verbosity=2)
