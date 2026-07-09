#!/usr/bin/env python3
"""Keyword filter for the regulatory feed watcher (.github/workflows/feed-watcher.yml).

Reads one RSS/Atom feed from disk and prints a Markdown bullet for every item
whose title *or* description matches the property-relevance keyword pattern.

Exit codes:
    0 — feed parsed (zero matches is a valid, healthy outcome)
    2 — feed unusable: malformed XML, or well-formed with zero items (soft-404)

Usage:
    python3 scripts/filter-feeds.py --name EC-Press --path _ci/EC-Press.xml \
        --keywords 'property|housing' --window-days 3
"""

from __future__ import annotations

import argparse
import html
import re
import sys
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from xml.etree import ElementTree

# Feeds carry 10-25 items and are polled daily; without a freshness window every
# poll re-reports the same items and opens a duplicate issue.
DEFAULT_WINDOW_DAYS = 3
SNIPPET_CHARS = 180


def localname(tag: str) -> str:
    return tag.rsplit("}", 1)[-1].lower()


def clean(raw: str | None) -> str:
    """Unescape entities, strip markup, collapse whitespace.

    Feed bodies are often double-escaped (`&lt;div&gt;` inside <description>), so
    unescape runs before tag-stripping and again after, to catch entities that
    were hidden inside the escaped markup.
    """
    if not raw:
        return ""
    text = html.unescape(raw)
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def child_text(item: ElementTree.Element, *names: str) -> str:
    for child in item:
        if localname(child.tag) in names:
            # CDATA is already merged into .text by ElementTree; .itertext()
            # additionally captures Atom content wrapped in inline XHTML.
            return clean("".join(child.itertext()))
    return ""


def item_link(item: ElementTree.Element) -> str:
    """RSS puts the URL in <link>text</link>; Atom puts it in <link href="..."/>."""
    fallback = ""
    for child in item:
        if localname(child.tag) != "link":
            continue
        href = child.get("href")
        if href:
            if child.get("rel", "alternate") == "alternate":
                return href.strip()
            fallback = fallback or href.strip()
        elif child.text and child.text.strip():
            return child.text.strip()
    return fallback


def item_date(item: ElementTree.Element) -> datetime | None:
    raw = child_text(item, "pubdate", "updated", "published", "date")
    if not raw:
        return None
    try:
        parsed = parsedate_to_datetime(raw)
    except (TypeError, ValueError):
        try:
            parsed = datetime.fromisoformat(raw.replace("Z", "+00:00"))
        except ValueError:
            return None
    return parsed.replace(tzinfo=timezone.utc) if parsed.tzinfo is None else parsed


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--name", required=True)
    ap.add_argument("--path", required=True)
    ap.add_argument("--keywords", required=True)
    ap.add_argument("--exclude", default="")
    ap.add_argument("--window-days", type=int, default=DEFAULT_WINDOW_DAYS)
    args = ap.parse_args()

    try:
        root = ElementTree.parse(args.path).getroot()
    except (ElementTree.ParseError, OSError) as exc:
        print(f"{args.name}: unparseable feed ({exc})", file=sys.stderr)
        return 2

    items = [el for el in root.iter() if localname(el.tag) in ("item", "entry")]
    if not items:
        print(f"{args.name}: 0 items — feed retired or soft-404", file=sys.stderr)
        return 2

    pattern = re.compile(rf"\b(?:{args.keywords})\b", re.IGNORECASE)
    excluder = re.compile(args.exclude, re.IGNORECASE) if args.exclude else None
    cutoff = datetime.now(timezone.utc) - timedelta(days=args.window_days)
    matched = stale = dropped = 0

    for item in items:
        title = child_text(item, "title")
        summary = child_text(item, "description", "summary", "content")
        # CJEU titles are bare case numbers ("101/... : null - Opinion of the
        # Advocate General"); the subject matter only ever appears in the body.
        haystack = f"{title} {summary}"
        if not pattern.search(haystack):
            continue
        # "property" alone matches "intellectual property" across EU press feeds.
        if excluder and excluder.search(haystack) and not pattern.search(
            excluder.sub(" ", haystack)
        ):
            dropped += 1
            continue
        published = item_date(item)
        if published and published < cutoff:
            stale += 1
            continue

        matched += 1
        print(f"- **[{args.name}]** {title or '(untitled)'}")
        if summary:
            snippet = summary[:SNIPPET_CHARS] + ("…" if len(summary) > SNIPPET_CHARS else "")
            print(f"  - {snippet}")
        link = item_link(item)
        if link:
            print(f"  - <{link}>")

    print(
        f"{args.name}: {len(items)} items, {matched} matched, {stale} older than "
        f"{args.window_days}d, {dropped} excluded",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
