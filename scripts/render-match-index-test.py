#!/usr/bin/env python3
"""Unit tests for render-match-index.py. Run: python3 scripts/render-match-index-test.py"""

import importlib.util
import json
import unittest
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    'render_match_index', Path(__file__).resolve().parent / 'render-match-index.py')
rmi = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(rmi)


class TestBanding(unittest.TestCase):
    def test_good_endpoints(self):
        self.assertEqual(rmi._band_good(1, 10), 100)
        self.assertEqual(rmi._band_good(10, 10), 55)
        self.assertEqual(rmi._band_good(1, 1), 100)  # single item

    def test_bad_endpoints(self):
        self.assertEqual(rmi._band_bad(1, 10), 0)
        self.assertEqual(rmi._band_bad(10, 10), 45)
        self.assertEqual(rmi._band_bad(1, 1), 0)  # single item

    def test_good_above_bad(self):
        # worst "good" band still beats best "bad" band
        self.assertGreater(rmi._band_good(10, 10), rmi._band_bad(1, 10))


class TestSectionExtraction(unittest.TestCase):
    MD = (
        "### Lowest acquisition cost (% of price)\n"
        "1. GE (~0.1%)\n2. **EE** (~1-2%)\n3. Eurozone (placeholder)\n"
        "### Highest acquisition friction\n"
        "1. TH (no land freehold for foreigners; condo 49% quota)\n"
        "2. ES (open, NIE only)\n"
        "## Next major\n1. ZZ (should not be captured)\n"
    )

    def test_extract_found(self):
        body = rmi._extract_section(self.MD, 'Lowest acquisition cost')
        self.assertIn('GE', body)
        self.assertNotIn('ZZ', body)

    def test_extract_stops_at_next_header(self):
        body = rmi._extract_section(self.MD, 'Highest acquisition friction')
        self.assertIn('TH', body)
        self.assertNotIn('ZZ', body)  # stopped at '## Next major'

    def test_extract_missing(self):
        self.assertIsNone(rmi._extract_section(self.MD, 'No Such Section'))

    def test_parse_codes_bold_and_eurozone(self):
        body = rmi._extract_section(self.MD, 'Lowest acquisition cost')
        codes = rmi._parse_ranked_codes(body)
        self.assertEqual(codes[0], 'ge')
        self.assertEqual(codes[1], 'ee')          # bold stripped
        self.assertIn('fr', codes)                # Eurozone expanded
        self.assertIn('de', codes)

    def test_parse_codes_dedupe(self):
        codes = rmi._parse_ranked_codes("1. GE (a)\n2. GE (dup)\n3. EE (b)\n")
        self.assertEqual(codes, ['ge', 'ee'])

    def test_parse_codes_skip_words(self):
        codes = rmi._parse_ranked_codes("1. Most things (not a code)\n2. PT (ok)\n")
        self.assertEqual(codes, ['pt'])

    def test_friction_open_flags(self):
        body = rmi._extract_section(self.MD, 'Highest acquisition friction')
        flags = rmi._parse_friction_open_flags(body)
        self.assertFalse(flags['th'])   # "no land freehold" → ban
        self.assertTrue(flags['es'])    # merely costly → still open


class TestVisaRoutes(unittest.TestCase):
    def test_returns_set(self):
        routes = rmi._load_visa_routes()
        self.assertIsInstance(routes, set)
        # all entries are lowercase iso2-ish strings
        for c in routes:
            self.assertTrue(c and c == c.lower())


class TestBuildIndex(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.idx = rmi.build_index()

    def test_top_level_shape(self):
        self.assertEqual(self.idx['schema_version'], rmi.SCHEMA_VERSION)
        self.assertGreater(self.idx['country_count'], 0)
        for c in rmi.PENDING_CRITERIA:
            self.assertIn(c, self.idx['criteria'])

    # The six inherently-live criteria — must NEVER be pre-baked (decay/fabrication).
    LIVE_ONLY = ['yield', 'climate', 'safety', 'connectivity', 'cost-of-living', 'schools']

    def test_live_only_criteria_always_pending(self):
        for code, rec in self.idx['countries'].items():
            for c in self.LIVE_ONLY:
                cell = rec['scores'][c]
                self.assertEqual(cell.get('status'), 'pending-extraction',
                                 f'{code}:{c} must stay pending (live-by-design)')
                self.assertNotIn('band', cell, f'{code}:{c} must have NO band')

    def test_extracted_healthcare_grounded(self):
        # Healthcare is curated for a small set; every populated cell must cite
        # its source + carry tier/evidence/conf — grounded, never guessed.
        populated = 0
        for code, rec in self.idx['countries'].items():
            cell = rec['scores']['healthcare']
            if 'band' in cell:
                populated += 1
                self.assertIn('digital-nomad-healthcare.md', cell['src'])
                self.assertEqual(cell['conf'], 'MEDIUM')
                self.assertTrue(cell.get('evidence'))
                self.assertTrue(0 <= cell['band'] <= 100)
            else:
                self.assertEqual(cell.get('status'), 'pending-extraction')
        self.assertGreaterEqual(populated, 8, 'expected ~10 curated healthcare tiers')

    def test_known_healthcare_tiers(self):
        de = self.idx['countries'].get('de')
        if de:
            self.assertEqual(de['scores']['healthcare']['band'], 95)  # immediate
        es = self.idx['countries'].get('es')
        if es:
            self.assertEqual(es['scores']['healthcare']['band'], 35)  # 1-yr contribution

    def test_every_band_has_provenance(self):
        for code, rec in self.idx['countries'].items():
            for crit, cell in rec['scores'].items():
                if 'band' in cell:
                    self.assertTrue(cell.get('src'), f'{code}:{crit} band needs src')
                    self.assertTrue(0 <= cell['band'] <= 100)
                    # deterministic bands cite compare.md; extracted cite a shared/ source
                    self.assertTrue(cell['src'].startswith('compare.md:')
                                    or 'shared/' in cell['src'],
                                    f'{code}:{crit} src not grounded: {cell["src"]}')

    def test_hard_filters_present(self):
        for rec in self.idx['countries'].values():
            for k in ('foreign-buyer-open', 'no-fx-risk', 'property-residency-route'):
                self.assertIn(k, rec['hard'])
                self.assertIsInstance(rec['hard'][k], bool)

    def test_eurozone_fx_pinned_top(self):
        pt = self.idx['countries'].get('pt')
        self.assertIsNotNone(pt)
        self.assertEqual(pt['scores']['fx']['band'], 100)
        self.assertTrue(pt['hard']['no-fx-risk'])

    def test_known_restricted_country(self):
        th = self.idx['countries'].get('th')
        if th:  # TH appears in the friction list
            self.assertFalse(th['hard']['foreign-buyer-open'])

    def test_golden_visa_absences_not_banded(self):
        # "NO golden-visa" countries must NOT get a friendly visa band (audit HIGH#1).
        for code in ('sg', 'in', 'ng', 'ke', 'kw'):
            rec = self.idx['countries'].get(code)
            if rec:
                self.assertIsNone(rec['scores'].get('visa', {}).get('band'),
                                  f'{code} has NO golden-visa — must not be visa-banded')

    def test_property_residency_route_open_prefix(self):
        # Qualified-OPEN property-linked routes must set the hard filter (audit HIGH#2).
        for code in ('gr', 'mt', 'eg'):
            rec = self.idx['countries'].get(code)
            if rec:
                self.assertTrue(rec['hard']['property-residency-route'],
                                f'{code} has an OPEN property-linked visa route')
        # ...but a REMOVED/excluded RE route ("**NO — RE removed") must NOT count,
        # even though its programme status starts with OPEN (re-audit HIGH).
        for code in ('pt', 'hu', 'kz', 'il'):
            rec = self.idx['countries'].get(code)
            if rec:
                self.assertFalse(rec['hard']['property-residency-route'],
                                 f'{code} has no affirmative property→residency route')

    def test_foreign_buyer_ban_consistency(self):
        # GCC designated-freehold-zone countries all open; land/purchase bans closed.
        for code in ('ae', 'qa', 'sa', 'bh', 'om'):
            rec = self.idx['countries'].get(code)
            if rec:
                self.assertTrue(rec['hard']['foreign-buyer-open'],
                                f'{code} allows in-zone freehold → open')
        for code in ('vn', 'th', 'id', 'ca', 'au', 'nz', 'kw'):
            rec = self.idx['countries'].get(code)
            if rec:
                self.assertFalse(rec['hard']['foreign-buyer-open'],
                                 f'{code} bans foreign freehold/purchase → closed')

    def test_mc_ad_fx_pinned(self):
        for code in ('mc', 'ad'):
            rec = self.idx['countries'].get(code)
            if rec:
                self.assertEqual(rec['scores']['fx']['band'], 100,
                                 f'{code} is no-FX-risk (EUR treaty) → top tier')

    def test_idempotent(self):
        again = rmi.build_index()
        self.assertEqual(json.dumps(self.idx, sort_keys=True),
                         json.dumps(again, sort_keys=True))


if __name__ == '__main__':
    unittest.main(verbosity=2)
