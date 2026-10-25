# Beggar-My-Neighbour: two balanced deals whose matches merge and then terminate

🕸️ **Graphs, games and automata** · standard · tractability ★★★★☆ · compute: laptop-hours (hash reachable trick states from balanced initial decks; a positive certificate replays in minutes or less) · open as of 2026-10-25

## The problem

Nicolas Andorno, Giulio Cernoia, Simone Duiz and Alessandro Michelangeli, 'The Dynamical Landscape of Beggar-My-Neighbour: Ultra-long Matches, Loops, and Infinite Matches' (arXiv:2602.23406, v1 26 Feb 2026, v2 2 Jul 2026), Section 13, ask for explicit examples of the trajectory types of their Figure 15 that have not been detected, specifically "merging trajectories that proceed to a finite termination (collisions)", and ask whether injectivity of the trick map F on reachable states is lost only when a trajectory enters a loop, or also when two distinct trajectories merge and proceed to termination. Section 7 shows that F is not injective even on states reachable from balanced deals (their Figure 5, in the (52,4) setting, built from the analysis of the infinite game of Casella, Anderson, Kleber, Mann, Nessler, Rucklidge, Williams and Wu, Amer. Math. Monthly 132 (2025) 978-994, arXiv:2403.13855); the known reachable collisions lead into loops. Model: the paper's (N,R) game (Sections 2 and 5): N cards, four indistinguishable copies of each special rank 1..R and N-4R ordinary cards, two decks of N/2 cards at the start, player A leads first. Ordinary cards alternate; a special rank r obliges the opponent to play up to r cards, and a new special card passes the challenge back. If the challenged player fails to answer, the challenger collects the central pile in the paper's collection order and leads the next trick. A state is (ordered deck A, ordered deck B, next leader) at an empty-pile trick boundary. As of 2026-10-25 the abstract page lists v2 as the latest version, and a search found no published terminating collision.

## What counts as a win

Provide two valid, distinct balanced initial deals in one specified (N,R) setting, together with reachable distinct playable trick-boundary states x!=y on their trajectories, such that F(x)=F(y)=z and the common continuation from z terminates after finitely many legal moves. Include both traces through the distinct predecessors, the shared successor, and the complete terminating suffix. A collision of arbitrary unbalanced states without balanced-start reachability, a mere equality of terminal winner identities, or entry into a known infinite loop does not count.

## How a win is checked

An independent simulator checks card multiplicities, equal initial deck sizes, initial leader A, and every card play and collection. Serialize each trick state as (ordered A deck, ordered B deck, next leader). Verify that x and y are distinct nonterminal states reached from the two supplied balanced starts, that their complete successor states are identical, and that the common suffix legally empties one deck. Include the central pile and challenge counter in move-level traces where needed to disambiguate end-of-game behavior. The checker must implement sections 2 and 5 of the paper, and is calibrated first on the local non-injectivity mechanism of the paper's equations (7.4)-(7.6) and on the Casella et al. deal, which must enter a loop. No exhaustive classification is needed for this existential question: a short finite replay is an exact certificate and is laptop-checkable in minutes.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2602.23406>

## Sources

- <https://arxiv.org/abs/2602.23406>
- <https://arxiv.org/pdf/2602.23406>
- <https://arxiv.org/abs/2403.13855>
- <https://www.richardpmann.com/beggar-my-neighbour-records.html>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Hash full reachable trick-boundary states and retain predecessors and balanced-start provenance; flag collisions whose common suffix terminates.
- Begin with small legal four-suit deck settings rather than the full 52-card configuration. The authors formulate the question for the (N,R) family.
- The paper’s section 7 illustrates local noninjectivity mechanisms. Use them as search seeds, but prove balanced-start reachability for any proposed witness.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Nontermination is settled (Casella et al., arXiv:2403.13855, Amer. Math. Monthly 2025); a collision that enters a loop is already known and is not this target.
- The next player is part of the state. Identical decks with different leaders are not a collision.
- The collected pile order matters; accidentally reversing it changes the game.
- A trajectory can pass through another balanced configuration. Demand two distinct predecessor states merging at one successor, not two starting points on one orbit.
- The primary source is a preprint; its explicit open question is what is quoted here, not its broader claims.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/beggar-terminating-trajectory-collision.md
```

Already set up? Say `run V3R1T4S on beggar-terminating-trajectory-collision`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `beggar-terminating-trajectory-collision`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
