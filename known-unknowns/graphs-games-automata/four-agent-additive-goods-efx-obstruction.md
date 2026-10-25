# Four additive agents: an exact finite counterexample to complete EFX existence

🕸️ **Graphs, games and automata** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: laptop-hours to laptop-days for structured counterexample search; 4^10=1048576 to 4^12=16777216 allocations for exact checking; no exhaustive search of all valuations is proposed · open as of 2026-10-25

## The problem

Eyad Alkassar, Mahmoud Fouz and Kurt Mehlhorn, 'Complete EFX Allocations Exist for Four Additive Agents and Up to Nine Goods' (arXiv:2608.08590, v1 9 Aug 2026), write that whether complete EFX allocations exist for additive valuations is open for n >= 4 agents; known territory includes two and three agents, four agents with at most one good unallocated, and complete EFX for m <= n + 3 goods (Mahara). Their Theorem 1 covers four additive agents and at most nine goods, even for zero-tolerant EFX0, by reduction lemmas plus a machine-verified certificate corpus. Recent counterexamples (Akrami et al. 2026; Mackenzie and Suzuki 2026) use submodular, not additive, valuations. The target is a counterexample with four agents and strictly positive rational item values, so that EFX and EFX0 coincide: a complete allocation A is EFX if v_i(A_i) >= v_i(A_j) - min_{g in A_j} v_ig for every i, j with A_j nonempty. By the published results any such witness has at least ten goods. As of 2026-10-25 the abstract page lists v1 only. This is a famous open question; long odds.

## What counts as a win

An explicit strictly positive rational 4 x m additive valuation matrix such that no allocation of all m goods to the four agents is EFX, together with an exact exhaustive or compressed obstruction certificate checkable within a few hours on a laptop. Every good must be assigned once; there are no constraints on bundle size. A witness for non-additive valuations, an incomplete allocation, or EFX plus an extra efficiency condition does not qualify. A witness with m <= 9 would contradict Theorem 1 of arXiv:2608.08590 (and, for m <= 7, Mahara's theorem); it counts only after three independently written checkers agree, and the conflict is reported to the authors by the human.

## How a win is checked

Clear denominators and verify strict positivity. Enumerate all 4^m labeled complete allocations and, using exact subset sums, find an i,j,g in A_j with v_i(A_i)<v_i(A_j)-v_ig for each allocation. It suffices to use the good of minimum v_i-value in each envied bundle. Any symmetry reduction must carry a proof that all allocations are covered; unproved canonicalization is not allowed. At m=10..12 a compiled enumerator is a laptop-scale checker. Larger witnesses need a compact proof with independently checked coverage, not just an UNSAT assertion.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2608.08590>

## Sources

- <https://arxiv.org/abs/2608.08590>
- <https://arxiv.org/pdf/2608.08590>
- <https://arxiv.org/abs/2606.08872>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- The source reports difficult regions with near-identical valuations and a common top good. Search perturbations in those regions rather than uniform random matrices.
- Combine adversarial rational valuation search with an exact EFX-allocation separation oracle.
- Use the published <=9 theorem as a negative control on any checker; a claimed positive-valued counterexample below ten goods signals a bug or a conflicting claim requiring resolution.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- All sizes up to nine goods are already solved for four agents. The original literature's older n+3 frontier is stale.
- The source used five 48-vCPU machines for its universal positive result. Extending that exhaustive computation is not the proposed laptop attack.
- Three-agent additive existence and recent submodular counterexamples cannot be repackaged as this target.
- The strictly positive witness requirement avoids counting a change in zero-good conventions as a disproof.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/four-agent-additive-goods-efx-obstruction.md
```

Already set up? Say `run V3R1T4S on four-agent-additive-goods-efx-obstruction`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `four-agent-additive-goods-efx-obstruction`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
