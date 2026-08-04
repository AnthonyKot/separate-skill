#!/usr/bin/env python3
"""Verify every registered match claim against the committed snapshot.

Reads checks/matches.tsv. This check is GATING: the snapshots live in this
repository, so a failure here is always actionable and never someone else's
server moving. Contrast checks/claims.py, which reads documents on dota2.com.

    checks/matches.py            all chapters
    checks/matches.py 21         one chapter

Claim types, one per row:

    duration        -                        seconds
    winner          -                        radiant | dire
    gold_adv_at     <minute>                 radiant gold advantage at that minute
    xp_adv_at       <minute>                 radiant xp advantage at that minute
    series_max      <gold|xp>                the maximum of that series
    series_max_minute <gold|xp>              the minute the maximum occurs
    objective_time  <type>:<key>[#N]         seconds; #N selects the Nth occurrence
    purchase_time   <player>:<item>          seconds into the game
    buyback_time    <player>                 seconds into the game
    teamfight_start <index>                  seconds, 1-based
    teamfight_end   <index>                  seconds, 1-based
    hero_purchase_time <Hero Name>:<item>    seconds, first completion
    purchases_between <start>:<end>:<items>  completions of any listed item in a window
    hero_series_at  <Hero>:<gold|xp|lh>:<min>  that hero's per-minute series
    teamfight_deaths <index>:<radiant|dire>  hero deaths on that side in that fight
    hero_stat       <Hero Name>:<field>      any scoreboard field, addressed by hero
    kills_outside_teamfights <outside|total> hero deaths outside every fight window
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


def hero_names():
    """id -> localized name, from the committed map in data/heroes.json."""
    path = os.path.join(HERE, "data", "heroes.json")
    with open(path, encoding="utf-8") as f:
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
        # An optional #N selects the Nth occurrence, 1-based. Needed because a
        # match has two tier-4 towers and the chapter cites both; without this the
        # second one could not be registered, and an unregistered figure in the
        # prose is exactly what the coverage rule in CONTEXT.md 5 cannot catch.
        arg, _, nth = arg.partition("#")
        nth = int(nth) if nth else 1
        kind, _, key = arg.partition(":")
        seen = 0
        for o in d.get("objectives") or []:
            if o.get("type") == kind and (not key or o.get("key") == key):
                seen += 1
                if seen == nth:
                    return o.get("time")
        raise LookupError(f"no occurrence {nth} of objective {arg!r} (found {seen})")

    if check == "hero_stat":
        # "<Hero Name>:<field>" — e.g. "Bane:deaths". Heroes rather than players,
        # deliberately: ch. 01 needs a scoreboard line and must not name the human
        # attached to it. See the ledger for 8928953683 in CONTEXT.md 7.
        name, _, field = arg.partition(":")
        heroes = hero_names()
        for p in d["players"]:
            if heroes.get(str(p.get("hero_id"))) == name:
                if field not in p:
                    raise LookupError(f"{name} has no field {field!r}")
                return p[field]
        raise LookupError(f"no {name!r} in this match")

    if check == "kills_outside_teamfights":
        # How many hero deaths fall outside every window the parser calls a
        # teamfight. The windows are OPENDOTA'S JUDGEMENT, not the game's, so any
        # chapter citing this must say whose definition it is.
        fights = [(t["start"], t["end"]) for t in d.get("teamfights") or []]
        total = outside = 0
        for p in d["players"]:
            for k in p.get("kills_log") or []:
                if not k["key"].startswith("npc_dota_hero_"):
                    continue
                total += 1
                if not any(a <= k["time"] <= b for a, b in fights):
                    outside += 1
        return outside if arg == "outside" else total

    if check in ("series_max", "series_max_minute"):
        # Registering a value at a minute does not license the word "peak" — the
        # value could be matched or beaten elsewhere in the series. These two make
        # the maximum itself the claim. Added after review pointed out that ch. 21
        # asserted a peak while the registry only proved a reading.
        key = {"gold": "radiant_gold_adv", "xp": "radiant_xp_adv"}[arg]
        series = d.get(key) or []
        if not series:
            raise LookupError(f"no {key} series in this match")
        top = max(series)
        return top if check == "series_max" else series.index(top)

    if check == "purchases_between":
        # "<start_sec>:<end_sec>:<item,item,...>" — completions of any listed item
        # inside the window. The item list is part of the CLAIM rather than baked
        # into this file on purpose: "expensive" is an editorial judgement, and a
        # chapter that counts expensive items must show which ones it counted.
        start, end, items = arg.split(":", 2)
        wanted = {i.strip() for i in items.split(",")}
        start, end = int(start), int(end)
        return sum(
            1
            for p in d["players"]
            for b in (p.get("purchase_log") or [])
            if b["key"] in wanted and start <= b["time"] <= end
        )

    if check == "teamfight_end":
        fights = d.get("teamfights") or []
        i = int(arg)
        if not 1 <= i <= len(fights):
            raise LookupError(f"match has {len(fights)} teamfights, no #{i}")
        return fights[i - 1]["end"]

    if check == "hero_purchase_time":
        # "<Hero Name>:<item>" — first completion. Hero-addressed for the same
        # reason as hero_stat: ch. 12 argues about what an item was for, not about
        # who bought it.
        name, _, item = arg.partition(":")
        heroes = hero_names()
        for p in d["players"]:
            if heroes.get(str(p.get("hero_id"))) == name:
                for buy in p.get("purchase_log") or []:
                    if buy["key"] == item:
                        return buy["time"]
                raise LookupError(f"{name} never completed {item!r}")
        raise LookupError(f"no {name!r} in this match")

    if check == "hero_series_at":
        # "<Hero Name>:<gold|xp|lh>:<minute>" — that hero's per-minute series.
        name, _, rest = arg.partition(":")
        series_name, _, minute = rest.partition(":")
        key = {"gold": "gold_t", "xp": "xp_t", "lh": "lh_t"}[series_name]
        heroes = hero_names()
        for p in d["players"]:
            if heroes.get(str(p.get("hero_id"))) == name:
                series = p.get(key) or []
                m = int(minute)
                if m >= len(series):
                    raise LookupError(f"{name} has {len(series)} minutes, no {m}")
                return series[m]
        raise LookupError(f"no {name!r} in this match")

    if check == "teamfight_start":
        fights = d.get("teamfights") or []
        i = int(arg)
        if not 1 <= i <= len(fights):
            raise LookupError(f"match has {len(fights)} teamfights, no #{i}")
        return fights[i - 1]["start"]

    if check == "teamfight_deaths":
        # "<index>:<radiant|dire>" — how many heroes of that side died in the fight.
        # The teamfights array lists players in player_slot order, so the first five
        # entries are Radiant. This carries chapter 21's load-bearing claim that a
        # fight went three-for-none, which no other registered figure would catch.
        idx, _, side = arg.partition(":")
        fights = d.get("teamfights") or []
        i = int(idx)
        if not 1 <= i <= len(fights):
            raise LookupError(f"match has {len(fights)} teamfights, no #{i}")
        slots = sorted(p["player_slot"] for p in d["players"])
        total = 0
        for slot, pl in zip(slots, fights[i - 1].get("players", [])):
            is_radiant = slot < 128
            if (side == "radiant") == is_radiant:
                total += pl.get("deaths", 0)
        return total

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
