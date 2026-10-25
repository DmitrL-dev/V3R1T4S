# Single-error-correcting codes for the Z-channel: beat 112, 198 or 379 (Sloane's 1zc challenge graphs), or certify a tighter upper bound

📊 **Record tables** · standard · tractability ★☆☆☆☆ · compute: laptop-hours to laptop-days (maximum-independent-set heuristics and exact solvers on graphs with 1,024 to 4,096 vertices; verification in milliseconds) · open as of 2026-10-25

## The problem

A Z-channel can change a transmitted 1 into 0, never 0 into 1. For distinct binary words x, y let N(x,y) count positions with x_i = 1 and y_i = 0; a code corrects one such error iff max(N(x,y), N(y,x)) >= 2 for every pair (asymmetric distance 2). OEIS A010101 (N. J. A. Sloane) gives the maximum code sizes 1, 2, 2, 4, 6, 12, 18, 36, 62 for n = 1..9 and says the next three terms lie in 112-117, 198-210 and 379-410 (last edited 24 Aug 2020); Sloane's 'Challenge Problems: Independent Sets in Graphs' page lists the equivalent graphs 1zc.1024, 1zc.2048 and 1zc.4096 (1zc.1024 'Most wanted!'), with the lower bounds from Etzion and Ostergard (IEEE Trans. Inform. Theory 44 (1998)) and, for n = 12, Butenko, Pardalos, Sergienko, Shylo and Stetsyuk (379, 2001). Lebedev, Vorobyev, Lebedev and Deppe (arXiv:2202.00136v2, 2022, Table I) give the same ranges for non-adaptive codes. As of 2026-10-25 a search found no improvement.

## What counts as a win

Success means either (a) RECORD: an explicit set of distinct binary words of length n in {10, 11, 12} with max(N(x,y), N(y,x)) >= 2 for every pair (checked for all pairs), also verified as an independent set of the DIMACS graph 1zc.1024, 1zc.2048 or 1zc.4096 from Sloane's page, whose size is STRICTLY GREATER (direction: max) than the best lower bound shown on OEIS A010101 and on the challenge page, both re-fetched at verification time, and than any later published value found by a literature search (on 2026-10-25: 112, 198 and 379); or (b) CLOSURE: a proof that 112 is optimal for n = 10 (the independence number of 1zc.1024 is 112), with a certificate checkable without trusting the search: a VeriPB proof log of a maximum-independent-set or clique solver run verified by VeriPB (and preferably CakePB), or a DRAT/LRAT proof for a CNF or pseudo-Boolean encoding whose correctness is argued in a short note and whose proof is accepted by cake_lpr.

## Partial wins

- **p1:** A certified upper bound strictly below the published one for n = 10, 11 or 12 (below 117, 210 or 410): an exact rational dual certificate of an LP or semidefinite relaxation adapted to asymmetric distance (exploiting the symmetric group on coordinates), checked by a standalone exact-arithmetic program that rebuilds the relaxation from the definition, or a verified proof log as in (b).

## How a win is checked

Parse the words (or the DIMACS node numbers, where node = 1 + decimal value of the word). Check the asymmetric-distance condition directly for every pair (O(M^2 n), milliseconds). Separately rebuild the graph from the definition, confirm that its edge set equals the downloaded 1zc file (this pins the bit-order convention), and check independence in the file. For a closure or upper bound, run VeriPB (and CakePB) on the proof log, or the exact rational checker on the dual certificate after rebuilding the relaxation from the definition. Re-fetch OEIS A010101 and the challenge page, and search the literature on asymmetric (Z-channel) single-error-correcting codes, before claiming.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A010101>

## Sources

- <https://oeis.org/A010101>
- <https://oeis.org/A265032/a265032.html>
- <https://arxiv.org/abs/2202.00136>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Use the symmetry: the problem is invariant under permutations of coordinates (not under complementation); prescribe a subgroup (cyclic shifts, products of cycles; for n = 11 the cyclic group of prime order) so the code is a union of orbits, then solve the orbit-weighted independent-set problem exactly with an ILP or CP-SAT.
- Layer by weight: two words of equal weight conflict only when they differ in exactly two positions, and words of adjacent weights conflict when one covers the other with one extra 1; seed each weight layer from good constant-weight codes of minimum distance 4 and solve the inter-layer conflicts exactly.
- Modern maximum-independent-set machinery, many runs in parallel: kernelization and reduce-and-peel (KaMIS-style), long local-search runs (NuMVC/FastVC-style vertex-cover search) with many seeds; the graphs are small enough for millions of moves per second.
- Closing n = 10 (112 against 117): exact branch-and-bound with orbital branching or symmetry-breaking constraints and clique cuts from Z-channel balls, with VeriPB proof logging (supported by the Glasgow subgraph/clique solvers), so the closure is checkable.
- Bounds: Delsarte-type LP and Schrijver-type SDP bounds for asymmetric distance (the metric is not translation-invariant, so reduce by the symmetric group acting on weight classes); a certified rational dual giving 116 would be a new upper bound (p1).

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Do not confuse asymmetric distance 2 (this entry) with Hamming distance 3 codes or with codes for unidirectional errors; check the definition against the graph file.
- Node numbering is 1 + decimal value of the word, but the bit order must be pinned by comparing a rebuilt graph with the file.
- Sloane's challenge page is stale in places (it still lists 1dc.2048 as open, although arXiv:2309.14736 settled it in 2023); use OEIS A010101 for the current range and search the literature before claiming.
- Maximum-clique benchmark tables list these graphs as complements; make sure the claimed set is independent in 1zc (a clique in the complement).
- A branch-and-bound log without a proof certificate is not a closure.
- Codes for a single deletion, or for adaptive or two-stage (feedback) Z-channel coding, are different problems.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/z-channel-single-error-codes.md
```

Already set up? Say `run V3R1T4S on z-channel-single-error-codes`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `z-channel-single-error-codes`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
