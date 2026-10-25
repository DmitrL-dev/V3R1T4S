# REPRODUCE skeptic: claim [31,18,10] over GF(9)

context: subagent (Claude Agent tool, model claude-opus-5-5), given only claim/

Bottom line: confirmed. My own checker, written from the definition before I read the author's code, finds rank 18 and
exact minimum distance d = 10. It uses two complete column-subset methods that agree, plus an unpruned run that
visits all C(31,9) = 20160075 subsets one at a time. A weight-10 codeword lies in the row space. The author's steps 1 to 4
and the optional Brouwer-Zimmermann step reproduce every expected line in claim/REPRODUCE.md verbatim (checked by script). The rebuild is byte-identical
(sha256 0dc7555b...e54f). Against the saved table page, 9 < 10 <= 12.

All commands ran from work-reproduce/mine/, so `../claim/` there means claim/. Every compute job ran under `nice -n 10`,
each top-level job with a perl `alarm` hard cap. At most 3 of my compute jobs ran at once (the cap was 4). None is still
running (background PIDs are in work-reproduce/mine/pids.txt, and all had exited before I wrote this).

## 1. Definition used (quoted from claim/CLAIM.md)

Claim: "The 18 x 31 matrix G over GF(9) in object/code_q9_n31_k18_d10.json generates a linear [31,18,10] code over GF(9),
whose minimum distance 10 is strictly above the codetables.de lower bound 9 (upper bound 12) for (q,n,k) = (9,31,18)."

Success criterion, items I check: "(1) Rank is exactly k over GF(q), computed independently. (2) The exact minimum
distance d is computed by full enumeration of all q^k - 1 nonzero codewords when feasible (2^k <= ~2^32), or, for large
k (or large k with small n-k, via the dual and MacWilliams identities), by two independent exact minimum-distance
implementations that agree; never by sampling. (3) d is STRICTLY GREATER (direction: max) than the lower bound in the
live http://www.codetables.de/ cell for (q,n,k) at verification time, and at most the upper bound."
(Item (3)'s live re-read and item (4)'s novelty are other skeptics' jobs. I only check against the saved page.)

Field convention, quoted from the object JSON: "GF(9) = GF(3)[w]/(w^2 - w - 1); a + b*w encoded as the integer a + 3b (0..8)".
So w^2 = w + 1 and (a+bw)(c+dw) = (ac+bd) + (ad+bc+bd)w, all mod 3.

Minimum distance: d = min weight of a nonzero vector in the row space of G. 9^18 - 1 (about 1.5e17) codewords are too
many to enumerate, so I used two exact subset methods.

## 2. My checker (work-reproduce/mine/dmin.c, gf9.py), method and completeness

- Field: built from the formula above, separately in C (dmin.c) and Python (gf9.py). Both check distributivity and
  associativity on all 729 triples and that every nonzero element has an inverse. gf9.py also checks that w^2 - w - 1
  has no root in GF(3), that w = 3 satisfies w^2 = w + 1, and that the multiplicative group has an element of order 8.
- Rank: Gaussian elimination over GF(9), done separately in Python (gf9.rank) and C (rank_mat).
- Mode H (dual). Compute H (13 x 31) from the reduced echelon form of G, and check G H^T = 0 and rank H = 13. Then
  C = ker H, and a codeword of weight w gives a dependent set of w columns of H, and conversely. So d >= D iff every
  D-1 columns of H are linearly independent. A depth-first search over every column subset of size <= D-1, in
  increasing order, keeps an incremental echelon basis and stops at the first dependent set. Completeness: the visited-node count for
  D = 10 is 31621023 = sum_(j=1..9) C(31,j), i.e. every subset of at most 9 columns was tested.
- Mode G (primal, H never used). d >= D iff every set of n-D+1 = 22 columns of G has rank 18, because a nonzero m
  with m G_S = 0 is a codeword of weight <= D-1, and conversely. A depth-first search runs over the removed set T (|T| = 9)
  and shares the work for common prefixes. A subtree is pruned only when the columns kept so far already reach rank 18,
  in which case every completion is fine. Completeness: with pruning disabled (NOPRUNE=1), it visits
  leaves = 20160075 = C(31,9), one rank check per 22-subset.
- When a test fails, the program finds the subset and prints a codeword m*G supported inside it (from the left kernel), with its weight.
- Exact d: run the test with D = 10 (it must pass, so d >= 10), then with D = 11 (it must fail and give a weight-10
  codeword, so d <= 10).
- Mode A (extra): counts the dependent 10-subsets of H-columns. Every 9-subset is independent, so each such subset carries
  exactly one codeword up to a scalar, with full support, and A_10 = 8 * count.

### Tests on known positives and negatives (before running on the claim)

Known positives: extended RS [9,k,10-k] (k = 1..8) and doubly-extended RS [10,k,11-k] (k = 1..9) over GF(9), both MDS;
40 random small codes whose d comes from full brute-force enumeration in Python. Known negatives: every one of those
codes with D = d+1 claimed (must fail, with a witness of weight exactly d). Output (work-reproduce/mine/tests_out.txt,
114 test lines; `grep -c MISMATCH` = 0):

```
Known positives (MDS RS codes, d known in closed form):
  RS9_k1                       [9,1] mode H: pass up to D=9, fail at D=10 with witness weight 9; expected d=9 -> OK
  RS9_k1                       [9,1] mode G: pass up to D=9, fail at D=10 with witness weight 9; expected d=9 -> OK
  ... (34 RS lines in total, all OK)
  RS10_k9                      [10,9] mode H: pass up to D=2, fail at D=3 with witness weight 2; expected d=2 -> OK
  RS10_k9                      [10,9] mode G: pass up to D=2, fail at D=3 with witness weight 2; expected d=2 -> OK
Known positives: brute force vs checker on random codes
  rand0_bf_d11                 [15,3] mode H: pass up to D=11, fail at D=12 with witness weight 11; expected d=11 -> OK
  rand0_bf_d11                 [15,3] mode G: pass up to D=11, fail at D=12 with witness weight 11; expected d=11 -> OK
  rand1_bf_d2                  [5,3] mode H: pass up to D=2, fail at D=3 with witness weight 2; expected d=2 -> OK
  ... (80 random-code lines in total, all OK)
  rand39_bf_d13                [16,2] mode H: pass up to D=13, fail at D=14 with witness weight 13; expected d=13 -> OK
  rand39_bf_d13                [16,2] mode G: pass up to D=13, fail at D=14 with witness weight 13; expected d=13 -> OK
ALL TESTS OK
```

Tests at the claim's scale (work-reproduce/mine/tests2_out.txt). Numpy brute force over all 9^7 - 1 messages of [31,7]
subcodes of the claim matrix and of random [24,7] codes, against modes H and G. Planted negatives: the claim matrix with one row
replaced by a planted weight-9, weight-8 or weight-3 vector (rank stays 18), which must be rejected at D = 10:

```
(2) numpy brute force vs dmin (both modes):
    claim_rows0-6      [31,7] brute d=18 (A_d=8448); dmin H: d=18, witness weight 18 -> OK
    claim_rows0-6      [31,7] brute d=18 (A_d=8448); dmin G: d=18, witness weight 18 -> OK
    claim_rows11-17    [31,7] brute d=16 (A_d=8); dmin H: d=16, witness weight 16 -> OK
    claim_rows11-17    [31,7] brute d=16 (A_d=8); dmin G: d=16, witness weight 16 -> OK
    claim_rows_rand7   [31,7] brute d=12 (A_d=192); dmin H: d=12, witness weight 12 -> OK
    claim_rows_rand7   [31,7] brute d=12 (A_d=192); dmin G: d=12, witness weight 12 -> OK
    rand24x7_0         [24,7] brute d=12 (A_d=16); dmin H: d=12, witness weight 12 -> OK
    rand24x7_0         [24,7] brute d=12 (A_d=16); dmin G: d=12, witness weight 12 -> OK
    rand24x7_1         [24,7] brute d=12 (A_d=8); dmin H: d=12, witness weight 12 -> OK
    rand24x7_1         [24,7] brute d=12 (A_d=8); dmin G: d=12, witness weight 12 -> OK
    rand24x7_2         [24,7] brute d=12 (A_d=32); dmin H: d=12, witness weight 12 -> OK
    rand24x7_2         [24,7] brute d=12 (A_d=32); dmin G: d=12, witness weight 12 -> OK
(3) planted negatives on the claim matrix (expect dmin D=10 to FAIL):
    planted weight-9 row 0: rank 18; dmin H 10 exit=10, witness weight 7 -> OK (rejected)
    planted weight-9 row 0: rank 18; dmin G 10 exit=10, witness weight 7 -> OK (rejected)
    planted weight-9 row 17: rank 18; dmin H 10 exit=10, witness weight 9 -> OK (rejected)
    planted weight-9 row 17: rank 18; dmin G 10 exit=10, witness weight 9 -> OK (rejected)
    planted weight-8 row 5: rank 18; dmin H 10 exit=10, witness weight 9 -> OK (rejected)
    planted weight-8 row 5: rank 18; dmin G 10 exit=10, witness weight 9 -> OK (rejected)
    planted weight-3 row 9: rank 18; dmin H 10 exit=10, witness weight 3 -> OK (rejected)
    planted weight-3 row 9: rank 18; dmin G 10 exit=10, witness weight 3 -> OK (rejected)
```

(In that run the A_d lines and the final line of tests2_out.txt read MISMATCH. That was a parsing bug in tests2.py: it took the
"8" of "8 * N" as the count. I fixed the parse and re-ran the counts in work-reproduce/mine/acount.py, and all agree with
brute force:)

```
rand24x7_0         dmin A 12: '=> A_12 = 8 * 2 = 16 codewords of weight 12'  brute-force A_12 = 16 -> OK
rand24x7_1         dmin A 12: '=> A_12 = 8 * 1 = 8 codewords of weight 12'  brute-force A_12 = 8 -> OK
rand24x7_2         dmin A 12: '=> A_12 = 8 * 4 = 32 codewords of weight 12'  brute-force A_12 = 32 -> OK
claim_rows_rand7   dmin A 12: '=> A_12 = 8 * 24 = 192 codewords of weight 12'  brute-force A_12 = 192 -> OK
claim_rows11-17    dmin A 16: '=> A_16 = 8 * 1 = 8 codewords of weight 16'  brute-force A_16 = 8 -> OK
claim_rows0-6      dmin A 18: '=> A_18 = 8 * 1056 = 8448 codewords of weight 18'  brute-force A_18 = 8448 -> OK
ALL A-COUNTS OK
```

All d tests pass. The checker accepts every true d, rejects every claim of d+1 with a witness of weight exactly d,
and rejects every planted low-weight word at full size.

## 3. My checker on the claim object

Object integrity and rank (Python), from work-reproduce/mine/export_claim.out and sha.out:

```
q,n,k,d(claimed) = 9 31 18 10
field: GF(9) = GF(3)[w]/(w^2 - w - 1); a + b*w encoded as the integer a + 3b (0..8)
python rank(G) over GF(9) = 18
wrote claimG.txt
```
```
0dc7555b8c9c50d09aa8d729be15230dfacad9168e0a197f87b3c67c9ef1e54f  ../claim/object/code_q9_n31_k18_d10.json
1ab4ec8f7b8516b1e52d16ea00ef697c16be779f8e63150c645f7b4d92639c80  ../claim/table/bklc_q9_n31_k18.html
```

The sha256 matches the value in claim/CLAIM.md. The text matrix written by my export is byte-identical (`cmp`) to the author's
json_to_code.py output.

`./dmin H 10 claimG.txt` (every 9 columns of H independent, so d >= 10):

```
k=18 n=31 rank(G) over GF(9) = 18
H computed: 13 x 31, rank H = 13, G*H^T = 0 verified
mode H: searched all subsets of <= 9 columns of H; nodes=31621023
RESULT: every 9 columns of H independent => d >= 10
exit=0
```

`./dmin G 10 claimG.txt` (every 22 columns of G have rank 18, so d >= 10), and the same with pruning disabled:

```
k=18 n=31 rank(G) over GF(9) = 18
mode G: removed-set size 9 (kept 22 of 31 columns); nodes=12862825 leaves=3297411 pruned_subtrees=7928687
RESULT: every 22 columns of G have rank 18 => d >= 10
exit=0
```
```
k=18 n=31 rank(G) over GF(9) = 18
mode G: removed-set size 9 (kept 22 of 31 columns); nodes=28048800 leaves=20160075 pruned_subtrees=0
RESULT: every 22 columns of G have rank 18 => d >= 10
```

`./dmin H 11` and `./dmin G 11` (d >= 11 fails, so the witness pins d = 10):

```
k=18 n=31 rank(G) over GF(9) = 18
H computed: 13 x 31, rank H = 13, G*H^T = 0 verified
mode H: searched all subsets of <= 10 columns of H; nodes=1090
dependent H-column set of size 10: {0,1,2,3,4,5,6,11,18,26}
witness m = [6,4,5,7,6,1,0,4,4,0,7,8,4,3,1,0,0,0]
witness c = m*G = [6,2,5,7,3,1,4,0,0,0,0,4,0,0,0,0,0,0,6,0,0,0,0,0,0,0,7,0,0,0,0]
witness weight = 10
RESULT: d <= 10 (so NOT d >= 11)
exit=10
```
```
k=18 n=31 rank(G) over GF(9) = 18
mode G: removed-set size 10 (kept 21 of 31 columns); nodes=1047 leaves=660 pruned_subtrees=301
removed set T = {0,1,2,3,4,5,6,11,18,26} : complement has rank < 18
witness m = [6,4,5,7,6,1,0,4,4,0,7,8,4,3,1,0,0,0]
witness c = m*G = [6,2,5,7,3,1,4,0,0,0,0,4,0,0,0,0,0,0,6,0,0,0,0,0,0,0,7,0,0,0,0]
witness weight = 10
RESULT: d <= 10 (so NOT d >= 11)
exit=10
```

Witness re-checked in pure Python, and compared with the author's witnesses (work-reproduce/mine/own_rebuild.out, bzwit.out):

```
(1) python witness: m = [6, 4, 5, 7, 6, 1, 0, 4, 4, 0, 7, 8, 4, 3, 1, 0, 0, 0]
    c = m*G = [6, 2, 5, 7, 3, 1, 4, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0]  weight = 10
```
```
own witness c = m*G: [6, 2, 5, 7, 3, 1, 4, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0] weight 10
7 * own witness == author witness: True
author witness in row space (own rank(G + [w]) == 18): True  weight 10
```
```
bz9w witness: weight 10  in row space (own rank(G+[w]) == 18): True  affine weight 7  tail weight 3
```

The author's m3 witness is exactly 7 times mine (same support {0,1,2,3,4,5,6,11,18,26}).

Weight-10 count (extra), from work-reproduce/mine/claim_A_10.out:

```
k=18 n=31 rank(G) over GF(9) = 18
H computed: 13 x 31, rank H = 13, G*H^T = 0 verified
mode A: dependent 10-subsets of H columns = 3108 (dependent smaller subsets met: 0)
=> A_10 = 8 * 3108 = 24864 codewords of weight 10
```

Determinism: re-running dmin H 10, H 11, G 10, G 11, A 10 and NOPRUNE G 10 gave byte-identical output (`cmp`). The
rebuild run twice gave the same sha256.

My result: rank(G) = 18 and d = 10 exactly.

## 4. The author's code and REPRODUCE.md steps (read only after section 3)

The author's checkers (claim/checkers/m3_mindist.c: every W-subset over a systematic form; subset_cert.c: every 9-subset
of the 27 affine coordinates with full null-space enumeration; bz9w.c: Brouwer-Zimmermann; witness_check.py) use the
same field formula. I read their completeness arguments and found them sound. m3 and subset_cert test every subset
exactly. bz9w's bound sum_j max(0, w+1-(K-r_j)) with sets 18,12,1 reaches 8+2+0 = 10 at w = 7. Outputs went to
work-reproduce/mine/author/, not claim/ (python3 -B, so no bytecode was written into claim/).

Step 1, rebuild and sha256 (byte for byte):

```
$ python3 -B ../claim/rebuild/build_code.py author/rebuilt.json
[31,18] rows 18, written author/rebuilt.json
$ shasum -a 256 author/rebuilt.json ../claim/object/code_q9_n31_k18_d10.json
0dc7555b8c9c50d09aa8d729be15230dfacad9168e0a197f87b3c67c9ef1e54f  author/rebuilt.json
0dc7555b8c9c50d09aa8d729be15230dfacad9168e0a197f87b3c67c9ef1e54f  ../claim/object/code_q9_n31_k18_d10.json
cmp: byte-identical
```

I also rebuilt G with my own code from the construction text alone (work-reproduce/mine/own_rebuild.py, not using
claim/rebuild/):

```
affine points on y^3+y=x^4: 27
pole orders used: [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
dim C(D,17P) = 15  dim C(D,20P) = 18
own rebuild equals JSON G: True
```

Steps 2 to 4 (work-reproduce/mine/author/steps2-4.out):

```
$ python3 -B ../claim/checkers/json_to_code.py ../claim/object/code_q9_n31_k18_d10.json > author/code.txt
$ cmp author/code.txt claimG.txt
identical to my own export
$ cc -O2 -o author/m3 ../claim/checkers/m3_mindist.c && ./author/m3 < author/code.txt
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
real 9.19
user 5.85
sys 0.02
exit=0
$ cc -O2 -o author/subset_cert ../claim/checkers/subset_cert.c && ./author/subset_cert 27 9 < author/code.txt
subsets=4686825 nonzero_nullspaces=465105 max_dim=1 words_le_W=0 min_weight_seen=10
real 25.14
user 16.45
sys 0.06
exit=0
$ python3 -B ../claim/checkers/witness_check.py author/code.txt "1 5 4 8 2 7 6 0 0 0 0 6 0 0 0 0 0 0 1 0 0 0 0 0 0 0 8 0 0 0 0"
k=18 n=31 rank(G)=18
witness weight=10 in_rowspace=True support=[0, 1, 2, 3, 4, 5, 6, 11, 18, 26]
exit=0
```

The optional bz9w step finished in 124 s (work-reproduce/mine/author/bz9w.out, .time):

```
K=18 n=31 d=10 sets=18,12,1 maxw=7 words=26962471566 witness=0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 2 0 0 5 0 0 3 5 3 8 0 4 7 6
```

Mechanical comparison (work-reproduce/mine/expcheck.py: every non-"..." expected line in claim/REPRODUCE.md must occur
verbatim in the actual output):

```
FOUND   k=18 n=31 rank=18
FOUND   W=9: no nonzero codeword of weight <= 9 (all 20160075 subsets)
FOUND   W=10 complete for all W'<10; first nonzero codeword supported in a 10-set after 985 subsets
FOUND   d=10 witness_weight=10 witness=1 5 4 8 2 7 6 0 0 0 0 6 0 0 0 0 0 0 1 0 0 0 0 0 0 0 8 0 0 0 0
FOUND   subsets=4686825 nonzero_nullspaces=465105 max_dim=1 words_le_W=0 min_weight_seen=10
FOUND   k=18 n=31 rank(G)=18
FOUND   witness weight=10 in_rowspace=True support=[0, 1, 2, 3, 4, 5, 6, 11, 18, 26]
FOUND   K=18 n=31 d=10 sets=18,12,1 maxw=7 words=26962471566 witness=0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 2 0 0 5 0 0 3 5 3 8 0 4 7 6
all expected lines found verbatim: True
```

So m3 gives d=10 after 985 subsets with the same witness,
subset_cert `subsets=4686825 nonzero_nullspaces=465105 max_dim=1 words_le_W=0 min_weight_seen=10`, witness_check
rank 18 and in_rowspace=True, and bz9w `d=10 ... words=26962471566` with the same witness. They agree with my d = 10.

## 5. Against the saved table page

claim/table/bklc_q9_n31_k18.html (sha256 1ab4ec8f...9c80, matching claim/table/RECORD.md) reads "Bounds on linear codes
[31,18] over GF(9) lower bound: 9 upper bound: 12". d = 10 > 9 and d = 10 <= 12, so the saved cell is beaten by 1.
The live re-read is another skeptic's job.

## 6. Concerns and notes (none blocking)

- The standard Construction X bound does not give 10 by itself. My exact distances for the parts (work-reproduce/mine/components.out)
  are C(D,17P) = [27,15,10], C(D,20P) = [27,18,7] and tail = [4,3,2], so the bound is min(10, 7+2) = 9. The tenth unit
  of distance rests only on the exhaustive computation. That computation is complete, and my two methods (plus the unpruned run)
  and the author's three methods all confirm it. The author's statement that scaling the tail columns by w "never changes a weight" is right (it is a monomial
  equivalence), so the "++--" pattern is irrelevant to d.
- My tests2.py run had a parsing bug in its A-count lines, described and fixed above. It did not affect any d result.
- Machine load was about 130 to 166 during the run. Timings are wall clock under that load.
- Not checked here: the live table (criterion 3, at verification time) and novelty against the LinCodeEvolve codes or newer
  arXiv work (criterion 4).

pass: true
