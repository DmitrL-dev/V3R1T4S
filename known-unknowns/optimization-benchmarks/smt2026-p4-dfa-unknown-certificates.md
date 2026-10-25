# SMT-COMP 2026 P4/DFA bit-vector holdouts: one exact SAT model or UNSAT certificate

🚚 **Optimization benchmarks** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours to laptop-days using alternative preprocessing and solver configurations; require model/proof checking within laptop-hours · open as of 2026-10-25

## The problem

The SMT-COMP 2026 benchmark metadata (benchmarks-2026.json.gz in the SMT-COMP/smt-comp.github.io repository) gives SMT-LIB status 'unknown' to 79 QF_BV files of the family 20221214-p4dfa-XiaoqiChen (P4 / DFA packet-processing benchmarks by Xiaoqi Chen). Eight of them were run in the 2026 single-query track, 23 runs each, all Timeout or unknown: under QF_BV/20221214-p4dfa-XiaoqiChen/, Composition/compose.s4._bit8_na6_nr4_paired.smt2; StringMatching/string2x16.10._bit8_na6_nr3_paired.smt2; StringMatching/string4x16.2._bit8_na6_nr4_pairedtwobranch.smt2; StringMatching/string4x8.2._bit8_na6_nr3_paired.smt2; StringMatching/string4x8.3._bit16_na6_nr4_paired.smt2; StringMatching/string4x8.5._bit8_na6_nr3_paired.smt2; StringMatching/string4x8.8._bit16_na6_nr4_paired.smt2; TCP/tcp_full_split4_bit8_na6_nr4_paired.smt2 (4969 assertions). Re-checked on 2026-10-25: none of the 79 unknown-status files has a sat or unsat result in the 2026 single-query, model-validation, parallel or unsat-core logs, and those of the eight that appear in the 2023-2025 single-query logs were never decided there either. Public timeouts do not exclude private results.

## What counts as a win

Decide any one of the eight exact benchmark instances with an independently checked SAT model or UNSAT certificate. Identify the official SMT-LIB file path and SHA-256 of the unmodified downloaded input. A SAT answer needs a total assignment satisfying every assertion under exact SMT-LIB bit-vector semantics. An UNSAT answer needs a checked bit-blasting translation plus a replayable SAT proof, or another independently checkable theory proof. A bare solver answer, timeout change or solution of a simplified non-equivalent instance does not win.

## Partial wins

- **p1:** The same standard of certificate for any other file of the 20221214-p4dfa-XiaoqiChen family whose status is 'unknown' in the SMT-COMP 2026 benchmark metadata and which has no sat or unsat result in any SMT-COMP 2023-2026 log at claim time.

## How a win is checked

For SAT, parse the original SMT-LIB input and evaluate all terms under the submitted assignment using width-bounded integers, including signed operations, shifts, overflow and division-by-zero semantics. For UNSAT, independently reconstruct or certify every preprocessing/bit-blasting step, and validate the resulting LRAT or comparably explicit proof. Verify that the CNF proved UNSAT is equisatisfiable with the original assertions. Accept only certificates that a reviewer can check within hours on one laptop; search runtime itself is not evidence.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://raw.githubusercontent.com/SMT-COMP/smt-comp.github.io/master/data/benchmarks-2026.json.gz>

## Sources

- <https://smt-comp.github.io/2026/results/>
- <https://smt-comp.github.io/2026/results/qf_bitvec-single-query/>
- <https://raw.githubusercontent.com/SMT-COMP/smt-comp.github.io/master/data/benchmarks-2026.json.gz>
- <https://raw.githubusercontent.com/SMT-COMP/smt-comp.github.io/master/data/results-sq-2026.json.gz>
- <https://raw.githubusercontent.com/SMT-COMP/smt-comp.github.io/master/data/results-mv-2026.json.gz>
- <https://raw.githubusercontent.com/SMT-COMP/smt-comp.github.io/master/data/results-parallel-2026.json.gz>
- <https://raw.githubusercontent.com/SMT-COMP/smt-comp.github.io/master/data/results-uc-2026.json.gz>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Inspect the TCP and smaller string-matching constraints first, identify repeated automaton structure, and derive semantics-preserving preprocessing.
- Try word-level simplification before bit-blasting and switch between eager and lazy bit-vector reasoning.
- Use failed runs to choose a different encoding or branching strategy; prioritize SAT models because their certificates are smaller.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Unknown metadata alone is insufficient; check corresponding result logs.
- The original input must be downloaded and hashed before attacking or claiming; metadata is not input verification.
- A public timeout does not prove no private solution exists.
- Every UNSAT preprocessing and translation step needs independent checking.
- SMT-LIB status fields change between releases; check the current SMT-LIB release and the SMT-COMP results of the latest year before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/optimization-benchmarks/smt2026-p4-dfa-unknown-certificates.md
```

Already set up? Say `run V3R1T4S on smt2026-p4-dfa-unknown-certificates`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `smt2026-p4-dfa-unknown-certificates`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
