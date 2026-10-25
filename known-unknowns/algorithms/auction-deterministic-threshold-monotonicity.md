# Two-item auction determinism threshold: a density pair for which Thirumulanathan's c2*(c1) strictly decreases

⚡ **Algorithms** · standard · tractability ★★★☆☆ · compute: laptop-hours to laptop-days for polynomial-density search, algebraic root isolation and exact inequality certificates; a general positive proof requires additional analysis · open as of 2026-10-25

## The problem

D. Thirumulanathan, On Deterministic Optimal Mechanisms in a Two-Item Setting for Distributions with Nondecreasing Density (arXiv:2608.22371; Journal of Mathematical Economics, DOI 10.1016/j.jmateco.2026.103293), states in the footnote to Section 3.1 (after Theorem 5 and Figure 4): "Whether c*2 is an increasing function of c1 or not is still an open problem." This is the explicitly constructed sufficient threshold of Section 3.1, not the minimal true boundary of deterministic optimality. Fix normalized, strictly positive, nondecreasing C1 densities g_i on [0,b_i]. Values for the two items are independent with translated densities f_i(z)=g_i(z-c_i). For c=c1 in [0,1/g1(0)), write G(x)=integral_0^x g1(u)du and q(c) for the unique optimal single-item price, solving q-(1-G(q-c))/g1(q-c)=0. Define h1=1/[g2(0)G(q-c)], h2=[2+max_{0<=x<=q-c}(c+x)g1'(x)/g1(x)]/g2(0), and R=q(1-G(q-c)). The third threshold h3 is the unique h>=1/g2(0) for which, with t=G^{-1}(1/[h g2(0)]), integral_0^t (c+x)g1(x)dx/G(t)=R. Then c2*(c)=max(h1,h2,h3). Theorem 4 guarantees a deterministic separate-sale mechanism above this threshold. Uniform densities already give the increasing expression 2*b2*b1^2/(b1-c)^2. The threshold depends on g2 only through g2(0), so a counterexample is a question about g1. As of 2026-10-25 the arXiv abstract page lists v1 only. This entry asks for a certified counterexample (a strict decrease); a proof that c2* is increasing for every admissible density pair is outside this repository's scope.

## What counts as a win

An explicit admissible pair of densities (g1 on [0,b1] and g2 on [0,b2], each normalized, strictly positive, nondecreasing and continuously differentiable, as in Theorem 4 of arXiv:2608.22371), preferably polynomials with rational coefficients, and two shifts 0 <= c < c' < 1/g1(0) with certified values showing c2*(c) > c2*(c') strictly, where c2* = max(c2^th1, c2^th2, c2^th3) exactly as defined in Section 3.1 of the paper (the statement above restates the definitions in shifted coordinates). Every quantity that enters the comparison (the monopoly price q at each shift, the maximum in c2^th2, the root defining c2^th3) must be certified by exact algebra (Sturm sequences, isolating intervals with rational endpoints) or rigorous interval arithmetic, and the two enclosures of c2* must be strictly separated. Alternatively, a positive resolution counts only as a kernel-checked formal proof (Lean, Rocq/Coq or Isabelle, with no sorry, admit or extra axioms, and an axiom audit) that c2* is nondecreasing in the shift for the full density class of Theorem 4, stating whether 'increasing' is meant weakly or strictly and handling the equality case; a written or computer-assisted proof whose analytic steps are not formalised does not count. A strict decrease refutes monotonicity in both the weak and the strict sense. Before claiming, re-check arXiv and the journal version for a later answer.

## How a win is checked

Check normalization, strict positivity and nonnegative derivative of the claimed densities on their entire intervals. For polynomial examples use exact integration, Sturm sequences or rational Bernstein/SOS certificates. Isolate each monopoly-price root and prove it is the required global maximizer. Certify h2's global maximum by checking endpoints and every stationary point, not a grid. Isolate h3 using its defining equation and the source's uniqueness property, bound all three h values at both shifts, and verify a strictly separated max comparison. Such a fixed low-degree algebraic witness takes minutes to hours to check. For a formal positive proof, build it in a clean environment, print the axioms used, and check by reading that the formal c2^th1, c2^th2, c2^th3 and the density class match Section 3.1 and Theorem 4.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2608.22371>

## Sources

- <https://arxiv.org/abs/2608.22371>
- <https://arxiv.org/pdf/2608.22371>
- <https://doi.org/10.1016/j.jmateco.2026.103293>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Search positive monotone polynomial densities for g1. For fixed g2, its value g2(0) only rescales these three threshold expressions.
- Track switches between the three active thresholds. A plot of a single branch is not a plot of the maximum.
- Use floating point only to locate candidates; convert a candidate to a rational polynomial and obtain exact root and inequality certificates.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The threshold is sufficient and is explicitly not claimed tight. Changing the question to monotonicity of the true optimal-auction boundary is a different problem.
- Keep the densities fixed while translating their supports. Comparing different density shapes at different c is not a monotonicity counterexample.
- Do not cross the boundary c=1/g1(0); the expression has a prescribed domain and diverges at that boundary.
- A sampled decrease, unchecked stationary maximum, or approximate auction solve does not certify this question.
- A proof that c2* is increasing counts only as a kernel-checked formal proof for the full density class; a written argument or a check on sample densities is not a win.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/algorithms/auction-deterministic-threshold-monotonicity.md
```

Already set up? Say `run V3R1T4S on auction-deterministic-threshold-monotonicity`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `auction-deterministic-threshold-monotonicity`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
