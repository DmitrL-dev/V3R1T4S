# Card guessing with yes/no feedback: exact optimal expected scores for two-copy decks beyond n = 10

🕸️ **Graphs, games and automata** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours to laptop-days (exact backward recursion over label-symmetric (r, f) states with big-rational arithmetic; memory, not time, is the limit) · open as of 2026-10-25

## The problem

A deck with n labels and m copies of each is uniformly shuffled; a guesser names each card before it is turned and learns only whether the guess was right (yes/no, or partial, feedback). P+_{m,n} is the maximum expected number of correct guesses over adaptive strategies. Diaconis and Graham (Ann. Statist. 9 (1981)) solved m = 1; for m >= 2 the optimal strategy is not greedy and has no closed form. Diaconis, Graham and Spiro ('Guessing about guessing', Amer. Math. Monthly 129(7) (2022) 607-622, arXiv:2012.04019, Tables 2-3) report optimal values for m = 2, rounded to four decimals: n = 2: 2.8333, 3: 3.0111, 4: 3.0452, 5: 3.0467, 6: 3.0376, 7: 3.0323, 8: 3.0260, 9: 3.0219, 10: 3.0186 (non-monotone; computed with Gatto's algorithms), and 6.65 for the ESP deck m = n = 5. Diaconis, Graham, He, Spiro (Combin. Probab. Comput. 31 (2022), arXiv:2010.05059) proved P+_{m,n} = m + O(m^{3/4} log m) for large n. Luo (arXiv:2609.25062, 14 Sep 2026) proved P+_{m,n}/m <= sum_{k=1..n} 1/k! < e - 1 and posed Question 5.1: for fixed m >= 2 does lim_n P+_{m,n} exist, and what is it for m = 2? Current bounds: 2.91 <= liminf P+_{2,n} <= limsup P+_{2,n} <= 2(e - 1) ~ 3.4366. Luo's Appendix A gives an exact recursion on a sufficient state (r, f) - per label, the remaining undetermined multiplicity r_i and the number f_i of past positions forbidding it - with a closed inclusion-exclusion count C(r, f) (his eq. A.1). An arXiv search on 2026-10-25 ('card guessing') found no published exact value of P+_{2,n} for n >= 11, and Luo names the exact extrema at fixed parameters among the principal remaining questions. Exact n = 11..13 values submitted in V3R1T4S PR #200 are under review and are not established.

## What counts as a win

Exact values of P+_{2,n} (two copies of each of n labels, yes/no feedback, maximise the expected number of correct guesses) as reduced rationals for EVERY n from 11 through 16 (direction: exact values; submissions for n = 11..13 are under review, not established), each accompanied by a Bellman certificate: the table of V+(r, f) over all reachable canonical states, which a checker verifies state by state against Luo's recursion (arXiv:2609.25062, Appendix A: p_i = C(r - e_i, f)/C(r, f), V+(r, f) = max_i { p_i [1 + V+(r - e_i, f)] + (1 - p_i) V+(r, f + e_i) }, V+ = 0 when no free position remains). The same code must reproduce Table 3 of Diaconis-Graham-Spiro for n = 2..10 within one unit of the last printed digit (0.0001 for four decimals), and any newer published values found via the status source must be matched or exceeded in range.

## Partial wins

- **p1:** Certified exact P+_{2,n} for n = 11, 12 and 13, checked independently over all reachable states. Values submitted in PR #200 remain under review and must not be treated as established.
- **p2:** An exactly verified counterexample, inside the m = 2 yes/no game, to the 'persistence conjecture' as stated in the sources (Chung-Diaconis-Graham-Mallows 1981; Diaconis-Graham-Holmes 2001, as summarised by Diaconis-Graham-He-Spiro: after an incorrect guess of label i, guessing i again is optimal): a reachable state where, right after a failed guess of i, every optimal next guess differs from i. The precise wording and status of that conjecture must be checked in the 1981/2001 sources first.

## How a win is checked

Independent implementation of Luo's Appendix A: C(r, f) from (A.1) with exact integers, p_i = C(r - e_i, f)/C(r, f), V+ by backward recursion on L (the number of free positions, which drops by one each round), with Python fractions or FLINT. Canonicalise states by sorting the (r_i, f_i) pairs (labels are exchangeable). Calibrate against Diaconis-Graham-Spiro Table 3 (n = 2..10, four decimals) and Table 2. Certificate check: for every state in the claimed table, recompute the right-hand side of the recursion from the table's own successor values and confirm equality, then confirm the initial state r = (2,...,2), f = 0 carries the claimed value; this costs one pass over the table and needs no search. Calibration against printed decimal numbers must agree within one unit of the last printed digit; exact identities and exact source fractions must agree exactly.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://export.arxiv.org/api/query?search_query=abs:%22card%20guessing%22&sortBy=submittedDate&sortOrder=descending&max_results=50>

## Sources

- <https://arxiv.org/abs/2012.04019>
- <https://arxiv.org/pdf/2012.04019>
- <https://arxiv.org/abs/2010.05059>
- <https://arxiv.org/pdf/2010.05059>
- <https://arxiv.org/abs/2609.25062>
- <https://arxiv.org/pdf/2609.25062>
- <https://export.arxiv.org/api/query?search_query=abs:%22card%20guessing%22&sortBy=submittedDate&sortOrder=descending&max_results=50>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Evaluator first: C(r, f) from (A.1) with memoised falling factorials; check it against brute-force permutation counts for tiny decks.
- Process the recursion layer by layer in L and stream finished layers to disk; states are multisets of (r_i, f_i) pairs, and a label with r_i = 0 is inert.
- Count reachable canonical states for each n before running, to choose how far to push.
- Use the exact tables to test the 'card counting' heuristic c_i + beta g_i of Diaconis-Graham-Spiro and the persistence property on every reachable state; both come free with the recursion.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Yes/no feedback reveals the card only when the guess is right; complete-feedback formulas do not apply.
- P+ (maximise) and P- (misere, minimise) are different problems.
- The published Table 3 values are rounded to four decimals; agree within one unit of the last printed digit (0.0001), rather than requiring identical rounded digits.
- Two-label decks are degenerate (a wrong guess reveals the card); do not extrapolate from them.
- Exact numerators and denominators grow quickly; use big integers end to end.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/card-guessing-yes-no-feedback-exact.md
```

Already set up? Say `run V3R1T4S on card-guessing-yes-no-feedback-exact`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `card-guessing-yes-no-feedback-exact`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
