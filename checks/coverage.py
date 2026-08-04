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
