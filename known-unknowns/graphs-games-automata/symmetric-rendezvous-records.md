# Symmetric rendezvous search: a line strategy below Han et al.'s 4.2574 (unchanged since 2008) or a four-location strategy beating FSD

🕸️ **Graphs, games and automata** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days (strategy optimisation over distributions on unit-step paths; exact rational evaluation of a candidate takes seconds to hours) · open as of 2026-10-25

## The problem

Two searchers start distance 2 apart on a line. They have no common orientation and use the same synchronised random rule with independent randomness, at speed at most 1. Han, Du, Vera and Zuluaga (Operations Research 2008) proved 4.152 <= R <= 4.2574 for agents starting at distance 2 (d = 1; Han et al. show steps of length d suffice) and conjectured R is close to 4.25; Georgiou, Gravel, Kapusin and Mandic (arXiv:2609.13632v2, Sep 2026) restate these as the best known bounds. The separate discrete-location model uses independent random labelings. Cembrano, Fischer and Klimm (arXiv:2604.02058) give an FSD strategy improving Anderson-Weber for n>=4. The target is a line strategy beating Han et al.'s upper bound, or a strategy beating the best exact FSD parameter choice for four locations. Lower bounds are proofs about all strategies and are outside this entry. Printed line bars require numerical separation; a strict comparison with the exact incumbent strategy is a partial target.

## What counts as a win

CONFIRMED by any one of the following, with the strategy given as a finite explicit object (for the line, for example a distribution over k-step unit-move paths in the sense of Han et al., or a finite-state randomized automaton over moves -1/0/+1 in the agent's own frame; for n locations, a finite-memory randomized rule over location labels) and its expected meeting time computed exactly in rational arithmetic, or enclosed by rigorous interval arithmetic, by a verifier sharing no code with the search. (a) Line, upper bound: expected meeting time <= 4.2573 for initial distance 2 (a margin of 1e-4 below the published 4.2574, so that rounding of the old value cannot matter), counting meetings that happen mid-step. (b) Four locations: a symmetric strategy for n = 4 whose exact expected meeting time is strictly below the minimum over theta in [0, 1) of the exact expected meeting time of the Cembrano-Fischer-Klimm strategy FSD(theta), computed from the exact expression in arXiv:2604.02058 in that paper's time convention (meetings possible from t = 0). In each case the value must beat every bound published at verification time (check arXiv for 'symmetric rendezvous'). The line margins compare against rounded numerical bars. The exact-incumbent comparison in p1 accepts any exactly certified strict improvement. Values in unmerged pull requests are not bars.

## Partial wins

- **p1:** Line: an explicit strategy certified strictly better than the exact expected meeting time of Han et al.'s published 15-Markovian strategy (recomputed exactly from the strategy given in their paper), even if the gain is smaller than 1e-4.
- **p2:** Five locations: an explicit symmetric strategy for n = 5 whose exactly computed expected meeting time is below that of FSD(theta) at its best theta, computed exactly by the verifier (the 2026 paper gives only a lower bound on FSD's improvement for n >= 5).

## How a win is checked

Line: write the joint process of the two agents (each agent's automaton state or path index, the relative position, and the relative orientation, which is +1 or -1 with probability 1/2) as an absorbing Markov chain; meeting is absorption when the relative position hits 0, at an integer time or by crossing within a step. For a k-Markovian strategy, enumerate all pairs of paths in the support for both relative orientations, compute the per-round meeting probability and the expected time spent, and solve the renewal equation exactly, as in the worked examples of arXiv:1805.03351 (Alpern's strategy gives exactly 5). Test the verifier on Alpern's 5 and on the simple 2-Markovian strategy (exactly 7) first. Locations: build the chain over (round position, both players' visit histories modulo the random labelings) and compute the expectation exactly; test on Anderson-Weber for n = 3 and on FSD's closed-form improvement for n = 4.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2609.13632>

## Sources

- <https://arxiv.org/abs/2609.13632>
- <https://arxiv.org/pdf/1805.03351>
- <https://optimization-online.org/2006/05/1400/>
- <https://arxiv.org/abs/2604.02058>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Push k: Han et al. stopped at k = 15 (2^15 paths per agent) with fractional quadratic programming in 2008, and their conjecture that R is about 4.25 suggests the k-Markovian optimum keeps falling with k. Optimise distributions over paths for k = 16 to 24 with sparse supports, many random starts in parallel, and exact re-evaluation of every improvement.
- Search over richer strategy classes than renewal-type k-Markovian ones: small randomized automata whose next path depends on the previous round's path; the September 2026 paper's truncated-chain and weak-peek frameworks give ready-made finite-state machinery for evaluating them.
- For four locations, start from FSD and Weber's 2009 12-step block idea and optimise over correlated tours across several rounds, guided by negative eigenvalues of the matrix of pairwise meeting times, as Weber did; exact evaluation is a finite sum over pairs of label sequences (15,852 pairs for Weber's block strategy).

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Published bounds are rounded to four decimals; a claim within 1e-4 of 4.2574 needs an exact comparison with Han et al.'s actual strategy (partial win p1), not with the rounded number.
- Conventions differ: n-location values depend on whether players can meet at time 0 (as in arXiv:2604.02058) or only from time 1. State the convention and compare like with like.
- Floating-point evaluation of a strategy is not a certificate; use exact rationals or rigorous intervals, and include meetings that occur mid-step on the line.
- Strategies must be symmetric: both agents use the same rule, with independent randomness and independent orientations; any rule that assigns roles (wait-for-mommy) is excluded.
- The unknown-distance line problem (best symmetric ratio 13.926, Klimm, Sagnol, Skutella and Tran, SODA 2022) is a different cell and is not covered by this criterion.
- Active field: Georgiou's and Klimm's groups both published in 2026; re-check arXiv before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/symmetric-rendezvous-records.md
```

Already set up? Say `run V3R1T4S on symmetric-rendezvous-records`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `symmetric-rendezvous-records`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
