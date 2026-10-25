# MINLPLib finance and marketing instances still open: beat saa_2 (strategic asset allocation) or close pricing050 (product pricing) with a certificate

🚚 **Optimization benchmarks** · standard · tractability ★★☆☆☆ · compute: laptop-hours (saa_2 has 4,408 variables and 400 binaries but may reduce to a few asset weights plus a funding scalar; pricing050 has 50 continuous variables) · open as of 2026-10-25

## The problem

MINLPLib, maintained by Stefan Vigerske, publishes feasible points and solver-reported dual bounds for each instance; minlplib.solu's '=bestdual=' uses the third-best solver bound. On 2026-10-25: saa_2 (asset management, MBNLP, minimise, in the library since 2001) has best point p4 = 12.1613089 and dual bounds up to 6.02323546 (GUROBI; =bestdual= 1.9954875180); pricing050 (marketing, NLP, maximise, added 2024; source Mohammadreza Kiaghadi; references Davarnia 2021 and Davarnia and van Hoeve 2021) has best point p1 = -1813.829078 and dual bounds down to -1534.3281 (SCIP; =bestdual= -1153.003281), a gap of 15.4% of the primal value against the best solver bound. The target is a better feasible point, or an independently checkable global certificate. A solver status line is not a certificate.

## What counts as a win

A point file in MINLPLib's text .sol format ('varname value' lines for the nonzero variables, omitted variables read as 0, in the variable space of the posted instance) for saa_2 or pricing050 such that an evaluator written independently from the instance as currently posted at https://www.minlplib.org/gms/<name>.gms (cross-checked against the .py or .nl version) reports: (a) every variable within its bounds and every binary exactly 0 or 1; (b) maximum absolute violation over all algebraic constraints <= 1e-8 in double precision, confirmed with 50-digit mpmath; (c) an objective, recomputed from the model (saa_2: objvar = x4407, minimise; pricing050: objvar = -sum c_i x_i, maximise), strictly better than the '=best=' value for that instance in https://www.minlplib.org/minlplib.solu AND the best primal bound on https://www.minlplib.org/<name>.html, both re-fetched live immediately before claiming, by more than 1e-6 * max(1, |best|). As of 2026-10-25 the bars are saa_2 < 12.1613089 (min) and pricing050 > -1813.829078 (max). The evaluator must first reproduce the posted best point of the same instance (https://www.minlplib.org/sol/<name>.p<k>.sol: saa_2 p4 = 12.1613089, pricing050 p1 = -1813.829078) within one unit of the last printed digit of the reference objective, and must reject a deliberately perturbed copy. Point file, evaluator, instance sha256 and page snapshots are saved together. Sending a point to the MINLPLib maintainer is an action for the human. The displayed incumbents and the stated objective margin are numerical. Keep that margin for comparison to printed numerical values. If the incumbent is reconstructed exactly and candidate feasibility and objective are certified exactly, any strict improvement over that exact incumbent counts.

## Partial wins

- **p1:** A machine-checkable certificate that the optimum of pricing050 is at most the best known primal value plus 1e-6 * |value|. Example: (i) an interval-arithmetic (directed-rounding) proof that each of the 250 univariate terms a * x * exp(-b * x^p) is concave on [0,10]; and (ii) multipliers lambda in R^5_+ whose Lagrangian dual value, with each of the 50 separable univariate maximisations bounded rigorously by interval branch-and-bound, is within that tolerance of the primal point. This closes an instance MINLPLib lists as open (against the best solver bound, SCIP -1534.3281, the gap is 15.4% of the primal value).
- **p2:** A certified lower bound on the optimal value of saa_2 strictly above 6.02323546 (the best solver-reported dual bound on 2026-10-25, GUROBI). It must come with a re-runnable certificate: for example an interval branch-and-bound over the 5-asset weight simplex and the funding scalar, whose leaf log a skeptic can re-check in under 24 h on a laptop.
- **p3:** Certified global optimality of the best saa_2 point: a certificate as in partial win p2 whose lower bound is within 1e-6 relative of the best primal value. This closes an instance open since it was added in 2001, even if 12.1613089 turns out to be optimal.
- **p4:** The full success criterion met on any other MINLPLib instance whose application field is Portfolio Optimization, Financial Optimization, Asset Management or Marketing, provided that no solver-reported dual bound on its instance page is within 1e-6 relative of its best primal value at claim time.

## How a win is checked

Download https://www.minlplib.org/gms/<name>.gms (and the .py/.nl versions from the same site for cross-checking) and the posted best point https://www.minlplib.org/sol/<name>.p<k>.sol. pricing050 is a 6-equation model; a 40-line Python evaluator reproduces p1 = -1813.829078 with violation <= 1e-8. saa_2 is GAMS scalar format: parse its 6,206 equations (products of linear factors, bilinear terms and linear rows), or load the Pyomo .py version, set all variable values from the .sol file, and evaluate every constraint body. Reproduce p4 = 12.1613089 first. For certificates: re-run the interval computations with an independent library (mpmath.iv or python-flint/arb) and check that every leaf of the branch-and-bound log is covered. Re-fetch minlplib.solu and the instance page with plain curl before claiming.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.minlplib.org/minlplib.solu>

## Sources

- <https://www.minlplib.org/instances.html>
- <https://www.minlplib.org/instancedata.csv>
- <https://www.minlplib.org/minlplib.solu>
- <https://www.minlplib.org/bounddates.html>
- <https://www.minlplib.org/doc.html>
- <https://www.minlplib.org/index.html>
- <https://www.minlplib.org/download.html>
- <https://www.minlplib.org/saa_2.html>
- <https://www.minlplib.org/pricing050.html>
- <https://www.minlplib.org/gms/pricing050.gms>
- <https://www.minlplib.org/sol/pricing050.p1.sol>
- <https://www.minlplib.org/gms/saa_2.gms>
- <https://www.minlplib.org/sol/saa_2.p4.sol>
- <https://optimization-online.org/wp-content/uploads/2020/03/7681.pdf>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- saa_2 is low-dimensional underneath. Fix the five weights w and the funding scalar, and every other variable (scenario wealths, products, shortfall binaries) is determined. So the true search is over a 4-simplex times an interval. Build a fast exact evaluator of 'minimal feasible funding given w', then run dense multistart or Lipschitz/interval branch-and-bound over the simplex. Either beat 12.1613089, or certify it (saa2-close). The 200 scenarios are monthly compounding paths, so precompute per-scenario polynomial coefficients.
- Read saa_2 as a chance-constrained portfolio. The binaries pick which scenarios may miss each liability date. Enumerate or cut over 'which scenarios fail' with a MILP master for fixed weights, and wrap it in a simplex search.
- pricing050: test the convexity reading first (interval second derivatives of x*exp(-b*x^p) on [0,10]). If it holds, any local NLP solve plus KKT multipliers gives the Lagrangian certificate. Separability means the dual function is a sum of 50 one-dimensional maximisations that can be bounded rigorously.
- Make the evaluator the deliverable: an independent MINLPLib point checker (GAMS-free) is itself useful and makes every claim cheap to audit.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The instance listing's gap and minlplib.solu's '=bestdual=' use the third-best solver bound, so they overstate how open an instance is. Check every solver bound on the instance page; some instances look open in the listing but are effectively closed.
- Solver-reported dual bounds are not certificates (the FAQ says they come 'from some run with some option settings on some machine'). A certified bound must carry its own checkable proof.
- pricing050 is a maximisation and saa_2 a minimisation. saa_2's objective variable is objvar = x4407 (equation e4003); do not read another variable as the objective.
- Tolerance games: MINLPLib accepts points with infeasibility <= 1e-8 absolute. An 'improvement' obtained by pushing degree-12 polynomial constraints to the edge of that tolerance is not a win; require the 1e-6 relative margin and an mpmath re-check.
- If pricing050 is convex (unproven), its posted point is probably already optimal and a primal 'record' there is a bug signal. Aim that cell at the closing certificate.
- Use the instance currently posted at minlplib.org (it is revised; the removed-instances archive holds older versions with the same names).

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/optimization-benchmarks/minlplib-finance-open-instances.md
```

Already set up? Say `run V3R1T4S on minlplib-finance-open-instances`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `minlplib-finance-open-instances`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
