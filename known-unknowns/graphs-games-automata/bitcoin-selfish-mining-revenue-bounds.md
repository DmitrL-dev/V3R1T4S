# Optimal selfish mining in Bitcoin (Sapirshtein-Sompolinsky-Zohar model, gamma = 0): certify an upper bound on the optimal relative revenue below 0.70109 at alpha = 0.45 or below 0.90476 at alpha = 0.475

🕸️ **Graphs, games and automata** · standard · tractability ★★★☆☆ · compute: laptop-hours (finite MDPs with up to ~10^6 states (a, h, fork); certificates are one exact or interval inequality per state-action pair) · open as of 2026-10-25

## The problem

Sapirshtein, Sompolinsky and Zohar ('Optimal Selfish Mining Strategies in Bitcoin', FC 2016, arXiv:1507.06183) model selfish mining as an MDP whose objective is the attacker's share of accepted blocks (REV). Their Table 2 (gamma = 0, truncation T = 95, epsilon = 1e-5) gives epsilon-optimal revenues 0.48866, 0.56808, 0.66891 and 0.80172 at alpha = 0.4, 0.425, 0.45 and 0.475, with upper bounds 0.48904, 0.57226, 0.70109 and 0.90476; at alpha = 0.475 the upper bound is the trivial alpha/(1-alpha). Bar-Zur, Eyal and Tamar (PTO, AFT 2020, arXiv:2007.05614, Table 1, forks capped at 95) report achievable revenues 0.56809, 0.66894 and 0.80184 at alpha = 0.425, 0.45 and 0.475. So at alpha = 0.45 and 0.475 the optimal revenue in the untruncated model is known only to lie in [0.66894, 0.70109] and [0.80184, 0.90476], and the published values are floating-point and uncertified. Sakurai, Nakai and Shudo (arXiv:2607.24415, July 2026) certify bounds on the incentive-compatibility threshold in a model with asymmetric tie-breaking, a different question. As of 2026-10-25 a search found no certified upper bound below SSZ's at these alpha. The target is a certified upper bound for the untruncated SSZ model, obtained from its over-paying finite MDP.

## What counts as a win

A machine-checkable certificate that max over all policies of REV in the untruncated SSZ model (definitions as in arXiv 1507.06183, Sections 2-4, with gamma = 0) is at most U, where U <= 0.70099 at alpha = 0.45 or U <= 0.90466 at alpha = 0.475. Each bar is 1e-4 below the published SSZ Table 2 upper bound (0.70109, 0.90476); lower is better. The certificate has three parts. (i) A rational rho = U and a truncation T. (ii) The finite over-paying MDP N_rho^T built exactly as SSZ Section 4.2 defines it (same states, actions and transition probabilities; compensation rewards from eq. (7) and the following display). (iii) A rational or outward-rounded interval average-reward dual certificate: a gain g < 0 and a bias vector h over all states of N_rho^T such that, for every state s and every action a allowed in s, r_rho(s,a) + sum_{s'} P(s'|s,a) h(s') - h(s) <= g. Here r_rho(s,a) is the expected one-step reward, the transition-probability-weighted w_rho(R_t, honest blocks accepted), including SSZ's truncation compensation. An independent checker rebuilds N_rho^T from the paper's formulas (not from the claimant's files), verifies every inequality, and concludes via SSZ Proposition 3 that max REV < rho. The checker must first reproduce SSZ Table 2's epsilon-OPT values 0.56808 (alpha = 0.425) and 0.66891 (alpha = 0.45) within one unit of their last printed digit with its own model builder. As a sanity test that the over-paying MDP is not mis-built, its own policy-iteration solve of N_rho^T at alpha = 0.45, rho = 0.66 must return a positive optimal gain. These safety margins compare against numerical published bars. If an incumbent is available as an exact certificate, any exactly certified strict improvement over it counts.

## Partial wins

- **p1:** An explicit stationary policy, given as an action table on a finite state set with 'adopt' at its boundary, whose relative revenue in the SSZ model at gamma = 0, computed in exact rational arithmetic from its Markov chain, exceeds 0.66894 + 1e-6 at alpha = 0.45 or 0.80184 + 1e-6 at alpha = 0.475. This is strictly above every published value (OSM 2016, PTO 2020), and those values are floating-point and uncertified.
- **p2:** The full certificate format at alpha = 0.4 or 0.425 (gamma = 0), with U below SSZ Table 2's upper bounds 0.48904 or 0.57226 by at least 1e-4.
- **p3:** A certified enclosure of width <= 1e-4 for the selfish-mining profitability threshold in the Ethereum PoW model of arXiv 2007.05614, Section 7 (gamma = 0.5, uncle and nephew rewards as defined there, REV_ARR objective). Equivalently, an exact policy profitable at alpha <= 0.2467, which would show the threshold is below the published 0.2468; that value was computed with forks capped at 20/25 in floating point.

## How a win is checked

Write an independent builder for N_rho^T from SSZ Section 4.2 (Python, under 300 lines; states (a, h, fork) with max(a, h) <= T). Load the claimed (rho, g, h). For every state-action pair, evaluate w_rho(s,a) + sum P h - h - g with fractions.Fraction, or mpmath intervals with outward rounding, and check that it is <= 0. Check g < 0. Then reproduce two calibration facts with the same builder. First, the under-paying MDP solved by policy iteration gives SSZ's epsilon-OPT values 0.56808 (alpha = 0.425) and 0.66891 (alpha = 0.45) within one unit of their last printed digit. Second, the optimal gain of N_rho^T is positive for rho comfortably below those values (e.g. rho = 0.56 at alpha = 0.425 and rho = 0.66 at alpha = 0.45), so no certificate can exist there. Cross-check model semantics against the Bitcoin model in the PTO repository and the OSM Matlab code. Minutes per alpha.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/1507.06183>

## Sources

- <https://arxiv.org/abs/1507.06183>
- <https://arxiv.org/abs/2007.05614>
- <https://arxiv.org/abs/2607.24415>
- <https://github.com/nirenzang/Optimal-Selfish-Mining-Strategies-in-Bitcoin>
- <https://github.com/roibarzur/pto-selfish-mining>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- The published upper bound may be loose for numerical rather than structural reasons. SSZ's Algorithm 1 reports rho' + 2(u + epsilon') from an epsilon'-optimal solver run. Start by certifying N_rho^T at T = 95 with an exact dual certificate before raising T.
- Certifier lens: solve N_rho^T in floating point by policy iteration, rationalise the bias vector, then repair it. Shift h by a small multiple of a Lyapunov-like function, or use exact policy evaluation of the final policy, until every inequality holds with margin. Binary-search rho downward.
- Raise T as needed: the over-paying compensation alpha(1-alpha)/(1-2alpha)^2 is 24.75 at alpha = 0.45 and 99.75 at alpha = 0.475, and Proposition 3 guarantees convergence as T grows. Use sparse structure (at most 3 successors per state-action).
- The lower side is a pure exact-evaluation problem: take PTO's or your own optimal truncated policy, compute its stationary revenue in rationals (or via a renewal-reward cycle decomposition), and push T to see if anything clears 0.66894 + 1e-6.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Model variants change the numbers. Use SSZ's gamma semantics (match needs a block prepared in advance), not Eyal-Sirer's SM1 or the 'uniform tie-breaking' variant (where SSZ's 0.2321 threshold lives), nor the gamma-minus/gamma-plus model of arXiv 2607.24415.
- Relative revenue is not time-averaged profit before a difficulty adjustment (Grunspan and Perez-Marco), and Ethereum's denominators include uncles. State the objective exactly as SSZ define REV.
- A truncated (under-paying) MDP gives only LOWER bounds. An upper bound must go through the over-paying construction or an equally rigorous dominance argument.
- Floating-point value iteration is not a certificate: every inequality must be checked exactly or with outward rounding, and the checker must build the MDP itself.
- The compensation rewards in eq. (7) are easy to transcribe wrongly (the PDF typesetting is dense). Test the builder by confirming that rho values below the known lower bounds cannot be certified.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/bitcoin-selfish-mining-revenue-bounds.md
```

Already set up? Say `run V3R1T4S on bitcoin-selfish-mining-revenue-bounds`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `bitcoin-selfish-mining-revenue-bounds`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
