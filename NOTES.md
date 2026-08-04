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

From external review, 2026-08-04. The five factual errors it found are **fixed**; these are the
structural items, which are larger and not yet done.

### 1a. It is not yet a decision-forcing case (accepted, not done)

The chapter reveals the whole sequence and then interprets it. The reader can agree or disagree but
never has to *choose*. The proposed fix is to stop the narrative at **40:22**, immediately after both
tier-four towers fall, and give the reader the state they would need:

- who is alive, and whose ultimates are up;
- which buybacks have been used and which have returned;
- where the waves are, whether Roshan is alive, who holds aegis;
- what the reader's own hero can do right now.

Then ask for four commitments *before* revealing what happened: the intended objective, the acceptable
cost, the condition that would make them disengage, and the missing information that matters most.

**This probably changes the template for every chapter**, not just 21 — which is why it is here and
not applied. If a decision-forcing hold is the right shape, `CONTEXT.md §3` gains a move and the
other three pilots should be written with it from the start.

### 1b. The pass mark is outcome-biased (accepted, not done)

Current: *you were alive at the end of the attempt; dying inside their base is a fail.* That grades
survival, not decision quality — and it is the same error the free-death definition was corrected for
one commit earlier, reappearing in the review loop where nobody was looking for it. A support dying
to force two buybacks may be correct.

Replacement shape: name the objective and the maximum acceptable cost **before** the attempt; pass if
the attempt achieved the objective within that cost, or if you disengaged when your stated stopping
condition occurred.

> Objective: force the final two buybacks. Acceptable cost: one support death, no core deaths.
> Stop if: the first core drops below half health before any defender dies.

**Check every other chapter's `After the game` block against this when they are written.** The bias
is attractive because survival is easy to score and decision quality is not.

### 1c. Three `Next game` rules overreach the case

- *"Count their buybacks"* — a reader can track buybacks they have **seen**, not who currently holds
  the gold. Reword to observed buybacks plus whether the cooldown has returned.
- *"Take a lane and a Roshan before the third attempt"* — invents thresholds the case does not
  support (three minutes, two attempts) and requires four teammates. Reword to: after two failed
  attempts, stop repeating the same entry and name the next enabling condition **you** can create.
- *"The same doorway"* — the parsed record proves the deaths, not the entry route. Either add a
  replay observation documenting it or drop the spatial claim. This is a class-2/class-3 confusion of
  exactly the kind `CONTEXT.md §5` exists to prevent, and it got past me.

### 1d. Chapter 21 currently consumes 22–24 (accepted, not done)

The most structural finding. Ch. 21 explains high-ground defensive advantage, buyback as a defensive
mechanism, when to delay for Roshan, and how to make the final attempt — which are the jobs of 22, 23
and 24. The register already assigns buyback to 22, and 21 uses it as a central explanatory device.

Proposed boundaries, to be moved into `CONTEXT.md §6` once settled:

| Chapter | Exclusive job |
|---|---|
| 21 | **Detect** that accumulated advantage has stopped producing progress |
| 22 | Why base defence changes the exchange rate — including buyback |
| 23 | Decide when conditions permit an attempt |
| 24 | Execute and sequence the final conversion |

Under this, ch. 21 ends on a diagnostic — *is my lead still growing, or has it stopped converting?* —
and hands the mechanisms forward rather than explaining them. One sentence naming buyback and high
ground, then: *why the final exchange becomes expensive is chapter 22.*

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

- **The thesis cannot be tested by the evidence the book collects.** `CONTEXT.md §1` promises the
  reader diagnosis stays a hypothesis until target-bracket evidence supports it; match records cannot
  establish age, employment, games per week, or whether someone understood the game while losing.
  Either recruit a consented cohort or say plainly that the thesis is unfalsifiable here. **Unresolved
  since 2026-08-04.**
- **Does the decision-forcing hold (1a) belong in the template?** Decide before pilot two.
- **Chapter length.** No ceiling has been set. Ch. 21 came in at ~1,850 words. Book 4 used 2,000–3,000
  and found the ceiling useful. Worth setting one before four chapters exist and set the norm by
  accident.

---

## 4. Known gaps in the machinery

- **The bracket sampler's seek overshoots.** It extrapolates from a match-ID rate that is not linear
  (measured 17–27 ids/second at different distances). Replace with bisection. Until then
  `checks/data.tsv` is empty and no bracket claim exists.
- **Nothing checks prose against the registry.** This is the gap that let ch. 21 say three deaths
  while its own registered claim said four. `verify.sh` proves the registry matches the record; it
  cannot prove the prose matches the registry, and `CONTEXT.md §5` already admits coverage is
  editorial. A partial check is possible — extract every number from a chapter's HTML and warn on any
  that appears in no registered row. It would be noisy, and it would have caught this.
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
