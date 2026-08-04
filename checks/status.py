#!/usr/bin/env python3
"""Fail when a stated status contradicts the repository.

GATING. Book 5 carries a check like this because its status sentence went stale
twice while the book was being written. This one exists because the README said
"No chapters are written" while four were live on the published site, "Three
verifiers" while there were six, and "No bracket claim is registered yet" while six
were registered and passing.

That is the same failure as retired terminology, in a different costume: **a
summary restates a fact, the fact changes, and nobody re-reads the summary because
it is a summary.** checks/retired.py freezes vocabulary; this freezes counts.

Anything asserted here must be COMPUTED, never typed. The rule the series has
always applied to chapter counts is applied to every other number that describes
the state of the work.
"""
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

WORDS = {
    "no": 0, "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11,
    "twelve": 12,
}


def number(token):
    token = token.strip().lower()
    if token.isdigit():
        return int(token)
    return WORDS.get(token)


def main():
    chapters = len(glob.glob(os.path.join(HERE, "docs", "chapters", "*.html")))
    checkers = len(
        [
            p
            for p in glob.glob(os.path.join(HERE, "checks", "*.py"))
            if os.path.basename(p) not in ("metrics.py", "status.py")
        ]
    )
    bracket_claims = 0
    tsv = os.path.join(HERE, "checks", "data.tsv")
    if os.path.exists(tsv):
        with open(tsv) as f:
            bracket_claims = sum(
                1 for line in f if line.strip() and not line.lstrip().startswith("#")
            )

    print(f"  computed: {chapters} chapters, {checkers} checkers, {bracket_claims} bracket claims")

    failures = []
    for rel in ("README.md", "docs/index.html", "docs/about.html"):
        path = os.path.join(HERE, rel)
        if not os.path.exists(path):
            continue
        with open(path, encoding="utf-8") as f:
            text = re.sub(r"\s+", " ", f.read())

        # "<n> chapters of thirty-two are written" / "no chapters are written"
        for m in re.finditer(r"\b([A-Za-z]+|\d+)\s+chapters?\s+(?:of thirty-two\s+)?(?:are|is)\s+written", text, re.I):
            claimed = number(m.group(1))
            if claimed is not None and claimed != chapters:
                failures.append(f"{rel}: says {m.group(1)!r} chapters written, {chapters} on disk")

        # "<n> verifiers" / "<n> checkers"
        for m in re.finditer(r"\b([A-Za-z]+|\d+)\s+(?:verifiers|checkers)\b", text, re.I):
            claimed = number(m.group(1))
            if claimed is not None and claimed != checkers:
                failures.append(f"{rel}: says {m.group(1)!r} verifiers, {checkers} in checks/")

        # "no bracket claim is registered"
        if re.search(r"no bracket claim is registered", text, re.I) and bracket_claims:
            failures.append(f"{rel}: says no bracket claim is registered, {bracket_claims} are")

    for f_ in failures:
        print(f"  FAIL: {f_}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
