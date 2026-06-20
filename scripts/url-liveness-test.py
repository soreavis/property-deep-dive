#!/usr/bin/env python3
"""Unit tests for scripts/url-liveness.py — deterministic parts only.

Network-level aiohttp checking is validated by the workflow's dry-run job,
not here.

Run: python3 scripts/url-liveness-test.py
"""

from __future__ import annotations

import sys
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import importlib.util
spec = importlib.util.spec_from_file_location("url_liveness", str(Path(__file__).parent / "url-liveness.py"))
url_liveness = importlib.util.module_from_spec(spec)
sys.modules["url_liveness"] = url_liveness  # required for dataclass annotation resolution on 3.12+
spec.loader.exec_module(url_liveness)

UL = url_liveness


def make_cfg(**overrides):
    raw = {
        "version": 1,
        "global": {
            "concurrency": 8,
            "req_per_sec": 4,
            "default_per_host_concurrency": 2,
            "default_per_host_interval_ms": 500,
            "request_timeout_seconds": 10,
            "max_retries": 2,
            "retry_backoff_seconds": [1, 2],
            "retry_jitter_pct": 25,
            "fail_streak_for_dead": 3,
            "random_refresh_pct": 10,
            "threshold_pct": 90,
            "cache_ttl_days": {"LIVE": 30, "REDIRECT_LIVE": 30, "AUTH_REQUIRED": 7},
            "user_agent": "test/{version}",
            "follow_redirects_max": 5,
        },
        "per_host_overrides": {
            "eur-lex.europa.eu": {"concurrency": 1, "interval_ms": 10000, "reason": "crawl-delay"},
        },
        "gov_suffix_default": {"concurrency": 1, "interval_ms": 1000, "reason": "gov"},
        "excluded_hosts": [{"host": "linkedin.com", "reason": "999"}],
        "indeterminate_status_codes": [403, 429, 503, 999],
        "live_status_codes": [200, 201, 204, 301, 302, 307, 308],
        "auth_required_status_codes": [401],
        "cloudflare_challenge_markers": {
            "headers": ["cf-ray"],
            "body_titles": ["Just a moment", "Attention Required"],
        },
    }
    raw.update(overrides)
    return UL.Config(raw=raw, plugin_version="9.9.9")


class TestGovSuffix(unittest.TestCase):
    def test_matches_gov_suffix(self):
        self.assertTrue(UL._is_gov_suffix("www.gov.uk"))
        self.assertTrue(UL._is_gov_suffix("irs.gov"))
        self.assertTrue(UL._is_gov_suffix("www.legifrance.gouv.fr"))
        self.assertTrue(UL._is_gov_suffix("www.gob.es"))
        self.assertTrue(UL._is_gov_suffix("sat.gob.mx"))

    def test_non_gov(self):
        self.assertFalse(UL._is_gov_suffix("github.com"))
        self.assertFalse(UL._is_gov_suffix("eur-lex.europa.eu"))


class TestHostPolicy(unittest.TestCase):
    def test_explicit_override_wins(self):
        cfg = make_cfg()
        p = cfg.host_policy("eur-lex.europa.eu")
        self.assertEqual(p.concurrency, 1)
        self.assertEqual(p.interval_ms, 10000)

    def test_gov_suffix_default(self):
        cfg = make_cfg()
        p = cfg.host_policy("www.gov.uk")
        self.assertEqual(p.concurrency, 1)
        self.assertEqual(p.interval_ms, 1000)

    def test_default_for_unknown(self):
        cfg = make_cfg()
        p = cfg.host_policy("example.com")
        self.assertEqual(p.concurrency, 2)
        self.assertEqual(p.interval_ms, 500)


class TestClassify(unittest.TestCase):
    def test_2xx_is_live(self):
        cfg = make_cfg()
        cls, _ = UL._classify(200, "", {}, cfg)
        self.assertEqual(cls, UL.LIVE)

    def test_3xx_is_redirect_live(self):
        cfg = make_cfg()
        cls, _ = UL._classify(301, "", {}, cfg)
        self.assertEqual(cls, UL.REDIRECT_LIVE)

    def test_404_dead(self):
        cfg = make_cfg()
        cls, _ = UL._classify(404, "", {}, cfg)
        self.assertEqual(cls, UL.DEAD)

    def test_401_auth_required(self):
        cfg = make_cfg()
        cls, _ = UL._classify(401, "", {}, cfg)
        self.assertEqual(cls, UL.AUTH_REQUIRED)

    def test_403_indeterminate(self):
        cfg = make_cfg()
        cls, _ = UL._classify(403, "", {}, cfg)
        self.assertEqual(cls, UL.INDETERMINATE)

    def test_429_rate_limited(self):
        cfg = make_cfg()
        cls, _ = UL._classify(429, "", {}, cfg)
        self.assertEqual(cls, UL.RATE_LIMITED)

    def test_999_bot_blocked(self):
        cfg = make_cfg()
        cls, _ = UL._classify(999, "", {}, cfg)
        self.assertEqual(cls, UL.BOT_BLOCKED)

    def test_cf_header_bot_blocked(self):
        cfg = make_cfg()
        cls, note = UL._classify(403, "", {"cf-ray": "abcd"}, cfg)
        self.assertEqual(cls, UL.BOT_BLOCKED)
        self.assertIn("cloudflare", note.lower())

    def test_cf_title_bot_blocked(self):
        cfg = make_cfg()
        cls, _ = UL._classify(403, "Just a moment...", {}, cfg)
        self.assertEqual(cls, UL.BOT_BLOCKED)

    def test_timeout(self):
        cfg = make_cfg()
        cls, _ = UL._classify(0, "", {}, cfg)
        self.assertEqual(cls, UL.TIMEOUT)


class TestHeadGetFallback(unittest.TestCase):
    """check_one() must retry with GET when HEAD returns any non-success.

    Locks in the 2026-05-27 triage finding: 74 of 267 reported-DEAD URLs were
    false positives because the checker only retried GET on (0, 403, 405, 5xx).
    Real-world HEAD-vs-GET mismatch patterns observed: HEAD=400 (armstat.am
    pattern), HEAD=404 (boi.org.il/ird.gov.lk bot-detection-fake-404), HEAD=406.
    """

    def _run_check(self, head_status: int, get_status: int):
        import asyncio

        cfg = make_cfg()
        calls = []

        async def fake_request(session, method, url, cfg_arg):
            calls.append(method)
            status = head_status if method == "HEAD" else get_status
            return status, "", {}, url

        class _FakeThrottle:
            def __init__(self):
                import asyncio as _a
                self.sem = _a.Semaphore(1)

            async def gate(self):
                return None

        class _FakeLimiter:
            async def acquire(self):
                return None

        class _FakeRobots:
            async def can_fetch(self, url):
                return True

        async def runner():
            orig_req = UL._http_request
            UL._http_request = fake_request
            try:
                r = await UL.check_one(None, "https://example.test/", cfg, _FakeThrottle(), _FakeLimiter(), _FakeRobots())
                return r, list(calls)
            finally:
                UL._http_request = orig_req

        return asyncio.run(runner())

    def test_head_400_then_get_200_is_live(self):
        # armstat.am pattern: HEAD-method-rejection 400 but GET-with-UA returns 200
        result, calls = self._run_check(head_status=400, get_status=200)
        self.assertEqual(result.cls, UL.LIVE)
        self.assertEqual(calls, ["HEAD", "GET"])

    def test_head_404_then_get_200_is_live(self):
        # boi.org.il / ird.gov.lk pattern: bot-detection serves 404 to HEAD, 200 to browser GET
        result, calls = self._run_check(head_status=404, get_status=200)
        self.assertEqual(result.cls, UL.LIVE)
        self.assertEqual(calls, ["HEAD", "GET"])

    def test_head_406_then_get_200_is_live(self):
        # 406 Not Acceptable on HEAD; some WAFs reject Accept: */* with HEAD
        result, calls = self._run_check(head_status=406, get_status=200)
        self.assertEqual(result.cls, UL.LIVE)
        self.assertEqual(calls, ["HEAD", "GET"])

    def test_head_200_skips_get(self):
        # Happy path: HEAD already succeeds, no GET retry
        result, calls = self._run_check(head_status=200, get_status=200)
        self.assertEqual(result.cls, UL.LIVE)
        self.assertEqual(calls, ["HEAD"])  # GET should NOT be called

    def test_head_404_then_get_404_is_dead(self):
        # Real DEAD: both HEAD and GET return 404
        result, calls = self._run_check(head_status=404, get_status=404)
        self.assertEqual(result.cls, UL.DEAD)
        self.assertEqual(calls, ["HEAD", "GET"])

    def test_head_301_skips_get(self):
        # Redirect on HEAD is enough — no GET retry
        result, calls = self._run_check(head_status=301, get_status=200)
        self.assertEqual(result.cls, UL.REDIRECT_LIVE)
        self.assertEqual(calls, ["HEAD"])


class TestCacheTTL(unittest.TestCase):
    def test_fresh_live_within_30d(self):
        cfg = make_cfg()
        now = datetime.now(timezone.utc)
        entry = {"cls": "LIVE", "checked_at": (now - timedelta(days=10)).isoformat()}
        self.assertTrue(UL.cache_is_fresh(entry, cfg))

    def test_stale_live_after_30d(self):
        cfg = make_cfg()
        now = datetime.now(timezone.utc)
        entry = {"cls": "LIVE", "checked_at": (now - timedelta(days=31)).isoformat()}
        self.assertFalse(UL.cache_is_fresh(entry, cfg))

    def test_auth_required_7d_window(self):
        cfg = make_cfg()
        now = datetime.now(timezone.utc)
        fresh = {"cls": "AUTH_REQUIRED", "checked_at": (now - timedelta(days=6)).isoformat()}
        stale = {"cls": "AUTH_REQUIRED", "checked_at": (now - timedelta(days=8)).isoformat()}
        self.assertTrue(UL.cache_is_fresh(fresh, cfg))
        self.assertFalse(UL.cache_is_fresh(stale, cfg))

    def test_dead_never_cached_as_fresh(self):
        cfg = make_cfg()
        now = datetime.now(timezone.utc)
        entry = {"cls": "DEAD", "checked_at": now.isoformat()}
        self.assertFalse(UL.cache_is_fresh(entry, cfg))

    def test_indeterminate_never_fresh(self):
        cfg = make_cfg()
        now = datetime.now(timezone.utc)
        entry = {"cls": "INDETERMINATE", "checked_at": now.isoformat()}
        self.assertFalse(UL.cache_is_fresh(entry, cfg))


class TestScore(unittest.TestCase):
    def test_all_live_score_100(self):
        cfg = make_cfg()
        entries = {f"https://x/{i}": {"cls": "LIVE", "fail_streak": 0, "checked_at": "x"} for i in range(10)}
        s = UL.compute_score(entries, cfg)
        self.assertEqual(s["score"], 100)
        self.assertEqual(s["confirmed_dead_count"], 0)

    def test_dead_below_fail_streak_not_counted(self):
        cfg = make_cfg()
        entries = {
            "https://a": {"cls": "LIVE", "fail_streak": 0, "checked_at": "x"},
            "https://b": {"cls": "DEAD", "fail_streak": 1, "checked_at": "x"},
            "https://c": {"cls": "DEAD", "fail_streak": 2, "checked_at": "x"},
        }
        s = UL.compute_score(entries, cfg)
        self.assertEqual(s["confirmed_dead_count"], 0)
        self.assertEqual(s["score"], 100)
        self.assertEqual(len(s["pending_dead"]), 2)

    def test_dead_at_fail_streak_threshold_counted(self):
        cfg = make_cfg()
        entries = {
            "https://a": {"cls": "LIVE", "fail_streak": 0, "checked_at": "x"},
            "https://b": {"cls": "DEAD", "fail_streak": 3, "checked_at": "x"},
        }
        s = UL.compute_score(entries, cfg)
        self.assertEqual(s["confirmed_dead_count"], 1)
        self.assertEqual(s["score"], 50)

    def test_excluded_hosts_dropped_from_denominator(self):
        cfg = make_cfg()
        entries = {
            "https://a": {"cls": "LIVE", "fail_streak": 0, "checked_at": "x"},
            "https://linkedin.com/x": {"cls": "EXCLUDED", "fail_streak": 0, "checked_at": "x"},
        }
        s = UL.compute_score(entries, cfg)
        self.assertEqual(s["counted"], 1)
        self.assertEqual(s["score"], 100)

    def test_indeterminate_counted_as_alive(self):
        cfg = make_cfg()
        entries = {
            "https://a": {"cls": "INDETERMINATE", "fail_streak": 0, "checked_at": "x"},
            "https://b": {"cls": "BOT_BLOCKED", "fail_streak": 0, "checked_at": "x"},
        }
        s = UL.compute_score(entries, cfg)
        self.assertEqual(s["confirmed_dead_count"], 0)
        self.assertEqual(s["score"], 100)


class TestRandomRefresh(unittest.TestCase):
    def test_zero_pct_returns_empty(self):
        self.assertEqual(UL.pick_random_refresh(["a", "b", "c"], 0), set())

    def test_10pct_of_10_is_1(self):
        s = UL.pick_random_refresh([f"u{i}" for i in range(10)], 10, seed=42)
        self.assertEqual(len(s), 1)

    def test_seeded_is_reproducible(self):
        urls = [f"u{i}" for i in range(100)]
        a = UL.pick_random_refresh(urls, 10, seed=42)
        b = UL.pick_random_refresh(urls, 10, seed=42)
        self.assertEqual(a, b)


class TestPruneCache(unittest.TestCase):
    def test_removes_stale_urls(self):
        cache = {"https://a": {"cls": "LIVE"}, "https://b": {"cls": "LIVE"}}
        removed = UL.prune_cache(cache, {"https://a"})
        self.assertEqual(removed, 1)
        self.assertNotIn("https://b", cache)
        self.assertIn("https://a", cache)


class TestExtractURLs(unittest.TestCase):
    """Smoke-test the extractor against a tmp md file."""

    def test_extracts_simple_urls(self):
        import tempfile
        orig_root = UL.ROOT
        try:
            with tempfile.TemporaryDirectory() as tmp:
                tmp_path = Path(tmp)
                (tmp_path / "a.md").write_text("Hello <https://example.gov/p1>\nSee https://gov.uk/x")
                (tmp_path / "test-fixtures.md").write_text("https://should-be-skipped.com")
                UL.ROOT = tmp_path
                urls = UL.extract_urls()
                self.assertIn("https://gov.uk/x", urls)
                self.assertNotIn("https://should-be-skipped.com", urls)
        finally:
            UL.ROOT = orig_root


if __name__ == "__main__":
    unittest.main(verbosity=2)
