# Criterion skeptic verdict: eaqecc-qutrit-codetables-gaps, claim [[28,7,14;11]]_3

context: subagent (Claude Agent tool, model claude-opus-5-5), given only claim/

## Bottom line

PASS. Read literally, the object meets the full success criterion, not just a partial win. S (32 x 56 over GF(3), symplectic
form) gives s = 32, c = rank(S J S^T)/2 = 11 and k = n - s + c = 7. Its distance, taken over span(S)^perp minus the
isotropic part, is exactly 14. That is strictly above the live table's d_lower = 13 for the listed cell (28,7,11), and
below d_upper = 19. I checked d two ways that share no code: the author's position-subset test, whose logic I
reviewed and re-ran, and my own GF(9) column-subset rank check, plus my own check of the witness.

The page's notes set two traps: the catalytic-setting note and the propagation rules. Neither one reaches this cell
with d = 14 from an existing table row. The parameters do coincide exactly with the catalytic consequence of the listed
[[28,8,14;12]]. The object still counts as non-catalytic, because c and k are computed from S itself. The only clause
the claim package cannot settle is the procedural one: the gate must re-fetch the page live immediately before
claiming. My single GET at 14:48:11Z returned a page byte-identical to the package copy.

## Evidence (all times UTC, from `date -u`)

- 14:45:16. `rebuild/build_obj.py 14 rebuilt.json 14 0` run in mine/run/ (a copy of claim/). The sha256 of
  rebuilt.json and of object/eaqecc_28_7_14_11.json are both 8f6536e49eecf3311af7ed4869dc270efad791545c86fff9627be2aa44ab97e4,
  which matches CLAIM.md.
- 14:46:43. My own exact GF(3) program (mine/my_params.py, shares no code with checkers/) printed:
  `rows_of_S=32 n=28 s=32 rank_SJST=22 c=11 k=n-s+c=7 dimN=24 dimI(span S ∩ N)=10 dimI(s-rankGram)=10` and
  `phi(G9): rows=24 rank=24 orthogonal_to_all_S=True equals_N=True`.
  The author's checkers/gf3prep.py agrees: `n=28 s=32 c=11 k=7 dim_isotropic=10 dim_dual=24` (mine/gf3prep.out).
  S has integer entries in {0,1,2} only and exactly 2n = 56 columns.
- 14:46:43. checkers/witness.py on T = {0,...,8,11,17,20,23,27} printed `symplectic_weight=14 orthogonal_to_all_rows_of_S=True
  in_span_S=False`. At 14:48:04 I re-checked that vector with my own rank and symplectic code (mine/wcheck.out):
  `symplectic_weight=14 hamming_weight_2n=18 orth_all_S=True rank_S=32 rank_S_plus_v=33`. So the vector lies in N and
  outside span(S), and therefore outside I. This gives d <= 14.
- 14:47:29 to 14:47:32. My own independent C check (mine/g9_subsets.c, output in mine/g9_Z15.out and mine/g9_Z14.out):
  every one of the C(28,15) = 37442160 15-column subsets of G9 has rank 12 over GF(9) (`rank_deficient=0`). So the
  GF(9) code spanned by G9 has minimum Hamming weight at least 14. N = phi(G9) was verified above, and phi turns
  GF(9) Hamming weight into symplectic weight, so every nonzero vector of N, and hence every vector of N \ I, has
  symplectic weight at least 14. This gives d >= 14.
  Positive control: for Z = 14 the check finds 9936 deficient subsets, so the test is not vacuous.
- 14:47:43 to 14:47:52. The author's checkers/subset_ea.c, run on 4 cores (mine/subset13.part*, mine/subset14.part*):
  - W = 13: all four parts print `with_vector_outside_isotropic=0`, with 4 x 9360540 = 37442160 subsets examined.
  - W = 14: the parts print 2474, 2494, 2494 and 2474, for a total of 9936. This matches REPRODUCE.md and my GF(9) count.
  - Logic review: the basis is ordered with I first. A non-I row that becomes dependent on the positions outside T is
    equivalent to dim N_T > dim I_T. Support is the symplectic support, because the x and z bits of each position are
    masked together. The pivot elimination and the GF(3) bit arithmetic are correct.
- Not run: the 18-CPU-minute full enumeration (REPRODUCE step 4). Two independent exact methods already fix d = 14.
- 14:48:11 to 14:48:12. One honest GET of the status page (mine/live/): HTTP 200, 628039 bytes, sha256
  37bbf731030c113e2e2e75fe7b5ed0b1d11829cfc4a5f1ad948a38b1ac7c936c. This is identical to table/qutrit.php (fetched
  12:58:19Z). The cell still reads `[[28,7,13-19;11]]` ("lengthening of [[27,7,13;11]] ..."), the footer still says
  "Last change: 10.07.2025", and no [[28,7,>=14;11]] entry exists.
- 14:49:09. None of my jobs were still running.

## Clause by clause

| Clause | Verdict | Evidence |
|---|---|---|
| Explicit exact generator matrix in an allowed form (GF(3) symplectic, 2n columns) | met | object JSON field S: 32 x 56, entries 0..2, rows (x\|z), form x.z' - z.x' stated |
| c >= 1 (c = 0 excluded, qudit-table pitfall) | met | c = 11 |
| c = rank(S J S^T)/2 from S, not chosen | met | rank of the Gram matrix = 22, so c = 11 (two independent programs) |
| s independent generators; k = n - s + c | met | s = rank S = 32 (all rows independent); k = 28 - 32 + 11 = 7; dim I = s - 2c = 10 = n - k - c, consistent with the table's [[n,k,d;c]] convention |
| d = minimum weight over span(S)^perp minus span(S) ∩ span(S)^perp, computed exactly | met, d = 14 | lower bound: subset test W=13 gives 0, and my GF(9) check gives d(N \ {0}) >= 14; upper bound: verified witness of weight 14 |
| Strictly greater than d_lower for that (n,k,c); d <= d_upper | met | 14 > 13 and 14 <= 19 |
| A cell of the live qutrit table | met | (28,7,11) is listed: `[[28,7,13-19;11]]_3`. Row n=28, k=7 lists c in {0,1,5,7,9,11,12,14,15,17,19,21} |
| Re-fetched live immediately before claiming | met as of 14:48:12Z; the gate must still do it | the package copy is from 12:58:19Z; my GET at 14:48:11Z is byte-identical. The gate's own re-fetch immediately before claiming is still required and is not replaced by mine |

## Hidden quantifiers, stretched definitions, null model

- **Weight notion.** d uses symplectic weight, the number of positions with (x_i, z_i) != (0,0). The witness has
  symplectic weight 14 and Hamming weight 18 over the 2n coordinates. The claim uses the smaller, standard weight, so
  nothing is inflated.
- **Isotropic clause.** For v in N, being outside I is the same as being outside span(S). The witness is outside
  span(S), since the rank rises from 32 to 33. My lower bound covers all of N \ {0}, which is stronger than needed.
- **Same convention as the page.** The page reads [[n,k,d_lower-d_upper;c]]_q, with c the number of required maximally
  entangled pairs (non-catalytic). The claim's s = n - k + c = 32 and dim I = n - k - c = 10 match that reading.
- **Propagation from existing rows** (page rules: subcode, lengthening, puncturing, quantum shortening, increasing
  dimension, length reduction, teleportation). The sources that map into (28,7,11) are:
  - (28,8,11) gives d 13 (subcode).
  - (27,7,11) gives 13 (lengthening).
  - (29,7,11) gives 13 - 1 (puncturing).
  - (29,6,11) gives 13 - 1 (quantum shortening).
  - (28,6,10) and (29,7,10) are not listed, so the increasing-dimension and length-reduction routes have no source.
  - Teleportation needs c = k, which does not hold here.

  None of these reaches 14, so the result is not a propagation-only improvement.
- **Catalytic setting.** The page's note says [[n,k,d;c]] with c >= k > 1 implies [[n,k-1,d;c-1]] in the catalytic
  setting. The listed [[28,8,14;12]] therefore gives exactly [[28,7,14;11]] catalytically. That is the main trap for
  this cell. The object passes it because its c = 11 and k = 7 come from the commutation structure of S itself. It is
  a genuine non-catalytic code, not [[28,8,14;12]] with one ebit borrowed (that code would show c = 12 and k = 8).
- **Author's own other code.** For context, I rebuilt E_14 without the column scaling as mine/run/unscaled.json.
  It has Hermitian hull 6, with s = 32, c = 10 and k = 6, the same classical code up to scaling, and d >= 14 by the
  same GF(9) check. That is [[28,6,>=14;10]]. Under the page's increasing-dimension rule it would itself imply
  [[28,7,14;11]]. The cell (28,6,10) is not listed and that code is not a table row, so the propagation pitfall does
  not apply. The claimed object is explicit and is checked on its own. This does not change the verdict.
- **Bundling.** The claim names one cell only. Consequences that follow by propagation, such as lengthening to
  [[29,7,14;11]] or a subcode [[28,6,14;11]], are not claimed and should not be counted as separate wins.
- **Null model.** None applies in the statistical sense. The claim is a deterministic, exact algebraic statement. The
  relevant baseline is what the table already implies (propagation rules and the catalytic note), and that baseline
  was checked above. The positive controls at W = 14 and Z = 14 show the subset tests can detect a word when one exists.

confirmed_scope: object/eaqecc_28_7_14_11.json (sha256 8f6536e49eecf331) defines, from its 32 x 56 GF(3) symplectic stabilizer matrix S alone, a non-catalytic qutrit EAQECC with s = 32, c = rank(S J S^T)/2 = 11, k = 7 and exact minimum symplectic distance d = 14 over span(S)^perp outside span(S) ∩ span(S)^perp, which is strictly above d_lower = 13 and at most d_upper = 19 of the listed cell (n,k,c) = (28,7,11), shown as [[28,7,13-19;11]]_3 on the eaqecc.codetables.de qutrit table copy fetched 2026-10-24T12:58:19Z (footer "Last change: 10.07.2025") and re-fetched byte-identical at 2026-10-24T14:48:11Z.

## Concerns (none blocks the pass)

1. **Live re-fetch is the gate's job.** The criterion requires a live re-fetch immediately before claiming. My
   14:48Z GET supports the claim but does not replace that re-fetch. If the cell's d_lower is 14 or more at claim
   time, the claim fails.
2. **"New" means new to the table.** The result relies on varying the hull of equivalent codes (one column scaled by
   w turns E_14 into hull 5). That technique is in the literature, and the paper behind the table's neighbouring
   entries (arXiv:2207.05647) is cited on the page. The criterion asks only about the live table, so the claim should
   be worded as "improves the table cell", not "new in the literature".
3. **A stronger sibling may exist.** [[28,6,>=14;10]] appears to follow from the unscaled code; d >= 14 is verified,
   but its exact d was not computed. It sits in an unlisted cell. If it is reported later, the (28,7,11) result
   becomes its increasing-dimension consequence, and the two should not be counted as independent wins.
4. **Outbound contact is not authorized.** Any report to the table maintainers is outbound contact and needs explicit
   human permission. None was made here.

pass: true
