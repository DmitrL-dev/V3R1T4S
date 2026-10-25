# Three agents dividing additive chores: does a complete EFX allocation always exist?

🕸️ **Graphs, games and automata** · standard · tractability ★★☆☆☆ · compute: laptop-hours to laptop-days for adversarial integer-cost search; checking a 3-agent, 13–15-chore counterexample means 1594323–14348907 allocations · open as of 2026-10-25

## The problem

Wentao He and Biaoshuai Tao, 'EFX for Additive Chores: Nonexistence, Pareto Incompatibility, and Bi-Valued Existence' (arXiv:2606.08872, v1 7 Jun 2026, v2 9 Jul 2026), explicitly state in Section 6: "It is open whether an EFX allocation always exists for three agents." They show nonexistence for every n>=4, using a four-agent, thirteen-chore, three-cost-level example, and prove existence for four agents with bi-valued costs. Thus neither the general four-agent nonexistence question nor four-agent bi-valued existence is a new target. The remaining three-agent problem has nonnegative additive costs c_ig. A complete allocation X is EFX if, whenever X_i is nonempty, c_i(X_i)-min_{g in X_i}c_ig <= c_i(X_j) for every i,j. This is Definition 2 in the paper, including zero-cost chores. No Pareto or efficiency condition is imposed. As of 2026-10-25 the abstract page lists v2 as the latest version.

## What counts as a win

Settle the stated three-agent existence question: EITHER an explicit nonnegative rational 3 x m cost matrix with no complete EFX allocation (Definition 2 of the paper) and a complete exact obstruction certificate; OR a kernel-checked formal proof (Lean, Coq or Isabelle, no sorry, admit or extra axioms) that a complete EFX allocation exists for every m and all nonnegative additive costs. A written proof whose steps are not formalised, bounded tests, or a bounded-size UNSAT search do not establish existence. The preferred computational route is a small counterexample with a strict violation in every allocation.

## How a win is checked

For a finite counterexample clear denominators, precompute exact subset costs for each agent and enumerate every assignment of every chore to one of the three labeled agents. For each allocation, verify an ordered pair i,j with nonempty X_i and c_i(X_i)-min_{g in X_i}c_ig > c_i(X_j). Empty bundles are handled exactly as in Definition 2. Enumeration with incremental subset sums takes minutes to hours for the suggested sizes. If chores have identical cost columns, an independently verified multiplicity enumeration can replace labeled enumeration. Positive general proofs require a proof kernel; bounded tests or a bounded-size UNSAT search do not prove existence for arbitrary m.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2606.08872>

## Sources

- <https://arxiv.org/abs/2606.08872>
- <https://arxiv.org/pdf/2606.08872>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Use the published four-agent, three-type obstruction as structural guidance, while recognizing that simply deleting an agent changes the problem.
- Search integer cost matrices with a few repeated chore types and a separation routine that returns an EFX allocation to rule out the current candidate.
- Require a positive exact obstruction margin and simplify a found instance before certifying all allocations.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- For chores, remove an item from the envious agent's OWN bundle. The goods convention removes an item from the envied bundle.
- EFX tests removal of every item, equivalently the cheapest own chore, not the most expensive one.
- The source's general n>=4 counterexamples are already published. Bi-valued instances with up to four agents are already covered by existence results.
- A failure of EFX plus Pareto optimality is not a failure of EFX existence.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/three-agent-additive-chores-efx.md
```

Already set up? Say `run V3R1T4S on three-agent-additive-chores-efx`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `three-agent-additive-chores-efx`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
