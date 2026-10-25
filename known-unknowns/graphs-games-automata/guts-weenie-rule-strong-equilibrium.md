# Guts with the Weenie rule: does the symmetric threshold resist every coalition for n >= 4?

🕸️ **Graphs, games and automata** · standard · tractability ★★★☆☆ · compute: laptop-hours to laptop-days for the n=4 and n=5 certificates (exact polynomial integration and chamber certificates in three or four opponent thresholds); the all-n route is a formalisation project · open as of 2026-10-25

## The problem

Kevin Buck, Jae Hwan Lee, Jacob Platnick, Aric Wheeler and Kevin Zumbrun, Continuous Guts Poker and Numerical Optimization of Generalized Recursive Games (2022), Appendix B.3, explicitly conjecture min_{t2,...,tn in [0,1]} alpha(3^(-1/(n-1)),t2,...,tn) >= 0 for every n >= 2. Their words are: "We conjecture that this property holds for general n ≥ 2". Appendix B.2 proves the cases n=2,3; B.3 reports numerical tests for n=3,4,5, not a proof for n>=4. The model gives each player an independent uniform [0,1] hand on every deal. A player holds exactly above their threshold. A sole holder wins and ends the game; otherwise the highest holder wins the pot, each losing holder matches it, and play continues. Under the Weenie rule, when everybody drops, the highest-hand player must match the pot, doubling it for the next deal. Alpha is the paper’s expected zero-sum immediate payoff including virtual-ante adjustments, in units of one player’s current ante. Explicitly, for h>=1 holders, each player receives the virtual amount h-2, the highest holder additionally receives n, and each other holder additionally pays n. For h=0 under the Weenie rule, each receives 1 and the highest-hand player additionally pays n. The target is this published alpha inequality, which underlies the claimed resistance to a coordinated coalition.

Source check, 2026-10-24 UTC (arXiv still lists v3 as the latest version on 2026-10-25): the retrieved status source still presents the question as open. This confirms the cited source, rather than establishing that no later result exists elsewhere. Recheck current literature before claiming a new result.

## What counts as a win

EITHER (a) a refutation: one n >= 4 and an explicit threshold vector (t2, ..., tn) for which the exact alpha value alpha(3^(-1/(n-1)), t2, ..., tn) is strictly negative. A counterexample must specify every threshold as a rational or real algebraic number with isolating data; the distinguished threshold is the positive root of 3*a^(n-1)-1=0. OR (b) a kernel-checked formal proof (Lean, Rocq/Coq or Isabelle, with no sorry, admit or extra axioms, and an axiom audit) of the displayed inequality for every integer n >= 2 and every opponent threshold vector. For the proof route, a written or computer-assisted proof whose analytic steps are not formalised does not count; exact or interval computations may support it only inside the formal proof, where the proof assistant checks them. A finite grid with no counterexample is not a proof.

## Partial wins

- **p1:** The inequality for n=4 for ALL (t2,t3,t4) in [0,1]^3, with an exact global nonnegativity certificate: on every ordering chamber and boundary, a rational sum-of-squares, Bernstein or Positivstellensatz identity (or a replayable real-algebraic decision certificate) that an independent checker verifies in exact arithmetic.
- **p2:** The same exact global nonnegativity certificate for n=5, for ALL four opponent thresholds.

## How a win is checked

Independently integrate the event payoffs over the unit cube of dealt hands, partitioning at the thresholds and the possible highest hand. This yields piecewise polynomials with rational coefficients. Substitute a=3^(-1/(n-1)) using its polynomial and a rational isolating interval. For a negative witness, evaluate in the real algebraic field and certify its sign. For a finite-n proof, check every ordering chamber and boundary using a supplied exact identity (for example a rational sum-of-squares/Bernstein certificate after mapping the ordered chamber to a simplex), or a replayable real-algebraic proof. A general-n proof must be a formal development (induction or other symbolic argument inside the proof assistant): build it in a clean environment, print the axioms used, and check that the formal alpha matches Appendix B and reproduces the proved n = 2, 3 cases. Finitely many positive samples cannot verify it. Small-n certificates should check in minutes to hours.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/pdf/2208.02788>

## Sources

- <https://arxiv.org/pdf/2208.02788>
- <https://arxiv.org/pdf/2412.19855>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Start with n=4. Opponent exchange symmetry reduces the cases to the position of a among the sorted opponent thresholds.
- Reconstruct payoffs from the event definition before optimizing; Appendix B.1 gives useful n=2,3 cross-checks.
- Search numerically for negative regions, then use exact algebraic arithmetic to validate a witness; if none appears, attempt a symbolic chamber certificate.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The abstract sounds more general than the proved body: Appendix B.3 explicitly leaves n>=4 conjectural.
- The 2024 solution of ordinary three-player Guts does not prove this different-rule, higher-player conjecture.
- The one-shot alpha includes virtual-ante accounting. Simply summing cash won during a deal computes a different expression.
- The source has typographical slips in some formulas; derive the definition independently and distinguish any corrected identity from a quotation.
- A proof of the alpha inequality is the precise target. Additional claims about infinite-play utilities require the source’s recursive-game justification.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/guts-weenie-rule-strong-equilibrium.md
```

Already set up? Say `run V3R1T4S on guts-weenie-rule-strong-equilibrium`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `guts-weenie-rule-strong-equilibrium`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
