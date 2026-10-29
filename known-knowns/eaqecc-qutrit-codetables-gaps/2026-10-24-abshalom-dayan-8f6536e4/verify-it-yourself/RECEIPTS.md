# Receipts

Real output of `sh verify-it-yourself/run_checks.sh` from this package folder (with the date, platform, compiler and
Python version printed before it and the timing after it):

```
2026-10-24T14:52:00Z
Darwin arm64
Apple clang version 21.0.0 (clang-2100.1.1.101)
Python 3.14.7
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
real 5.25
user 17.64
sys 0.34
exit=0
2026-10-24T14:52:06Z
```
