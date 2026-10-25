# Risk or Safety: exact optimal-play win probabilities beyond n = 30 (OEIS A387261/A387262)

🕸️ **Graphs, games and automata** · harvest (many cells or partial wins within reach) · tractability ★★★★☆ · compute: laptop-hours to laptop-days (exact policy iteration over O(n^3) positions with big rationals, one strongly connected component at a time; measure growth at n >= 31) · open as of 2026-10-25

## The problem

Two players race to n banked points. On a turn the player tosses a fair coin: each head adds one open point and the player may then stop, banking the open points (turn passes), or toss again; a tail loses all open points and passes the turn. First to n points wins. Jehn ('Optimal strategy in the game Risk or Safety', arXiv:2603.01002, March 2026) proves the solution is unique (following Glenn, Fang and Kruskal's argument for Can't Stop), solves n <= 6 analytically (first-player win probability 6/11 for n = 3, 2236/4165 for n = 4, 1026/1925 for n = 5, 275848876/521145625 for n = 6) and gives optimal strategies up to n = 20 (paper Table 1; OEIS A394776, b-file of 400 terms). On 2026-10-25 OEIS A387261 (numerators) and A387262 (denominators), keyword 'hard', list n = 1..15 (last edited 10 Apr 2026). Exact terms for n = 16..30, each with a Bellman certificate, are in this repository at known-knowns/risk-or-safety-exact-optimal-play/ (merged 2026-10-15, pull request #169). The rules appear to coincide with the coin variant of Pig ('Piglet') analysed by Neller and Presser; check that work for prior exact values before claiming novelty. The open extension starts at n = 31.

## What counts as a win

Exact reduced rationals A387261(n)/A387262(n) - the starting player's win probability from (0 open, 0 banked, 0 banked) under optimal play by both players - for EVERY n from 31 through 45 (direction: new terms), each with a certificate: the claimed value P(a, b, c) for every position (a open and b banked points of the player to move, c banked by the opponent) and the claimed action, satisfying exactly P(a, b, c) = max(continue, stop) for a >= 1 and the forced toss for a = 0, where continue = (1/2)(1 - P(0, c, b)) + (1/2) P(a + 1, b, c) and stop = 1 - P(0, c, a + b), with P = 1 when a + b >= n (equations of Sections 3-4 of arXiv:2603.01002), all checked in exact arithmetic. The same code must reproduce the published terms (n <= 15) and the terms in known-knowns/risk-or-safety-exact-optimal-play/ (n = 16..30), or certify a correction (see p1). Check the OEIS entries, b-files, edit histories and the repository's known-knowns before claiming; terms already established there do not count as new terms.

## Partial wins

- **p1:** A certified correction: an exact Bellman certificate showing that a published value (A387261/A387262 for n <= 15, or the repository's terms for n = 16..30) or a published optimal action (paper Table 1 / A394776, n <= 20) is not optimal.
- **p2:** Certified exact terms for every n = 31..35 with complete independently checked Bellman value/action tables, after calibration on the published and repository terms through n = 30.

## How a win is checked

A short checker in Python fractions reads the claimed value and action tables, checks terminal positions, then checks at every non-terminal position that the claimed value equals the maximum of the two action values computed from the table itself (only the toss at a = 0) and that the claimed action attains it. Every strategy pair ends the game with probability 1 (banked totals never fall and each turn has positive probability of progress), so these equations have a unique solution (Jehn Section 2) and the check proves optimality. Reduce P(0,0,0) and compare with OEIS; calibrate on the closed forms for n <= 6, the OEIS terms for n <= 15 and the repository's terms for n = 16..30.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A387261>

## Sources

- <https://arxiv.org/abs/2603.01002>
- <https://oeis.org/A387261>
- <https://oeis.org/A387262>
- <https://oeis.org/A394776>
- <https://oeis.org/A387260>
- <https://github.com/elder-plinius/V3R1T4S/tree/main/known-knowns/risk-or-safety-exact-optimal-play>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Banked scores never decrease, so positions split into components with a fixed pair {b, c}; solve components in decreasing b + c, each a small two-player stochastic game, by exact policy iteration.
- Find the policy in floating point first, then do one exact rational solve per component and an exact policy-improvement check.
- Numerators reach 38 digits at n = 15 and keep growing: use GMP or FLINT rationals.
- Cross-check the action table against A394776's encoding (n = (j-1)^2 + i if i < j, else i^2 - j + 1, for i points needed by the mover and j by the opponent).

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- At a = 0 the player must toss; stopping with no open points is not an action.
- Reaching n with open points counts as a win (the paper sets P = 1 when a + b = n).
- Near-ties can flip a floating-point policy choice; decide actions only after an exact comparison.
- OEIS 'hard' reflects the original method, not the problem; the main risk is a rules mismatch (who moves first, banking at n), so reproduce n <= 6 exactly before scaling up.
- If the game is exactly Neller-Presser's Piglet, earlier exact or numerical work may exist for some n; check before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/risk-or-safety-exact-optimal-play.md
```

Already set up? Say `run V3R1T4S on risk-or-safety-exact-optimal-play`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `risk-or-safety-exact-optimal-play`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
