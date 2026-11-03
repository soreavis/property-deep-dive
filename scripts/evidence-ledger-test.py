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

    def test_settled_lines_need_no_agent(self):
        self.assertTrue(EL.SETTLED.search("- Notary fee ~est. 500 (no tariff)"))
        self.assertTrue(EL.SETTLED.search("total (computed: 3 % + €362)"))
        self.assertFalse(EL.SETTLED.search("- Transfer tax **3 %** of price (2026 data, source vero.fi)"))


if __name__ == "__main__":
    unittest.main()
