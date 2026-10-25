"""Rebuild the [31,18]_9 Construction X code of the claim from its construction and write it as JSON.

C(D,17P) inside C(D,20P): plain one-point codes of the Hermitian curve y^3 + y = x^4 over GF(9), rows x^i y^j
(j <= 2, pole order 3i + 4j) evaluated at the 27 affine points (ordered by x, then y, in the a + 3b encoding).
Rows of pole order <= 17 (15 rows) get 4 zero tail columns; the 3 rows of pole order 18, 19, 20 get a
Reed-Solomon [4,3] tail: row t has e^t at tail column e = 0..3 (0^0 = 1), and tail columns 2 and 3 are multiplied
by w (sign pattern ++--; scaling a column never changes a weight).
Usage: python3 build_code.py out.json"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hermitian import pts, pw   # noqa: E402
from gf9lib import MUL          # noqa: E402

a, b, l, signs = 17, 20, 4, "++--"
mons = sorted([(i, j) for j in range(3) for i in range(30) if 3 * i + 4 * j <= 26], key=lambda t: 3 * t[0] + 4 * t[1])
rows = [[MUL[pw(x, i)][pw(y, j)] for x, y in pts] for i, j in mons]
pole = [3 * i + 4 * j for i, j in mons]
Ka = sum(1 for p in pole if p <= a)
Kb = sum(1 for p in pole if p <= b)
r = Kb - Ka
sg = [1 if s == "+" else 3 for s in signs]          # 3 encodes w
tail = [[MUL[sg[e]][pw(e, t) if not (e == 0 and t == 0) else 1] for e in range(l)] for t in range(r)]
G = [rows[i] + [0] * l for i in range(Ka)] + [rows[Ka + t] + tail[t] for t in range(r)]
obj = {
    "target_id": "codetables-binary-linear",
    "q": 9, "n": 27 + l, "k": Kb, "d": 10,
    "field": "GF(9) = GF(3)[w]/(w^2 - w - 1); a + b*w encoded as the integer a + 3b (0..8)",
    "G": G,
    "construction": "Construction X: C(D,17P) inside C(D,20P), plain one-point codes of the Hermitian curve "
                    "y^3 + y = x^4 over GF(9) (monomials x^i y^j, j <= 2, pole order 3i + 4j, at the 27 affine points "
                    "ordered by x then y in the encoding), with a Reed-Solomon tail [4,3] (rows e^t, e = 0..3, 0^0 = 1) "
                    "on the last 4 columns for the 3 rows of pole order in (17,20]; tail columns 2 and 3 multiplied by w",
}
json.dump(obj, open(sys.argv[1], "w"))
print("[%d,%d] rows %d, written %s" % (obj["n"], obj["k"], len(G), sys.argv[1]))
