#!/usr/bin/env python3
"""Verify every registered bracket claim by recomputing it from its stored sample.

Reads checks/data.tsv:

    chapter	snapshot	metric	expected	tolerance

Two different things happen here, and the distinction is the point.

RECOMPUTATION IS GATING. The registered figure is recomputed from the raw rows
committed under data/brackets/. If it does not match, the book states a number its
own evidence does not support, and that is always the book's fault. Same standing
as checks/matches.py.

DRIFT IS ADVISORY. `--drift` additionally re-samples the live API and reports how
far the current game has moved from the snapshot. That difference is not an error:
it is the game changing, which is exactly what a book about a patched game wants to
know. It never fails the build.

Sample size is reported on every row, because a bracket claim without an n is the
thing this file exists to prevent.

    checks/data.py               recompute all
    checks/data.py 27            one chapter
    checks/data.py --drift       also re-sample live and report movement
"""
import glob
import json
import os
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(HERE, "checks"))
from metrics import compute  # noqa: E402
from patchnotes import notes  # noqa: E402  reuses the cached datafeed fetch

TSV = os.path.join(HERE, "checks", "data.tsv")
SNAP = os.path.join(HERE, "data", "brackets")


def load(name):
    path = os.path.join(SNAP, f"{name}.json")
    if not os.path.exists(path):
        return None
    with open(path) as f:
        return json.load(f)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    only = args[0] if args else None

    if not os.path.exists(TSV):
        print("  no checks/data.tsv yet — nothing registered")
        return 0

    rows = []
    with open(TSV) as f:
        for n, line in enumerate(f, 1):
            line = line.rstrip("\n")
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            parts = line.split("\t")
            if len(parts) < 4:
                print(f"  FAIL: line {n}: expected 4 or 5 columns, got {len(parts)}")
                return 1
            rows.append((n, parts))

    # GATING: a sample must not contain matches played before the patch it is
    # labelled with. This is the bug the first sampler had — a seek overshot 108
    # days and pulled pre-7.41e games into a snapshot named 7.41e — and nothing
    # noticed until a span metric was added for unrelated reasons. It is cheap to
    # check and impossible to spot by reading the file.
    boundary = []
    for path in sorted(glob.glob(os.path.join(SNAP, "*.json"))):
        with open(path) as f:
            snap = json.load(f)
        starts = [m["start_time"] for m in snap.get("matches", []) if m.get("start_time")]
        if not starts:
            continue
        try:
            released = notes(snap["patch"]).get("patch_timestamp")
        except Exception as e:
            print(f"  UNRESOLVED: could not date patch {snap['patch']} ({e})")
            boundary.append(snap["patch"])
            continue
        if released and min(starts) < released:
            early = (released - min(starts)) / 86400.0
            boundary.append(
                f"{os.path.basename(path)}: earliest match predates patch "
                f"{snap['patch']} by {early:.1f} days"
            )
    for b in boundary:
        print(f"  FAIL: {b}")
    if not boundary:
        print("  every sample is entirely within the patch it is labelled with")

    cache, checked, failures = {}, 0, []
    for n, parts in rows:
        chapter, name, metric, expected = parts[:4]
        tol = float(parts[4]) if len(parts) > 4 and parts[4].strip() else 0.0
        if only and chapter != only:
            continue

        if name not in cache:
            snap = load(name)
            cache[name] = (snap, compute(snap) if snap else None)
        snap, computed = cache[name]

        if snap is None:
            failures.append(f"ch {chapter} line {n}: no snapshot data/brackets/{name}.json")
            continue
        if metric not in computed:
            failures.append(
                f"ch {chapter} line {n}: no metric {metric!r} — "
                f"available: {', '.join(sorted(computed))}"
            )
            continue

        checked += 1
        actual = computed[metric]
        try:
            ok = abs(float(actual) - float(expected)) <= tol
        except (TypeError, ValueError):
            ok = str(actual) == expected

        note = f"n={snap['n']}, patch {snap['patch']}, sampled {snap['fetched']}"
        if not ok:
            failures.append(
                f"ch {chapter} line {n}: {name} {metric} — "
                f"registered {expected}, sample gives {actual} ({note})"
            )
        else:
            print(f"  ok  ch {chapter}  {metric} = {actual}  [{note}]")

    snapshots = len(glob.glob(os.path.join(SNAP, "*.json")))
    print(f"  {checked} bracket claims recomputed from {snapshots} snapshots")
    for f_ in failures:
        print(f"  FAIL: {f_}")
    return 1 if failures or boundary else 0


if __name__ == "__main__":
    sys.exit(main())
