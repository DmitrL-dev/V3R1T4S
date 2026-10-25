# Binary minimal codes for secret sharing: shorten the dimension 10–13 records

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours to laptop-days for structured generator-matrix search; exact minimality checking over at most 8191 nonzero messages takes seconds to minutes with GF(2) rank tests · open as of 2026-10-25

## The problem

Vladimir Chubenko and Sascha Kurz, Divisible Minimal Codes, Serdica Journal of Computing 18(2), 97–124 (issue year 2024; published 25 June 2025), Table 2, give m(10,2)=28–29, m(11,2)=31–35, m(12,2)=34–38 and m(13,2)=39–43. Here m(k,2) is the minimum length of a k-dimensional binary linear minimal code. Minimality means no distinct nonzero codewords have one support contained in the other. The paper relates these codes to secret sharing and uses generalized circulant constructions. Dimensions 7–9 are exact and excluded. An arXiv search on 2026-10-25 found no later values for these dimensions. This optimizes minimal-code length; the upstream codetables target optimizes Hamming minimum distance.

## What counts as a win

Give a full-rank binary generator matrix for a minimal [n,k] code with k=10 and n≤28, k=11 and n≤34, k=12 and n≤37, or k=13 and n≤42. The resulting code must satisfy minimality for all nonzero codewords. No divisibility, quasi-cyclic structure, projectivity or minimum-distance assumption beyond what follows from minimality is imposed. A valid dimension-10 construction would settle m(10,2)=28 using the published lower bound; the other cases improve a published upper bound. Also strictly improve the best comparable published result at claim time, including compatible compositions of published objects. State whether the candidate is a composition and identify its components. Values in unmerged pull requests do not set the bar.

## How a win is checked

Check that the supplied k-by-n matrix is binary and has rank k over GF(2). For every nonzero message a in GF(2)^k, compute c=aG and collect the columns of G at positions where c is zero. Their rank must be k−1. This is an exact minimality test: a codeword bG is supported within supp(c) precisely when b annihilates those columns; a one-dimensional kernel must be {0,a}. Independently cross-check by enumerating all nonzero codewords and rejecting any pair with a proper support inclusion. The rank version avoids a quadratic pair scan and uses at most 8191 small elimination problems. Check n against the corresponding record after validation.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://serdica-comp.math.bas.bg/index.php/serdicajcomputing/article/download/sjc.2024.18.97-124/pdf>

## Sources

- <https://serdica-comp.math.bas.bg/index.php/serdicajcomputing/article/download/sjc.2024.18.97-124/pdf>
- <https://doi.org/10.55630/sjc.2024.18.97-124>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Reproduce the paper’s generalized circulant constructions, then puncture, repair and replace columns while tracking low-rank hyperplane intersections.
- Use the exact rank criterion as a counterexample-guided search objective; each failing message gives a concrete missing-span constraint.
- Search small projective strong blocking sets in GF(2)^k with local trades and occasional exact repair; output a generator matrix for the final unrestricted check.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Good minimum distance alone does not imply minimality.
- Minimality concerns support inclusion, not the size of a generator matrix.
- The Ashikhmin–Barg sufficient weight-ratio condition is not necessary.
- The actual publication date is June 2025; the issue year is 2024.
- Later constructions and compatible combinations of published constructions must be checked before claiming. The lower bounds 28, 31, 34 and 39 come from codetables.de minimum-distance data and move if that table moves.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/binary-minimal-code-length-records.md
```

Already set up? Say `run V3R1T4S on binary-minimal-code-length-records`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `binary-minimal-code-length-records`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
