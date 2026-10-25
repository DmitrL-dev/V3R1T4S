# Graph Golf (order/degree and host-switch problems): beat a 2021 best diameter and average shortest path length

🕸️ **Graphs, games and automata** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days (bit-parallel BFS; one exact evaluation of the n = 158976 instance takes minutes on a multi-core laptop) · open as of 2026-10-25

## The problem

Graph Golf, the order/degree problem competition run by the National Institute of Informatics from 2015 to 2021, ranks graphs with a fixed number of vertices and a degree bound by diameter and then by average shortest-path length (ASPL); its host-switch variant measures paths between degree-one hosts attached to switches of bounded radix. The 2021 rankings page (update 2021-10-11) lists the best graphs for each featured problem, with entries by Team RK, EvbCFfp1XB, MODAL-Team, D. Shimizu, SDKY-NITTYM and others, and an ASPL gap to the lower bound for each; only n40d5 and n432d12 have gap 0. The competition is closed, so the table is frozen; later papers may hold better graphs. The target is a strict lexicographic improvement for a featured 2021 problem whose gap is positive, with the incumbent's ASPL recomputed exactly from its published edge file.

## What counts as a win

Success means an explicit graph for one of the 2021 featured problems other than n40d5 and n432d12 (which meet the lower bound), satisfying the definition on http://research.nii.ac.jp/graphgolf/problem.html (general: simple, undirected, connected, exactly n vertices, every degree <= d; host-switch: exactly n hosts of degree 1, each adjacent to a switch, any number of switches of degree <= r, simple and connected), whose (diameter, ASPL), or (h-diameter, h-ASPL), is lexicographically STRICTLY smaller (direction: min) than the best graph listed for that problem on http://research.nii.ac.jp/graphgolf/ranking.html, with the incumbent's ASPL recomputed exactly (total distance divided by the number of pairs, as a rational number) from its published edge file rather than read from the 5-decimal display, and also smaller than any later published graph for that problem. Ties do not count.

## Partial wins

- **p1:** A strict improvement, under that year's rules and verified the same way, on a featured problem of the 2015-2019 Graph Golf competitions (their ranking pages on the same site), against the best graph listed there and any later published one.

## How a win is checked

Read the edge list (calibrate the format by recomputing an incumbent from its published edges.gz file). Check vertex and host counts, simplicity, degree or radix bounds and connectivity. Run BFS from every vertex (bit-parallel BFS for large n; the organisers link Ryuhei Mori's C++ ASPL program and Ryota Yasudo's host-switch program from problem.html) to get the exact diameter and the exact sum of distances, and compare with the incumbent as rationals. Seconds for small cells, minutes for n = 158976.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <http://research.nii.ac.jp/graphgolf/ranking.html>

## Sources

- <http://research.nii.ac.jp/graphgolf/>
- <http://research.nii.ac.jp/graphgolf/problem.html>
- <http://research.nii.ac.jp/graphgolf/rules.html>
- <http://research.nii.ac.jp/graphgolf/ranking.html>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Start from the published incumbents and run degree-preserving edge-swap local search with an incremental bit-parallel ASPL evaluator; most cells saw only two serious teams over one season, five years ago.
- For the large structured cells (n65536d64, n100000d128, n158976d10) use algebraic seeds such as Cayley graphs, lifts of small optimal graphs and voltage graphs; vertex-transitive candidates need only one BFS per orbit to evaluate.
- For n1024d5 and n3602d24 the prize is a smaller diameter: check the degree-diameter tables for degree-5 diameter-5 and degree-24 diameter-3 graphs of at least that order, and try vertex deletion or merging while keeping the diameter. Any such graph beats every 2021 entry outright.
- Host-switch cells with small radix (h32r4, h80r6) are small enough for exhaustive or SAT-assisted search over switch topologies, which could improve the incumbent or show it is optimal.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The 5-decimal ASPL display hides near-ties; recompute both graphs exactly.
- Diameter is compared first: a lower ASPL at a larger diameter loses.
- General graphs allow degree <= d (not necessarily regular). Hosts must have exactly one edge, to a switch. Multi-edges and loops are not allowed.
- The competition is closed, so the organisers will not list a new record. The claim stands against the frozen 2021 table, and a novelty search ('order/degree problem', 'host-switch graph', 2022-2026) is part of it; any later published graph for the same problem sets the bar.
- Cells whose gap is 0 are optimal and cannot be beaten; a result below a lower bound means a bug.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/graph-golf-order-degree-aspl.md
```

Already set up? Say `run V3R1T4S on graph-golf-order-degree-aspl`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `graph-golf-order-degree-aspl`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
