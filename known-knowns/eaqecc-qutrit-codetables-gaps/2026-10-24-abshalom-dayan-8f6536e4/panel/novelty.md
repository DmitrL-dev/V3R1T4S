# Novelty skeptic: [[28,7,14;11]]_3 at (n,k,c) = (28,7,11)

context: subagent (Claude Agent tool, model claude-opus-5-5), given only claim/ and public sources

## Bottom line

**PASS, with three caveats.** The live table, fetched once at 2026-10-24T14:14:03Z, gives `[[28,7,13-19;11]]_3`. The claimed d = 14 beats d_lower = 13 by 1 and stays within d_upper = 19.

I found nothing known that already reaches d >= 14 at (28,7,11):
- **The page's own propagation rules:** I computed their closure over all 3888 cells. It gives exactly 13 at this cell.
- **Literature:** nothing in the last 24 months or earlier.
- **This repo:** nothing in TROPHY_CASE.md or known-knowns/.
- **Pull requests:** none of the 5 EAQECC/qutrit PRs.
- **codetables.de qutrit stabilizer table:** no c = 0 code there propagates to this cell.

The three caveats (details under "Concerns"):

1. **Catalytic setting.** The page's `[[28,8,14;12]]` would give `[[28,7,14;11]]` in the catalytic setting. The page explicitly does not consider that setting, and the criterion uses the non-catalytic c. So under the criterion this is still a strict record, but it is a one-ebit improvement over a known neighbour, not a new distance.
2. **The claimed object is one standard scaling step away from a code that is stronger and still unclaimed.** It is the extended one-point Hermitian code [28,12,>=14]_9 (m = 14) with one column multiplied by w. The unscaled code has Hermitian hull dimension 6, which gives `[[28,6,>=14;10]]_3`. Rule (6) "increasing dimension" turns that into the claim. I found `[[28,6,14;10]]_3` nowhere (page, literature, repo, PRs), so it is not prior art. But it would itself beat (28,6,10) (page 12) and (28,6,11) (page 13).
3. **The table does not cover all of the literature.** Christensen, Munuera, Pereira and Ruano (AMC, arXiv:2105.02166) published `[[27,6,13;9]]_3` and `[[27,9,10;6]]_3`. Both are above the page's (27,6,9) = 12 and (27,9,6) = 9. Neither one implies d >= 14 at (28,7,11): the best they give is `[[28,7,13;10]]`.

## 1. Claim as read

- **What is claimed** (from claim/CLAIM.md): the stabilizer matrix S in claim/object/eaqecc_28_7_14_11.json defines `[[28,7,14;11]]_3`, against the table's `[[28,7,13-19;11]]_3`.
- **Construction** (from the object's `construction` field): monomials x^i y^j (j <= 2, 3i+4j <= 14) on the Hermitian curve y^3 + y = x^4 over GF(9), evaluated at its 27 affine points. A 28th coordinate holds the leading coefficient at the pole-order-14 monomial. Column 0 is then multiplied by w. D9 is its Hermitian dual (16 x 28), and S = phi(D9).
- **Independent check (mine/herm.py, mine/hermitian_hulls.txt):** I rebuilt this code in my own script. The claim's G9 has the same rows as my extended m = 14 code with column 0 scaled by w. I computed (k, Hermitian hull) = (12, 5), which gives [[28, 12-5, >=d; 16-5]] = [[28,7,>=d;11]]. The code-to-EA formulas follow Luo et al. Proposition 1 and Galindo et al.
- **Not judged here:** whether d = 14 is correct. That is another skeptic's job.
- **My own check, about novelty only:** the weight-14 lower bound for the unscaled and scaled codes follows from the Goppa bound plus the extra coordinate.

## 2. Live status fetch (one honest GET, no retry)

- **Command:** `curl -sS -A "V3R1T4S-research-agent (honest single fetch)" -D mine/qutrit.headers -o mine/qutrit.php ... "https://eaqecc.codetables.de/qutrit.php"`
- **URL:** https://eaqecc.codetables.de/qutrit.php
- **UTC fetch time:** 2026-10-24T14:14:03Z (before) to 2026-10-24T14:14:05Z (after). The server `date:` header reads Sat, 24 Oct 2026 14:14:04 GMT.
- **HTTP status:** 200 (`HTTP/2 200`), content-type text/html; charset=UTF-8, 628039 bytes. It is not a challenge page: it parses to 3888 cells.
- **sha256 (mine/qutrit.php):** `37bbf731030c113e2e2e75fe7b5ed0b1d11829cfc4a5f1ad948a38b1ac7c936c`. This is identical to the claim's copy in claim/table/RECORD.md, so the table has not changed since the claim's fetch.
- **Page footer:** "Last change: 10.07.2025".
- **Cell (28,7,11), verbatim:**
  `<TD NOWRAP bgcolor="#ff9900" class="EAQECC" title="lengthening of [[27,7,13;11]] subcode of [[27,8,13;11]] from arXiv:2207.05647">[[28,7,13-19;11]]<sub>3</sub></TD>`
  So d_lower = 13, d_upper = 19. The construction note reads: lengthening of [[27,7,13;11]], which is a subcode of [[27,8,13;11]] from arXiv:2207.05647.
- **Comparison:** 14 > 13 and 14 <= 19, a strict improvement of +1.
- **Neighbouring cells, verbatim titles:**
  - `[[28,7,14-19;12]]` "subcode of [[28,8,14;12]] from arXiv:2207.05647"
  - `[[28,8,14-18;12]]` "from arXiv:2207.05647"
  - `[[27,8,13-17;11]]` "from arXiv:2207.05647"
  - `[[27,7,13-18;11]]` "subcode of [[27,8,13;11]]"
  - `[[29,7,13-20;11]]` "lengthening of [[27,7,13;11]] ..."
  - `[[28,6,13-20;11]]`
  - `[[28,6,12-19;8]]`
  - `[[27,6,12-19;9]]`
- **Row (28,7), by c:** 0: 8; 1: 9; 5: 10; 7: 11; 9: 12; 11: 13; 12: 14.

## 3. Does the page's own propagation already give d >= 14?

**No.** Every rule application I tested, including permissive ones, gives 13.

**The rules.** The page's legend lists eight rules:
- subcode [[n,k-1,d;c]]
- lengthening [[n+1,k,d;c]]
- puncturing [[n-1,k,d-1;c]]
- trivial [[n,0,n+1;n]]
- quantum shortening [[n-1,k+1,d-1;c]]
- increasing dimension [[n,k+1,d;c+1]]
- length reduction [[n-1,k,d;c+1]]
- teleportation [[n,k,d;k]]

Luo, Ezerman, Grassl and Ling (arXiv:2207.05647, Section 4, rules (1) to (8), read in mine/luo_ezerman_grassl_ling_2207.05647.txt) add the conditions:
- puncturing needs d > 1 and c < n-k;
- increasing dimension applies only to a *pure* code with q > 2 and c <= n-k-2;
- length reduction needs c <= n-k-2;
- shortening applies only to *pure* codes;
- "requiring more entanglement" [[n,k,d;c]] -> [[n,k,d;c+1]] is trivial.

**Scripts.** mine/parse.py parses all 3888 cells. mine/closure*.py iterate every rule to a fixed point, with c-monotonicity.

- **Naive run (mine/closure_naive_all_rules.txt).** I applied every rule to every cell, teleportation entries included. The result was 2700 values above the page's own upper bounds, and 25 at (28,7,11). I traced why this application is wrong:
  - The chains start at "using teleportation" cells, for example `[[8,1,6;1]]` -> length reduction -> `[[5,1,6;4]]`, which is above d_upper = 5.
  - Teleportation schemes are not pure stabilizer codes, so rules (6) to (8) do not apply to them. The prior panel's published novelty note says the same.
  - Lengthening or subcode into k = 0 cells is also invalid under the k = 0 (pure-distance) convention: lengthening adds a weight-1 stabilizer. That produced the one remaining violation, (11,0,0) = 6 > 5.
- **Corrected runs (mine/closure_final_k0_puncture.txt, mine/closure_final_general_puncture.txt).** With those two exclusions there are zero violations of page upper bounds, and the closure at (28,7,11) is **13**. This holds whether puncturing is allowed for all k or only for k = 0. Keeping the k = 0 lengthening and subcode steps also gives 13 (mine/closure_no_teleport_general_puncture.txt).
- **Remaining anomalies explained.** The permissive closure exceeds the page's d_lower at only 4 listed cells: (22,11,11), (33,2,24), (33,3,24) and (34,2,24). Each comes from applying increasing dimension or shortening to a *lengthened*, and therefore impure, code, which rules (6) and (8) forbid. So they are artifacts of my permissive run, not missed page entries.
- **Direct filters on the page.** No rule increases d, and no rule decreases c, so only sources with d >= 14 and c <= 11 could matter. Results:
  - No non-teleportation cell has d_lower >= 14, c <= 11 and k >= 7 at any n <= 36.
  - The only such cells at all are k = 0 (n = 17, c = 11) and k = 2 (n = 21, c = 11). Neither has the ebit budget to reach k = 7.
  - For the k = 7, c <= 11 row, d_lower stays at 13 for every n from 27 to 36.
  - No qshort, incdim or length-reduction source exists with the required (n,k,d,c).
- **Teleportation cells with d >= 14** (for example [[27,4,14;4]], [[28,2,18;2]]) have k <= 4, and they cannot raise k without a classical [n,2k,d]_3 code. A [28,14,>=14]_3 code would be needed for (28,7,7), which does not exist at that distance.

## 4. Catalytic note (concern, not a fail)

- **The page's own statement:** "In the catalytic setting, the existence of a code [[n,k,d;c]] with c >= k > 1 implies the existence of a code [[n,k-1,d;c-1]]. We do not consider this case here."
- **Effect here:** applied to the listed `[[28,8,14;12]]`, this gives `[[28,7,14;11]]`. So in catalytic accounting the claim is already known.
- **Why it still passes:** the success criterion fixes c = rank(S J S^T)/2, which is the non-catalytic count, and the table is non-catalytic. In that sense the claim is a strict record. Any write-up should say plainly that it saves one ebit relative to the known non-catalytic `[[28,7,14;12]]`.

## 5. A stronger code from the same construction, nowhere in the record

- **Hull dimensions (mine/hermitian_hulls.txt).** I computed Hermitian hull dimensions of one-point Hermitian codes C(m) over GF(9) with my own GF(9) arithmetic. The affine values match Christensen et al. Table 2 and Example 2: m = 8, 11, 14 and 17 give `[[27,1,19;16]]`, `[[27,4,16;13]]`, `[[27,6,13;9]]` and `[[27,9,10;6]]`.
- **The extended m = 14 code.** Unscaled, it has k = 12 and hull 6, which gives `[[28,6,>=14;10]]_3`. It is pure, since every nonzero codeword has weight >= 14.
- **Scaling.** Scaling any one of the 27 affine columns by w lowers the hull to 5, which gives the claim. Scaling the extra coordinate leaves the hull at 6. This is the diagonal-scaling hull reduction of Luo et al. Theorem 4, and the hull-variation idea of H. Chen (arXiv:2206.14516).
- **Consequence.** The claim follows from `[[28,6,14;10]]` by the page's rule (6). That code is not on the page, not in any paper I found, not in this repo and not in any PR, so it is not prior art. The claimant could, however, claim more: (28,6,10), where the page has 12, and (28,6,11), where it has 13.

## 6. Literature (last 24 months, plus older where relevant)

| source | covers | effect on (28,7,11) |
|---|---|---|
| Luo, Ezerman, Grassl, Ling, arXiv:2207.05647 v2 (QIP 23:4, 2024), the table's source. Abstract page and full PDF read (text in mine/). | Qutrit Table 2 at n = 28 lists [[28,20,4;0]], [[28,14,8;6]], [[28,13,9;7]], [[28,12,10;8]], [[28,11,11;9]], [[28,10,13;12]], [[28,9,12;9]], [[28,8,14;12]], [[28,5,16;13]], [[28,4,17;14]], [[28,4,18;16]], [[28,4,19;18]], [[28,2,20;18]], [[28,1,21;19]], [[28,0,28;26]]. At n = 27 it lists [[27,8,13;11]], [[27,7,14;12]], [[27,4,16;13]], and others. Classical inputs are Magma BKLC codes and quasi-cyclic codes with large Hermitian hulls. | no [[28,7,>=14;<=11]] and no [[28,6,14;10]] |
| Christensen, Munuera, Pereira, Ruano, arXiv:2105.02166 v2 (Jan 2022; AMC, doi 10.3934/amc.2021072). Full PDF read. | EAQECCs from one-point Hermitian codes, affine length q^3 = 27 only, no extension. For q = 3: [[27,1,19;16]], [[27,4,16;13]], [[27,6,13;9]], [[27,9,10;6]], [[27,13,7;4]], [[27,16,4;1]]. | Best implication is [[28,7,13;10]] (incdim, then lengthen); never d >= 14 at c <= 11. Two of these entries exceed the page (see Concerns). |
| Li, Ezerman, Li, Ling, Sun, arXiv:2607.02170 (2 Jul 2026). Full PDF read (text in mine/); supplementary TSVs fetched once each (mine/si_table_V_ternary.tsv, mine/si_table_VII_lit_equal.tsv). | Compared against this page (accessed 15 Jun 2026) and the latest records: Cao–Li–Zhu, IEEE TIT 71(10), 2025; Liu–Li–Shi, AMC 19(2), 2025; Li–Li–Guan–Song, IJTP 63:221, 2024; Li–Zhu, DM 347, 2024; Fan et al., arXiv:2501.04921; and others. Its 14 new qutrit codes and 5 literature qutrit codes all have n <= 25: [[7,1,7;6]] ... [[25,3,20;22]], [[7,0,7;5]], [[7,2,5;3]], [[9,0,9;7]], [[15,2,13;13]], [[16,2,14;14]]. | none implies the cell (d too small or c too large) |
| Pereira, Pellikaan, La Guardia, de Assis, arXiv:1907.06357 (IEEE TIT 2021). Abstract read. | AG-code EAQECC families with Singleton defect 0 or 1, plus LCD towers with maximal entanglement. Over GF(9), defect 0 or 1 is impossible at n = 28, and maximal entanglement means c = n-k = 21. | none |
| Sok, Ezerman, Ling, arXiv:2512.17128 (Dec 2025; DCC 2026). Search snippets only. | Hermitian hulls of rational AG (MDS) codes. Over GF(9) these have length <= q^2+1 = 10. | none |
| arXiv:2607.03802 (TGRS Hermitian hulls), 2507.18361 (GRS EAQMDS), 2401.08195 (GRS propagation), 2404.04993 (Hermitian hulls that are MDS). Titles from arXiv API listing. | GRS/MDS families: over GF(9), length <= 10. | none |
| Lu, Yang, Liu, Fu, Guo, arXiv:2607.12242 v3 (Oct 2026). Abstract and first half of HTML read. | Stabilizer codes (c = 0) from Hermitian hulls of cyclic codes. Only ternary code named: [[80,64,6]]_3. | none |
| Ezerman, Grassl, Ling, Özbudak, Özkaya, arXiv:2405.15057 (IEEE TIT 71(1), 2025). Abstract read. | Stabilizer records from quasi-twisted codes (c = 0), added to codetables.de. | covered by the codetables check below |
| Zengin, Köroğlu, arXiv:2606.02137; DeFranco, Nemec, arXiv:2603.03182; Hu et al., arXiv:2605.05613; Wang, Luo, arXiv:2604.08843; EA-LRC preprints 2607.27091, 2608.06854, 2608.09886, 2608.17118, 2610.23889; Chen, arXiv:2206.14516 and 2206.13995; Luo, Ezerman, Ling, arXiv:2206.09782. Abstracts or snippets read. | binary-ring codes; non-stabilizer EA codes; constacyclic 3-designs; hull embeddings; locally recoverable codes; hull variation; propagation rules. None lists a qutrit [[28,...]] code. | none |
| Luo, Sok, Ezerman, Ling, "On propagation rules for EA quantum codes" (ISTC 2023), NTU repository PDF. | The repository's CDN returned **HTTP 403**; not retried. Its rules are summarised in Luo et al. Section 4. | not read |

**Searches I ran:**
- **Web search (US index):**
  - arXiv 2207.05647 authors;
  - EAQECC + Hermitian curve + AG + Hermitian hull + GF(9) qutrit;
  - "extended" one-point Hermitian codes + Hermitian hull + EAQECC, length q^3+1;
  - the exact strings "[[28,7,14;11]]" and "[[28,6,14;10]]" (no hits);
  - new qutrit EA codes 2025-2026 over F9 against the Grassl table;
  - "On Propagation Rules ...";
  - Li–Li–Guan–Song, "Hermitian self-orthogonal codes over F9";
  - Hermitian hull of one-point AG codes, q = 3, length 27;
  - H. Chen hull variation;
  - two-point Hermitian and Castle codes in an EA setting;
  - hull dimension of one-point Hermitian codes;
  - quasi-twisted and quasi-cyclic F9 EA records;
  - a Chinese-language query (纠缠辅助量子纠错码 Hermitian曲线 代数几何码), which surfaced only MDS-type EA papers in 电子学报 and 电子与信息学报 (lengths <= q^2+1);
  - the codetables.de qutrit QECC URL.
- **arXiv API, one GET each:**
  - `abs:"entanglement-assisted" AND abs:qutrit` (8 results)
  - `abs:"entanglement-assisted" AND abs:"Hermitian hull"` (15 results)
  - `abs:"entanglement-assisted" AND (abs:"algebraic geometry" OR abs:"Hermitian curve" OR abs:"AG codes")` (7 results)
  - Saved as mine/arxiv_q1.xml, mine/arxiv_q2.xml, mine/arxiv_q3.xml. No result reports a qutrit code at n = 27 to 30 that reaches the cell.
- **GitHub repository search, one GET:** `https://api.github.com/search/repositories?q=eaqecc`, saved as mine/gh_repos_eaqecc.json. It returned 5 repositories:
  - SI-EAQECCs-from-GECs (supplement of 2607.02170): qutrit n <= 25.
  - llm_guided_EAQECC_search (tree listing in mine/gh_tree_llm_guided_search.json): its qutrit witnesses are all k = 1, n <= 20 (for example n15_k1_c10_d14), and cannot reach k = 7 at c <= 11.
  - A V3R1T4S contributor's search repository, a 2023 arithmetic table, and a Lean formalisation: none lists a qutrit [[28,...]] code.

## 7. codetables.de qutrit stabilizer table (c = 0 sources)

- **Fetches** (one GET each, all HTTP 200): https://codetables.de/ (frameset), https://codetables.de/nav.html, https://codetables.de/QECC/index.html, and https://codetables.de/QECC/Tables_color.php?q=9&n0=28&n1=39&k0=0&k1=7 (2026-10-24T14:30:46Z; sha256 `7ee04786f0fee5d06b0f55bef24fc4c54d71462ec4238b01b075ed2bb8f06204`; footer "Last change: 23.05.2024"). Saved in mine/.
- **What would be needed.** A c = 0 source reaches (28,7,<=11) only as [[28+t, 7-u, >=14]]_3 with t + u <= 11 (length reduction t times, increasing dimension u times).
- **What the table has.** For n = 28 to 39 and k = 0 to 7, d_lower is at most 11. The one exception is [[38,0,14]], which would need t = 10 and u = 7, that is c = 17.
- **The page agrees.** All the needed cells for n <= 36 sit at d_lower <= 12.

## 8. This repo and its pull requests

- **TROPHY_CASE.md:** read; grep finds no "eaqecc", "qutrit", "entangle", "quantum" or "codetables" row. It does not list the EAQECC family.
- **known-knowns/eaqecc-qutrit-codetables-gaps/:** one package, `[[14,3,8;5]]_3` (README.md, INDEX.csv, panel/novelty.md read). With n = 14 and d = 8, it cannot propagate to d = 14, because no rule increases d.
- **Pull requests:** one GET each of
  `https://api.github.com/search/issues?q=repo:elder-plinius/V3R1T4S+is:pr+eaqecc&per_page=100` (14:18:47Z, HTTP 200, total_count 5, mine/gh_pr_eaqecc.json) and
  `...+is:pr+qutrit&per_page=100` (14:18:52Z, HTTP 200, total_count 5, mine/gh_pr_qutrit.json). Both return the same 5 PRs:

| PR | state | code | can it reach (28,7,11)? |
|---|---|---|---|
| #331 | closed | [[14,3,8;5]] | no: d = 8 cannot increase |
| #363 | open | [[33,1,31;24]] | no: c = 24, and no rule lowers c |
| #403 | open | [[16,4,8;4]] | no: d = 8 cannot increase |
| #404 | open | [[34,2,24;24]] | no: c = 24, and no rule lowers c |
| #405 | open | [[33,3,23;24]] | no: c = 24, and no rule lowers c |

None covers (28,7,11), and none implies it.

## Concerns

1. **Catalytic setting (section 4).** Under catalytic counting the cell is already implied by `[[28,8,14;12]]`. The claim is a record only in the non-catalytic sense that the table and criterion use.
2. **A stronger code from the same construction (section 5).** The unscaled extended Hermitian code gives `[[28,6,>=14;10]]_3`, which implies the claim and beats two more cells. I found it unpublished, so the claim is new. Even so, the claimed object is not the strongest consequence of its own construction, and its novelty rests on nobody having published the Hermitian hull of the extended m = 14 Hermitian code over GF(9).
3. **The table is not a complete census of the literature.** Christensen et al. (2021/22) give `[[27,6,13;9]]_3` and `[[27,9,10;6]]_3`, both above the page's (27,6,9) = 12 and (27,9,6) = 9, and neither is listed. My hull computation reproduces their c values. So "beats the table" does not by itself mean "beats the literature". For this cell I checked the literature directly, and these codes reach only d = 13 at c <= 11.
4. **Literature I could not read in full.** Paywalled journal versions (Cao–Li–Zhu 2025; Liu–Li–Shi 2025; Li–Li–Guan–Song 2024; Li–Zhu 2024) were covered only through the July 2026 comparison in arXiv:2607.02170. The ISTC 2023 PDF returned 403. Several abstracts were read only through search or fetch summaries. A search is never exhaustive.
5. **Housekeeping.** The fetch tool cached three arXiv PDFs (2105.02166, 2207.05647 and 2607.02170) in its own session cache, outside mine/. My scratch scripts ran from the session scratchpad and were then copied into mine/. Nothing else was written outside mine/ and this file.

pass: true
