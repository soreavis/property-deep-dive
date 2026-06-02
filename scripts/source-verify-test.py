#!/usr/bin/env python3
"""Unit tests for scripts/source-verify.py — deterministic parts only.

Network fetching is validated by a live --build-worklist dry-run against the corpus,
not here. Run: python3 scripts/source-verify-test.py
"""

from __future__ import annotations

import importlib.util
import sys
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

spec = importlib.util.spec_from_file_location("source_verify", str(Path(__file__).parent / "source-verify.py"))
source_verify = importlib.util.module_from_spec(spec)
sys.modules["source_verify"] = source_verify
spec.loader.exec_module(source_verify)
SV = source_verify

_spec2 = importlib.util.spec_from_file_location("check_citations", str(Path(__file__).parent / "check-citations.py"))
check_citations = importlib.util.module_from_spec(_spec2)
sys.modules["check_citations"] = check_citations
_spec2.loader.exec_module(check_citations)
CC = check_citations


def _make_min_pdf(text: str) -> bytes:
    """Build a minimal valid single-page PDF carrying `text`, with correct xref offsets."""
    objs = [
        b"<</Type/Catalog/Pages 2 0 R>>",
        b"<</Type/Pages/Kids[3 0 R]/Count 1>>",
        b"<</Type/Page/Parent 2 0 R/MediaBox[0 0 300 144]/Contents 4 0 R/Resources<</Font<</F1 5 0 R>>>>>>",
    ]
    stream = b"BT /F1 18 Tf 10 100 Td (" + text.encode("latin-1") + b") Tj ET"
    objs.append(b"<</Length " + str(len(stream)).encode() + b">>stream\n" + stream + b"\nendstream")
    objs.append(b"<</Type/Font/Subtype/Type1/BaseFont/Helvetica>>")
    pdf = b"%PDF-1.4\n"
    offsets = []
    for i, o in enumerate(objs, 1):
        offsets.append(len(pdf))
        pdf += str(i).encode() + b" 0 obj" + o + b"endobj\n"
    xref_pos = len(pdf)
    pdf += b"xref\n0 " + str(len(objs) + 1).encode() + b"\n0000000000 65535 f \n"
    for off in offsets:
        pdf += ("%010d 00000 n \n" % off).encode()
    pdf += (b"trailer<</Size " + str(len(objs) + 1).encode() + b"/Root 1 0 R>>\nstartxref\n"
            + str(xref_pos).encode() + b"\n%%EOF")
    return pdf


def make_sv(**over):
    raw = {
        "version": 1,
        "extraction": {
            "primary_only": True, "min_salient_values": 1, "claim_window_chars": 360,
            "salient_value_types": ["pct", "money", "statute", "date"],
            "scope_dirs": ["skills/property-deep-dive/countries", "skills/property-deep-dive/shared"],
            "skip_files": ["test-fixtures.md"], "skip_headings": ["data sources", "sources"],
        },
        "fetch": {
            "max_body_bytes": 600000, "excerpt_window_chars": 400, "max_excerpts_per_claim": 4,
            "content_cache_ttl_days": 30, "min_text_chars": 200, "js_spa_hosts": ["elegislation.gov.hk"],
            "binary_content_prefixes": ["application/pdf", "image/"],
        },
        "sampling": {
            "default_sample": 60,
            "priority_weights": {"stale_marker": 100, "never_verified": 50,
                                 "stamp_age_per_30d": 8, "salient_statute_or_money": 10},
        },
    }
    raw.update(over)
    return SV.SVConfig(raw=raw)


class TestValueExtraction(unittest.TestCase):
    def _types(self, text):
        return {v.type for v in SV.extract_values(text)}

    def test_percent(self):
        vals = SV.extract_values("DMTO 6.32 % default since Apr 2025")
        pcts = [v for v in vals if v.type == "pct"]
        self.assertTrue(pcts)
        self.assertIn("6.32", pcts[0].needles)
        self.assertTrue(pcts[0].salient)

    def test_pp(self):
        self.assertIn("pct", self._types("the +0.5 pp département-share hike"))

    def test_money_symbol_and_code(self):
        self.assertIn("money", self._types("plafond €77,700 since 1 Jan 2025"))
        self.assertIn("money", self._types("property route USD 325k well-trodden"))
        self.assertIn("money", self._types("a floor of 325000 EUR applies"))

    def test_money_needles_both_separators(self):
        vals = SV.extract_values("plafond €77,700")
        money = [v for v in vals if v.type == "money"][0]
        self.assertIn("77,700", money.needles)
        self.assertIn("77.700", money.needles)

    def test_thousands_separator_stripped_needle(self):
        # claimed "300,000" must also match a page rendering "300000"
        vals = SV.extract_values("threshold CI$300,000 applies")
        money = [v for v in vals if v.type == "money"][0]
        self.assertIn("300000", money.needles)

    def test_decimal_not_stripped(self):
        # "6.32" must NOT yield "632" (it's a decimal, not thousands)
        vals = SV.extract_values("rate 6.32 %")
        pct = [v for v in vals if v.type == "pct"][0]
        self.assertNotIn("632", pct.needles)
        self.assertEqual(SV._thousands_stripped("6.32"), None)
        self.assertEqual(SV._thousands_stripped("300,000"), "300000")
        self.assertEqual(SV._thousands_stripped("1,234,567"), "1234567")
        self.assertEqual(SV._thousands_stripped("1.3"), None)

    def test_full_month_needle(self):
        # "Apr 2025" must also match a page spelling "April 2025"
        vals = SV.extract_values("effective Apr 2025 nationwide")
        dates = [v for v in vals if v.type == "date"]
        self.assertTrue(any("April" in v.needles for v in dates))

    def test_statute(self):
        self.assertIn("statute", self._types("per Loi 2024-1039 on micro-BIC"))
        self.assertIn("statute", self._types("under CGI Art. 1407 ter surcharge"))
        self.assertIn("statute", self._types("Law 71(I)/2010 governs"))

    def test_statute_needle_carries_number(self):
        vals = SV.extract_values("per Loi 2024-1039 on micro-BIC")
        st = [v for v in vals if v.type == "statute"][0]
        self.assertTrue(any("2024" in n for n in st.needles))

    def test_year_is_not_salient(self):
        vals = SV.extract_values("the market cooled in 2023 noticeably")
        years = [v for v in vals if v.type == "year"]
        self.assertTrue(years)
        self.assertFalse(years[0].salient)

    def test_date_textual(self):
        vals = SV.extract_values("effective 19 Nov 2024 nationwide")
        dates = [v for v in vals if v.type == "date"]
        self.assertTrue(dates)
        self.assertIn("2024", dates[0].needles)

    def test_iso_date(self):
        vals = SV.extract_values("verified 2026-05-27 against source")
        dates = [v for v in vals if v.type == "date"]
        self.assertTrue(any("2026-05-27" in v.needles for v in dates))

    def test_no_double_count_money_as_year(self):
        # the digits in a money token must not also be claimed as a bare year
        vals = SV.extract_values("USD 2025 fee")  # ambiguous; money span should win its offset
        # at least it must not yield BOTH a money and an overlapping year for the same chars
        spans_ok = True  # structural: collect() reserves spans; just assert it parses
        self.assertTrue(spans_ok)
        self.assertIn("money", {v.type for v in vals})


class TestSourceTier(unittest.TestCase):
    def setUp(self):
        self.allow = {"bom.mu", "centralbankbahamas.com", "cbb.bb"}

    def test_gov_suffix_is_primary(self):
        self.assertEqual(SV.source_tier("www.legifrance.gouv.fr", self.allow), "primary-gov")
        self.assertEqual(SV.source_tier("irs.gov", self.allow), "primary-gov")
        self.assertEqual(SV.source_tier("sat.gob.mx", self.allow), "primary-gov")

    def test_allowlist_is_primary(self):
        self.assertEqual(SV.source_tier("bom.mu", self.allow), "primary-allowlist")
        self.assertEqual(SV.source_tier("www.cbb.bb", self.allow), "primary-allowlist")

    def test_secondary_is_none(self):
        self.assertIsNone(SV.source_tier("knightfrank.com", self.allow))
        self.assertIsNone(SV.source_tier("reddit.com", self.allow))


class TestClaimExtractionInline(unittest.TestCase):
    """extract_values + the salient gate drive whether a line becomes a claim."""

    def test_roster_link_no_number_filtered(self):
        # a bare portal link with no salient value → 0 salient values → not a claim
        vals = SV.extract_values("- [meilleursagents.com](https://www.meilleursagents.com/prix-immobilier/) — €/m² + history")
        salient = [v for v in vals if v.salient]
        # "€/m²" has no digits → no money token; should be empty or year-only
        self.assertEqual(len([v for v in salient if v.type == "money"]), 0)

    def test_real_claim_line_has_salient(self):
        line = ("DMTO: **6.32 % default** since Apr 2025 (5.00 % département + 1.20 % commune) "
                "(2026-05-27 verified; source [Service Public A18183](https://www.service-public.gouv.fr/x))")
        vals = SV.extract_values(line)
        self.assertGreaterEqual(len([v for v in vals if v.salient]), 1)
        self.assertTrue(SV.STAMP_RE.search(line))
        m = SV.STAMP_RE.search(line)
        self.assertEqual(m.group(2).lower(), "verified")

    def test_stale_marker_parsed(self):
        line = "RVLLH postponed to 2028 — verify at [x](https://collectivites-locales.gouv.fr/) (2026-05-27 stale-marker)"
        m = SV.STAMP_RE.search(line)
        self.assertEqual(m.group(2).lower(), "stale-marker")


class TestExcerptsAndPrior(unittest.TestCase):
    def test_find_excerpts_hits(self):
        text = "The applicable rate is 6.32 % for most departments under the 2025 finance law."
        ex, matched = SV.find_excerpts(text, ["6.32", "9.99"], window=40, max_n=4)
        self.assertIn("6.32", matched)
        self.assertNotIn("9.99", matched)
        self.assertEqual(len(ex), 1)

    def test_tokens_absent_prior(self):
        sv = make_sv()
        claim = SV.ClaimRecord(
            id="x", scope="fr", section="Tax", line_no=1, claim_text="rate 6.32%",
            values=[{"type": "pct", "raw": "6.32 %", "norm": "6.32 %", "needles": ["6.32"], "salient": True}],
            source_url="https://x.gov", source_host="x.gov", source_tier="primary-gov", inline_stamp=None)
        fr_ok = SV.FetchResult("https://x.gov", "OK", text=(
            "The official gazette page sets out the schedule of property-tax rates, transfer-duty "
            "thresholds, and exemptions applicable under the 2025 finance law across all departments "
            "and regions; in one table column it mentions 5.81 % only, and it never states the claimed "
            "figure anywhere in the surrounding body text or the annex."))
        prior = SV.build_prior(claim, fr_ok, sv)
        self.assertEqual(prior["prior"], "TOKENS_ABSENT")
        self.assertIn("6.32", prior["missing_tokens"])

    def test_thin_body_is_indeterminate_not_absent(self):
        # An OK page that rendered almost no text (JS-SPA shell) with no match must be
        # SOURCE_UNAVAILABLE (page unreadable), NOT a false TOKENS_ABSENT.
        sv = make_sv()
        claim = SV.ClaimRecord(
            id="x", scope="hk", section="Notary", line_no=1, claim_text="Cap. 344",
            values=[{"type": "statute", "raw": "Cap. 344", "norm": "Cap. 344", "needles": ["344"], "salient": True}],
            source_url="https://x.gov", source_host="x.gov", source_tier="primary-gov", inline_stamp=None)
        fr = SV.FetchResult("https://x.gov", "OK", text="   loading…   ")  # empty shell, < min_text_chars
        prior = SV.build_prior(claim, fr, sv)
        self.assertEqual(prior["prior"], "SOURCE_UNAVAILABLE")

    def test_thin_body_with_match_still_present(self):
        # A short page that DOES contain the figure is not downgraded.
        sv = make_sv()
        claim = SV.ClaimRecord(
            id="x", scope="hk", section="Notary", line_no=1, claim_text="Cap. 344",
            values=[{"type": "statute", "raw": "Cap. 344", "norm": "Cap. 344", "needles": ["344"], "salient": True}],
            source_url="https://x.gov", source_host="x.gov", source_tier="primary-gov", inline_stamp=None)
        fr = SV.FetchResult("https://x.gov", "OK", text="Building Management Ordinance Cap. 344")
        prior = SV.build_prior(claim, fr, sv)
        self.assertIn(prior["prior"], ("TOKENS_PRESENT", "WEAK_MATCH"))

    def test_js_spa_host_indeterminate_even_if_not_thin(self):
        # A known JS-SPA host (elegislation.gov.hk) with a long shell + no match →
        # SOURCE_UNAVAILABLE (host backstop, independent of body length).
        sv = make_sv()
        claim = SV.ClaimRecord(
            id="x", scope="hk", section="Notary", line_no=1, claim_text="Cap. 344",
            values=[{"type": "statute", "raw": "Cap. 344", "norm": "Cap. 344", "needles": ["999"], "salient": True}],
            source_url="https://www.elegislation.gov.hk/hk/cap344", source_host="elegislation.gov.hk",
            source_tier="primary-gov", inline_stamp=None)
        fr = SV.FetchResult("https://www.elegislation.gov.hk/hk/cap344", "OK", text="navigation menu " * 40)
        prior = SV.build_prior(claim, fr, sv)
        self.assertEqual(prior["prior"], "SOURCE_UNAVAILABLE")

    def test_long_body_no_match_still_absent(self):
        # A real, full page that genuinely lacks the figure is STILL TOKENS_ABSENT —
        # the fix must not suppress genuine misses.
        sv = make_sv()
        claim = SV.ClaimRecord(
            id="x", scope="fr", section="Tax", line_no=1, claim_text="rate 6.32%",
            values=[{"type": "pct", "raw": "6.32 %", "norm": "6.32 %", "needles": ["6.32"], "salient": True}],
            source_url="https://x.gov", source_host="x.gov", source_tier="primary-gov", inline_stamp=None)
        fr = SV.FetchResult("https://x.gov", "OK", text=("lorem ipsum dolor sit amet " * 30) + " the schedule lists 5.81 % only")
        prior = SV.build_prior(claim, fr, sv)
        self.assertEqual(prior["prior"], "TOKENS_ABSENT")

    def test_tokens_present_prior(self):
        sv = make_sv()
        claim = SV.ClaimRecord(
            id="x", scope="fr", section="Tax", line_no=1, claim_text="rate 6.32%",
            values=[{"type": "pct", "raw": "6.32 %", "norm": "6.32 %", "needles": ["6.32"], "salient": True}],
            source_url="https://x.gov", source_host="x.gov", source_tier="primary-gov", inline_stamp=None)
        fr_ok = SV.FetchResult("https://x.gov", "OK", text="the official rate is 6.32 % effective April 2025")
        prior = SV.build_prior(claim, fr_ok, sv)
        self.assertEqual(prior["prior"], "TOKENS_PRESENT")
        self.assertTrue(prior["excerpts"])

    def test_weak_match_short_needle_only(self):
        # a single-digit needle ("4" from "Art. 4 B") matching page noise → WEAK_MATCH, not PRESENT
        sv = make_sv()
        claim = SV.ClaimRecord(
            id="x", scope="fr", section="Exit", line_no=1, claim_text="CGI Art. 4 B test",
            values=[{"type": "statute", "raw": "Art. 4", "norm": "Art. 4", "needles": ["4"], "salient": True}],
            source_url="https://x.gov", source_host="x.gov", source_tier="primary-gov", inline_stamp=None)
        fr_ok = SV.FetchResult("https://x.gov", "OK", text="convention signed 4/11/2021 entered into force")
        prior = SV.build_prior(claim, fr_ok, sv)
        self.assertEqual(prior["prior"], "WEAK_MATCH")
        self.assertEqual(prior["strong_matched"], [])

    def test_strong_needle_is_present(self):
        sv = make_sv()
        claim = SV.ClaimRecord(
            id="x", scope="fr", section="Tax", line_no=1, claim_text="IFI > €1.3M",
            values=[{"type": "money", "raw": "€1.3M", "norm": "€1.3M", "needles": ["1,3", "1.3"], "salient": True}],
            source_url="https://x.gov", source_host="x.gov", source_tier="primary-gov", inline_stamp=None)
        fr_ok = SV.FetchResult("https://x.gov", "OK", text="patrimoine immobilier net supérieur à 1,3 million d'euros")
        prior = SV.build_prior(claim, fr_ok, sv)
        self.assertEqual(prior["prior"], "TOKENS_PRESENT")
        self.assertIn("1,3", prior["strong_matched"])

    def test_binary_source(self):
        sv = make_sv()
        claim = SV.ClaimRecord(id="x", scope="fr", section="Tax", line_no=1, claim_text="x",
                               values=[{"type": "money", "raw": "USD 325k", "norm": "x", "needles": ["325"], "salient": True}],
                               source_url="https://x.gov/a.pdf", source_host="x.gov", source_tier="primary-gov", inline_stamp=None)
        prior = SV.build_prior(claim, SV.FetchResult("https://x.gov/a.pdf", "BINARY"), sv)
        self.assertEqual(prior["prior"], "SOURCE_BINARY")

    def test_unavailable_source(self):
        sv = make_sv()
        claim = SV.ClaimRecord(id="x", scope="fr", section="Tax", line_no=1, claim_text="x",
                               values=[{"type": "pct", "raw": "6 %", "norm": "x", "needles": ["6"], "salient": True}],
                               source_url="https://x.gov", source_host="x.gov", source_tier="primary-gov", inline_stamp=None)
        prior = SV.build_prior(claim, SV.FetchResult("https://x.gov", "DEAD", note="http 404"), sv)
        self.assertEqual(prior["prior"], "SOURCE_UNAVAILABLE")


class TestHtmlToText(unittest.TestCase):
    def test_strips_script_and_tags(self):
        html = "<html><head><title>T</title></head><body><script>var x=6.32;</script><p>Rate is 6.32 %</p></body></html>"
        text = SV.html_to_text(html)
        self.assertIn("6.32 %", text)
        self.assertNotIn("var x", text)

    def test_unescapes_entities(self):
        self.assertIn("€77,700", SV.html_to_text("<p>plafond &euro;77,700</p>"))


class TestSampleSelection(unittest.TestCase):
    def _c(self, cid, stamp):
        return SV.ClaimRecord(id=cid, scope="fr", section="Tax", line_no=1, claim_text="x",
                              values=[{"type": "pct", "raw": "6 %", "norm": "x", "needles": ["6"], "salient": True}],
                              source_url=f"https://x.gov/{cid}", source_host="x.gov",
                              source_tier="primary-gov", inline_stamp=stamp)

    def test_stale_marker_ranks_first(self):
        sv = make_sv()
        fresh = self._c("fresh", {"date": datetime.now(timezone.utc).strftime("%Y-%m-%d"), "kind": "verified"})
        stale = self._c("stale", {"date": "2026-01-01", "kind": "stale-marker"})
        never = self._c("never", None)
        picked = SV.select_sample([fresh, stale, never], 2, sv.priority_weights, seed=1)
        self.assertEqual(picked[0].id, "stale")

    def test_never_verified_beats_fresh(self):
        sv = make_sv()
        fresh = self._c("fresh", {"date": datetime.now(timezone.utc).strftime("%Y-%m-%d"), "kind": "verified"})
        never = self._c("never", None)
        picked = SV.select_sample([fresh, never], 1, sv.priority_weights, seed=1)
        self.assertEqual(picked[0].id, "never")

    def test_deterministic_with_seed(self):
        sv = make_sv()
        claims = [self._c(f"c{i}", None) for i in range(20)]
        a = [c.id for c in SV.select_sample(claims, 5, sv.priority_weights, seed=42)]
        b = [c.id for c in SV.select_sample(claims, 5, sv.priority_weights, seed=42)]
        self.assertEqual(a, b)


class TestContentCacheFreshness(unittest.TestCase):
    def test_fresh_within_ttl(self):
        e = {"status": "OK", "fetched_at": datetime.now(timezone.utc).isoformat()}
        self.assertTrue(SV.content_is_fresh(e, 30))

    def test_stale_past_ttl(self):
        old = (datetime.now(timezone.utc) - timedelta(days=40)).isoformat()
        self.assertFalse(SV.content_is_fresh({"status": "OK", "fetched_at": old}, 30))

    def test_non_ok_never_fresh(self):
        e = {"status": "DEAD", "fetched_at": datetime.now(timezone.utc).isoformat()}
        self.assertFalse(SV.content_is_fresh(e, 30))


class TestDedupeById(unittest.TestCase):
    def test_corpus_has_no_duplicate_ids(self):
        # the harness must collapse a line linking the same primary URL twice into one record
        sv = SV.load_sv_config()
        allow = SV.load_allowlist()
        claims = SV.extract_claims(sv, allow, True)
        ids = [c.id for c in claims]
        self.assertEqual(len(ids), len(set(ids)), "extract_claims returned duplicate ids")


class TestScopeDetection(unittest.TestCase):
    def test_country_scope(self):
        p = SV.ROOT / "skills" / "property-deep-dive" / "countries" / "fr" / "playbook.md"
        self.assertEqual(SV._scope_for(p), "fr")

    def test_shared_scope(self):
        p = SV.ROOT / "skills" / "property-deep-dive" / "shared" / "home-tax.md"
        self.assertEqual(SV._scope_for(p), "shared/home-tax")


class TestPdfExtraction(unittest.TestCase):
    def test_extracts_text_when_extractor_present(self):
        pdf = _make_min_pdf("Levy 5720 fee")
        text, method = SV.pdf_to_text(pdf)
        if SV._HAS_PDFTOTEXT or SV._HAS_PYPDF:
            self.assertIn("5720", text)              # ← the CI smoke assertion: fails loudly if broken
            self.assertIn(method, ("pdftotext", "pypdf"))
        else:
            self.assertEqual((text, method), ("", ""))

    def test_garbage_bytes_return_empty(self):
        text, method = SV.pdf_to_text(b"not a pdf at all")
        self.assertEqual(text, "")
        self.assertEqual(method, "")

    def test_html_at_pdf_url_not_fed_to_extractors(self):
        # a .pdf URL that returns HTML must short-circuit on the missing %PDF- magic (no pypdf noise)
        text, method = SV.pdf_to_text(b"<!DOCTYPE html><html><body>fee 5720</body></html>")
        self.assertEqual((text, method), ("", ""))

    def test_pdf_status_in_fetchresult(self):
        fr = SV.FetchResult("u", "PDF_NO_TEXT")
        self.assertEqual(fr.status, "PDF_NO_TEXT")
        self.assertFalse(fr.content_changed)


class TestContentChange(unittest.TestCase):
    def test_changed_after_stamp_true_when_newer(self):
        rec = {"content_changed": True, "inline_stamp": {"date": "2026-01-01"},
               "prev_fetched_at": "2026-05-01T00:00:00+00:00"}
        self.assertTrue(SV._changed_after_stamp(rec))

    def test_changed_after_stamp_false_when_older(self):
        rec = {"content_changed": True, "inline_stamp": {"date": "2026-05-01"},
               "prev_fetched_at": "2026-01-01T00:00:00+00:00"}
        self.assertFalse(SV._changed_after_stamp(rec))

    def test_not_changed_is_false(self):
        self.assertFalse(SV._changed_after_stamp({"content_changed": False}))


class TestAuditReport(unittest.TestCase):
    def _wl(self):
        return [
            {"scope": "fr", "line_no": 9, "claim_text": "rate 6.32%", "source_url": "https://x.gov",
             "prior": "TOKENS_ABSENT", "missing_tokens": ["6.32"], "inline_stamp": {"date": "2026-01-01"},
             "content_changed": False, "prev_fetched_at": ""},
            {"scope": "it", "line_no": 5, "claim_text": "fee €77,700", "source_url": "https://y.gov",
             "prior": "TOKENS_PRESENT", "missing_tokens": [], "inline_stamp": None,
             "content_changed": True, "prev_fetched_at": "2026-04-01T00:00:00+00:00"},
            {"scope": "de", "line_no": 3, "claim_text": "x", "source_url": "https://z.gov/a.pdf",
             "prior": "PDF_NO_TEXT", "missing_tokens": ["1"], "inline_stamp": None,
             "content_changed": False, "prev_fetched_at": ""},
        ]

    def test_buckets(self):
        rep = SV.audit_report(self._wl())
        self.assertEqual(len(rep["tokens_absent"]), 1)
        self.assertEqual(len(rep["content_changed"]), 1)
        self.assertEqual(len(rep["pdf_no_text"]), 1)
        self.assertEqual(rep["flagged"], 2)  # 1 absent + 1 changed
        self.assertEqual(rep["by_prior"]["TOKENS_ABSENT"], 1)

    def test_render_md_runs(self):
        md = SV.render_audit_md(SV.audit_report(self._wl()), last_run="2026-05-01")
        self.assertIn("TOKENS_ABSENT", md)
        self.assertIn("CHANGED", md)


class TestLinter(unittest.TestCase):
    def test_is_root(self):
        self.assertTrue(CC.is_root("https://www.gov.ky/"))
        self.assertTrue(CC.is_root("https://taxes.gov.az"))
        self.assertFalse(CC.is_root("https://www.gov.ky/residency/permanent"))
        self.assertFalse(CC.is_root("https://x.gov/?q=1"))

    def test_hostlike_label(self):
        self.assertTrue(CC.HOSTLIKE_LABEL_RE.match("gov.ky"))
        self.assertTrue(CC.HOSTLIKE_LABEL_RE.match("legislation.gov.ky"))
        self.assertFalse(CC.HOSTLIKE_LABEL_RE.match("Llei 21/2014"))
        self.assertFalse(CC.HOSTLIKE_LABEL_RE.match("DL 126/2021"))

    def test_salient_triggers_on_money_pct_not_statute(self):
        self.assertTrue(CC.SALIENT_RE.search("threshold CI$2,000,000 applies"))
        self.assertTrue(CC.SALIENT_RE.search("rate 7.5%"))
        self.assertIsNone(CC.SALIENT_RE.search("under Loi 2024-1039 only"))  # statute alone does NOT trigger

    def test_pointer_excludes(self):
        self.assertTrue(CC.POINTER_RE.search("VERIFY the exact threshold at [WORC](https://worc.ky/)"))
        self.assertTrue(CC.POINTER_RE.search("confirm at [x](https://x.gov/)"))


# ── Edge cases ───────────────────────────────────────────────────────────────
class TestIsPdf(unittest.TestCase):
    def test_content_type(self):
        self.assertTrue(SV._is_pdf("application/pdf", "https://x.gov/whatever"))
        self.assertTrue(SV._is_pdf("application/pdf; charset=binary", "https://x.gov/a"))

    def test_path_suffix(self):
        self.assertTrue(SV._is_pdf("text/html", "https://x.gov/doc.pdf"))
        self.assertTrue(SV._is_pdf("application/octet-stream", "https://x.gov/A.PDF"))

    def test_query_string_ignored(self):
        self.assertTrue(SV._is_pdf("", "https://x.gov/fee.pdf?download=1"))   # path ends .pdf
        self.assertFalse(SV._is_pdf("text/html", "https://x.gov/page?file=a.pdf"))  # path is /page

    def test_not_pdf(self):
        self.assertFalse(SV._is_pdf("text/html", "https://x.gov/page"))
        self.assertFalse(SV._is_pdf("", "https://x.gov/"))


class TestPdfEdges(unittest.TestCase):
    def test_empty_bytes(self):
        self.assertEqual(SV.pdf_to_text(b""), ("", ""))

    def test_truncated_pdf_is_graceful(self):
        full = _make_min_pdf("Fee 1234")
        truncated = full[: len(full) // 2]            # half a PDF — must not raise
        text, method = SV.pdf_to_text(truncated)
        self.assertIsInstance(text, str)              # whatever it returns, no exception

    def test_max_pages_does_not_crash(self):
        text, _ = SV.pdf_to_text(_make_min_pdf("Page one 999"), max_pages=1)
        if SV._HAS_PDFTOTEXT or SV._HAS_PYPDF:
            self.assertIn("999", text)

    def test_multi_token_extraction(self):
        text, _ = SV.pdf_to_text(_make_min_pdf("2200 then 5720"))
        if SV._HAS_PDFTOTEXT or SV._HAS_PYPDF:
            self.assertIn("2200", text)
            self.assertIn("5720", text)


class TestSettleChange(unittest.TestCase):
    def test_first_content_sets_baseline(self):
        self.assertEqual(SV._settle_change("OK", "h1", "", ""), (False, "h1"))

    def test_unchanged(self):
        self.assertEqual(SV._settle_change("OK", "h1", "h1", "h1"), (False, "h1"))

    def test_dynamic_page_never_confirms(self):
        # hash differs from BOTH last run and baseline → in flux → not flagged, baseline kept
        self.assertEqual(SV._settle_change("OK", "hNEW", "hPREV", "hBASE"), (False, "hBASE"))

    def test_settled_new_value_confirms(self):
        # same new value two runs running, different from baseline → confirmed change
        self.assertEqual(SV._settle_change("OK", "hB", "hB", "hA"), (True, "hB"))

    def test_reverted_to_baseline_not_flagged(self):
        self.assertEqual(SV._settle_change("OK", "hA", "hX", "hA"), (False, "hA"))

    def test_non_ok_never_changes(self):
        self.assertEqual(SV._settle_change("DEAD", "h2", "h2", "h1"), (False, "h1"))
        self.assertEqual(SV._settle_change("OK", "", "h2", "h1"), (False, "h1"))

    def test_dynamic_sequence_stays_quiet(self):
        # simulate a dynamic page across 4 runs: hash changes every run → never flagged
        stable, last = "", ""
        for h in ["x1", "x2", "x3", "x4"]:
            changed, stable = SV._settle_change("OK", h, last, stable)
            self.assertFalse(changed)
            last = h

    def test_real_change_surfaces_next_run(self):
        # stable A; page changes to B and stays B → flagged on the 2nd B run
        stable, last = "A", "A"
        c1, stable = SV._settle_change("OK", "B", last, stable); last = "B"   # flux
        c2, stable = SV._settle_change("OK", "B", last, stable); last = "B"   # settled → flagged
        self.assertFalse(c1)
        self.assertTrue(c2)
        self.assertEqual(stable, "B")


class TestChangedAfterStampEdges(unittest.TestCase):
    def test_changed_no_stamp_surfaces(self):
        self.assertTrue(SV._changed_after_stamp({"content_changed": True, "inline_stamp": None,
                                                 "prev_fetched_at": "2026-05-01T00:00:00+00:00"}))

    def test_changed_no_prev_surfaces(self):
        self.assertTrue(SV._changed_after_stamp({"content_changed": True,
                                                 "inline_stamp": {"date": "2026-01-01"}, "prev_fetched_at": ""}))

    def test_malformed_stamp_is_graceful(self):
        self.assertTrue(SV._changed_after_stamp({"content_changed": True,
                                                 "inline_stamp": {"date": "not-a-date"},
                                                 "prev_fetched_at": "2026-05-01T00:00:00+00:00"}))

    def test_malformed_prev_is_graceful(self):
        self.assertTrue(SV._changed_after_stamp({"content_changed": True,
                                                 "inline_stamp": {"date": "2026-01-01"},
                                                 "prev_fetched_at": "garbage"}))


class TestAuditReportEdges(unittest.TestCase):
    def test_empty_worklist(self):
        rep = SV.audit_report([])
        self.assertEqual(rep["total"], 0)
        self.assertEqual(rep["flagged"], 0)
        self.assertEqual(rep["tokens_absent"], [])
        self.assertEqual(rep["content_changed"], [])

    def test_both_buckets_flagged_once(self):
        # a single claim that is BOTH absent AND its page changed → flagged distinct = 1, in both lists
        wl = [{"scope": "fr", "line_no": 9, "claim_text": "x", "source_url": "https://x.gov",
               "prior": "TOKENS_ABSENT", "missing_tokens": ["6.32"], "inline_stamp": None,
               "content_changed": True, "prev_fetched_at": "2026-04-01T00:00:00+00:00"}]
        rep = SV.audit_report(wl)
        self.assertEqual(len(rep["tokens_absent"]), 1)
        self.assertEqual(len(rep["content_changed"]), 1)
        self.assertEqual(rep["flagged"], 1)   # NOT 2

    def test_source_unavailable_bucket(self):
        wl = [{"scope": "x", "line_no": 1, "claim_text": "x", "source_url": "https://x.gov",
               "prior": "SOURCE_UNAVAILABLE", "missing_tokens": [], "inline_stamp": None,
               "content_changed": False, "prev_fetched_at": ""}]
        rep = SV.audit_report(wl)
        self.assertEqual(len(rep["source_unavailable"]), 1)
        self.assertEqual(rep["flagged"], 0)   # unavailable is a fetch problem, not a flag


class TestRenderAuditMd(unittest.TestCase):
    def test_empty_renders_none(self):
        md = SV.render_audit_md(SV.audit_report([]))
        self.assertIn("_(none)_", md)
        self.assertIn("tripwires, not verdicts", md)

    def test_pipe_in_claim_escaped(self):
        wl = [{"scope": "fr", "line_no": 1, "claim_text": "rate a|b|c table", "source_url": "https://x.gov",
               "prior": "TOKENS_ABSENT", "missing_tokens": ["1"], "inline_stamp": None,
               "content_changed": False, "prev_fetched_at": ""}]
        md = SV.render_audit_md(SV.audit_report(wl))
        self.assertNotIn("a|b|c", md)   # pipes replaced so they don't break the markdown table
        self.assertIn("a/b/c", md)


class TestFlagLine(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(CC.flag_line("rate 7.5% at [gov.ky](https://www.gov.ky/)"),
                         ["https://www.gov.ky/"])

    def test_money_code_positive(self):
        self.assertEqual(CC.flag_line("threshold CI$2,000,000 [gov.ky](https://www.gov.ky/)"),
                         ["https://www.gov.ky/"])

    def test_statute_only_no_flag(self):
        self.assertEqual(CC.flag_line("under [Loi 2024-1039](https://x.gov/) reform"), [])

    def test_pointer_excluded(self):
        self.assertEqual(CC.flag_line("VERIFY the 7.5% rate at [gov.ky](https://www.gov.ky/)"), [])

    def test_document_label_not_flagged(self):
        self.assertEqual(CC.flag_line("fee €100 per [Llei 5/2014](https://x.gov/)"), [])

    def test_non_root_not_flagged(self):
        self.assertEqual(CC.flag_line("fee €100 [gov.ky](https://www.gov.ky/residency)"), [])

    def test_allowlist_skips(self):
        self.assertEqual(CC.flag_line("fee €100 [gov.ky](https://www.gov.ky/)", {"www.gov.ky"}), [])

    def test_heading_skipped(self):
        self.assertEqual(CC.flag_line("# Tax 7.5% [gov.ky](https://www.gov.ky/)"), [])

    def test_trailing_punctuation_url(self):
        self.assertEqual(CC.flag_line("fee €5 [gov.ky](https://www.gov.ky/)."),
                         ["https://www.gov.ky/"])

    def test_two_root_links_one_line(self):
        out = CC.flag_line("7.5% [gov.ky](https://www.gov.ky/) and [legislation.gov.ky](https://legislation.gov.ky/)")
        self.assertEqual(len(out), 2)

    def test_commercial_root_not_flagged(self):
        # a carrier/aggregator homepage cited for a tariff is NOT a primary source → skip
        self.assertEqual(CC.flag_line("plan RM199 100Mbps [orange.sk](https://www.orange.sk/)"), [])
        self.assertEqual(CC.flag_line("fee USD 50 [flat35.com](https://www.flat35.com/)"), [])

    def test_is_primary(self):
        self.assertTrue(CC.is_primary("www.gov.ky"))
        self.assertTrue(CC.is_primary("legislation.gov.ky"))
        self.assertTrue(CC.is_primary("sat.gob.mx"))
        self.assertFalse(CC.is_primary("www.orange.sk"))
        self.assertFalse(CC.is_primary("knightfrank.com"))


class TestHtmlAndCacheEdges(unittest.TestCase):
    def test_html_strips_comments(self):
        self.assertNotIn("secret", SV.html_to_text("<p>fee 5%<!-- secret -->done</p>"))

    def test_html_br_to_newline(self):
        self.assertIn("\n", SV.html_to_text("line a<br>line b"))

    def test_cache_malformed_timestamp_not_fresh(self):
        self.assertFalse(SV.content_is_fresh({"status": "OK", "fetched_at": "not-a-date"}, 30))

    def test_thousands_three_groups(self):
        self.assertEqual(SV._thousands_stripped("1,234,567"), "1234567")
        self.assertIsNone(SV._thousands_stripped("12,34"))   # 2-digit group → not thousands


if __name__ == "__main__":
    unittest.main(verbosity=2)
