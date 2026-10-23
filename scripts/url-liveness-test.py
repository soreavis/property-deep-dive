#!/usr/bin/env python3
"""Unit tests for scripts/url-liveness.py — deterministic parts only.

Network-level aiohttp checking is validated by the workflow's dry-run job,
not here.

Run: python3 scripts/url-liveness-test.py
"""

from __future__ import annotations

import asyncio
import contextlib
import socket
import ssl
import sys
import threading
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest import mock

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


class _FakeThrottle:
    def __init__(self):
        self.sem = asyncio.Semaphore(1)

    async def gate(self):
        return None


class _FakeLimiter:
    async def acquire(self):
        return None


class _FakeRobots:
    async def can_fetch(self, url):
        return True


def run_check_one(respond, url="https://example.test/", cfg=None):
    """Run check_one with _http_request replaced by respond(method, url) -> Response; return (result, calls)."""
    cfg = cfg or make_cfg()
    calls = []

    async def fake_request(session, method, target, cfg_arg):
        calls.append((method, target))
        return respond(method, target)

    async def runner():
        with mock.patch.object(UL, "_http_request", fake_request):
            return await UL.check_one(None, url, cfg, _FakeThrottle(), _FakeLimiter(), _FakeRobots())

    return asyncio.run(runner()), calls


def single_attempt_cfg():
    cfg = make_cfg()
    cfg.raw["global"]["max_retries"] = 1
    return cfg


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

    def test_connect_failed_is_timeout(self):
        cfg = make_cfg()
        cls, note = UL._classify(UL.CONNECT_FAILED, "", {}, cfg)
        self.assertEqual(cls, UL.TIMEOUT)
        self.assertIn("TLS", note)


class TestHeadGetFallback(unittest.TestCase):
    """check_one() must retry with GET when HEAD returns any non-success.

    Locks in the 2026-05-27 triage finding: 74 of 267 reported-DEAD URLs were
    false positives because the checker only retried GET on (0, 403, 405, 5xx).
    Real-world HEAD-vs-GET mismatch patterns observed: HEAD=400 (armstat.am
    pattern), HEAD=404 (boi.org.il/ird.gov.lk bot-detection-fake-404), HEAD=406.
    """

    def _run_check(self, head_status: int, get_status: int):
        result, calls = run_check_one(
            lambda method, url: UL.Response(head_status if method == "HEAD" else get_status, "", {}, url)
        )
        return result, [method for method, _ in calls]

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


def _gaierror(errno: int) -> socket.gaierror:
    return socket.gaierror(errno, "resolver says no")


NOERROR, SERVFAIL, NX = 0, 2, UL.RCODE_NXDOMAIN
REFUSED = "refused"


@contextlib.contextmanager
def fake_resolver(rcode, decoy=False, drop=0):
    """127.0.0.1 UDP resolver replying to every query after the first drop with rcode, or never when rcode is None.

    decoy first sends a NOERROR reply with another id, which must be ignored. Yields (address, queries).
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("127.0.0.1", 0))
    sock.settimeout(0.01)
    queries, stop = [], threading.Event()

    def serve():
        while not stop.is_set():
            try:
                query, peer = sock.recvfrom(512)
            except TimeoutError:
                continue
            queries.append(query)
            if len(queries) <= drop:
                continue
            if decoy:
                sock.sendto(bytes([query[0] ^ 1, query[1], 0x81, 0x80]) + query[4:], peer)
            if rcode is not None:
                sock.sendto(query[:2] + bytes([0x81, 0x80 | rcode]) + query[4:], peer)

    thread = threading.Thread(target=serve)
    thread.start()
    try:
        yield sock.getsockname(), queries
    finally:
        stop.set()
        thread.join()
        sock.close()


def refused_address():
    """A 127.0.0.1 UDP port nothing listens on, so a query socket connected to it gets ECONNREFUSED."""
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind(("127.0.0.1", 0))
        return sock.getsockname()


@contextlib.contextmanager
def resolvers(*specs, decoy=False, drop=0):
    """Point DNS_RESOLVERS at one fake per spec (an RCODE, None or REFUSED); yields their query logs."""
    with contextlib.ExitStack() as stack:
        addrs, logs = [], []
        for spec in specs:
            addr, queries = (refused_address(), []) if spec == REFUSED else stack.enter_context(fake_resolver(spec, decoy, drop))
            addrs.append(addr)
            logs.append(queries)
        stack.enter_context(mock.patch.object(UL, "DNS_RESOLVERS", tuple(addrs)))
        yield logs


class TestDnsPrePass(unittest.TestCase):
    def setUp(self):
        patcher = mock.patch.object(UL, "DNS_RESOLVERS", ())  # tests never reach the real resolvers
        patcher.start()
        self.addCleanup(patcher.stop)

    def _lookup(self, side_effect, *hosts):
        async def runner():
            dns = UL.DnsCache()
            return await asyncio.gather(*(dns.is_nxdomain(h) for h in hosts))

        with mock.patch.object(socket, "getaddrinfo", side_effect=side_effect) as gai:
            return asyncio.run(runner()), gai

    def test_noname_confirmed_by_resolvers_is_nxdomain(self):
        with resolvers(NX, NX) as logs:
            (nx,), gai = self._lookup(_gaierror(socket.EAI_NONAME), "gone.example")
        self.assertTrue(nx)
        self.assertEqual(gai.call_count, 1)
        for queries in logs:
            self.assertEqual(len(queries), 1)
            self.assertTrue(queries[0].endswith(b"\x04gone\x07example\x00\x00\x01\x00\x01"))

    def test_servfail_no_address_or_disagreement_is_not_nxdomain(self):
        # macOS getaddrinfo says EAI_NONAME for all of these; only RCODE 3 means the name does not exist.
        for rcodes in ((SERVFAIL, SERVFAIL), (NOERROR, NOERROR), (NX, NOERROR), (SERVFAIL, NX)):
            with self.subTest(rcodes=rcodes), resolvers(*rcodes):
                (nx,), _ = self._lookup(_gaierror(socket.EAI_NONAME), "live.example")
                self.assertFalse(nx)

    def test_silent_or_refused_resolver_withholds_nxdomain(self):
        for rcodes in ((NX, None), (REFUSED, NX)):
            with self.subTest(rcodes=rcodes), resolvers(*rcodes) as logs, \
                    mock.patch.object(UL, "DNS_QUERY_TIMEOUT_S", 0.1):
                (nx,), _ = self._lookup(_gaierror(socket.EAI_NONAME), "gone.example")
                self.assertFalse(nx)
                if rcodes[1] is None:
                    self.assertEqual(len(logs[1]), UL.DNS_QUERY_TRIES)

    def test_lost_reply_is_resent(self):
        with resolvers(NX, NX, drop=1) as logs, mock.patch.object(UL, "DNS_QUERY_TIMEOUT_S", 0.1):
            (nx,), _ = self._lookup(_gaierror(socket.EAI_NONAME), "gone.example")
        self.assertTrue(nx)
        self.assertEqual([len(queries) for queries in logs], [2, 2])

    def test_reply_with_another_id_is_ignored(self):
        with resolvers(NX, decoy=True):
            (nx,), _ = self._lookup(_gaierror(socket.EAI_NONAME), "gone.example")
        self.assertTrue(nx)

    def test_temporary_resolver_error_is_not_nxdomain(self):
        with resolvers(NX) as (queries,):
            (nx,), gai = self._lookup(_gaierror(socket.EAI_AGAIN), "flaky.example")
        self.assertFalse(nx)
        self.assertEqual(gai.call_count, 1)
        self.assertEqual(queries, [])

    def test_idna_error_is_not_nxdomain(self):
        (nx,), _ = self._lookup(UnicodeError("label empty or too long"), "a" * 64 + ".example")
        self.assertFalse(nx)

    def test_each_host_resolved_once(self):
        results, gai = self._lookup(lambda *a, **k: [], "a.example", "a.example", "b.example", "a.example")
        self.assertEqual(results, [False] * 4)
        self.assertEqual(gai.call_count, 2)

    def test_backlog_does_not_delay_aiohttp_lookups(self):
        # aiohttp resolves on the loop's default executor; a slow pre-pass backlog must not queue ahead of it.
        release = threading.Event()

        def gai(host, *args, **kwargs):
            if host != "fast.example":
                release.wait(5)
            return []

        async def runner():
            dns = UL.DnsCache()
            backlog = [asyncio.ensure_future(dns.is_nxdomain(f"h{i}.example")) for i in range(40)]
            await asyncio.sleep(0.01)
            fast = asyncio.ensure_future(asyncio.get_running_loop().getaddrinfo("fast.example", None))
            done, _ = await asyncio.wait([fast], timeout=2)
            release.set()
            await asyncio.gather(fast, *backlog)
            return fast in done

        with mock.patch.object(socket, "getaddrinfo", side_effect=gai):
            self.assertTrue(asyncio.run(runner()))

    def test_confirmations_hold_no_pool_thread(self):
        # Waiting on a silent resolver must leave the 8-thread DNS pool free for other hosts' lookups.
        def gai(host, *args, **kwargs):
            if host == "ok.example":
                return []
            raise _gaierror(socket.EAI_NONAME)

        async def runner():
            dns = UL.DnsCache()
            backlog = [asyncio.ensure_future(dns.is_nxdomain(f"h{i}.example")) for i in range(16)]
            await asyncio.sleep(0.05)
            ok = asyncio.ensure_future(dns.is_nxdomain("ok.example"))
            done, _ = await asyncio.wait([ok], timeout=UL.DNS_QUERY_TIMEOUT_S / 2)
            backlog_waiting = not any(t.done() for t in backlog)
            return ok in done, backlog_waiting, await asyncio.gather(*backlog)

        with resolvers(None), mock.patch.object(UL, "DNS_QUERY_TIMEOUT_S", 0.3), \
                mock.patch.object(socket, "getaddrinfo", side_effect=gai):
            ok_done, backlog_waiting, verdicts = asyncio.run(runner())
        self.assertTrue(ok_done)
        self.assertTrue(backlog_waiting)
        self.assertEqual(verdicts, [False] * 16)

    def _run(self, gai_error, cache, *rcodes):
        url = "https://gone.example/page"
        check_one = mock.AsyncMock(return_value=UL.CheckResult(url=url, cls=UL.LIVE, checked_at="x"))
        with resolvers(*rcodes), mock.patch.object(socket, "getaddrinfo", side_effect=gai_error), \
                mock.patch.object(UL, "check_one", check_one), \
                mock.patch.object(UL.RobotsCache, "crawl_delay", mock.AsyncMock(return_value=None)):
            asyncio.run(UL.run_check([url], make_cfg(), cache, set()))
        return cache[url], check_one

    def test_nxdomain_skips_http_and_extends_fail_streak(self):
        prior = {"https://gone.example/page": {"cls": "DEAD", "fail_streak": 2, "checked_at": "x"}}
        entry, check_one = self._run(_gaierror(socket.EAI_NONAME), prior, NX, NX)
        self.assertEqual(entry["cls"], UL.NXDOMAIN)
        self.assertEqual(entry["fail_streak"], 3)
        check_one.assert_not_called()
        self.assertEqual(UL.compute_score(prior, make_cfg())["confirmed_dead_count"], 1)

    def test_temporary_resolver_error_still_runs_http_check(self):
        entry, check_one = self._run(_gaierror(socket.EAI_AGAIN), {})
        self.assertEqual(entry["cls"], UL.LIVE)
        check_one.assert_called_once()

    def test_noname_with_servfail_runs_http_check(self):
        entry, check_one = self._run(_gaierror(socket.EAI_NONAME), {}, SERVFAIL, SERVFAIL)
        self.assertEqual(entry["cls"], UL.LIVE)
        check_one.assert_called_once()


class _RaisingSession:
    def __init__(self, exc):
        self.exc = exc

    def request(self, *args, **kwargs):
        self.timeout = kwargs["timeout"]
        raise self.exc


class TestHttpOnlyFallback(unittest.TestCase):
    def _status_for(self, exc):
        resp = asyncio.run(UL._http_request(_RaisingSession(exc), "GET", "https://example.test/", make_cfg()))
        return resp.status

    def test_refused_connection_is_connect_failed(self):
        exc = UL.aiohttp.ClientConnectorError(mock.Mock(), ConnectionRefusedError(61, "refused"))
        self.assertEqual(self._status_for(exc), UL.CONNECT_FAILED)

    def test_tls_error_is_connect_failed(self):
        exc = UL.aiohttp.ClientConnectorSSLError(mock.Mock(), ssl.SSLError(1, "wrong version number"))
        self.assertEqual(self._status_for(exc), UL.CONNECT_FAILED)

    def test_connect_timeout_is_connect_failed(self):
        session = _RaisingSession(UL.aiohttp.ConnectionTimeoutError("Connection timeout to host"))
        resp = asyncio.run(UL._http_request(session, "GET", "https://example.test/", make_cfg()))
        self.assertEqual(resp.status, UL.CONNECT_FAILED)
        self.assertEqual(session.timeout.sock_connect, UL.CONNECT_TIMEOUT_S)

    def test_dns_and_read_timeouts_are_not_connect_failed(self):
        dns = UL.aiohttp.ClientConnectorError(mock.Mock(), _gaierror(socket.EAI_AGAIN))
        self.assertEqual(self._status_for(dns), 0)
        self.assertEqual(self._status_for(asyncio.TimeoutError()), 0)
        self.assertEqual(self._status_for(UL.aiohttp.SocketTimeoutError()), 0)

    def _respond(self, https_status, http_status):
        def respond(method, url):
            return UL.Response(https_status if url.startswith("https://") else http_status, "", {}, url)
        return respond

    def test_live_over_plain_http_is_http_only(self):
        result, calls = run_check_one(self._respond(UL.CONNECT_FAILED, 200), cfg=single_attempt_cfg())
        self.assertEqual(result.cls, UL.HTTP_ONLY)
        self.assertEqual(result.final_url, "http://example.test/")
        self.assertEqual(calls[-1], ("GET", "http://example.test/"))

    def test_plain_http_failing_too_stays_timeout(self):
        result, calls = run_check_one(self._respond(UL.CONNECT_FAILED, UL.CONNECT_FAILED), cfg=single_attempt_cfg())
        self.assertEqual(result.cls, UL.TIMEOUT)
        self.assertEqual(len(calls), 3)

    def test_timeout_does_not_try_plain_http(self):
        result, calls = run_check_one(self._respond(0, 200), cfg=single_attempt_cfg())
        self.assertEqual(result.cls, UL.TIMEOUT)
        self.assertTrue(all(url.startswith("https://") for _, url in calls))


HTML = {"content-type": "text/html; charset=utf-8"}


class TestMetaRefreshParse(unittest.TestCase):
    BASE = "https://a.example/old/page"

    def test_absolute_target(self):
        html = '<head><meta http-equiv="refresh" content="0; url=https://new.example/x"></head>'
        self.assertEqual(UL._meta_refresh_target(html, self.BASE), "https://new.example/x")

    def test_attribute_order_case_quotes_and_relative_url(self):
        html = "<HEAD><META CONTENT=\"5;URL='/moved'\" HTTP-EQUIV=\"Refresh\"></HEAD>"
        self.assertEqual(UL._meta_refresh_target(html, self.BASE), "https://a.example/moved")

    def test_entities_unescaped(self):
        html = '<meta http-equiv="refresh" content="0;url=/p?a=1&amp;b=2">'
        self.assertEqual(UL._meta_refresh_target(html, self.BASE), "https://a.example/p?a=1&b=2")

    def test_delay_only_and_non_http_targets_ignored(self):
        self.assertEqual(UL._meta_refresh_target('<meta http-equiv="refresh" content="30">', self.BASE), "")
        html = '<meta http-equiv="refresh" content="0;url=javascript:void(0)">'
        self.assertEqual(UL._meta_refresh_target(html, self.BASE), "")
        self.assertEqual(UL._meta_refresh_target("<title>x</title>", self.BASE), "")

    def test_long_delay_refresh_is_not_followed(self):
        for content in ("1200;url=/SessionExpired.aspx", "1800; url=/logout"):
            html = f'<meta http-equiv="refresh" content="{content}">'
            self.assertEqual(UL._meta_refresh_target(html, self.BASE), "")
        html = '<meta http-equiv="refresh" content="10.9;url=/stub">'
        self.assertEqual(UL._meta_refresh_target(html, self.BASE), "https://a.example/stub")

    def test_noscript_refresh_ignored(self):
        html = '<head><noscript><meta http-equiv="refresh" content="0;url=/nojs"></noscript></head>'
        self.assertEqual(UL._meta_refresh_target(html, self.BASE), "")
        html += '<meta http-equiv="refresh" content="0;url=/moved">'
        self.assertEqual(UL._meta_refresh_target(html, self.BASE), "https://a.example/moved")


class TestMetaRefreshFollow(unittest.TestCase):
    URL = "https://example.test/"

    def _run(self, pages):
        """pages: GET url -> (status, refresh). HEAD always answers 200 text/html."""
        def respond(method, url):
            if method == "HEAD":
                return UL.Response(200, "", HTML, url)
            status, refresh = pages[url]
            return UL.Response(status, "", HTML, url, refresh)
        return run_check_one(respond, url=self.URL)

    def test_classified_by_dead_target(self):
        result, calls = self._run({self.URL: (200, "https://example.test/new"), "https://example.test/new": (404, "")})
        self.assertEqual(result.cls, UL.DEAD)
        self.assertEqual(result.final_url, "https://example.test/new")
        self.assertIn("meta-refresh → https://example.test/new", result.note)
        self.assertEqual(calls, [("HEAD", self.URL), ("GET", self.URL), ("GET", "https://example.test/new")])

    def test_live_target(self):
        result, _ = self._run({self.URL: (200, "https://other.example/"), "https://other.example/": (200, "")})
        self.assertEqual(result.cls, UL.LIVE)
        self.assertEqual(result.final_url, "https://other.example/")

    def test_refresh_get_only_when_head_may_be_a_stub(self):
        def methods(length):
            _, calls = run_check_one(lambda m, u: UL.Response(200, "", HTML | {"Content-Length": length}, u))
            return [m for m, _ in calls]

        self.assertEqual(methods("50000"), ["HEAD"])
        self.assertEqual(methods("300"), ["HEAD", "GET"])

    def test_get_without_refresh_keeps_live_head(self):
        result, _ = self._run({self.URL: (403, "")})
        self.assertEqual(result.cls, UL.LIVE)
        self.assertEqual(result.note, "")

    def test_self_refresh_is_live_without_hops(self):
        result, calls = self._run({self.URL: (200, self.URL)})
        self.assertEqual(result.cls, UL.LIVE)
        self.assertEqual(len(calls), 2)

    def test_loop_stops_at_visited_url(self):
        b = "https://example.test/b"
        result, calls = self._run({self.URL: (200, b), b: (200, self.URL)})
        self.assertEqual(result.cls, UL.LIVE)
        self.assertEqual(calls[-1], ("GET", b))
        self.assertEqual(len(calls), 3)

    def test_hops_capped_at_follow_redirects_max(self):
        chain = [f"https://example.test/{i}" for i in range(10)]
        pages = {self.URL: (200, chain[0])} | {u: (200, chain[i + 1]) for i, u in enumerate(chain[:-1])}
        result, calls = self._run(pages)
        self.assertEqual(result.cls, UL.LIVE)
        self.assertEqual(len(calls), 2 + make_cfg().follow_redirects_max)


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

    def test_nxdomain_follows_fail_streak_and_http_only_is_alive(self):
        cfg = make_cfg()
        entries = {
            "https://a": {"cls": "NXDOMAIN", "fail_streak": 1, "checked_at": "x"},
            "https://b": {"cls": "NXDOMAIN", "fail_streak": 3, "checked_at": "x"},
            "https://c": {"cls": "HTTP_ONLY", "fail_streak": 0, "checked_at": "x"},
            "https://d": {"cls": "LIVE", "fail_streak": 0, "checked_at": "x"},
        }
        s = UL.compute_score(entries, cfg)
        self.assertEqual([d["url"] for d in s["confirmed_dead"]], ["https://b"])
        self.assertEqual([d["url"] for d in s["pending_dead"]], ["https://a"])
        self.assertEqual(s["score"], 75)


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

    def test_keeps_balanced_parentheses(self):
        import tempfile
        orig_root = UL.ROOT
        try:
            with tempfile.TemporaryDirectory() as tmp:
                tmp_path = Path(tmp)
                (tmp_path / "a.md").write_text(
                    "[CGT](https://ird.gov.lk/en/Type%20of%20Taxes/Capital%20Gain%20Tax%20(CGT).aspx) and "
                    "([Cayman](https://en.wikipedia.org/wiki/The_Bluff_(Cayman_Islands))) end."
                )
                UL.ROOT = tmp_path
                urls = UL.extract_urls()
                self.assertIn("https://ird.gov.lk/en/Type%20of%20Taxes/Capital%20Gain%20Tax%20(CGT).aspx", urls)
                self.assertIn("https://en.wikipedia.org/wiki/The_Bluff_(Cayman_Islands)", urls)
                self.assertNotIn("https://ird.gov.lk/en/Type%20of%20Taxes/Capital%20Gain%20Tax%20(CGT", urls)
        finally:
            UL.ROOT = orig_root


if __name__ == "__main__":
    unittest.main(verbosity=2)
