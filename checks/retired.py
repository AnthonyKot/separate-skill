#!/usr/bin/env python3
"""Fail when retired terminology reappears outside its declared historical uses.

GATING. This check exists because the same failure happened twice in one day: a
structural decision was changed in three places and survived in a fourth, both
times in a *summary* — the spine arrow still said "invert by seat" after Part VII's
premise was replaced, and the claim-class table still said "advisory" after the
bracket checker became gating.

The pattern is worth stating, because it is not forgetfulness. **When a decision
changes, the places that repeat it are exactly the places nobody re-reads, because
they are summaries.** A manual re-read will not catch it reliably; a search will.

    checks/retired.tsv        term / replaced by / date / why
    checks/retired-allow.tsv  term / file / count / why this file may say it

Historical mentions are legitimate and expected: CONTEXT.md 8 records what got
caught, and a decision record that cannot state what it replaced is a worse
document. So this check does not ban the term — it **freezes the count** per file.
A new occurrence anywhere fails the build, including one more in a file that
already has declared mentions. That is the case worth catching: the old idea
creeping back into a summary that used to merely reminisce about it.

Excludes .git, data/ and the two tsv files themselves.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TERMS = os.path.join(HERE, "checks", "retired.tsv")
ALLOW = os.path.join(HERE, "checks", "retired-allow.tsv")
SKIP_DIRS = {".git", "data", ".cache", "__pycache__"}
SKIP_FILES = {"retired.tsv", "retired-allow.tsv", "retired.py"}


def rows(path):
    if not os.path.exists(path):
        return []
    out = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            out.append(line.rstrip("\n").split("\t"))
    return out


def main():
    terms = [r[0] for r in rows(TERMS)]
    if not terms:
        print("  no retired terminology registered")
        return 0

    allowed = {}
    for r in rows(ALLOW):
        if len(r) >= 3:
            allowed[(r[0].lower(), r[1])] = int(r[2])

    found = {}
    for root, dirs, files in os.walk(HERE):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for name in files:
            if name in SKIP_FILES or not name.endswith((".md", ".html", ".py", ".sh", ".tsv", ".yml")):
                continue
            path = os.path.join(root, name)
            rel = os.path.relpath(path, HERE)
            try:
                with open(path, encoding="utf-8") as f:
                    text = f.read()
            except (UnicodeDecodeError, OSError):
                continue
            for term in terms:
                n = len(re.findall(re.escape(term), text, re.I))
                if n:
                    found[(term.lower(), rel)] = n

    failures = []
    for (term, rel), n in sorted(found.items()):
        limit = allowed.get((term, rel), 0)
        if n > limit:
            failures.append(
                f"{rel}: {n} occurrence(s) of retired {term!r}, {limit} declared"
                + ("" if limit else " — declare it in checks/retired-allow.tsv with a reason, or remove it")
            )

    print(f"  {len(terms)} retired term(s) checked across the repository")
    for f_ in failures:
        print(f"  FAIL: {f_}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
