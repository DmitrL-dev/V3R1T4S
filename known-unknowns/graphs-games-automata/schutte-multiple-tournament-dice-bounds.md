# Unfair dice games: improve a small Schütte multiple-tournament construction bound

🕸️ **Graphs, games and automata** · harvest (many cells or partial wins within reach) · tractability ★★★★☆ · compute: laptop-hours to laptop-days (SAT/local search on two or three tournaments with at most thirteen vertices; witness checking is sub-second scale) · open as of 2026-10-25

## The problem

Joel Jeffries, Schütte’s property for sets of tournaments and an application to dice games (arXiv:2604.08790, April 2026), Definition 2.2, defines f(m,k) as the minimum order of m tournaments on one vertex set such that every k-subset is dominated by a vertex outside that subset in at least one tournament. Section 4 leaves improvement of its construction bound open. Proposition 2.3 composes orders n1,n2 into order n1+n2, with m=m1+m2 and k=k1+k2+1. The published composition bounds in Figure 7 are f(2,5)<=14 and f(3,6)<=13. They follow from two order-7 S2 tournaments, or two order-3 S1 tournaments and one order-7 S2 tournament, respectively. Closing the small published cells under this composition gives the same bars, 14 and 13. Figure 7 marks f(2,4) = 10 and the other small cells as confirmed exact (starred) by a SAT formulation; f(2,5) and f(3,6) are unstarred. The two retained cells are unstarred construction bounds, not claims of proven optimality. The definition is motivated by dice games with a last chooser who selects both a die and a roll mode. Tournament matrices alone do not establish physical dice realization. As of 2026-10-25 the arXiv abstract page lists v1 only.

## What counts as a win

Give explicit adjacency matrices proving f(2,5)<=13 or f(3,6)<=12, with n>=k+1, and strictly below the best composition of all published constructions available when the claim is checked. The cited-source composition bars are 14 and 13; a later published improvement or its compositions can lower them. Unmerged pull-request values are not bars. Report whether the submitted object is itself a composition, and cite every ingredient if it is. One vertex fewer suffices because orders and the verification are exact. An exact value proved by an UNSAT certificate is partial win p1.

## Partial wins

- **p1:** An exact value: an UNSAT certificate (DRAT or LRAT checked by a formally verified checker such as cake_lpr) for a CNF encoding of 'two tournaments on 13 vertices with every 5-subset dominated' (proving f(2,5) = 14) or 'three tournaments on 12 vertices with every 6-subset dominated' (proving f(3,6) = 13), with symmetry breaking proved sound and the encoding's correctness argued in a short note that a skeptic checks against Definition 2.2.

## How a win is checked

Check each matrix has diagonal zero, entries in {0,1}, and A[i,j]+A[j,i]=1 for i!=j. For every k-subset U, check that some single tournament and vertex v outside U have A[v,u]=1 for every u in U. At most C(13,5)=1287 subsets are needed for the proposed witnesses. Regenerate the best composition bar from published ingredients using Proposition 2.3 and compare exact integer orders. For a submitted composition, also check its ingredients and assembly rule; direct checking of the final matrices remains required. A positive SAT search is certified by the matrices independently of the solver. For p1, re-encode the CNF independently from Definition 2.2 (or check the claimant's encoder line by line against it), check every symmetry-breaking clause against its soundness argument, and run the verified checker on the proof.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2604.08790>

## Sources

- <https://arxiv.org/abs/2604.08790>
- <https://arxiv.org/pdf/2604.08790>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Seed the search with Proposition 2.3’s block construction, remove one vertex, and repair uncovered k-subsets.
- Use symmetry breaking for vertex relabeling and permutation of the tournaments; retain a direct matrix checker independent of the encoding.
- Search (m,k)=(2,5) and (3,6), whose Figure 7 cells are unstarred.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Figure 7 marks f(2,4)=10 as exact. No optimality is claimed for 14 or 13; a quick SAT run may settle either cell, so check p1 before a long construction search.
- The dominator must be the same vertex for all elements of U in one tournament; allowing a different tournament for each edge changes the property.
- A tournament tuple alone does not supply physical dice whose first m roll sums realize it. The paper explicitly leaves that additional realization question open.
- Do not retarget the solved m>=k+1 regime, for which the paper proves f(m,k)=k+1.
- This is distinct from lottery coverings and covering codes already in the bank, despite the SAT encoding’s covering interpretation.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/schutte-multiple-tournament-dice-bounds.md
```

Already set up? Say `run V3R1T4S on schutte-multiple-tournament-dice-bounds`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `schutte-multiple-tournament-dice-bounds`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
