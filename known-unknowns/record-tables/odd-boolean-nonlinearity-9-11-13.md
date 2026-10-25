# Odd-variable Boolean nonlinearity: exceed 242, 996 or 4040

📊 **Record tables** · standard · tractability ★★☆☆☆ · compute: laptop-hours to laptop-days for symmetry-restricted search and local modifications; a full Walsh certificate takes milliseconds to seconds · open as of 2026-10-25

## The problem

Claude Carlet, Marko Ðurasevic, Domagoj Jakobovic, Stjepan Picek and Luca Mariot, A Systematic Study on the Design of Odd-Sized Highly Nonlinear Boolean Functions via Evolutionary Algorithms (arXiv:2504.17666v1, April 2025; journal publication December 2025), describe maximum nonlinearity for odd n>7 as open. Table 1 gives unrestricted best-known values 242,996,4040 for n=9,11,13, and upper bounds 244,1000,4050. Nonlinearity is minimum Hamming distance to an affine Boolean function. The n=9 construction is credited to Kavut and Yücel. Direct sums of an n=9, nonlinearity-242 function with two- or four-variable bent functions already give 996 and 4040. These compositions belong to the bar. Author spellings here follow the cited preprint.

## What counts as a win

Supply the complete truth table of f:{0,1}^n→{0,1}, for n=9,11 or 13, with nonlinearity strictly greater than 242,996 or4040 respectively. No balancedness, rotation symmetry or algebraic-degree restriction is imposed. Report the full Walsh spectrum and the exact achieved nonlinearity; the checker recomputes it. Also strictly improve the best comparable published result at claim time, including compatible compositions of published objects. State whether the candidate is a composition and identify its components. Values in unmerged pull requests do not set the bar.

## How a win is checked

Validate 2^n Boolean table entries in explicitly specified lexicographic bit order. Apply the integer fast Walsh–Hadamard transform to (-1)^f(x). Compute NL(f)=2^(n−1)−max_a |W_f(a)|/2, which includes distances to both affine constants. Check Parseval sum_a W_f(a)^2=2^(2n) and compare the exact integer result with the threshold. This requires at most 8192×13 additions and no floating-point tolerance.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/html/2504.17666v1>

## Sources

- <https://arxiv.org/html/2504.17666v1>
- <https://link.springer.com/article/10.1007/s10710-025-09526-5>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Explore generalized rotation-symmetric orbits, but verify the expanded unrestricted truth table.
- Use incremental Walsh updates for small truth-table moves and optimize the largest coefficients first.
- Search secondary constructions from the n=9 examples while tracking exact spectral changes.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Balanced-function records do not set unrestricted thresholds.
- Semi-bent values are below the records here.
- A Walsh spectrum alone is not a function certificate; include the truth table.
- The established bent-function compositions already attain 996 and 4040.
- Re-check the literature before claiming; an arXiv search on 2026-10-25 found no improvement of 242, 996 or 4040.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/odd-boolean-nonlinearity-9-11-13.md
```

Already set up? Say `run V3R1T4S on odd-boolean-nonlinearity-9-11-13`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `odd-boolean-nonlinearity-9-11-13`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
