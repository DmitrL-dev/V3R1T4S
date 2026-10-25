# Lottery numbers L(n,6,6,2) for n >= 71: fewest 6-number tickets that guarantee a 2-match prize (UK-lottery problem, past the published range)

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours to laptop-days (constraint programming or SAT on a local model around a maximal independent set, as in Cushing-Stewart; checking an explicit design means scanning C(n,6) draws, about 1.3e8 at n = 71 and 6.2e8 at n = 90, which takes seconds to minutes) · open as of 2026-10-25

## The problem

L(n,6,6,2) is the minimum number of six-number tickets such that every six-number draw from n numbers shares at least two numbers with some ticket. David Cushing and David I. Stewart, 'Applying constraint programming to minimal lottery designs' (arXiv:2307.12430v3, 17 Jun 2024; journal version Constraints 2024, doi:10.1007/s10601-024-09368-5), determine L(n,6,6,2) for every n <= 70, including L(70,6,6,2) = 35; their program's output for n = 71 reads 'Conjecture L(71,6,6,2) = 38'. Their lower bounds rest on a Prolog constraint-programming run without a proof certificate. As of 2026-10-25 a search found no later paper settling any n >= 71. The target is an exact value for some 71 <= n <= 90: an explicit design plus a certified proof that one ticket fewer is impossible. Upper bounds alone are already covered by the lottery-design partial win of covering-designs-record.

## What counts as a win

Success means the EXACT value of L(n,6,6,2) for at least one n with 71 <= n <= 90, established by both of the following. (a) An explicit list of L tickets (6-subsets of {1..n}) such that every one of the C(n,6) draws meets some ticket in >= 2 numbers, checked exhaustively. (b) A proof that no design with L - 1 tickets exists, whose computational part comes with a certificate an independent tool checks: an LRAT/DRAT proof checked by cake_lpr or drat-trim, a VeriPB proof, or an exact ILP infeasibility certificate re-verified in rational arithmetic. Any mathematical reduction must be written out in full or cited to a published lemma (e.g. Cushing-Stewart arXiv:2307.12430 Section 3). L must also be no larger than the live upper bound for the cell. Read that bound from coveringrepository.com ((v,k,t,m) = (n,6,2,6)), lottodesigns.altervista.org, and any later paper citing Cushing-Stewart, all re-fetched at claim time. Before claiming, the claimant must also check that no later paper has already settled the cell. The first target is n = 71 (L(71,6,6,2) >= 35 by monotonicity; the published program conjectures 38).

## Partial wins

- **p1:** A certified lower bound: for some n in 71..90, a proof (same certificate standard as success criterion part b) that L(n,6,6,2) is STRICTLY greater than max(35, the Füredi-Székely-Zubor bound for n) and strictly greater than any lower bound published for that n after 2024-06-17.
- **p2:** A certificate-backed re-proof of a Cushing-Stewart value for some n in 60..70 (e.g. L(67,6,6,2) = 34 or L(70,6,6,2) = 35): an explicit design plus an LRAT/DRAT, VeriPB or exact-ILP certificate for the non-existence of a design one ticket smaller. The published proofs rest on an uncertified Prolog CP run, so this is the first independently checkable proof of that value.

## How a win is checked

Upper part: parse the tickets and assert each has 6 distinct numbers in 1..n. Enumerate all C(n,6) draws, or equivalently build the graph G whose edges are pairs sharing a ticket and confirm that G has no independent set of size 6 (a clique search in the complement, run as a second, independent check). Lower part: run the certificate through its checker (cake_lpr or drat-trim for LRAT/DRAT, VeriPB for pseudo-Boolean proofs, exact rational re-verification for ILP), and confirm the encoding's generator matches the written reduction. Re-derive the reduction lemmas against Cushing-Stewart Section 3. Recompute the FSZ bound and the monotonicity bound. Re-fetch coveringrepository.com and lottodesigns.altervista.org for the cell, and search arXiv/Google Scholar for papers citing arXiv:2307.12430.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2307.12430>

## Sources

- <https://arxiv.org/abs/2307.12430>
- <https://arxiv.org/pdf/2307.12430>
- <https://doi.org/10.1007/s10601-024-09368-5>
- <https://coveringrepository.com/>
- <https://lottodesigns.altervista.org/>
- <https://lottodesigns.altervista.org/Improvements.html>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Start at n = 71. The published program already reduces it to a few exceptional configurations (Figure 1 of arXiv:2307.12430: four 'bad (r,s)' tuples and one degree-pattern exception). Encode only those as SAT/CP with symmetry breaking, and emit LRAT or VeriPB certificates.
- Re-implement the paper's local model (structure around a maximal independent set I, with |I| <= 5 forced because 6 independent numbers form a losing draw) in a certificate-producing solver (CaDiCaL plus LRAT, or RoundingSat/VeriPB) rather than Prolog CP. Calibrate by re-proving n = 66 to 70 first (partial win p2).
- Equivalent form: L(n,6,6,2) is the fewest 6-cliques whose union graph on n vertices has independence number <= 5. The Turán-type and Shannon chromatic-index arguments in the paper are the obstruction side. Look there for the extra lemma that kills the n = 71 exceptions.
- Upper side: a non-disjoint-union design with 37 tickets at n = 71 would also refute the program's conjecture of 38. Try local search seeded from the (14,14,14,14,15) union. Note that an upper-bound record by itself is already a covering-designs-record partial win (lottery (v,k,t,m) tables); here it counts only as part of an exact value.
- Sweep n = 71..90 in order. L is monotone in n, so each settled value is a lower bound for the next. n = 90 (SuperEnalotto shape) is the showpiece cell.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Do not confuse L(n,k,p,t) (lottery designs) with covering designs C(v,k,t). The repositories write lottery designs as (v,k,t,m), with t the guarantee and m the draw size, so this entry's cells are (n,6,2,6).
- The Cushing-Stewart lower bounds are not certificate-backed, and Bate-van Rees 1998 has known gaps. Do not cite either as a checker.
- The FSZ minimum is over unequal partitions: the balanced partition overstates it.
- The live repository value for (n,6,2,6) may already be below the disjoint-union bound. Read it before quoting an upper bound.
- The Springer journal version (Constraints, 2024) was not read for this entry. Check it for any added values or corrections before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/lottery-numbers-l-n-6-6-2-beyond-70.md
```

Already set up? Say `run V3R1T4S on lottery-numbers-l-n-6-6-2-beyond-70`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `lottery-numbers-l-n-6-6-2-beyond-70`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
