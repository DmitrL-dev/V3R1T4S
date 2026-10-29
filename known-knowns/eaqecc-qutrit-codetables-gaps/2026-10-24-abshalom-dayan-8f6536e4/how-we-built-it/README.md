# How we built it

- `build_obj.py m out.json d_claimed [columns scaled by w]`: builds the claim JSON from the extended one-point
  Hermitian code E_m (`hermitian.py`: points and monomials of y^3 + y = x^4 over GF(9); `gf9lib.py`: GF(9)
  arithmetic, Hermitian dual, phi map to GF(3)). This object: `python3 build_obj.py 14 out.json 14 0` (E_14, column 0
  multiplied by w), byte-identical to `object/eaqecc_28_7_14_11.json`.
- `PREREG.md`: the frozen plan of the run that panelled this claim (run 2026-10-24-1253). `PREREG_found_run.md`: the
  frozen plan of the run that found it and kept it as a candidate (run 2026-10-24-1033). No null test: an explicit object checked
  by deterministic exact checkers against a table value.
