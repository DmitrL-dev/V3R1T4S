# Regret matching+ inside CFR+/PCFR+: does alternating predictive RM+ converge ergodically? Prove RM+ non-convergence on the 3x3 counterexample game

⚡ **Algorithms** · standard · tractability ★☆☆☆☆ · compute: pure thought plus a formalisation effort (exact rational simulation of candidate games helps find the argument) · open as of 2026-10-25

## The problem

Regret matching+ (RM+) with alternating updates is the regret minimizer inside CFR+, the algorithm that essentially solved heads-up limit hold'em (Tammelin, Burch, Johanson, Bowling, IJCAI 2015). Predictive RM+ (PRM+) with alternation is the core of PCFR+, a state-of-the-art tabular solver (best on 3x3 Abrupt Dark Hex in Table 3 of arXiv:2502.08938). Cai, Farina, Grand-Clément, Kroer, Lee, Luo and Zheng ('Last-Iterate Convergence Properties of Regret-Matching Algorithms in Games', ICLR 2025, arXiv:2311.00676v2) state: 'Despite its strong empirical performance, it is unknown if alternating PRM+ enjoys ergodic convergence', and call alternating PRM+ 'an algorithm for which neither ergodic nor last-iterate convergence guarantees are known'. For simultaneous RM+, alternating RM+ and simultaneous PRM+ the average iterate converges at O(1/sqrt(T)), but the paper shows only NUMERICALLY that their last iterates fail to converge on A = [[3,0,-3],[0,3,-4],[0,0,1]]. That game has a unique, fully mixed, non-strict equilibrium x* = (1/12, 1/12, 5/6), y* = (1/3, 5/12, 1/4), with value 1/4. From R = 0 and uniform strategies the duality gap stays about 1e-1 after 1e5 iterations (their Figure 1), while alternating PRM+ converges there in practice. The paper proves last-iterate convergence of RM+ only when a strict equilibrium exists (Theorem 1); divergence of RM+ was proved earlier only for rock-paper-scissors (Lee et al. 2021, cited there). A literature search on 2026-10-14 found no proof for either question. The positive last-iterate results in that paper, and in later work that searches surfaced, concern smoothed or extragradient variants (SPRM+, ExRM+), not these algorithms. On 2026-10-25 the arXiv listing of 2311.00676 still shows v2 as the latest version.

## What counts as a win

Settle the published question: does alternating PRM+ (Algorithm 8 of arXiv:2311.00676v2, self-play on a two-player zero-sum matrix game, initialized at R = 0 with uniform strategies, uniformly averaged iterates) enjoy ergodic convergence, i.e. does the duality gap of the averaged strategies tend to 0 in every matrix game? Direction: settle, either way. EITHER (a) an explicit matrix game with rational entries and a kernel-checked formal proof (Lean, Rocq/Coq or Isabelle, with no sorry, admit or extra axioms, and an axiom audit) that the averaged duality gap of alternating PRM+ on it does NOT tend to 0, OR (b) a kernel-checked formal proof (Lean, Rocq/Coq or Isabelle, with no sorry, admit or extra axioms, and an axiom audit) that it tends to 0 in every matrix game (any rate). For the proof route, a written or computer-assisted proof whose analytic steps are not formalised does not count; exact or interval computations may support it only inside the formal proof, where the proof assistant checks them.

## Partial wins

- **p1:** A kernel-checked formal proof (as in the success criterion) that alternating RM+ (Algorithm 7 of arXiv:2311.00676v2, the matrix-game core of CFR+), started from R = 0 and uniform strategies, does not converge in the last iterate on A = [[3,0,-3],[0,3,-4],[0,0,1]]: the liminf over t of the duality gap of (x_t, y_t) is positive. This turns the paper's Figure 1 into a theorem.
- **p2:** The same kernel-checked last-iterate non-convergence proof on A for simultaneous RM+ (Algorithm 1) or for PRM+ (Algorithm 2), from R = 0 and uniform strategies.

## How a win is checked

Build the formal development in a clean environment and run #print axioms (or Print Assumptions). Diff the formal update rules against Algorithms 1, 2, 7 and 8 of the paper, and test the formal definitions by executing the first 1,000 iterations on A and matching an independent floating-point implementation. Any exact or interval computation the argument relies on must be checked inside the proof assistant (kernel evaluation or a verified checker). Plots and long simulations never count.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2311.00676>

## Sources

- <https://arxiv.org/abs/2311.00676>
- <https://arxiv.org/pdf/2311.00676v2>
- <https://webdocs.cs.ualberta.ca/~games/poker/publications/2015-ijcai-cfrplus.pdf>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- RM+ is scale-invariant. Normalize the cumulative regrets and study the piecewise-smooth map on the normalized regret simplex, whose effective step size decays like 1/t. Show that the continuous-time RM+ dynamics on A have an attracting set that excludes the equilibrium, then control the discretization (asymptotic pseudotrajectories), or look for exact invariants of the discrete map.
- Simulate in exact rational arithmetic (the updates are rational) and record the sequence of positive-part clipping events. An eventually periodic clipping pattern with linearly growing regret would give a finite core that a formal proof can check by computation, both for p1 and for a counterexample to ergodic convergence of alternating PRM+.
- Search small games (2x2, 2x3, 3x3 with small integer entries) for alternating PRM+ runs whose average-iterate regret grows linearly. Seed the search with A and with rock-paper-scissors perturbations, where non-alternating variants are known or observed to cycle.
- Start from the two proofs in hand: Lee et al.'s RPS divergence for RM+, and Theorem 1 (convergence under a strict equilibrium). Find exactly which step fails for A's fully mixed, non-strict equilibrium.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Numerical non-convergence on A (a duality gap of about 0.1 after 1e5 iterations) is already published and is not a result.
- Variants matter: simultaneous vs alternating updates, which player updates first, uniform vs linear averaging, the initialization, and the prediction used by PRM+. Match Algorithms 1, 2, 7 and 8 of the paper exactly and state the averaging used.
- Ergodic (average), last-iterate and best-iterate convergence are different questions. Alternating PRM+ converges well in practice, so a counterexample to its ergodic convergence may not exist; the convergence proof (b) is the likelier truth and the harder formalisation.
- The positive-part clipping makes the maps non-smooth; arguments for smooth dynamics (replicator, mirror descent) do not transfer automatically.
- Extragradient and smooth variants (ExRM+, SPRM+) already have last-iterate guarantees; results about them do not answer this question.
- Check 2025-2026 papers from the Farina, Kroer, Grand-Clément and Luo groups before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/algorithms/alternating-prm-plus-ergodic-convergence.md
```

Already set up? Say `run V3R1T4S on alternating-prm-plus-ergodic-convergence`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `alternating-prm-plus-ergodic-convergence`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
