# PREREG (frozen 2026-10-24T13:01:23Z, before any checker of this run has been run on any object)

null_test: not needed because the claim is one explicit stabilizer matrix checked by deterministic exact checkers against a table value (no search statistic, no "beats chance" claim)

## Criterion (verbatim, bank entry eaqecc-qutrit-codetables-gaps)

Success means an explicit EAQECC with parameters [[n,k,d;c]]_3, c >= 1, given by an exact generator matrix over GF(3) (symplectic form, 2n columns) or over GF(9) (trace-Hermitian form), for a cell of the live qutrit table (https://eaqecc.codetables.de/qutrit.php, re-fetched live immediately before claiming), such that: with s independent generators on Alice's n qutrits, c = rank(S J S^T)/2 (half the rank of the symplectic commutation matrix) and k = n - s + c; the minimum distance d, computed exactly as the minimum weight of vectors in the symplectic dual of span(S) that are not in the isotropic part span(S) ∩ span(S)^perp (the EAQECC definition used by Grassl), is STRICTLY GREATER (direction: max) than the table's d_lower for that (n,k,c), and d <= d_upper. Results for c = 0 are excluded (they belong to the qudit table entry).

## Object to be judged

Default: the dossier's priority-1 candidate, run 2026-10-24-1033's constructor/objects/eaqecc_28_7_14_11.json
(sha256 8f6536e49eecf3311af7ed4869dc270efad791545c86fff9627be2aa44ab97e4), claimed [[28,7,14;11]]_3 for the listed
cell (n,k,c) = (28,7,11). Replacement rule, fixed now: if a lens of this run produces an object with exact
d >= 15 at (n,k,c) = (28,7,11) passing every threshold below, that object is the claim instead. Any other new object
(other cells) is recorded as a live lead and not claimed in this run (one cell per claim).

## Statistic and checkers

- s = rank(S) over GF(3), c = rank(S J S^T)/2, k = n - s + c, computed from S alone, never copied.
- d, exact, by two independent methods that agree, none sampling:
  (A) a checker written in this run (evaluator-first lens) from the definition: for every set T of d - 1 = 13 of
      the 28 positions, every vector of span(S)^perp supported inside T lies in span(S) ∩ span(S)^perp (dimension
      comparison by exact GF(3) ranks); plus an explicit vector of span(S)^perp of symplectic weight d outside the
      isotropic part. All C(28,13) = 37442160 subsets, uncapped.
  (B) run 2026-10-24-1033's full Gray-code enumeration of all 3^24 vectors of span(S)^perp (enum_min.c), rerun here
      if the machine allows; otherwise its saved verdict is cited and the panel's REPRODUCE skeptic supplies the
      second independent computation.
  Checker (A) is tested before it judges the claim on a known positive (this workspace's panel-confirmed
  [[28,5,15;11]]_3 object, d = 15, and small random codes against brute force) and on known negatives (seeded
  objects with a low-weight logical, and the candidate with a claimed d that is too high).

## Thresholds

1. Computed (n, k, c) = (28, 7, 11) with c >= 1.
2. d computed exactly = claimed d by (A), agreeing with (B) or with the REPRODUCE skeptic's own exact computation.
3. d > d_lower and d <= d_upper of the listed cell on a live one-GET re-read of https://eaqecc.codetables.de/qutrit.php
   right before claiming (scout: 13-19 at 12:58:19Z).
4. Not implied, through the page's propagation rules, by any listed cell, any code in this repo, its open PRs, the
   literature found (already-settled lens; NOVELTY skeptic), or this workspace's own other codes. A tie is not a win.
5. One cell per claim; propagated neighbours are listed as not claimed.

## Search space record

Every search records its exact family and whether it was exhausted (uncapped) or capped. Capped or sampled searches
are never used as exclusions.
