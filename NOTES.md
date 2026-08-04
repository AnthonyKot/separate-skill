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

## 9. Revision backlog — from ch. 30's external review

The review that produced these was the most useful the book has had, and it is worth recording what
kind of finding it was: **none of it was catchable by any checker in this repository**, and three of
the items are foundations-level rather than chapter-level.

### 9a. Applied to ch. 30 already

- **The impossible exercise.** `Next game` #1 told the reader to read the enemy carry's gold. Rebuilt
  around what is visible live; the record is now the *check* on the reader's judgement rather than
  its input. Recorded in `CONTEXT.md §8`, with the rule that came out of it.
- **"The comparison expires" → "a statistic can stay accurate after it has stopped being
  sufficient."** The case establishes that the gap crossed zero. It does **not** establish that the
  comparison stopped mattering — the carry's recovery may matter enormously, and a shrinking gap is
  equally consistent with wasted advantage, conversion elsewhere, farm deliberately redistributed, or
  the economic shape the draft always expected. The new formulation is defensible and also resolves
  an internal contradiction: the old text told the reader to stop reading their row and then told
  them to read a different row.
- **Three absolutes removed.** *Not gold* (gold is still scarce for a core seat; what is unusually
  scarce is the conversion window). *A direct measurement of what you were sent to do* (it is a proxy
  for one part of the job, blind to tower pressure, rotations forced, area denied). *The expected
  shape for this seat* — **a prevalence claim, from one professional match, in a chapter that says
  three paragraphs later that it has no bracket evidence.** That one is the worst of the three
  because §5 bans it explicitly.
- **"Read that table in either direction and it says nothing"** → the row is evidence; it is
  *insufficient* evidence. It cannot grade decisions or identify the winner. It says plenty about
  what each player accumulated.
- **Death priming.** The hold's *your own death is a legitimate line item; write the number* nudged
  toward treating dying as the sophisticated offlane answer, in a chapter that elsewhere warns
  against exactly that reading. Now carries ch. 32's repaired formulation — **zero is valid and may
  be right** — plus costs that are not deaths: farm, a cooldown, tower health, an item revealed, an
  area surrendered.
- **Minute 14 was overweighted.** It was described as "the last minute your lane advantage was still
  large enough to be worth something", with *large enough* undefined and the gap at +393. Now stated
  as a transition point in this match and explicitly not a threshold.

### 9b. Foundations — applied to `CONTEXT.md §3`, and owed by three published chapters

**The pass mark was self-validating.** It graded compliance with a plan the reader wrote themselves,
so *objective: their tower; cost: three deaths; stop: after three deaths* passes every time it is
followed. Split into a **process mark** and a **calibration review** — the second asking whether the
objective was worth that cost *on what was knowable*, which is ex ante and not hindsight.

This was an inconsistency inside the document rather than a decision. §6's free-death definition
already asks whether a meaningful exchange was **reasonably available** — a calibration question —
while the pass mark asked only whether instructions were followed. **Ch. 12, 21 and 32 carry pure process marks and are owed
the calibration half; ch. 01 needs a clause rather than a block** — its mark already asks whether an
exchange was *available*, which is the calibration question, because it was derived from the
free-death definition rather than from the template. It omits only whether the exchange was worth the
risk. The first version of this note said "three chapters" and there are four; that the chapter built
directly on the definition is the one closest to correct is an argument about which document to trust.

That is the revision backlog for the next session, and it is small: one block in three chapters, one
clause in a fourth.

### 9c. Pushed back on, with reasons

- **The `.owed` block's "an inversion would look like this" is not a retired remnant.** The reviewer
  read it as architecture left over from Part VII's abandoned premise. It is not: what was retired is
  the premise that *seat chapters find inversions*, while `.inversion` / `.owed` remain live
  book-wide devices, and `§3` defines `.owed` as "a visible note that no inversion was found,
  **saying what one would have to look like**". Ch. 32's `.owed` does the same thing. Naming the
  test that was not run is the block's whole function; removing it would leave a limitation stated
  without saying what would settle it.
- **"Net worth" was the wrong correction.** The review said the figures are net worth rather than
  spendable gold. Half right, and the precise answer matters: `gold_t` is **cumulative gold earned**,
  which tracks `total_gold` and is a third quantity distinct from both net worth and unspent gold.
  Adopting "net worth" would have replaced one wrong noun with another.

### 9d. What this says about the review pipeline

Every item in §9a and §9b was an **argument** defect, and the machinery is green on all of them —
before and after. `matches.py` verified every figure in the impossible exercise, because the figures
were right and the instruction built on them was not. This is the fourth consecutive pilot where the
serious findings came from a reader, and the first where one of them invalidated a rule in the
foundations rather than a sentence in a chapter.

### 9e. The sweep, done — and the checker that makes the next one cheaper

Applied 2026-08-04, after review pushed back on the sequencing.

**One correction to the review, checked rather than argued.** It said five live chapters carry the
defect. It is four. **Ch. 30 already carries both marks** — it is the chapter the split was found in.
The confusion came from a grep for the string *"pass mark"*, which returns nothing for ch. 30
precisely *because* it had been migrated and the block renamed. A search for the old name cannot find
the chapters that have moved past it, which is a small lesson about auditing by string.

What ch. 30 *did* owe was the four-outcome taxonomy, which it did not have.

**Migrated, all five:**

| Ch. | What changed |
|---|---|
| 01 | A clause, not a block. Its mark already asked whether an exchange was *available*; it now also asks whether the exchange was worth the risk accepted, and reports four outcomes |
| 12 | Process mark / calibration review split; four outcomes |
| 21 | Same; its worked example makes the self-validating failure concrete |
| 30 | Four outcomes added; both marks were already present |
| 32 | Same split, with the seat-specific point that naming a purpose does not make it worth dying for |

**`checks/rules.py` is new, gating, negative-controlled, and is the third checker aimed at the same
failure.** `retired.py` freezes vocabulary, `status.py` freezes counts, and neither can see a chapter
implementing an *old version of a rule in current words* — which is exactly what four chapters were
doing. Each chapter now declares, near the top:

    <!-- rules: CALIBRATION_MARK=2 HOLD_PASSABLE=2 NEXT_GAME_LIVE=1 -->

Bumping a version in `checks/rules.tsv` turns **every** chapter red at once, and the only route back
to green is opening each one. Negative-controlled both ways: a bumped rule failed all five, a
stripped declaration failed one.

**What it cannot do, stated in its own header so it is never oversold.** It cannot read prose and
decide whether a chapter obeys a rule. No checker can — the rules are semantic. It makes migration
**deliberate** rather than remembered. A version bumped without reading the chapter is a false claim,
but it is a false claim in a diff with someone's name on it, and every instance of this failure so
far has been an omission rather than a lie.

**One rule was narrowed before being registered.** `NEXT_GAME_LIVE` was first written as *replay work
belongs in `After the game`*, which would have failed ch. 01 — whose `Next game` is a review list by
design, every item obtainable, none of it live. That is a design choice this repository has no
evidence against. `checks/register.py` made the same mistake on its first run by banning words the
foundations do not ban, and the cost is identical: a checker that enforces more than its case
establishes trains the author to argue with it.

### 9f. SETTLED — ch. 01's `Next game` is a review list, and that is allowed once

Settled 2026-08-04, while drafting ch. 02, and written into `CONTEXT.md §3` as a **principled
exception**: a chapter whose own finding is that the decision cannot be judged in the moment may put
review work in `Next game`, because a live list would contradict the chapter. Ch. 01 argues that a
death cannot be classified while it happens; instructing the reader to classify deaths live would be
the chapter arguing with itself.

The exception is narrow by construction — it requires the chapter to have **argued** the
impossibility, not merely to have found live actions hard to invent. **Ch. 02 is the evidence that it
is rare rather than a loophole:** it covers adjacent ground, reaches an equally negative conclusion
about what the record can settle, and its `Next game` is live in all five items.

## 10. Part I is drafta ble, and the feasibility check found a live error

Run 2026-08-04, before drafting ch. 02 — because `CONTEXT.md §7`'s ledger for 8928953683 says ch. 02
and ch. 03 "need *reconstruction* evidence this match cannot supply", and chapters 02, 03 and 04 are
all contracted on precisely that. Committing four chapters to an assumption about the evidence would
have repeated ch. 30's process failure (§8i) inside a day.

**The assumption was wrong in the good direction.** The parsed record carries substantially more
reconstruction material than ch. 01 claimed:

| Field | What it supports |
|---|---|
| `teamfights[].players[].deaths_pos` | Map coordinates for deaths inside fight windows — 30 of 59 in ch. 01's match, 25 in ch. 30's |
| `obs_log` / `obs_left_log` with `x`, `y`, `z` | **Vision state reconstructed at any timestamp.** Directly ch. 02's contract |
| `sen_log` / `sen_left_log` | The same for sentries — what was being denied, and when |
| `lane_pos` | Position density per hero, whole-game rather than timestamped |
| `runes_log`, `purchase_log` | Rune timings; TP scroll purchases, which bear on ch. 04's exit decision |
| `damage_taken`, `killed_by`, `stuns`, `life_state` | Who did the damage, who landed the kill, seconds of disable |

**What is still absent, and it is the important half.** No hero position over time, no health, no mana,
no cooldown state, no camera, no intent. So a decision can be *situated* — where, with what vision,
against whose damage — and still not be *reconstructed*. Ch. 02's contract is "reconstruct the
information that was available before the decision", and the honest version of that is now
**bounded**: vision is genuinely reconstructable, position is reconstructable only for deaths in
fights, and everything about the player's own state is not.

That bound is a chapter, not an obstacle. Ch. 02 can show a reader exactly which observer wards were
standing when they walked somewhere — which is the single most useful reconstruction the record
affords, and one no scoreboard has ever offered.

**The check also found ch. 01 asserting the opposite, on the live site.** Corrected; see
`CONTEXT.md §8`. Two new check types register the absences as claims, because *the record does not
contain this* had been resting on somebody's memory of having looked.

### 10a. Order for Part I, revised by the above

1. **Ch. 02** — vision reconstruction is its evidence base and it is the strongest of the four.
   Needs a case where a death follows a ward expiring or a sentry landing.
2. **Ch. 04** — the exit decision; TP purchases and `purchase_log` timings give it something real.
3. **Ch. 03** — the weakest evidence position of the four, since "the sequence that removed the
   escape" wants per-second position the record does not hold. Draft it after 02 and 04 so its
   boundaries are already fenced by what they established.
4. **Ch. 05** — the anti-passivity chapter, and the one that needs a *different* kind of case: a
   player who did not die and lost anyway. `life_state_dead`, low deaths with poor `lane_efficiency`,
   or a low `teamfight_participation` on a losing side are the places to look.

**Settle `§9f` first** — whether ch. 01's `Next game` being a review list is the template or a
deviation — because 02 through 05 will otherwise inherit it by copying.

### 10b. Nothing else outstanding — the sweep that found the last of it

Ran a deliberate audit rather than declaring the work clean, and it found one more instance of the
same pattern: the absence rule from `CONTEXT.md §8` had been applied to ch. 01 and to nothing else,
while chapters 12, 30 and 32 all made unchecked absence claims about the bracket sample. Fixed by
registering the sample's schema, four new claims, negative-controlled.

`checks/status.py` also gained a bracket-claim count check, because the count moved from six to ten
and README.md still said six — drift in the one number that file already computed and did not compare.

**Open, and genuinely open rather than forgotten:**

1. **`§9f` — ch. 01's `Next game` is a review list.** Blocks nothing mechanically, but chapters 02–05
   will copy whatever ch. 01 does. **Recommendation: keep it, and write the reason into `§3`.** The
   chapter's argument is that a death cannot be classified live; a live action list would contradict
   the chapter. What §3 should say is that `Next game` may be review work *when the chapter's own
   finding is that the decision cannot be judged in the moment* — which is a principled exception, not
   a licence, and ch. 01 is currently the only chapter that earns it.
2. **Part VII's sizing.** `§8h`, `§8i`. The author's call, deferred, blocks nothing until ch. 28.

Everything else in this file is closed. Part I can start at ch. 02.

## 11. Ch. 02 on review — and the ward-fate error it exposed in ch. 32

Review 2026-08-04. The most consequential finding was a factual one that propagated backwards into a
published chapter.

### 11a. Expiry versus destruction is a fact, not an inference

Ch. 02 called three Radiant observers *"320, 361 and 361 — their full duration, untouched"*, which is
self-contradictory: the same table gives 360 as a full life. The reviewer spotted the inconsistency
and offered three candidate explanations. The record supplies a fourth and better one.

**`obs_left_log` carries `attackername`, and it is self-attributed on expiry** — an expiring ward is
credited to the player who placed it, a destroyed one to whoever killed it. So the 320-second ward was
**killed by Mirana**, the very hero the chapter is about, three minutes after the death it examines.
That is not a footnote: it is the evidence against the reading the chapter was drifting toward, that
Dire were not contesting vision. She killed two Radiant observers in that game.

**The same field falsifies ch. 32, which was live.** Ch. 32 said *"eleven survived exactly 360
seconds… eleven expired and one was destroyed"*, inferring fate from duration. By `attackername`:
**ten expired, two were destroyed**, and only **nine** ran exactly 360 with a tenth at 361. The extra
kill lived **351 of its 360 seconds** — taken nine seconds before it would have run out anyway, which
no duration heuristic could ever have caught, and which is a better illustration of the seat's fixed
clock than the sentence it replaces.

Two new check types, `ward_ended_by` and `ward_fates`, so the fate is registered rather than read off
a lifetime. **The individual lifetimes in ch. 32 were all registered and all correct; the sentence
that counted them was checked by nothing.** That is the aggregate-versus-item gap `coverage.py` cannot
see, because the count was written in words.

### 11b. Applied to ch. 02

- **`KNOWN` renamed to `AVAILABLE WITHOUT LOOKING FURTHER`.** The chapter said in one breath that the
  record cannot establish what anyone attended to, and in another labelled a list *what you know*.
  Availability is not attention, and the gap between them may be the improvable error the chapter is
  hunting.
- **Three categories became four:** available / **checkable** / **inferable** / unavailable. The old
  middle row held two different operations — a sentry *settles* whether a ward is there; a missing
  hero *shifts a probability* and says nothing about wards. Collapsing them eventually grades a reader
  for failing to deduce something never deducible.
- **The reveal now closes the loop**, answering each item rather than introducing a proposition the
  hold never raised.
- **"Every answer passes" → "admissible".** The self-validation defect in miniature, in the one place
  the calibration split had not reached.
- **"a half of the map her team had been unable to see"** → no observer coverage. Ward counts are not
  vision; heroes, creeps and buildings see things. The chapter said so two sections later and the
  later caveat cannot repair the earlier claim.
- **"you have found the answer" → "you have found an information gap"**, which is what an empty blank
  actually is. Acting under a known gap can be correct.
- Superlative removed (*the single largest thing most players never hold on to* — a bracket-frequency
  claim in a chapter that states it has no bracket data). *Do not infer enemy ward counts* narrowed to
  the exact banned move: no confident global number, provisional local beliefs encouraged with their
  evidence named.
- **The after-game loop no longer runs on memory.** It requires the in-game note, and *not enough
  evidence to reconstruct my process* is a stated valid outcome — because a known outcome will
  cheerfully invent a plan for you. The ten-minute mark and sixty seconds are now labelled arbitrary
  standardisation rather than implied thresholds.

### 11bis. A second review arrived, of a version that no longer existed

Worth recording because the failure is not the reviewer's and will recur. A second pass on ch. 02
returned seven recommendations, all confident, all well argued, and **all seven already applied and
deployed two commits earlier**. It was a fresh generation from a stale copy of the chapter — the
wording differs from the first pass, so it was genuinely re-run rather than resubmitted.

This is `CONTEXT.md §9`'s standing rule doing its job in an unexpected direction. The rule was written
for reviewers asserting facts about *the world* — an API that did not exist while it was returning
200. Here the stale fact was about **the repository itself**, which felt safer and was not.

**The practical countermeasure is one line: give a reviewer the commit, not the prose.** A review of
"chapter 02" is a review of whichever chapter 02 the reviewer happens to hold. Nothing in a
well-argued report signals that its subject has moved, and the report will not mention the fixes
because it cannot see them.

One item in it was genuinely new and was taken — see §11d.

### 11d. The four rungs, from the second pass

The first pass said *rename `known` to `available`*. The second went further and proposed a ladder for
the player's relationship to a fact: **available → noticed → remembered → acted upon.**

That is orthogonal to the chapter's existing four categories, which describe the *information*. These
describe the *reader*, and they break differently: not-noticed is an attention problem, not-remembered
is a holding problem, not-acted-on is a decision problem, and only the last is one the rest of this
book can help with. Added to ch. 02's review loop, where it converts a diagnosis into a repair, and
deliberately not to the hold — the chapter has enough taxonomy in it already.

It also closes the chapter's own loop: the record can establish that a fact was available and can
never say which rung the reader fell off. That is precisely the half of the reconstruction the chapter
keeps saying the reader must supply, and it had not previously said *where*.

### 11c. One thing caught in the drafting rather than the review

The first version of the repaired reveal ended on *everything you were shown was unavailable*, which
is **ch. 01's reveal in a new costume** and is forbidden by §1e. Restructured so the reader **writes
their own two facts** — one checkable, one unavailable — and the reveal contrasts those with the list
they were handed. The finding becomes positive rather than negative: *the replay is best at exactly
the category you can never act on, and worst at the one you can.*

## 12. Ch. 04 — and the word-count gap, closed

### 12a. The chapter

*Leaving Is a Skill*, match **8927063876**, GLYPH vs PlayTime. Teamfight 5 ran 49:49–50:36 and
**seven of ten heroes died in forty-seven seconds**. Three of them — Undying, Doom, Earthshaker —
spent **seven movement-item uses between them** inside that window and died anyway. Dark Seer spent
three and lived.

The chapter's two halves:

1. **An exit has a price and a failure rate.** It was available, it was paid for, and three times it
   did not work.
2. **The record can price staying and can never price leaving.** Gyrocopter *died* in this fight and
   came out **+1,769 gold and +5,912 experience**, more than anyone on the map — including Dark Seer,
   who survived it. So *I should have left sooner* compares a real outcome against a fantasy in which
   leaving was free, instant and successful, and this fight contains three demonstrations that it is
   none of those.

Boundaries named in the chapter, because three neighbours are close: **ch. 03** owns how the escape
closed, **ch. 17** owns cooldowns as a clock, **ch. 20** owns declining a fight not yet entered.

**The parser contradicts itself in this case and the chapter says so.** The fight's own `deaths` field
reads 6; the per-player entries and the kill log both give 7. The difference is a hero who died at the
exact closing second. Both are registered — `teamfight_deaths` and `teamfight_summary_deaths` — because
picking the convenient one quietly is the habit this book is against.

### 12b. Two counts shipped wrong because they were written as words

`coverage.py` compares prose figures against the registry and **only saw digits**. Two errors got
through it:

- **Ch. 32: "eleven wards expired"** — ten did. Live for a day.
- **Ch. 04: "nine movement-item uses"** — seven. Caught before publishing, but only because the
  number was re-derived by hand for an unrelated reason.

Worse, when correcting ch. 32 I audited with a **case-sensitive `grep`** and declared it clean while
two capitalised instances survived. That is the audit rule failing at the level of the tool: *a search
for the old string finds neither the chapters that moved past it nor the ones that capitalised it.*

`coverage.py` now reads **spelled-out counts**, including hyphenated compounds. Durations are excluded
deliberately — *forty-nine minutes and thirty-three seconds* is a registered timestamp in words and
flagging it is noise. On its first run over seven chapters it produced **three** hits, all genuine
derived figures now declared, and **one real error**: ch. 02's *seventy-one seconds* against its own
window of 6:39–7:48, which is seventy. Negative-controlled by restoring ch. 32's "Eleven".

**Its limit is in its header.** The registry is a flat set of values, so a small count clears whenever
that number is registered anywhere for any reason — *nine* passes if any claim in the book has the
value 9. It catches large counts reliably and small ones only sometimes. It is not a substitute for
adding up twice.

## 13. Ch. 04 on review — the central claim was wrong, and the record replaced it

The most serious defect found in any chapter so far, because it was the chapter's **thesis** rather
than a sentence in it.

### 13a. "Three exits failed" was never supported

The draft said *"The exit was available, was paid for, and did not work. Three times"*, and later
*"three of three"*. Its own reasoning section, four paragraphs down, said a town portal scroll can
bring a player in and a blink is an entry tool as often as an escape, and that the record holds no
destination and no intention.

Both cannot be true. The evidence supports only: **three heroes spent seven mobility actions inside
the fight and all three died.** It does not support that an exit was attempted, that one was available
at the relevant moment, that leaving failed, or a failure rate of any kind.

This is §4's headline rule breaking in the most expensive available place. Every figure underneath the
claim was registered and correct, so no checker could see it — the same shape as book 4's chapter
where every claim verified and the causal arrow pointed backwards.

### 13b. The record had a better answer than either repair on offer

The review offered two fixes: check the replay tape, or retreat to "mobility was consumed". The tape
is unavailable here — there is no client and no replay parser beyond the JSON. But the record holds
something neither option used: **`deaths_pos` for every death in the fight.**

- All seven deaths fall within **20.6 cells** of one another. One pile.
- **Undying, who spent three mobility actions — the most of anyone — died 3.3 cells from the centre,
  nearer than five of the other six.**

So the honest replacement is stronger than the false claim it replaces: **spending mobility did not,
here, put anybody anywhere else.** It says nothing about intention, needs nothing about intention, and
makes the chapter's point better — *an item in your inventory is not an exit; mobility is a resource
an exit consumes, and it can be consumed for four other purposes first.*

Three new check types: `teamfight_death_pos`, `teamfight_death_spread`,
`teamfight_death_dist_from_centre`.

### 13c. Everything else applied

- **"Staying had a recorded value"** → survival and value are different measurements and came apart.
  The figures do not show that staying produced the gains, that leaving would have forfeited them, or
  that the death bought anything. Some may have been banked before any exit decision existed.
- **"The record can price staying, never leaving"** → *can describe the path taken, cannot price the
  path forgone.* True whichever the player did.
- **The price figure is an upper bound** on missing the whole fight, never the marginal cost of
  leaving at one second — which is the number a reader actually needs and cannot have.
- **The hold now lists what the record withholds** — position, health, mana, cooldowns, enemy
  locations, terrain — and *"I cannot construct a realistic exit from this"* is the fifth admissible
  answer. Ch. 01 and 02 spend themselves establishing that discipline; ch. 04 does not get to suspend
  it for the convenience of its own exercise.
- **The martyrdom answer no longer self-validates.** Naming a purchase does not make the exchange
  sound: the purchase must have been plausibly available from what was known, and zero deaths remains
  a valid maximum cost. Also stated: *no exit* does not mean *I must die here*.
- **Trigger must precede expiry**, stated explicitly. If they are the same event the plan tells you to
  leave at the moment leaving became impossible.
- **The opening said three parts and the chapter taught four.** Fixed.
- **Six frequency claims removed** — *usually feel it*, *never write it down*, *nobody says out loud*,
  *most players*, *almost nobody*, and the promise that ten games yields a personal failure rate. The
  chapter's own `.owed` block says the bracket sample holds no fight data.

### 13d. The audit rule again, and the reviewer was half right

The review said the retired framing *"the moment leaving was still free"* survived in **both** ch. 01
and ch. 04. Checked: it is in **ch. 01 only**, at line 194 — a forward reference to ch. 04 written
before ch. 04 existed, describing it with a phrase its entire argument contradicts. Ch. 04's own
closing was already correct.

Fixed, and *leaving was still free* added to `checks/retired.tsv`. **A summary written before the
thing it summarises is the one case the audit rule cannot catch by construction**, because at the time
of writing there is nothing yet to be inconsistent with. The only defence is to re-read forward
references when the referenced chapter lands, and that is now what the runbook's step 6 means.

## 14. Ch. 03 — the contract could not be met, and the failure is the chapter

### 14a. What the record can and cannot trace

Checked before drafting, per §10a's warning that this was the thinnest of the four.

**Traceable, with timestamps:** deaths, objectives, buybacks, ward placements and endings (with x, y),
purchases, runes. **Positions:** deaths inside teamfight windows only. **Per minute only:** gold, xp,
last hits. **Absent entirely:** hero position over time, health, mana, cooldown state, ability
timestamps.

So the contract as written — *trace the action sequence that removed the escape* — **is not
deliverable** if "action" means the player's own actions. There is no per-second anything. The
original title, *The Thirty Seconds Before*, promised precisely that reconstruction and was retired
before a word was drafted.

**What is deliverable is one step earlier and turned out to be worth more.** A sequence can only be
traced once it is established to be one sequence, and the record can test that: ordered deaths, with
places.

### 14b. The case

Match **8928851109**. The parser's third teamfight runs 18:38–19:30 and holds **six deaths** —
Puck 18:53, Techies 18:54, Mirana 19:05, Earth Spirit 19:15, Clinkz and Undying at 19:30. Four
against two: a rout, with an obvious story.

The positions say otherwise. **Puck and Techies died 1.0 cell apart; everyone else died 63 to 69 cells
away from them.** Spread **69.6**, against **20.6** for ch. 04's fight — which was genuinely one pile.
The eleven-second "pause" is not a pause; it is the record crossing the map with no marker, under one
heading.

The hold gives the reader the six timings alone and asks where the joins are. The gaps are visible
without coordinates, so the split is reachable from the evidence shown, and *"these are one
engagement and here is why the pauses do not trouble me"* is stated as a passing answer.

**The threshold is declared as the book's choice**, not the record's: 30 cells, and any value between
roughly 30 and 60 gives the same two groups because the between-group gap is 63 and the widest
within-group gap is 26. A case whose answer moved with the threshold would not have been usable, and
the chapter says so.

### 14c. The runbook's new step 6 paid for itself immediately

Ch. 01 described ch. 03 as *"the thirty seconds that removed your exit"* — a forward reference written
before ch. 03 existed, to a title that no longer does. Caught by the step added one commit earlier
after the same failure with ch. 04. **Two for two: every forward reference written before its subject
existed has been wrong when the subject arrived.** That is now the expectation rather than a surprise,
and it is an argument for writing forward references vaguely or not at all.

### 14d. `coverage.py` had a compound-value gap

`teamfight_death_pos` registers a coordinate as the string `"118,122"`. The registry scan only matched
cells that were entirely one integer, so **every coordinate ch. 03 quotes looked unregistered while
being registered exactly.** Fixed by splitting compound numeric cells into their parts. The pattern to
watch: a checker that reads claim *files* has to understand every shape a claim value can take, and
each new check type is a new shape.

### 14e. Part I is complete except ch. 05

01, 02, 03, 04 are written. **Ch. 05 remains**, and it needs a different kind of case from all four:
a player who did not die and lost anyway. `life_state_dead`, low deaths beside poor `lane_efficiency`,
or a low `teamfight_participation` on a losing side are the places to look. It is the chapter that
stops Part I teaching the second stuck population to keep doing what is already losing them games —
see §6's two-population table, which remains a **hypothesis with no bracket evidence** and must not be
presented as more.
