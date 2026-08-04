#!/usr/bin/env python3
"""Report numbers that appear in a chapter's prose but in no registered claim.

ADVISORY, and the only advisory check in this repository. It cannot be gating
because prose legitimately contains numbers that are not claims — years, chapter
cross-references, figures derived by arithmetic from two registered values — and a
gating version would be silenced by exceptions until it meant nothing.

WHY IT EXISTS. Every other check here verifies the registry against the record.
None verified the PROSE against the registry, and CONTEXT.md 5 admits as much:
coverage is editorial discipline, not a property of the script. That gap had a
cost within one chapter of being written. Ch. 21 stated that a team lost three
heroes in a fight while its own registered claim for that fight said four — a
player had died twice, and the extraction behind the sentence counted players
rather than deaths. Every check passed. This one would have fired.

Declared exceptions live in checks/coverage-allow.tsv, one per line, each with a
reason. The reason is the point: an exception nobody had to justify is how a check
stops working.

    checks/coverage.py            all chapters
    checks/coverage.py 21         one chapter
"""
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHAPTERS = os.path.join(HERE, "docs", "chapters")
ALLOW = os.path.join(HERE, "checks", "coverage-allow.tsv")


def registered():
    """Every value appearing in the last column of any claim file."""
    values = set()
    for name in ("matches.tsv", "data.tsv", "claims.tsv"):
        path = os.path.join(HERE, "checks", name)
        if not os.path.exists(path):
            continue
        with open(path) as f:
            for line in f:
                if line.lstrip().startswith("#"):
                    continue
                for cell in line.rstrip("\n").split("\t"):
                    cell = cell.strip()
                    if re.fullmatch(r"-?\d+", cell):
                        values.add(cell.lstrip("+-"))
                    # A compound value registers each of its parts. Coordinates are
                    # stored as "118,122" by teamfight_death_pos, and ch. 03 quotes
                    # the two numbers separately — which the scan above could not
                    # see, so every coordinate in that chapter looked unregistered
                    # while being registered exactly.
                    if re.fullmatch(r"-?\d+(,-?\d+)+", cell):
                        for part in cell.split(","):
                            values.add(part.strip().lstrip("+-"))
                    # a match id is registered by being the row's subject
                    if re.fullmatch(r"\d{8,}", cell):
                        values.add(cell)
    return values


def allowed():
    out = {}
    if not os.path.exists(ALLOW):
        return out
    with open(ALLOW) as f:
        for line in f:
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) >= 2:
                out.setdefault(parts[0], set()).add(parts[1].replace(",", ""))
    return out


_UNITS = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
    "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12,
    "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
    "seventeen": 17, "eighteen": 18, "nineteen": 19,
}
_TENS = {
    "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60,
    "seventy": 70, "eighty": 80, "ninety": 90,
}
_SMALL = "|".join(k for k, v in _UNITS.items() if v < 10)
_WORD_NUM = re.compile(
    r"\b(?:(%s)[- ](%s)|(%s)|(%s))\b"
    % ("|".join(_TENS), _SMALL, "|".join(_TENS), "|".join(_UNITS)),
    re.I,
)
# A spelled-out number followed by a time unit is a duration restating a
# registered timestamp — "forty-nine minutes and thirty-three seconds" is the
# duration 2973 in words. Those are not the failure this pass is for.
_TIME_UNIT = re.compile(r"^[-\s]*(minute|minutes|second|seconds|hour|hours|per)\b", re.I)


def word_numbers(body):
    """Spelled-out COUNTS in prose, as integers. Durations are excluded."""
    out = set()
    for m in _WORD_NUM.finditer(body):
        tens, unit, tens_only, unit_only = m.groups()
        if tens:
            value = _TENS[tens.lower()] + _UNITS[unit.lower()]
        elif tens_only:
            value = _TENS[tens_only.lower()]
        else:
            value = _UNITS[unit_only.lower()]
        if value <= 3:
            continue
        if _TIME_UNIT.match(body[m.end():m.end() + 12]):
            continue
        if re.search(r"\bminute\s*$", body[:m.start()], re.I):
            continue
        out.add(value)
    return out


def main():
    only = sys.argv[1] if len(sys.argv) > 1 else None
    reg, allow = registered(), allowed()
    total = 0

    for path in sorted(glob.glob(os.path.join(CHAPTERS, "*.html"))):
        chapter = os.path.basename(path)[:2]
        if only and chapter != only:
            continue
        with open(path, encoding="utf-8") as f:
            html = f.read()
        body = re.sub(r"<script.*?</script>|<[^>]+>", " ", html, flags=re.S)

        # Three or more digits only. Two-digit numbers are overwhelmingly clock
        # times and counts already covered by other rows, and including them
        # produced more noise than signal.
        found = {n.replace(",", "") for n in re.findall(r"\b\d[\d,]{2,}\b", body)}

        # Counts written as WORDS. This exists because two of them shipped: ch. 32
        # said "eleven wards expired" when ten did, and ch. 04 said "nine uses"
        # when there were seven. Both passed every check in this repository,
        # because the digit pass above cannot see a word — and a count is exactly
        # the kind of figure a writer adds up by hand and gets wrong.
        #
        # LIMIT, stated because a checker oversold is worse than none: the
        # registry is a flat set of values, so a small count clears whenever that
        # number is registered anywhere for any reason. "nine" passes if any claim
        # in the book has the value 9. It catches the larger counts reliably and
        # the small ones only sometimes, and it is not a substitute for adding up
        # twice.
        found |= {str(v) for v in word_numbers(body)}

        ok = reg | allow.get(chapter, set()) | allow.get("*", set())
        unregistered = sorted(n for n in found if n not in ok)

        if unregistered:
            total += len(unregistered)
            print(f"  ch {chapter}: {len(unregistered)} unregistered — {', '.join(unregistered)}")
        else:
            print(f"  ch {chapter}: every figure traced to a registered claim")

    if total:
        print(f"  {total} number(s) in prose with no registered claim.")
        print("  Register them, or declare them with a reason in checks/coverage-allow.tsv.")
    return 0  # advisory, always


if __name__ == "__main__":
    sys.exit(main())
