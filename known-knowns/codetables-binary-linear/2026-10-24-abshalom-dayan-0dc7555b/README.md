# Linear code `[31, 18, 10]` over GF(9) (table: lower bound `9`)

## What

The 18 x 31 matrix G in object/code_q9_n31_k18_d10.json (sha256 0dc7555b8c9c50d0, GF(9) = GF(3)[w]/(w^2-w-1) with a + 3b encoding) has rank 18 and generates a linear [31,18,10] code over GF(9) with exact minimum distance 10 (A_10 = 24864, no nonzero word of weight <= 9). This is strictly above the lower bound 9 and within the upper bound 12 of the codetables.de cell q=9, n=31, k=18, as read live at 2026-10-24T13:47:25Z, the page being byte-identical to the claim's table copy fetched 2026-10-24T12:09:31Z; novelty against LinCodeEvolve (arXiv:2609.37056) and later arXiv work was not checked here.

Note: the sentences above are quoted word for word from `panel/gate.md` (the CRITERION skeptic's `confirmed_scope`).
"Not checked here" refers to that skeptic: the panel's NOVELTY skeptic did check LinCodeEvolve (binary codes only)
and the 2024-2026 literature, and found nothing reaching `[31,18,>=10]` over GF(9) (`panel/novelty.md`). The gate
re-read the cell once more at 2026-10-24T13:49:51Z: same page hash, same bounds (`the-record-we-beat/README.md`).
The object's full SHA-256 is
`0dc7555b8c9c50d09aa8d729be15230dfacad9168e0a197f87b3c67c9ef1e54f`.

The code is a Construction X on the Hermitian curve `y^3 + y = x^4` over GF(9): the one-point codes
`C(D,17P) ⊂ C(D,20P)` on the 27 affine points (`[27,15,10]` inside `[27,18,7]`), with a `[4,3]` Reed-Solomon tail on
the 3 extra rows. The textbook Construction X bound gives only `min(10, 7 + 2) = 9`; the true distance 10 comes from
the specific tail and rests on exact computation (five exact methods agree, see `panel/`).

This is a GF(9) result. The bank target is named `codetables-binary-linear`, but its success criterion is stated for
GF(q); this code is not a binary code.

## Check it yourself

From this package folder, run:

```sh
sh verify-it-yourself/run_checks.sh
```

- **Requirements:** `python3` (standard library only) and a C compiler (`cc`).
- **Rough laptop time:** about 10 seconds on one core (7.7 s measured, see `verify-it-yourself/RECEIPTS.md`).
- **Expected last line:** `PASS`

It checks the rank, then examines every set of at most 9 of the 31 coordinates (all 20,160,075 9-subsets) exactly
over GF(9) and finds no nonzero codeword supported inside any of them, then prints a codeword of weight 10 and checks
that it lies in the row space. Expected output and a second independent check are in `RUN_IT_YOURSELF.md`.

## Compared to

| table | cell | table value | our value | URL | fetched (UTC) |
|---|---|---|---|---|---|
| Grassl, Bounds on the minimum distance of linear codes (codetables.de) | `q=9, n=31, k=18` | lower bound 9, upper bound 12 (`[31,18,9]`, shortened BCH subcode, last modified 2001-12-17) | `[31,18,10]` (`d = 10`) | https://codetables.de/BKLC/BKLC.php?q=9&n=31&k=18 | 2026-10-24T13:49:51Z |

Details, HTTP headers, page hash and the neighboring cells are in `the-record-we-beat/README.md`.

## Not claimed

- Optimality is not claimed; the table's upper bound is 12.
- Only cell `(q, n, k) = (9, 31, 18)` is claimed (one cell per package). Codes derived from it (shortened `[30,17,10]`,
  subcode `[31,17,10]`, `[32,18,10]` by a zero column) only tie the table and are not claimed. Punctured codes have
  `d = 9` (`[30,18,9]`, a tie).
- No quantum or entanglement-assisted code is claimed here.
- Not yet submitted to or listed by the table maintainer (codetables.de).
- Not peer reviewed; verified by a three-skeptic panel (`panel/`) and by the standalone checker in
  `verify-it-yourself/`.

## Credits

- **Markus Grassl**, maintainer of the code tables at https://codetables.de/, whose cell this improves; the upper
  bound there comes from **Andries E. Brouwer**'s tables.
- **N. J. A. Sloane, S. M. Reddy and C.-L. Chen**, "New binary codes", IEEE Transactions on Information Theory 18
  (1972), 503-510: Construction X.
- **V. D. Goppa** (algebraic-geometry codes) and **Henning Stichtenoth** (Hermitian codes), whose one-point codes on
  the Hermitian curve are the two nested codes used here.
- **I. S. Reed and G. Solomon**, Reed-Solomon codes (the `[4,3]` tail).
- Contributor credit: Abshalom Dayan, using the V3R1T4S kit (https://github.com/elder-plinius/V3R1T4S).
