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
    objectives_between <start>:<end>:<type>  objectives of that type in a window
    ward_count      <Hero>:<obs|sen>         wards placed
    ward_lifetime   <Hero>:<obs|sen>:<sec>   seconds that ward survived, -1 if never
    ward_uptime     <Hero>:<obs|sen>         ward-seconds contributed (overlaps counted)
    hero_death_time <Hero>:<n>               nth death, 1-based
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


def hero_npc_names():
    """id -> internal name, from the committed map in data/hero-npc-names.json.

    Needed because the internal name is NOT derivable from the localized one for
    19 of 127 heroes: Magnus is magnataur, Clockwerk is rattletrap, Windranger is
    windrunner, Zeus is zuus. The first version of hero_death_time built the
    internal name by lowercasing the localized one, which silently restricted that
    check to the 108 heroes where the guess happens to be right — and ch. 32's
    Crystal Maiden was one of them, so the bug shipped green. It raises rather
    than passing, but a checker that cannot see 15% of the game's heroes is a
    checker that decides which cases the book is allowed to use.
    """
    path = os.path.join(HERE, "data", "hero-npc-names.json")
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

    def _hero(name):
        heroes = hero_names()
        for pl in d["players"]:
            if heroes.get(str(pl.get("hero_id"))) == name:
                return pl
        raise LookupError(f"no {name!r} in this match")

    if check == "ward_count":
        # "<Hero>:<obs|sen>" — wards placed. Position five's resources are not
        # gold, and no other check in this file can see them.
        name, _, kind = arg.partition(":")
        return len(_hero(name).get(f"{kind}_log") or [])

    if check == "ward_lifetime":
        # "<Hero>:<obs|sen>:<placed_seconds>" — how long that ward survived, by
        # matching the entity handle to the corresponding left-log entry.
        # -1 means it was still standing when the game ended.
        name, kind, placed = arg.split(":", 2)
        p_ = _hero(name)
        placed = int(placed)
        gone = {o.get("ehandle"): o["time"] for o in (p_.get(f"{kind}_left_log") or [])}
        for o in p_.get(f"{kind}_log") or []:
            if o["time"] == placed:
                end = gone.get(o.get("ehandle"))
                return -1 if end is None else end - placed
        raise LookupError(f"{name} placed no {kind} ward at {placed}s")

    if check == "ward_uptime":
        # "<Hero>:<obs|sen>" — total seconds of ward uptime contributed, counting
        # only wards whose end is recorded. Overlaps are NOT deduplicated: this is
        # ward-minutes contributed, not minutes of the game covered, and a chapter
        # citing it must say which.
        name, _, kind = arg.partition(":")
        p_ = _hero(name)
        gone = {o.get("ehandle"): o["time"] for o in (p_.get(f"{kind}_left_log") or [])}
        return sum(
            gone[o["ehandle"]] - o["time"]
            for o in p_.get(f"{kind}_log") or []
            if o.get("ehandle") in gone
        )

    if check == "hero_death_time":
        # "<Hero>:<n>" — the nth death, 1-based, from every player's kill log.
        name, _, nth = arg.partition(":")
        heroes = hero_names()
        hid = next((k for k, v in heroes.items() if v == name), None)
        if hid is None:
            raise LookupError(f"unknown hero {name!r}")
        npc = hero_npc_names().get(hid)
        if npc is None:
            raise LookupError(f"no internal name recorded for {name!r}")
        times = sorted(
            k["time"]
            for pl in d["players"]
            for k in (pl.get("kills_log") or [])
            if k["key"] == npc
        )
        i = int(nth)
        if not 1 <= i <= len(times):
            raise LookupError(f"{name} died {len(times)} times, no #{i}")
        return times[i - 1]

    if check == "objectives_between":
        # "<start_sec>:<end_sec>:<type>" — objectives of that type in the window.
        start, end, kind = arg.split(":", 2)
        start, end = int(start), int(end)
        return sum(
            1
            for o in d.get("objectives") or []
            if o.get("type") == kind and start <= o.get("time", -1) <= end
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

    if check == "deaths_with_position":
        # How many hero deaths carry map coordinates. Added when ch. 01 turned out
        # to assert the record holds none, which is false: OpenDota records
        # deaths_pos on teamfight players, so a death INSIDE a fight window has an
        # x and a y and a death outside one does not.
        #
        # The chapter's argument survives the correction and improves — the deaths
        # it examines are the ones the record cannot place — but the sweeping
        # sentence was wrong and had been sitting on a published page.
        return sum(
            c
            for t in (d.get("teamfights") or [])
            for pl in t.get("players", [])
            for ys in (pl.get("deaths_pos") or {}).values()
            for c in ys.values()
        )

    if check == "wards_standing_at":
        # "<obs|sen>:<seconds>" — how many of that ward type were standing at that
        # moment, from the placement and removal logs. This is vision state
        # reconstructed at an arbitrary timestamp, which ch. 01 also said the
        # record does not contain. It does.
        kind, _, when = arg.partition(":")
        when = int(when)
        standing = 0
        for pl in d["players"]:
            gone = {o.get("ehandle"): o["time"] for o in (pl.get(f"{kind}_left_log") or [])}
            for o in pl.get(f"{kind}_log") or []:
                end = gone.get(o.get("ehandle"))
                if o["time"] <= when and (end is None or when <= end):
                    standing += 1
        return standing

    if check == "ward_ended_by":
        # "<Hero>:<obs|sen>:<placed_seconds>" -> "expired", or the internal name of
        # whatever killed it.
        #
        # The left-log carries `attackername`, and it is SELF-ATTRIBUTED when a ward
        # runs out: an expiring ward is credited to the hero who placed it. So
        # expiry versus destruction is a fact in the record, not an inference from
        # duration — which matters, because both ch. 32 and ch. 02 inferred it from
        # duration and both got it wrong. Ch. 32 called eleven wards expired when
        # ten expired and two were killed, one of them after 351 seconds, which no
        # duration heuristic would ever have caught.
        name, kind, placed = arg.split(":", 2)
        p_ = _hero(name)
        placed = int(placed)
        gone = {o.get("ehandle"): o for o in (p_.get(f"{kind}_left_log") or [])}
        for o in p_.get(f"{kind}_log") or []:
            if o["time"] == placed:
                e = gone.get(o.get("ehandle"))
                if e is None:
                    return "standing"
                att = e.get("attackername") or "unknown"
                own = hero_npc_names().get(str(p_.get("hero_id")))
                return "expired" if att == own else att
        raise LookupError(f"{name} placed no {kind} ward at {placed}s")

    if check == "ward_fates":
        # "<Hero>:<obs|sen>:<expired|destroyed|standing>" — how many of that hero's
        # wards met that end. Registers the AGGREGATE, which is where ch. 32 went
        # wrong: individual lifetimes were registered and correct, and the sentence
        # that counted them was not checked by anything.
        name, kind, want = arg.split(":", 2)
        p_ = _hero(name)
        own = hero_npc_names().get(str(p_.get("hero_id")))
        gone = {o.get("ehandle"): o for o in (p_.get(f"{kind}_left_log") or [])}
        n = 0
        for o in p_.get(f"{kind}_log") or []:
            e = gone.get(o.get("ehandle"))
            if e is None:
                fate = "standing"
            else:
                fate = "expired" if (e.get("attackername") == own) else "destroyed"
            if fate == want:
                n += 1
        return n

    if check == "wards_standing_side_at":
        # "<obs|sen>:<radiant|dire>:<seconds>" — how many of that ward type ONE
        # SIDE had standing at that moment. Ch. 02's whole argument is the vision
        # asymmetry at a single instant, and a total across both teams hides it.
        kind, s, when = arg.split(":", 2)
        when = int(when)
        want_radiant = s == "radiant"
        standing = 0
        for pl in d["players"]:
            if (pl["player_slot"] < 128) != want_radiant:
                continue
            gone = {o.get("ehandle"): o["time"] for o in (pl.get(f"{kind}_left_log") or [])}
            for o in pl.get(f"{kind}_log") or []:
                end = gone.get(o.get("ehandle"))
                if o["time"] <= when and (end is None or when <= end):
                    standing += 1
        return standing

    if check == "team_gold_rank":
        # "<Hero>:<minute>" — that hero's rank by gold within their OWN five, 1 =
        # richest. Added for ch. 30, whose argument is that the offlane's advantage
        # is real, recorded, and recorded in a place that stops describing it.
        #
        # It exists as a check type rather than as five registered gold figures and
        # a sentence, because "he was the richest player on his team" is the claim
        # the chapter actually makes, and a claim assembled by the author from five
        # numbers is an editorial reading that no checker can recompute. The rule in
        # CONTEXT.md 10 is that the machinery grows to fit the argument.
        name, _, minute = arg.partition(":")
        p_ = _hero(name)
        m = int(minute)
        side = p_["player_slot"] < 128
        mine = [
            q for q in d["players"] if (q["player_slot"] < 128) == side
        ]
        for q in mine:
            if m >= len(q.get("gold_t") or []):
                raise LookupError(f"minute {m} is past the end of a gold series")
        mine.sort(key=lambda q: -q["gold_t"][m])
        return mine.index(p_) + 1

    if check == "hero_series_gap_at":
        # "<HeroA>:<HeroB>:<gold|xp|lh>:<minute>" — A minus B, signed.
        #
        # The gap is registered rather than derived in prose for one reason: the
        # sign changes during ch. 30's case, and a chapter whose argument turns on
        # a sign change must not compute that sign by hand. Two registered values
        # and a subtraction in the author's head is exactly how ch. 21 published
        # "three deaths" against its own claim of four.
        a, b, series_name, minute = arg.split(":", 3)
        key = {"gold": "gold_t", "xp": "xp_t", "lh": "lh_t"}[series_name]
        m = int(minute)
        out = []
        for name in (a, b):
            series = _hero(name).get(key) or []
            if m >= len(series):
                raise LookupError(f"{name} has {len(series)} minutes, no {m}")
            out.append(series[m])
        return out[0] - out[1]

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
