#!/usr/bin/env python3
"""Unit tests for scripts/maintain.py footer logic. Run: python3 scripts/maintain-test.py"""

from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

_spec = importlib.util.spec_from_file_location("maintain", Path(__file__).parent / "maintain.py")
M = sys.modules["maintain"] = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(M)
CP = M._load("check_playbooks", "check-playbooks.py")

HEAD = """# XX
## Section: `--price`
p
## Section: `--tax`
t
## Section: `--traffic`
x
## Cost benchmarks (XX 2026)
c
## Status

✅ **Fully populated** (initial population as of 2026-04-25).
**Confidence**: MEDIUM.
"""
TABLE = """
### Per-section verification (overrides playbook-level date)

| Section | Last verified | Verifier | Notes |
|---|---|---|---|
| `--price` (benchmarks) | 2026-10-23 | refresh wave | old note |
"""
HISTORY_SECTION = "\n## Extension TODOs\n\n- [ ] x\n\n## Update history\n\n- **2026-04-25** — Initial population\n"
HISTORY_BOLD = "**Update history**:\n\n- **2026-04-25** — Initial population\n"


def row(name, d="2026-12-01"):
    return f"| {name} | {d} | {d} maintenance run | n |"


class FastKeys(unittest.TestCase):
    def test_leading_token_decides(self):
        self.assertEqual(M.fast_key("`--rental` / Tax on rental"), "rental")
        self.assertEqual(M.fast_key("Section: `--work=<profession>`"), "work")
        self.assertEqual(M.fast_key("Cost benchmarks (FI 2026)"), "cost benchmark")
        self.assertIsNone(M.fast_key("`--traffic`"))

    def test_fast_sections_skip_status(self):
        self.assertEqual(list(M.fast_sections(HEAD)), ["price", "tax", "cost benchmark"])


class Packing(unittest.TestCase):
    def test_clusters_merge_up_to_the_cap_and_big_ones_stay_alone(self):
        c = lambda n, s: {"sections": [s], "lines": [{}] * n}
        packed = M.pack({"market": c(30, "a"), "tax-legal": c(8, "b"), "risk-infra": c(5, "c")})
        self.assertEqual({k: len(v["lines"]) for k, v in packed.items()}, {"market+tax-legal": 38, "risk-infra": 5})
        self.assertEqual(packed["market+tax-legal"]["sections"], ["a", "b"])


class Hold(unittest.TestCase):
    def test_a_patch_with_an_untraceable_figure_stays_out_and_its_section_stays_open(self):
        page = M.SV.FetchResult("https://x", "OK", text="Stopa 2,5 %" + " tekst bez brojeva" * 30)
        real, M.EL.fetch_all = M.EL.fetch_all, lambda urls: {"https://x": page}
        good = {"file": "a", "section": "Section: `--tax`", "old": "- x", "new": "- Tax 2.5%", "kind": "fact-changed",
                "evidence": [{"url": "https://x", "fact": "f"}]}
        bad = {**good, "section": "Section: `--price`", "new": "- Price €9,999"}
        res = {"playbooks": [{"clusters": [{"items": [good, bad], "sections": [
            {"section": "Section: `--tax`", "closed": True}, {"section": "Section: `--price`", "closed": True}]}]}]}
        try:
            kept, held = M.hold_ungrounded(res, [good, bad])
        finally:
            M.EL.fetch_all = real
        self.assertEqual((kept, [h["new"] for h in held]), ([good], ["- Price €9,999"]))
        self.assertEqual([s["closed"] for s in res["playbooks"][0]["clusters"][0]["sections"]], [True, False])
        M.EL.fetch_all = lambda urls: {"https://x": page}
        try:
            self.assertEqual(M.hold_ungrounded(res, [{**bad, "flag_cleared": True}])[1], [])
        finally:
            M.EL.fetch_all = real


class OpenSections(unittest.TestCase):
    PLAYBOOK = "# X\n## Section: `--tax`\n- a\n## Status\n"

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        (root / "countries" / "fi").mkdir(parents=True)
        (root / "countries" / "fi" / "playbook.md").write_text(self.PLAYBOOK)
        self.real = M.EL.COUNTRIES, M.EL.LEDGER_DIR
        M.EL.COUNTRIES, M.EL.LEDGER_DIR = root / "countries", root / "ledger"

    def tearDown(self):
        M.EL.COUNTRIES, M.EL.LEDGER_DIR = self.real
        self.tmp.cleanup()

    def test_an_objection_survives_in_the_ledger_and_returns_to_an_agent_until_closed(self):
        M.record_open_sections("fi", [{"section": "Section: `--tax`", "closed": False, "objection": "citation not on the page"}])
        clusters = {}
        M.add_open_sections("fi", clusters)
        self.assertEqual(clusters["tax-legal"]["sections"], ["`--tax`"])
        self.assertIn("citation not on the page", clusters["tax-legal"]["pending"][0]["request"])
        M.record_open_sections("fi", [{"section": "Section: `--tax`", "closed": True}])
        self.assertEqual(M.EL.load("fi").get("open", {}), {})


class RequestQueue(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.real, M.REQUESTS = M.REQUESTS, Path(self.tmp.name) / "q.json"

    def tearDown(self):
        M.REQUESTS = self.real
        self.tmp.cleanup()

    def test_unconfirmed_batch_items_and_new_requests_are_kept(self):
        res = {"playbooks": [{"clusters": [
            {"cluster": "shared", "items": [], "sections": [
                {"section": "CA row", "closed": False, "note": "n", "remaining": ["minister statement"]},
                {"section": "BE row", "closed": False, "note": "no primary source"},
                {"section": "FI row", "closed": True, "note": "ok"}]},
            {"cluster": "market", "items": [], "sections": [{"section": "`--tax`", "closed": False, "note": "x"}],
             "shared_requests": [{"file": "shared/finance.md", "request": "add a row"}]}]}]}
        self.assertEqual({r["request"] for r in M.leftovers(res)}, {"minister statement", "no primary source", "add a row"})

    def test_a_settled_request_leaves_the_queue_and_repeats_merge(self):
        one = {"target": "a", "request": "r1", "evidence": ""}
        M.queue_requests([one, {**one, "request": "r2"}])
        M.queue_requests([one])
        self.assertEqual(len(M.load_requests()), 2)
        M.queue_requests([], {"r1"})
        self.assertEqual([r["request"] for r in M.load_requests()], ["r2"])

    def test_the_queue_becomes_batches_for_the_workflow(self):
        M.queue_requests([{"target": "a", "request": f"r{i}", "evidence": ""} for i in range(M.REQUEST_BATCH + 1)])
        out = Path(self.tmp.name) / "out"
        M.cmd_requests(out)
        plan = json.loads((out / "plan.json").read_text())
        self.assertEqual([(p["code"], p["lines"], p["batch"]) for p in plan], [("shared-01", M.REQUEST_BATCH, True), ("shared-02", 1, True)])


class Restatements(unittest.TestCase):
    ITEM = {"file": "x", "old": "- **Belair**: €14,489/m²", "new": "- **Belair**: €12,951/m²"}

    def test_a_rounded_restatement_of_a_replaced_figure_is_found(self):
        text = "| LU-City Belair €/m² | ~€14,500 |\n- Limpertsberg €14,500\n- **Belair**: €12,951/m²"
        self.assertEqual([f["line"] for f in M.restatements([self.ITEM], text)], ["| LU-City Belair €/m² | ~€14,500 |"])

    def test_roundings_keep_two_significant_digits(self):
        self.assertEqual(M.roundings(14489), {14489, 14490, 14500, 14000})


class Footer(unittest.TestCase):
    def test_reader_note_drops_sentences_about_the_run(self):
        note = "All 3 worklist lines are patched. IFON enters into force on 1 Jan 2029. Each old string occurs once."
        self.assertEqual(M.reader_note(note), "IFON enters into force on 1 Jan 2029.")
        self.assertEqual(M.reader_note("All worklist lines closed."), M.DEFAULT_NOTE)

    def test_a_subsection_row_does_not_date_the_section(self):
        table = "### Per-section verification\n\n| Section | Last verified | Verifier | Notes |\n|---|---|---|---|\n" \
                "| `--price` › Listings | 2026-10-23 | w | n |\n| `--tax` | 2026-10-23 | w | n |\n"
        self.assertEqual(M.section_dates(table), {"tax": "2026-10-23"})

    def test_table_created_when_missing_and_rows_upserted(self):
        t = M.upsert_rows(HEAD + HISTORY_SECTION, {"tax": row("`--tax`")})
        self.assertIn(M.TABLE_HEAD, t)
        self.assertLess(t.index(M.TABLE_HEAD), t.index("## Extension TODOs"))
        t = M.upsert_rows(HEAD + TABLE, {"price": row("`--price`")})
        self.assertNotIn("old note", t)
        self.assertEqual(t.count("| `--price`"), 1)

    def test_restamp_uses_oldest_section_date_only_when_all_dated(self):
        t = M.upsert_rows(HEAD + TABLE, {"tax": row("`--tax`")})
        self.assertIsNone(M.restamp(t)[1])  # cost benchmarks undated
        t = M.upsert_rows(t, {"cost benchmark": row("Cost benchmarks (XX 2026)")})
        t, d = M.restamp(t)
        self.assertEqual(d, "2026-10-23")  # --price is the oldest
        self.assertTrue(t.split("## Status")[1].lstrip("\n").startswith("✅ Fast-changing sections re-verified as of 2026-10-23"))
        self.assertEqual(CP.restamp_errors(t), [])  # the CI lint agrees

    def test_restamp_never_moves_backwards(self):
        t = HEAD.replace("as of 2026-04-25", "as of 2026-11-30") + TABLE
        t = M.upsert_rows(t, {"tax": row("`--tax`"), "cost benchmark": row("Cost benchmarks (XX 2026)")})
        self.assertIsNone(M.restamp(t)[1])

    def test_history_goes_where_the_playbook_keeps_it(self):
        t = M.add_history(HEAD + HISTORY_SECTION, "- **2026-12-01** — run")
        self.assertTrue(t.rstrip().endswith("- **2026-12-01** — run"))
        t = M.add_history(HEAD + HISTORY_BOLD + TABLE, "- **2026-12-01** — run")
        self.assertLess(t.index("2026-12-01** — run"), t.index("### Per-section"))
        t = M.add_history(HEAD, "- **2026-12-01** — run")
        self.assertIn("## Update history\n\n- **2026-12-01** — run", t)


if __name__ == "__main__":
    unittest.main()
