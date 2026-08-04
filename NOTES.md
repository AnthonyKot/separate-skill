# NOTES — the working notebook

Unsettled things. Chapter ideas, candidate cases, leads to chase, questions with no answer yet, and
the backlog of revisions owed.

**How this differs from `CONTEXT.md`.** That file is the decision record: what has been settled and
should not be relitigated without a reason. This file is everything before that. An idea lives here
while it is still an idea; when it becomes a rule it moves to `CONTEXT.md` and is deleted from here.
Nothing in this file is binding, and nothing in it has been checked — figures that appear here are
**not registered claims** and must not reach a chapter without going through `checks/`.

**Rule for this file:** a note that has been here a long time is either a decision nobody has made or
an idea that turned out not to be one. Both are worth noticing. Date entries.

---

## 1. Revision backlog — chapter 21

From external review, 2026-08-04. **All of it is now done** — the five factual errors, and the four
structural items below. Kept rather than deleted because the reasoning is worth having when the same
questions come up in the next chapter; the headings say what changed.

### 1a. Not decision-forcing — DONE, and it changed the template

The chapter reveals the whole sequence and then interprets it. The reader can agree or disagree but
never has to *choose*. The proposed fix is to stop the narrative at **40:22**, immediately after both
tier-four towers fall, and give the reader the state they would need:

- who is alive, and whose ultimates are up;
- which buybacks have been used and which have returned;
- where the waves are, whether Roshan is alive, who holds aegis;
- what the reader's own hero can do right now.

Then ask for four commitments *before* revealing what happened: the intended objective, the acceptable
cost, the condition that would make them disengage, and the missing information that matters most.

**It did change the template.** `CONTEXT.md §3` now requires **the hold** in every chapter, with two
rules that keep it honest: the state given must contain no hindsight, and the reveal must say that a
right answer can still lose. Ch. 21 holds at 39:39 — mega creeps up, a fight just won three-for-two,
aegis denied so nobody holds it, gold +12,380 against an experience lead of **+989**. The other three
pilots are written with it from the start.

### 1b. Outcome-biased pass mark — DONE

Current: *you were alive at the end of the attempt; dying inside their base is a fail.* That grades
survival, not decision quality — and it is the same error the free-death definition was corrected for
one commit earlier, reappearing in the review loop where nobody was looking for it. A support dying
to force two buybacks may be correct.

Replacement shape: name the objective and the maximum acceptable cost **before** the attempt; pass if
the attempt achieved the objective within that cost, or if you disengaged when your stated stopping
condition occurred.

> Objective: force the final two buybacks. Acceptable cost: one support death, no core deaths.
> Stop if: the first core drops below half health before any defender dies.

Now in `CONTEXT.md §3` as a rule with the ban stated: *a pass mark of the form "you survived" is
forbidden.* Ch. 21's block now grades the commitment and says explicitly that dying is not
automatically a fail and surviving is not automatically a pass. **Check every future chapter against
this**; the bias is attractive because survival is easy to score and decision quality is not.

### 1c. Three `Next game` rules overreached — DONE

- *"Count their buybacks"* — a reader can track buybacks they have **seen**, not who currently holds
  the gold. Reword to observed buybacks plus whether the cooldown has returned.
- *"Take a lane and a Roshan before the third attempt"* — invents thresholds the case does not
  support (three minutes, two attempts) and requires four teammates. Reword to: after two failed
  attempts, stop repeating the same entry and name the next enabling condition **you** can create.
- *"The same doorway"* — the parsed record proves the deaths, not the entry route. Either add a
  replay observation documenting it or drop the spatial claim. This is a class-2/class-3 confusion of
  exactly the kind `CONTEXT.md §5` exists to prevent, and it got past me.

### 1d. Ch. 21 consumed 22–24 — DONE

The most structural finding. Ch. 21 explains high-ground defensive advantage, buyback as a defensive
mechanism, when to delay for Roshan, and how to make the final attempt — which are the jobs of 22, 23
and 24. The register already assigns buyback to 22, and 21 uses it as a central explanatory device.

Settled and moved into `CONTEXT.md §6`:

| Chapter | Exclusive job |
|---|---|
| 21 | **Detect** that accumulated advantage has stopped producing progress |
| 22 | Why base defence changes the exchange rate — including buyback |
| 23 | Decide when conditions permit an attempt |
| 24 | Execute and sequence the final conversion |

Ch. 21 now ends on the diagnostic — *is my lead still growing, or has it stopped converting?* — and
hands the mechanisms forward by name: high ground and buyback to 22, whether conditions permit an
attempt to 23, sequencing the ending to 24.

---

## 1e. Do not reuse chapter 01's reveal — standing note for pilots 12 and 32

Ch. 01's hold works *once*. Now that the reader has been taught that insufficient evidence is a
legitimate answer, later holds may use the principle but must not repeat the theatrical reveal — the
second time it lands as a mannerism, and the third as a reason to stop trusting the holds.

Later holds should conceal the outcome and the interpretation, never a premise. The recurring skill
is deciding **what can be concluded, what stays uncertain, and what further information is needed**;
ch. 12 and ch. 32 should each find a different shape for asking it. The rule is now in
`CONTEXT.md §3`; this note is the reminder of *why*, which the rule does not carry.

---

## 2. Cases wanted

Leads to chase. Nothing here is sourced yet.

- **Ch. 21's owed inversion.** A match with the same shape — barracks taken, lead peaked, repeated
  failed attempts — that **ends the other way**. Without it the chapter shows that conversion stalls
  but cannot price the stall. Likely findable: professional matches are parsed, and a comeback from
  mega creeps is a memorable enough event to search for by name and then verify by match ID.
- **A target-bracket case for any chapter.** Every registered match so far is professional. The
  moment `data/brackets/` has a clean sample, look for an Archon–Legend match that shows the same
  shape, so at least one chapter is anchored in the reader's own bracket. Consent and anonymity apply
  — see `checks/privacy.py`.
- **Ch. 25 has its case already** and does not need one: 7.41 deleting facets is registered and
  dated, and is a better worked example than any match.

---

## 3. Open questions

- ~~The thesis cannot be tested by the evidence the book collects.~~ **Settled 2026-08-04, now in
  `CONTEXT.md §1`.** The promise that the diagnosis stays hypothetical until target-bracket evidence
  supports it specified a test that could never run. The **prevalence** claim is dropped — the book
  does not need it, because the reader self-selects — and the Thesis row is now a **conditional**.
  **Efficacy** remains untested and is declared as untested; the instrument is three to five readers
  running an `After the game` loop, not a cohort, because the cohort was specified to establish the
  claim that has been dropped.
- **Chapter length.** No ceiling has been set. Ch. 21 is 2,386 words with the hold, up from ~1,850
  without it — so the hold costs roughly 500 words, and a ceiling set now should account for it.
  Book 4 used 2,000–3,000 and found the ceiling useful. Worth setting before four chapters exist and
  fix the norm by accident.
- ~~Is one hold per chapter right?~~ **Settled 2026-08-04, now `CONTEXT.md §3`.** One by default; a
  second only when it tests re-evaluation after the state materially changes, and only if it brings
  new information, a changed resource state or a recovery decision. Ch. 12 drafts second and is the
  test case, because item decisions chain naturally — *what do I buy*, then *do I act on it or keep
  farming*.

---

## 4. Known gaps in the machinery

- ~~The bracket sampler's seek overshoots.~~ **Closed 2026-08-04.** Replaced with bisection, which
  converges from both sides and cannot run past the target; the extrapolation could not be fixed by
  tuning because the match-ID rate is not constant (17–27 ids/second at different distances). First
  clean sample: 240 ranked Archon–Legend matches across six windows, span 96.1 hours, zero out of
  band, every match played after 7.41e shipped. `checks/data.py` now enforces that last property —
  a sample containing matches older than the patch it is labelled with fails the build.
- ~~Nothing checks prose against the registry.~~ **Closed 2026-08-04.** `checks/coverage.py` extracts
  every number from a chapter's HTML and reports any that matches no registered claim. Advisory, and
  the only advisory check here, because prose legitimately contains years and derived figures — but
  exceptions must be declared with a reason in `checks/coverage-allow.tsv`, since an exception nobody
  justified is how a check stops working. It found a genuine miss on its first run: +4,934 sat in the
  reveal unregistered.
- **No local ASR fallback** (`ffmpeg`, `whisper` absent), so a VOD without captions is unusable.

---

## 5. Rejected, with reasons

Kept so they are not re-proposed.

- **A teamfight-execution chapter.** Position, focus and spell order are too hero-specific for the
  general spine. Revisit only if drafting ch. 19 surfaces a decision principle that survives being
  stated without naming a hero.
- **A facets chapter.** Facets were removed in 7.41, 2026-03-24. Registered.
- **Compressing Part I to three chapters.** Ch. 05 is the only chapter addressing the player who dies
  too little; cutting it would leave Part I teaching passivity to exactly the reader it would harm.
- **Demoting ch. 27 to an appendix.** For a reader with six games a week, practice design is the
  subject rather than lifestyle advice around it.

---

## 5b. Part VII's premise was wrong, and pilot 32 is why

**Settled 2026-08-04, now in `CONTEXT.md` §1 and §6.** Part VII was specified to find where general
advice *inverts* for a seat. Ch. 32 tested three chapters against position five and found no
inversions at all: ch. 01's free-death test is right for every seat and only its prior changes; a
ward is not the opposite of ch. 12's forecast but its most visible instance, with the window printed
on it; ch. 21's conversion is redistributed rather than reversed.

The replacement question — **how does this seat change what is scarce, what is visible, and which
presumption you start from?** — is truer and more interesting than hunting reversals.

**Why this matters beyond Part VII:** had the original contract stood, chapters 28–31 would each
have had to produce an inversion, and four chapters obliged to find something that does not exist
would have manufactured it. That is book 4's counter-case failure exactly, and this time a pilot
caught it instead of a reviewer at chapter four. **The pilots paid for themselves here.**

---

## 6. Chapter 12 — the plan

*The Item You Want and the Item That Wins.* Part III, contract: **buying for your own required
function**. Third pilot to be drafted, and the designated test of whether a chapter ever needs two
holds (`CONTEXT.md §3`).

### Why this chapter is the risky one

Ch. 21 tested whether professional evidence transfers. Ch. 01 tested whether the method avoids
hindsight. Ch. 12 tests something harder: **whether a general principle survives contact with
specifics.** Item decisions are where a decision book is most likely to collapse into a build guide —
and a build guide is stale within two patches, which is the failure `CONTEXT.md §6` already flags for
this part.

The chapter must therefore be about a **procedure for choosing**, with the items as dated examples.
Test to apply to every draft sentence: *would this still be true if every item in it were renamed?*
If not, it is a build guide sentence and it goes.

### The evidence available

Better than either pilot had. `purchase_log` gives every item every player bought, to the second, so
the record supports:

- exact completion timings for any item;
- what happened in the minutes after a completion — fights, objectives, gold and XP curves;
- what the *opponents* had bought by that moment.

What it still cannot establish, and the chapter must say so: why anything was bought, what was
expected, or whether an alternative would have been better. There is no counterfactual in a replay.

### The hold, and the two-hold experiment

The natural chain is exactly the one that motivated the question:

1. **Hold one** — you have the gold. Which function do you buy? *Commit: the function, not the item;
   the cost you will accept; the condition that would change your mind.*
2. **Hold two** — the item is finished. *Now* do you act on it or keep farming?

Two holds are permitted only if the second tests a genuinely different operation and introduces new
information, a changed resource state, or a recovery decision. Here it plausibly does: between the
two, the state has materially changed — the item exists, and so does a window that expires.

**Result, 2026-08-04: one hold.** The second was designed and cut, and not for the anticipated
reason. *The item is finished and there is still no fight — act or keep farming?* is a good question
owned by **ch. 15** (the capability is reached, stop farming) and **ch. 16** (acting on a spike). The
second hold did not make the chapter a quiz; it made it two chapters. Now in `CONTEXT.md §3`, with
the general test: **if the second decision belongs to another chapter's exclusive job, it is a
boundary violation with a timestamp on it.**

### Case

**Do not reuse 8929124210.** Its ledger reserves later returns for chapters 22–24, and a third use of
one match starts making the book look like a study of a single game. Fetch a new parsed professional
match and write its ledger *before* drafting — the policy ch. 21 broke and ch. 01 kept.

Selection criterion: a game containing a clearly datable expensive-item completion followed by an
identifiable window — a fight, an objective, or a conspicuous absence of both. The absence is the
more interesting case, because ch. 12's real subject is the item that was bought and then not used.

### The inversion, which this chapter can probably earn

Ch. 21 and ch. 01 both owe an inversion. Ch. 12 has a strong candidate already identified in the genre
survey: **copying professional item builds is advice that inverts by bracket**, because a professional
build assumes stacking, space and draft coordination that a solo-queue game does not supply. If a
bracket sample can show a divergence in what wins at Archon–Legend versus what professionals buy,
that is a real `.inversion` rather than a boundary — the first in the book.

Depends on `checks/data.tsv` having claims, which depends on the sampler.

### Risks, in order

1. Becoming a build guide. Mitigated by the rename test above.
2. Patch decay — item specifics move most. Every item figure gets a patch stamp, and the principle
   must not depend on the current cost of anything.
3. Two holds turning the chapter into a quiz. Decide honestly after drafting.
4. Altitude error, worse here than elsewhere, because item builds are the single most-copied thing
   professionals produce.

---

## 7. The handover plan

Written 2026-08-04, at the end of the session that built the machinery and the four pilots. For
whoever picks this up — including a later version of the same session with no memory of it.

**Read first:** `CONTEXT.md` for every settled decision, `CONTEXT.md §10` for how a chapter gets
made, this file for what is not settled. The repository is authoritative; anything outside it
(including agent memory) is a summary and drifts.

### 7a. Two open decisions, with proposals

Neither is settled. Both are the author's call, and both are recorded here rather than in
`CONTEXT.md` for that reason.

**Decision one — SETTLED 2026-08-04, applied in `CONTEXT.md §1`.** The prevalence claim is dropped
and the Thesis row is conditional; efficacy is declared untested. The analysis that produced it is
kept below because the reasoning is the useful part.

**What the thesis claims.** `§1` promises the reader diagnosis stays a hypothesis
"until target-bracket evidence supports it", and `§5` defines that as OpenDota bracket samples.
Those records cannot show age, employment, games per week, or whether someone understood the game
while losing, so the promise cannot be kept. Three different claims are tangled in it:

| Claim | What it needs | Status |
|---|---|---|
| **Prevalence** — this is what keeps such players stuck | Population evidence | Unavailable, and not obviously available to anyone |
| **Fit** — if this describes you, here is a method | A recognisable description | Already written, in §1's in/out test |
| **Efficacy** — applying the method helps | A few readers | Cheap, and untested |

*Proposed:* drop the prevalence claim, which the book does not need — the reader self-selects by
recognising themselves — and rewrite the Thesis row as a **conditional**. Then test efficacy with
three to five readers running one chapter's `After the game` loop on their own replays for a
fortnight, reporting whether they could execute it. Not the 8–12 consented cohort: that instrument
was specified to establish prevalence, which is the claim being dropped.

*Also legitimate and free:* the author is in the target group. Running the loops on his own replays
is real evidence about executability, provided it is declared as author self-testing and never as
data about anyone else.

*How it was settled:* the Thesis row became conditional and now states that efficacy is untested.
What remains optional, and is not blocking: running the three-to-five-reader efficacy test at all.

**Decision two — how many seat chapters.** Part VII was specified as five full chapters when its
premise was inversion. The premise is now reweighting (§5b), so the sizing is genuinely reopened.

*Proposed:* settle it the way the premise was settled — with one more pilot rather than an argument.
**Draft ch. 30, Position Three**, which is the maximal test: the offlane shares position five's
invisible-product problem while having a core's resource profile.

- Distinct from ch. 32 → the seat axis is real; keep five chapters.
- Overlapping ch. 32 → the real axis is *visible versus invisible product*, not seat; Part VII
  collapses to about three chapters (cores, offlane, supports), or one chapter with a per-seat table.

Either outcome settles four chapters' worth of structure for the price of one.

### 7b. Suggested order of work

1. **Ch. 30, Position Three** — settles Part VII's size before anything is written on the assumption
   of five. **The brief is §8, and its criteria are pre-registered.**
2. **Ch. 02, 03, 04, 05** — completes Part I. This tests something no pilot did: **whether a whole
   part hangs together**, and whether four chapters with adjacent contracts stay distinct in practice
   rather than only on paper. Part I is also the most-read part of any book, and ch. 01 already exists
   to open it.
3. **Ch. 27 as a contract only** — the last untested template question, whether a season-level
   chapter can work under a template built for moments inside a match. A page, not prose.
4. Everything else, in spine order.

### 7c. Standing risks, in the order they have actually bitten

1. **Outcome-grading creeps back.** It has now appeared in three disguises — the free-death
   definition, ch. 21's pass mark, ch. 12's calibration line — after being banned each time. Expect a
   fourth.
2. **The headline outruns the evidence** (`CONTEXT.md §4`). All four pilots did it.
3. **A decision changes and a summary keeps the old version.** Two checkers now catch this inside the
   repo; nothing catches it outside.
4. **Reviewers are confidently wrong.** One asserted an API did not exist while it was returning 200
   all session. Every factual claim goes back to a primary source.

### 7d. What not to do

- Do not draft the remaining chapters in bulk. Each pilot needed a substantial revision pass after
  publication and each pass improved it; the rate has not fallen.
- Do not register a figure that was typed rather than computed from a record.
- Do not let a chapter explain a mechanism that belongs to a later chapter — check the contract list
  in `CONTEXT.md §6` before drafting, not after.
- Do not reuse ch. 01's reveal (§1e). The principle carries; the theatre does not.

---

## 8. Pilot #2 — the brief

One chapter, written to settle whether Part VII wants five chapters or about three. Everything below
is **pre-registered**: the criteria are fixed now, before the chapter exists, because a test whose
criteria are chosen after the result is the ex-post error this book bans in three other places. If
the criteria turn out to be wrong, change them *and say so in the chapter* — do not quietly re-cut
them to fit what got written.

### 8a. The question

Ch. 32 found that the seat does not *invert* general advice; it changes what is scarce, what is
visible, and which presumption you start from. **Is that variation actually indexed by seat, or by
something else that position five happens to sit at one end of?**

The suspicion worth testing: the real axis may be **whether the seat's product is visible in the
record** — vision, space and pressure are not; farm, items and buildings are. If so, Part VII is
organised around the wrong variable and five chapters is three too many.

### 8b. Why position three (ch. 30)

The maximal test. The offlane is the only seat that shares position five's problem — its product is
space and pressure, which the record cannot see — while holding a **core's** resource profile: its
own gold, its own farm, its own item timings. Every other seat varies both together.

- If ch. 30 comes out like ch. 32, the axis is **visibility of product**, not seat.
- If ch. 30 comes out unlike ch. 32 despite sharing the invisibility, the axis is genuinely **seat**.

Positions one and two are weak tests: both are visible and well-resourced, so a distinct chapter
would prove only that carries differ from supports, which nobody doubted.

### 8c. What ch. 32 established, for comparison

Fixed here so the comparison cannot drift. Position five:

| Axis | Ch. 32's answer |
|---|---|
| What is scarce | Gold that is not really yours, spent on things that expire; your body, risked to deliver information; vision, on a fixed clock |
| What is visible | Almost nothing the seat produces; the scoreboard captures outcomes and omits the work |
| Which presumption | An isolated death is *not* presumed avoidable, because the exchange is routinely unrecorded |

### 8d. The decision rule, fixed in advance

Score ch. 30 against the table above once drafted.

- **KEEP FIVE CHAPTERS** if at least **two of the three axes** differ materially from ch. 32, **and**
  at least **three of five `Next game` actions** have no analogue in ch. 32.
- **COLLAPSE PART VII** otherwise — to cores / offlane / supports, or to a single chapter carrying a
  per-seat table. Under this outcome ch. 30 is rewritten as part of the collapsed structure and ch. 32
  is trimmed to fit beside it.
- **A third outcome is possible and must be reported if it happens:** the axes differ, but they differ
  in the *same direction* as ch. 32 — both seats scarce in invisible product, both presuming an
  unrecorded exchange. That is evidence for the visibility axis and against the seat axis even though
  the chapters read differently, and it is the outcome most likely to be mistaken for success.

### 8e. Constraints on the draft

- **New case, new ledger, ledger first** (`CONTEXT.md §10`). Do not reuse 8928118730 — ch. 32 spent it,
  and comparing two chapters drawn from one match tests nothing.
- The record can see, for an offlane: lane assignment and position, gold and XP curves against the
  enemy safe lane, item timings, deaths, and participation in fights. It **cannot** see space created,
  pressure applied, or attention absorbed — which is the whole difficulty and should be stated in the
  chapter rather than worked around.
- One hold, offering a way to pass (`§3`). Do not reuse ch. 01's reveal (§1e).
- Do not read ch. 32 while drafting. Draft, then compare. A chapter written next to its comparison
  will converge on it, and the convergence is exactly what is being measured.

### 8f. What this pilot does not test

Efficacy, prevalence, or whether any of Part VII is worth reading. It tests one structural question
and should not be asked to carry more — the four-pilot round was valuable because each pilot had a
single question, and the temptation now is to make this one settle everything left over.

### 8g. The kickoff prompt

The first prompt of the next session. Short on purpose: everything it would otherwise explain is in
the repository, checked, and would drift if restated here.

> Work in `~/book6` — *Winning Is a Separate Skill*.
>
> Read `CONTEXT.md` before anything else, especially §10, the runbook. Then read `NOTES.md` §7 (the
> handover plan) and §8 (the brief for this task).
>
> **Task: draft chapter 30, Position Three.** It is pilot #2, and it exists to settle whether Part VII
> wants five chapters or about three. Follow §8e's constraints exactly — in particular, **do not open
> chapter 32 until your draft is finished.** A chapter written beside its comparison converges on it,
> and that convergence is the thing being measured.
>
> When it is drafted, score it against §8d's decision rule and tell me which of the three outcomes it
> is, including the third one. **Do not adjust the criteria to fit what you wrote** — if they turn out
> to be the wrong criteria, say so explicitly rather than re-cutting them.
>
> Then publish it the way §10 says: verify, commit, push, confirm the page is live and CI is green.

**Why it is this short.** A prompt that restates the reader, the spine, the template or the voice
rules is a summary of documents that are already authoritative and mechanically checked — and §4's
audit rule exists because summaries are where decisions go stale. The prompt's only job is to name
the task and the two things a fresh session cannot infer: which brief applies, and that the
comparison must not be read first.

### 8h. The result — reported against the criteria as written

Drafted 2026-08-04. Ch. 32 was not opened until the draft was finished, per §8e.

**The rule returns COLLAPSE PART VII.** The two conditions are conjunctive and only the first is met.

**Axes — 2 of 3 differ materially. Condition met.**

| Axis | Ch. 32 | Ch. 30 | Differs? |
|---|---|---|---|
| What is scarce | Gold that is not really yours, spent on things that expire; your body; vision on a fixed clock | **Not** gold — this seat has a core's claim on it. What is scarce is the window in which the advantage is still yours | **Yes**, and it contradicts ch. 32's first row outright. Both nevertheless turn on something expiring, which is a shared motif |
| What is visible | Almost nothing the seat produces | A direct, checkable measurement early — then nothing, with no marker for the transition | **Yes**, and in the opposite direction for the first quarter of the game. The strongest differentiator |
| Which presumption | An isolated death is not presumed avoidable, because the exchange is unrecorded | A falling rank is not presumed a failure and not presumed fine — it is the expected shape, so it carries no information | **No.** Different mechanism, same instruction: do not read your own bad-looking number as a verdict. This is §8d's third outcome on this axis |

**`Next game` actions — 2 of 5 have no analogue. Condition NOT met; the threshold was 3.**

| # | Ch. 30 action | Analogue in ch. 32? |
|---|---|---|
| 1 | At minute ten read two numbers — your gold and your lane opponent's — and write the gap down | **None.** Ch. 32's list contains no quantitative reading at all |
| 2 | Name what the gap is for, in a sentence without the word *gold* | Yes — ch. 32 #1, "say what it is for, not 'vision'". Same operation, different noun |
| 3 | Set the stopping condition out loud before you go | Yes, and worse: a stopping condition is **required of every hold in the book** (`CONTEXT.md §3`). An action the template mandates universally cannot be evidence that two seats differ |
| 4 | After minute twenty stop reading your net worth rank; read the enemy safe-lane hero's row instead | **None in the list**, though it is the same family as ch. 32 #5 ("do not review this seat from the scoreboard alone"). Counted as distinct because it names a time threshold and a substitute number; the weakest of the two |
| 5 | Write one line describing something you did that appears nowhere in your row | Yes — this is ch. 32's central claim restated as an instruction |

Not fudged: #3 was the deciding item and the strict reading was taken. Ch. 30's #4 and #5 are also close to each other, which is a weakness in the draft rather than in the test.

### 8i. The criteria were partly the wrong criteria, and this is the more useful finding

Reported rather than re-cut, per §8's own instruction.

**§8b's premise about the offlane is false.** The whole design rested on this sentence: *"The offlane
is the only seat that shares position five's problem — its product is space and pressure, which the
record cannot see."* The record does not agree. It holds a direct, continuous, checkable measurement
of the offlane against a single named opponent — the gap that ran +1,741 at minute ten and −8,357 by
minute forty-two. Position three is not an invisible seat. It is a **seat whose visibility expires**,
which is a third category neither §8a nor §8b anticipated.

That damages the test in a specific way worth stating. §8b reasoned: *if ch. 30 comes out unlike
ch. 32 despite sharing the invisibility, the axis is genuinely seat.* The antecedent never held, so
the inference is unavailable in both directions. Ch. 30 differs from ch. 32 **most** on visibility —
which under §8a's own suspicion is evidence for the visibility axis, not the seat axis, even though
the two chapters read nothing alike.

So the honest summary is three sentences:

1. **By the pre-registered rule, Part VII collapses.**
2. The rule's discriminating power was compromised by a factual assumption about the offlane that the
   record contradicts, and that assumption was made in this file before any evidence was consulted.
3. The variable that actually separates these two chapters is **how long the seat stays visible** —
   not seat, and not visibility, but the duration of it.

**What is not being done here.** Ch. 30 is not being rewritten into a collapsed structure and ch. 32
is not being trimmed, because §7a records Part VII's sizing as the author's call and a three-category
result is not the two-category result the rule was built to adjudicate. The pilot's job was to
produce the evidence and the verdict; both are above.

**The obvious next question, if one is wanted:** position one or two, which §8b dismissed as weak
tests on the assumption that visible and well-resourced travel together. Under the duration finding
that dismissal no longer holds — a carry is the seat whose visibility *never* expires, which is now
the interesting contrast rather than the trivial one. That would be a third pilot, and it should be
pre-registered the same way, with the premise checked against the record **before** the criteria are
fixed. That is the process failure this round actually exposed.
