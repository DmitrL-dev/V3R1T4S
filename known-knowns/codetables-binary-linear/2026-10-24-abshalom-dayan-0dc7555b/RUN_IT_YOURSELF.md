# Run it yourself

From this package folder, in a fresh shell (needs python3 and cc, no network):

```sh
sh verify-it-yourself/run_checks.sh
```

Expected output (about 10 seconds on one core):

```
claimed n=31 k=18 d=10; computed rank(G)=18
k=18 n=31 rank=18
W=1: no nonzero codeword of weight <= 1 (all 31 subsets)
...
W=9: no nonzero codeword of weight <= 9 (all 20160075 subsets)
W=10 complete for all W'<10; first nonzero codeword supported in a 10-set after 985 subsets
d=10 witness_weight=10 witness=1 5 4 8 2 7 6 0 0 0 0 6 0 0 0 0 0 0 1 0 0 0 0 0 0 0 8 0 0 0 0
m3_mindist: W=9: no nonzero codeword of weight <= 9 (all 20160075 subsets); d=10
witness: weight 10, nonzero codeword of the row space: True
computed n=31 k=18 d=10; claimed n=31 k=18 d=10
PASS
```

Why this is exact: every nonzero codeword of weight at most 9 is supported inside some 9-subset T of the 31
coordinates. With G in systematic form on an information set I, such a codeword exists for T iff the submatrix of
the redundancy part with rows I∩T and columns outside T has a nonzero left-kernel vector. The program examines all
C(31,9) = 20160075 subsets exactly over GF(9) and finds none, then prints a codeword of weight 10, which the Python
part checks is a combination of the rows of G.

Rebuild the object from its construction:

```sh
python3 how-we-built-it/build_code.py rebuilt.json
shasum -a 256 rebuilt.json object/code_q9_n31_k18_d10.json   # both 0dc7555b8c9c50d09aa8d729be15230dfacad9168e0a197f87b3c67c9ef1e54f
```

A second, independent exact check (all 9-subsets of the 27 affine coordinates, about 20 seconds):

```sh
python3 -c "import json;o=json.load(open('object/code_q9_n31_k18_d10.json'));print(o['k'],o['n']);[print(*r) for r in o['G']]" > code.txt
cc -O2 -o subset_cert how-we-built-it/subset_cert.c && ./subset_cert 27 9 < code.txt
# expected: subsets=4686825 nonzero_nullspaces=465105 max_dim=1 words_le_W=0 min_weight_seen=10
```
