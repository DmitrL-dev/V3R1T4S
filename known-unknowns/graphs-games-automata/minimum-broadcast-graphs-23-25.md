# Minimum broadcast graphs on 23–25 vertices: improve the remaining edge bounds

🕸️ **Graphs, games and automata** · standard · tractability ★★★☆☆ · compute: laptop-hours to laptop-days for constrained graph search with embedded five-round schedules; certificate checks take seconds · open as of 2026-10-25

## The problem

Mohammadhossein Fakharan’s November 2025 Concordia PhD thesis, Dimensional Broadcast Schemes and Their Applications in Broadcast Graphs, section 1.3, printed pages 20–21, lists the remaining gaps through n=32: B(23) in {33,34}, B(24) in {35,36}, and B(25) in {38,39,40}. It credits earlier constructions and degree-based lower bounds, including Bermond and coauthors. In the synchronous telephone model, a simple undirected broadcast graph informs all vertices from every possible source in ceil(log2 n) rounds. Each vertex participates in at most one call per round. A call goes from an endpoint informed at the start of the round to an uninformed neighbor. All three cases allow five rounds. The thesis (pages 20-21) says the values of B(23), B(24) and B(25) have been unknown since 2014: B(24) <= 36 and B(25) <= 40 come from constructions of Bermond et al., and B(24) >= 35 and B(25) >= 38 from degree inequalities plus a computer check of graphs of order 24 and 25.

## What counts as a win

Give a simple graph and explicit five-round broadcast schedules from every vertex, with either 23 vertices and at most 33 edges, 24 vertices and at most 35 edges, or 25 vertices and at most 39 edges. The first two possibilities settle the corresponding exact values using the published lower bounds; a 39-edge 25-vertex graph improves the record, while 38 edges settles B(25). Every source must have its own valid schedule. Also strictly improve the best comparable published result at claim time, including compatible compositions of published objects. State whether the candidate is a composition and identify its components. Values in unmerged pull requests do not set the bar.

## How a win is checked

Check the graph has exactly n labeled vertices, no loops or parallel edges, and the claimed number of edges. For each of n sources initialize only that source as informed. In each round verify that each listed pair is an edge, pairs form a matching, and one endpoint was informed at the start of the round while the other was not. Update all calls simultaneously. After at most five rounds all n vertices must be informed. The entire certificate contains at most n(n−1) transmissions and is tiny.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://spectrum.library.concordia.ca/id/eprint/996508/1/Fakharan_PhD_F2025.pdf>

## Sources

- <https://spectrum.library.concordia.ca/id/eprint/996508/1/Fakharan_PhD_F2025.pdf>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Start from known 34/36/40-edge constructions and try edge deletion with local rewiring.
- Jointly encode graph edges and per-source schedules in SAT, sharing graph variables across sources.
- Exploit a graph automorphism only with a verified orbit argument; expand the final certificate to all sources.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Small diameter does not ensure a five-round broadcast under one-call-per-vertex contention.
- A schedule from one source is insufficient.
- A newly informed vertex can transmit in the next round.
- Allowing six rounds changes the problem.
- The thesis gives the published numerical gaps as of November 2025; search for later exact-case results before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/minimum-broadcast-graphs-23-25.md
```

Already set up? Say `run V3R1T4S on minimum-broadcast-graphs-23-25`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `minimum-broadcast-graphs-23-25`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
