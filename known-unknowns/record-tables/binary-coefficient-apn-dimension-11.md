# Quadratic APN functions with coefficients in F2 in dimension 11: a seventh CCZ class

📊 **Record tables** · standard · tractability ★★☆☆☆ · compute: laptop-days for a bounded structured counterexample search; roughly four million derivative evaluations per APN check, with invariant checks in minutes to hours; full classification is out of scope · open as of 2026-10-25

## The problem

Yuyin Yu, Jingchen Li, Nadiia Ichanska and Nikolay Kaleyski, 'Construction of quadratic APN functions with coefficients in F2 in dimensions 10 and 11' (IACR ePrint 2024/1778; journal version doi:10.1007/s00200-025-00711-8), speed up the search of Yu, Kaleyski, Budaghyan and Li (dimensions up to 9), classify all quadratic APN functions over F_{2^10} with coefficients in F2, and, from partial computations over F_{2^11}, conjecture that the quadratic APN functions over F_{2^11} with coefficients in F2 'form 6 CCZ-inequivalent classes which also correspond to known APN functions' (ePrint abstract). The class is F(x) = sum over 0 <= i < j <= 10 of c_ij x^(2^i+2^j) with c_ij in {0,1}. APN means that for every nonzero a and every b the equation F(x+a)+F(x) = b has at most two solutions. The known quadratic APN functions of this form in dimension 11 include the Gold functions x^(2^k+1), k = 1..5 (pairwise CCZ-inequivalent), and x^3 + Tr(x^9); the paper's own table of class representatives must be read and used at claim time. As of 2026-10-25 a search found no result settling the conjecture. The target is one explicit function of this form in a seventh class, with a certificate; a full classification is not asked for.

## What counts as a win

An explicit F of the stated form (the list of pairs (i,j) with c_ij = 1) together with a stated irreducible degree-11 binary modulus, such that (1) F is APN, checked exhaustively over all 2047 nonzero a and all 2048 x; and (2) F is CCZ-inequivalent to every class representative listed in the paper (journal version, table of dimension-11 representatives) and to each of x^3, x^5, x^9, x^17, x^33 and x^3 + Tr(x^9), certified by an invariant that differs: for quadratic APN functions CCZ-equivalence reduces to EA-equivalence (Yoshiara, J. Algebraic Combin. 35 (2012) 461-475), and the differential spectrum and the extended Walsh spectrum of the ortho-derivative are EA-invariants of quadratic APN functions. The verifier recomputes these invariants for F and for every representative; F counts only if its invariant histogram differs from each of them. A different truth table, a failed equivalence search or the output of a heuristic classifier is not a certificate.

## How a win is checked

Specify an irreducible binary degree-11 modulus; independently verify irreducibility and build exact field arithmetic. Expand F and each reference function on all 2048 inputs. Check all 2047 nonzero differences and all 2048 inputs, requiring difference counts 0 or 2. For each a≠0, form the linear derivative x↦F(x+a)+F(x)+F(a)+F(0); its image has rank 10. Compute its unique nonzero orthogonal normal vector by GF(2) elimination to obtain the ortho-derivative. Recompute its full differential spectrum and component Walsh spectra. Compare invariant histograms with every reference. Any other inequivalence certificate must cite a published invariant theorem and replay exactly; a failed equivalence search never counts.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://eprint.iacr.org/2024/1778>

## Sources

- <https://eprint.iacr.org/2024/1778>
- <https://doi.org/10.1007/s00200-025-00711-8>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Adapt the paper’s reduced-matrix partial-search algorithm, concentrating on matrix patterns omitted by its restriction.
- Reject non-APN candidates after the first low-rank derivative, before constructing full invariants.
- Use symmetry and algebraic constructions to bias toward a new invariant signature rather than enumerate the full space.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Binary coefficients and dimension 11 are part of the conjecture; an APN function outside the class does not refute it.
- Equal spectra do not prove equivalence; a differing valid invariant does prove inequivalence.
- The ortho-derivative invariants need the quadratic-APN hypotheses (every derivative is 2-to-1 and affine).
- Failure of an equivalence program is not an inequivalence certificate.
- On 2026-10-25 the ePrint PDF and the Springer page were behind a bot check, so only the ePrint abstract was read for this entry; read the paper's dimension-11 table of representatives honestly before claiming, and treat its list as the comparison set.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/binary-coefficient-apn-dimension-11.md
```

Already set up? Say `run V3R1T4S on binary-coefficient-apn-dimension-11`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `binary-coefficient-apn-dimension-11`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
