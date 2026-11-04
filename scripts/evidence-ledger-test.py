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
        self.real_fetch = EL.fetch_all
        EL.fetch_all = self._pages("Varainsiirtovero 3 % kiinteistön kauppahinnasta.")

    def tearDown(self):
        EL.fetch_all = self.real_fetch
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
        led = self._add([self.item(self.LINE + "\n- gone 9 %")])
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

    LINE = "- Transfer tax **3 %** of price (2026 data, source vero.fi)"
    RULE = "- Rule of Art. 11 in force 7 Aug 2026, rate 3 %"
    SCATTERED = "Art. 11: siirtovero 3 %" + " x" * 2000 + " 7 Aug 2026"

    def test_agent_confirmed_lines_enter_with_the_fingerprint_of_a_page_showing_them(self):
        self.assertEqual(EL.add_confirmed_lines("fi", [(self.LINE, ["https://www.vero.fi/a"])], "2026-12-01"), 1)
        self.assertTrue(EL.load("fi")["lines"][EL.line_key(self.LINE)]["h"])

    def test_a_shell_page_or_a_line_gone_from_the_playbook_stays_out(self):
        EL.fetch_all = self._pages("Please enable JavaScript to view this site.")
        self.assertEqual(EL.add_confirmed_lines("fi", [(self.LINE, ["https://www.vero.fi/b"])], "2026-12-01"), 0)
        self.assertEqual(EL.add_confirmed_lines("fi", [("- a line not in the playbook 5 %", ["https://x"])], "2026-12-01"), 0)

    def _confirmed_on(self, page, line=LINE, proved="2026-10-01", today="2026-11-01"):
        """Ledger the line against one page version, then re-check it against `page`."""
        (EL.COUNTRIES / "fi" / "playbook.md").write_text(f"# FI\n## Section: `--tax`\n{line}\n## Status\n")
        EL.fetch_all = self._pages(self.SCATTERED)
        EL.add_confirmed_lines("fi", [(line, ["https://www.vero.fi/a"])], proved)
        EL.fetch_all = self._pages(page)
        return EL.check("fi", touch_date=today)

    def test_an_unchanged_page_confirms_a_line_whose_figures_cannot_be_read_together(self):
        res = self._confirmed_on(self.SCATTERED, self.RULE)
        self.assertEqual((res["confirmed"], res["unchanged"]), (1, 1))
        self.assertEqual(next(iter(EL.load("fi")["lines"].values()))["d"], "2026-10-01")

    def test_a_changed_page_sends_the_line_back_to_an_agent(self):
        res = self._confirmed_on("A new text with nothing in common", self.RULE)
        self.assertEqual(res["confirmed"], 0)

    def test_an_unchanged_page_stops_counting_after_a_year(self):
        res = self._confirmed_on(self.SCATTERED, self.RULE, proved="2025-10-01", today="2026-11-01")
        self.assertEqual(res["unchanged"], 0)

    def _ledgered_without_fingerprint(self, proved):
        (EL.COUNTRIES / "fi" / "playbook.md").write_text(f"# FI\n## Section: `--tax`\n{self.RULE}\n## Status\n")
        led = EL.load("fi")
        EL.put(led, EL.line_key(self.RULE), ["https://www.vero.fi/a"], proved)
        EL.save("fi", led)

    def test_a_recent_proof_is_skipped_unless_audited_and_keeps_its_date(self):
        self._ledgered_without_fingerprint("2026-10-23")
        EL.fetch_all = self._pages(self.SCATTERED)
        real, EL.in_audit_sample = EL.in_audit_sample, lambda *_: False
        try:
            res = EL.check("fi", touch_date="2026-11-04", max_risk=0.10)
            self.assertEqual((len(res["fresh"]), res["worklist"]), (1, []))
            self.assertEqual(res["fresh"][0]["proved"], "2026-10-23")
            entry = EL.load("fi")["lines"][EL.line_key(self.RULE)]
            self.assertEqual(entry["d"], "2026-10-23")
            self.assertTrue(entry["h"])
            EL.in_audit_sample = lambda *_: True
            self._ledgered_without_fingerprint("2026-10-23")
            self.assertTrue(EL.check("fi", touch_date="2026-11-04", max_risk=0.10)["worklist"][0]["audit"])
        finally:
            EL.in_audit_sample = real

    def test_an_old_proof_or_a_changed_page_is_not_fresh(self):
        self._ledgered_without_fingerprint("2026-01-01")
        EL.fetch_all = self._pages(self.SCATTERED)
        self.assertEqual(EL.check("fi", max_risk=0.10, touch_date="2026-11-04")["fresh"], [])
        self.assertFalse(EL.freshly_proved({"d": "2026-11-01", "h": "old"}, ["https://x"], EL.fetch_all(["https://x"]), "2026-11-04", 0.10))

    def test_a_forward_looking_date_now_past_is_stale_whatever_the_figures_say(self):
        self.assertEqual(EL.expired_promise("next rate meeting 12 Nov 2026", "2026-12-01"), "2026-11-12")
        self.assertEqual(EL.expired_promise("will apply from 2026-01-01", "2026-12-01"), "2026-01-01")
        self.assertIsNone(EL.expired_promise("next rate meeting 12 Nov 2026", "2026-11-04"))
        self.assertIsNone(EL.expired_promise("in force since 12 Nov 2020", "2026-11-04"))
        line = "- Key rate 3 %, next meeting 12 Nov 2026"
        res = self._confirmed_on("Key rate 3 %, next meeting 12 Nov 2026", line, today="2026-12-01")
        self.assertEqual((res["confirmed"], res["worklist"][0]["expired"]), (0, "2026-11-12"))

    def test_hints_rank_the_passage_holding_the_figure_first(self):
        fetches = {"https://a": EL.SV.FetchResult("https://a", "OK", text="Kirchberg asunnot 11 161 euroa " + "muu " * 400),
                   "https://b": EL.SV.FetchResult("https://b", "OK", text="Kirchberg average 12,542 per square metre")}
        row = {"line": "- **Kirchberg**: €12,542/m²"}
        EL.add_hints([row], fetches)
        self.assertEqual(row["hints"][0]["url"], "https://b")

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
