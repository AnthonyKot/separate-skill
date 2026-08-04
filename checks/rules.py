#!/usr/bin/env python3
"""Fail when a chapter has not been migrated to the current version of a rule.

GATING, and the third checker in this repository aimed at the same failure: a
decision changes, and the places that already implement it are never revisited.
checks/retired.py freezes vocabulary. checks/status.py freezes counts. Neither can
see a chapter that still implements the OLD VERSION OF A RULE in perfectly current
words, which is what happened to the pass mark — CONTEXT.md 3 was rewritten and
four published chapters went on teaching a review loop that validates any plan the
reader was willing to write down.

HOW IT WORKS. checks/rules.tsv lists rules that have changed, each with a current
version. Every chapter declares what it was migrated to, near the top:

    <!-- rules: CALIBRATION_MARK=2 HOLD_PASSABLE=2 NEXT_GAME_LIVE=1 -->

A missing rule, or a version behind the current one, fails the build. Bumping a
rule in rules.tsv therefore turns every chapter red at once, and the only way back
to green is to open each one.

WHAT IT DOES NOT DO, stated here because a checker oversold is worse than no
checker — that lesson cost this repository a fail-open patch check. **It cannot
tell whether the prose actually obeys the rule.** No checker can; the rules are
semantic. What it enforces is that migration is DELIBERATE rather than
remembered. A declaration bumped without reading the chapter is a false claim, but
it is a false claim in a diff, attributable, and reviewable — which is the whole of
the improvement being claimed, and it is not nothing, because every instance of
this failure so far has been an omission rather than a lie.

A version AHEAD of rules.tsv also fails: it means a chapter was migrated to a rule
the foundations do not carry, which is the same drift pointing the other way.
"""
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHAPTERS = os.path.join(HERE, "docs", "chapters")
TSV = os.path.join(HERE, "checks", "rules.tsv")

DECL = re.compile(r"<!--\s*rules:\s*([^>]*?)\s*-->")


def current():
    rules = {}
    with open(TSV, encoding="utf-8") as f:
        for line in f:
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) >= 2:
                rules[parts[0].strip()] = int(parts[1])
    return rules


def main():
    if not os.path.exists(TSV):
        print("  no checks/rules.tsv — nothing versioned")
        return 0

    rules = current()
    if not rules:
        print("  no versioned rules declared")
        return 0

    failures = []
    chapters = sorted(glob.glob(os.path.join(CHAPTERS, "*.html")))

    for path in chapters:
        ch = os.path.basename(path)[:2]
        with open(path, encoding="utf-8") as f:
            head = f.read(4000)

        m = DECL.search(head)
        if not m:
            failures.append(
                f"ch {ch}: no rules declaration. Add "
                f"<!-- rules: {' '.join(f'{k}={v}' for k, v in sorted(rules.items()))} --> "
                f"after reading the chapter against each rule"
            )
            continue

        declared = {}
        for token in m.group(1).split():
            if "=" not in token:
                failures.append(f"ch {ch}: malformed rule token {token!r}")
                continue
            k, _, v = token.partition("=")
            try:
                declared[k] = int(v)
            except ValueError:
                failures.append(f"ch {ch}: non-numeric version in {token!r}")

        for rule, version in sorted(rules.items()):
            if rule not in declared:
                failures.append(f"ch {ch}: does not declare {rule} (current v{version})")
            elif declared[rule] < version:
                failures.append(
                    f"ch {ch}: {rule}=v{declared[rule]}, current is v{version} — migrate it"
                )
            elif declared[rule] > version:
                failures.append(
                    f"ch {ch}: {rule}=v{declared[rule]} is ahead of rules.tsv (v{version})"
                )

        for rule in declared:
            if rule not in rules:
                failures.append(f"ch {ch}: declares unknown rule {rule!r}")

    print(
        f"  {len(chapters)} chapters checked against {len(rules)} versioned rules "
        f"({', '.join(f'{k} v{v}' for k, v in sorted(rules.items()))})"
    )
    print("  note: this proves migration was deliberate, never that the prose complies")
    for f_ in failures:
        print(f"  FAIL: {f_}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
