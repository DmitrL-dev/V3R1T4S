# Entanglement-assisted qutrit code `[[28, 7, 14; 11]]_3` (table: `13-19`)

## What

object/eaqecc_28_7_14_11.json (sha256 8f6536e49eecf331) defines, from its 32 x 56 GF(3) symplectic stabilizer matrix S alone, a non-catalytic qutrit EAQECC with s = 32, c = rank(S J S^T)/2 = 11, k = 7 and exact minimum symplectic distance d = 14 over span(S)^perp outside span(S) ∩ span(S)^perp, which is strictly above d_lower = 13 and at most d_upper = 19 of the listed cell (n,k,c) = (28,7,11), shown as [[28,7,13-19;11]]_3 on the eaqecc.codetables.de qutrit table copy fetched 2026-10-24T12:58:19Z (footer "Last change: 10.07.2025") and re-fetched byte-identical at 2026-10-24T14:48:11Z.

Note: the sentence above is quoted word for word from `panel/gate.md` (the CRITERION skeptic's `confirmed_scope`).
The gate re-read the page once more at 2026-10-24T14:50:19Z: same page hash, same cell
(`the-record-we-beat/README.md`). The object's full SHA-256 is
`8f6536e49eecf3311af7ed4869dc270efad791545c86fff9627be2aa44ab97e4`.

The code comes from the extended one-point Hermitian code `E_14` on `y^3 + y = x^4` over GF(9): a `[28, 12, 14]_9`
code with Hermitian hull dimension 6. Multiplying its first coordinate by `w` (an element of norm -1) lowers the
hull to 5, which gives `[[28, 12 - 5, 14; 28 - 12 - 5]]_3`. The object holds the GF(9) generator `G9`, its Hermitian
dual `D9`, and the stabilizer matrix `S = phi(D9)` over GF(3).

## Check it yourself

From this package folder, run:

```sh
sh verify-it-yourself/run_checks.sh
```

- **Requirements:** `python3` (standard library only) and a C compiler (`cc`).
- **Rough laptop time:** about 10 seconds with 4 free cores (5.3 s measured, see `verify-it-yourself/RECEIPTS.md`).
- **Expected last line:** `PASS`

It computes `s`, `c` and `k` from `S`, checks every one of the 37,442,160 sets of 13 positions by exact GF(3) ranks
(no vector of `span(S)^perp` outside the isotropic part fits inside any of them, so `d >= 14`), and checks an explicit
weight-14 vector of `span(S)^perp` outside `span(S)` (so `d <= 14`). `RUN_IT_YOURSELF.md` has the expected output and a
second, independent check: the full enumeration of all 3^24 vectors of `span(S)^perp` (about 18 CPU-minutes), which
finds `d = 14` with 79,488 vectors of that weight.

## Compared to

| table | cell | table value | our value | URL | fetched (UTC) |
|---|---|---|---|---|---|
| Grassl, Bounds on the minimum distance of entanglement-assisted qutrit quantum codes (`Last change: 10.07.2025`) | `(n=28, k=7, c=11)` | `[[28,7,13-19;11]]_3` (`d_lower = 13, d_upper = 19`) | `[[28, 7, 14; 11]]_3` (`d = 14`) | https://eaqecc.codetables.de/qutrit.php | 2026-10-24T14:50:19Z |

Details, HTTP headers, page hash and the listed `(28, 7)` row are in `the-record-we-beat/README.md`.

Published codes that the table does not list: the plain one-point Hermitian EA codes of length 27 (Christensen,
Munuera, Pereira, Ruano) imply, through the table's own propagation rules, at most `d = 13` at `(28, 7, 11)`.

## Not claimed

- Optimality for `(n=28, k=7, c=11)` is not claimed; the table's upper bound is 19.
- Only cell `(n=28, k=7, c=11)` is claimed in this package (one cell per package). Cells that follow from it by the
  table's propagation rules (for example `[[29, 7, 14; 11]]_3` by lengthening) are not claimed here.
- This is an improvement of the table cell, not a new technique: changing the Hermitian hull by scaling columns is
  known, and the code is the hull-lowered member of `E_14`. The unscaled `E_14` gives `[[28, 6, 14; 10]]_3` (at that
  cell the table reads d = 12, inherited from `[[28,6,12-19;8]]_3` by its rule for unlisted c), from which this code follows by the table's "increasing dimension" rule; the two are not
  independent results, and `[[28, 6, 14; 10]]_3` is not claimed here.
- Catalytic setting: the table's own note says that in the catalytic setting `[[n,k,d;c]]` with `c >= k > 1` gives
  `[[n,k-1,d;c-1]]`, so the listed `[[28,8,14;12]]_3` would give these parameters catalytically. The table and this
  claim are non-catalytic (c is computed from `S`); against the known non-catalytic `[[28,7,14;12]]_3` this code
  saves one entangled pair.
- The classical `[28, 12, 14]_9` code is not ours: `codetables.de` has listed a `[28,12,14]_9` algebraic-geometry
  code since 2003. What is new is the qutrit EA code obtained from the extended code's Hermitian hull.
- Not yet submitted to or listed by the table maintainer (`eaqecc.codetables.de`).
- Not peer reviewed; verified by a three-skeptic panel (`panel/`) and by the standalone checker in
  `verify-it-yourself/`.

## Credits

- **Markus Grassl**, maintainer of the online EAQECC bounds tables (https://eaqecc.codetables.de/ and
  https://eaqecc.codetables.de/qutrit.php) and `codetables.de` (https://codetables.de/).
- **Gaojun Luo, Martianus Frederic Ezerman, Markus Grassl, and San Ling**, "Constructing quantum error-correcting
  codes that require a variable amount of entanglement", *Quantum Information Processing* 23, 4 (2024),
  https://doi.org/10.1007/s11128-023-04211-x (preprint https://arxiv.org/abs/2207.05647), whose Hermitian
  construction (Proposition 1) turns a GF(9) code with a given Hermitian hull into the qutrit EA code, and whose
  propagation rules the table uses.
- **Todd A. Brun, Igor Devetak, and Min-Hsiu Hsieh**, "Correcting quantum errors with entanglement", *Science* 314,
  436-439 (2006), https://arxiv.org/abs/quant-ph/0610092.
- **Carlos Galindo, Fernando Hernando, Ryutaroh Matsumoto, and Diego Ruano**, "Entanglement-assisted quantum
  error-correcting codes over arbitrary finite fields", *Quantum Information Processing* 18, 116 (2019),
  https://arxiv.org/abs/1812.05312.
- **Christensen, Munuera, Pereira, and Ruano**, entanglement-assisted quantum codes from one-point Hermitian codes,
  https://arxiv.org/abs/2105.02166 (Advances in Mathematics of Communications 17(1), 2023): the length-27 family
  this code extends, and the comparison above.
- **V. D. Goppa** (algebraic-geometry codes) and **Henning Stichtenoth** (Hermitian codes), whose distance bound
  gives `d >= 28 - m` for the extended code `E_m`.
- Contributor credit: Abshalom Dayan, using the V3R1T4S kit (https://github.com/elder-plinius/V3R1T4S).
