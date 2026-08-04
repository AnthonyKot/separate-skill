#!/usr/bin/env python3
"""The metric definitions, in one place.

Imported by BOTH tools/fetch-bracket.py (which prints them when a sample is taken)
and checks/data.py (which recomputes them when a claim is verified). One definition,
two callers, on purpose: if the fetcher and the checker each carried their own
arithmetic they could drift apart, and the check would then be verifying the
checker rather than the claim.
"""


def _median(xs):
    xs = sorted(xs)
    if not xs:
        return None
    mid = len(xs) // 2
    return xs[mid] if len(xs) % 2 else (xs[mid - 1] + xs[mid]) / 2


def compute(snapshot):
    """Return every metric derivable from a bracket snapshot, as {name: value}."""
    rows = snapshot.get("matches") or []
    n = len(rows)
    if not n:
        return {"n": 0}

    durations = [r["duration"] for r in rows]
    tiers = [r["avg_rank_tier"] for r in rows if r.get("avg_rank_tier")]
    radiant_wins = sum(1 for r in rows if r["radiant_win"])

    out = {
        "n": n,
        "radiant_win_pct": round(100.0 * radiant_wins / n, 2),
        "median_duration_s": _median(durations),
        "mean_duration_s": round(sum(durations) / n, 1),
        "shortest_duration_s": min(durations),
        "longest_duration_s": max(durations),
        "pct_over_40min": round(100.0 * sum(1 for d in durations if d > 2400) / n, 2),
        "pct_under_25min": round(100.0 * sum(1 for d in durations if d < 1500) / n, 2),
    }
    if tiers:
        out["median_rank_tier"] = _median(tiers)
        out["min_rank_tier"] = min(tiers)
        out["max_rank_tier"] = max(tiers)

    # The window the sample actually came from, computed from the rows rather than
    # from the fetch date. The seek in tools/fetch-bracket.py deliberately overshoots
    # backwards — landing early is safe, landing late reintroduces the length bias —
    # so "when was this fetched" and "when were these games played" are different
    # questions, and a chapter citing this sample needs the second one.
    starts = [r["start_time"] for r in rows if r.get("start_time")]
    if starts:
        out["earliest_start"] = min(starts)
        out["latest_start"] = max(starts)
        out["sample_span_hours"] = round((max(starts) - min(starts)) / 3600.0, 2)
    return out
