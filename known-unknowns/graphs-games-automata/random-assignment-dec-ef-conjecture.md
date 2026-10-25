# Random assignments: a finite SD-EF assignment with no Dec-EF decomposition (counterexample to Li-He-Li Conjecture 1)

🕸️ **Graphs, games and automata** · standard · tractability ★★☆☆☆ · compute: laptop-hours to laptop-days; focus counterexample search on 5–8 agents, with 120–40320 permutation columns; exact LP dual checking is small · open as of 2026-10-25

## The problem

Keyi Li, Yihao He and Quanyi Li, Envy-Free Decompositions of Random Assignments: Settling Four Agents, and What Lies Beyond (arXiv:2609.35192, September 2026), state Conjecture 1: for every n and every strict preference profile, every stochastic-dominance envy-free (SD-EF) assignment matrix is EF-decomposable. Given n agents, n objects, strict rankings and a bistochastic matrix P, SD-EF means that for every i,j and top-k set U_ik of agent i, sum_{o in U_ik}P_io >= sum_{o in U_ik}P_jo. A decomposition is a distribution p over bijections sigma with marginals P. It is Dec-EF when for all ordered pairs i,j, Pr[sigma(j) is preferred by i to sigma(i)] <= 1/2. The source builds on Kawase et al., Decomposition envy-freeness in random assignment (Mathematical Social Sciences, 2026). Li et al. settle all four-agent matrices, five-agent matrices with at most four distinct preferences, all five-agent probabilistic-serial outputs, and certain larger type patterns. They report adversarial search through seven agents without a counterexample; this does not settle general five-agent inputs. The first remaining five-agent inputs have five distinct preferences and need not be probabilistic-serial outcomes. As of 2026-10-25 the arXiv abstract page lists v1 only.

## What counts as a win

Produce a finite strict preference profile and nonnegative rational bistochastic P satisfying every SD-EF inequality, together with an exact certificate that NO decomposition of P has all ordered-pair envy probabilities <=1/2. Equivalently certify t*(P)>1/2, where t* is the minimum achievable maximum pairwise envy probability. A bad decomposition of P does not suffice: the claim quantifies over every decomposition.

## How a win is checked

Check P's row and column sums and all SD-EF prefix inequalities in rational arithmetic. Enumerate the n! permutations and their 0/1 pairwise-envy indicators. The feasibility LP has variables p_sigma>=0, marginals sum_sigma p_sigma 1[sigma(i)=o]=P_io, total mass 1, and sum_sigma p_sigma 1[sigma(j) preferred to sigma(i)]<=1/2 for each i!=j. Verify an exact rational Farkas infeasibility certificate by checking its signs, every permutation column and its strictly contradictory right-hand side. Alternatively verify a rational dual bound >1/2 for the minimax LP. For n<=8 this is at most 40320 columns and 56 envy inequalities. Larger witnesses must include a certificate whose full checking still fits the bank's laptop-hours limit.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2609.35192>

## Sources

- <https://arxiv.org/abs/2609.35192>
- <https://arxiv.org/pdf/2609.35192>
- <https://doi.org/10.1016/j.mathsocsci.2026.102532>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Search vertices of the SD-EF polytope; Lemma 3.1 proves the minimax value is convex, so vertices suffice for worst cases of a fixed profile.
- Concentrate on distinct preferences and matrices with several distinct rows. The source has already solved two-row and several repeated-type cases.
- Alternate preference perturbations with primal/dual LP optimization, then rationalize a strict infeasibility margin.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Greedy and maximum-entropy decompositions already have counterexamples. Those are not counterexamples to the existence conjecture.
- All four-agent inputs and all five-agent probabilistic-serial outputs are solved in the status paper; do not claim those cases as new.
- An approximate LP gap near 1/2 is especially unreliable because repeated preferences often force equality exactly.
- The 216-million-vertex positive enumeration in the paper used a server. This entry targets a small obstruction, not a repeat of that computation.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/random-assignment-dec-ef-conjecture.md
```

Already set up? Say `run V3R1T4S on random-assignment-dec-ef-conjecture`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `random-assignment-dec-ef-conjecture`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
