# Winning Is a Separate Skill

**Read it: <https://anthonykot.github.io/separate-skill/>**

Thirty-two chapters on Dota 2 decision-making, for a player with two thousand hours who keeps losing
games they understood while they were losing them.

Sixth in a series built the same way, after
[The Quantum Quartet](https://anthonykot.github.io/quantum-quartet/),
[The Bridge](https://anthonykot.github.io/quantum-bridge/),
[No Such Form](https://anthonykot.github.io/fermat-last-theorem/),
[The Going Concern](https://anthonykot.github.io/going-concern/) and
[DutchABC](https://anthonykot.github.io/dutch-abc/).

**Corrections welcome**, especially about the Dota. The script checks that quoted figures are real.
It cannot check whether a case supports the lesson drawn from it, or whether a principle survives at
your bracket.

## Status

**Five chapters of thirty-two are written, and all five are pilots.** They were drafted and reviewed
before the remaining chapters are commissioned, each testing a different way this book could fail.
`checks/status.py` verifies that sentence against the files on disk, because it went stale here once
already.

| | |
|---|---|
| `CONTEXT.md` | The foundations: reader, spine, template, sourcing standard, chapter register |
| `NOTES.md` | The working notebook: unsettled things, plans, and what was rejected |
| `checks/` | Eight verifiers, seven gating, all negative-controlled |
| `docs/` | The static site — contents, method, and the chapters |
| `data/` | Committed match snapshots and bracket samples |

| Pilot | What it tests | What it found |
|---|---|---|
| 01 | Does the method avoid hindsight? | A hold must offer a way to pass; instructing a reader to do the impossible tests obedience |
| 12 | Do general principles survive item specificity? | One hold, not two — a second belongs to a neighbouring chapter |
| 21 | Does professional evidence transfer? | Yes, with a transfer block; the case shows a stall, not a loss |
| 32 | Does a seat chapter produce different advice? | **The premise was wrong.** Nothing inverts; what changes is what is scarce, visible and presumed |
| 30 | Is that variation indexed by seat, or by something else? | **Neither, as posed.** The test's own premise — that the offlane's product is invisible — is contradicted by the record. What separates the two seats is how long each stays visible |

## The premise

Dota instruction is organised by hero, by role, or by phase — parallel modules readable in any order.
This is organised as a **diagnostic sequence**. Whether a fight was a mistake cannot be diagnosed
until it is established whether the player arrived alive, arrived resourced, and had converted those
resources into something the fight could use. A bad fight often begins five minutes earlier in the
item queue.

The reader is defined by what they can and cannot do rather than by hours: someone who executes their
familiar heroes at bracket level and repeatedly chooses the wrong place, purchase, moment or
objective. Anyone whose *intended* actions fail mechanically needs a different book first, and
`CONTEXT.md §1` says so.

## Sourcing, and how to check it

Four classes, ordered by distance from the game: Valve's official record, the machine-derived match
record, direct observation of a replay, and interpretive commentary — which never supplies a number.

```bash
./verify.sh                  # everything
./verify.sh --links          # internal links only, no network
python3 checks/patchnotes.py # registered strings vs Valve's datafeed
python3 checks/matches.py    # registered events vs committed snapshots
python3 checks/data.py       # bracket figures recomputed from their sample
```

Unlike its predecessors, **every check here is gating** — with one deliberate exception, stated
rather than buried. Books 4 and 5 could only mark claim checks advisory, because they read HTML on
other people's servers and a moved page is not an error. Two things changed that:

- **Valve publishes structured patch notes.** `dota2.com/datafeed/patchnotes?version=7.41&language=english`
  returns versioned, timestamped JSON. The human-facing `/patches/{version}` pages are a JavaScript
  shell serving an identical 46,711-byte document for every version, so hashing them would have
  verified nothing.
- **Match evidence is committed.** Each registered case has its parsed JSON snapshot in
  `data/matches/`, so a failure is always this repository's fault.

Gating also means an **unreachable source fails the build**. The first version of the patch checker
printed `SKIP` and returned 0 when it could not reach a source, so a DNS failure produced a green
build indistinguishable from a verified one.

**The exception**: bracket figures are gating when *recomputed from the sample committed beside
them*, and advisory when compared against a fresh sample of live play. Those are two different
questions — one about this repository, one about the current game — and only the first can be
somebody's fault. Giving both the same name is how the foundations came to say "advisory" while the
code said "gating"; caught on review, 2026-08-04.

**What a green build proves:** every registered figure is present in the record it is attributed to,
checked by something that could actually see that record. **What it does not prove:** that the advice
is right. The previous book shipped a chapter where every claim verified and the central causal arrow
pointed backwards.

## Bracket evidence

Claims about what Archon–Legend players do are sourced from Archon–Legend games, not from
professional matches:

```bash
tools/fetch-bracket.py --min 40 --max 55 --target 240 --patch 7.41e --name archon-legend
```

Four sampling biases were found and fixed while writing that tool, each visible only after the
previous one was corrected — length, mode, temporal clustering, and a seek that drifted across
patches. The first sample it produced reported a median game length of 18.6 minutes; corrected, the
same bracket reads 39.8. Both came from the same short program. The header of
`tools/fetch-bracket.py` documents all four.

Six bracket claims are registered from a corrected sample of 240 ranked Archon–Legend matches:
median game length 39.9 minutes, 49.6% running past forty. Every match in it was played after 7.41e
shipped, which `checks/data.py` enforces — a sample containing games older than the patch it is
labelled with fails the build.

## Stack

Plain HTML, one stylesheet, one small script. No build step, no framework, no static-site generator,
no CDN, no trackers. `.nojekyll` so GitHub Pages serves the committed HTML as-is. Light/dark theme
honouring `prefers-color-scheme` with a manual toggle in `localStorage`.

Caster transcripts are research material and are never committed: `data/transcripts/` is gitignored,
and `verify.sh` fails if one is ever tracked. The commentary belongs to the people who made it, it
supplies hypotheses rather than numbers, and it is not this repository's to redistribute.
