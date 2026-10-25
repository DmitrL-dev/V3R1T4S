# PREREG (frozen 2026-10-24T12:24:27Z, before any checker of this run has been run on the [31,18]_9 code)

null_test: not needed because the claim is one explicit generator matrix checked by deterministic exact checkers against a table value (no search statistic, no "beats chance" claim)

## Criterion (verbatim, bank entry codetables-binary-linear)

Success means a k x n generator matrix over GF(q) with these properties. (1) Rank is exactly k over GF(q), computed independently. (2) The exact minimum distance d is computed by full enumeration of all q^k - 1 nonzero codewords when feasible (2^k <= ~2^32), or, for large k (or large k with small n-k, via the dual and MacWilliams identities), by two independent exact minimum-distance implementations that agree; never by sampling. (3) d is STRICTLY GREATER (direction: max) than the lower bound in the live http://www.codetables.de/ cell for (q,n,k) at verification time, and at most the upper bound. (4) The code is not one of the 7 LinCodeEvolve codes (arXiv:2609.37056) or a code derived from them, and no newer arXiv claim already reaches that d.

## Object

A JSON file with q = 9, n = 31, k = 18, the field representation (GF(9) = GF(3)[w]/(w^2 - w - 1), element a + b w
stored as a + 3b) and the 18 x 31 generator matrix G over GF(9). It is the classical code of run 2026-10-24-1033's
Construction X object X(17,20,4): C(D,17P) inside C(D,20P) (27 affine points of y^3 + y = x^4 over GF(9)) plus a
Reed-Solomon [4,3] tail. Column scalings by nonzero constants do not change any weight, so the claim object is the
unscaled code.

## Statistic and checkers

- Rank: Gaussian elimination over GF(9), written in this run (no shared code with the builders).
- Minimum distance, exact, by three methods (q^k = 9^18 is far beyond full enumeration, so criterion (2) asks for two
  independent exact implementations that agree):
  (M1) bz9 / bz9w, the Brouwer-Zimmermann programs of run 2026-10-24-1033 (tested against brute force there);
  (M2) subset_cert of run 2026-10-24-1033: every codeword of weight <= 9 vanishes on the complement of some 9-subset
       of the 27 affine coordinates, so checking the kernel of all C(27,9) = 4686825 such restrictions is a complete
       certificate;
  (M3) a new checker written in this run from the definition, with a different field encoding and different code:
       for every 9-subset T of all 31 coordinates, the codewords vanishing outside T; no nonzero one means no word
       of weight <= 9. Plus an explicit codeword of weight 10 (a row combination, checked by multiplication), which
       pins d = 10 exactly.
  Each checker is tested before it judges the claim on a known positive (a code of known minimum distance) and a
  known negative (a seeded code with a low-weight word, or a claimed d that is too high).

## Thresholds

1. Rank exactly 18, computed, not copied.
2. At least two of M1, M2, M3 run on the claim object and agree on d; none of them samples.
3. d > the live lower bound and d <= the live upper bound of the codetables.de cell for (q,n,k) = (9,31,18), on a
   live re-read of https://www.codetables.de/BKLC/BKLC.php?q=9&n=31&k=18 (one honest GET) before claiming.
4. Not one of the 7 LinCodeEvolve codes (arXiv:2609.37056) or derived from them; no newer arXiv or other published
   claim found that already reaches d = 10 for [31,18] over GF(9) (already-settled lens and NOVELTY skeptic).
5. One cell per claim. Neighbor cells reached by shortening, puncturing or extension are listed as not claimed.
6. A tie (d = 9) is not a win.

## Search space record

Every search records its exact family and whether it was exhausted (uncapped) or capped. Sampled searches are
never used as exclusions.
