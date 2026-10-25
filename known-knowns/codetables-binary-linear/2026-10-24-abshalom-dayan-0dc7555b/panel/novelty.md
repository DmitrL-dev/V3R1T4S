# Novelty skeptic: [31,18,10] over GF(9)

context: subagent (Claude Agent tool, model claude-opus-5-5), given only claim/ and public sources

Claim under review (claim/CLAIM.md): G in claim/object/code_q9_n31_k18_d10.json generates a linear [31,18,10] code
over GF(9), against the codetables.de cell (q,n,k) = (9,31,18) with lower bound 9 and upper bound 12. The construction
(from the JSON and claim/rebuild/build_code.py) is Construction X: C(D,17P) inside C(D,20P), one-point codes of the
Hermitian curve y^3 + y = x^4 over GF(9) at its 27 affine points, plus a [4,3] Reed-Solomon tail.
Scope of this review: whether a [31,18,>=10] GF(9) code is already known. I did not judge whether d = 10 is computed
correctly (another skeptic covers that).

## Verdict

Novel as far as everything I could reach shows. The live table says 9; d = 10 beats it by +1, so this is not a tie,
and it stays under the upper bound 12. Neighbouring cells do not give 10 by shortening, puncturing, subcode or
extension. I found nothing in this repo, its pull requests, LinCodeEvolve or the last 24 months of literature that
reaches d >= 10 at [31,18] over GF(9). This passes only if the correctness skeptic confirms d = 10.

## 1. Live primary table (one GET, no retry)

- URL: https://codetables.de/BKLC/BKLC.php?q=9&n=31&k=18
- Command: curl -sS -A "V3R1T4S-research-agent (honest single fetch)", a single request.
- UTC time: started 2026-10-24T13:21:24Z, finished 2026-10-24T13:21:24Z. Server `date:` header: "Sat, 24 Oct 2026 13:21:24 GMT".
- HTTP status: 200, 3395 bytes, no challenge page (headers: x-ws-ratelimit-remaining: 999).
- sha256 of the saved page: 1ab4ec8f7b8516b1e52d16ea00ef697c16be779f8e63150c645f7b4d92639c80
  (byte-identical to claim/table/bklc_q9_n31_k18.html, fetched 2026-10-24T12:09:31Z, so the cell did not change in between).
- Bound text, verbatim from the HTML:
  `<H3>Bounds on linear codes [31,18] over GF(9)</H3><TABLE><TR><TD>lower bound:</TD><TD>9</TD></TR><TR><TD>upper bound:</TD><TD>12</TD></TR></TABLE>`
- Construction shown: [41,29,9] BCH code (d = 5, b = 34), then a [41,28,9] subcode, then shortening at {32..41}, giving [31,18,9]; "last modified: 2001-12-17".
  Brouwer section (as of 2007-02-13): "Lb(31,18) = 9 is found by shortening of: Lb(41,28) = 9 XL"; "Ub(31,18) = 12 ... Ub(17,4) = 12 MPa".
- Files: work-novelty/mine/cell.html, cell.headers, cell.result, cell.sha256, cell.time_start, cell.time_end.

Comparison: claimed d = 10 > live lower bound 9, and 10 <= upper bound 12. Strict improvement of +1.

## 2. Neighbouring cells (one GET each, no retries)

| cell (q=9) | UTC fetch | HTTP | bytes | sha256 | verbatim bounds | how the table builds it |
|---|---|---|---|---|---|---|
| [30,17] | 2026-10-24T13:22:05Z | 200 | 3586 | f88a3e065dfe4558ebead149907a45b30de468b1e0f0116460bbf8c925920cca | lower bound: 10, upper bound: 12 | AG code from a plane curve, divisor of degree 2 (2003-10-23) |
| [30,18] | 2026-10-24T13:22:05Z | 200 | 3055 | 1d0f09a5fac1390d0d2d30ad781304caa3ee6c99de79e85af079766bd80707a9 | lower bound: 9, upper bound: 11 | shortened [41,29,9] BCH (2003-10-21) |
| [31,17] | 2026-10-24T13:22:05Z | 200 | 3510 | 920f1b71ab28952457d69a6f2ef2b422cba4790e647ba66d4f42f990965e524e | lower bound: 10, upper bound: 13 | [37,21,12] RS-subfield subcode, punctured, shortened (2001-12-17) |
| [31,19] | 2026-10-24T13:22:06Z | 200 | 3379 | 8b12a6f68c3a3671c51238613754dd33b913b93f78b0957501f9480d2715171a | lower bound: 9, upper bound: 11 | shortened [41,29,9] BCH (2003-10-21) |
| [32,18] | 2026-10-24T13:22:06Z | 200 | 3510 | a9dc5cec9d64a438b6461cc6425a6e77bce32b912a7a271cf23659030b8255fa | lower bound: 10, upper bound: 13 | [37,21,12], punctured, shortened (2001-12-17) |
| [32,19] | 2026-10-24T13:22:06Z | 200 | 3395 | 046bcdd475bd50f284382faa704382c748885ef8b22f02f48c9a9038e1be7bca | lower bound: 9, upper bound: 12 | BCH subcode, shortened (2001-12-17) |

All six URLs have the form https://codetables.de/BKLC/BKLC.php?q=9&n=N&k=K. Files: work-novelty/mine/nb_nN_kK.{html,headers,result}.

Does the table's own propagation already give [31,18,10]? No:
- shortening [32,19,9] gives [31,18,9];
- puncturing [32,18,10] gives [31,18,9];
- a subcode of [31,19,9] gives [31,18,9];
- extending [30,18,9] gives [31,18,9] (the table records nothing higher);
- [30,17,10] and [31,17,10] have k = 17, and no monotone rule raises k at fixed d.
What the claim implies for neighbouring cells is consistent with every upper bound: shortening gives [30,17,10] (ub 12),
puncturing gives [30,18,9] (ub 11), and a subcode gives [31,17,10] (ub 13). So no table cell contradicts the claim.

Extra context, two cells outside the neighbour list, one GET each (public web):
- https://codetables.de/BKLC/BKLC.php?q=9&n=27&k=18, 2026-10-24T13:30:50Z, HTTP 200, 2905 bytes, sha256
  d453e304de874e141b6e489c3ff7112b48d5af535bec53150dd5bfd4ae7adb6e, "lower bound: 7", "upper bound: 9" (shortened XL code, 2001-12-17).
- https://codetables.de/BKLC/BKLC.php?q=9&n=27&k=15, 2026-10-24T13:30:50Z, HTTP 200, 3217 bytes, sha256
  7181f66dbf0f15af2a84204cf218f74021b70a0b5058c86a13f2a1877ad54704, "lower bound: 10", "upper bound: 11" (AG code on the
  Hermitian curve 2x^4 + y^3 z + y z^3, degree-3 divisor, shortened from [28,16,10]).
- Files: work-novelty/mine/ctx_n27_k18.*, ctx_n27_k15.*

## 3. Other table copies

- Bayreuth copy of Grassl's GF(9) table: https://algorithm.uni-bayreuth.de/en/research/Coding_Theory/Bounds/q9.html,
  fetched once at 2026-10-24T13:28:45Z, HTTP 200, 328297 bytes, sha256 a17eabc5deb6deb2c7f50d4994d8fb24730e3486163b3fbbaaad7ca4f8efa376,
  Last-Modified "Wed, 16 Jun 2021 12:33:41 GMT". Row n=31, column k=18 reads "9 - 12". Rows 30 and 32 match the live
  neighbours: [30,17] "10 - 12", [32,18] "10 - 13". File: work-novelty/mine/bayreuth_q9.html.
- MinT (https://mint.sbg.ac.at/): one request at 2026-10-24T13:27:35Z failed with curl error 28, connection timed out
  after 30 s, http_code=000. Not retried. MinT is unchecked.
- Kohnert's "List of new Linear Codes" (https://mathe2.uni-bayreuth.de/axel/new_linear_codes.html, opened with WebFetch):
  covers q = 2, 3, 4 and 8 only; no GF(9) section; last update 10 Oct 2005.

## 4. This repo (published results) and its pull requests

- TROPHY_CASE.md: no linear-code rows at all; its families are graphs, constant-weight codes, matrix multiplication,
  Lehmer, VNN-COMP, RobustBench and cipher commitments. Nothing over GF(9).
- known-knowns/codetables-binary-linear/: three published results, all binary: q=2 [173,17,72], [175,25,61] and
  [213,26,77] (from their INDEX.csv files). Nothing over GF(9).
- GitHub search API, one GET each, all HTTP 200, run 2026-10-24T13:24:06Z to 13:24:30Z, User-Agent as above.
  Saved in work-novelty/mine/gh_pr_*.json.

| query (repo:elder-plinius/V3R1T4S is:pr ...) | total | result for (9,31,18) |
|---|---|---|
| `codetables`, page 1 (100 items) | 118 | none |
| `codetables`, page 2 (18 items; a different page, not a retry) | 118 | none |
| `"GF(9)"` | 6 | none; all are qutrit EAQECC PRs (#331, #363, #403, #404, #405) or AME (#619) |
| `q=9` | 33 | none |
| `hermitian` | 6 | none; EAQECC/AME/qubit PRs |
| `"31,18"` | 0 | none |

  Every PR body was scanned for GF(9), GF(3^2), F_9, q = 9, [31,18 and q9_n. The only hits are the qutrit EAQECC
  claims, which use GF(9) Hermitian hulls for a different table. #363 mentions in passing that its run found "GF(9)-linear
  ... codes elsewhere" beating the EAQECC table, explicitly not claimed. The classical non-binary codetables PRs are
  GF(4) [157,10,102], [160,11,102], [163,11,104] (#498-#500, earlier #95-#101) and Delsarte LP upper-bound claims over
  GF(4), GF(5), GF(7) and GF(8) (#503-#508). No PR covers q = 9 classical linear codes, and none covers (9,31,18).

## 5. Literature and web (last 24 months emphasised; older where relevant)

Searches run (WebSearch unless stated), with what they found:
1. "LinCodeEvolve arXiv 2609.37056 linear codes codetables": arXiv:2609.37056 (Seddas, Shashkov, Viazovska, Abbe,
   29 Sep 2026) reports seven binary codes: [172,21,66], [173,20,68], [176,21,68], [181,21,70], [184,21,72],
   [189,22,72] and [200,21,77], plus 22 derived binary entries. All are binary, so the GF(9) code is neither one of
   them nor derived from them (criterion item 4).
2. "new linear codes over GF(9) improving Grassl table minimum distance 2025 2026": no 2025-26 GF(9) classical
   improvements. Found Daskalov, Metodieva and Hristov 2004 (Probl. Inf. Transm. 40), Bierbrauer-Gulliver "New linear
   codes over F_9" (AJC v21), and Okazaki-Maruta / Kumegawa-Okazaki-Maruta on [n,4,d]_9. All are low-dimension
   (k <= 8) work that predates or is already reflected in the table; this cell is unchanged since 2001-12-17.
3. "[31,18,10]" with GF(9) / F_9 / F9: no hit for these parameters anywhere.
4. Construction X with Hermitian codes over GF(9) (two phrasings, plus a Chinese-language query): only quantum
   Construction X (arXiv:1906.04964, 1312.6064, 2405.15057), Duursma-Kirov two-point Hermitian codes
   (arXiv:1004.1752), Hermitian codes from higher-degree places (arXiv:1206.4480), and improvements of Hermitian AG
   code parameters (arXiv:0709.1983). None gives a classical [31,18,10]_9.
5. "Machine Learning Discovers New Champion Codes" (arXiv:2512.13370, Dec 2025; npj AI Mar 2026), opened: searched
   F_7 and F_8 only; F_9 is named as future work.
6. arXiv:2608.18664 (abelian codes via shift bounds and genetic algorithms, Aug 2026), opened: records over F_3 and
   F_4 only.
7. arXiv:2607.02170 (generalized extended codes, EA qubit and qutrit codes) and arXiv:2607.12242 (Hermitian hulls of
   cyclic codes), opened: their improvements are quantum and EA-quantum table entries, not classical GF(9) entries.
   For 2607.12242 I read the first 100k characters of the HTML only.
8. arXiv:2604.12499 (cyclic AG codes on the Hermitian curve, Apr 2026), opened: length q^2 - 1 = 8 over F_9; no records claimed.
9. arXiv:2509.03337 (new bounds for linear codes with a codeword of weight w), opened: restrictions, not constructions.
10. arXiv API (export.arxiv.org, one GET each at https after an HTTP-to-HTTPS 301; files work-novelty/mine/arxiv_q1..q5.xml):
    - q1 abs "construction X" AND Hermitian: 4 results, all quantum;
    - q2 abs "linear codes" AND GF(9)/F_9: 2 results, both additive codes;
    - q3 abs "best known" AND "linear codes" AND new/improve: 31 results; the only 2026 record paper is LinCodeEvolve (binary);
    - q4 abs codetables / "code tables" / "Grassl's table(s)": 80 results; from 2024-10-24 onward, nothing classical over F_9;
    - q5 AG/Hermitian codes AND best known/record/new codes/improve: 3 results since 2024-10, none relevant.
11. GitHub: Foundation-0/gfq-codes, a project targeting GF(3)-GF(9) table gaps, surfaced by search. Opened its page,
    its git tree and commits via the API (one GET each, 2026-10-24T13:32:22Z), and four raw notes files (one GET each;
    work-novelty/mine/gfq/). It has three commits (2026-10-19), and codes/ holds only a README: no codes. Its own
    (unverified) scouting note says "Linear codes over GF(3)-GF(9): still open". It also says codetables.de's newest
    dated update is 24 May 2024 (quantum codes), and that Grassl's 2025-26 arXiv papers are on other topics.
    A web search for GitHub plus [31,18] plus GF(9) found nothing else.

## Concerns

- The construction uses textbook ingredients: 1990s-era Hermitian one-point codes and Construction X. It is somewhat
  surprising that the table never had it. But the live cell, the 2021 Bayreuth mirror, the propagation check and every
  search agree that no [31,18,>=10]_9 is recorded.
- The table's [27,18] cell is only 7. So the generic Construction X bound min(d(C17), d(C20) + 2) gives
  min(10, 7 + 2) = 9, not 10. The claimed d = 10 therefore depends on the specific tail: every weight-7 word of
  C(D,20P) outside C(D,17P) must get a tail of weight >= 3. Alternatively C(D,20P) would have d >= 8, which would itself
  beat the [27,18] cell. That is the correctness skeptic's question, but it is the load-bearing point. If exact
  enumeration does not confirm d = 10, novelty is moot.
- MinT was unreachable (one timeout, no retry). Paywalled full texts (Springer/IEEE: Daskalov et al. 2004,
  Bierbrauer-Gulliver) were judged from abstracts. Both are low-dimension (k <= 8) work, and the cell has been
  unchanged since 2001.
- GitHub PR coverage rests on keyword search. A PR naming none of codetables, GF(9), q=9, hermitian or "31,18" would be missed.
- My first neighbour loop failed locally. zsh did not split "30 17" into two words, so curl got a URL with a space and
  exited with error (3), "URL rejected", before connecting: http_code=000, 0 bytes, no request sent. Recorded in
  work-novelty/mine/neighbour_loop_bug.txt. The six real neighbour GETs above were each the first and only request to
  their URL.
- The claim's target_id "codetables-binary-linear" covers non-binary q in this bank (criterion text says GF(q)). The
  label is misleading but not disqualifying.

pass: true
