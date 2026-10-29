# REPRODUCE skeptic: [[28,7,14;11]]_3 claim

context: subagent (Claude Agent tool, model claude-opus-5-5), given only claim/

## Bottom line

Confirmed. I wrote my own exact checker from the definition before reading anything under claim/checkers/ or claim/rebuild/ (and before opening claim/REPRODUCE.md). Working from S alone, it gives n = 28, s = 32, rank(S J S^T) = 22, so c = 11 and k = 7. It also gives dim N = 24 and dim I = 10, and **d = 14 exactly**, with 79488 vectors of weight 14 in N \ I.

The method was a full enumeration of every vector of N \ I, with no sampling. Every claimed value matches: n = 28, k = 7, c = 11, d = 14. The author's rebuild reproduces the object byte for byte (sha256 8f6536e4...ab97e4). The author's two checkers give exactly the outputs that claim/REPRODUCE.md documents, and those agree with mine. My own GF(9) check confirms that G9 and D9 are consistent with S. The author's argument for why the subset test is complete holds when I re-derive it.

Scope: I did not check the live or saved table cell (d_lower = 13, d_upper = 19). That is another skeptic's job, and I made no network access. The result d = 14 satisfies 13 < 14 <= 19 only if those table values are correct.

## Definition used (quoted from claim/CLAIM.md, success criterion)

> "with s independent generators on Alice's n qutrits, c = rank(S J S^T)/2 (half the rank of the symplectic commutation matrix) and k = n - s + c; the minimum distance d, computed exactly as the minimum weight of vectors in the symplectic dual of span(S) that are not in the isotropic part span(S) ∩ span(S)^perp (the EAQECC definition used by Grassl)"

Conventions, from the object JSON field `S_convention`:

> "S rows are (x|z) over GF(3), 2n columns; symplectic form <(x|z),(x'|z')> = x.z' - z.x' (J = [[0,I],[-I,0]])"

Symplectic weight of (x|z) is the number of positions i with (x_i, z_i) != (0,0).

## My method (mine/gf3.py, mine/enum.c, mine/run.py) and why it is exact

- **Linear algebra (mine/gf3.py), exact mod 3:**
  - s = rank(S).
  - K_ij = <s_i, s_j>, and c = rank(K)/2.
  - N is the null space of the functionals v -> <s_i, v>; the coefficient vector of each is (-z_i | x_i).
  - I = { aS : aK = 0 }. This is exactly span(S) ∩ N, because <aS, s_j> = (aK)_j.
  - A complement C is chosen so that N = I ⊕ C.
  - Asserts: every N and I vector is orthogonal to every row of S, I ⊆ N, and dim N = 2n - s.
  - Cross-check: dim(span S ∩ N) = 32 + 24 - rank(S ∪ N) = 32 + 24 - 46 = 10.
- **Enumeration (mine/enum.c, bitsliced GF(3)):**
  - Every v in N \ I can be written uniquely as v = c + i, with c a nonzero vector in span(C) and i in I.
  - Nonzero scalars preserve weight and map N \ I to itself. So c runs over the (3^14 - 1)/2 = 2391484 projective representatives (leading nonzero coefficient 1), and i runs over all 3^10 = 59049 vectors of I.
  - Each projective point of N \ I is therefore visited exactly once, 141214738716 points in all. Each vector count is 2 x the histogram value.
  - Size check: 3^24 is about 2.8e11, which is feasible. The run took 30 s on 6 cores.
  - The GF(3) adder is self-tested on all 9 input pairs at startup.
- **Checks on the output:**
  - The visited counts equal the expected counts.
  - The reported minimum vector is re-checked in Python straight from the definition: orthogonal to all rows of S, not in span(S), and the right weight.
  - All weight-14 vectors were dumped and each one re-checked from the definition. Membership in span(S) used an ordinary parity check H of span(S), which is a computation separate from the one that builds I.
  - The full weight distribution passes a MacWilliams test. With A = dist(N \ I) + dist(I), the transform with alphabet 9 per position gives a distribution that is integral and nonnegative, sums to 3^32, and has B_0 = 1.

## Tests of my checker

- **Brute force on random small S (mine/smalltest.py):** n from 2 to 6, random row counts, and some rows forced dependent. The brute force ranges over all of GF(3)^{2n}:
  - s comes from |span S| and rank(K) from |span K|.
  - N is found by testing every vector; I = N ∩ span(S).
  - The reference values are d and the count of minimum-weight vectors.
  - Results: 12 cases at 13:53:40 UTC, then 120 cases from 13:53:51 to 13:53:56 UTC. **132 of 132 OK, 0 failures.** Brute-force d values were 1, 2, 3 and 4, plus 24 cases where N \ I is empty; dim I ranged from 0 to 3.
- **Positive control (planted low weight, n = 28; mine/control.py make-planted):**
  - S' = S with each row adjusted by a multiple of a vector u, so that the weight-3 vector v0 = 0000010000000000002000010000|0000010000000000000000010000 lies in span(S')^perp and not in span(S').
  - Prep gives s = 32, c = 12, k = 8, dim N = 24, dim I = 8.
  - Enumeration from 13:57:13 to 13:57:42 UTC gives **d = 3, with 2 vectors (±v0)**. The planted vector was found.
- **Degenerate control (exclusion of I, n = 28; mine/control.py make-degen):**
  - S'' = S + [v], where v is a weight-14 vector of N \ I. This makes v isotropic, so it must now be excluded.
  - Prep gives s = 33, c = 11, k = 6, dim N = 23, dim I = 11. I'' now holds 4 vectors of weight 14.
  - The expected number of weight-14 vectors in N'' \ I'' is 27674, computed from the verified weight-14 dump by the definition.
  - Enumeration from 13:57:03 to 13:57:13 UTC gives **d = 14, with exactly 27674 vectors**.
- **Determinism:** I ran the main enumeration twice, once plain at 13:54:33 to 13:55:03 UTC and once with the dump at 13:56:02 to 13:56:38 UTC. The per-worker histograms were identical.

## My numbers for the claimed object (command output)

- **13:54:25 UTC:**
  - Object sha256: 8f6536e49eecf3311af7ed4869dc270efad791545c86fff9627be2aa44ab97e4, matching claim/CLAIM.md.
  - prep output: `{"n": 28, "s": 32, "rankK": 22, "c": 11, "k": 7, "dimN": 24, "dimI": 10, "dimC": 14}`
- **13:55:03 UTC (mine/main_combine.txt):**
  - `outer visited 2391484 expected 2391484 inner 59049 expected 59049`
  - `projective points of N\I visited 141214738716 expected 141214738716`
  - Weight distribution of N \ I (vectors): 14: 79488, 15: 939680, 16: 4675320, 17: 24025464, 18: 130746736, 19: 539726088, 20: 1921352864, 21: 5907822192, 22: 14996858352, 23: 31303436912, 24: 52185741352, 25: 66787536888, 26: 61653168824, 27: 36534838952, 28: 10438528320. There are no vectors of weight 1 to 13.
  - `d = min weight over N \ I = 14 ; number of weight-d vectors: 79488`
  - Example (checked: orthogonal to all rows of S True, in span(S) False, weight 14): `2200002102101200000000210120|0220001110000000000000000000`
  - Weight distribution of I: 0: 1, 15: 64, 18: 536, 19: 1536, 20: 2128, 21: 4608, 22: 9120, 23: 14464, 24: 15536, 25: 8064, 26: 2992. The minimum nonzero weight of I is 15, so the minimum over all of N \ {0} is also 14.
  - sum A = 282429536481 = 3^24. The MacWilliams dual is integral and nonnegative, sums to 1853020188851841 = 3^32, and has B_0 = 1. It implies span(S) has minimum weight 10, with 25728 vectors of that weight.
- **13:56:42 UTC, dump re-check:** `dumped projective vectors: 39744 distinct up to scalar: 39744 weights seen: [14] failing definition: 0 => vectors (x2): 79488`.
- **Supports of the weight-14 vectors:** 9936 distinct supports, with exactly 4 projective GF(3) vectors per support, which is 8 vectors and matches the 8 nonzero GF(9) multiples.

Summary, mine against the claim:

| quantity | mine | claimed |
|---|---|---|
| n | 28 | 28 |
| s | 32 | (32 implied) |
| c | 11 | 11 |
| k | 7 | 7 |
| dim N | 24 | – |
| dim I | 10 | – |
| d | 14 | 14 |
| number of weight-14 vectors | 79488 | – |

## Author's steps, run in a copy (mine/claimcopy/) after my result

I read claim/REPRODUCE.md at 13:58:03 UTC and read every checker and rebuild file before running any of them. They make no network calls and write only to the outputs they name. Step 5 (the live table) was skipped, since no network is allowed.

- **Step 1, 13:58:35 UTC.** `E_14 scaled_cols=[0] [28,12] hull=5 -> [[28,7,?;11]]  S 32x56  D9 16x28`. rebuilt.json has sha256 8f6536e49eecf3311af7ed4869dc270efad791545c86fff9627be2aa44ab97e4, the same as object/, and `cmp` found the files identical.
- **Step 2, 13:58:35 to 13:58:54 UTC.**
  - `n=28 s=32 c=11 k=7 dim_isotropic=10 dim_dual=24`.
  - W = 13: all four parts examined 9360540 of 37442160 subsets each, with `with_vector_outside_isotropic=0`.
  - W = 14: the four parts give 2474, 2494, 2494, 2474, out of 40116600 subsets. The total, 9936, equals my count of distinct weight-14 supports.
- **Step 3, 13:59:05 UTC.** `symplectic_weight=14 orthogonal_to_all_rows_of_S=True in_span_S=False` on T = {0,1,2,3,4,5,6,7,8,11,17,20,23,27}. That support is among my 9936.
- **Step 4, 13:59:11 to 14:05:37 UTC, on 4 cores.**
  - The parts give `d=14` with counts 28620, 19734, 20832 and 10302.
  - Verdict: `computed n=28 k=7 c=11 d=14 (79488 words of weight d; enumerated 282429536481 vectors, 3^24 = 282429536481); claimed n=28 k=7 c=11 d=14`, `D9 Hermitian-orthogonal to G9: True; rowspace(S) = phi(D9): True`, exit 0.
  - The 79488 count is the same as mine. The author's method shares no code with mine: it walks a ternary Gray code over all 3^24 vectors, while mine enumerates projective points of C × I.
- **My own GF(9) check (mine/gf9check.py, 14:06:14 UTC).**
  - G9 has rank 12 and D9 has rank 16 over GF(9). Every row of G9 is Hermitian-orthogonal to every row of D9, so D9 = G9^perpH.
  - S equals [phi(r); phi(w r)] over the rows r of D9, row by row.
  - phi(G9) has GF(3) rank 24 and is symplectically orthogonal to S, so it equals span(S)^perp.
  - The Hermitian Gram matrix of G9 has rank 7, so the hull has dimension 5. That matches k = 12 - 5 = 7 and c = 28 - 12 - 5 = 11.
  - I regenerated G9 from the construction text with my own GF(9) code: 27 affine points, 12 monomials with pole orders 0,3,4,6,...,14, a last coordinate, and column 0 scaled by w. It equals the JSON's G9 exactly.

## Re-derivation of "Why the subset test is complete"

Let N_T = {v in N : supp(v) ⊆ T} and I_T = I ∩ N_T. Both are subspaces, and I_T ⊆ N_T.

1. **Soundness.** Take v in N \ I with weight w <= 13. Then |supp(v)| <= 13 <= n = 28, so supp(v) lies inside some 13-subset T. That gives v in N_T and v not in I_T, so N_T ≠ I_T, which means dim N_T > dim I_T.
2. **Converse.** If dim N_T > dim I_T, there is a u in N_T \ I_T. This u is in N. It is not in I, because u in I would put it in I ∩ N_T = I_T. Its weight is at most 13. So "for every 13-subset, dim N_T = dim I_T" is equivalent to "N \ I has no vector of weight <= 13", which is d >= 14.
3. **Computing the dimensions.** Let B be a basis of N, D = 24 rows, with the first dI = 10 rows a basis of I.
   - The map a -> aB is injective, and aB is supported in T exactly when (aB) restricted to the x and z columns of the positions outside T (OUT) is zero.
   - So dim N_T = D - rank(B|OUT), and likewise dim I_T = dI - rank(B_I|OUT).
   - The test dim N_T > dim I_T becomes rank(B|OUT) - rank(B_I|OUT) < D - dI. This holds exactly when some non-I row becomes dependent on the rows before it during incremental elimination, which is the condition claim/checkers/subset_ea.c checks.
4. **The code is correct.**
   - The incremental elimination in claim/checkers/subset_ea.c works. Each stored pivot row is zero at all earlier pivot columns, so reducing a row by the pivots in order never brings back a column already cleared. A reduced row that is nonzero is independent of the pivots. Taking the smallest-index pivot with a nonzero coefficient in a supposed dependence gives a contradiction.
   - All four cases of the clearing step are right: 1-1, 1+2, 2-2 and 2+1.
   - The OUT mask covers both the x bits and the z bits.
   - The combination generator visits all C(28,13) = 37442160 subsets, and the four parts partition them; 4 x 9360540 checks.
   - The input basis puts I first and spans exactly span(S) ∩ N. I confirmed dim I = 10 independently.
5. **Upper bound.** The witness has weight 14 and lies in N \ I, so d <= 14. With step 2, d = 14. The W = 14 run is also consistent: once d = 14, any 14-subset that holds a vector of N \ I is exactly that vector's support, so the 9936 subsets should equal my 9936 distinct supports, and they do.

## Concerns (none affect the verdict)

- I did not verify the table values (d_lower = 13, d_upper = 19 for (28,7,11)); that check belongs to another skeptic. The claim "strictly above d_lower, at most d_upper" depends on those values.
- One cosmetic issue: the docstring of claim/checkers/check_eaqecc.py mentions "3^22 vectors", but the enumeration actually covers 3^24. The code and its output use 3^24 correctly.
- No safety guard blocked any command. Every job I started (logged in mine/pids.log) ran in the foreground with `wait` and with `nice -n 10`, on at most 6 cores, and all of them had finished before I wrote this file.

pass: true
