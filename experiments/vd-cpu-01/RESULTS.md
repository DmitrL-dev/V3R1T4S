# VD-CPU-01 r2: local engineering regression result

The frozen implementation passes all predeclared acceptance checks: 48 bases, 192 cases, A/B/oracle/expected-label agreement, 48 label-preserving metamorphic pairs, recognized always controls, and an exact deterministic second outcome matrix. Six manually constructed primitive/format unit tests also passed before freeze.

Measured run: 0.052486402 process CPU seconds, 12,800 KiB Linux peak RSS, 423,602 bytes for dataset plus report. Python 3.12.14 on Linux. No resource cap stopped the run. CPU includes generation and two evaluations; serialization is performed afterward. Peak RSS is sampled before report serialization. Limits remain active through process exit. These tiny measurements characterize this fixture run, not production verifier performance.

## Fault outcomes (all 96 cases per family)

| Family / A fault | Activations = A errors | Errors after A AND B |
|---|---:|---:|
| Graph: omit degree | 24 | 0 |
| Graph: omit diameter | 24 | 0 |
| Graph: one-source BFS | 9 | 0 |
| Graph: off-by-one | 48 | 0 |
| Code: omit count | 24 | 0 |
| Code: omit distance | 24 | 0 |
| Code: first-pair only | 4 | 0 |
| Code: off-by-one | 48 | 0 |
| Graph: always PASS | 48 | 0 |
| Code: always PASS | 48 | 0 |
| Graph: always FAIL | 48 | 48 |
| Code: always FAIL | 48 | 48 |

Every fault activates somewhere in the full bank. Case-specific nonactivation is retained, as are split-specific statistics and all missed case IDs. Always-FAIL yields 96 retained false rejections across both families: AND does not repair them. Raw confusion counts, every verdict, and each fault's activation status are in results/report.json. The complete input bank is in results/dataset.json.

## Interpretation and limitations

This is an OPEN regression check. Faults touch A only; unchanged B rejects the known false claims, so its added rejection coverage is expected and descriptive. This does not establish scientific or causal diversity, independence, blinding, or held-out generalization. Oracle and A share a format validator. Base objects are deduplicated under graph relabeling and code coordinate/word permutations; broader code equivalences are not included. The second evaluation repeats the generated cases, while a clean-directory rerun can additionally reproduce generation.

No source or protocol changes were made after freeze and no outcome-driven tuning was performed. No existing repository was modified, and nothing was published. The source hashes are in freeze.json. Independent review remains required before publication.
