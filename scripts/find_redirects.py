#!/usr/bin/env python3
"""Detect permanent (301/308) URL redirects in country playbooks where the
final URL is on the SAME registered root domain (e.g., gov.fr → www.gov.fr,
or impots.gouv.fr → www.impots.gouv.fr).

Cross-domain redirects are EXCLUDED — they may be hijacks, link-rot
forwarding services, or content moves that warrant manual review (and
potentially a source-tier downgrade).

Usage:
    python3 scripts/find_redirects.py [--max 20] [--out _ci/redirects.tsv]

Output (TSV): old_url\tnew_url\tplaybook_path
"""

import argparse
import sys
import urllib.request
import urllib.error
import re
from pathlib import Path
from urllib.parse import urlparse

PLAYBOOK_GLOB = "skills/property-deep-dive/countries/*/playbook.md"
URL_RE = re.compile(r"https?://[^\s<>\"'`)\]]+")
USER_AGENT = "property-deep-dive-ci/1.0 (+https://github.com/soreavis/property-deep-dive)"
TIMEOUT = 10


def root_domain(host: str) -> str:
    """Crude registered-domain extractor — last 2 labels for most TLDs, last 3 for known ccTLDs."""
    parts = host.lower().split(".")
    # Two-label ccTLDs that take 3 labels for registered domain (e.g., .co.uk, .com.au)
    two_label_cctlds = {"uk", "au", "nz", "za", "br", "mx", "ar", "pe", "co", "ec", "in", "id", "my",
                        "sg", "tw", "kr", "jp", "tr", "il", "ae", "sa", "qa", "om", "kw", "bh"}
    if len(parts) >= 3 and parts[-1] in two_label_cctlds and parts[-2] in {"co", "com", "net", "org", "gov", "edu", "ac"}:
        return ".".join(parts[-3:])
    return ".".join(parts[-2:]) if len(parts) >= 2 else host


def head_with_redirect(url: str) -> tuple[int, str | None]:
    """Return (initial_status, final_url) by manually following redirects.
    Returns (status, None) if no redirect or non-permanent redirect.
    """
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": USER_AGENT})
    try:
        # OpenerDirector with only HTTP/HTTPS handlers — no redirect handler — so 301/308
        # surface as HTTPError instead of being auto-followed. This lets us inspect the
        # first-hop status and Location header.
        no_follow = urllib.request.OpenerDirector()
        for h in [urllib.request.HTTPHandler(), urllib.request.HTTPSHandler()]:
            no_follow.add_handler(h)
        try:
            r = no_follow.open(req, timeout=TIMEOUT)
            return (r.status, None)
        except urllib.error.HTTPError as e:
            if e.code in (301, 308):
                new = e.headers.get("Location")
                if new and not new.startswith("http"):
                    # Relative redirect — resolve against original
                    from urllib.parse import urljoin
                    new = urljoin(url, new)
                return (e.code, new)
            return (e.code, None)
    except (urllib.error.URLError, TimeoutError, ConnectionError, OSError):
        return (0, None)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--max", type=int, default=20, help="Max redirects to report")
    ap.add_argument("--out", type=Path, default=Path("_ci/redirects.tsv"))
    args = ap.parse_args()

    args.out.parent.mkdir(parents=True, exist_ok=True)

    # Build (url, playbook) pairs
    pairs: list[tuple[str, Path]] = []
    seen: set[str] = set()
    for pb in Path().glob(PLAYBOOK_GLOB):
        text = pb.read_text(encoding="utf-8")
        for m in URL_RE.finditer(text):
            url = m.group(0).rstrip(".,;:)")
            if url in seen:
                continue
            seen.add(url)
            pairs.append((url, pb))

    print(f"Scanning {len(pairs)} unique URLs across {len(set(p for _, p in pairs))} playbooks", file=sys.stderr)

    found: list[tuple[str, str, str]] = []
    for url, pb in pairs:
        if len(found) >= args.max:
            break
        status, new = head_with_redirect(url)
        if status not in (301, 308) or not new:
            continue
        old_root = root_domain(urlparse(url).hostname or "")
        new_root = root_domain(urlparse(new).hostname or "")
        if old_root != new_root:
            # Cross-domain redirect — skip for safety, flag in stderr
            print(f"SKIP cross-domain: {url} -> {new}", file=sys.stderr)
            continue
        if url == new:
            continue
        # Find ALL playbooks that contain this URL (the URL might appear in multiple)
        for affected in Path().glob(PLAYBOOK_GLOB):
            if url in affected.read_text(encoding="utf-8"):
                found.append((url, new, str(affected)))
                break  # just record one occurrence — sed will replace globally

    with args.out.open("w", encoding="utf-8") as f:
        for old, new, pb in found:
            f.write(f"{old}\t{new}\t{pb}\n")

    print(f"Found {len(found)} same-root permanent redirects", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
