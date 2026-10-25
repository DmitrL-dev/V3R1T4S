# CRITERION skeptic verdict: claim [31,18,10] over GF(9), cell codetables.de q=9 n=31 k=18

context: subagent (Claude Agent tool, model claude-opus-5-5), given only claim/

## Bottom line

The claim meets clauses (1), (2) and (3) of the success criterion. Clause (4) holds as far as I could check it. The code is rebuilt entry by entry from a classical Hermitian-curve Construction X recipe by my own program, with nothing taken from LinCodeEvolve. I did not search the literature for LinCodeEvolve (arXiv:2609.37056) or newer arXiv claims; that is the NOVELTY skeptic's job.

- The minimum distance is exactly 10. Four exhaustive methods agree. Three are the claim's own: a column-subset test, an affine-subset certificate and Brouwer-Zimmermann. The fourth is mine and written independently: I enumerated all 9^13 dual codewords and applied the exact MacWilliams transform. It gives the full weight distribution: A_1..A_9 = 0 and A_10 = 24864.
- The live cell, read once at 2026-10-24T13:47:25Z, still shows lower bound 9 and upper bound 12. So 9 < 10 <= 12.
- No partial win is claimed, and none is needed. This is a full-criterion claim for one code.

## Run log (UTC)

| Time (date -u) | Step | Result |
|---|---|---|
| 13:39:43 | start, read claim/ | — |
| 13:43:14 | `rebuild/build_code.py` in mine/claim_copy | rebuilt.json sha256 = 0dc7555b8c9c50d09aa8d729be15230dfacad9168e0a197f87b3c67c9ef1e54f, the same as object/code_q9_n31_k18_d10.json |
| 13:43:26 to 13:43:31 | `checkers/m3_mindist.c` (cc -O2), 5.4 s | rank=18; W=1..9 no word (W=9: all 20160075 subsets); `d=10 witness_weight=10` |
| 13:43:26 to 13:43:41 | `checkers/subset_cert.c 27 9`, 14.8 s | `subsets=4686825 nonzero_nullspaces=465105 max_dim=1 words_le_W=0 min_weight_seen=10` |
| 13:43:26 to 13:44:39 | `checkers/bz9w.c` (cc -O3), 72.9 s | `K=18 n=31 d=10 sets=18,12,1 maxw=7 words=26962471566` |
| 13:44:51 | mine/my_gf9.py rank / construction / dual | rank(G)=18; rank on the 27 affine columns = 18; rebuilt G differs from the object in 0 entries; the [4,3] tail has minimum weight 2 (all 728 words); H is 13 x 31, rank 13, G H^T = 0 |
| 13:46:05 | test of mine/dualwd.c + mine/macwilliams.py on a random [12,5] code | MacWilliams result equals brute-force enumeration (59049 words): `matches brute force: True` |
| 13:46:12 | positive control: mine/dualwd on the dual of the code punctured at column 30 ([30,18]) | d=9, A_9=4032 (so the pipeline does detect weight-9 words) |
| 13:46:23 to 13:46:45 | **main run**: mine/dualwd on H (13 x 31), 6 threads, nice 10, 22.5 s | 317733228541 normalized dual words = (9^13-1)/8, as expected; every A_i is an integer >= 0; sum A = 9^18; **A_1..A_9 = 0, d = 10, A_10 = 24864** (mine/main_macwilliams.out) |
| 13:46:59 to 13:47:47 | positive control: the claim's checkers on the punctured [30,18] code | m3 `d=9`; subset_cert `words_le_W=199728 min_weight_seen=9`; bz9w `d=9` |
| 13:47:12 | both weight-10 witnesses (m3 and bz9w) checked with my own solver (mine/my_witness.py) and with `checkers/witness_check.py` | both are consistent, mG = w, weight 10 |
| 13:47:25 | the single live GET of the cell page (mine/live/) | HTTP 200, 3395 bytes, sha256 1ab4ec8f7b8516b1..., byte-identical to table/bklc_q9_n31_k18.html; "lower bound: 9", "upper bound: 12", "last modified: 2001-12-17" |
| 13:48:31 | baseline (component codes, mine/base_*) | C(D,20P) = [27,18,7] (A_7=2160); C(D,17P) = [27,15,10] (A_10=17280) |

## Clause by clause

**(1) Rank exactly k over GF(q), computed independently: MET.**
Three programs give rank 18: m3 (C), `checkers/witness_check.py` (Python), and mine/my_gf9.py. My program uses its own arithmetic: log/antilog tables built from a primitive element, found by polynomial multiplication with w^2 -> w + 1. It is self-tested on all 9^3 triples for associativity and distributivity. The field convention is the JSON's: GF(3)[w]/(w^2 - w - 1), with a + b*w stored as a + 3b. w^2 - w - 1 has no root in GF(3), so this really is GF(9). Every entry of G is in 0..8. The code is truly [31,18], with no rank deficiency.

**(2) Exact d, with the method the criterion requires: MET.**
- *Is full enumeration "feasible"?* The criterion asks for "full enumeration of all q^k - 1 nonzero codewords when feasible (2^k <= ~2^32)". Here q^k - 1 = 150094635296999120, about 2^57.06 words. The parenthetical says 2^k, and read character by character, 2^18 <= 2^32 would make enumeration "feasible". But the parenthetical is a word-count budget written for q = 2. For q = 9, the count is 2^25 times over that budget: about 4.8 core-years at 1e9 words/s. So I read q = 9, k = 18 as the "large k" branch, which asks for two independent exact implementations that agree and never sampling.
- *The claim's methods.* All three are exhaustive; I read the code, and none samples.
  - m3 tests every W-subset of all 31 coordinates for W <= 9. It uses the left kernel of the systematic form.
  - subset_cert tests every 9-subset of the 27 affine coordinates. It computes the null space exactly and weighs every vector in it.
  - bz9w is Brouwer-Zimmermann with disjoint fresh information sets 18, 12 and 1, and bit-sliced GF(3) planes. The lower bound at w=7 is 8+2+0 = 10 = best found. Its word count, 26962471566 = 3 x sum_{w=1..7} C(18,w) 8^(w-1), matches the algorithm.
  - Each counts Hamming weight over GF(9) symbols (any nonzero component), not GF(3) components or bits.
  - On independence: m3 and subset_cert share the support-covering principle and the same author's field-table formula, so they are only partly independent. bz9w uses a different algorithm and a different vector arithmetic. m3 + bz9w therefore meet "two independent exact implementations that agree".
- *My own exact method.* It is a different algorithm, code and arithmetic, and it is the dual/MacWilliams route the criterion itself names. It enumerates every dual codeword up to scalars and returns the complete weight distribution of the code, so it carries the same information as full enumeration. Result: d = 10 exactly.
- Positive controls on the punctured [30,18] code, whose true d = 9, show that every method detects weight-9 words. The checkers do not just print 10.

**(3) d strictly greater than the live lower bound, and at most the upper bound: MET at 2026-10-24T13:47:25Z.**
- Right cell: the URL has q=9&n=31&k=18, and the page heading is "Bounds on linear codes [31,18] over GF(9)". It shows lower bound 9 and upper bound 12, so 9 < 10 <= 12.
- The claim package holds only a copy from 2026-10-24T12:09:31Z (table/RECORD.md). My one GET, about 1.6 h later, returned a byte-identical page. The table entry is still the 2001 shortened-BCH [31,18,9], so the LinCodeEvolve results have not raised this cell.
- **The gate must still do its own live re-read at its verification time.** My read does not stand in for that.

**(4) Not a LinCodeEvolve code or derived from one, and no newer arXiv claim reaching d=10: met as far as checkable here; literature not checked.**
- My own program rebuilds G with 0 differing entries from the stated recipe. The recipe:
  - C(D,17P) ⊂ C(D,20P), one-point codes on y^3 + y = x^4 over GF(9). There are 27 affine points; the monomials x^i y^j (j <= 2) are ordered by pole order 3i+4j.
  - A Reed-Solomon [4,3] tail (points 0, 1, -1, w), with columns 2 and 3 scaled by w, sits on the three rows of pole order 18, 19 and 20.
- This is a classical algebraic-geometry Construction X. Nothing in it is taken from another code.
- What I could not check:
  - the 7 LinCodeEvolve codes;
  - whether this code is equivalent to one of them;
  - whether any arXiv paper (or older literature such as the Xing-Ling AG constructions cited on the page) already has a [31,18,>=10] code over GF(9).
  These go to the NOVELTY skeptic.

## Hidden quantifiers, stretched definitions, null model

- **"binary" in the target name.** The target is called codetables-binary-linear. Its pitfalls say "GF(2) arithmetic", and its feasibility rule is written as 2^k. But the criterion text says "over GF(q)" and "the live cell for (q,n,k)" throughout. Read literally, q = 9 is admitted. If the bank owner meant binary codes only, this claim is outside the intended target. It must always be described as a GF(9) record, never as a binary one.
- **Hamming weight.** It counts GF(9) symbols in all four methods (checked in the code).
- **Bundling or partial wins.** The claim is one code and one cell. p1 (quantum) and p2 (upper bound) are not claimed. rebuild/gf9lib.py contains unused Hermitian-dual and symplectic helpers, but no quantum claim is made, so none is credited.
- **Null model.** This is a deterministic exact claim, so no statistical null model applies. The relevant baseline is the textbook Construction X bound, min(d(C(D,17P)), d(C(D,20P)) + d(tail)) = min(10, 7 + 2) = 9. I computed both components exactly. That bound equals the table's 9. The +1 is therefore not given by the generic bound: it depends on the specific tail and rests wholly on the exact computation. The four methods confirm it. One example: the bz9w witness has affine weight 7 and tail weight 3.
- **Overflow.** Field operations are table lookups reduced mod 3. Counters are 64-bit (the largest dual count is 6.6e10). MacWilliams is done in exact Python integers, with integrality and nonnegativity of every A_i asserted.

confirmed_scope: The 18 x 31 matrix G in object/code_q9_n31_k18_d10.json (sha256 0dc7555b8c9c50d0, GF(9) = GF(3)[w]/(w^2-w-1) with a + 3b encoding) has rank 18 and generates a linear [31,18,10] code over GF(9) with exact minimum distance 10 (A_10 = 24864, no nonzero word of weight <= 9). This is strictly above the lower bound 9 and within the upper bound 12 of the codetables.de cell q=9, n=31, k=18, as read live at 2026-10-24T13:47:25Z, the page being byte-identical to the claim's table copy fetched 2026-10-24T12:09:31Z; novelty against LinCodeEvolve (arXiv:2609.37056) and later arXiv work was not checked here.

## Concerns

1. The gate must re-read the live cell at its own verification time. The claim package carries only the 12:09:31Z copy, and my 13:47:25Z read is not the gate's read.
2. Clause (4) literature novelty is unverified by me and depends on the NOVELTY skeptic.
3. Scope wording: the result is over GF(9). It would be a stretch of the target's "binary" name to report it as a binary-code record.
4. The 2^k parenthetical in clause (2), read character by character, would demand full enumeration of 9^18 words. I read it as a binary-written word-count budget. In any case, my dual/MacWilliams computation gives the full weight distribution exactly, so the result does not hinge on that reading.

pass: true
