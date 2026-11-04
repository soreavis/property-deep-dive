#!/usr/bin/env python3
"""Number provenance: a figure a patch introduces must trace to its evidence, by script.

Hallucinated and miscopied figures read as fluently as real ones, so this does not ask a model.
For each new money or percentage figure of a patch:

  * grounded    a number on an evidence page falls inside the figure's rounding interval
                (`€85k` covers 84,500-85,500; `2.5%` covers 2.45-2.55)
  * near miss   not grounded, but a page number is a digit permutation of it (same orbit of the
                symmetric group: same sorted digits) or one digit away. Those are the two classic
                copying errors, and the page number is the likely correct value.
  * underived   the line labels the figure as computed or estimated, and no expression of up to
                three operands from the line and its evidence gives it. This test is one-sided:
                with many operands something always fits, so a pass proves little and a failure
                says a lot.
  * ungrounded  anything else, on a page the script could read.

A quote copied from the page is checked by k-gram containment (Broder 1997), which survives
reflowed whitespace and fails on invented text.

This is a second key, not the main defence. On 691 raw proposals of the 2026-10-23 gap run it
flagged 16 and confirmed no digit error, while refuters caught 149 issues, mostly of scope, date
and label, which no digit check can see. So a flag asks the refuter to read the figure itself,
and only a figure nobody cleared is held back.
"""
from __future__ import annotations

import bisect
import importlib.util
import itertools
import operator
import re
import sys
from pathlib import Path

_spec = importlib.util.spec_from_file_location("evidence_ledger", Path(__file__).parent / "evidence-ledger.py")
EL = sys.modules.get("evidence_ledger")
if EL is None:
    EL = sys.modules["evidence_ledger"] = importlib.util.module_from_spec(_spec)
    _spec.loader.exec_module(EL)

PAGE_NUMBER = re.compile(r"\d{1,3}(?: \d{3})+(?:[.,]\d+)?|\d(?:[\d.,  ]*\d)?")
RAW_NUMBER = re.compile(r"(\d[\d.,   ]*\d|\d)\s?(k|m|bn|million|billion)?\b", re.I)
SCALE = {"k": 1e3, "m": 1e6, "million": 1e6, "bn": 1e9, "billion": 1e9}
LABELLED = re.compile(r"(~|≈|\best\.|\bcomputed\b|\bverify (at|with)\b|data not publicly available)", re.I)
OPS = (operator.add, operator.sub, operator.mul, operator.truediv)
MAX_OPERANDS, QUOTE_K, QUOTE_MIN = 10, 5, 0.8


def readings(token: str) -> list[float]:
    """Every value a printed number can mean: 12.951 is twelve thousand in Serbia, near 13 elsewhere."""
    token = re.sub(r"[   ]", "", token)
    seps = re.findall(r"[.,]", token)
    plain = re.sub(r"[.,]", "", token)
    out = {float(plain)} if plain else set()
    if seps:
        head, tail = re.split(r"[.,](?=\d*$)", token)
        out.add(float(re.sub(r"[.,]", "", head) + "." + tail))
    return sorted(out)


class PageIndex:
    def __init__(self, text: str):
        tokens = PAGE_NUMBER.findall(text)
        self.values = sorted(v for t in tokens for v in readings(t))
        self.orbits: dict[str, set[str]] = {}
        for t in tokens:
            digits = re.sub(r"\D", "", t)
            if len(digits) >= 3:
                self.orbits.setdefault("".join(sorted(digits)), set()).add(digits)
        self.digits = {d for orbit in self.orbits.values() for d in orbit}

    def holds(self, lo: float, hi: float) -> bool:
        i = bisect.bisect_left(self.values, lo)
        return i < len(self.values) and self.values[i] <= hi

    def near_misses(self, digits: str) -> list[str]:
        same_orbit = self.orbits.get("".join(sorted(digits)), set()) - {digits}
        one_off = {digits[:i] + c + digits[i + 1:] for i in range(len(digits)) for c in "0123456789"} & self.digits - {digits}
        return sorted(same_orbit | one_off)


def rounding_interval(token: str, scale: float = 1.0) -> list[tuple[float, float]]:
    """Half a unit of the last printed digit either side, for each reading of the number."""
    out = []
    for v in readings(token):
        decimals = len(str(v).split(".")[1]) if v != int(v) else 0
        half = 0.5 * 10 ** -decimals
        out.append(((v - half) * scale, (v + half) * scale))
    return out


def figure_of(raw: str) -> tuple[str, float] | None:
    m = RAW_NUMBER.search(raw)
    return (m[1].strip(), SCALE.get((m[2] or "").lower(), 1.0)) if m else None


def new_figures(old: str, new: str) -> list[dict]:
    clean = lambda raw: raw.rstrip(",.;:) ")
    before = {clean(v["raw"]) for line in old.splitlines() for v in EL.salient_values(line)}
    return [v for line in new.splitlines() for v in EL.salient_values(line)
            if v["type"] in ("money", "pct") and clean(v["raw"]) not in before and figure_of(v["raw"])]


def expressions(operands: list[float]):
    """Values of every expression over up to three operands: each ordering (permutation) of the
    operands, each choice of operators, both ways of bracketing three."""
    for a, b in itertools.permutations(operands, 2):
        for f in OPS:
            try:
                yield f(a, b)
            except ZeroDivisionError:
                pass
    for a, b, c in itertools.permutations(operands, 3):
        for f, g in itertools.product(OPS, OPS):
            try:
                yield g(f(a, b), c)
                yield f(a, g(b, c))
            except ZeroDivisionError:
                pass


def operands_of(text: str) -> list[float]:
    vals = {v for t in PAGE_NUMBER.findall(text) for v in readings(t)}
    pcts = {v / 100 for m in re.findall(r"(\d[\d.,]*)\s?%", text) for v in readings(m)}
    return sorted(vals | pcts, key=lambda v: -v)[:MAX_OPERANDS]


def derivable(intervals: list[tuple[float, float]], operands: list[float]) -> bool:
    inside = lambda x: any(lo <= x <= hi for lo, hi in intervals)
    return any(inside(x) for x in expressions([o for o in operands if not inside(o)]))  # never from itself


def containment(quote: str, text: str) -> float:
    """Share of the quote's word k-grams found on the page."""
    def grams(s: str) -> set[tuple[str, ...]]:
        words = re.findall(r"\w+", s.casefold())
        return {tuple(words[i:i + QUOTE_K]) for i in range(max(len(words) - QUOTE_K + 1, 1))}
    q = grams(quote)
    return len(q & grams(text)) / len(q) if q else 0.0


def readable(fr) -> bool:
    """An .xls read as text comes back as noise, and silence there proves nothing."""
    text = fr.text or "" if fr and fr.status == "OK" else ""
    return len(text) >= 200 and text.count("�") < len(text) * 0.01


def audit_patch(item: dict, fetches: dict) -> dict:
    """{status: CLEAN | FLAGGED | UNVERIFIABLE, findings: [...]} for one patch."""
    evidence = [e for e in item.get("evidence", []) if isinstance(e, dict)]
    pages = [fetches[e["url"]] for e in evidence if readable(fetches.get(e.get("url")))]
    figures = new_figures(item.get("old", ""), item["new"])
    if not pages:
        return {"status": "UNVERIFIABLE" if figures else "CLEAN", "findings": []}
    every_page_read = len(pages) == len(evidence)  # else a missing figure may sit on the unread one
    index = PageIndex(" ".join(p.text for p in pages))
    facts = " ".join(str(e.get("fact", "")) for e in evidence)
    findings = []
    for line in item["new"].splitlines():
        labelled = bool(LABELLED.search(line))
        for v in new_figures(item.get("old", ""), line):
            token, scale = figure_of(v["raw"])
            intervals = rounding_interval(token, scale) + rounding_interval(token)
            if any(index.holds(lo, hi) for lo, hi in intervals):
                continue
            digits = re.sub(r"\D", "", token)
            miss = index.near_misses(digits) if len(digits) >= 4 else []
            if labelled:
                if not derivable(intervals, operands_of(f"{line} {facts}")):
                    findings.append({"figure": v["raw"], "kind": "underived"})
            elif every_page_read or miss:
                findings.append({"figure": v["raw"], "kind": "near miss" if miss else "ungrounded", "page_has": miss[:3]})
    for e in evidence:
        q, fr = e.get("quote"), fetches.get(e.get("url"))
        if q and readable(fr) and containment(q, fr.text) < QUOTE_MIN:
            findings.append({"figure": q[:60], "kind": "quote not on page", "url": e["url"]})
    return {"status": "FLAGGED" if findings else "CLEAN", "findings": findings}
