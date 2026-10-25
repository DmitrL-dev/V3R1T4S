# Jehn's adversarial coin-basket games: 'Fill your basket' fair compensation beyond n = 16 (OEIS A392305) and the 3-basket guaranteed win beyond n = 14 (A391538, conjectured formula)

🕸️ **Graphs, games and automata** · harvest (many cells or partial wins within reach) · tractability ★★★★☆ · compute: laptop-hours (exact minimax with memoisation over (remaining-coin set, sorted 3-basket sums) states plus alpha-beta or decision-version search; about 2^n * P^2/12 states before pruning; a rough estimate, not measured) · open as of 2026-10-25

## The problem

Two perfect-information games on coins worth 1..n and three baskets, both by Ruediger Jehn. (1) 'Fill your basket' (A392305, keywords nonn,more, added Jan 06 2026): each of n turns the presenter chooses one of three baskets and the placer puts one remaining coin of their choice into it; at the end the placer scores the largest basket sum and the presenter the second largest; a(n) is the compensation paid to the presenter that makes the game a draw under optimal play, i.e. the minimax value of (largest - second largest). Known for n = 1..16: 1, 1, 1, 2, 3, 3, 3, 3, 3, 4, 4, 5, 5, 5, 6, 6. (2) A391538 (keywords nonn,more, Dec 12 2025): each turn the opponent chooses one of three baskets and the player puts a coin of their choice into it; at the end the player takes the largest basket; a(n) is the sum the player can guarantee. Known for n = 1..14: 1, 2, 3, 5, 8, 11, 14, 17, 21, 25, 29, 34, 39, 44, with the entry's CONJECTURED formula a(n) = floor(n(n-1)/6) + n for n > 4 (it is a problem from the Mathekalender 2025 'Game of Chests' challenge by F. Niessen and S. Rathke). The 2-basket version A391537 has a proved closed form floor(n(n-1)/4) + n and is not a target. OPEN as of 2026-10-25: no term beyond n = 16 (A392305) or n = 14 (A391538), and the A391538 formula is unproved. Checked 2026-10-25: A392305 is at revision #13 (20 Jan 2026) and A391538 at revision #18 (30 Dec 2025), with the terms above, no b-files and no pending drafts.

## What counts as a win

CONFIRMED: the exact values of A392305(17), A392305(18), A392305(19), A392305(20) (K = 4 new terms; direction: new terms) under the entry's definition (presenter chooses the basket, then the placer chooses the coin, each turn; payoff = largest basket sum minus second-largest; placer maximises, presenter minimises; a(n) is that minimax value), each with a game certificate: a placer strategy table guaranteeing margin >= a(n) against every presenter choice AND a presenter strategy table holding the margin <= a(n) against every placer choice, both checked by an independent program that walks the (memoised) game graph exhaustively; plus exact reproduction of A392305 for n = 1..16. The terms must not already be in the OEIS entry, its b-file or edit history at verification time. Submitting to the OEIS is an action for the human only.

## Partial wins

- **p1:** A391538 for every n from 15 through 22 with the same two-sided certificate (opponent strategy capping the player's guaranteed sum at a(n), player strategy achieving it), reproducing n = 1..14; this confirms the conjectured formula floor(n(n-1)/6) + n on that range or refutes it at the first n where it fails (a certified counterexample to the formula as stated in the entry).
- **p2:** A392305(17) and A392305(18) only, with the two-sided certificate and calibration.

## How a win is checked

Independent minimax from the definition, memoised on (frozen set of remaining coins, sorted basket sums); a terminal state scores largest minus second largest (A392305) or the largest sum (A391538). For a claimed value v, run two decision searches: 'can the placer force margin >= v' (must be true) and 'can the placer force margin >= v + 1' (must be false); each search returns a strategy table (the placer's move per reachable state for the first, the presenter's basket per reachable state for the second) that a third short program checks by exhaustive play-out against all replies. Calibrate on all published terms first. Exact integers throughout.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A392305>

## Sources

- <https://oeis.org/A392305>
- <https://oeis.org/A391538>
- <https://oeis.org/A391537>
- <https://ruedigerj.github.io/fill_your_basket/>
- <https://www.mathekalender.de/wp/calendar/challenges/2025-01-en/>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Decision version with a known bracket: the terms move by at most 1 per step so far, so test v = a(n-1) and a(n-1) + 1 first; each test is a boolean AND-OR search with heavy pruning.
- Canonicalise the three sums by sorting; baskets with equal sums are interchangeable, which also prunes the presenter's choices.
- Order the placer's coin choices largest-first and the presenter's baskets smallest-sum-first for early cutoffs.
- For A391538, compare optimal play against Jehn's stated strategy (spread the first n-1 coins as evenly as possible over the three baskets, keep coin n for last); the first n where an even split of 1..n-1 into three parts is impossible is where to look for a formula failure.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- In A392305 the placer scores the LARGEST basket and the presenter the SECOND largest; the third basket scores for nobody.
- The presenter moves first in each turn (chooses the basket), then the placer chooses the coin; reversing this order is a different game.
- A392305 is a margin game; do not compute the placer's guaranteed sum (that is A391538, a different payoff).
- A391538's formula is labelled conjectured in the entry; matching it for n <= 14 is not evidence for larger n.
- Memoisation keys must include the multiset of basket sums, not just their total.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/coin-basket-adversarial-games.md
```

Already set up? Say `run V3R1T4S on coin-basket-adversarial-games`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `coin-basket-adversarial-games`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
