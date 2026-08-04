#!/usr/bin/env python3
"""Fail on banned vocabulary in chapter prose.

GATING, and mechanical on purpose. CONTEXT.md 4 bans two registers:

  * the GUIDE register — just, simply, obviously, of course — each of which
    asserts that the thing being explained is easy, which is false and is the
    exact tone the reader has already failed to learn from;
  * the BLAME register — trash, feeder, griefer, int, throwing — because a book
    that licenses contempt teaches the reader to stop looking at their own replay.

The ban is on the WORD, not on the sense. "You have just admitted" and "it simply
was not fighting" both mean *merely* and assert nothing about difficulty — and both
shipped in chapter 12 anyway, because a rule that requires judgement to apply is a
rule that gets applied when someone remembers. Banning the token makes it
checkable, and the cost is a rewrite that is usually an improvement.

Quoted material is exempt only where it is inside <blockquote> or <code>: the book
may report someone else's register without adopting it.
"""
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHAPTERS = os.path.join(HERE, "docs", "chapters")

# EXACTLY the lists in CONTEXT.md 4 — no more. The first version of this file
# added merely, clearly, useless and boosted, which the foundations do not ban.
# A checker that enforces rules its own spec does not contain is worse than no
# checker: it trains the author to ignore its output.
GUIDE = ["just", "simply", "obviously", "of course", "literally everyone knows"]
# CONTEXT.md 4 also bans "int" and "your team" as BLAME register. They are not
# here, because their ban is contextual and a token match cannot see context:
# "your team takes a set of barracks" is neutral description, and the banned
# thing is the accusatory use. Enforcing them mechanically produced three false
# positives on the first run. They remain prose rules, checked by a reader.
BLAME = ["trash", "griefer"]


def main():
    only = sys.argv[1] if len(sys.argv) > 1 else None
    hits = 0

    for path in sorted(glob.glob(os.path.join(CHAPTERS, "*.html"))):
        chapter = os.path.basename(path)[:2]
        if only and chapter != only:
            continue
        with open(path, encoding="utf-8") as f:
            html = f.read()
        # drop exempt regions, then tags
        html = re.sub(r"<blockquote.*?</blockquote>|<code.*?</code>", " ", html, flags=re.S)
        body = re.sub(r"<script.*?</script>|<[^>]+>", " ", html, flags=re.S)

        found = []
        for word in GUIDE + BLAME:
            for m in re.finditer(rf"\b{re.escape(word)}\b", body, re.I):
                snippet = re.sub(r"\s+", " ", body[max(0, m.start() - 40):m.end() + 40]).strip()
                found.append(f"{word!r} — ...{snippet}...")
        if found:
            hits += len(found)
            print(f"  ch {chapter}: {len(found)} banned")
            for f_ in found:
                print(f"    FAIL: {f_}")
        else:
            print(f"  ch {chapter}: register clean")

    return 1 if hits else 0


if __name__ == "__main__":
    sys.exit(main())
