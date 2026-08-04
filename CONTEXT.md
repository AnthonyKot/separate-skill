# CONTEXT — *Winning Is a Separate Skill*

Working title. Working document. What this book is, what it refuses to be, and the rules that keep
thirty-two chapters sounding like one writer.

Sixth in the series, after *The Quantum Quartet*, *The Bridge*, *No Such Form*, *The Going Concern*
and *DutchABC*. It inherits their machinery — computed counts, registered claims, a verify script
that fails the build — and changes the evidence model, because this subject has something none of
the others had: **the reader can open the replay.**

---

## 1. The decision record

Settled at the outset. Not to be relitigated without a reason.

| Question | Decision | Why |
|---|---|---|
| Reader | **The hardstuck adult.** Two thousand hours or more, Archon–Legend, thirty to forty-five, three to six games a week. Knows every hero, every item, most interactions. Loses for structural reasons. | Underserved and specifically shaped. Beginner guides teach what they already know; pro analysis shows them things they cannot execute. Nobody writes for the player whose problem is not knowledge. |
| Thesis | **Winning is a separate skill from playing.** The reader's mechanics are adequate for the bracket they are in. What is missing is a decision sequence. | It is what the evidence keeps showing, including at the professional level — see the case in `data/matches/m8929124210.json`, where a team with two lanes of barracks and a sixteen-thousand-gold lead needed another eleven minutes to finish. |
| Evidence | **The pairing.** Parsed match JSON establishes *what happened*; caster commentary supplies *why*, and is then tested against the JSON. Neither source is used alone. | §5. This is the book's central device and the reason it can say things other guides cannot check. |
| Structure | **General chapters first, role chapters last.** Parts I–VI are decisions all five positions face. Part VII is one chapter per seat. | A role-specific prescription is illegible until the general sequence is in place — the same dependency logic that orders the parts. Part VII's real job is to name which earlier chapters *invert* for that seat. |
| Register | **Funny, and exact.** The humour comes from naming the disaster the reader has personally lived, accurately enough that they wince. | §4. A book this reader finds boring does not get read, and the genre's alternative register — confident, numberless, faintly contemptuous — is the thing being replaced. |
| Scope | **No coaching, nothing sold.** No VOD review service, no Discord, no rank guarantee. | Series rule. The book ends and that is all it does. |

## 2. The spine

The parts are ordered because the questions are ordered. A later question is not merely subsequent —
it is **unreadable** until the earlier one is answered. A player who studies power spikes while dying
twelve times a game is tuning an engine that is not attached to anything.

> **staying alive → resources → spending them → timing → ending → keeping it → your seat**

| Part | Question | Why it gates the next | Ch. |
|---|---|---|---|
| I | Can you stop dying for free? | Every later skill is unmeasurable at twelve deaths. Deaths are the denominator. | 01–05 |
| II | Can you get gold and XP? | Nothing to convert until this works. | 06–10 |
| III | Are you spending it, or hoarding it? | Farm you never spend is not farm. This is where most of the bracket actually lives. | 11–15 |
| IV | Do you fight when you are strong? | Requires knowing what you have, which is Part III. | 16–20 |
| V | Can you actually end? | The only part that wins games, and the last to become legible. | 21–24 |
| VI | Can you keep it across patches? | A season, not a game. | 25–27 |
| VII | Which of this changes for your seat? | Needs all of the above to have something to invert. | 28–32 |

**Part III is the load-bearing part** and should be the best in the book. The reader's characteristic
failure is not that they farm badly — it is that they farm *instead of deciding*. Farming is the
comfortable act, the one with continuous feedback and no risk of blame, and it is available at every
moment of every game. This is the exact analogue of book 4's developer who writes code instead of
selling.

## 3. Chapter template

Filename: `chapters/NN-slug.html`. Four moves, fixed order, fixed headings.

1. **The situation** — the decision, stated concretely, second person, present tense, from inside a
   real game state. *"It is twenty-four minutes. You have your first big item. Two of them are
   missing and you have no idea where."* No throat-clearing, no history of the game.
2. **What actually happened** — one named, dated, **replay-verifiable** match. Match ID stated. At
   least two hard figures from the JSON. This is the load-bearing move; if the case is thin the
   chapter is thin.
3. **The reasoning** — the transferable principle, *with its boundaries stated in the same breath*.
4. **Next game** — three to five things to do in your next game. Concrete enough to fail at. No
   "consider", no "try to", no "be aware of".

Then the **inversion** block, then **the replay** (match ID, timestamps, what to watch for).

### The honesty mechanism: the inversion

Book 4 uses the counter-case because business failure is unpublished. This book's characteristic
failure is different and far more tractable: **Dota advice is true at one bracket and false at
another, and true in one patch and false in the next.** Every confident guide on the internet fails
exactly there, and none of them say so.

So every chapter must state where its own advice stops being true — and where the data allows, must
*show* it rather than assert it, because pick and win rates are published stratified by bracket.
An inversion is a query, not an opinion.

| Block | What it is | Satisfies the rule? |
|---|---|---|
| `.inversion` | The chapter's advice, correctly applied, producing a worse result — at a stated bracket, patch or draft | **Yes** — this is the rule |
| `.limit` | A qualification that narrows the advice without inverting it | **No** |
| `.owed` | A visible note that no inversion was found, saying what it would have to be | **No — but it is the honest fallback** |

The pull will be to call a boundary an inversion, because the alternative is an admission. Book 4 did
this in three of its first four chapters. Score the candidate against the chapter's *central* advice,
clause by clause, before claiming a fit.

### Standing constraint: the book must not become a licence to blame the team

Set before chapter 1, because it is this book's version of the failure book 4 only noticed at
chapter 7 — the risk created by the book's own virtues.

A rigorous, well-sourced book about decision quality, handed to a hardstuck player, can be read as
ammunition. Every chapter that explains what *should* have happened gives the reader a sharper
vocabulary for describing what their teammates did wrong. That is the opposite of the intended
effect and it will happen by default, because it is the more comfortable reading.

Three rules follow.

1. **Every chapter's `Next game` list contains only actions the reader takes alone.** If an item
   requires a teammate to cooperate, it is not an item. This is a checkable trip-wire.
2. **No chapter may end on a decision someone else made.** The case may involve five players; the
   lesson is always about the seat the reader occupies.
3. **The blame register is banned outright** — §4. Not softened, banned.

## 4. Voice

- **Second person for the reader, third for the match.** "You have no vision" / "Yakult took top rax at 34:46."
- **Present tense in the situation, past in the case.**
- **Numbers or nothing.** A case without figures is a story about a game. Every figure traces to §5.
- **Funny by accuracy.** The joke is the recognition, never a meme, never a reference. If a line
  would land the same way with the numbers removed, it is decoration and it goes.
- **Banned register — blame.** No trash, throwing accusations, griefer, int, "your team". The reader
  plays with humans and will be one of them in the next game. This is not politeness; a book that
  licenses contempt teaches the reader to stop looking at their own replay.
- **Banned words — the guide register.** *Just*, *simply*, *obviously*, *of course*, *literally
  everyone knows*. Each one asserts that the thing being explained is easy, which is false, and is
  the exact tone the reader has already failed to learn from.
- **No hero players.** The point of a case is the decision. Nobody in this book is a genius.
- **Name the failure mode inside the principle**, not in a footnote.

### Provocations are not laws

The prose is sharp; the genre's failure is letting a memorable sentence harden into a universal
claim. Every compression gets complicated inside the chapter that makes it. A provocation may open a
chapter or a part. It may not close one.

## 5. Sourcing standard

Three classes, and they are not equal.

| Class | What | Strength |
|---|---|---|
| **Primary** | Official patch notes at dota2.com, dated; parsed match JSON from the OpenDota API; the full draft in `picks_bans` | Quotable directly, registered in `checks/` |
| **Secondary** | Named analysis published with a date and a byline; a team's own contemporaneous post | Quotable, cited |
| **Weakest** | Caster commentary, a player's later recollection, bracket consensus | **Never a number.** See below |

### The pairing

The device the book is built on, and the reason both sources are needed:

- **The JSON cannot tell you why.** It records that Radiant did not move on high ground between
  35:00 and 46:00. It has no theory about it.
- **The caster can, and is often wrong.** Casters work live, with partial information, and speculate
  out loud. That is their job, not a defect.

So: **commentary supplies the hypothesis; the JSON tests it.** When a caster says *"they've got no
buyback here"*, that is not a quote to reproduce — it is a claim, and `buyback_log` settles it. A
chapter may report that the caster's reading was wrong. That is one of the more valuable things this
book can do, and it is only possible because both sources are present.

### Hard prohibitions

- **A transcript never supplies a number, and never enters this repository.** `data/transcripts/` is
  gitignored. The commentary is someone else's expression: short attributed quotes only, ideas free,
  expression not. Same rule as book 4 §5c and book 5's `sources/`.
- **A VOD is bound to a match by evidence, never by its title.** Found the hard way on day one — see
  §8. Confirm against `picks_bans`, team names and duration.
- **Pub win rate is never a prescription.** A hero's win rate is confounded by who picks it and what
  they are picking into. It may describe a population; it may not instruct a reader. This is the
  single largest contamination risk in the genre — the analogue of book 4's round numbers that appear
  in every blog post.
- **No number from memory.** Cooldowns, gold values, mana costs, timings. Every one is a claim row
  against the patch notes or the match record. Including numbers that "everybody knows" — those are
  the ones that are two patches stale.
- **No meta claim without a patch number and a date.**
- **The altitude error, named so it can be caught.** Using a professional match to justify an action
  available to an Archon, without stating what is different. Pro players have five coordinated
  teammates and this reader has four strangers. Every case drawn from a pro match must say what
  transfers and what does not. This is expected to be the most common defect in drafts.

### Claim classes

Three files, three checkers, because the sources verify differently:

| File | Claim | Check | Gating? |
|---|---|---|---|
| `checks/claims.tsv` | Exact string in a dated patch note | String still present | Advisory — other people's servers |
| `checks/matches.tsv` | An event in a registered match | Re-fetch, assert against the JSON | **Gating** — snapshot is committed |
| `checks/data.tsv` | An aggregate query, stamped with the patch it ran under | Re-run, compare within tolerance, diff the snapshot | Advisory — drift is the game changing, which is information |

Note what this proves and what it does not. It proves every registered figure is really in the record
it is attributed to. It cannot tell you whether the case supports the lesson drawn from it — book 4
shipped a chapter whose every claim passed while its central causal arrow pointed backwards. **A green
build means the numbers are real. It does not mean the advice is.**

## 6. Chapter register

Legend: ☐ not started · ◐ drafted · ☑ written and sourced

### Part I — Can you stop dying for free?
| # | Title | Status |
|---|---|---|
| 01 | The Death You Didn't Notice | ☐ |
| 02 | What the Map Already Said | ☐ |
| 03 | The Thirty Seconds Before | ☐ |
| 04 | Leaving Is a Skill | ☐ |
| 05 | The Death You Should Have Taken | ☐ closes Part I |

### Part II — Can you get gold and XP?
| # | Title | Status |
|---|---|---|
| 06 | Two Resources, and You Count One | ☐ |
| 07 | The Lane Is Not the Game | ☐ |
| 08 | The Map Is Full of Money | ☐ |
| 09 | Farming a Map You Don't Control | ☐ |
| 10 | Efficient Is Not Fast | ☐ closes Part II |

### Part III — Are you spending it, or hoarding it?
| # | Title | Status |
|---|---|---|
| 11 | Gold in the Bank Is Not Gold | ☐ |
| 12 | The Item You Want and the Item That Wins | ☐ |
| 13 | Buying for Them | ☐ |
| 14 | Reading the Scoreboard | ☐ |
| 15 | Enough Farm | ☐ closes Part III |

### Part IV — Do you fight when you are strong?
| # | Title | Status |
|---|---|---|
| 16 | The Spike | ☐ |
| 17 | Cooldowns Are the Real Clock | ☐ |
| 18 | Vision Is a Timing | ☐ |
| 19 | No Fight Without a Reason | ☐ |
| 20 | The Fight You Declined | ☐ closes Part IV |

### Part V — Can you actually end?
| # | Title | Status |
|---|---|---|
| 21 | The Lead That Melts | ☐ · earmarked: match 8929124210 |
| 22 | High Ground Is a Different Game | ☐ |
| 23 | Roshan and the Two-Minute Window | ☐ |
| 24 | Ending | ☐ closes Part V |

### Part VI — Can you keep it?
| # | Title | Status |
|---|---|---|
| 25 | Reading a Patch | ☐ |
| 26 | Five Heroes Is a Strategy | ☐ |
| 27 | The Queue Is Part of the Game | ☐ |

### Part VII — The five seats
| # | Title | Status |
|---|---|---|
| 28 | Position One | ☐ |
| 29 | Position Two | ☐ |
| 30 | Position Three | ☐ |
| 31 | Position Four | ☐ |
| 32 | Position Five | ☐ |

Each Part VII chapter has one job beyond its own advice: **name the earlier chapters that invert for
this seat, and say why.** A chapter that merely restates general advice in role-flavoured language
has failed and should be cut.

## 7. Match ledger

Five fields per match, written **when the match is first used**, consulted before it is reused. Ported
from book 4 §6b, including the correction that cost that book a chapter: a case is spent when it has
carried **the same inference**, not when it has merely appeared. Before declaring a match spent, name
the inference the earlier chapter drew. A different question asked of the same match is continuity.

Fields: **Facts** (registered figures) · **Permitted** (what it may be used to show) · **Confounders**
(what else was happening) · **Prohibited** (the claim it must never carry) · **Spent** (what each
chapter took).

*Prohibited* is the load-bearing field. It is what catches a chapter drawing a conclusion its own
evidence cannot support, and no claim checker will ever flag it.

### 8929124210 — Yakult Brothers vs Rune Eaters, The Games of the Future 2026
Earmarked for ch. 21. Ledger to be written when the chapter is drafted, not before — book 4
reconstructed one afterwards and found it materially harder.

## 8. What got caught

The table of errors the process caught, kept because the sequence teaches more than any single fix.

**Day one, before a word was written — a transcript from the wrong game.** Searching YouTube for a
named tournament returned a video whose title gave a Dota-shaped tournament, a grand final and two
team names. The captions were Mobile Legends. Games of the Future is a multi-discipline event and the
title was accurate about everything except the game being played. Nothing in a title, a channel name
or a search ranking binds a video to a match. **Rule that came out of it: bind by `picks_bans`, team
names and duration, or do not use the VOD.** Cost: about four minutes, because it was caught in a
sampling pass. Had it been caught after a chapter was drafted around it, the cost would have been the
chapter.

## 9. The pipeline

Built for parallelism where the work is genuinely independent, and strictly serial where it is not.

**Parallel: research.** Case-finding, transcript harvesting and claim registration for different
chapters have no dependencies. These fan out — one agent per chapter, each in its own git worktree,
each returning a candidate match, its ledger fields and a draft claim set.

**Serial: drafting.** The spine means chapter *N* may use anything from 1…*N*−1 and nothing later.
Drafting out of order produces chapters that silently re-teach earlier material or lean on later
material. Parts may overlap slightly; chapters within a part may not.

**Operational limits found on day one:** the OpenDota API is unauthenticated and generous; YouTube
rate-limits hard (HTTP 429 after four caption requests). Transcript harvesting is a paced background
job, never inline. There is no local ASR fallback — neither `ffmpeg` nor `whisper` is installed — so
a VOD without captions is currently unusable.

### The reviewer panel

Four reviewers that fail differently, which is the entire point. A model reviewing its own prose
agrees with itself.

| Reviewer | Job | Why |
|---|---|---|
| `codex` | Checking machinery, claim/prose consistency, the verify script | Strongest on code and on whether an assertion matches its evidence |
| `grok` | Whether the Dota is actually right | Most current game discourse; the one likeliest to catch a two-patch-stale claim |
| `gemini` | Structure, long-range coherence, repetition across chapters | Long context, and reads the book as a book |
| The author, with GPT, on deployed pages | Whether it reads | The only review that sees what a reader sees. Manual, and last |

Reviews run against a drafted chapter, in parallel, each with the chapter and this file. Findings are
triaged by the author; nothing is applied automatically. Book 4's record is the argument for this:
every one of its worst errors passed the mechanical checks and was caught by a reader.
