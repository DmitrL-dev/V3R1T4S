# Run it yourself

From this package folder, in a fresh shell (needs python3, standard library only, and cc; no network):

    sh verify-it-yourself/run_checks.sh

Expected output (about 10 seconds with 4 free cores; 5.3 s measured, see verify-it-yourself/RECEIPTS.md):

    n=28 s=32 c=11 k=7 dim_isotropic=10 dim_dual=24
    {"n": 28, "s": 32, "c": 11, "k": 7, "dim_perp": 24, "dim_isotropic": 10, "D9_herm_orthogonal_to_G9": true, "rowspace_S_equals_phi_D9": true}
    W=13 part=0/4 total_subsets=37442160 examined=9360540 with_vector_outside_isotropic=0
    W=13 part=1/4 total_subsets=37442160 examined=9360540 with_vector_outside_isotropic=0
    W=13 part=2/4 total_subsets=37442160 examined=9360540 with_vector_outside_isotropic=0
    W=13 part=3/4 total_subsets=37442160 examined=9360540 with_vector_outside_isotropic=0
    T=[0, 1, 2, 3, 4, 5, 6, 7, 8, 11, 17, 20, 23, 27]
    v_x=2 0 1 0 2 2 0 2 2 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 2
    v_z=0 1 0 2 1 0 2 1 0 0 0 2 0 0 0 0 0 1 0 0 2 0 0 1 0 0 0 0
    symplectic_weight=14 orthogonal_to_all_rows_of_S=True in_span_S=False support=[0, 1, 2, 3, 4, 5, 6, 7, 8, 11, 17, 20, 23, 27]
    ok:   parameters computed from S
    ok:   computed n=28 s=32 c=11 k=7; claimed n=28 k=7 c=11
    ok:   GF(9) description consistent with S
    ok:   all parts of the W=13 subset test present
    ok:   examined 37442160 of C(28,13) = 37442160 subsets
    ok:   no vector of span(S)^perp outside the isotropic part on <= 13 positions (found 0)
    ok:   witness of symplectic weight 14 outside span(S), claimed d=14
    computed d=14; claimed d=14
    PASS

What it does:
- gf3prep.py (standard library) computes s = rank(S), c = rank(S J S^T)/2, k = n - s + c, a basis of
  N = span(S)^perp and of the isotropic part I = span(S) ∩ N, from S alone.
- check_eaqecc.py prepare checks the object's GF(9) description (D9 is Hermitian-orthogonal to G9 and
  rowspace(S) = phi(D9)).
- subset_ea.c examines every one of the C(28,13) = 37442160 sets T of 13 positions and compares, by exact GF(3)
  ranks, the dimension of the vectors of N supported inside T with that of the vectors of I supported inside T.
  They are equal for every T, so no vector of N outside I has symplectic weight <= 13: d >= 14.
- witness.py finds, inside the given 14 positions, a vector of N that is not in span(S) (so not in I), of
  symplectic weight 14: d <= 14.
- verdict.py compares every computed value with the claim in the JSON.

Why the subset test is complete: a vector of N outside I with weight <= 13 is supported inside some 13-set T; for
that T the vectors of N supported in T then include one outside I, so dim N_T > dim I_T. Conversely, any T with
dim N_T > dim I_T holds such a vector. The program checks the condition through incremental elimination of the
basis restricted to the positions outside T (both the x and z column of each position).

A second, independent exact check (full enumeration of all 3^24 = 282429536481 vectors of span(S)^perp, about
18 CPU-minutes, 4 parallel parts):

    cc -O3 -o enum_min verify-it-yourself/enum_min.c
    python3 verify-it-yourself/check_eaqecc.py prepare object/eaqecc_28_7_14_11.json enum.basis > enum.results
    for p in 0 1 2 3; do ./enum_min $p 4 < enum.basis > enum.part$p & done; wait
    cat enum.part0 enum.part1 enum.part2 enum.part3 >> enum.results
    python3 verify-it-yourself/check_eaqecc.py verdict object/eaqecc_28_7_14_11.json enum.results

Expected last lines: `computed n=28 k=7 c=11 d=14 (79488 words of weight d; enumerated 282429536481 vectors, 3^24 =
282429536481); claimed n=28 k=7 c=11 d=14` and `D9 Hermitian-orthogonal to G9: True; rowspace(S) = phi(D9): True`.
(The docstring of check_eaqecc.py mentions 3^22, from the earlier package it was written for; the code enumerates
3^(2n - s) = 3^24 here.)

Rebuild the object from scratch:

    python3 how-we-built-it/build_obj.py 14 rebuilt.json 14 0
    shasum -a 256 rebuilt.json object/eaqecc_28_7_14_11.json   # both 8f6536e49eecf3311af7ed4869dc270efad791545c86fff9627be2aa44ab97e4
