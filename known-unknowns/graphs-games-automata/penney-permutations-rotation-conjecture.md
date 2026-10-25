# Permutation Penney: a pattern that its right rotation does not beat (counterexample to Elizalde-Lin Conjecture 6.1), or certified k = 4, 5

🕸️ **Graphs, games and automata** · standard · tractability ★★★☆☆ · compute: laptop-hours to laptop-days (exact consecutive-pattern counts and rational tail certificates for small k; a general proof is harder) · open as of 2026-10-25

## The problem

Sergi Elizalde and Yixin Lin, Penney’s Game for Permutations, DMTCS 28:1 (2026), Conjecture 6.1, state: "For any k ≥ 3 and any σ = σ1 . . . σk−1 σk ∈ Sk, the permutation τ = σk σ1 . . . σk−1" satisfies Pr(sigma precedes tau)<1/2. Generate independent draws from any continuous distribution and inspect consecutive length-k windows by relative order. Alice first chooses sigma; Bob chooses its indicated right rotation tau. The first chosen consecutive pattern to appear wins. The paper proves k=3 and reports numerical evidence for k=4,5 from truncation at n=11; it does not prove the general conjecture. This is a probability-game response strategy, not the already solved binary-word version of Penney’s game. As of 2026-10-25 the arXiv abstract page lists v4 (6 Jul 2026) as the latest version. This entry asks for certified computations only: a counterexample, or certified verification of the conjecture for k = 4 or k = 5. A proof for all k is outside this repository's scope.

## What counts as a win

A specific k >= 4 and sigma in S_k whose right rotation tau = sigma_k sigma_1 ... sigma_(k-1) satisfies Pr(sigma precedes tau) >= 1/2 in the game of arXiv:2404.06585 (independent draws from a continuous distribution; the first of the two consecutive patterns to appear wins), certified by a rigorous lower bound: exact integer counts A, B, R of the permutations of length H in which sigma wins by H, tau wins by H, or neither has appeared, with A/H! >= 1/2. Floating-point values and truncated series without the tail term R/H! do not count. Alternatively, a kernel-checked formal proof (Lean, Rocq/Coq or Isabelle, with no sorry, admit or extra axioms, and an axiom audit) of Conjecture 6.1 for every k >= 3 is also a full win; a written or computer-assisted proof whose analytic steps are not formalised does not count. Before claiming, re-check arXiv and DMTCS for a later version or follow-up.

## Partial wins

- **p1:** Certified verification of Conjecture 6.1 for k = 4: for every sigma in S_4 (up to justified symmetries), exact integer counts A, B, R at some length H with (A + R)/H! < 1/2, so that Pr(sigma precedes its right rotation) < 1/2 rigorously, beyond the paper's truncated numerical evidence.
- **p2:** The same certified verification for every sigma in S_5. Reproducing the truncated numerical estimates does not qualify.

## How a win is checked

Check that sigma is a permutation and that tau is exactly its right rotation. The verifier writes its own exact counter from the definition (for example a cluster-method or transfer recurrence for consecutive patterns, or the series of Theorem 3.7 of the paper with exact avoidance counts) and cross-checks it against brute force over all H! permutations for H <= 10. Uniform iid continuous draws induce the uniform distribution on the H! relative orders, so if A, B and R count permutations of length H in which sigma wins by H, tau wins by H, or neither pattern has appeared, then Pr(sigma wins) lies in [A/H!, (A + R)/H!]. A counterexample needs A/H! >= 1/2; p1 and p2 need (A + R)/H! < 1/2 for every sigma in S_4 (resp. S_5), with any symmetry reduction (reversal, complement) justified. All counts and comparisons use integers. Reproduce the paper's k = 3 values and its Pr(2341 precedes 1234) ~ 0.443 for calibration. For a formal proof, build it in a clean environment, print the axioms used, and check that the formal game definition reproduces the k = 3 values.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2404.06585>

## Sources

- <https://arxiv.org/abs/2404.06585>
- <https://arxiv.org/pdf/2404.06585>
- <https://doi.org/10.46298/dmtcs.16361>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Start by turning the paper’s k=4 numerical evidence into rigorous intervals; retain the unresolved tail explicitly.
- Complement symmetry halves the number of permutations to check. Keep all other symmetry reductions justified.
- Look for small margins at k=5 or k=6 to prioritize counterexample search. The rotation need not be Bob’s best response to be a winning response.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The relative order of the most recent k-1 draws, by itself, must not be treated as a Markov state with uniform next-rank insertion after conditioning on avoidance. That defines the different model mentioned at the end of the paper.
- These probabilities need not be rational; the source proves irrational examples. Require bounds or symbolic real values, not an unjustified rational linear system.
- The source’s example sigma=2341 already shows its rotation is not always the best response; that does not refute Conjecture 6.1.
- The k=3 case is solved and is excluded as a win.
- Problem 6.2 (Bob's best response) is a different question and is not covered by this entry.
- A proof of the conjecture for all k counts only as a kernel-checked formal proof; a written argument is not a win, and certified computations for single k are the partial wins.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/penney-permutations-rotation-conjecture.md
```

Already set up? Say `run V3R1T4S on penney-permutations-rotation-conjecture`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `penney-permutations-rotation-conjecture`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
