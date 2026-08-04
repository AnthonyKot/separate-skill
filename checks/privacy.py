#!/usr/bin/env python3
"""Fail if a non-professional match snapshot carries player identifiers.

GATING. The rule it enforces used to exist only as a sentence in CONTEXT.md 5,
and a rule that is only prose is a rule that gets forgotten by whoever is in a
hurry — which, for this one, means publishing an ordinary person's account id in
a book that calls their game a cautionary tale.

The tension is real and worth stating rather than resolving by hand-waving. The
chapter template requires a match id so the reader can open the replay and check
the argument. The sourcing standard requires ordinary ranked players to be
anonymous. Publishing the id largely defeats prose-level anonymity: anyone can
reopen the record. So the two rules cannot both be honoured for an unconsented
public match, and the book resolves it by source:

  * PROFESSIONAL matches (leagueid set) are broadcast, the players are named on
    stream, and identity is part of the public record. Ids and names stay.
  * PUBLIC matches are scrubbed of account_id and persona names before being
    committed, and may only be identified in prose at all with the player's
    consent. Aggregate bracket data — the usual reason to touch public matches —
    needs no identity whatsoever, and lives in data/brackets/ instead.

Run tools/scrub-snapshot.py to strip a public snapshot before committing it.
"""
import glob
import json
import os
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MATCHES = os.path.join(HERE, "data", "matches")
BRACKETS = os.path.join(HERE, "data", "brackets")

IDENTIFYING = ("account_id", "personaname", "name", "steamid", "profile")


def main():
    failures, checked, pro = [], 0, 0

    for path in sorted(glob.glob(os.path.join(MATCHES, "m*.json"))):
        with open(path) as f:
            d = json.load(f)
        rel = os.path.relpath(path, HERE)
        checked += 1

        if d.get("leagueid"):
            pro += 1
            continue

        for p in d.get("players") or []:
            present = [k for k in IDENTIFYING if p.get(k) not in (None, "", 0)]
            if present:
                failures.append(
                    f"{rel}: public match carries {', '.join(present)} — "
                    f"run tools/scrub-snapshot.py {rel}"
                )
                break

    # Bracket samples must never carry identity at all: they exist to support
    # claims about a population, and a population does not need names.
    for path in sorted(glob.glob(os.path.join(BRACKETS, "*.json"))):
        with open(path) as f:
            d = json.load(f)
        rel = os.path.relpath(path, HERE)
        checked += 1
        for row in d.get("matches") or []:
            present = [k for k in IDENTIFYING if k in row]
            if present:
                failures.append(f"{rel}: bracket sample carries {', '.join(present)}")
                break

    print(f"  {checked} snapshots checked ({pro} professional, identities permitted)")
    for f_ in failures:
        print(f"  FAIL: {f_}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
