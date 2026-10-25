# ⚡ Algorithms

Fast matrix multiplication schemes and other algorithmic records.

**13 open problems**, easiest first. Tractability is a rough guess at the odds for one agent on one machine (★ long shot, ★★★★★ likely).

| Odds | Problem | Kind | Compute |
|---|---|---|---|
| ★★★☆☆ | [AdderBoard: smallest transformer (fewest unique parameters) adding two 10-digit numbers](adderboard-smallest-adder-transformer.md) | harvest | laptop-hours |
| ★★★☆☆ | [Binary polynomial multiplication M(n): fewer AND/XOR gates than the best known circuit fo…](binary-polynomial-multiplication-gates.md) | harvest | laptop-hours (straight-line-program heuristics and SAT-based local improvement on circuits of 100 to 8,000 gates; symbolic verification in seconds) |
| ★★★☆☆ | [Fast matrix multiplication: beat a best-known rank in the Lille FMM catalogue for a small…](fmm-catalogue-small-format-rank.md) | harvest | laptop-hours |
| ★★★☆☆ | [Fast matrix multiplication: best-known rank with ternary/integer coefficients where only…](fmm-ternary-integer-ring-upgrade.md) | harvest | laptop-hours |
| ★★★☆☆ | [Fast matrix multiplication: fewer additions for a fixed best-known rank (straight-line pr…](fmm-additive-complexity-records.md) | harvest | laptop-hours |
| ★★★☆☆ | [Minimum-comparison selection: settle V8(16) in {28, 29}, or beat the new n = 17 upper bou…](selection-min-comparisons-n16-n17.md) | harvest | laptop-hours to laptop-days (single-threaded proof-number or depth-first construction search in Rust, many workers in parallel; certificates check in seconds; refuting a budget is far more expensive than finding an algorithm) |
| ★★★☆☆ | [NIST Circuit Complexity AES tables: a smaller or shallower {AND, XOR, XNOR} circuit for t…](nist-aes-circuit-records.md) | harvest | laptop-days for the search (SAT and heuristic linear-layer optimisation, basis enumeration); verification takes seconds |
| ★★★☆☆ | [Shorter addition chains for elliptic-curve field and scalar inversion exponents (Curve255…](ecc-inversion-addition-chains.md) | harvest | laptop-hours (laptop-days for the field-inversion cells); verification takes milliseconds |
| ★★★☆☆ | [Two-item auction determinism threshold: a density pair for which Thirumulanathan's c2*(c1…](auction-deterministic-threshold-monotonicity.md) | standard | laptop-hours to laptop-days for polynomial-density search, algebraic root isolation and exact inequality certificates; a general positive proof requires additional analysis |
| ★★☆☆☆ | [Multiply two 8-term binary polynomials with 25 products (NIST open problem), or a smaller…](gf2-polymult-8term-25-products.md) | standard | laptop-days (flip-graph or SAT search over rank-25 decompositions); verification takes milliseconds |
| ★★☆☆☆ | [Packomania csqv: circles in the unit square with maximised sum of radii (AlphaEvolve prob…](packomania-csqv-sum-of-radii.md) | harvest | laptop-hours |
| ★☆☆☆☆ | [MOONSHOT - 4x4 matrices with 47 multiplications in characteristic 0, or 3x3 matrices with…](fmm-4x4x4-rank47-3x3x3-rank22.md) | moonshot | laptop-hours |
| ★☆☆☆☆ | [Regret matching+ inside CFR+/PCFR+: does alternating predictive RM+ converge ergodically?…](alternating-prm-plus-ergodic-convergence.md) | standard | pure thought plus a formalisation effort (exact rational simulation of candidate games helps find the argument) |

← [All categories](../README.md)
