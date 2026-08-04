#!/usr/bin/env python3
"""Fetch a parsed match from the OpenDota API into data/matches/.

    tools/fetch-match.py 8929124210

Refuses to overwrite an existing snapshot unless --force is given: the snapshot is
the record as it stood when a chapter was written, and silently replacing it would
destroy the only thing that makes drift detectable.
"""
import json
import os
import sys
import urllib.request

API = "https://api.opendota.com/api/matches/{}"
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEST = os.path.join(HERE, "data", "matches")


def fetch(match_id):
    req = urllib.request.Request(
        API.format(match_id), headers={"User-Agent": "book6-verify/1.0"}
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    force = "--force" in sys.argv
    if not args:
        sys.exit(__doc__)

    for match_id in args:
        path = os.path.join(DEST, f"m{match_id}.json")
        if os.path.exists(path) and not force:
            print(f"  {match_id}: snapshot exists, not overwriting (--force to replace)")
            continue
        d = fetch(match_id)
        if d.get("version") is None:
            print(f"  {match_id}: NOT PARSED — no teamfights, logs or per-minute series.")
            print("    Request a parse at opendota.com and try again later.")
            continue
        with open(path, "w") as f:
            json.dump(d, f, separators=(",", ":"))
        print(
            f"  {match_id}: parsed v{d['version']}, {d['duration']}s, "
            f"{len(d.get('teamfights') or [])} teamfights, "
            f"{len(d.get('objectives') or [])} objectives -> {os.path.relpath(path, HERE)}"
        )


if __name__ == "__main__":
    main()
