# Cookson–Shah four-agent key matroids: EF1 with ordered no-envy on 8 or 12 goods

🕸️ **Graphs, games and automata** · standard · tractability ★★★★☆ · compute: laptop-hours to laptop-days for rational MILP/SMT search; a counterexample has only 864 or 31104 feasible labeled allocations to check · open as of 2026-10-25

## The problem

Benjamin Cookson and Nisarg Shah, Constrained Fair Allocations via Partition Matroid Reductions (arXiv:2608.31121, August 2026), explicitly leave two finite key-matroid questions open in Section 5 and Appendix B. They write that their computer-aided attempts were "unfruitful" but the result may be within reach with "a smarter brute-force strategy". Four agents have arbitrary nonnegative additive values v_ig and a prescribed order 1,2,3,4. In the size-8 matroid, the goods form groups {1,2,3}, {4,5,6}, {7,8}; each bundle contains at most two goods and at most one from each group. In the size-12 matroid there are four groups of three; each bundle contains at most three goods and at most one from each group. All goods must be allocated. The question is whether an allocation can always be both EF1 and free of envy from every earlier agent to every later agent. EF1 means v_i(A_i) >= v_i(A_j)-max_{g in A_j} v_ig; ordered no-envy means v_i(A_i) >= v_i(A_j) for i<j. Positive resolutions for both key matroids complete the authors' reduction for all four-colorable laminar matroids. There are 864 and 31104 feasible labelled complete allocations, respectively (recounted for this entry); these are search-space sizes, not evidence either way. As of 2026-10-25 the abstract page lists v1 (31 Aug 2026) only.

## What counts as a win

EITHER a nonnegative rational 4x8 or 4x12 valuation matrix and an agent order for which no complete feasible allocation under the corresponding key matroid is both EF1 and free of envy from each agent towards every later agent, with a complete exact obstruction certificate; OR an existence certificate for BOTH key matroids covering every nonnegative additive valuation matrix and every agent order: either a kernel-checked formal proof (Lean, Coq or Isabelle, no sorry, admit or extra axioms), or a finite partition of the normalised valuation space into rational polyhedra, each with a named allocation and exact linear-arithmetic (Farkas) certificates of coverage and of every EF1 and ordered-no-envy inequality, re-checked by an independent exact checker. A counterexample refutes the stronger key-matroid property the authors' reduction needs, not EF1 existence for laminar matroids.

## Partial wins

- **p1:** An existence certificate of the same standard for exactly one of the two key matroids, covering arbitrary nonnegative additive values and any prescribed agent order.

## How a win is checked

For a counterexample, clear denominators and enumerate injective assignments of each group to the four agents, retaining equal loads two or three. Verify completeness of the resulting 864/31104 allocations, then exhibit an exact EF1 or ordered-envy violation in every allocation. Regenerate the enumeration from the group constraints instead of trusting a supplied allocation list. A universal proof may partition normalized valuation space into finitely many rational polyhedra, associate allocations with each region, and supply exact linear-arithmetic/Farkas certificates of coverage and the required inequalities. Include all boundary/tie cases and zero-value rows. A kernel-checked general proof is also acceptable; an unexplained SMT UNSAT exit is not.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2608.31121>

## Sources

- <https://arxiv.org/abs/2608.31121>
- <https://arxiv.org/pdf/2608.31121>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Solve the size-8 question first. An adversarial MILP can search valuation matrices while a separation routine finds satisfying allocations.
- Exploit within-group item symmetries and per-agent positive scaling. Do not sort agents away when the no-envy order is fixed.
- For a positive proof, use small allocation menus on valuation regions and exact linear certificate checking, rather than exhaustively enumerating numerical valuations.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Lemma 12 already disproves the top-i-goods-in-distinct-bundles construction. Rediscovering that example is not a win; it does not disprove the desired EF1/no-envy property.
- EF1 alone, or the existence of some acyclic envy order rather than the prescribed order, is insufficient.
- All goods must be allocated, and every bundle must obey both its size and group constraints.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/laminar-ef1-four-agent-key-matroids.md
```

Already set up? Say `run V3R1T4S on laminar-ef1-four-agent-key-matroids`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `laminar-ef1-four-agent-key-matroids`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
