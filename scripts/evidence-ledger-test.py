#!/usr/bin/env python3
"""Unit tests for scripts/evidence-ledger.py. Run: python3 scripts/evidence-ledger-test.py"""

from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

_spec = importlib.util.spec_from_file_location("evidence_ledger", Path(__file__).parent / "evidence-ledger.py")
EL = sys.modules["evidence_ledger"] = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(EL)

PLAYBOOK = """# FI
## Section: `--tax`
- Transfer tax **3 %** of price (2026 data, source vero.fi)
- Notary fee ~est. 500 (no tariff)
## Status
"""


class Ledger(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        (root / "countries" / "fi").mkdir(parents=True)
        (root / "countries" / "fi" / "playbook.md").write_text(PLAYBOOK)
        EL.COUNTRIES, EL.LEDGER_DIR = root / "countries", root / "ledger"
        self.result = root / "result.json"

    def tearDown(self):
        self.tmp.cleanup()

    def _add(self, items, date="2026-10-23"):
        self.result.write_text(json.dumps({"playbooks": [{"clusters": [{"items": items}]}]}))
        EL.cmd_add([self.result], date)
        return EL.load("fi")

    def item(self, new, url="https://www.vero.fi/a", status="APPLY"):
        return {"file": "skills/property-deep-dive/countries/fi/playbook.md", "new": new, "status": status,
                "evidence": [{"url": url, "fact": "3 %", "tier": "primary"}]}

    def test_line_key_ignores_whitespace(self):
        self.assertEqual(EL.line_key("a  b\t c "), EL.line_key("a b c"))

    def test_only_lines_still_in_the_playbook_are_kept(self):
        led = self._add([self.item("- Transfer tax **3 %** of price (2026 data, source vero.fi)\n- gone 9 %")])
        self.assertEqual(len(led["lines"]), 1)
        self.assertEqual(led["urls"], ["https://www.vero.fi/a"])

    def test_dropped_patches_and_items_without_evidence_are_ignored(self):
        led = self._add([self.item("- Transfer tax **3 %** of price (2026 data, source vero.fi)", status="DROP"),
                         {**self.item("- Transfer tax **3 %** of price (2026 data, source vero.fi)"), "evidence": []}])
        self.assertEqual(led["lines"], {})

    def test_newer_evidence_is_not_overwritten_by_older(self):
        line = "- Transfer tax **3 %** of price (2026 data, source vero.fi)"
        self._add([self.item(line, url="https://www.vero.fi/new")], date="2026-11-03")
        led = self._add([self.item(line, url="https://www.vero.fi/old")], date="2026-10-23")
        entry = next(iter(led["lines"].values()))
        self.assertEqual(entry["d"], "2026-11-03")
        self.assertEqual([led["urls"][i] for i in entry["u"]], ["https://www.vero.fi/new"])

    def _pages(self, text):
        return lambda urls: {u: EL.SV.FetchResult(u, "OK", text=text) for u in urls}

    def test_agent_confirmed_lines_enter_only_when_a_script_reads_them(self):
        line = "- Transfer tax **3 %** of price (2026 data, source vero.fi)"
        real = EL.fetch_all
        try:
            EL.fetch_all = self._pages("Varainsiirtovero 3 % kiinteistön kauppahinnasta.")
            self.assertEqual(EL.add_confirmed_lines("fi", [(line, ["https://www.vero.fi/a"])], "2026-12-01"), 1)
            EL.fetch_all = self._pages("No such figure on this page.")
            self.assertEqual(EL.add_confirmed_lines("fi", [(line, ["https://www.vero.fi/b"])], "2026-12-01"), 0)
            self.assertEqual(EL.add_confirmed_lines("fi", [("- a line not in the playbook 5 %", ["https://x"])], "2026-12-01"), 0)
        finally:
            EL.fetch_all = real

    def test_inline_urls_are_the_fallback_evidence(self):
        self.assertEqual(EL.inline_urls("rate 3 % (source `https://www.vero.fi/x`)"), ["https://www.vero.fi/x"])

    def test_named_sources_resolve_through_the_source_table(self):
        lines = [("", "## Source URL templates"), ("", "| Source | URL |"), ("", "|---|---|"),
                 ("", "| **Destatis** HPI | `https://www.destatis.de/hpi` |"), ("", "## Status")]
        named = EL.named_sources(lines)
        self.assertEqual(named, [("Destatis", "https://www.destatis.de/hpi")])
        self.assertEqual(EL.candidate_urls("index +3.1 % (2026 data, source Destatis)", named), ["https://www.destatis.de/hpi"])
        self.assertEqual(EL.candidate_urls("index +3.1 % (source destatistics blog)", named), [])

    def test_settled_lines_need_no_agent(self):
        self.assertTrue(EL.SETTLED.search("- Notary fee ~est. 500 (no tariff)"))
        self.assertTrue(EL.SETTLED.search("total (computed: 3 % + €362)"))
        self.assertFalse(EL.SETTLED.search("- Transfer tax **3 %** of price (2026 data, source vero.fi)"))


if __name__ == "__main__":
    unittest.main()
