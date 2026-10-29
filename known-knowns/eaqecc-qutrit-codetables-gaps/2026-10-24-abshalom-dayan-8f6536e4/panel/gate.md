# Honesty gate (main session), run 2026-10-24-1253

status: CONFIRMED_SOLUTION
confirmed_scope: object/eaqecc_28_7_14_11.json (sha256 8f6536e49eecf331) defines, from its 32 x 56 GF(3) symplectic stabilizer matrix S alone, a non-catalytic qutrit EAQECC with s = 32, c = rank(S J S^T)/2 = 11, k = 7 and exact minimum symplectic distance d = 14 over span(S)^perp outside span(S) ∩ span(S)^perp, which is strictly above d_lower = 13 and at most d_upper = 19 of the listed cell (n,k,c) = (28,7,11), shown as [[28,7,13-19;11]]_3 on the eaqecc.codetables.de qutrit table copy fetched 2026-10-24T12:58:19Z (footer "Last change: 10.07.2025") and re-fetched byte-identical at 2026-10-24T14:48:11Z.

Claim: [[28,7,14;11]]_3 at the listed cell (n,k,c) = (28,7,11) of https://eaqecc.codetables.de/qutrit.php, object
claim/object/eaqecc_28_7_14_11.json (sha256 8f6536e49eecf3311af7ed4869dc270efad791545c86fff9627be2aa44ab97e4), the
extended one-point Hermitian code E_14 over GF(9) with column 0 scaled by w (Hermitian hull 6 -> 5).

Self-break (self_break/verdict.md, main session, in a copy of claim/): SURVIVES.

Panel files read in full by the main session (each skeptic a fresh subagent, claude-opus-5-5, given only its own
copy of claim/, run one after another, never in parallel):
- reproduce.md (13:53Z-14:07Z): own checker written before reading the author's code (exact GF(3) linear algebra,
  bitsliced enumeration of every projective point of N \ I, 141214738716 points); 132/132 brute-force tests, a
  planted weight-3 control found, an isotropic-exclusion control with the exact expected count 27674; deterministic
  rerun. Result s = 32, c = 11, k = 7, dim N = 24, dim I = 10, d = 14 with 79488 weight-14 vectors; author's rebuild
  byte-identical, subset test and full 3^24 enumeration reproduced (same 79488). pass: true.
- novelty.md (14:14Z-14:37Z): one honest GET at 2026-10-24T14:14:03Z, HTTP 200, sha256 37bbf731..., cell
  [[28,7,13-19;11]]_3; the page's own rules (teleportation cells and k = 0 cells excluded, zero upper-bound
  violations) give 13 at the cell; the table's source arXiv:2207.05647 and arXiv:2607.02170 read in full,
  arXiv:2105.02166 checked (its codes reach 13 here); codetables.de qutrit stabilizer table, TROPHY_CASE.md,
  known-knowns/ and the five EAQECC/qutrit PRs give nothing at d >= 14. pass: true, with caveats (below).
- criterion.md (14:45Z-14:50Z): clause by clause met; own GF(3) recomputation s = 32, rank(S J S^T) = 22, c = 11,
  k = 7; own GF(9) check that all 37442160 15-column subsets of G9 have full rank (d >= 14 on all of N) plus the
  author's subset test and the witness (d <= 14); listed cell, single cell, c >= 1, non-catalytic; page rules give no
  source reaching 14. One GET at 14:48:11Z, byte-identical. pass: true.

Live re-fetch at the gate: one plain curl GET, User-Agent "V3R1T4S-research-agent (honest single fetch)", no
retries, 2026-10-24T14:50:19Z to 14:50:20Z (server date Sat, 24 Oct 2026 14:50:19 GMT), HTTP 200, 628039 bytes,
sha256 37bbf731030c113e2e2e75fe7b5ed0b1d11829cfc4a5f1ad948a38b1ac7c936c (unchanged since 12:58:19Z), cell verbatim
`[[28,7,13-19;11]]<sub>3</sub>` (title "lengthening of [[27,7,13;11]] subcode of [[27,8,13;11]] from
arXiv:2207.05647"), footer "Last change: 10.07.2025". Saved in data/gate_fetch/. 14 > 13 and 14 <= 19.

Downgrade checks (none triggered): no hedging panelist; no reproduction mismatch (four exact computations agree:
the author's subset test and full enumeration, REPRODUCE's projective enumeration, CRITERION's GF(9) subset-rank
bound with the witness); 14 strictly above the live d_lower 13; no stretched criterion or hidden quantifier found
(symplectic weight, isotropic exclusion and the page's [[n,k,d;c]] convention checked); scope no wider than
reproduced; no sample presented as complete; no capped search used as an exclusion; no probable prime; the table
read only by honest single GETs (no browser User-Agent, cookies or retries; self_break audit). One object, one cell.

Caveats carried into the package and report, not downgrades:
- Catalytic setting: by the page's own note, the listed [[28,8,14;12]] gives [[28,7,14;11]] catalytically. The page
  and the criterion exclude that setting, and this object's c and k come from S itself, so it is a non-catalytic
  record: one ebit fewer than the known non-catalytic [[28,7,14;12]].
- Stronger sibling: the unscaled E_14 gives [[28,6,>=14;10]]_3 (hull 6), our own, unpublished, at an unlisted cell;
  the claim follows from it by the page's increasing-dimension rule. The two must not be counted as independent
  wins; [[28,6,14;10]] is the top live lead (partial win p2).
- Wording: "improves the table cell", not "new in the literature" (hull variation by column scaling is a known
  technique).
Not part of this claim: propagated cells (e.g. [[29,7,14;11]], [[28,6,14;11]]) and the run's other leads.
