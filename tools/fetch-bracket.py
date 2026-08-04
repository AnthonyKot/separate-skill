#!/usr/bin/env python3
"""Sample ranked public matches from the reader's own bracket and snapshot them.

    tools/fetch-bracket.py --min 40 --max 55 --target 200 --patch 7.41e --name archon-legend

Writes data/brackets/<name>-<patch>.json: the query, its filters, the fetch date,
the patch it ran under, and the raw rows the aggregates were computed from.

The raw rows are kept deliberately. A registered figure whose underlying sample is
gone is an assertion with a citation attached — checks/data.py recomputes every
registered metric from these rows, so the claim is reproducible rather than merely
re-fetchable. See CONTEXT.md 5.

Rank tiers are two digits: medal (1 Herald ... 8 Immortal) then star. 40-55 is
Archon 1 through Legend 5.

THREE SAMPLING TRAPS, each found only after the previous one was fixed, which is
itself the lesson: a corrected sample looks correct, and the next bias is only
visible once the first stops dominating.

1. LENGTH BIAS. publicMatches returns the most recent FINISHED matches ordered by
   match_id, and a match_id is assigned when the game STARTS. The newest ids are
   therefore the games that ended soonest after starting; a fifty-minute game begun
   at the same moment has not been ingested yet. Sampling the head of this endpoint
   selects for short games. The first sample taken here had a median of 18.6 minutes
   and no game longer than 25.7 in five hundred rows, which is what gave it away.
   Fixed by seeking back --settle-hours before collecting, so every game started in
   the retained window has had time to finish regardless of length.

2. MODE CONTAMINATION. The rank filter does not imply ranked. In one unfiltered
   sample, 58% of rows were Turbo and only 3% were ranked all draft. The reader
   plays ranked all draft; the default filters say so. Note this is the same bias
   wearing a second hat: Turbo dominates the head of the feed BECAUSE Turbo games
   finish fastest. Two days back, ranked all draft is a majority of the rows.

3. TEMPORAL CLUSTERING. Seek once, page forward, and every match collected started
   within about a minute of every other, because the feed is dense enough that 150
   ranked games fit in one minute of match time. One instant is not a sample: it is
   one time of day, one day of the week, one regional mix. Fixed by drawing from
   --windows separate points spread over --spread-hours.

Seeking is done by extrapolation rather than paging: consecutive pages move only
about a minute of match time, so walking back three hours would cost ~170 requests.
"""
import argparse
import datetime
import json
import os
import sys
import time
import urllib.request

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEST = os.path.join(HERE, "data", "brackets")
API = "https://api.opendota.com/api/publicMatches"

sys.path.insert(0, os.path.join(HERE, "checks"))
from metrics import compute  # noqa: E402  shared with checks/data.py, deliberately


def page(min_rank, max_rank, less_than=None):
    url = f"{API}?min_rank={min_rank}&max_rank={max_rank}"
    if less_than:
        url += f"&less_than_match_id={less_than}"
    req = urllib.request.Request(url, headers={"User-Agent": "book6-verify/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def seek(min_rank, max_rank, target_time, probes=8):
    """Return a match_id whose page is at or before target_time, by extrapolation."""
    head = page(min_rank, max_rank)
    ref_id = max(m["match_id"] for m in head)
    ref_t = max(m["start_time"] for m in head)
    cur_id, cur_t = ref_id, ref_t

    for i in range(probes):
        if cur_t <= target_time:
            return cur_id
        # ids per second, measured over the distance travelled so far
        span_t = ref_t - cur_t
        rate = ((ref_id - cur_id) / span_t) if span_t > 60 else 400.0
        jump = int(rate * (cur_t - target_time) * 1.1) or 200_000
        cur_id -= jump
        batch = page(min_rank, max_rank, cur_id)
        if not batch:
            return cur_id
        cur_id = max(m["match_id"] for m in batch)
        cur_t = max(m["start_time"] for m in batch)
        print(
            f"  seek {i + 1}: at {datetime.datetime.fromtimestamp(cur_t, datetime.UTC):%H:%M} UTC, "
            f"{(cur_t - target_time) / 60:+.0f} min from target"
        )
        time.sleep(1.1)
    return cur_id


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--min", type=int, required=True)
    ap.add_argument("--max", type=int, required=True)
    ap.add_argument("--target", type=int, default=200, help="matches wanted after filtering")
    ap.add_argument("--max-pages", type=int, default=120)
    ap.add_argument("--lobby-type", type=int, default=7, help="7 = ranked")
    ap.add_argument("--game-mode", type=int, default=22, help="22 = all draft")
    ap.add_argument("--settle-hours", type=float, default=2.0)
    ap.add_argument("--windows", type=int, default=6, help="separate points in time to sample")
    ap.add_argument("--spread-hours", type=float, default=120.0, help="span the windows cover")
    ap.add_argument("--band-hours", type=float, default=6.0,
                    help="how far from a window target a match may fall before it is discarded")
    ap.add_argument("--patch", required=True)
    ap.add_argument("--name", required=True)
    a = ap.parse_args()

    head = page(a.min, a.max)
    newest_t = max(m["start_time"] for m in head)
    print(
        f"  newest match started {datetime.datetime.fromtimestamp(newest_t, datetime.UTC):%H:%M} UTC"
    )

    # A THIRD TRAP, found after the first two were fixed. Seeking once and then
    # paging forward collects matches that all STARTED WITHIN ABOUT A MINUTE of each
    # other — the feed is dense enough that 150 ranked games fit in one minute of
    # match time. That is not a sample of the bracket, it is a single instant: one
    # time of day, one day of the week, one regional mix. Time of day changes who is
    # playing, and a median game length drawn from a Sunday afternoon in Europe is a
    # fact about Sunday afternoon in Europe.
    #
    # So the sample is drawn from --windows separate points spread across
    # --spread-hours, each already behind the settle horizon.
    per_window = max(1, a.target // a.windows)
    rows, seen, skipped, pages = [], set(), {"mode": 0, "out_of_band": 0}, 0

    for w in range(a.windows):
        offset_h = a.settle_hours + (a.spread_hours * w / max(1, a.windows - 1) if a.windows > 1 else 0)
        target_t = newest_t - offset_h * 3600
        stamp = datetime.datetime.fromtimestamp(target_t, datetime.UTC)
        print(f"\n  window {w + 1}/{a.windows}: seeking to {stamp:%Y-%m-%d %H:%M} UTC (-{offset_h:.0f}h)")
        cursor = seek(a.min, a.max, target_t)

        # The seek extrapolates and routinely overshoots — landing early is safe for
        # the length bias, so it is tuned to overshoot rather than undershoot. But
        # "early" has no floor, and one window here landed 108 DAYS back, dragging
        # matches played under three earlier patches into a snapshot labelled 7.41e.
        # Nothing in the fetch noticed; the sample_span_hours metric did.
        #
        # So a row is only accepted if it actually falls near the window it was
        # sought for. A missed seek now discards rows instead of quietly widening
        # the sample into a different game.
        band = a.band_hours * 3600
        got = 0
        for i in range(a.max_pages):
            batch = page(a.min, a.max, cursor)
            pages += 1
            if not batch:
                break
            for m in batch:
                if m["match_id"] in seen:
                    continue
                seen.add(m["match_id"])
                if abs(m.get("start_time", 0) - target_t) > band:
                    skipped["out_of_band"] += 1
                    continue
                if m.get("lobby_type") != a.lobby_type or m.get("game_mode") != a.game_mode:
                    skipped["mode"] += 1
                    continue
                rows.append(
                    {
                        "match_id": m["match_id"],
                        "duration": m["duration"],
                        "radiant_win": m["radiant_win"],
                        "avg_rank_tier": m.get("avg_rank_tier"),
                        "start_time": m.get("start_time"),
                        "lobby_type": m.get("lobby_type"),
                        "game_mode": m.get("game_mode"),
                    }
                )
                got += 1
            cursor = min(m["match_id"] for m in batch)
            if got >= per_window:
                break
            time.sleep(1.1)
        print(f"    kept {got}  (out of band so far: {skipped['out_of_band']})")

    rows = rows[: a.target]
    snap = {
        "query": {
            "endpoint": "publicMatches",
            "min_rank": a.min,
            "max_rank": a.max,
            "lobby_type": a.lobby_type,
            "game_mode": a.game_mode,
            "settle_hours": a.settle_hours,
            "windows": a.windows,
            "spread_hours": a.spread_hours,
        },
        "pages_fetched": pages,
        "filtered_out": skipped,
        "band_hours": a.band_hours,
        "fetched": datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%d"),
        "patch": a.patch,
        "n": len(rows),
        "matches": rows,
    }
    os.makedirs(DEST, exist_ok=True)
    path = os.path.join(DEST, f"{a.name}-{a.patch}.json")
    with open(path, "w") as f:
        json.dump(snap, f, separators=(",", ":"))

    print(f"\n  {len(rows)} ranked matches -> {os.path.relpath(path, HERE)}")
    print(f"  patch {a.patch}, fetched {snap['fetched']}, {pages} pages, {skipped['mode']} wrong mode")
    print("\n  computed metrics (register any of these in checks/data.tsv):")
    for k, v in sorted(compute(snap).items()):
        print(f"    {k:<24} {v}")
    print(
        "\n  NOTE: a sample of recent ranked matches, not a population. "
        "Any claim registered from it must say so, with its n."
    )


if __name__ == "__main__":
    main()
