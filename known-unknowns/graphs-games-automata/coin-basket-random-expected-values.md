# Jehn's random-basket coin game: exact optimal expected win for 2 baskets beyond n = 22 (OEIS A391791) and 3 baskets beyond n = 18 (A391792)

🕸️ **Graphs, games and automata** · harvest (many cells or partial wins within reach) · tractability ★★★★☆ · compute: laptop-hours to laptop-days (exact backward induction over (remaining-coin set, basket-sum profile) states, layer by layer; memory, not time, is the limit: roughly 2^n * T/2 states for 2 baskets, T = n(n+1)/2, so the largest two adjacent layers reach about 1.5e10 entries near n = 26; rough estimates, not measured) · open as of 2026-10-25

## The problem

Coins worth 1, 2, ..., n are placed one per turn for n turns. Each turn one of k baskets is chosen uniformly at random and the player then puts one remaining coin of their choice into it; after the last turn the player takes the basket with the largest sum. OEIS A391791 (k = 2) gives a(n) = 2^(n-1) times the maximum expected win and A391792 (k = 3) gives 3^(n-1) times it. Both are by Ruediger Jehn (author of the 'Risk or Safety' sequences A387261/A387262), carry keywords nonn,hard,more, and link his Julia program a391791_1.jl.txt. On 2026-10-25 A391791 (revision #16, last edited 7 Jan 2026) lists n = 1..22: 1, 5, 20, 65, 190, 530, 1407, 3585, 8942, 21819, 52204, 123190, 287044, 661329, 1509949, 3420580, 7688444, 17173896, 38143782, 84262365, 185278522, 405700861; and A391792 (revision #6, last edited 7 Jan 2026) lists n = 1..18: 1, 7, 40, 192, 837, 3423, 13478, 51396, 190809, 693595, 2477822, 8740848, 30419671, 104752091, 357748926, 1211285880, 4074000387, 13615817865. A391791 also states a conjecture: for n > 9 the optimal first move is to put coin floor((n+3)/2) in the first basket.

## What counts as a win

CONFIRMED: the exact integer values of A391791(23), A391791(24), A391791(25) AND A391792(19), A391792(20), A391792(21) (K = 3 new terms of each; direction: new terms), under the entries' own definitions (a(n) = k^(n-1) times the maximum, over all adaptive placement strategies, of the expected largest basket sum; baskets chosen independently and uniformly each turn; coins 1..n each used exactly once), each computed by two independently written exact programs that (i) agree on every new term, (ii) reproduce every published term (A391791 n = 1..22, A391792 n = 1..18), and (iii) use integer or rational arithmetic only (no floating point anywhere in the value recursion). The terms must not already be in the OEIS entries, their b-files or their edit history at verification time. Submitting to the OEIS is an action for the human only.

## Partial wins

- **p1:** The three new terms of only one of the two sequences (A391791 n = 23..25, or A391792 n = 19..21), with the same two-program confirmation and calibration.
- **p2:** A settled status for A391791's stated conjecture over a range: for every n from 10 through the largest n computed, the full set of optimal first moves listed exactly, either confirming that coin floor((n+3)/2) is optimal for each n or giving the first n where it is not (a counterexample to the conjecture as stated in the entry).

## How a win is checked

Write the recursion from the definition: V(R, s) = (1/k) * sum over baskets b of max over coins c in R of V(R - {c}, s + c*e_b), with V(empty, s) = max(s); canonicalise s by sorting (baskets are exchangeable) and, for k = 2, use only the difference |s1 - s2| because the total placed is fixed by R. For a state with m = |R| turns remaining, store W(R,s) = k^m V(R,s), so W(empty,s) = max(s) and W(R,s) = sum_b max_c W(R-{c},s+c*e_b) are exact integers. At the empty-basket initial state, the published term is W(R,0)/k because the first random basket is irrelevant by symmetry; verify divisibility by k. Use arbitrary-precision integers or prove fixed-width safety for every intermediate value. Sweep layers by |R| from 0 up to n, keeping two layers in memory. Calibrate on every published term, then compute the new terms with a second, independently written program (different language or different state encoding, e.g. full sorted sum vector instead of differences) and require exact agreement. Optionally publish per-layer SHA-256 hashes of the value tables so a third checker can compare layer by layer.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A391791>

## Sources

- <https://oeis.org/A391791>
- <https://oeis.org/A391792>
- <https://oeis.org/A391791/a391791_1.jl.txt>
- <https://oeis.org/A391537>
- <https://oeis.org/A391538>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Two baskets: the state is (remaining set R, |s1 - s2|); the difference has the parity of the placed total, which halves the table; store layer |R| = m as C(n, m) rows indexed by subset rank.
- Three baskets: state (R, sorted (s1, s2, s3)); the number of sorted triples for placed total P is about P^2/12, so n = 19..21 is far smaller than it looks.
- Evaluator first: reproduce n <= 12 in seconds with a memoised recursion, then switch to the layered sweep and confirm it matches before scaling.
- Parallelise inside a layer: each subset R's row depends only on the next layer, so cores split subsets with no locking.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The basket is chosen BEFORE the player picks the coin each turn; reversing the order changes the game (the adversarial siblings A391537/A391538 are different sequences).
- The player takes the larger basket at the end (max), not a fixed basket.
- a(n) is scaled by k^(n-1), not k^n: the first coin's basket choice does not matter by symmetry. Check the scaling against a(3) = 20 (k = 2) and a(3) = 40 (k = 3).
- Do not search only strategies of the conjectured form; the maximum is over all adaptive strategies.
- Memory grows as 2^n times the sum range: measure the largest layer before launching.
- Check both entries, their b-files and their edit histories at claim time; the two sequences can move independently.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/coin-basket-random-expected-values.md
```

Already set up? Say `run V3R1T4S on coin-basket-random-expected-values`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `coin-basket-random-expected-values`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
