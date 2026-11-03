#!/usr/bin/env python3
"""Deterministic playbook checks that used to cost an agent pass or a hand rewrite.

  PROCESS NOTES  an added line must not describe how a page was fetched (status codes,
                 bot walls, fetch tools). The reader needs "could not be read for
                 verification on <date> — check it directly", not the fetch log.
  STALE DATA     an added "(YYYY data" two or more calendar years old must carry
                 "may have changed since" (CLAUDE.md, date-stamp rule).
  ARITHMETIC     an added "computed" expression with a stated result (a × b = c,
                 a ÷ b ≈ c, a + b = c) must hold to 1 %.
  RE-STAMP       a Status footer that says "re-verified as of D" next to a Per-section
                 verification table must list every fast-changing section the
                 playbook has, each dated D or later.

The line checks look only at lines added against --base, so text already on main never
blocks an unrelated PR. RE-STAMP reads each changed playbook whole.

    python3 scripts/check-playbooks.py                 # changed playbooks vs origin/main
    python3 scripts/check-playbooks.py --base main     # another base
    python3 scripts/check-playbooks.py --all           # every playbook, every line (report)
"""
import argparse
import datetime
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLAYBOOKS = "skills/property-deep-dive/countries/*/playbook.md"
FAST = ("price", "tax", "rental", "risks", "mains", "work", "cost benchmark")

PROCESS = re.compile(
    r"\b(automated (requests?|fetch\w*|reads?|checks?|clients?)|bot[- ]?(wall|check)\w*"
    r"|scripted clients?|non-browser|curl\b|tavily|webfetch|wayback machine snapshots?"
    r"|read (through|via) wayback|(returns?|returned|answers?) (http )?[45]\d\d\b"
    r"|HTTP [45]\d\d\b|ECONNREFUSED)", re.I)
DATA_YEAR = re.compile(r"\((20\d\d) data\b")
STALE_OK = "may have changed since"

NUM = r"[€$£¥]?\d(?:[\d,\u00a0\u202f]*\d)?(?:\.\d+)?(?:\s?(?:%|[kKmM]\b|bn\b))?"
TERM = rf"[+−-]?{NUM}(?:\s*[×x*÷/+−-]\s*{NUM})*"
CHAIN = re.compile(rf"{TERM}(?:\s*[=≈]\s*{TERM})+")
SCALE = {"k": 1e3, "m": 1e6, "bn": 1e9}

STAMP = re.compile(r"re-verified as of (\d{4}-\d{2}-\d{2})")
TABLE_HEAD = re.compile(r"^#{2,4} Per-section verification", re.M)
SECTION_HEAD = re.compile(r"^##\s+(?:Section:\s*)?(.+?)\s*$", re.M)


def number(tok: str, pct_scale: bool) -> float | None:
    t = tok.strip().lstrip("€$£¥+").replace("−", "-").replace("\u00a0", "").replace("\u202f", "").lower()
    m = re.fullmatch(r"(-?\d[\d,]*(?:\.\d+)?)(%|k|m|bn)?", t)
    if not m:
        return None
    digits, unit = m.groups()
    if "," in digits and not re.fullmatch(r"-?\d{1,3}(,\d{3})+(\.\d+)?", digits):
        return None  # a decimal comma or a malformed group: ambiguous, skip rather than guess
    v = float(digits.replace(",", ""))
    if unit == "%":
        return v / 100 if pct_scale else v
    return v * SCALE.get(unit or "", 1)


def evaluate(term: str, pct_scale: bool) -> float | None:
    parts = re.split(r"\s*([×x*÷/+−-])\s*", term.strip())
    if parts and parts[0] == "":
        parts = ["0"] + parts[1:]  # leading sign
    expr = []
    for i, p in enumerate(parts):
        if i % 2:
            expr.append({"×": "*", "x": "*", "÷": "/", "−": "-"}.get(p, p))
        else:
            v = number(p, pct_scale)
            if v is None:
                return None
            expr.append(repr(v))
    try:
        return eval("".join(expr), {"__builtins__": {}})  # only floats and + - * / reach here
    except ZeroDivisionError:
        return None


def arithmetic_errors(line: str) -> list[str]:
    """Each side of `a = b ≈ c` must equal the next (1 % for =, 3 % for ≈). Percent signs are
    tried both as ×0.01 and as a bare unit, since `11 + 21 + 12 = 44 %` adds percentages."""
    if "comput" not in line.lower():
        return []
    out = []
    for m in CHAIN.finditer(line):
        sides = re.split(r"\s*([=≈])\s*", m.group(0))
        for i in range(0, len(sides) - 2, 2):
            lhs, op, rhs = sides[i], sides[i + 1], sides[i + 2]
            if not re.search(r"\d\s*[×x*÷/+−-]\s*[€$£¥]?\d", lhs):
                continue  # `2025 = 100` is an index base and `€250k ≈ 2.2 %` a label, not a sum
            verdicts = []
            for scale in (True, False):
                got, want = evaluate(lhs, scale), evaluate(rhs, scale)
                if got is not None and want is not None:
                    tol = 0.01 if op == "=" else 0.03
                    verdicts.append(abs(got - want) <= tol * max(abs(want), 1e-9))
            if verdicts and not any(verdicts):
                out.append(f"arithmetic: `{lhs} {op} {rhs}` does not hold")
    return out


def line_errors(line: str, today: datetime.date) -> list[str]:
    errs = [f"process note: `{m.group(0)}` — write \"could not be read for verification on <date>"
            f" — check it directly\" or drop it" for m in PROCESS.finditer(line)]
    for m in DATA_YEAR.finditer(line):
        if int(m[1]) <= today.year - 2 and STALE_OK not in line[m.start():]:
            errs.append(f"stale data: `{m.group(0)}` needs \"— rates/figures may have changed since\"")
    return errs + arithmetic_errors(line)


def restamp_errors(text: str) -> list[str]:
    status = text[text.find("\n## Status"):] if "\n## Status" in text else ""
    stamp, table = STAMP.search(status), TABLE_HEAD.search(text)
    if not (stamp and table):
        return []
    rows = {}
    for row in text[table.end():].splitlines()[1:]:
        if not row.strip():
            if rows:
                break
            continue
        if not row.lstrip().startswith("|"):
            break
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        if len(cells) >= 2 and re.fullmatch(r"\d{4}-\d{2}-\d{2}", cells[1]):
            rows[cells[0].lower()] = cells[1]
    errs = []
    for head in SECTION_HEAD.findall(text[:text.find("\n## Status")]):
        key = next((k for k in FAST if k in head.lower()), None)
        if not key:
            continue
        dated = [d for name, d in rows.items() if key in name]
        if not dated:
            errs.append(f"re-stamp {stamp[1]}: fast section `{head}` is missing from the Per-section table")
        elif min(dated) < stamp[1]:
            errs.append(f"re-stamp {stamp[1]}: `{head}` is dated {min(dated)} in the Per-section table")
    return errs


def added_lines(base: str, path: str) -> list[tuple[int, str]]:
    diff = subprocess.run(["git", "diff", "-U0", f"{base}...HEAD", "--", path], cwd=ROOT,
                          capture_output=True, text=True).stdout
    out, n = [], 0
    for l in diff.splitlines():
        h = re.match(r"@@ -\S+ \+(\d+)", l)
        if h:
            n = int(h[1])
        elif l.startswith("+") and not l.startswith("+++"):
            out.append((n, l[1:]))
            n += 1
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--base", default="origin/main")
    ap.add_argument("--all", action="store_true", help="every playbook, every line (report only)")
    a = ap.parse_args()
    today = datetime.date.today()
    if a.all:
        files = sorted(str(p.relative_to(ROOT)) for p in ROOT.glob(PLAYBOOKS))
    else:
        files = subprocess.run(["git", "diff", "--name-only", "--diff-filter=ACMR", f"{a.base}...HEAD",
                                "--", PLAYBOOKS], cwd=ROOT, capture_output=True, text=True).stdout.split()
    fails = []
    for f in files:
        text = (ROOT / f).read_text(encoding="utf-8")
        lines = list(enumerate(text.splitlines(), 1)) if a.all else added_lines(a.base, f)
        fails += [f"{f}:{n}: {e}" for n, l in lines for e in line_errors(l, today)]
        fails += [f"{f}: {e}" for e in restamp_errors(text)]
    for e in fails:
        print(e)
    print(f"{'✘' if fails else '✔'} {len(fails)} playbook check failure(s) in {len(files)} file(s)")
    return 1 if fails and not a.all else 0


if __name__ == "__main__":
    sys.exit(main())
