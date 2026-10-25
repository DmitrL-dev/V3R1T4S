# Binary polynomial multiplication M(n): fewer AND/XOR gates than the best known circuit for n-term polynomials over GF(2)

⚡ **Algorithms** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours (straight-line-program heuristics and SAT-based local improvement on circuits of 100 to 8,000 gates; symbolic verification in seconds) · open as of 2026-10-25

## The problem

M(n) is the minimum number of two-input AND and XOR gates that multiply two n-term polynomials over GF(2), computing all 2n-1 product coefficients. Only upper bounds are known beyond tiny n. Bernstein's page 'Minimum number of bit operations for multiplication' (binary.cr.yp.to/m.html) tabulates upper bounds for n = 1..1000 from his 2009 work and earlier sources. Find and Peralta, 'Better circuits for binary polynomial multiplication' (IEEE Transactions on Computers 2019, doi:10.1109/TC.2018.2874662), improved many values and posted circuits for n <= 100 (BinPolMult.tar.gz, linked from Peralta's CMT page). NIST's Circuit Complexity list of circuits currently lists M(11) <= 186, M(12) <= 207, M(15) <= 312, M(16) <= 349, M(18) <= 454, M(19) <= 498 and M(20) <= 527 (checked 2026-10-25), and Peralta's CMT page lists M(10) <= 154 and the history of n = 15 (Bernstein 329, Cenk and Hasan 317, Peralta 312). De Piccoli, Visconti and Rizzo, 'Polynomial multiplication over binary finite fields: new upper bounds' (Journal of Cryptographic Engineering 10 (2020) 197-210), give further upper bounds; it is paywalled and its values must be checked before claiming. The frontier is spread over these sources, so the bar for a given n is the minimum over all of them.

## What counts as a win

Success means an explicit straight-line program over GF(2) for some 2 <= n <= 100, with inputs f0..f(n-1), g0..g(n-1), each line a two-input AND or XOR of earlier values (no constants, no other gate types), and designated outputs h0..h(2n-2), that a symbolic checker confirms computes every h_k = sum_{i+j=k} f_i g_j exactly, and whose gate count is STRICTLY LESS (direction: min) than the minimum for that n over: Bernstein's table (binary.cr.yp.to/m.html), the NIST list of circuits, the circuits on Peralta's CMT page and in BinPolMult.tar.gz (each recounted with the verifier's own counter), the tables of Find and Peralta (2019), the values of De Piccoli, Visconti and Rizzo (2020), and any later value found by a literature search at verification time. If a paywalled source cannot be read, the claim is PENDING TABLE CHECK until a human has read it. The bar also includes the best valid composition of published circuits for the same n under the same gate count; state whether the candidate is a composition and name its components and composition rule. Values in unmerged pull requests are not bars.

## Partial wins

- **p1:** The same kind of strict improvement for some 101 <= n <= 1000 over Bernstein's table and every later published value for that n (Cenk-Hasan 2015 and De Piccoli-Visconti-Rizzo 2020 must be checked), with priority to cryptographic sizes such as n = 113, 127, 128, 131, 163, 193, 233, 239, 251, 256, 283, 409 and 571.
- **p2:** An exact value: for some n >= 3 with no published optimality proof (check the literature first), a SAT encoding of 'n-term binary polynomial multiplication with at most M - 1 AND/XOR gates', where M is the current best upper bound, shown unsatisfiable with a proof accepted by a formally verified checker (cake_lpr), together with a short argument that the encoding is complete for circuits of that size.

## How a win is checked

Parse the program and evaluate it symbolically in the Boolean polynomial ring: represent each wire as the set of monomials it computes over the 2n input variables (XOR = symmetric difference, AND = product reduced with x*x = x), and compare each designated output with sum_{i+j=k} f_i g_j. This is exact and runs in seconds for n <= 100 because these circuits stay bilinear. Count gates (each AND or XOR line is one; renaming or outputting an existing wire is free). Calibrate the counter by recounting Peralta's published circuits for n = 10, 11, 12, 15 and 16 (154, 186, 207, 312 and 349 gates) and Bernstein's straight-line code for one n. Re-fetch the reference pages before claiming. Recompute comparison compositions using the same checker and resource metric.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://csrc.nist.gov/Projects/circuit-complexity/list-of-circuits>

## Sources

- <https://binary.cr.yp.to/m.html>
- <https://csrc.nist.gov/Projects/circuit-complexity/list-of-circuits>
- <http://www.cs.yale.edu/homes/peralta/CircuitStuff/CMT.html>
- <http://www.cs.yale.edu/homes/peralta/CircuitStuff/BinPolMult.tar.gz>
- <https://doi.org/10.1109/TC.2018.2874662>
- <https://doi.org/10.1007/s13389-019-00210-w>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Polish the linear layers: a Find-Peralta circuit is a top XOR layer, an AND layer and a bottom XOR layer; each XOR layer is a shortest-linear-program problem where heuristics newer than the 2019 circuits (Boyar-Peralta with all ties explored, Tan-Peyrin, cancellation-allowing searches) often shave gates.
- SAT-based local improvement (Kulikov et al., 'SAT-based circuit local improvement', 2021): cut windows of 6 to 12 gates out of a record circuit and ask a SAT solver for a smaller equivalent subcircuit; repeat over thousands of windows in parallel.
- Change the bilinear formula, not only its wiring: other choices of the products with the same number of AND gates (Montgomery's five-, six- and seven-term formulae, enumerations of optimal bilinear formulae) can have cheaper linear layers.
- Recursion bookkeeping for composite n: combine the best k-term formula with the best m-term circuits for every split of n and count shared XORs across recursive calls (Bernstein's refined Karatsuba overlap); sweep all splits automatically for n <= 100 and propagate improvements upward.
- A win at n = 64 or 128 (carry-less multiplication, GHASH) or at a NIST binary-curve size is the one practitioners would notice.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Conventions differ between sources (some circuits on these pages use XNOR or constants); this entry counts only two-input AND and XOR gates, so recount every reference circuit with the same counter.
- The frontier is spread over several sources (2009-2020), one of them paywalled; take the minimum per n and keep a claim PENDING TABLE CHECK until every source is checked.
- Sources are not monotone in n or in date: a later paper can be worse than an earlier one for a given n.
- Random-input testing is not a proof for larger n; use the symbolic check.
- Depth is not part of this record.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/algorithms/binary-polynomial-multiplication-gates.md
```

Already set up? Say `run V3R1T4S on binary-polynomial-multiplication-gates`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `binary-polynomial-multiplication-gates`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
