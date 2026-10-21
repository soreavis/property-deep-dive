#!/usr/bin/env python3
"""Unit tests for scripts/check-link-labels.py. Run: python3 scripts/check-link-labels-test.py"""

from __future__ import annotations

import importlib.util
import unittest
from collections import Counter
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    "check_link_labels", Path(__file__).parent / "check-link-labels.py"
)
CL = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(CL)


def hosts(line: str) -> list[tuple[str, str]]:
    return [(lh, uh) for _, lh, uh in CL.line_mismatches(line)]


class LineTest(unittest.TestCase):
    def test_match_and_mismatch(self):
        self.assertEqual(hosts("see [gov.ky](https://gov.ky/tax)"), [])
        self.assertEqual(
            hosts("see [gov.ky](https://other.ky/tax)"), [("gov.ky", "other.ky")]
        )

    def test_subdomain_either_way(self):
        self.assertEqual(
            hosts("[gov.uk](https://www.legislation.gov.uk/ukpga/2017/1)"), []
        )
        self.assertEqual(hosts("[legislation.gov.uk](https://gov.uk/)"), [])
        self.assertEqual(hosts("[admin.ch](https://map.geo.admin.ch)"), [])
        self.assertEqual(
            hosts("[map.geo.admin.ch](https://bafu.admin.ch)"),
            [("map.geo.admin.ch", "bafu.admin.ch")],
        )
        self.assertEqual(hosts("[ov.ky](https://gov.ky/)"), [("ov.ky", "gov.ky")])

    def test_www_case_port_scheme_path_trailing_dot(self):
        self.assertEqual(hosts("[WWW.Gov.KY](https://gov.ky)"), [])
        self.assertEqual(hosts("[gov.ky](https://www.gov.ky:8443/x)"), [])
        self.assertEqual(hosts("[https://gov.ky/a/b](https://gov.ky/c)"), [])
        self.assertEqual(hosts("[gov.ky:8080/path](http://gov.ky.)"), [])
        self.assertEqual(
            hosts("[https://gov.ky/a](https://bad.ky/a)"), [("gov.ky", "bad.ky")]
        )

    def test_only_host_like_labels(self):
        for label in (
            "Cadastre portal",
            "Llei 21/2014",
            "Art. 5.2",
            "robots.txt",
            "decree.pdf",
            "e.g",
        ):
            self.assertEqual(hosts(f"[{label}](https://other.example/)"), [], label)

    def test_decorated_label(self):
        self.assertEqual(hosts("[`gov.ky`](https://bad.ky)"), [("gov.ky", "bad.ky")])
        self.assertEqual(hosts("[**gov.ky**](https://gov.ky)"), [])

    def test_code_spans_skipped(self):
        self.assertEqual(hosts("`[gov.ky](https://bad.ky)`"), [])
        self.assertEqual(hosts("``a ` [gov.ky](https://bad.ky)``"), [])
        self.assertEqual(hosts("`[x` [gov.ky](https://bad.ky)"), [("gov.ky", "bad.ky")])
        self.assertEqual(
            hosts("`x` [gov.ky](https://bad.ky) `y`"), [("gov.ky", "bad.ky")]
        )


class TextTest(unittest.TestCase):
    def test_fenced_code_skipped_and_line_numbers(self):
        text = "\n".join(
            [
                "[a.ky](https://b.ky)",
                "```markdown",
                "[c.ky](https://d.ky)",
                "~~~",
                "```",
                "  ~~~~",
                "[e.ky](https://f.ky)",
                "  ~~~~",
                "[g.ky](https://h.ky)",
            ]
        )
        self.assertEqual(
            [(n, lh) for n, _, lh, _ in CL.text_mismatches(text)],
            [(1, "a.ky"), (9, "g.ky")],
        )


class BaselineTest(unittest.TestCase):
    def test_new_vs_stale(self):
        found = [
            ("f.md", 3, "a.ky", "a.ky", "b.ky"),
            ("f.md", 9, "a.ky", "a.ky", "b.ky"),
            ("g.md", 1, "c.ky", "c.ky", "d.ky"),
        ]
        baseline = [
            {"file": "f.md", "label": "a.ky", "href": "b.ky"},
            {"file": "x.md", "label": "y.ky", "href": "z.ky"},
        ]
        new, stale = CL.compare(found, baseline)
        self.assertEqual([(f, n) for f, n, *_ in new], [("f.md", 9), ("g.md", 1)])
        self.assertEqual(stale, Counter({("x.md", "y.ky", "z.ky"): 1}))

    def test_clean_when_baseline_covers_all(self):
        found = [("f.md", 3, "a.ky", "a.ky", "b.ky")]
        self.assertEqual(
            CL.compare(found, [{"file": "f.md", "label": "a.ky", "href": "b.ky"}]),
            ([], Counter()),
        )


if __name__ == "__main__":
    unittest.main()
