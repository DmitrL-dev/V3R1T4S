# How we built it

The code was found by a Construction X scan run for a different table (entanglement-assisted qutrit codes), then
compared with the classical codetables.de cell for [31,18] over GF(9).

- `xscan.py`: Construction X on nested plain one-point Hermitian codes C(D,aP) ⊂ C(D,bP) (27 affine points of
  y^3 + y = x^4 over GF(9)) with a Reed-Solomon tail; for each code the exact minimum distance (by `bz9t`, a
  Brouwer-Zimmermann program built from `bz9t.c`) and the Hermitian hull. Usage:
  `python3 xscan.py cells.csv ./bz9t 9 15` (cells.csv lists the qutrit table cells; it is not part of this
  package because only the scan's bookkeeping uses it). Its output line for this code was
  `X(a=17,b=20,l=4) [31,18,10] hull 5 signs ++-- -> [[31,13,10;8]] newly beats 1: (31,18,13) 10>9`.
  Helpers: `hermitian.py` (curve points), `gf9lib.py` (GF(9) arithmetic), `closure_exact.py` (table propagation
  rules for the qutrit table), `find_hull0.py` (column scalings for the qutrit claim; not needed for the classical
  code).
- `build_code.py`: rebuilds exactly the object in `object/` from the construction:
  `python3 build_code.py out.json` (the output has the same sha256 as `object/code_q9_n31_k18_d10.json`).
- Exact distance programs used before the panel: `bz9w.c` (64-bit Brouwer-Zimmermann; `cc -O3 -o bz9w bz9w.c`,
  input "k n" then the rows on stdin) and `subset_cert.c` (`cc -O2 -o subset_cert subset_cert.c`;
  `./subset_cert 27 9 < code.txt` examines all 9-subsets of the 27 affine coordinates and finds no word of weight
  <= 9). The package's own checker is in `verify-it-yourself/`.
- `PREREG.md`: the frozen plan of the run that panelled this claim (run 2026-10-24-1223). `PREREG_scan_run.md`:
  the frozen plan of the run whose scan found the code (run 2026-10-24-1033, written for the qutrit table).
  No null test: an explicit object checked by deterministic exact checkers against a table value.
