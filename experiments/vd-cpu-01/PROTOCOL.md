# VD-CPU-01 revision 2

## Scope and claims
OPEN, CPU-only engineering regression benchmark for V3R1T4S. This is not a scientific diversity experiment. One author and a shared filesystem mean no independence, blinding, held-out generalization, causal diversity, or scientific novelty claim. No inference beyond this finite fixture bank; no bootstrap, p-values, or effect-size acceptance threshold. All derivatives of a base object stay in one split. Both splits are open development/regression bookkeeping, not training/test partitions.

## Fixed dataset
Seed 6202601, Python standard-library Random. 24 simple connected undirected graphs with 4–7 vertices, 24 constant-weight binary codes of length 4–8 with 2–5 distinct words. Generate connected graphs using a random recursive tree plus random edges. Generate codes by sampling words of a sampled fixed weight. Bound attempts at 10,000 per family. The first 12 accepted objects in each family are development; the next 12 are regression.

Canonical deduplication before split: graphs under vertex relabeling (exact permutation search restricted to degree groups); codes under coordinate permutation and word reordering (row permutation and sorted column signatures). Complement and translation equivalence are deliberately not included. Canonical keys cover all equivalences used by the metamorphic transformation. No duplicate equivalent bases within a family under these stated equivalences.

Each base produces exactly four cases: joint true claim, relabeled/permuted true claim, and two separate false claims. Thus 48 bases and 192 cases, 96 true and 96 false. Graph claims: exact vertex count, maximum-degree upper bound, diameter upper bound. Two false claims independently lower the exact degree or diameter by one. Code claims: exact cardinality, constant weight for every word, minimum-distance lower bound. Two false claims independently overstate distance or cardinality by one. Transformation: reverse graph vertex labels; reverse code coordinates and word order. Sorting edge endpoints preserves canonical input format. Transformations are label-preserving bijections.

## Algorithms and format
Oracle graph metric: Boolean adjacency-matrix reachability with repeated Boolean matrix multiplication. Oracle code metric: pairwise per-symbol Hamming comparisons. A: all-source BFS, XOR/popcount. B: Floyd–Warshall, support-set intersections. A and B each implement full exact input-key/type/shape/range/uniqueness checks. Graphs must be connected; code words must all have claimed weight. Boolean values are not integers for input purposes. Oracle uses A's format validator: this is an explicitly shared boundary, with separate malformed-input unit tests, not an independent parser oracle. Empty/singleton codes are outside the protocol domain; minimum distance is therefore always defined.

## Frozen fault bank
Apply faults to A only, one at a time; B and oracle remain unchanged. Each family has exactly four faults plus always-PASS and always-FAIL controls.

Graph: omit degree check; omit diameter check; use BFS from vertex zero only (connectivity still checked); allow degree and diameter upper-bound violations by one.

Code: omit count check; omit distance check; check distance of the first pair only; allow cardinality error by one and distance shortfall by one.

The combined verdict is logical A AND B. On oracle-negative fixtures, unchanged B can reject A's false acceptance by construction. Any added coverage is descriptive, not causal evidence for algorithmic diversity. AND cannot repair false rejection. First-pair and one-source faults can remain unactivated or missed; preserve every such result. Controls bypass all checks intentionally.

## Freeze and execution
Before evaluating the generated dataset, freeze this protocol, generator, validators, algorithms, fault bank, tests, and README by SHA-256 in freeze.json. Unit tests use manual examples and are permitted before freeze. The evaluation must wait for root's explicit signal that Spectorn heavy tests ended. No outcome-driven adjustment after freeze. Any defect requires a new explicit version, retaining the old manifest and outputs; no silent overwrite.

Run generates the dataset once, computes the full case/fault outcome matrix twice, and compares matrices exactly. Determinism concerns verdicts, not timings. Reproducible generator seed and Python version are documented; a repeat command must use a fresh copy without results/ because output is never overwritten.

## Budget
Linux/POSIX, Python >=3.10, no dependencies, downloads, paid models, GPU, external services, or publication. Process CPU limit 600 seconds; virtual address-space limit 512 MiB; case wall-time alarm 2 seconds including all verifier/fault calls. Generator is under the overall CPU and memory caps. Dataset plus report must be <=20 MiB. No subprocesses or parallel CPU work. Record process CPU seconds and Linux peak RSS KiB. Cap stops are failures, not missing rows silently removed.

## Outputs and acceptance
Persist full dataset and exact outcome matrix, per-family/per-split confusion counts, fault activations, unactivated flags, added corrections, and all remaining missed case IDs. Positive means valid claim/acceptance: TP/TN/FP/FN. Persist metamorphic results per base. No aggregate metric replaces raw outcomes.

Acceptance: 48/192 sizes; unchanged A/B/oracle agree with all fixed expected labels; always controls make observable errors in both families; every metamorphic true pair preserves labels; exact repeated outcome matrix agrees. No requirement that every injected fault activates. An acceptance failure must be reported without retuning. Independent root review is required before any fork publication, which is outside this task's authorization.
