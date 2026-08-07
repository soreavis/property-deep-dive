#!/usr/bin/env python3
"""Unit tests for scripts/regwatch_parse.py.

Each test pins one defect found in the three inline parsers this module replaced.

Run: python3 scripts/regwatch_parse-test.py
"""

from __future__ import annotations

import sys
import unittest
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import regwatch_parse as rp  # noqa: E402

HEADER = "### 🇧🇧 BB\n"


def doc(*entries: str, header: str = HEADER) -> str:
    return "## Recently enacted reforms\n\n" + header + "\n" + "".join(f"- `{e}`\n" for e in entries)


class TestNestedBackticks(unittest.TestCase):
    """The defect: `[^`]+` stopped at the first nested code span, dropping 27 entries."""

    def test_source_field_with_code_span_parses(self):
        entries, unparsed = rp.parse(
            doc("2026 income year | tax | Band reduction | BRA — `https://bra.gov.bb/` | 2026-05-08 | 2026-08-01 | 2 | --tax")
        )
        self.assertEqual(unparsed, [])
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0].source, "BRA — `https://bra.gov.bb/`")
        self.assertEqual(entries[0].revisit_date, date(2026, 8, 1))

    def test_multiple_code_spans_in_one_entry(self):
        entries, unparsed = rp.parse(
            doc("2024-XX-XX | visa | Portal renamed `a.gov.mc` → `b.gov.mc` | Gov `https://b.gov.mc/` | 2026-04-01 | 2027-12-31 | 4 | --visa")
        )
        self.assertEqual(unparsed, [])
        self.assertEqual(entries[0].topic, "visa")
        self.assertIn("`a.gov.mc` → `b.gov.mc`", entries[0].summary)


class TestCoverageGuard(unittest.TestCase):
    """An entry that does not parse is invisible to both schedulers — never silent."""

    def test_misplaced_closing_backtick_is_reported(self):
        # The real defect at regulatory-watch.md L534: the closing backtick sat one
        # word early, leaving " ownership" outside the span and the whole entry
        # unparseable. Built raw — doc() would append the backtick this test omits.
        text = (
            "## Recently enacted reforms\n\n"
            + HEADER
            + "\n- `2021-02 | foreign-buyer | Hak Pakai | ATR/BPN | 2026-05-01 | 2026-11-01 | 1 | --tax --visa` ownership\n"
        )
        entries, unparsed = rp.parse(text)
        self.assertEqual(entries, [])
        self.assertEqual(len(unparsed), 1)
        self.assertEqual(unparsed[0][0], 5)

    def test_wrong_field_count_is_reported(self):
        _, unparsed = rp.parse(doc("2026-01-01 | tax | Summary | Source | 2026-01-01 | 2026-06-01 | 2"))
        self.assertEqual(len(unparsed), 1)

    def test_bullets_outside_a_country_header_are_not_entries(self):
        # "## Related files" bullets used to inherit the last country header and be
        # audited as malformed entries.
        text = doc("2026-01-01 | tax | S | Src | 2026-01-01 | 2026-06-01 | 2 | --tax")
        text += "\n## Related files\n\n- `shared/updater.md` — auto-downgrade rule\n"
        entries, unparsed = rp.parse(text)
        self.assertEqual(len(entries), 1)
        self.assertEqual(unparsed, [])

    def test_format_template_is_not_an_entry(self):
        text = doc("2026-01-01 | tax | S | Src | 2026-01-01 | 2026-06-01 | 2 | --tax")
        text += "\n## Format for new entries\n\n- `<effective_date> | <topic> | <summary> | <source name> | <verified_date> | <revisit_by> | <tier> | <sections>`\n"
        entries, _ = rp.parse(text)
        self.assertEqual(len(entries), 1)


class TestAttribution(unittest.TestCase):
    def test_multi_country_header_fans_out(self):
        entries, _ = rp.parse(
            doc(
                "2026-05-20 | rental | EU STR reg | Src | 2026-05-20 | 2026-11-01 | 2 | --rental",
                header="### 🇸🇪 SE / 🇫🇮 FI / 🇳🇴 NO\n",
            )
        )
        self.assertEqual(entries[0].isos, ("SE", "FI", "NO"))

    def test_trailing_iso_tag_pins_to_one_country(self):
        entries, _ = rp.parse(
            doc(
                "2026-05-20 | rental | Local rule | Src | 2026-05-20 | 2026-11-01 | 2 | --rental (FI)",
                header="### 🇸🇪 SE / 🇫🇮 FI / 🇳🇴 NO\n",
            )
        )
        self.assertEqual(entries[0].isos, ("FI",))

    def test_iso_tag_outside_the_header_set_falls_back_to_fan_out(self):
        entries, _ = rp.parse(
            doc(
                "2026-05-20 | rental | Rule | Src | 2026-05-20 | 2026-11-01 | 2 | --rental (DE)",
                header="### 🇸🇪 SE / 🇫🇮 FI\n",
            )
        )
        self.assertEqual(entries[0].isos, ("SE", "FI"))

    def test_non_country_h3_clears_attribution(self):
        text = "### Recently enacted reforms\n\n- `2026-01-01 | tax | S | Src | 2026-01-01 | 2026-06-01 | 2 | --tax`\n"
        entries, unparsed = rp.parse(text)
        self.assertEqual(entries, [])
        self.assertEqual(unparsed, [])


class TestDateFields(unittest.TestCase):
    def test_revisit_requires_a_bare_iso_date(self):
        entries, _ = rp.parse(doc("2026-01-01 | tax | S | Src | 2026-01-01 | pending | 2 | --tax"))
        self.assertIsNone(entries[0].revisit_date)

    def test_effective_tolerates_a_parenthetical(self):
        entries, _ = rp.parse(doc("2026-11-01 (pending) | tax | S | Src | 2026-01-01 | 2026-06-01 | 2 | --tax"))
        self.assertEqual(entries[0].effective_date, date(2026, 11, 1))

    def test_effective_rejects_ranges_and_placeholders(self):
        entries, _ = rp.parse(
            doc(
                "2025-12-06 to 2026-06-05 | tax | S | Src | 2026-01-01 | 2026-06-01 | 1 | --tax",
                header=HEADER,
            )
        )
        self.assertIsNone(entries[0].effective_date)


class TestShippedCorpus(unittest.TestCase):
    def test_the_real_file_parses_completely(self):
        entries, unparsed = rp.load()
        self.assertEqual(unparsed, [], f"{len(unparsed)} entries invisible to the schedulers")
        self.assertGreater(len(entries), 300)


if __name__ == "__main__":
    unittest.main(verbosity=2)
