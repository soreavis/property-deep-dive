#!/usr/bin/env python3
"""Unit tests for scripts/filter-feeds.py.

Each test pins one defect found in the inline parser this script replaced.

Run: python3 scripts/filter-feeds-test.py
"""

from __future__ import annotations

import contextlib
import importlib.util
import io
import sys
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from email.utils import format_datetime
from pathlib import Path
from xml.etree import ElementTree

spec = importlib.util.spec_from_file_location(
    "filter_feeds", str(Path(__file__).parent / "filter-feeds.py")
)
filter_feeds = importlib.util.module_from_spec(spec)
sys.modules["filter_feeds"] = filter_feeds
spec.loader.exec_module(filter_feeds)

FF = filter_feeds
KEYWORDS = "property|housing|stamp duty"


def rss(items: str) -> str:
    return f'<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel>{items}</channel></rss>'


def run(xml: str, *, window_days: int = 3, name: str = "TEST", exclude: str = "") -> tuple[int, str]:
    """Run main() against an XML string; return (exit_code, stdout)."""
    with tempfile.NamedTemporaryFile("w", suffix=".xml", delete=False, encoding="utf-8") as fh:
        fh.write(xml)
        path = fh.name
    argv = ["filter-feeds.py", "--name", name, "--path", path,
            "--keywords", KEYWORDS, "--exclude", exclude, "--window-days", str(window_days)]
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        old, sys.argv = sys.argv, argv
        try:
            code = FF.main()
        finally:
            sys.argv = old
    Path(path).unlink()
    return code, out.getvalue()


def rfc822(dt: datetime) -> str:
    return format_datetime(dt)


NOW = datetime.now(timezone.utc)


class TestClean(unittest.TestCase):
    def test_strips_cdata_without_eating_the_title(self):
        # The old parser ran re.sub(r'<[^>]+>', '', ...) over a CDATA-wrapped
        # title; `]]>` supplied the closing `>`, so the whole title vanished.
        item = ElementTree.fromstring("<item><title><![CDATA[Housing reform]]></title></item>")
        self.assertEqual(FF.child_text(item, "title"), "Housing reform")

    def test_unescapes_double_escaped_markup(self):
        item = ElementTree.fromstring(
            "<item><description>&lt;p&gt;Stamp duty &amp;amp; property&lt;/p&gt;</description></item>"
        )
        self.assertEqual(FF.child_text(item, "description"), "Stamp duty & property")

    def test_collapses_whitespace(self):
        self.assertEqual(FF.clean("a\n\n  b\t c"), "a b c")

    def test_empty_input(self):
        self.assertEqual(FF.clean(None), "")


class TestLink(unittest.TestCase):
    def test_rss_link_text(self):
        item = ElementTree.fromstring("<item><link>https://example.com/a</link></item>")
        self.assertEqual(FF.item_link(item), "https://example.com/a")

    def test_atom_link_href_prefers_alternate(self):
        item = ElementTree.fromstring(
            '<entry xmlns="http://www.w3.org/2005/Atom">'
            '<link rel="self" href="https://example.com/self"/>'
            '<link rel="alternate" href="https://example.com/post"/></entry>'
        )
        self.assertEqual(FF.item_link(item), "https://example.com/post")

    def test_missing_link_is_empty(self):
        self.assertEqual(FF.item_link(ElementTree.fromstring("<item/>")), "")


class TestDate(unittest.TestCase):
    def test_rfc822(self):
        self.assertIsNotNone(FF.item_date(
            ElementTree.fromstring("<item><pubDate>Thu, 9 Jul 2026 10:22:09 +0200</pubDate></item>")))

    def test_iso8601_atom(self):
        item = ElementTree.fromstring(
            '<entry xmlns="http://www.w3.org/2005/Atom"><updated>2026-07-09T10:22:09Z</updated></entry>')
        self.assertIsNotNone(FF.item_date(item))

    def test_nonstandard_ctime_form_parses_leniently(self):
        # CJEU emits this shape. parsedate_to_datetime recovers the date and
        # drops the zone; a <=2h skew is immaterial to a multi-day window.
        parsed = FF.item_date(
            ElementTree.fromstring("<item><pubDate>Thu Jul 09 00:00:00 CEST 2026</pubDate></item>"))
        self.assertIsNotNone(parsed)
        self.assertEqual((parsed.year, parsed.month, parsed.day), (2026, 7, 9))
        self.assertIsNotNone(parsed.tzinfo, "naive datetimes would crash the cutoff compare")

    def test_garbage_date_is_none_not_crash(self):
        self.assertIsNone(FF.item_date(
            ElementTree.fromstring("<item><pubDate>not a date</pubDate></item>")))

    def test_missing_date_is_none(self):
        self.assertIsNone(FF.item_date(ElementTree.fromstring("<item/>")))


class TestFiltering(unittest.TestCase):
    def test_matches_on_description_when_title_is_opaque(self):
        # Verbatim shape of a real CJEU item: subject matter only in the body.
        code, out = run(rss(
            "<item><title>101/Thu Jul 09 : null - Opinion of the Advocate General</title>"
            f"<description>Dispute over housing rent caps</description>"
            f"<pubDate>{rfc822(NOW)}</pubDate></item>"))
        self.assertEqual(code, 0)
        self.assertIn("Opinion of the Advocate General", out)

    def test_non_matching_item_omitted(self):
        code, out = run(rss(
            f"<item><title>Fisheries quota</title><description>Cod</description>"
            f"<pubDate>{rfc822(NOW)}</pubDate></item>"))
        self.assertEqual(code, 0)
        self.assertEqual(out, "")

    def test_stale_item_dropped(self):
        code, out = run(rss(
            f"<item><title>Property tax</title><pubDate>{rfc822(NOW - timedelta(days=30))}</pubDate></item>"))
        self.assertEqual(code, 0)
        self.assertEqual(out, "")

    def test_fresh_item_kept(self):
        code, out = run(rss(
            f"<item><title>Property tax</title><pubDate>{rfc822(NOW - timedelta(hours=6))}</pubDate></item>"))
        self.assertEqual(code, 0)
        self.assertIn("Property tax", out)

    def test_undated_item_kept(self):
        # Absent/garbage dates must not silently drop an item.
        code, out = run(rss("<item><title>Property tax</title></item>"))
        self.assertEqual(code, 0)
        self.assertIn("Property tax", out)

    def test_case_insensitive(self):
        code, out = run(rss(f"<item><title>PROPERTY levy</title><pubDate>{rfc822(NOW)}</pubDate></item>"))
        self.assertIn("PROPERTY levy", out)

    def test_emits_link_and_snippet(self):
        code, out = run(rss(
            f"<item><title>Housing</title><description>Rent caps introduced</description>"
            f"<link>https://example.com/x</link><pubDate>{rfc822(NOW)}</pubDate></item>"))
        self.assertIn("  - Rent caps introduced", out)
        self.assertIn("  - <https://example.com/x>", out)


class TestPrecision(unittest.TestCase):
    EXCLUDE = "intellectual property"

    def test_intellectual_property_excluded(self):
        code, out = run(rss(
            f"<item><title>Speech on intellectual property enforcement</title>"
            f"<pubDate>{rfc822(NOW)}</pubDate></item>"), exclude=self.EXCLUDE)
        self.assertEqual(code, 0)
        self.assertEqual(out, "")

    def test_excluded_phrase_does_not_suppress_a_genuine_match(self):
        # Item mentions both; the real-estate signal must survive.
        code, out = run(rss(
            f"<item><title>Intellectual property and housing policy</title>"
            f"<pubDate>{rfc822(NOW)}</pubDate></item>"), exclude=self.EXCLUDE)
        self.assertIn("housing policy", out)

    def test_word_boundary_prevents_substring_match(self):
        code, out = run(rss(
            f"<item><title>Propertyless tenants</title><description>Nothing relevant</description>"
            f"<pubDate>{rfc822(NOW)}</pubDate></item>"))
        self.assertEqual(out, "")

    def test_multiword_keyword_still_matches(self):
        code, out = run(rss(
            f"<item><title>New stamp duty rules</title><pubDate>{rfc822(NOW)}</pubDate></item>"))
        self.assertIn("stamp duty", out)


class TestUnusableFeeds(unittest.TestCase):
    def test_soft_404_exits_2(self):
        # EUR-Lex served HTTP 200 with this body for years; the old parser read
        # it as a healthy feed with zero matches.
        code, _ = run('<?xml version="1.0"?><rss version="2.0"><channel>'
                      "<description>The RSS feed doesn't exist or is no longer valid.</description>"
                      "</channel></rss>")
        self.assertEqual(code, 2)

    def test_empty_body_exits_2(self):
        # AWS WAF answers a challenge with HTTP 202 + an empty body; the workflow
        # catches that before parsing, but a zero-byte feed must never read as OK.
        code, _ = run("")
        self.assertEqual(code, 2)

    def test_malformed_xml_exits_2(self):
        code, _ = run("<rss><channel><item><title>unclosed")
        self.assertEqual(code, 2)

    def test_atom_entries_are_found(self):
        code, out = run(
            '<?xml version="1.0"?><feed xmlns="http://www.w3.org/2005/Atom">'
            '<entry><title>Property register</title>'
            '<link rel="alternate" href="https://example.com/e"/></entry></feed>')
        self.assertEqual(code, 0)
        self.assertIn("Property register", out)


if __name__ == "__main__":
    unittest.main(verbosity=2)
