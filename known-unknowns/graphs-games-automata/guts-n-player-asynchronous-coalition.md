# Continuous Guts: is the asynchronous coalition value zero for every n >= 4?

🕸️ **Graphs, games and automata** · standard · tractability ★★☆☆☆ · compute: laptop-hours to laptop-days (n=4 payoff analysis, finite-support counterexample search, and exact univariate or chamber certificates) · open as of 2026-10-25

## The problem

Kevin Buck, Jessica Babyak, Leah Dichter, David Jiang and Kevin Zumbrun (2024), Remark 5.9 and section 9.1, explicitly conjecture: "VA = 0 also for the n-player game with (n − 1) vs. 1 coalition." Their paper proves the three-player case. This proposal concerns the ordinary ONE-SHOT continuous Guts alpha payoff and n>=4, not a new game and not the already solved n=3 case. Each player sees an independent uniform [0,1] hand and holds above a selected threshold. The zero-sum alpha accounting is defined in section 3 of Kevin Buck, Jae Hwan Lee, Jacob Platnick, Aric Wheeler and Kevin Zumbrun (2022): if h>=1 hold, everybody receives h-2, the highest holder additionally receives n, and each other holder additionally pays n; if nobody holds, alpha=0. For probability measures mu2,...,mun on [0,1], define VA(n)=inf_{mu2,...,mun} sup_{t1 in [0,1]} E[alpha(t1,T2,...,Tn)], where the opponent thresholds T2,...,Tn are independent with these respective laws. This infimum of a best response is the asynchronous coalition value. A symmetric Nash profile supplies the known upper bound zero; the conjecture is that an independent coalition cannot force it lower. As of 2026-10-25 the abstract page of arXiv:2412.19855 lists v1 (25 Dec 2024) only.

## What counts as a win

EITHER (a) a counterexample: one n >= 4 and explicit independent opponent laws mu_2..mu_n (finite support, with rational or real-algebraic support points and weights) for which sup over t1 in [0,1] of E[alpha(t1, T2, ..., Tn)] < 0, with an exact certificate: the verifier rebuilds the expected alpha as a piecewise polynomial in t1 from the definition, and every candidate maximum (endpoints, breakpoints and every real root of the derivative on each piece, isolated exactly) is shown strictly negative; OR (b) a kernel-checked formal proof (Lean, Coq or Isabelle, with no sorry, admit or extra axioms) that VA(n) = 0 for every n >= 4, over arbitrary independent opponent probability measures. A written or computer-assisted proof whose analytic steps are not formalised does not count. Exhibiting an ordinary Nash equilibrium, or a result for a correlated (synchronous) coalition, does not answer this question.

## Partial wins

- **p1:** A kernel-checked formal proof (as in (b)) that VA(4) = 0 for arbitrary independent probability measures on the three opponent thresholds. A check of pure opponent thresholds alone is insufficient unless the formal proof includes the reduction to them.

## How a win is checked

For a finite-support counterexample: verify nonnegative weights summing to 1 for each independent law, form the product distribution, and reconstruct E[alpha] independently from the alpha accounting of section 3 of arXiv:2208.02788 (calibrate on Proposition 3.2 there for n = 3 and on the symmetric equilibrium threshold 2^(-1/(n-1)) of Proposition 3.3, which must give value 0). As a function of t1 it is piecewise polynomial with breakpoints at the opponents' support points; isolate every derivative root exactly, evaluate all roots, breakpoints and endpoints in exact arithmetic, and require every value strictly negative. For a formal proof: build in a clean environment, print the axioms used, and check that the formal definitions of alpha and of VA match the papers by evaluating them on the n = 3 closed forms.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2412.19855>

## Sources

- <https://arxiv.org/abs/2412.19855>
- <https://arxiv.org/pdf/2412.19855>
- <https://arxiv.org/abs/2208.02788>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Try to extend the partial convexity/concavity arguments of the solved three-player case to four players.
- For counterexample discovery, optimize two- or three-point distributions for each opponent, then rationalize and certify the entire best-response curve.
- Keep the product-distribution restriction explicit in the search representation.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The order is inf over opponent product measures, then sup over player 1; swapping these operations gives a different value.
- Independent mixing and synchronized mixing are different. The known negative synchronous value does not refute this conjecture.
- The follow-up’s Corollary 5.8 contains a repeated-subscript typo; its prose, abstract, and section 9.1 identify the conjecture unambiguously.
- This entry concerns the one-shot alpha game. Do not attach an unsupported conclusion about the infinite recursive asynchronous game.
- The paper’s suggestions about negotiation are excluded because they do not specify an exact success criterion.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/guts-n-player-asynchronous-coalition.md
```

Already set up? Say `run V3R1T4S on guts-n-player-asynchronous-coalition`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `guts-n-player-asynchronous-coalition`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
