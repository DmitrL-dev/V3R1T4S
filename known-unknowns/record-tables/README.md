# 📊 Record tables

Codes, designs, packings and constructions measured against public tables.

**27 open problems**, easiest first. Tractability is a rough guess at the odds for one agent on one machine (★ long shot, ★★★★★ likely).

| Odds | Problem | Kind | Compute |
|---|---|---|---|
| ★★★★☆ | [Binary deletion codes: improve the best size at length 15 or 16, correcting two or three…](short-binary-multiple-deletion-code-records.md) | harvest | laptop-hours to laptop-days for local clique/independent-set search on 32768 or 65536 candidate words; certificate verification is seconds to minutes |
| ★★★★☆ | [Median selection networks: reduce a current comparator count for 10–25 inputs](median-selection-network-size-records.md) | harvest | laptop-hours to laptop-days for evolutionary search or SAT-assisted local replacement; exhaustive zero-one verification at n≤25 fits laptop memory and minutes to hours |
| ★★★☆☆ | [Binary (or small-q) linear codes beating codetables.de lower bounds](codetables-binary-linear.md) | harvest | laptop-hours |
| ★★★☆☆ | [Binary constant-weight codes A(n,d,w): new lower bounds in Brouwer's table](constant-weight-codes.md) | harvest | laptop-hours |
| ★★★☆☆ | [Binary minimal codes for secret sharing: shorten the dimension 10–13 records](binary-minimal-code-length-records.md) | harvest | laptop-hours to laptop-days for structured generator-matrix search; exact minimality checking over at most 8191 nonzero messages takes seconds to minutes with GF(2) rank tests |
| ★★★☆☆ | [Condorcet domains: a larger domain than the best published one for some n in 9..25](condorcet-domains.md) | harvest | laptop-hours |
| ★★★☆☆ | [Covering codes K_q(n,R) for q = 2, 3, 4 (hypercube domination, football pool): beat an up…](covering-codes-q2-q4-upper-bounds.md) | harvest | laptop-hours to laptop-days (local search and large-neighbourhood search with exact coverage counts; exhaustive verification over q^n words takes seconds for ternary and up to minutes for binary n <= 33 with a 1 GiB bit array) |
| ★★★☆☆ | [Covering designs C(v,k,t): beat a repository entry](covering-designs-record.md) | harvest | laptop-hours |
| ★★★☆☆ | [Erdos #757: (4,5)-set with Sidon density below 4/7](erdos757-sidon-in-45-sets.md) | harvest | laptop-hours |
| ★★★☆☆ | [Hadamard maximal determinant: new record determinants for orders n not divisible by 4](hadamard-maxdet-records.md) | harvest | laptop-hours |
| ★★★☆☆ | [Kissing number lower bounds in dimensions 25-48 (beat the max over ALL sources, not Cohn'…](kissing-number-dims-25-48.md) | harvest | laptop-hours |
| ★★★☆☆ | [Snake-in-the-box / coil-in-the-box records in dimensions 9-13](snake-coil-in-the-box.md) | harvest | laptop-hours |
| ★★★☆☆ | [Sorting networks: fewer comparators than the best known for n = 16..32](sorting-network-size-records.md) | harvest | laptop-hours |
| ★★★☆☆ | [Stable marriage: an instance of size n with more stable matchings than the best known (OE…](stable-marriage-max-stable-matchings.md) | harvest | laptop-hours (exact counting through the rotation poset is fast at these sizes; the search is local search over preference lists, embarrassingly parallel) |
| ★★☆☆☆ | [Erich Friedman Packing Center: beat a listed packing](friedman-packing-records.md) | harvest | laptop-hours |
| ★★☆☆☆ | [Heilbronn triangle problem: new best configurations (square, triangle, convex region)](heilbronn-records.md) | harvest | laptop-hours |
| ★★☆☆☆ | [Lottery numbers L(n,6,6,2) for n >= 71: fewest 6-number tickets that guarantee a 2-match…](lottery-numbers-l-n-6-6-2-beyond-70.md) | harvest | laptop-hours to laptop-days (constraint programming or SAT on a local model around a maximal independent set, as in Cushing-Stewart; checking an explicit design means scanning C(n,6) draws, about 1.3e8 at n = 71 and 6.2e8 at n = 90, which takes seconds to minutes) |
| ★★☆☆☆ | [Low-autocorrelation binary sequences: best-known merit factors for lengths 67-600](labs-merit-factor-records.md) | harvest | laptop-hours |
| ★★☆☆☆ | [Odd-variable Boolean nonlinearity: exceed 242, 996 or 4040](odd-boolean-nonlinearity-9-11-13.md) | standard | laptop-hours to laptop-days for symmetry-restricted search and local modifications; a full Walsh certificate takes milliseconds to seconds |
| ★★☆☆☆ | [Quadratic APN functions with coefficients in F2 in dimension 11: a seventh CCZ class](binary-coefficient-apn-dimension-11.md) | standard | laptop-days for a bounded structured counterexample search; roughly four million derivative evaluations per APN check, with invariant checks in minutes to hours; full classification is out of scope |
| ★★☆☆☆ | [Shannon capacity of odd cycles: larger independent sets in strong powers](shannon-capacity-odd-cycles.md) | harvest | laptop-hours |
| ★★☆☆☆ | [Shorter superpermutations for n=7 (below 5905) or n=8 (below 46188)](superpermutations-n7-n8.md) | harvest | laptop-hours |
| ★★☆☆☆ | [Small two-color Ramsey numbers: new lower bounds via explicit graphs](small-ramsey-lower-bounds.md) | harvest | laptop-hours |
| ★☆☆☆☆ | [AlphaEvolve-family analytic constants: autocorrelation inequalities and Erdos minimum ove…](alphaevolve-analytic-constants.md) | standard | laptop-hours |
| ★☆☆☆☆ | [Kissing number lower bounds in dimensions 9-23](kissing-number-low-dim.md) | moonshot | laptop-hours |
| ★☆☆☆☆ | [Larger cap sets in F_3^7 (beat 236) or F_3^8 (beat 512)](cap-set-dim7-dim8.md) | moonshot | laptop-hours |
| ★☆☆☆☆ | [Single-error-correcting codes for the Z-channel: beat 112, 198 or 379 (Sloane's 1zc chall…](z-channel-single-error-codes.md) | standard | laptop-hours to laptop-days (maximum-independent-set heuristics and exact solvers on graphs with 1,024 to 4,096 vertices; verification in milliseconds) |

← [All categories](../README.md)
