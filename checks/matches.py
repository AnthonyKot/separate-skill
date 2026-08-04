#!/usr/bin/env python3
"""Verify every registered match claim against the committed snapshot.

Reads checks/matches.tsv. This check is GATING: the snapshots live in this
repository, so a failure here is always actionable and never someone else's
server moving. Contrast checks/claims.py, which reads documents on dota2.com.

    checks/matches.py            all chapters
    checks/matches.py 21         one chapter

Claim types, one per row:

    duration        -                       seconds
    winner          -                       radiant | dire
    gold_adv_at     <minute>                radiant gold advantage at that minute
    xp_adv_at       <minute>                radiant xp advantage at that minute
    objective_time  <type>:<key>            seconds into the game
    purchase_time   <player>:<item>         seconds into the game
    buyback_time    <player>                seconds into the game
    count           <buybacks|teamfights|objectives|picks_bans>

A tolerance may be given in the optional sixth column, as an integer. It is
meant for the per-minute series, where the API's own resolution is a minute;
event timestamps are exact and must be registered exactly.
"""
import glob
import json
import os
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TSV = os.path.join(HERE, "checks", "matches.tsv")
SNAP = os.path.join(HERE, "data", "matches")


def load(match_id):
    path = os.path.join(SNAP, f"m{match_id}.json")
    if not os.path.exists(path):
        return None
    with open(path) as f:
        return json.load(f)


def player(d, name):
    for p in d["players"]:
        if (p.get("name") or p.get("personaname") or "") == name:
            return p
    return None


def resolve(d, check, arg):
    """Return the value the match record actually holds, or raise LookupError."""
    if check == "duration":
        return d["duration"]

    if check == "winner":
        return "radiant" if d["radiant_win"] else "dire"

    if check in ("gold_adv_at", "xp_adv_at"):
        key = "radiant_gold_adv" if check.startswith("gold") else "radiant_xp_adv"
        series = d.get(key) or []
        minute = int(arg)
        if minute >= len(series):
            raise LookupError(f"match is {len(series) - 1} minutes long, no minute {minute}")
        return series[minute]

    if check == "objective_time":
        kind, _, key = arg.partition(":")
        for o in d.get("objectives") or []:
            if o.get("type") == kind and (not key or o.get("key") == key):
                return o.get("time")
        raise LookupError(f"no objective {arg!r} in this match")

    if check == "purchase_time":
        name, _, item = arg.partition(":")
        p = player(d, name)
        if p is None:
            raise LookupError(f"no player named {name!r}")
        for buy in p.get("purchase_log") or []:
            if buy["key"] == item:
                return buy["time"]
        raise LookupError(f"{name} never bought {item!r}")

    if check == "buyback_time":
        p = player(d, arg)
        if p is None:
            raise LookupError(f"no player named {arg!r}")
        log = p.get("buyback_log") or []
        if not log:
            raise LookupError(f"{arg} never bought back")
        return log[0]["time"]

    if check == "count":
        field = {
            "buybacks": lambda: sum(len(p.get("buyback_log") or []) for p in d["players"]),
            "teamfights": lambda: len(d.get("teamfights") or []),
            "objectives": lambda: len(d.get("objectives") or []),
            "picks_bans": lambda: len(d.get("picks_bans") or []),
        }.get(arg)
        if field is None:
            raise LookupError(f"unknown count {arg!r}")
        return field()

    raise LookupError(f"unknown check type {check!r}")


def main():
    only = sys.argv[1] if len(sys.argv) > 1 else None
    if not os.path.exists(TSV):
        print("  no checks/matches.tsv yet — nothing registered")
        return 0

    rows, failures, checked = [], [], 0
    with open(TSV) as f:
        for n, line in enumerate(f, 1):
            line = line.rstrip("\n")
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            parts = line.split("\t")
            if len(parts) < 5:
                failures.append(f"line {n}: expected 5 or 6 columns, got {len(parts)}")
                continue
            rows.append((n, parts))

    cache = {}
    for n, parts in rows:
        chapter, match_id, check, arg, expected = parts[:5]
        tol = int(parts[5]) if len(parts) > 5 and parts[5].strip() else 0
        if only and chapter != only:
            continue

        if match_id not in cache:
            cache[match_id] = load(match_id)
        d = cache[match_id]
        if d is None:
            failures.append(
                f"ch {chapter} line {n}: no snapshot for match {match_id} — "
                f"run tools/fetch-match.py {match_id}"
            )
            continue

        try:
            actual = resolve(d, check, arg)
        except LookupError as e:
            failures.append(f"ch {chapter} line {n}: {check} {arg} — {e}")
            continue

        checked += 1
        try:
            ok = abs(int(actual) - int(expected)) <= tol
        except (TypeError, ValueError):
            ok = str(actual).strip().lower() == expected.strip().lower()

        if not ok:
            failures.append(
                f"ch {chapter} line {n}: {match_id} {check} {arg} — "
                f"registered {expected}, record says {actual}"
            )

    snapshots = len(glob.glob(os.path.join(SNAP, "m*.json")))
    print(f"  {checked} match claims checked against {snapshots} snapshots")
    for f_ in failures:
        print(f"  FAIL: {f_}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
