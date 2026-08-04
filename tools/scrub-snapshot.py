#!/usr/bin/env python3
"""Strip player identifiers from a public match snapshot, in place.

    tools/scrub-snapshot.py data/matches/m1234567890.json

Removes account_id, persona names and profile blocks from every player, leaving
everything the book actually argues from: hero, slot, timings, purchases,
buybacks, wards, per-minute series, and the match id itself.

Refuses to touch professional matches. Those players are named on a broadcast and
their identity is part of the public record; scrubbing them would make the case
uncheckable for no gain. See checks/privacy.py for the full reasoning.

Note what this does and does not achieve. It keeps identifiers out of THIS
repository. It does not anonymise the match — the id is still published, and
anyone can reopen the record upstream. That is why a public match may only be
used as an identified case with the player's consent; scrubbing is hygiene, not
a substitute for asking.
"""
import json
import os
import sys

IDENTIFYING = ("account_id", "personaname", "name", "steamid", "profile")


def main():
    paths = [a for a in sys.argv[1:] if not a.startswith("-")]
    if not paths:
        sys.exit(__doc__)

    for path in paths:
        if not os.path.exists(path):
            print(f"  {path}: no such file")
            continue
        with open(path) as f:
            d = json.load(f)

        if d.get("leagueid"):
            print(
                f"  {path}: professional match (league {d['leagueid']}) — "
                f"not scrubbed, by design"
            )
            continue

        removed = 0
        for p in d.get("players") or []:
            for k in IDENTIFYING:
                if k in p:
                    del p[k]
                    removed += 1

        with open(path, "w") as f:
            json.dump(d, f, separators=(",", ":"))
        print(f"  {path}: removed {removed} identifying field(s) from {len(d.get('players') or [])} players")


if __name__ == "__main__":
    main()
