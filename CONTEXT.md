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
| Reader | **The hardstuck adult**, defined by what they can and cannot do rather than by hours. **In:** a player who can execute their familiar heroes at bracket level, and who repeatedly chooses the wrong place, the wrong purchase, the wrong moment or the wrong objective. Typically Archon–Legend, thirty to forty-five, three to six games a week. **Out:** a player whose *intended* actions routinely fail — chronically poor CS at ten under free farm, camera and hotkey problems, micro they cannot perform. That reader needs a different intervention first, and the book must say so instead of flattering them. | The surveyed public English-language material rarely addresses either group precisely; it teaches beginners what exists and shows improvers professional play they cannot execute. Stating the exclusion is what makes the inclusion mean anything. |
| Thesis | **Winning is a separate skill from playing.** For the reader defined above, the missing piece is a decision sequence rather than execution. | **This is the book's working hypothesis, not an established finding**, and it stays labelled as one until target-bracket evidence supports it. Note what cannot support it: match 8929124210 shows a professional team fail to convert, which is ch. 21's case and nothing more. A pro comeback cannot establish what usually keeps Archon–Legend adults stuck, and the first draft of this row cited it as though it could. |
| Evidence | **Four sources, ranked by distance from the game, and no chapter is required to use all of them.** Parsed data establishes registered events. Replay observation supplies visible context. Commentary proposes hypotheses. **Nothing available supplies intention.** | §5. The first version of this row made caster commentary mandatory in every chapter, which would have required a *broadcast* in every chapter — quietly converting a book for Archon–Legend players into a book about professional Dota, with the actual reader appearing only in qualifications. Caught on meta-review. |
| Structure | **General chapters first, role chapters last.** Parts I–VI are decisions all five positions face. Part VII is five full chapters, one per seat, each carrying its own case and its own actions *as well as* the inversions of earlier chapters for that seat. | A role-specific prescription is diagnostically premature until the general sequence is in place. Note the standing tension, which is real and must not be resolved by pretending: general advice is often *false until inverted by seat*, so Parts I–VI and Part VII each make the other honest. |
| Register | **Funny, and exact.** The humour comes from naming the disaster the reader has personally lived, accurately enough that they wince. | §4. A book this reader finds boring does not get read, and the genre's alternative register — confident, numberless, faintly contemptuous — is the thing being replaced. |
| Scope | **No coaching, nothing sold.** No VOD review service, no Discord, no rank guarantee. | Series rule. The book ends and that is all it does. |

## 2. The spine

The parts form a **diagnostic sequence**, not a claim that Dota is linear. Later decisions can be
understood on their own — high-ground discipline is comprehensible to a Crusader — but they cannot be
*diagnosed* reliably until the earlier constraints have been checked. A bad fight may begin thirty
seconds before contact; it may also begin five minutes earlier in the item queue, and you cannot tell
which without working backwards through the sequence.

The first version of this section claimed a later question was **unreadable** until the earlier one
was answered. That is false and was corrected on review. Dota is a web, not a chain. What survives is
the diagnostic order, and it is the book's only structural invention — the reason to keep it is that
nothing else published organises the game this way, and the reason to state it carefully is that the
strong version is untrue.

> **survive with purpose → acquire resources → convert them into capability → act while it matters →
> convert advantage → keep the framework current → invert by seat**

| Part | Question | What it establishes for the next | Ch. |
|---|---|---|---|
| I | Can you distinguish free deaths from necessary risk? | Whether the player arrived at the situation alive, and whether the deaths were avoidable. | 01–05 |
| II | Can you get gold and XP? | Whether they arrived adequately resourced. | 06–10 |
| III | Can you turn resources into capability? | What their resources now permit them to do. | 11–15 |
| IV | Do you act while it matters? | Whether they act before that permission expires. | 16–20 |
| V | Can you convert advantage into a win? | Whether the action changed the game state that actually wins. | 21–24 |
| VI | Can you keep the framework current? | A season, not a game. | 25–27 |
| VII | Which of this changes for your seat? | Where the general advice is false until inverted. | 28–32 |

**Parts I and II describe one loop.** You die *while* farming and rotating; where you stand, which
camp is next, when you leave for a wave and when you leave at all are the same decision viewed twice.
They are separated here for teaching, and any chapter that treats them as genuinely independent has
misread this section.

**Part III is the hinge; Part V is the payoff.** Part III establishes what the player's resources
permit. Part IV asks whether they act before that permission expires. Part V asks whether the action
changed the state that actually wins games.

What the book will *not* claim is where the bracket "mostly lives". An earlier draft of this section
said Part III was where most of the reader's problems are, which is a prevalence claim with no
bracket evidence behind it — forbidden by §5, in the book's own foundations, three sections later.

One thing Part III should say and can defend: farming is the comfortable act. It has continuous
feedback, it never gets you blamed, and it is available at every moment of every game. That is the
exact analogue of book 4's developer who writes code instead of selling, and it is a claim about
incentives rather than about frequency.

## 3. Chapter template

Filename: `chapters/NN-slug.html`. Four moves, fixed order, fixed headings.

1. **The situation** — the decision, stated concretely, second person, present tense, from inside a
   real game state. *"It is twenty-four minutes. You have your first big item. Two of them are
   missing and you have no idea where."* No throat-clearing, no history of the game.
2. **What actually happened** — one named, dated, **replay-verifiable** match. Match ID stated. At
   least two hard figures from the record. This is the load-bearing move; if the case is thin the
   chapter is thin.
3. **The reasoning** — the transferable principle, *with its boundaries stated in the same breath*.
   This move must keep four things visibly apart, because collapsing them is how a guide starts
   inventing: **observed fact** (it is in the record), **supported inference** (it follows from the
   record), **hypothesis** (it is a reading, and other readings exist), and **unknowable intention**
   (why a human did something, which no source in this book can establish).
4. **Next game** — three to five things to do in your next game. Concrete enough to fail at. No
   "consider", no "try to", no "be aware of". Solo-actionable only, per the standing constraint.
5. **After the game** — the review loop. A timestamp to open, one observable decision to look at,
   and a pass/fail criterion stated in advance. Three to six games a week is not enough repetition
   to install a habit by volume, so the reader has to get the repetitions from review instead. This
   is what makes the book's audience wedge structural rather than a line in the marketing.

Then the **boundary** block, optionally the **inversion**, then **the replay** (match ID, timestamps,
what to watch for).

### The honesty mechanism: the inversion

Book 4 uses the counter-case because business failure is unpublished. This book's characteristic
failure is different and far more tractable: **Dota advice is true at one bracket and false at
another, and true in one patch and false in the next.** Every confident guide on the internet fails
exactly there, and none of them say so.

So every chapter must state where its own advice stops being true — and where the data allows, must
*show* it rather than assert it, because pick and win rates are published stratified by bracket.
A genuine inversion is a query, not an opinion.

**The mandatory block is the boundary. The inversion is earned, not required.** This is a correction
to the original design and the reasoning matters more than the rule: three plausible inversions were
found in a single review pass, and it does not follow that thirty-two exist. A device that *demands*
one per chapter would manufacture the rest — fake bracket flips, win-rate theatre, a hero chart
pressed into service as an epistemology. That is book 4's counter-case failure with the labels
changed, and this book has the advantage of knowing about it in advance.

| Block | What it is | Required? |
|---|---|---|
| `.boundary` | Where the advice stops applying — the stated conditions under which the chapter's prescription is not the right move | **Yes, every chapter** |
| `.inversion` | The advice, correctly applied, producing a *worse* result at a stated bracket, patch or draft | No — claim it only when it is real |
| `.owed` | A visible note that no inversion was found, saying what one would have to look like | Honest outcome, not a deficiency |

The pull will be to call a boundary an inversion, because the alternative feels like an admission.
Book 4 did this in three of its first four chapters. Score the candidate against the chapter's
*central* advice, clause by clause, before claiming a fit — and remember that under this design
there is no longer any reason to reach, because the boundary alone satisfies the rule.

A further trap, specific to this book: **most apparent inversions are altitude errors** — advice that
assumes professional execution and coordinated teammates, rather than advice that genuinely reverses
by bracket. Those belong in the boundary block. Reserve `.inversion` for cases where the same action,
correctly performed, produces opposite results at two stated brackets.

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

Four classes, ordered by distance from the game itself.

| Class | What | Strength |
|---|---|---|
| **1. Official record** | Valve's patch datafeed at `dota2.com/datafeed/patchnotes`, dated and versioned; official rules and announcements | Quotable directly, registered, **gating** |
| **2. Machine-derived match record** | Parsed match JSON from OpenDota — events, logs, per-minute series, `picks_bans`; bracket-stratified public match data | Registered and checkable, but **derived** data, not the replay itself |
| **3. Direct observation** | The replay, or a VOD correctly bound to a match | What a careful viewer can see. Describe it as observation, never as measurement |
| **4. Interpretive** | Caster commentary, named analysis, a player's recollection, bracket consensus | **Never a number.** Proposes; never establishes |

Class 2 deserves its qualifier. OpenDota's JSON is excellent evidence and it is not the game — it is
Valve's replay put through somebody else's parser. Calling it primary would flatten a real
distinction the book can afford to keep.

### Evidence from the reader's own bracket

`api.opendota.com/api/publicMatches?min_rank=40&max_rank=55` returns matches at `avg_rank_tier` 41–55
— Archon 1 through Legend 5. This is structurally important rather than merely convenient: it is the
answer to the altitude error at its source. A claim about what Archon players do gets evidenced with
Archon games, instead of borrowing a professional example and apologising for the difference in a
footnote.

**Any claim about what the reader's bracket typically does must come from class 2 bracket data, not
from a professional match.** A pro case shows the *shape* of a decision. It cannot establish
prevalence, and the book must never let it try.

### The pairing, and its limits

Commentary and record do different jobs:

- **The record cannot tell you why.** It shows that Radiant took top barracks at 34:46 and that the
  game ran to 46:21. It has no theory about the eleven minutes in between.
- **The caster offers one, and is often wrong.** Casters work live with partial information and
  speculate out loud. That is the job, not a defect.

So commentary *proposes* and the record *tests the observable part*. When a caster says *"they've got
no buyback here"*, that is not a quote to reproduce — it is a claim, and `buyback_log` settles it.
Reporting that a caster's reading was wrong is one of the more valuable things this book can do.

**Two hard limits, both learned on review rather than by design.**

First: **no chapter is required to carry commentary.** Requiring it would require a broadcast in every
chapter, and broadcasts are professional Dota. The book would drift, chapter by chapter, into being
about players the reader is not — with the reader surviving only as a qualification. The pairing is
available, not mandatory.

Second: **neither source establishes intention.** `buyback_log` proves a buyback existed. Nothing in
this book proves why a player declined a fight, and the honest vocabulary for that is §3's four-way
split. An earlier draft of §1 said commentary "supplies the why", which overstates what a person
talking over a live game can know about five strangers' reasoning.

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
| `checks/claims.tsv` | Exact string in the official notes for a stated patch | Fetch the datafeed, match the string | **Gating** — Valve's own structured record |
| `checks/matches.tsv` | An event in a registered match | Assert against the committed snapshot | **Gating** — the snapshot is in this repository |
| `checks/data.tsv` | An aggregate query, stamped with the patch it ran under | Re-run, compare within tolerance, diff the snapshot | Advisory — drift is the game changing, which is information |

Gating means *content mismatch fails the build*, and it also means **an unreachable source fails the
build**. Those are different guarantees and conflating them is how a check quietly stops working; see
§8. What a green build proves is that every registered string was found in the record it is attributed
to, by a checker that could actually see that record.

### Licensing, and what may be redistributed

The book is published; most of its sources are not the book's to republish. The pattern that stays
defensible is **cite a computed figure and a re-fetchable address**, never ship someone else's corpus.

- **Valve** owns the game data and the patch text. Short quoted balance lines with a link are ordinary
  practice; reprinting whole patch notes is not. Never imply Valve endorsement.
- **OpenDota** publishes MIT code, not a licence to redistribute bulk data. Cite `match_id`s and query
  URLs; do not commit dumps beyond the per-case snapshots in `data/matches/`.
- **Liquipedia** is CC BY-SA. Reusing substantial text pulls the share-alike obligation into this
  repository, so use it for orientation and cite primary sources instead.
- **Broadcast commentary** belongs to the organiser and the talent. Short attributed excerpts with a
  link to the VOD; never a transcript in the repository, already enforced in `.gitignore`.
- **Public-bracket players are not public figures.** Anonymise everyone in a non-professional match by
  default — no persona names, no account IDs in the prose. They are evidence, and they did not
  volunteer to be examples.

Note what this proves and what it does not. It proves every registered figure is really in the record
it is attributed to. It cannot tell you whether the case supports the lesson drawn from it — book 4
shipped a chapter whose every claim passed while its central causal arrow pointed backwards. **A green
build means the numbers are real. It does not mean the advice is.**

## 6. Chapter register

Legend: ☐ not started · ◐ drafted · ☑ written and sourced

### Part I — Can you distinguish free deaths from necessary risk?
| # | Title | Status |
|---|---|---|
| 01 | The Death You Didn't Notice | ☐ |
| 02 | What the Map Already Said | ☐ |
| 03 | The Thirty Seconds Before | ☐ |
| 04 | Leaving Is a Skill | ☐ |
| 05 | The Death You Should Have Taken | ☐ closes Part I · **the anti-passivity chapter** |

**The working definition of a free death, and the reason Part I is five chapters.** A death is *free*
when no objective, no map information and no economic trade was gained by it. That definition is what
separates this part from the KDA doctrine the genre correctly rejects — the target is avoidable
deaths, not zero deaths, and never an attractive scoreboard.

There appear to be **two different stuck players**, and a book that addresses only one will actively
harm the other:

| | dies too much | dies too little |
|---|---|---|
| Pattern | TPs into lost fights, farms past vision with the map dark | Farms safe camps while the towers fall, declines winnable fights |
| Loses by | Feeding tempo and gold | Starvation, with a respectable scoreboard |
| Needs | Part I as written | **Chapter 05**, which is why it cannot be cut |

Ch. 05 is the insurance against the misreading, not a coda. It is the chapter that stops Part I from
teaching the second player to keep doing what is already losing them games. Proposed for merging on
review; kept for this reason. **The two-population split is a hypothesis borrowed from a review pass
that cited no usable data; the thresholds that would make it operational are owed to §5 bracket
evidence and must not be invented.**

### Part II — Can you get gold and XP?
| # | Title | Status |
|---|---|---|
| 06 | Two Resources, and You Count One | ☐ |
| 07 | The Lane Is Not the Game | ☐ · must carry wave state, and the decision to stay or leave |
| 08 | The Map Is Full of Money | ☐ |
| 09 | Farming a Map You Don't Control | ☐ · must carry the wave–camp–wave loop and safe map ownership |
| 10 | Efficient Is Not Fast | ☐ closes Part II |

### Part III — Can you turn resources into capability?
| # | Title | Status |
|---|---|---|
| 11 | Gold in the Bank Is Not Gold | ☐ |
| 12 | The Item You Want and the Item That Wins | ☐ |
| 13 | Buying for Them | ☐ · neutral items and Madstone belong here, as dated examples |
| 14 | Reading the Scoreboard | ☐ |
| 15 | Enough Farm | ☐ closes Part III |

### Part IV — Do you act while it matters?
| # | Title | Status |
|---|---|---|
| 16 | The Spike | ☐ |
| 17 | Cooldowns Are the Real Clock | ☐ |
| 18 | Vision Is a Timing | ☐ |
| 19 | No Fight Without a Reason | ☐ |
| 20 | The Fight You Declined | ☐ closes Part IV |

**No teamfight-execution chapter, by decision.** Review asked for one — position, focus, spell order,
who to hit first. It is not here because those are hero- and role-specific in a way the general spine
cannot carry without turning into a hero guide. Revisit only if drafting ch. 19 surfaces a clean
decision principle that survives being stated without naming a hero. If it does, that is the argument
for a thirty-third chapter, and it should be made then rather than assumed now.

### Part V — Can you convert advantage into a win?
| # | Title | Status |
|---|---|---|
| 21 | The Lead That Melts | ☐ · earmarked: match 8929124210 · **pilot chapter** |
| 22 | High Ground Is a Different Game | ☐ · buyback belongs here, as part of high-ground state |
| 23 | The Objective Window | ☐ · Roshan and Tormentor are dated examples, not the subject |
| 24 | Ending | ☐ closes Part V |

Ch. 23 was *Roshan and the Two-Minute Window* and was renamed before drafting. 7.41 moved Tormentor's
spawn preference, its terrain and its relationship to the Lotus Pools — all registered in
`checks/claims.tsv` — which is precisely the demonstration that a chapter built on current geography
would have needed rewriting within one patch of publication. The window is the concept; the pit is an
example, and examples get patch-stamped.

### Part VI — Can you keep the framework current?
| # | Title | Status |
|---|---|---|
| 25 | Reading a Patch | ☐ · worked examples: facets removed, the neutral-item system |
| 26 | Five Heroes Is a Strategy | ☐ |
| 27 | Six Games a Week | ☐ |

Ch. 27 was *The Queue Is Part of the Game*. One review pass wanted it demoted out of the spine as
lifestyle content; the opposite is correct. For a reader with three to six games a week, practice
design **is** the subject — an improvement method that assumes forty games a week is not merely
unhelpful to them, it is the reason the existing genre does not fit. This chapter carries the
book's audience wedge, and it is where hero-pool stability belongs: as a practice constraint that
reduces noise while learning, never as a theory of how MMR is won.

### Part VII — The five seats
| # | Title | Status |
|---|---|---|
| 28 | Position One | ☐ |
| 29 | Position Two | ☐ |
| 30 | Position Three | ☐ |
| 31 | Position Four | ☐ |
| 32 | Position Five | ☐ |

**Part VII chapters are full chapters, not appendices.** Each carries the complete template — its own
situation, its own replay-verifiable case, its own figures, its own `Next game` and `After the game`
blocks — *and* does the seat-specific job on top: **name the earlier chapters that invert for this
seat, and say why.**

Both halves are required, and the second is what justifies the first. A chapter that restates general
advice in role-flavoured language has failed. So has one that lists inversions without giving the
reader a case and a set of actions of their own.

Part VII also opens on the question nothing earlier asks: **are you actually playing the seat you
queued for?** A reader who selects support and then farms like a core is not failing at any chapter
in Parts I–VI; they are answering a question they never noticed was asked.

Note the tension recorded in §1, which Part VII exists to hold rather than resolve: the general
chapters are what make the seat chapters legible, and the seat chapters are what make several
general prescriptions true. Neither part is subordinate.

## 7. Match ledger

Five fields per match, written **when the match is first used**, consulted before it is reused. Ported
from book 4 §6b, including the correction that cost that book a chapter: a case is spent when it has
carried **the same inference**, not when it has merely appeared. Before declaring a match spent, name
the inference the earlier chapter drew. A different question asked of the same match is continuity.

Fields: **Facts** (registered figures) · **Permitted** (what it may be used to show) · **Confounders**
(what else was happening) · **Prohibited** (the claim it must never carry) · **Spent** (what each
chapter took) · **Patch** (the version it was played under) · **Source mode** (pro broadcast, or
target-bracket public match) · **Observation vs inference** (which parts are in the record and which
are read into it) · **Transfer** (what carries to the reader, and what does not) · **Identity** (how
the players are named).

The last four are new to this book and each answers a specific way it could go wrong. *Patch*, because
a case played under different rules teaches a game the reader is not playing. *Source mode*, because
the register must make visible at a glance how much of the book rests on professional matches — if
that column reads "pro broadcast" thirty times, the drift §5 warns about has happened and nobody
noticed. *Observation vs inference*, because the difference is invisible in finished prose. *Identity*,
because public-bracket matches involve people who did not volunteer to appear in a book: name
professionals playing in broadcast tournaments, and anonymise everyone else by default.

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

**Day one — the patch pages prove nothing, and the fix was better than the plan.** The design assumed
patch claims would be advisory, checked by hashing `dota2.com/patches/{version}`. Those pages are a
JavaScript shell: 7.41e, 7.41 and 7.40b each return an identical 46,711-byte document, so the check
would have passed forever regardless of what the notes said. Probing found
`dota2.com/datafeed/patchnotes`, which returns structured, versioned, timestamped JSON. **The lesson
is not "Valve has an API". It is that a check nobody has tried to fool is not a check** — the shell
was found by fetching two different patches and comparing sizes, which took one command and should be
the first thing done to any new source.

**Day one — a reviewer stated a fact about the world, confidently, and was wrong.** The resource
survey reported "No official JSON/XML patch-note API." The datafeed above had been returning 200 for
the entire conversation. The same reviewer, in the same pass, was *correct* that facets were removed
in 7.41 — a claim the datafeed confirms verbatim. One pass, one true and one false assertion, neither
distinguishable by tone. This is the entire argument for §9's rule that no reviewer's factual claim
enters the book directly.

**Day one — the checker was fail-open, and the commit message oversold it.** `checks/patchnotes.py`
printed `SKIP` and returned 0 when a source was unreachable, so a DNS failure produced a green build
carrying the same output as a verified one. It was described as "gating" in its own commit message.
Caught by meta-review reading the code rather than the claim. Now an unreachable source is a distinct,
visible, non-zero outcome. **A check that cannot see its source must never report success** — which is
the same failure as a guide asserting a number it has not looked up, in a different medium.

**Day one — statistics with no query behind them.** A research pass returned precise-looking win rates
by death count, citing three site homepages and no endpoint, query or sample. The *concepts* it
supplied were good and are used: the definition of a free death, and the two stuck sub-populations in
§6. The *numbers* are not in this book and will not be until they come from a registered query. Plausible
figures with a citation that cannot be followed are the exact contamination §5 exists to stop, and they
arrive most easily from a source that is trying to be helpful.

**Day one — the orchestrator's own sampling error.** The gold advantage for match 8929124210 was first
reported as peaking at +16,032 at minute 35, by reading the per-minute series at five-minute intervals.
Generated from the full series, the peak is **+19,106 at minute 37**. The error made the case weaker
than the truth, which is the direction that does not get caught by disbelief. **Compute from the whole
series; never eyeball a sample and call it a maximum.**

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

Reviewers that fail differently, which is the entire point. A model reviewing its own prose agrees
with itself.

Roles are defined by **what the pass does**, not by which model is reputedly better at what. The first
version of this table said one reviewer had "the most current game discourse", which is not a property
anyone can check and which turned out to be false in the same session — that reviewer produced both
the confirmed facets claim and the invented patch-API claim.

| Pass | What it does | Invocation |
|---|---|---|
| Web-grounded research | Finds sources, tournaments, licensing, current-game facts. Everything it returns is a lead, never a citation | `grok --prompt-file P --deny Write --deny Edit --deny Bash` |
| High-volume mechanical | Claim extraction, prose scans, checking a draft against the rules in this file. Cheap enough to run per chapter, repeatedly | `agy --model gemini-3.6-flash-high -p "…"` |
| Meta-review | Consolidates the other passes, judges where they overcorrect, reads the code rather than the claims about it | `codex exec --sandbox read-only -` |
| The author, on deployed pages | Whether it reads. Manual, and last | Browser |

**`agy` flag order is load-bearing.** `-p` takes the prompt as its argument, so options must precede
it: `agy --model X -p "prompt"`. Written the other way round, `agy -p --model X "prompt"` silently
passes the literal string `--model` as the prompt, and the model dutifully answers a question about
command-line flags. This happened twice before it was noticed, because the output was fluent.

Two standing rules:

> **No reviewer's factual claim enters the book directly.** Current-game, API, licensing, tournament
> and prevalence claims go back to the relevant primary source, or stay explicitly marked unverified.

> **A target-bracket evidence pass runs before a chapter is drafted.** A professional match may
> illustrate a principle. It may never establish that the principle describes what Archon–Legend
> players actually do — that requires §5 class-2 bracket data.

Reviews run in parallel against a drafted chapter, each given the chapter and this file. Findings are
triaged by the author; nothing is applied automatically. Book 4's record is the argument for keeping a
human at the end: every one of its worst errors passed the mechanical checks.
