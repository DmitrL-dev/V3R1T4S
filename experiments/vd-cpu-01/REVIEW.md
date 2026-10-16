# Independent finite-fixture review

2026-10-16. Read-only reproduction passed for the stated OPEN engineering regression scope. All frozen source and saved artifact hashes matched. Regeneration reproduced all 48 base objects, 192 cases, outcome matrices and summaries; six unit tests passed.

Independent exhaustive simple-path calculations checked graph metrics and all labels. Independent exhaustive vertex/coordinate permutations confirmed the stated deduplication. Every family/split contains 12 bases, 24 valid and 24 invalid cases. All 96 combined always-FAIL false rejections remain recorded.

Generation plus two evaluations took 0.05669 process CPU seconds in this review; the entire review used 0.6603 seconds. The original measurement of 0.05249 seconds covers generation, canonicalization, evaluations and summaries, but excludes imports, manifest checks, serialization and writes. Original peak RSS was sampled before serialization and is not a final whole-process peak.

Important limits: expected claims were generated using the evaluation oracle, so oracle-versus-expected agreement alone is circular; independent checks found no incorrect labels here. Hashes prove present consistency, not historical preregistration or absence of tuning. Transformations are fixed reversals and the fault bank is narrow. Unchanged checker B rejects incorrect claims by construction, so improvements from A AND B do not prove causal diversity. AND does not repair false rejection. No LLM independence, parser completeness, scientific novelty or general robustness claim follows.
