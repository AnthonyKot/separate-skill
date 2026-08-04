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
| Thesis | **Winning is a separate skill from playing** — stated as a **conditional**, not a finding. *If* the reader above describes you, then what is missing is a decision sequence rather than execution, and this is one. The book does not claim this is what keeps Archon–Legend players stuck in general. | Three claims were tangled here and only two are needed. **Prevalence** — that this is the common cause — would need population evidence that nothing available can supply, and the book does not need it, because the reader self-selects by recognising themselves in the row above. **Fit** is that recognition. **Efficacy** is whether the method works when applied, which is testable with a few readers rather than a population and is currently **untested** — say so rather than implying otherwise. An earlier version of this row promised the thesis would stay hypothetical "until target-bracket evidence supports it", specifying a test that could never run: match records contain no age, no employment, no games per week, and no evidence of what a player understood while losing. |
| Evidence | **Four sources, ranked by distance from the game, and no chapter is required to use all of them.** Parsed data establishes registered events. Replay observation supplies visible context. Commentary proposes hypotheses. **Nothing available supplies intention.** | §5. The first version of this row made caster commentary mandatory in every chapter, which would have required a *broadcast* in every chapter — quietly converting a book for Archon–Legend players into a book about professional Dota, with the actual reader appearing only in qualifications. Caught on meta-review. |
| Structure | **General chapters first, role chapters last.** Parts I–VI are decisions all five positions face. Part VII is five full chapters, one per seat, each carrying its own case and its own actions *as well as* the seat's reweighting of the earlier chapters: **same decision standard, different resources, different evidence, different default assumptions.** | A role-specific prescription is diagnostically premature until the general sequence is in place. **The original framing — that seat chapters would find general advice to *invert* — was wrong, and ch. 32 disproved it before four more seat chapters were written.** Tested against chapters 01, 12 and 21, nothing inverted: the decision rules held and what changed was what is scarce, what the record can see, and which presumption to start from. That is a better question and a truer one, and it is what Part VII now asks. |
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
> convert advantage → keep the framework current → reweight by seat**

| Part | Question | What it establishes for the next | Ch. |
|---|---|---|---|
| I | Can you distinguish free deaths from necessary risk? | Whether the player arrived at the situation alive, and whether the deaths were avoidable. | 01–05 |
| II | Can you get gold and XP? | Whether they arrived adequately resourced. | 06–10 |
| III | Can you turn resources into capability? | What their resources now permit them to do. | 11–15 |
| IV | Do you act while it matters? | Whether they act before that permission expires. | 16–20 |
| V | Can you convert advantage into a win? | Whether the action changed the game state that actually wins. | 21–24 |
| VI | Can you keep the framework current? | A season, not a game. | 25–27 |
| VII | Which of this changes for your seat? | What is scarce, what is visible, and which presumption you start from. | 28–32 |

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

Filename: `chapters/NN-slug.html`. Five moves, fixed order, fixed headings.

1. **The situation** — the decision, stated concretely, second person, present tense, from inside a
   real game state. *"It is twenty-four minutes. You have your first big item. Two of them are
   missing and you have no idea where."* No throat-clearing, no history of the game.
2. **What actually happened** — one named, dated, **replay-verifiable** match. Match ID stated. At
   least two hard figures from the record. This is the load-bearing move; if the case is thin the
   chapter is thin. **The narration stops at a stated hold point** and does not resume until the
   reader has committed — see below.
3. **The reasoning** — the transferable principle, *with its boundaries stated in the same breath*.
   This move must keep four things visibly apart, because collapsing them is how a guide starts
   inventing: **observed fact** (it is in the record), **supported inference** (it follows from the
   record), **hypothesis** (it is a reading, and other readings exist), and **unknowable intention**
   (why a human did something, which no source in this book can establish).
4. **Next game** — three to five things to do in your next game. Concrete enough to fail at. No
   "consider", no "try to", no "be aware of". Solo-actionable only, per the standing constraint.
   Every action must be performable with information the reader can actually obtain, and any figure
   it names must be one they can read at the moment the action calls for it — `NEXT_GAME_LIVE` v1,
   §8.

   **One principled exception, and ch. 01 is currently the only chapter that earns it.** A chapter
   whose own finding is that *the decision cannot be judged in the moment* may put review work here,
   because a list of live actions would contradict the chapter that precedes it. Ch. 01 establishes
   that a death cannot be classified while it is happening; telling the reader to classify deaths
   live would be the chapter arguing with itself. The test is narrow and it is not a licence: the
   exception applies only when the chapter has **argued** for the impossibility, not when live
   actions were merely harder to think of. Ch. 02 covers adjacent ground and its list is live
   throughout, which is the evidence that the exception is genuinely rare rather than a loophole.
5. **After the game** — the review loop. A timestamp to open, one observable decision to look at,
   and a pass/fail criterion stated in advance. Three to six games a week is not enough repetition
   to install a habit by volume, so the reader has to get the repetitions from review instead. This
   is what makes the book's audience wedge structural rather than a line in the marketing.

   **The pass mark grades the decision, never the outcome.** It reads: *before the attempt you named
   an objective and a maximum acceptable cost; you pass if the attempt achieved the objective within
   that cost, or if you disengaged when your stated stopping condition occurred.* A pass mark of the
   form *you survived* is forbidden.

   **That mark is necessary and not sufficient, and every chapter must carry the second half.**
   As written above it grades *compliance with a plan the reader wrote themselves*, which is
   self-validating: a plan reading **objective: their tower; cost: three deaths; stop: after three
   deaths** passes every time it is followed. So the review loop splits in two, and the halves must be
   visibly separate on the page:

   | | Question | Why it is not the other one |
   |---|---|---|
   | **Process mark** | Did you name an objective, a maximum cost and a stopping condition *before* acting, and did you honour them? | Catches acting without a plan, which is the common failure |
   | **Calibration review** | Given what was knowable at the time, was that objective worth that cost, and was the stopping condition sensitive enough to fire before the cost was paid? | Catches a plan that was followed faithfully and was not worth following |

   **The calibration review is not hindsight and must not be allowed to become it.** It asks whether
   the plan was reasonable on the information available when it was made — never what happened
   afterwards. That is the same ex-ante standard §6's free-death definition already applies, and the
   omission was an inconsistency in this document rather than a decision: the definition asks whether
   a meaningful exchange was *reasonably available*, which is precisely a calibration question, while
   the pass mark asked only whether the reader followed their own instructions. **Found on external
   review of ch. 30, and it applies retroactively.** Every published chapter is affected and they are
   not affected equally, which the first version of this note got wrong by listing three of four:

   - **Ch. 12, 21 and 32 carry pure process marks** — *could you name the function, the window, the
     cost; did you honour them* — and are owed the calibration half as written above.
   - **Ch. 01 is the exception and needs a different fix.** Its mark asks whether an exchange was
     *available* and whether you took it, which is already the calibration question, because it was
     derived from §6's free-death definition rather than from the template. What it does not ask is
     whether the exchange was worth the risk accepted. It needs a clause, not a second block — and
     the fact that the one chapter built directly on the definition is the one closest to correct is
     the argument for the definition over the template.
   - **Ch. 30 already carries both marks**, being the chapter the split was found in.

   **The result of a review is one of four things, and it is not pass/fail.** A two-valued mark
   collapses the interesting cases back together, which is how the single mark survived four chapters:

   | Outcome | What it means |
   |---|---|
   | **Sound process, sound calibration** | You planned, and the plan was worth following on what you knew |
   | **Sound process, poor calibration** | You did exactly what you said you would, and it was not worth doing. **The most valuable cell in the table**, and the one a single mark cannot see at all |
   | **Poor process** | There was no stated objective, cost or stopping condition, so there is nothing to grade |
   | **Insufficient evidence** | You cannot now reconstruct what was knowable at the time. A real answer, and the same move ch. 01 offers its reader |

   **The outcome is recorded on a separate line and never moves the grade.** Whether it worked belongs
   in the review — a reader who cannot see that a bad decision was rescued will not learn calibration
   — but it is written beside the grade, never inside it. The third row is where this matters most:
   *poor process, and it worked anyway* is the cell most likely to be quietly self-awarded as a pass. Ch. 21 shipped with one — "you were alive at the end of it" —
   which is the free-death error of §6 reappearing in the review loop one commit after it was
   corrected in the definition, because survival is easy to score and decision quality is not. A
   support who dies to force two buybacks may have played the sequence correctly, and a book that
   marks them down has become the passive-KDA doctrine it exists to replace.

Then the **boundary** block, optionally the **inversion**, then **the replay** (match ID, timestamps,
what to watch for).

### The hold — the difference between a case study and a decision

Required in every chapter, inside move 2. The narration of the case stops at a chosen moment, the
reader is given the state, and is asked to **commit before reading on**:

1. **The objective** — what this attempt is meant to buy.
2. **The acceptable cost** — stated as a quantity, not a feeling. *One support death, no cores.*
3. **The stopping condition** — the observable event that means disengage.
4. **The missing information** — what they would most want to know and do not.

Then, and only then, what actually happened.

**Why this is a required move rather than a flourish.** Without it a chapter reveals a sequence and
interprets it, and the reader can agree or disagree but never has to choose. Agreement with a good
interpretation is not the skill being taught; the skill is committing under uncertainty and being
graded on the commitment. Ch. 21 was written without a hold, read well, and taught nothing the reader
had to do — which is what the pilot was for.

Two rules that keep the hold honest:

- **The hold point must precede the outcome, and the state given must contain no hindsight.** List
  what the record establishes at that moment and mark what a player would additionally have seen on
  their own screen. If a fact is only knowable afterwards, it does not belong in the state.
- **The reader's answer may be right and still lose, or wrong and still win.** Say so at the reveal.
  A hold that grades by outcome is the ex-post error again, and this book has now made that error
  twice in two different places.
- **There must always be a way to pass using only the information presented.** A hold may conceal the
  outcome, what the professionals actually did, the author's interpretation, or which variable turns
  out to matter. It may **not** conceal a premise that makes the requested task impossible — unless
  *"this cannot be determined"* is offered as a valid answer in the instruction itself.

  This is the rule that separates a test from a trick, and ch. 01 needed it. Its hold instructed the
  reader to classify three deaths and its reveal announced that classification was impossible. The
  chapter had left a route to the right answer, but the instruction still told a cooperative reader to
  do something that could not be done, and then corrected them for complying. *Unclassifiable* is now
  one of the offered options, with a warning not to choose it merely because the judgement is hard,
  and the reveal credits the reader who took it.

  The general form, which every later hold should reach for: the skill being tested is **what can be
  concluded, what remains uncertain, and what further information is required.** That is a recurring
  epistemic discipline. A reveal that depends on the reader having been misled is a recurring
  authorial trick, and it only works once.

**How many holds — settled.** **One is the default.** A single decision gives the chapter a centre,
keeps the prose continuous, and leaves room for the reconstruction and transfer work that follows it.

A **second hold is permitted only when it tests a genuinely different operation**: the first is the
initial decision, the second a *re-evaluation after the state has materially changed*. To qualify, the
second hold must introduce **new information, a changed resource state, or a recovery decision**. If
it amounts to *do you still agree?*, it is not a second hold and it comes out.

The risks of reaching for two are specific and worth naming, because each is a way the book stops
being a book:

- the chapter becomes a quiz;
- the second decision dilutes the chapter's exclusive job (§6);
- the reader starts trying to **guess what historically happened** rather than deciding — which is
  the failure the "right answers can lose" rule exists to prevent, arriving through the back door;
- the prose fragments, and every case begins to read as a branching simulation.

**Ch. 12 was the test, and it came back: one hold.** The second was designed, drafted in outline and
cut, and the reason is more useful than the verdict. The natural second question — *the item is
finished and there is still no fight; do you act on it or keep farming?* — is not a weak question. It
is a **different chapter's question**: ch. 15 owns recognising that the required capability is reached
and farming must stop, and ch. 16 owns acting on a spike. A second hold did not turn the chapter into
a quiz; it turned it into two chapters.

So the failure mode to watch for is not the one anticipated. **A second hold is usually the moment a
chapter starts doing a neighbour's job**, which the contracts in §6 exist to prevent, and the contract
list is therefore the test to apply: if the second decision belongs to another chapter's exclusive
job, it is not a second hold, it is a boundary violation with a timestamp on it.

One hold stands as the rule. The exception above remains available and has now been tried once
without being needed.

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

  **The ban is on the token, not the sense, and `checks/register.py` enforces it.** *You have just
  admitted* and *it simply was not fighting* both mean **merely** and assert nothing about
  difficulty — and both shipped in ch. 12 anyway, because a rule needing judgement is a rule applied
  when someone remembers. The rewrites were improvements in every case so far. Note what the checker
  deliberately does **not** carry: *int* and *your team*, whose ban is contextual — "your team takes
  a set of barracks" is neutral description — and a token match cannot see context. Those stay prose
  rules for a reader.
- **No hero players.** The point of a case is the decision. Nobody in this book is a genius.
- **Name the failure mode inside the principle**, not in a footnote.

### Which document wins

Established after ch. 30, from evidence rather than taste. When two parts of this repository imply
different things, the **earlier normative source wins**:

> **foundation definition → chapter contract → reusable template → chapter prose**

**Templates are conveniences, not authorities.** The evidence is §3's pass mark: chapters 12, 21 and
32 inherited it from the template and all three ended up grading compliance with a self-written plan,
while **ch. 01, which was built directly from §6's free-death definition, is the one that stayed
closest to correct** — it asks whether an exchange was *reasonably available*, which is the question
the template had dropped. The definition survived four chapters of drift; the template introduced it.

That is not an accident of this one rule. A definition states *what is true*, so a chapter derived
from it has to re-derive the reasoning. A template states *what to write*, so a chapter derived from
it copies a shape and inherits whatever the shape has quietly lost. **A template is a compressed
summary of a definition, and §4's audit rule already says summaries are where decisions go stale.**

Practical consequence: when drafting, read the definition the block comes from, not only the block.
When a rule changes, change the definition first and regenerate the template from it — never the
reverse.

### The audit rule

> **Any structural decision change triggers a repository-wide search for its old terminology and
> every summary that restates it.** Not a manual re-read — a search, for the retired phrases and for
> any label or status value the decision touched.

`checks/retired.py` and `checks/status.py` enforce it, because the rule was needed twice before it
was written and a rule that relies on remembering to search fails the same way the re-read does.

The pattern, stated once so it is recognisable next time: **when a decision changes, the places that
repeat it are exactly the places nobody re-reads, because they are summaries.** The Part VII premise
was removed from the decision record, the register and the chapter, and survived in the spine arrow.
The bracket claim class became gating in the code, the script and the README, and stayed advisory in
the foundations. Both were found by someone else.

On the first run of `checks/retired.py`, **seven surviving occurrences appeared, one of them on the
published home page** — the spine table still telling readers that Part VII finds advice "false until
inverted", a premise the book had already abandoned. That is the whole argument for the rule.

The two checkers do different halves. `retired.py` freezes *vocabulary*: each retired phrase has a
declared count per file, so a historical mention in the decision record is legitimate and a new one
anywhere fails. `status.py` freezes *counts*: how many chapters are written, how many checkers exist,
whether any bracket claim is registered. It exists because the README simultaneously claimed no
chapters were written, three verifiers, and no bracket claims, while four chapters were live, seven
checkers existed and six claims were passing.

### The headline rule

> **No headline sentence may claim more than its chapter's observed / inference / hypothesis /
> unknowable section allows it to retain.**

Every one of the four pilots broke this, in the same shape: the most memorable sentence outran the
evidence, and a later caveat was sent to repair it. Ch. 01 instructed the reader to classify what
could not be classified. Ch. 12 said *they were right* on the page after saying correctness was
unknowable. Ch. 21 implied a stall had cost something in a game its own case says was won. Ch. 32
called vision the seat's *product* and its contribution *usually complete before the fight*, on the
evidence of one professional support.

The mechanism is worth naming because it is not carelessness: **the most quotable form of a true
observation is almost always a stronger claim than the observation.** Compression is where the
overclaim gets in, and the compression is written last, after the careful section, by which point the
care feels done.

The rule is checkable by hand and by a reviewer, and the check is mechanical: take each bolded or
otherwise headline sentence, and confirm that it survives being read next to the *unknowable* list in
the same chapter. If it does not, the sentence is wrong, not the list.

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
| `checks/data.tsv` | An aggregate figure, computed from a committed sample and stamped with the patch it ran under | **Recompute** from the stored rows | **Gating** — the sample is in this repository |
| `checks/data.tsv`, live | The same figure against a fresh sample | Re-query and compare | Advisory — drift is the game changing, which is information |

The bracket row was recorded as "advisory" in the first version of this table and stayed that way
after the checker was redesigned, so the foundations said advisory while `checks/data.py`,
`verify.sh` and `README.md` all said gating. Caught on external review. **Two different operations
were being given one name**: recomputing a registered figure from its own committed sample is a
question about this repository and fails the build; re-querying the live game is a question about
the game and cannot.

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

### Chapter contracts

Each chapter has **one job no other chapter may do**. Written before drafting, because the failure
mode is specific and predictable: adjacent chapters in the same part converge, and Part I in
particular can collapse into four retellings of *look at the map and leave sooner*. A chapter that
cannot state a job distinct from its neighbours should be merged rather than padded — but that test
is only meaningful if the jobs were fixed in advance, rather than discovered afterwards by whoever
notices the repetition.

| # | The exclusive job |
|---|---|
| 01 | **Classify** a death: necessary risk, execution failure, or free risk. Establishes the ex-ante test above |
| 02 | Reconstruct the information that was **available before** the decision |
| 03 | Trace the **action sequence** that removed the escape |
| 04 | Identify the **final exit decision** and what leaving would have cost |
| 05 | Stop the framework teaching passive scoreboard preservation |
| 06 | Distinguish **gold from XP** — two resources, different purchases, one usually ignored |
| 07 | Decide when the lane **stops being the best source** |
| 08 | Identify the income **available** across the map |
| 09 | Determine which of that income is **safe and ownable** given who controls what |
| 10 | **Deadline-adjusted** farming: the fastest route to a required capability may have lower GPM |
| 11 | Unspent resources and **delayed delivery** |
| 12 | A purchase is a **forecast**: which function, in what window, at what cost |
| 13 | Buying **against enemy capabilities** |
| 14 | Reading what **all ten heroes** can currently do |
| 15 | Recognising the capability is **reached**, and that farming must now stop |
| 16 | Your own **level and item** spike |
| 17 | **Cooldowns** — spells, ultimates, buyback, defensive items |
| 18 | The **lifetime** of usable vision |
| 19 | The **state change** a fight is meant to purchase |
| 20 | The **cost of refusing** — declining is also a decision with a price |
| 21 | **Detect** that accumulated advantage has stopped producing progress |
| 22 | Why base defence **changes the exchange rate** — high ground, and buyback |
| 23 | Decide **when conditions permit** an attempt |
| 24 | **Execute and sequence** the final conversion |

**Part V's boundaries were redrawn after ch. 21 was drafted**, because the draft did all four jobs:
it explained high-ground defence, used buyback as a central mechanism, argued for delaying to take
Roshan, and prescribed how to make the final attempt. The register had already assigned buyback to
22. A chapter that explains every mechanism it touches leaves the following three with nothing to do,
and the first draft of a part is where that happens — so 21 now **detects** and hands the mechanisms
forward, naming them in one sentence and pointing at the chapter that owns them.

Two more boundaries worth naming because they are the ones most likely to blur. **10** is not another
farming-pattern chapter; 08 and 09 have already covered where the money is and which of it is yours,
so 10 is about arriving in time to matter. And **19 and 20** must not become the positive and
negative forms of one maxim: 19 diagnoses *purpose*, 20 diagnoses the *cost of refusal*.

Parts VI and VII are not contracted here. Part VI runs on a different engine (below) and Part VII's
jobs are defined by the seat rather than by the topic.

### Part I — Can you distinguish free deaths from necessary risk?
| # | Title | Status |
|---|---|---|
| 01 | The Death You Didn't Notice | ☑ 11 claims · match 8928953683 · **pilot** |
| 02 | What the Map Already Said | ☑ 24 claims · match 8928953683 · reuses ch. 01's case for a different inference |
| 03 | The Thirty Seconds Before | ☐ |
| 04 | Leaving Is a Skill | ☑ 34 claims · match 8927063876 |
| 05 | The Death You Should Have Taken | ☐ closes Part I · **the anti-passivity chapter** |

**The working definition of a free death, and the reason Part I is five chapters.**

> A death is **free** when, given what was reasonably knowable at the time, the player accepted
> substantial death risk without a plausible exchange — in objectives, information, resources, space,
> time, or another player's survival.

The definition is deliberately **ex ante**: it is settled by what was knowable when the risk was
accepted, not by what the risk went on to produce. Two things are then assessed separately, and
keeping them apart is the whole method:

| | Question | Settled by |
|---|---|---|
| **Decision quality** | Was a meaningful exchange reasonably available, and was it taken? | What the player could know at the moment of the decision |
| **Outcome** | Did the exchange actually occur? | What happened afterwards, including what four other people did |

An earlier version defined a free death as one from which no objective, information or trade **was
gained**, which judges the decision by its result. Under that wording a sound sacrifice fails its
grade because a teammate misexecuted, and a reckless one passes because it happened to reveal a
rotation. Corrected on external review before any chapter existed, which is the only cheap time to
correct a definition: **chapter 01 is built on this distinction**, and had it been drafted first, the
book would have spent five chapters teaching hindsight while calling it diagnosis.

This is also what separates Part I from the KDA doctrine the genre correctly rejects. The target is
*avoidable* deaths, not zero deaths, and never an attractive scoreboard. A player who takes no risks
is not passing this test — they are failing it in the direction chapter 05 exists to catch.

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
| 12 | Every Item Is a Forecast | ☑ 17 claims · match 8928916055 · **pilot** · one hold, and why |
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
| 21 | The Lead That Melts | ☑ 41 claims · match 8929124210 · **pilot** · revisions owed, see `NOTES.md` §1 |
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
| 30 | Position Three | ☑ 53 claims · match 8926599506 · **pilot** · see `NOTES.md` §8h–8i |
| 31 | Position Four | ☐ |
| 32 | Position Five | ☑ 23 claims · match 8928118730 · **pilot** · disproved Part VII's premise |

**Part VII chapters are full chapters, not appendices.** Each carries the complete template — its own
situation, its own replay-verifiable case, its own figures, its own `Next game` and `After the game`
blocks — *and* does the seat-specific job on top:

> **How does this seat change what is scarce, what is visible, and which presumption you start from?**

**That question replaced an earlier one — *which earlier chapters invert for this seat* — and the
replacement is ch. 32's most useful finding.** Asked to produce inversions, ch. 32 tested three
chapters and found none: ch. 01's free-death test is right for every seat and only its *prior*
changes; a ward is not the opposite of ch. 12's forecast but an unusually visible instance of it,
with the window printed on it; ch. 21's conversion is not reversed but redistributed. Chasing
inversions for the remaining four seats would have meant manufacturing them, which is the counter-case
failure of book 4 with a different label — and this time it was caught by a pilot rather than by a
reviewer at chapter four.

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

Written after ch. 21 was published rather than before it was drafted, which is a process failure and
is recorded as one: the policy above says the ledger is written when a match is first used, and the
chapter shipped without the field that states what the case may never be made to say. Caught on
external review. The next chapter writes its ledger first.

- **Patch.** 7.41e. **Source mode.** Professional broadcast — identities permitted, per
  `checks/privacy.py`. **Identity.** Players named; they are named on stream.
- **Facts.** All registered in `checks/matches.tsv`, 38 rows, every value generated from the record:
  barracks at 34:46 / 35:17 / 35:28 / 37:20 / 39:39; both tier-four towers 40:09 and 40:22; fort
  46:21; gold advantage peaking at +19,106 at minute 37, which is the series maximum, falling to
  +11,252 by minute 45; experience advantage +4,934 at minute 40 and −2,705 at 41, −3,124 at 42;
  teamfights 5 through 8 with per-side deaths; six buybacks; Roshan at 38:36 with the aegis denied
  at 38:37.
- **Permitted.** That a large structural and economic advantage can coexist with several minutes of
  failed final conversion. That buildings are the cheapest thing an advantage buys. That the reported
  peak of a lead can postdate the trade that began reversing it.
- **Observation vs inference.** Every timestamp is observed. That the side ahead lost more heroes
  than it killed between the last barracks and the fort is computed from the record. That defending
  a base is a strong position is a **hypothesis** the record is consistent with and does not
  establish. Nothing here is intention.
- **Confounders.** The draft; individual hero scaling; deaths taken *while* converting buildings,
  which are not the same as deaths taken for nothing; the aegis denial; buybacks; and professional
  coordination throughout.
- **Prohibited.** Never that stalling **caused** a loss — this team **won**. Never that this pattern
  is common in Archon–Legend; a professional match cannot establish prevalence in any bracket. Never
  that a specific alternative line would have ended the game sooner; the record contains no
  counterfactual. Never that any player intended anything.
- **Transfer.** Replay diagnosis only. The coordinated actions in this match — a one-second aegis
  denial, five players arriving together, buybacks timed to a siege — are not available to a
  solo-queue reader and must never be presented as instructions.
- **Spent.** Ch. 21 took the stock-versus-flow inference: advantage accumulates, closure does not.
  A later chapter may return **only for a different inference** — 22 for why the defender's exchange
  rate improves, 23 for objective windows, 24 for sequencing the ending — and each must draw its own
  conclusion rather than retell this one.

### 8928953683 — Team resilience vs PlayTime, The Games of the Future 2026

Written **before** ch. 01 was drafted, which is the policy and which the previous entry failed.

- **Patch.** 7.41e. **Source mode.** Professional broadcast. **Identity.** Named in the record and
  permitted, but **the chapter names heroes only, never players.** Nothing in ch. 01's argument needs
  a person's name, and the one thing the chapter must not become is a published judgement of a named
  professional's twelve deaths. §4: nobody in this book is a genius, and nobody is an idiot either.
- **Facts.** 49:33, Dire won. 59 hero deaths, of which 30 fall outside every teamfight window
  OpenDota records. Scoreboard extremes: one hero finished 0 kills and 12 deaths, another 18 and 1.
  Per-hero kill and death counts, the kill log with timestamps and victims, and the teamfight windows.
- **Permitted.** That the death *count* on a scoreboard classifies nothing. That roughly half the
  deaths in a professional game happen outside anything the parser recognises as a fight — so
  "deaths" and "deaths in fights" are different quantities, and the scoreboard reports neither
  usefully.
- **Observation vs inference.** Timestamps, victims and killers are observed. The teamfight windows
  are **the parser's**, not the game's: OpenDota decides what counts as a teamfight, and a death at
  the edge of one is a classification artefact rather than a fact. Say so wherever the 30 is used.
- **Confounders.** The parser's teamfight definition, as above. Role: a position-five hero dying
  repeatedly may be buying space each time, and the record cannot distinguish that from carelessness
  — which is the chapter's point rather than a gap in it.
- **Prohibited.** **Never classify an individual death in this match.** For the deaths the chapter
  examines — all outside teamfight windows — the record has no position, no vision state, no
  cooldowns and no intent, so no death here can be called free, necessary or
  misexecuted on this evidence — and a chapter that did so would be inventing the ex-ante information
  its own definition requires. Never that the 0/12 hero played badly; never that the 18/1 hero played
  well. Never a prevalence claim about any bracket.
- **Transfer.** The classification framework and the demonstration that the scoreboard cannot apply
  it. Not any judgement about these players.
- **Spent.** Ch. 01 takes the deaths-outside-fights count and the two scoreboard extremes, to show
  that the count is uninformative. **Ch. 02 returns to the same match for a different inference**, as
  the policy above permits: the reconstructed vision state at 8:15 — which is ch. 01's own death A,
  the death it could not classify. Ch. 03 still needs per-second position this record does not hold.

  **This entry originally said the match "cannot supply reconstruction evidence without replay
  observation", and that was wrong** — written when the ledger also believed the record held no
  vision state. It holds a complete one: every observer and sentry, placed and ended, per side, at
  any instant. The correction is why ch. 02 exists at all, and it is recorded here rather than
  silently replaced because a ledger that quietly revises what a source can supply is a ledger that
  cannot be audited.

- **Ch. 02's additional facts.** At 8:15 Radiant had **3 observers and 3 sentries** standing; Dire had
  **1 and 2**. Dire's single observer had been placed by the victim **26 seconds earlier**, at 7:49,
  and was destroyed at 9:10 after **81 seconds** against the 360 that Radiant's three each ran. Dire
  had **no observer standing at all** between 6:39 and 7:48 — Storm Spirit's, placed at 6:14, lasted
  **24 seconds** — while Radiant placed two more at 7:41 and 7:47.
- **Ch. 02's prohibitions, additional to those above.** **Never that the vision asymmetry caused the
  death** — the record holds no position for this death, it falls outside every fight window, and
  ch. 01's prohibition against classifying it stands unchanged and is the point ch. 02 ends on.
  Never that Dire warded badly: ward *counts* are not ward *value*, the record cannot say what any
  ward saw, and two of Dire's short-lived observers were destroyed rather than wasted, which is
  evidence of contest and not of carelessness. Never that the reader's bracket wards like either team.

### 8928916055 — BoomBoys vs OG, 1win Essence II

Written before ch. 12 was drafted.

- **Patch.** 7.41e. **Source mode.** Professional broadcast. **Identity.** Heroes only in the prose,
  as in ch. 01. The argument is about what an item was for, never about who bought it.
- **Facts.** 41:14, Radiant won. **Four teamfights in the whole match**, and a stretch of **22:59**
  between the end of the second (10:08) and the start of the third (33:07) containing none. Inside
  that stretch: sixteen expensive item completions, **five of them Black King Bars, spanning
  4 minutes 22 seconds** across both teams — 21:05, 21:17, 22:59, 23:42, 25:27 — and seven towers.
- **Permitted.** That an expensive item is bought for a moment, and that the moment can be a long way
  from the purchase. That five players on two teams independently reached the same conclusion about
  what the next fight would require, well before there was a next fight.
- **Observation vs inference.** Purchase times, fight windows and tower times are observed. That the
  five purchases were *for* the fight at 33:07 is **inference**, and a weak one: nothing connects a
  purchase to an intention. The teamfight windows are again the parser's judgement.
- **Confounders.** The gap contained seven towers, so this was not an idle game and the chapter must
  not say it was. Draft and hero scaling determine when spell immunity becomes necessary. Two of the
  five buyers were on the losing side.
- **Prohibited.** **Never that these purchases were mistimed or wasteful.** Nothing in the record
  supports it, professional players buying spell immunity before contesting objectives is ordinary,
  and the chapter's argument does not need them to have been wrong — it needs them to have been
  *deliberate*, which is the opposite claim. Never a counterfactual: no alternative purchase can be
  evaluated from a replay. Never a prevalence claim about any bracket, and specifically **never that
  Archon–Legend players buy differently**, because `publicMatches` carries no item data and this book
  has no bracket evidence about items at all.
- **Transfer.** The question *what moment is this item for* transfers completely. The answer these
  five arrived at does not, because it assumes a team that will produce the moment.
- **Spent.** Ch. 12 takes the five-BKB cluster, the fight gap and the seven buildings, for the
  inference that a purchase and its first observable use can be separated by many minutes. Ch. 16 (*The Spike*) may return for a different inference about timing, and
  must draw its own.

### 8928118730 — Vici Gaming vs Team Liquid, 1win Essence II

Written before ch. 32 was drafted.

- **Patch.** 7.41e. **Source mode.** Professional broadcast. **Identity.** Heroes only.
- **Facts.** 46:36, Radiant won. Crystal Maiden finished **0 kills, 8 deaths, 15 assists** on the
  winning side, with a final net worth of **16,558** against the same team's highest of **40,243**.
  Placed **14 observers and 25 sentries**; the observers whose end is recorded contributed
  **3,964 ward-seconds**. Eleven of twelve tracked observers survived exactly 360 seconds. The
  exception was placed at 35:09 and killed twelve seconds later; Crystal Maiden's eighth and last
  death was at 35:39, and two enemy tier-two towers fell at 37:01 and 37:23.
- **Permitted.** That a scoreboard line can omit almost everything a position-five player did. That
  a support's resources are time-boxed in a way a core's are not — a ward has a fixed duration
  printed on it before you place it.
- **Observation vs inference.** All times, counts and lifetimes are observed. That eleven identical
  360-second lifetimes indicate the ward's full duration is a safe inference from the repetition.
  **That the deep ward at 35:09 or the death at 35:39 contributed to the towers at 37:01 and 37:23
  is neither** — it is a sequence, and the chapter must present it as one.
- **Confounders.** Ward uptime counts overlapping wards separately, so 3,964 seconds is ward-seconds
  contributed rather than seconds of the game covered; say which. A support's death count is
  entangled with the team's whole approach. Two towers falling ninety seconds later has many
  candidate causes and this record ranks none of them.
- **Prohibited.** Never that the deaths were justified *because* the team won — that is outcome
  reasoning, banned in ch. 01 and no more permissible here. Never that the ward bought the towers.
  Never that supports should die more, or less. Never a prevalence claim: this is one support in one
  professional game, and the book has no bracket evidence about warding at all.
- **Transfer.** That the seat changes which resources are scarce, and therefore which of the earlier
  chapters apply unchanged. Not the ward count, the death count, or any tempo from this match.
- **Spent.** Ch. 32 takes the scoreboard line, the ward counts and lifetimes, and the 35:08–35:39
  sequence, for the inference that position five's resources are time-boxed and largely invisible to
  the scoreboard. Chapter 18 (*Vision Is a Timing*) may return for a different inference and must
  draw its own.

### 8926599506 — Team Syntax vs Ilbirs Esports, Asgard Championship

Written before ch. 30 was drafted. Chosen because it contains **both** offlanes, which is what makes
it a case rather than an anecdote: two players in the same seat, in the same game, both ahead of
their lane opponent at minute ten, finishing with rows that order the opposite way to the result.

- **Patch.** 7.41e — played 2026-08-02, three days after the patch shipped. **Source mode.**
  Professional broadcast. **Identity.** Heroes only in the prose, as in ch. 01, 12 and 32. The
  argument is about what a seat's record can show, and needs no one's name to make it.
- **Facts.** 43:14, Radiant won. Radiant's offlane hero held **more gold than anyone else on his own
  team from minute 6 through minute 14**, while his team was **2,161 gold behind overall at minute
  14**. Against the enemy safe-lane carry he was **+1,741 gold and +13 last hits at minute 10**,
  **+393 at 14**, **−66 at 16**, **−1,256 at 20** and **−8,357 at 42**. He finished **fourth of five
  on his own team**: 18,287 net worth, 213 last hits, 7/10/6, 1,227 tower damage. The carry he had
  been ahead of finished on 28,577 and 427 last hits. His own team's carry finished on 32,900 with
  **two deaths in 43 minutes** and 10,690 tower damage — the highest in the game. The opposing
  offlane hero was **+197 gold and +12 last hits** on *his* lane opponent at minute 10 and finished
  with 24,470, 409 last hits and five deaths — the better-looking row, on the losing side.
- **Permitted.** That the offlane's advantage over its lane opponent is recorded, is largest early,
  and reverses sign inside the same game. That an offlane row cannot be ranked against another
  offlane row to establish which player did the seat's job.
- **Observation vs inference.** Every figure is observed, including the team-relative rank, which is
  recomputed rather than read off a scoreboard. That the seat's advantage was *spent* on anything is
  **inference**, and where it went is not in the record at all. That the winning team's carry reached
  500 last hits and two deaths *because* of anything the offlane did is **not** supported and must
  not be written.
- **Confounders.** The draft on both sides; two Roshans, at 26:06 and 37:42; a mid lane that finished
  on 34,500 and thirteen kills, which is a larger difference than anything in the offlane; and
  professional coordination throughout. The parser's lane assignment is itself a judgement — it
  reports a role, and roles in a professional game are fluid after the laning stage.
- **Prohibited.** **Never that either offlaner played well or badly.** Never that the ten deaths were
  justified because the team won — that is the outcome reasoning banned in ch. 01 and in the
  free-death definition, and it is the exact form it would take here. Never that the offlane created
  the space the carry farmed in: the record contains no lane pressure and no counterfactual, and the whole chapter depends on saying so. Never a prevalence claim about
  Archon–Legend offlanes; `publicMatches` carries no per-hero data whatsoever.
- **Transfer.** The reading procedure — which two numbers describe the seat, when they stop
  describing it, and what the row does not report. Not the timings, not the item build, and not the
  death count. A professional offlaner dying ten times has four teammates who can use what that buys;
  the reader has four strangers, and that difference is the chapter's boundary block.
- **Spent.** Ch. 30 takes the rank-over-time series, the sign change against the lane opponent, and
  the two-offlane comparison, for the inference that this seat's product is recorded early and
  against the wrong opponent. Ch. 07 (*The Lane Is Not the Game*) and ch. 11 (*Gold in the Bank Is
  Not Gold*) may return for different inferences and must draw their own.

### 8927063876 — GLYPH vs PlayTime, The Games of the Future 2026

Written before ch. 04 was drafted.

- **Patch.** 7.41e — played 2026-08-03. **Source mode.** Professional broadcast. **Identity.** Heroes
  only, as in ch. 01, 02, 12, 30 and 32.
- **Facts.** 60:38, Radiant won. Teamfight 5 ran **49:49–50:36**, forty-seven seconds, and **seven of
  the ten heroes died in it** — four Radiant, three Dire, at 50:04, 50:06, 50:15, 50:15, 50:21, 50:21
  and 50:36. Inside that fight: **Undying used a town portal scroll and two blinks and died**;
  **Doom used a scroll, a blink and a Shiva's and died**; **Earthshaker used a blink and a force
  staff and died**. Dark Seer used two blinks and a wind waker and lived, gaining 980 gold and 5,868
  experience. **Gyrocopter died in the fight and still finished it +1,769 gold and +5,912
  experience** — the largest gain of anyone on the map.
- **The parser contradicts itself here, and the chapter says so.** The fight's own `deaths` field
  reads **6**; the per-player entries sum to **7**, and the kill log inside the window also gives 7.
  The difference is Earth Spirit, who died at 50:36 — the exact end of the window. Both figures are
  registered. Choosing the convenient one silently is the failure this book exists to avoid.
- **Permitted.** That an exit is an action with a price and a failure rate: it costs an item, a
  cooldown and a position, and in this fight it was paid three times and failed three times. That
  what staying earns is partly recorded — and that the largest earner in this fight is a player who
  died in it.
- **Observation vs inference.** Every time, item use, delta and death is observed. That a scroll or a
  blink was used **in order to leave** is **inference and a weak one** — a scroll can bring a player
  in, a blink is an entry tool at least as often as an exit, and the record carries no destination.
  The chapter must say this where it uses the word *exit*.
- **Confounders.** An aegis was taken at 47:39, three minutes before the fight, and Gyrocopter used a
  cheese inside it — so at least one participant had resources the record prices at nothing. Two
  Radiant barracks had already fallen at 46:56 and 47:06. A Radiant tier-two fell at 51:12, after the
  fight. Professional coordination throughout.
- **Prohibited.** **Never that anyone should have left**, or left earlier — the record contains no
  counterfactual and no position, and the whole chapter is that the price of leaving is unrecorded.
  Never that the three who used movement items used them to escape; see *Observation vs inference*.
  Never that Gyrocopter's death was worth it *because* of the gold — that grades by outcome, which
  ch. 01 bans. Never a prevalence claim about any bracket.
- **Transfer.** The pricing procedure — naming what the exit costs and when it expires, before it is
  needed. Not the items, the timings, or the survival rate. Five coordinated professionals contesting
  a base after mega creeps is not a solo-queue skirmish.
- **Spent.** Ch. 04 takes fight 5's exit-item usage and the gold and experience deltas, for the
  inference that leaving has a price the record cannot state and staying has one it can. Ch. 17
  (*Cooldowns Are the Real Clock*) and ch. 20 (*The Fight You Declined*) may return for different
  inferences and must draw their own.

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

**Ch. 30 — four checkers answered narrower questions than their names, and two of them shipped.**
The pilot produced findings about position three and a separate set about the machinery that approves
chapters, and the second set has a shape the earlier entries here do not. Every failure above was a
**wrong answer**: fail-open, a biased sample, a VOD bound by its title. These four were **right
answers to smaller questions**, under headings that sounded general.

| Checker | What green actually meant | Shipped? |
|---|---|---|
| `retired.py` | No retired *string* appears — not no retired *idea*. A decision restated in new words passes forever | **Yes.** A premise the book had abandoned was live on the home page, twice, across many green builds |
| `status.py` | *Three named numbers* are current — under the heading "stated status vs reality" | **Yes.** Three of five per-chapter claim counts were wrong in the register |
| `matches.py`, `hero_death_time` | Unaffected: it raises rather than passing | No. But it could not see 19 of 127 heroes, so it silently decided **which cases the book was allowed to use** |
| `coverage.py` | Unaffected: the check was correct and said so on every run | No. Two ch. 32 figures were unregistered and both were right |

The third row is the one worth remembering, because it is the only failure here that leaves **no
artifact**. A fail-open check publishes something wrong that can be pointed at afterwards. A checker
with a blind spot produces *absence* — a case not chosen, a chapter not attempted — and absence
cannot be audited later by anyone, including the person who caused it. It was found only because
ch. 30's case happened to need a hero whose internal name is `magnataur`.

The fourth row is not a machinery failure at all. `coverage.py` worked, reported, and was read past on
every run since it was written. **Advisory came to mean optional, and optional came to mean never** —
which is worth stating in the foundations because §5 deliberately keeps one advisory check and this is
the cost of having one.

**Ch. 30 — the book prescribed an exercise the game cannot perform.** Its `Next game` list opened
with *at minute ten, write down your gold and the enemy carry's gold*. No player can do that. The
per-hero series this book registers is `gold_t`, which is **cumulative gold earned** — it tracks
`total_gold` (18,305 against 18,287 for ch. 30's offlaner) and is not the 1,440 he was carrying
unspent, nor the 17,620 of his net worth. It is a replay quantity. Nobody reads it live for an
opponent and nobody reads it live for themselves.

Three separate failures stacked to produce one instruction, and the stack is the lesson:

1. **A quantity was renamed on the way into prose.** `gold_t` became "gold", which sounds spendable.
   Every registered figure was correct and the word attached to them was not, so no checker could
   see it — `matches.py` verifies values against the record and has no opinion about nouns.
2. **Replay evidence was converted into a live instruction** without asking whether the reader has
   the same view the record has. The whole book rests on the reader being able to open the replay;
   that is exactly why the boundary between *what the replay shows* and *what the screen shows* has
   to be policed, and this chapter walked across it.
3. **A claim about the current client was needed and was not available.** Whether any in-client
   feature exposes enemy economy is a §9 question — a reviewer asserted it does not, community
   sources agree, and none of them is a primary source. The chapter does not resolve it, because the
   fix does not depend on it: the quantity the chapter uses is not that quantity either.

**The rule that comes out of it, registered as `NEXT_GAME_LIVE` v1: every action must be performable
with information the reader can actually obtain, and any figure it names must be one they can read at
the moment the action calls for it.** Ch. 30's list is now built from level, items, tower state and
lane safety — a judgement made live and *checked* against the record afterwards, which also makes it
a calibration exercise rather than a data-entry one.

The first draft of that rule said something stronger — *replay work belongs in `After the game`* —
and it was narrowed before being registered, because it would have failed ch. 01, whose `Next game`
is deliberately a review list. Every item there is obtainable; none of it is live. That is a design
choice this document has no evidence against, and a rule written to catch one chapter's defect had
begun condemning another chapter's decision. **`checks/register.py` did exactly this on its first run
by banning words the foundations do not ban.** A rule that enforces more than its case establishes
trains the author to argue with the checker, and an author who argues with the checker stops reading
it.

**Ch. 01 asserted the record holds no positions and no vision state. Both are false, and both were
live on a published page.** The sentence read: *"I checked before writing this... there is no death
log with coordinates, no `x`, no `y`."* The check was real and it looked in one place — `kills_log`,
which indeed carries only a time, a victim and a killer. **`teamfights[].players[].deaths_pos` carries
map coordinates**, and `obs_log` with `obs_left_log` reconstructs exactly how many wards were standing
at any moment. Thirty of that match's fifty-nine deaths have an x and a y; three observers were
standing at 14:24.

Two things make this worth a full entry rather than a correction line.

**First, the shape of the error is the chapter's own argument.** Coordinates exist for deaths inside a
teamfight window and not for deaths outside one — 29 inside against 30 outside, and thirty positions
recorded, the two structures disagreeing by one, which is itself a demonstration that "teamfight" is
the parser's judgement. The record sees the deaths that happened in fights and not the deaths that
happened alone, and the second group is what ch. 01 is about. The corrected chapter is **stronger**
than the overclaim it replaces. That is the usual direction: §4's headline rule exists because the
most quotable form of a true observation is a stronger claim than the observation, and the repair is
almost always more interesting than the thing repaired.

**Second, "I checked" is not a citation.** The claim was written in the confident register this
document reserves for reviewers who assert facts about the world — §8's *a reviewer stated a fact
about the world, confidently, and was wrong* — and it was written here, by the author, about this
repository's own data. The rule that catches it is one the book already has and did not apply to
itself: **an absence claim needs a registered check, exactly like a presence claim.** `deaths_with_position`
and `wards_standing_at` now exist so that "the record does not contain this" is a row that runs on
every build, rather than a memory of having looked.

The audit rule then found the same overclaim restated in **two ledgers and in ch. 30**, which had
inherited the phrasing wholesale. All corrected; *contains no positions* is now retired terminology.

**The absence rule, applied once and then not swept — caught the same day it was written.** Ch. 01's
correction produced the rule that *an absence claim needs a registered check, exactly like a presence
claim*. It was applied to ch. 01 and to nothing else. Three other chapters were making absence claims
about the bracket sample — ch. 12's *no item histories*, ch. 30's *no per-hero data of any kind*,
ch. 32's *no evidence about position five at Archon–Legend at all* — all true, none checked.

They are now. An absence is only checkable as a statement about a **schema**, so the sample's exact
field set is registered as a claim per chapter, plus `row_shapes = 1` proving all 240 rows carry the
same fields. Enrich the sampler and those three sentences go red by name. Negative-controlled by
adding a `hero_ids` field to one row, which failed all four.

The pattern is now sufficiently established to state as a standing expectation rather than an
anecdote: **this repository's characteristic failure is a rule correctly derived, correctly written
down, and applied only to the instance that produced it.** It has happened with the retired premise,
the bracket claim class, the pass mark, and now the absence rule. The countermeasure is not more
resolve; it is that **deriving a rule and sweeping for its other instances are one task, and the task
is not done when the rule is written.**

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

## 10. Drafting a chapter — the runbook

The order below is not a suggestion. Two of these steps exist because skipping them cost something,
and the numbering records which.

1. **Pick the chapter and read its contract** (§6). One exclusive job. If the chapter you want to
   write is doing a neighbour's job, stop and fix the register first.
2. **Find a case.** `curl api.opendota.com/api/proMatches`, then check `version` is non-null —
   `tools/fetch-match.py` refuses unparsed matches rather than committing an empty snapshot. Prefer
   a match no chapter has spent (§7), and read the `Spent` field of any you reuse.
3. **Write the ledger BEFORE drafting** (§7). Ch. 21 shipped without one and the omission was found
   by a reviewer; the `Prohibited` field is the one that shapes the draft, and written afterwards it
   only rationalises it. Ch. 01's ledger forbade classifying any individual death, which changed what
   the chapter could be — that is the field working.
4. **Register the claims from the record, never by hand.** Generate the rows with a script that reads
   the snapshot. If a figure you want has no check type, add one (`checks/matches.py`) — the
   machinery grows to fit the argument, not the reverse. Ch. 32 needed four new types to see wards.
5. **Draft**, five moves, one hold (§3). The hold must offer a way to pass using only what it shows.
6. **Link it** in `docs/index.html` and mark the register row in §6.
7. **`./verify.sh`** — the whole suite; the count is printed rather than stated here, because a
   number typed into a runbook is the thing §4's audit rule is about. Expect `register.py` to catch
   something; it usually does. Expect `status.py` to catch the chapter count, every time.
8. **Commit and push**, then confirm the page is live and CI is green. Pages deploys take about a
   minute, and a 404 immediately after pushing means the deploy is still running, not that anything
   is wrong.

**What to write next, and the two decisions still open, are in `NOTES.md §7` — the handover plan.**

**Then, and separately: review.** Run the panel (§9) or hand it to a human. Every serious defect in
the four pilots was found this way and none by the checkers — the checkers caught figures, reviewers
caught arguments. Budget for the revision; each pilot needed one substantial pass after publication,
and each pass improved the chapter.
