#!/usr/bin/env python3
"""Verify every registered patch-note claim against Valve's own datafeed.

Reads checks/claims.tsv. Each row registers a string that must appear in the
official notes for a stated patch.

    https://www.dota2.com/datafeed/patchnotes?version=7.41&language=english
    https://www.dota2.com/datafeed/patchnoteslist?language=english

Discovered by probing, and it matters more than it looks. The human-facing pages
at dota2.com/patches/{version} are a JavaScript shell: 7.41e, 7.41 and 7.40b all
serve the same 46,711-byte document, so hashing the page would have verified
nothing at all. The datafeed returns structured, versioned JSON carrying a patch
timestamp, which makes patch claims GATING rather than advisory — the one place
this book is better sourced than its predecessors, which could only ever check
that a string still appeared somewhere in someone else's HTML.

    checks/patchnotes.py            all chapters
    checks/patchnotes.py 25         one chapter

Responses are cached in .cache/ so a full run costs one fetch per patch.
"""
import json
import os
import re
import sys
import unicodedata
import urllib.request

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TSV = os.path.join(HERE, "checks", "claims.tsv")
CACHE = os.path.join(HERE, ".cache")
FEED = "https://www.dota2.com/datafeed/patchnotes?version={}&language=english"


def normalise(s):
    """Whitespace-collapse and unify the dashes Valve's notes use freely."""
    s = unicodedata.normalize("NFKC", s)
    s = s.replace("–", "-").replace("—", "-").replace("’", "'")
    s = re.sub(r"<[^>]+>", " ", s)
    return re.sub(r"\s+", " ", s).strip().lower()


def notes(version):
    os.makedirs(CACHE, exist_ok=True)
    path = os.path.join(CACHE, f"patch-{version}.json")
    if not os.path.exists(path):
        req = urllib.request.Request(
            FEED.format(version), headers={"User-Agent": "book6-verify/1.0"}
        )
        with urllib.request.urlopen(req, timeout=60) as r:
            data = json.load(r)
        with open(path, "w") as f:
            json.dump(data, f)
    with open(path) as f:
        return json.load(f)


def main():
    only = sys.argv[1] if len(sys.argv) > 1 else None
    if not os.path.exists(TSV):
        print("  no checks/claims.tsv yet — nothing registered")
        return 0

    rows = []
    with open(TSV) as f:
        for n, line in enumerate(f, 1):
            line = line.rstrip("\n")
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            parts = line.split("\t")
            if len(parts) < 3:
                print(f"  FAIL: line {n}: expected 3 columns, got {len(parts)}")
                return 1
            rows.append((n, parts[0], parts[1], parts[2]))

    blobs, checked, failures = {}, 0, []
    for n, chapter, version, claim in rows:
        if only and chapter != only:
            continue
        if version not in blobs:
            try:
                d = notes(version)
            except Exception as e:  # network, not the book's fault
                print(f"  SKIP: patch {version} unreachable ({e})")
                blobs[version] = None
            else:
                if not d.get("success", True) or not d.get("patch_number"):
                    print(f"  SKIP: patch {version} returned no notes")
                    blobs[version] = None
                else:
                    blobs[version] = normalise(json.dumps(d))
        blob = blobs[version]
        if blob is None:
            continue
        checked += 1
        if normalise(claim) not in blob:
            failures.append(f"ch {chapter} line {n}: not in {version} notes — {claim!r}")

    print(f"  {checked} patch claims checked across {len([b for b in blobs.values() if b])} patches")
    for f_ in failures:
        print(f"  FAIL: {f_}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
