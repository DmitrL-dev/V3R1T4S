# NIST Circuit Complexity AES tables: a smaller or shallower {AND, XOR, XNOR} circuit for the AES S-box, inverse S-box, MixColumns or InvMixColumns

⚡ **Algorithms** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-days for the search (SAT and heuristic linear-layer optimisation, basis enumeration); verification takes seconds · open as of 2026-10-25

## The problem

NIST's Circuit Complexity project maintains straight-line circuits for the AES S-box, inverse S-box, MixColumns and InvMixColumns over the gate set {AND, XOR, XNOR} with no constants (GitHub usnistgov/Circuits, data/slp/aes/README.md, with subfolders holding more files than the README tables). On 2026-10-25 the README lists, for the S-box, minimum #AND 28 (best total at #AND 28: 124 gates), minimum total 110 gates and minimum gate depth 11; for the inverse S-box, minimum #AND 28 (126 gates at #AND 28), minimum total 112 and minimum gate depth 13; for MixColumns, 88 XOR (depth 5), 90 (depth 4) and 97 (depth 3); for InvMixColumns, 91 XOR (depth 15), 107 (depth 6) and 119 (depth 5). The CSRC page asks for external contributions on a wish list: S-box and inverse S-box with A <= 27, G <= 100, or G <= 120 with GD <= 12; MixColumns with G <= 86, or G <= 93 at GD 3; inverse MixColumns with G <= 105 at GD <= 5. These are construction bounds, not optimality results; contributors are credited in the repository tables. The repository changes often (commits on 2026-10-15 and 2026-10-16).

## What counts as a win

Success means a circuit, given as a list of 2-input gates of types AND, XOR and XNOR only (NIST Circuit File Format, or one 'GATE out in1 in2' line per gate), with no other gate types and no constants, that computes exactly FIPS 197 SBox(), InvSBox(), MixColumns() or InvMixColumns() under the NIST files' bit conventions (U0 and S0 are the most significant bits of the S-box input and output byte; for [inv]mixcols x_(8b+r) and y_(8b+r) are bit r, LSB = 0, of byte b), verified on all 256 inputs for [inv]SBox and as an exact GF(2)-linear map for [inv]MixColumns, and that meets at least one wish-list target on https://csrc.nist.gov/Projects/circuit-complexity/list-of-circuits as re-fetched at claim time (direction: min in every case; on 2026-10-25: (a) [inv]SBox with #AND <= 27; (b) [inv]SBox with #gates <= 100; (c) [inv]SBox with #gates <= 120 and gate depth <= 12; (d) MixColumns with #XOR <= 86; (e) MixColumns with #XOR <= 93 at gate depth 3; (f) InvMixColumns with #XOR <= 105 at gate depth <= 5). The metric must also strictly improve the best comparable circuit in the live README, the subfolder files, the CSRC page and later publications, under the same gate model. The verifier recomputes all metrics: #gates counts every AND, XOR and XNOR; gate depth is the longest input-to-output path counted in gates; AND depth is the largest number of AND gates on any path.

## Partial wins

- **p1:** An [inv]SBox circuit with fewer total gates than the live minimum for that direction (110 for SBox and 112 for InvSBox on 2026-10-25), at any #AND and any depth, verified as in the success criterion.
- **p2:** An [inv]SBox circuit whose #AND equals the live minimum (28 on 2026-10-25) and whose total gate count is strictly below every listed circuit with that #AND (124 for SBox and 126 for InvSBox on 2026-10-25).
- **p3:** A MixColumns or InvMixColumns circuit with strictly fewer XOR gates than every listed circuit of the same function whose gate depth is at most the candidate's depth (on 2026-10-25: MixColumns 88 at any depth, 90 at depth <= 4, 97 at depth 3; InvMixColumns 91 at any depth, 107 at depth <= 6, 119 at depth 5).
- **p4:** An [inv]SBox circuit with gate depth strictly below the live minimum for that direction (11 for SBox and 13 for InvSBox on 2026-10-25) at any size, or with AND depth 3 and at most 34 AND gates (the listed AND-depth-3 circuits use 35).

## How a win is checked

Parse the gate list; reject any gate type other than AND, XOR and XNOR, any wire used before it is defined or defined twice, and any constant. Evaluate the gates in order. [inv]SBox: compare all 256 inputs with the FIPS 197 tables, most significant bit first (calibrate on the listed aes-sbox-a32-ad5-g110-gd22-xx78-3 and aes-mixcols-xor88-depth5 files first). [inv]MixColumns: require XOR gates only, feed the 32 unit vectors and compare the resulting 32x32 GF(2) matrix with the byte matrices [02 03 01 01; 01 02 03 01; 01 01 02 03; 03 01 01 02] and [0e 0b 0d 09; 09 0e 0b 0d; 0d 09 0e 0b; 0b 0d 09 0e] in the files' bit convention (calibrate on a listed file first). Compute #AND, #gates, gate depth and AND depth in one pass, then compare with the live README tables, the subfolder listings (file names encode A, AD, G, GD) and the CSRC page, all re-fetched just before claiming. Seconds on any machine. Condition the comparison bar on the selected target depth or AND budget. For partial p2 compare total gates at the best AND count; for p3 compare XOR counts at depth no greater than the candidate. For p4 compare minimum gate depth without a size limit, or AND count at AND depth at most 3 for its second route.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://raw.githubusercontent.com/usnistgov/Circuits/master/data/slp/aes/README.md>

## Sources

- <https://csrc.nist.gov/Projects/circuit-complexity/list-of-circuits>
- <https://github.com/usnistgov/Circuits>
- <https://raw.githubusercontent.com/usnistgov/Circuits/master/data/slp/aes/README.md>
- <https://github.com/usnistgov/Circuits/tree/master/data/slp/aes>
- <https://www.cs.yale.edu/homes/peralta/CircuitStuff/CMT.html>
- <https://tches.iacr.org/index.php/TCHES/article/view/8346>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Treat the listed circuits as data: several 2026 entries were 'derived therefrom via linear optimization' of contributed circuits. Re-optimise the top and bottom linear layers of each listed S-box with exact or randomised linear-circuit methods (Boyar-Peralta exploring all ties, RNBP, Maximov-Ekdahl depth-bounded search, SAT-based exact SLP for small blocks) while keeping the nonlinear core fixed.
- Enumerate tower-field and basis choices (polynomial or normal bases for GF(2^2), GF(2^4) and GF(2^8), and the isomorphism matrices) as Canright and Boyar-Peralta did, now with modern SAT/MaxSAT optimisation of each linear layer; the best basis for G need not be the best for A or GD.
- For A <= 27, study how the A28 circuits beat the classical split of 32 ANDs (three GF(2^4) multiplications at 9 ANDs each plus a 5-AND GF(2^4) inversion), and search for shared bilinear products across the multiplications with multiplicative-complexity tools for 4- to 6-bit functions.
- MixColumns is a byte-circulant matrix: impose its 4-fold rotation symmetry to shrink an exact bounded-depth SAT search (depth 3 is the natural first target), then break the symmetry. For InvMixColumns, seed from the factorisation of InvMixColumns as MixColumns times a sparse matrix.
- Run many diversified searches in parallel and keep one Pareto archive over (A, AD, G, GD); improvements in one coordinate often appear as by-products of searching another.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The repository moves fast (commits on 2026-10-15 and 2026-10-16 alone). Re-fetch the README, the subfolder listings, the commit log and the CSRC page immediately before claiming; the CSRC page and the README can differ.
- Gate set: NOT, NAND, NOR, OR, MUX and constant inputs are not allowed. Maximov-Ekdahl's 102-gate S-box and Canright's 120-gate S-box use other gates and are not comparable.
- Bit order: U0/S0 are the most significant bits for the S-boxes, and MixColumns uses x_(8b+r) = bit r of byte b. A circuit correct under another convention computes a different function until its wires are permuted, and the claim must be about the circuit as submitted.
- The README tables show selected circuits only; the subfolders hold more files. Compare against every file and the CSRC page, and recompute metrics yourself rather than trusting file names.
- Change-of-basis layers count: a tower-field S-box must take and return standard AES bytes.
- Novelty: AI-assisted search is active on this exact table, so the window is short; also check ePrint and arXiv for 2026 AES circuit papers. The maintainers prefer wish-list targets to small increments, so a partial win may beat the table without being listed by them.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/algorithms/nist-aes-circuit-records.md
```

Already set up? Say `run V3R1T4S on nist-aes-circuit-records`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `nist-aes-circuit-records`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
