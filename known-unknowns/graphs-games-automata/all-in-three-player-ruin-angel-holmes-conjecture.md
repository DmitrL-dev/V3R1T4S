# Three-player all-in betting game (Angel-Holmes): is being short-stacked always worse than tying your opponent? Prove or refute Conjecture 9

🕸️ **Graphs, games and automata** · standard · tractability ★★☆☆☆ · compute: laptop-hours for a pointwise counterexample hunt (certified depth-n recursion, error <= 2^-n); the proof route is a formalisation project (the source's MILP region method stalled beyond depth 6 on 8 cores and only guides a formal proof) · open as of 2026-10-25

## The problem

The 'all in' variant of three-player gambler's ruin (the final-table / ICM setting): players 1, 2, 3 hold real stacks x, y, z > 0. Each round an unordered pair of players is chosen uniformly at random (probability 1/3 each) and they bet on a fair coin; the bet is the largest possible, namely the whole stack of the poorer of the two (a heads-up all-in). A player at 0 is eliminated. f(x, y, z) is the probability that player 1 is eliminated first. The game is scale invariant, and from every state the six transitions (pair, coin) each have probability 1/6 (He-Holmes Figure 1). Angel and Holmes (unpublished manuscript ''All In' poker sequences') showed f is NOT monotone decreasing in x (a player can lower their chance of busting first by giving chips away), and conjectured two weaker monotonicity statements. The first, f(x, y, z) > f(y, x, z) > f(z, x, y) for 0 < x < y < z ('you are better off starting with more money than your opponent'), was proved by Angel Y. He and Mark Holmes, 'All In: Give me your money!', arXiv:2410.15329 (v1, 20 Oct 2024, Theorem 1), with a computer-assisted proof (framework MeshItUp: region partition of the simplex plus mixed-integer programs; code github.com/7angel4/betting-game-proof, MIT licence). Their Section 5.3 (Future Work) states the second as open: Conjecture 9 (Angel-Holmes): for x, y, z > 0 with x < y, f(x, y, z) > f(y, y, z), i.e. a short stack is always strictly worse off than a stack tied with the opponent's. They report that their attempt to prove it with the same method 'ran beyond n = 6' and became too slow. On 2026-10-25 only v1 of arXiv:2410.15329 was listed, and a literature search on 2026-10-14 found no proof or refutation; the earlier page review noted that the repository README identifies a yyz module for this comparison but did not establish a resolution. A computer-assisted proof submitted in V3R1T4S PR #192 was closed on 2026-10-24 without a ruling on its correctness: its region certificates reproduced exactly (9,839 nodes, minimum 379/1813985280), but it rests on two analytic lemmas that need peer review. The conjecture is not established.

## What counts as a win

Settle Angel-Holmes Conjecture 9 as stated in arXiv:2410.15329 Section 5.3 (direction: settle, either way), for the game exactly as defined in that paper's abstract and Section 1. EITHER (A) COUNTEREXAMPLE: explicit positive rationals x < y and z with f(x, y, z) <= f(y, y, z), proved by rigorous enclosures: f(s) lies in [h_n(s), h_n(s) + 2^-n] where h_n(s) is the exact (rational) probability that player 1 is eliminated first within n rounds, so it suffices to exhibit n with h_n(x, y, z) + 2^-n <= h_n(y, y, z), computed in exact rational arithmetic (or interval arithmetic with directed rounding) by a checker that shares no code with the search. OR (B) PROOF: a kernel-checked formal proof (Lean, Rocq/Coq or Isabelle, with no sorry, admit or extra axioms, and an axiom audit) that f(x, y, z) > f(y, y, z) for ALL real x, y, z > 0 with x < y. For the proof route, a written or computer-assisted proof whose analytic steps are not formalised does not count; exact or interval computations may support it only inside the formal proof, where the proof assistant checks them. A region certificate plus hand-proved tail or boundary lemmas is therefore not a full win.

## Partial wins

- **p1:** A kernel-checked formal proof (as in (B)) of Conjecture 9 on one of the three orderings of z separately: z >= y (player 3 is the chip leader), or z <= x (player 3 is the shortest), or x < z < y. All three together are the full win (B).

## How a win is checked

Write an exact evaluator: from state (a, b, c) with a, b, c > 0, each of the 6 (pair, winner) outcomes has probability 1/6; the poorer member of the chosen pair either doubles or is eliminated (equal stacks: the loser is eliminated). h_0 = 0; h_n(s) = sum over outcomes of (1/6) * [1 if player 1 is eliminated by that outcome; 0 if another player is eliminated; h_{n-1}(next state) otherwise]. Every round ends the game with probability at least 1/2, so 0 <= f - h_n <= 2^-n, which turns finite-depth exact values into rigorous enclosures. Sanity checks before trusting anything: f(1, 1, 1) = 1/3 (first round always eliminates someone; player 1 is in 2 of the 3 pairs and loses half the time); f(x, y, z) = f(x, z, y); scale invariance f(cx, cy, cz) = f(x, y, z); Monte Carlo agreement at random points; reproduce the sign of He-Holmes Theorem 1 at random 0 < x < y < z. For (A), check the enclosures separate. For (B) and p1, build the formal development in a clean environment, print the axioms used (#print axioms or Print Assumptions), check by reading that the formal definition of f follows the rules above (including the boundary cases x -> 0 and equal stacks), and check that the formal h_n agrees with the exact evaluator at sample rational points.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2410.15329>

## Sources

- <https://arxiv.org/abs/2410.15329>
- <https://arxiv.org/pdf/2410.15329>
- <https://github.com/7angel4/betting-game-proof>
- <https://arxiv.org/abs/2011.07610>
- <https://github.com/elder-plinius/V3R1T4S/pull/192>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Counterexample first, it is cheap: f is piecewise defined with discontinuities (transitions change whenever two stacks cross or one doubles past another), so the gap f(x, y, z) - f(y, y, z) may be smallest near such boundaries. Scan a fine rational grid of (x/y, z/y) with depth-12 exact values, then refine wherever the certified lower bound of the gap is smallest; Angel-Holmes's own non-monotonicity example shows where f behaves badly.
- If the gap stays bounded away from 0 numerically, the remaining route is a formal proof. The He-Holmes decomposition into h_n plus a tail bound, symmetry (f(x, y, z) = f(x, z, y)), scale normalisation (y = 1) and a partition aligned with the hyperplanes where transitions change can guide it; PR #192's reproduced region certificates show where the margins are smallest.
- Split by the position of z relative to x and y (the partial win p1) and formalise the easiest ordering first.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The conjecture compares f(x, y, z) with f(y, y, z): player 1 moves to player 2's stack while player 3 keeps z (the total changes). Do not confuse it with Theorem 1 (already proved) or with plain monotonicity in x (false, per Angel-Holmes).
- Bets are all-in for the poorer stack, not unit bets: this is NOT the Diaconis-Ethier unit-step model (proposed target gamblers-ruin-scaling-conjecture).
- Floating-point evaluation of h_n is not a certificate; near-ties at region boundaries are exactly where rounding lies.
- Before claiming, inspect the 'yyz' folder of github.com/7angel4/betting-game-proof (it may hold partial or complete progress on this very conjecture), search for the Angel-Holmes manuscript if it has appeared, and search papers citing arXiv:2410.15329.
- The Angel-Holmes manuscript is unpublished; the binding statement is the one quoted in arXiv:2410.15329 Section 5.3.
- PR #192 (closed 2026-10-24) is not a resolution: its certificates reproduced, but its two analytic lemmas were never refereed. A formal proof must cover those steps itself.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/all-in-three-player-ruin-angel-holmes-conjecture.md
```

Already set up? Say `run V3R1T4S on all-in-three-player-ruin-angel-holmes-conjecture`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `all-in-three-player-ruin-angel-holmes-conjecture`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
