# Covering codes K_q(n,R) for q = 2, 3, 4 (hypercube domination, football pool): beat an upper bound in Kéri's tables

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours to laptop-days (local search and large-neighbourhood search with exact coverage counts; exhaustive verification over q^n words takes seconds for ternary and up to minutes for binary n <= 33 with a 1 GiB bit array) · open as of 2026-10-25

## The problem

K_q(n,R) is the minimum number of q-ary words needed so that every length-n word is within Hamming distance R of one of them. Gerzson Kéri's tables cover binary, ternary and quaternary cells. Kéri's ternary table (3_tables.pdf, file date 2011-11-24) gives 71 <= K_3(6,1) <= 73 and credits Laarhoven, Aarts, van Lint and Wille for the upper construction. Márk Marosi (arXiv:2608.19872) gives newer search methods and 83 improved bounds for alphabets 5 <= q <= 21. Tamal Maharaj (arXiv:2610.03760) gives K_4(8,2) <= 256 and K_4(6,2) <= 48. The target is a smaller explicit code for a still-open cell. Reference tables alone do not establish the full current frontier; compositions and later publications must also be checked.

## What counts as a win

Success means an explicit code C contained in Z_q^n with q in {2, 3, 4}, given as a list of distinct words, whose covering radius is at most R (every one of the q^n words lies within Hamming distance R of a codeword, checked exhaustively), for a cell inside the ranges of Kéri's tables (q = 2: n <= 33, 1 <= R <= 10; q = 3: n <= 14, 1 <= R <= 8; q = 4: n <= 11, 1 <= R <= 8), such that |C| is STRICTLY SMALLER (direction: min) than (a) the upper bound for (q, n, R) in Kéri's table re-fetched at verification time, read from the rendered PDF, and (b) every later published upper bound for that cell, including the values implied through K_q(n+1, R+1) <= K_q(n, R) and K_q(n+1, R) <= q * K_q(n, R) by newer codes (later bounds known on 2026-10-25: K_4(8,2) <= 256 and K_4(6,2) <= 48, Maharaj arXiv:2610.03760), found by a search of arXiv and Google Scholar for covering codes with the cell's parameters (2012-present). |C| must be at least the best published lower bound for the cell; a smaller code means a checker bug. Cells with a perfect code (key h) are closed. For compositions, include direct products and direct sums with added radii, plus valid coordinate-extension constructions. Include the best valid composition of published objects for the same parameters and metric in the bar, even if it is absent from a printed table. State whether the candidate is a composition. Identify its components and composition rule. Values in unmerged pull requests are not bars.

## Partial wins

- **p1:** A strictly smaller explicit code for a cell of Kéri's mixed binary/ternary table (mixed_tables.pdf, file date 2011-11-24), below that table's upper bound and any later published value, checked exhaustively in the same way.
- **p2:** A certified lower bound strictly above the best published lower bound for a cell with q in {2, 3, 4} (for example from a higher level of the Gijswijt-Polak semidefinite hierarchy), delivered as an exact rational dual certificate verified by a standalone exact-arithmetic checker that rebuilds the program from (q, n, R), as in Marosi's pipeline.

## How a win is checked

Parse the code (one word per line, symbols 0..q-1), assert the length n, the symbol range and distinctness, and count M. Method 1: mark the radius-R ball of every codeword in a q^n-entry array (M * sum_{j<=R} C(n,j)(q-1)^j updates) and confirm that no word is unmarked. Method 2 (shares no code with method 1): R rounds of coordinate-wise dilation of the code's indicator array, which computes no distances (one of the four checks Marosi used). Binary n <= 33 needs at most 2^33 bits (1 GiB); ternary n <= 14 needs about 4.8 million entries. Re-fetch Kéri's directory listing and the cell's PDF, read the cell from the rendered PDF, and repeat the literature search before claiming. Recompute comparison compositions using the same checker and resource metric.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://old.sztaki.hu/~keri/codes/>

## Sources

- <https://old.sztaki.hu/~keri/codes/>
- <https://old.sztaki.hu/~keri/codes/2_tables.pdf>
- <https://old.sztaki.hu/~keri/codes/3_tables.pdf>
- <https://old.sztaki.hu/~keri/codes/4-5_tables.pdf>
- <https://arxiv.org/abs/2608.19872>
- <https://arxiv.org/html/2608.19872>
- <https://arxiv.org/abs/2610.03760>
- <https://arxiv.org/abs/2511.02542>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Transfer Marosi's two searches (arXiv:2608.19872 Sections 4-5) to q = 2, 3, 4: a focused local search seeded with structured codes, and a large-neighbourhood search that scores every candidate codeword position at once by exact coverage counts computed with a coordinate-wise transform. Kéri's largest binary cell has 2^33 (about 8.6 * 10^9) words and the largest ternary cell 3^14 (about 4.8 * 10^6), so exact full-space coverage transforms fit on a laptop.
- Aim first at cells whose upper bound is an old direct sum or algebraic construction far above the sphere-covering bound (for example K_2(13,2) <= 128 from 1985 against a lower bound of 97, K_3(8,2) <= 81 against 54, K_3(8,3) <= 27 against 14); Marosi's largest gains came from cells whose tabulated bound was a direct sum.
- Prescribe automorphisms (cyclic shifts, a subgroup of coordinate permutations, a linear subcode acting by translation: the matrix method of Östergård and Kéri) so the code is a union of orbits, then solve the orbit set-cover exactly with CP-SAT or an ILP.
- Propagate every win automatically: a new code for (n, R) gives bounds for (n+1, R+1), (n+1, R) via the factor q, and direct sums with other table codes; sweep the neighbours before claiming each cell once.
- Moonshot cell inside the harvest: the football pool K_3(6,1) in [71, 73]; a 72-word ternary code of length 6 with covering radius 1 would improve the upper bound. It would not establish optimality against the reported lower bound 71.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- In text extraction of Kéri's PDFs the key letters and footnote marks are glued to the numbers (for example '2717' for an exactly known cell of 27 with marks); always read the cell from the rendered PDF.
- The q >= 5 cells moved in August 2026 (Marosi) and two q = 4 cells moved in October 2026 (Maharaj); Kéri's binary and quaternary tables date from 2009 and the ternary table from 2011, so a literature search is part of every claim and a tie is not a record.
- Covering radius is a maximum over all q^n words: sampling words is not a check.
- Count distinct codewords; duplicates do not count.
- Do not mix tables: unrestricted codes K_q(n,R) (this entry), linear covering codes and the length function l(r,R) (e.g. Davydov-Marcugini-Pambianco, arXiv:2511.02542), mixed binary/ternary codes (p1) and Lee-metric or Z4-linear Gray-image codes are different records.
- A code smaller than a certified lower bound means a checker bug.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/covering-codes-q2-q4-upper-bounds.md
```

Already set up? Say `run V3R1T4S on covering-codes-q2-q4-upper-bounds`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `covering-codes-q2-q4-upper-bounds`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
