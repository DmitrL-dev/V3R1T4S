#!/bin/sh
# Run from the package folder: sh verify-it-yourself/run_checks.sh   (last line: PASS or FAIL)
# Needs python3 (standard library only) and a C compiler (cc). About 10 seconds on one core.
V=verify-it-yourself; O=object/code_q9_n31_k18_d10.json; W="$V/tmp_work"; rm -rf "$W"; mkdir -p "$W"
fail() { echo "$1"; rm -rf "$W"; echo FAIL; exit 1; }
cc -O2 -o "$W/m3_mindist" "$V/m3_mindist.c" || fail "could not compile m3_mindist.c"
python3 "$V/check_code.py" prepare "$O" "$W/code.txt" || fail "object malformed or rank deficient"
"$W/m3_mindist" < "$W/code.txt" > "$W/m3.out" || fail "m3_mindist failed"
cat "$W/m3.out"
python3 "$V/check_code.py" verdict "$O" "$W/m3.out" || fail "parameters do not match the claim"
rm -rf "$W"; echo PASS
