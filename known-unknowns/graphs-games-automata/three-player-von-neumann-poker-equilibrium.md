# Three-player von Neumann poker (Krityakierne-Thanatipanonda-Zeilberger 2024): is the conjectured threshold equilibrium a Nash equilibrium at bet size 2?

🕸️ **Graphs, games and automata** · standard · tractability ★★☆☆☆ · compute: laptop-minutes to laptop-hours for exact algebra over piecewise-polynomial payoffs and finite-deck LP/NLP cross-checks; the confirmation route (A) also needs a formalisation effort · open as of 2026-10-25

## The problem

Krityakierne, Thanatipanonda and Zeilberger, 'von Neumann and Newman Pokers with Finite Decks', arXiv:2407.16155 (v1, 23 Jul 2024; Maple packages FinitePoker and ThreePersonPoker), Section 4, extend von Neumann's poker to three players: each antes 1 and receives an independent uniform(0,1) hand; Player I checks (three-way showdown for the pot of 3) or bets b; if I bets, Players II and III each call or fold, the call/fold of each not depending on the other's action (their Call2/Call3 payoffs and Fast NLP give II and III strategies that depend only on their own card), and the highest hand among the non-folded players wins. They write that 'the dynamics of the three-player game therein remain unexplored', guess the form of the continuous equilibrium from finite-deck data ('conjectured Nash equilibrium strategies', Figure 2): I bets iff x < A or x > B, II and III call iff their hand > C, with II and III symmetric, and obtain A, B, C from three indifference equations only (Eq. A, B, C). For b = 2 they report A = 0.137058194328370, B = 0.829422249795391, C = 0.641304115985175, value to I 0.122557074714865, and an optimal bet b* ~ 2.07 with value 0.122590664136184. The paper does not verify the global best-response conditions (only indifference at the three cut points), does not discuss asymmetric equilibria of II and III, and gives no exact closed form. The proposal found no later work on this game, and on 2026-10-25 the arXiv listing still shows v1 only. A written proof for every b > 0 with simultaneous callers was submitted in V3R1T4S PR #196 and closed on 2026-10-24 because its analytic steps need peer review; its b = 2 values reproduced exactly, so it is no refutation, but it is not an established proof either.

## What counts as a win

For b = 2 in the game exactly as defined in arXiv:2407.16155 Section 4 (II and III decide without observing each other's decision), EITHER (A) a kernel-checked formal proof (Lean, Rocq/Coq or Isabelle, with no sorry, admit or extra axioms, and an axiom audit) that the profile (A, B, C) defined by the paper's Eq. A-C (with A, B, C given as exact real algebraic numbers, isolating intervals included) is a Nash equilibrium: for every hand value, each player's prescribed action is a best response against the other two, over ALL measurable deviations (for the proof route, a written or computer-assisted proof whose analytic steps are not formalised does not count; exact or interval computations may support it only inside the formal proof, where the proof assistant checks them); OR (B) a refutation: an explicit hand interval and deviation for one player that strictly improves that player's payoff against the other two players' profile, certified in exact or interval arithmetic. Direction: settle, either way. In case (A) the exact game value at b = 2 must be stated as an algebraic number agreeing with the printed 0.122557074714865 within one unit of its last printed digit (10^-15).

## Partial wins

- **p1:** Settle the same question for every b > 0 (or for every b in a stated interval containing 2): a kernel-checked formal proof (as in (A)) that the threshold profile from Eq. A-C is a Nash equilibrium, or, for a certified explicit b, a refutation certified as in (B).

## How a win is checked

Write the three payoff functions in closed form: against threshold opponents, each player's payoff from each action is a piecewise polynomial in their own hand with breakpoints at A, B, C, so best-response checks reduce to sign conditions of explicit polynomials on finitely many intervals, decidable exactly (Sturm sequences or real-root isolation in sympy, msolve or Mathematica). Validate the evaluator by reproducing the paper's two-player special case (von Neumann: a = 1/9, b = 7/9, c = 5/9, value 1/9 at bet 2) and the reported three-player numbers. Cross-check with the paper's finite-deck solutions, e.g. FastMNE(4,1): value 1/24 for I and -1/48 for II and III, recomputed by exact LP or exact best responses on the finite game. Calibration against printed decimal numbers must agree within one unit of the last printed digit; exact identities and exact source fractions must agree exactly. For (A) and p1, build the formal development in a clean environment, print the axioms used, and check by reading that the formal payoff functions follow Section 4 of the paper (simultaneous callers) and reproduce the two-player von Neumann values.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2407.16155>

## Sources

- <https://arxiv.org/abs/2407.16155>
- <https://arxiv.org/pdf/2407.16155>
- <https://www.math.ucla.edu/~tom/papers/poker2.pdf>
- <https://github.com/elder-plinius/V3R1T4S/pull/196>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Check the regions the indifference equations do not cover: I's check region (A, B) against betting, II's fold region below C (including hands below A, which beat I's bluffs), and whether a hand between C and B prefers to fold when the other caller's range is accounted for.
- If the symmetric profile fails, solve for the true equilibrium with an exact finite-deck NLP sequence (n up to a few hundred) and lift its pattern, the method the paper itself used.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The observation structure matters: if Player III sees Player II's decision before acting (as at a real table), the game is different and the paper's profile does not even have the right strategy space. Stick to the paper's simultaneous reading, or state clearly that a sequential-variant result is a different target.
- Ties have probability zero in the continuous game; in finite decks the paper deals distinct cards, which matters for cross-checks.
- A modest target: the most likely outcome is a clean confirmation (A). Do not overstate it; the novelty is the first full verification, not a new strategy.
- PR #196 (closed 2026-10-24) is not a resolution of the b = 2 target or of the all-b partial win; a formal proof must cover its analytic steps itself.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/three-player-von-neumann-poker-equilibrium.md
```

Already set up? Say `run V3R1T4S on three-player-von-neumann-poker-equilibrium`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `three-player-von-neumann-poker-equilibrium`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
