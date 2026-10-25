# Levine's hat puzzle with 3 to 12 players: beat a best-known success probability in the Buhler et al. record table (or lower V3 <= 89/256)

🕸️ **Graphs, games and automata** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours to laptop-days (an exact evaluation of a t-level strategy enumerates 2^(n*t) hat configurations: 2^15 for n=3, t=5; 2^18 for t=6; 2^20 for n=4, t=5) · open as of 2026-10-25

## The problem

n players each wear an infinite stack of independent fair black/white hats, see every stack but their own, and simultaneously name a position on their own stack; the team wins iff every named hat is black. V_n is the supremum of the success probability. No V_n is known exactly for n > 1; V_n is strictly decreasing in n (Buhler et al. 2021; Alon, Friedgut, Kalai, Kindler, arXiv:2208.06858), and Levine conjectured V_n -> 0 (the best general lower bounds behave like 1/log2(n), via Winkler-type strategies). Buhler, Freiling, Graham, Kariv, Roche, Tiefenbruck, Van Alten, Yeroshkin (INTEGERS 21A (2021), arXiv:1407.4711v8, Section 5 'Best Current Lower Bounds', offered 'for puzzle aficionados ... who would like to improve upon existing strategies') list: V3 >= 9119/32670 ~ 0.279124, V4 >= 14844/64120 ~ 0.231503, V5 >= 205447/1012494 ~ 0.202911, V6 >= 2984604/15946868 ~ 0.187159, V7 >= 43930663/250593742 ~ 0.175306, V8 >= 651583632/3929765616 ~ 0.165807, V9 >= 0.158764..., V10 >= 0.153517..., V11 >= 0.149025..., V12 >= 0.145047... (decimals rounded down). Provenance: V3 and V4 come from 2014 hill climbs (Reyes and Carter) over SYMMETRIC strategies only: for n = 3 a symmetric 32x32 table with values in 1..5 (5 levels) wins 9120 of 32768 configurations, and white-and-black recursive resets give (9120 - 1)/(31^3 + 3*31^2 - 4); for n = 4 a symmetric 4-level 16x16x16 tensor wins 14845/65536, then resets. V5..V12 come from generalized Winkler strategies (Latin-square 'sums' of lowest-black-hat levels over t ~ log2(n) levels, counting bonus wins) with resets; the reset denominators are (2^t - 1)^n + n(2^t - 1)^(n-1) - (n + 1). Upper bounds: V3 <= 89/256 = 0.34765625 (their Theorem 9, a hint argument) and V_n <= V2 <= 81/224. The 2025 papers (Heilman-Tamuz arXiv:2503.09042; Bouquet et al. arXiv:2508.01737v2) give new values for n = 2 only (plus an uncountable-stack variant); an arXiv search on 2026-10-25 found no newer n >= 3 values, so the table appears unchanged since 2021.

## What counts as a win

An explicit strategy for some n with 3 <= n <= 12 - a finite t-level strategy (for each player, a function from the other players' first t hats to a level in 1..t), optionally extended by recursive resets whose renewal bookkeeping is written out in full - whose EXACT success probability, computed by enumerating all 2^(n*t) configurations of one tier and solving the renewal equations in exact rational arithmetic, is STRICTLY GREATER (direction: max) than the value for that n in Buhler et al. Section 5 (arXiv:1407.4711v8) and than any newer published value found via the status source at verification time. For n = 3..8 compare with the printed fractions; for n = 9..12, where only 6-decimal round-downs are printed, the claim must reach at least the printed decimal + 0.000001 (0.158765, 0.153518, 0.149026, 0.145048) unless the exact table fraction is recovered from the paper's construction and strictly beaten. The improvement bar includes the best valid composition of published objects under these same rules, as well as direct published objects. Unmerged submissions are not bars. State whether the submitted object is a composition and identify all components and their sources.

## Partial wins

- **p1:** A certified upper bound V3 < 89/256 = 0.34765625: a hint or matrix-game construction in the style of Buhler et al. Theorem 9 whose value is computed by an exhaustive, re-runnable search in exact arithmetic.

## How a win is checked

Write an evaluator from the definition: for a t-level strategy, loop over all 2^(n*t) hat assignments, compute each player's named level from the OTHER players' hats only, and count the assignments in which every named hat is black; the base success probability is count/2^(n*t), exact. If resets are claimed, model the play tier by tier as an absorbing Markov chain (state: which players have not yet named a level, and whether every level already named was black), with one-tier transition probabilities obtained from the same exhaustive enumeration, and solve it in exact rationals; cross-check against the paper's closed form (W - 1)/((2^t - 1)^n + n(2^t - 1)^(n-1) - (n + 1)) where it applies. Calibrate on n = 2 (the 3-level S3 strategy: W = 22 of 64, value 21/60 = 7/20) and by re-deriving 9119/32670 from a re-searched symmetric 5-level n = 3 strategy. Calibration against printed decimal numbers must agree within one unit of the last printed digit; exact identities and exact source fractions must agree exactly.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://export.arxiv.org/api/query?search_query=abs:Levine%20AND%20abs:hat&sortBy=submittedDate&sortOrder=descending&max_results=50>

## Sources

- <https://arxiv.org/abs/1407.4711>
- <https://arxiv.org/pdf/1407.4711>
- <https://arxiv.org/abs/2208.06858>
- <https://arxiv.org/abs/2508.01737>
- <https://export.arxiv.org/api/query?search_query=abs:Levine%20AND%20abs:hat&sortBy=submittedDate&sortOrder=descending&max_results=50>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Drop the symmetry assumption: the 2014 V3/V4 searches were over symmetric strategies; seed asymmetric local search from symmetric optima.
- More levels: n = 3 with t = 6 (2^18 configurations) and n = 4 with t = 5 (2^20); changing one entry of a player's table (one view of the others' hats) touches only the 2^t configurations in which that view occurs, so incremental exact scoring makes local search fast.
- Run many diversified hill climbs or annealers in parallel, mark each by improvement per CPU-minute, keep the best, then apply the white/black reset construction to every finalist.
- For n >= 5, search over quasigroups (Latin squares of order t) and over which levels count, including the 'bonus' wins when the target sum is missed.
- Exact local completion: fix most of a strategy and solve the best assignment of a block of views with an ILP or MaxSAT model.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The team wins only if ALL players name black hats.
- A player's choice may depend only on the other players' hats; full-configuration enumerators make it easy to leak a player's own hats into their own decision.
- Players may reset at different tiers; renewal bookkeeping must cover mixed cases, not only simultaneous resets.
- V9..V12 are printed as rounded-down decimals; clear them by at least 1e-6 or recover the exact fractions.
- Use exact integer counts; never compare rounded floats against the table.
- p1 is a maximum over all strategies of a hint game; heuristic search cannot certify it.
- Recursive resets and any other valid composition of published strategies belong in the comparison bar; identify the submitted strategy as composed when it is composed.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/levine-hat-n-player-records.md
```

Already set up? Say `run V3R1T4S on levine-hat-n-player-records`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `levine-hat-n-player-records`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
