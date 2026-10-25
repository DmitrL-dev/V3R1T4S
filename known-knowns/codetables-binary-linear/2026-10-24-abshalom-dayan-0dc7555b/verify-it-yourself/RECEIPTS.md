# Receipts

Real output of `sh verify-it-yourself/run_checks.sh` from this package folder (with the date, platform, compiler and
Python version printed before it and the timing after it):

```
2026-10-24T12:40:04Z
Darwin arm64
Apple clang version 21.0.0 (clang-2100.1.1.101)
Python 3.14.7
claimed n=31 k=18 d=10; computed rank(G)=18
k=18 n=31 rank=18
W=1: no nonzero codeword of weight <= 1 (all 31 subsets)
W=2: no nonzero codeword of weight <= 2 (all 465 subsets)
W=3: no nonzero codeword of weight <= 3 (all 4495 subsets)
W=4: no nonzero codeword of weight <= 4 (all 31465 subsets)
W=5: no nonzero codeword of weight <= 5 (all 169911 subsets)
W=6: no nonzero codeword of weight <= 6 (all 736281 subsets)
W=7: no nonzero codeword of weight <= 7 (all 2629575 subsets)
W=8: no nonzero codeword of weight <= 8 (all 7888725 subsets)
W=9: no nonzero codeword of weight <= 9 (all 20160075 subsets)
W=10 complete for all W'<10; first nonzero codeword supported in a 10-set after 985 subsets
d=10 witness_weight=10 witness=1 5 4 8 2 7 6 0 0 0 0 6 0 0 0 0 0 0 1 0 0 0 0 0 0 0 8 0 0 0 0
m3_mindist: W=9: no nonzero codeword of weight <= 9 (all 20160075 subsets); d=10
witness: weight 10, nonzero codeword of the row space: True
computed n=31 k=18 d=10; claimed n=31 k=18 d=10
PASS
real 7.72
user 6.14
sys 0.38
exit=0
2026-10-24T12:40:12Z
```
