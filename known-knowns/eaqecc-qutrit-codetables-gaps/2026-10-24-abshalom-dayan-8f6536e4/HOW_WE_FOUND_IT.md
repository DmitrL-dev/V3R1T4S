# How we found it

contributor text, unverified

The family is the one behind this workspace's earlier [[28,5,15;11]]_3: the extended one-point codes E_m on the
Hermitian curve y^3 + y = x^4 over GF(9) (the 27 affine points plus a coordinate for the point at infinity), which
reach the best known distance 28 - m. An [n, kappa, d]_9 code with Hermitian hull dimension l gives an
[[n, kappa - l, d; n - kappa - l]]_3 code (Luo, Ezerman, Grassl and Ling, arXiv:2207.05647, Prop. 1).

E_14 is a [28,12,14]_9 code with hull 6, which gives [[28,6,14;10]]_3; at (28,6,10) the table reads d = 12, inherited from
[[28,6,12-19;8]]_3 by its rule for unlisted c. Multiplying
one affine column by w (an element of norm -1) lowers the hull to 5 and gives [[28,7,14;11]]_3, where the table
lists d_lower = 13. An earlier run the same day found it while scanning the family against the table and kept it as a
panel-ready candidate; this run rebuilt it byte for byte, wrote a new exact checker (the position-subset rank test in
verify-it-yourself/), tested that checker on a known positive, seeded negatives and 244 random brute-force cases,
reran the full 3^24 enumeration, and sent a claim folder to a three-skeptic panel, one skeptic at a time.

What failed, looking for something stronger at the same cell: two-point and three-point Hermitian divisors
(a P_inf + b P_0 + c P_1, all divisor classes up to symmetry at the relevant degrees) all sit exactly on the Goppa
bound, and none reaches a larger Hermitian hull than E_m (exhaustive over all 2^27 column sign patterns). So no
d >= 15 at (28,7,11) from these families.
