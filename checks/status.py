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

    # Chapters tagged as pilots on the contents page. Added when ch. 02 — the
    # first chapter that is NOT a pilot — made "all five are pilots" false in two
    # files, and nothing noticed. Every count that describes the state of the work
    # gets computed; that is the rule this file exists to apply, and it had been
    # applied to three numbers.
    pilots = 0
    idx = os.path.join(HERE, "docs", "index.html")
    if os.path.exists(idx):
        with open(idx, encoding="utf-8") as f:
            pilots = len(re.findall(r'<span class="tag">pilot</span>', f.read()))

    print(
        f"  computed: {chapters} chapters, {checkers} checkers, "
        f"{bracket_claims} bracket claims, {pilots} pilots"
    )

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

        # "all <n> are pilots" / "<n> are pilots" / "all four are pilots"
        for m in re.finditer(r"\b(?:all\s+)?([A-Za-z]+|\d+)\s+(?:of them\s+)?are pilots\b", text, re.I):
            claimed = number(m.group(1))
            if claimed is not None and claimed != pilots:
                failures.append(
                    f"{rel}: says {m.group(1)!r} are pilots, {pilots} tagged on the contents page"
                )

        # "no bracket claim is registered"
        if re.search(r"no bracket claim is registered", text, re.I) and bracket_claims:
            failures.append(f"{rel}: says no bracket claim is registered, {bracket_claims} are")

        # "<n> bracket claims are registered". Added when the count went from six
        # to ten and README.md still said six — the same drift this file was
        # written for, in the one number it already computed and did not compare.
        for m in re.finditer(r"\b([A-Za-z]+|\d+)\s+bracket claims?\s+(?:are|is)\s+registered", text, re.I):
            claimed = number(m.group(1))
            if claimed is not None and claimed != bracket_claims:
                failures.append(
                    f"{rel}: says {m.group(1)!r} bracket claims registered, {bracket_claims} in data.tsv"
                )

    # Per-chapter claim counts in CONTEXT.md 6's register.
    #
    # Added after three of five had drifted unnoticed: ch. 12 said 18 against 17,
    # ch. 21 said 38 against 41, ch. 32 said 15 against 17. Every one of them was
    # correct when it was typed. This is the same failure the audit rule in
    # CONTEXT.md 4 describes — a summary restates a fact, the fact moves, and the
    # summary is the last place anyone re-reads — and it survived a checker
    # written specifically to catch it, because that checker only knew about
    # three numbers. Anything asserted must be computed.
    per_chapter = {}
    tsv_m = os.path.join(HERE, "checks", "matches.tsv")
    if os.path.exists(tsv_m):
        with open(tsv_m) as f:
            for line in f:
                if line.lstrip().startswith("#"):
                    continue
                parts = line.rstrip("\n").split("\t")
                if len(parts) >= 5 and parts[0].strip():
                    per_chapter[parts[0].strip()] = per_chapter.get(parts[0].strip(), 0) + 1

    ctx = os.path.join(HERE, "CONTEXT.md")
    if os.path.exists(ctx) and per_chapter:
        with open(ctx, encoding="utf-8") as f:
            for m in re.finditer(
                r"^\|\s*(\d+)\s*\|[^|]*\|\s*☑\s*(\d+)\s+claims", f.read(), re.M
            ):
                ch, claimed = m.group(1).lstrip("0") or "0", int(m.group(2))
                actual = per_chapter.get(ch)
                if actual is None:
                    failures.append(f"CONTEXT.md: ch {ch} says {claimed} claims, none registered")
                elif actual != claimed:
                    failures.append(
                        f"CONTEXT.md: ch {ch} says {claimed} claims, {actual} in matches.tsv"
                    )
        print(f"  computed: claim counts for {len(per_chapter)} chapters checked against CONTEXT.md")

    for f_ in failures:
        print(f"  FAIL: {f_}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
