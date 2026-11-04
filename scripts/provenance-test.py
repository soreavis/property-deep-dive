#!/usr/bin/env python3
"""Unit tests for scripts/provenance.py. Run: python3 scripts/provenance-test.py"""

from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

_spec = importlib.util.spec_from_file_location("provenance", Path(__file__).parent / "provenance.py")
P = sys.modules["provenance"] = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(P)

PAD = " Lorem ipsum dolor sit amet." * 10


def page(text):
    return P.EL.SV.FetchResult("https://x", "OK", text=text + PAD)


def patch(new, old="- old line", url="https://x", **evidence):
    return {"old": old, "new": new, "evidence": [{"url": url, "fact": "f", **evidence}]}


class Numbers(unittest.TestCase):
    def test_a_printed_number_keeps_both_readings(self):
        self.assertEqual(P.readings("12.951"), [12.951, 12951.0])
        self.assertEqual(P.readings("3,067.75"), [3067.75, 306775.0])

    def test_rounding_interval_is_half_a_unit_of_the_last_digit(self):
        self.assertEqual(P.rounding_interval("85", 1000), [(84500.0, 85500.0)])


class Gate(unittest.TestCase):
    def audit(self, new, text, **kw):
        return P.audit_patch(patch(new, **kw), {"https://x": page(text)})

    def test_a_rounded_figure_is_grounded_by_the_exact_one(self):
        self.assertEqual(self.audit("- Price €85k", "Cena 85.200 eura")["status"], "CLEAN")

    def test_a_transposed_figure_is_a_near_miss_naming_the_real_one(self):
        f = self.audit("- Price €12,591/m²", "Prix moyen 12 951 euros")["findings"][0]
        self.assertEqual((f["kind"], f["page_has"]), ("near miss", ["12951"]))

    def test_one_wrong_digit_is_a_near_miss(self):
        self.assertEqual(self.audit("- Fee €3,467", "Tarif 3,067 euros")["findings"][0]["kind"], "near miss")

    def test_an_invented_figure_is_ungrounded(self):
        self.assertEqual(self.audit("- Tax 7.7%", "Stopa 2,5 %")["findings"][0]["kind"], "ungrounded")

    def test_a_figure_already_in_the_old_line_is_not_new(self):
        self.assertEqual(self.audit("- Tax 7.7% (2026 data)", "x", old="- Tax 7.7%")["status"], "CLEAN")

    def test_a_computed_figure_must_be_derivable_from_its_line(self):
        ok = "- RSD 10,000,000 at 117.37 is ~€85,200 (computed)"
        self.assertEqual(self.audit(ok, "kurs dinara")["findings"], [])
        self.assertEqual(self.audit("- RSD 10 at 2 is ~€85,200 (computed)", "kurs")["findings"][0]["kind"], "underived")

    def test_a_missing_figure_is_not_flagged_while_a_page_went_unread(self):
        item = {"old": "", "new": "- Tax 7.7%", "evidence": [{"url": "https://x"}, {"url": "https://y"}]}
        self.assertEqual(P.audit_patch(item, {"https://x": page("Stopa 2,5 %")})["findings"], [])

    def test_no_readable_page_is_unverifiable(self):
        self.assertEqual(P.audit_patch(patch("- Tax 7.7%"), {})["status"], "UNVERIFIABLE")

    def test_a_quote_must_stand_on_the_page(self):
        text = "Porez na prenos apsolutnih prava iznosi dva i po procenta od kupoprodajne cene nepokretnosti"
        self.assertEqual(self.audit("- none", text, quote=text[:70])["findings"], [])
        bad = self.audit("- none", text, quote="Porez je ukinut za sve kupce prve nekretnine od januara ove godine")
        self.assertEqual(bad["findings"][0]["kind"], "quote not on page")


if __name__ == "__main__":
    unittest.main()
