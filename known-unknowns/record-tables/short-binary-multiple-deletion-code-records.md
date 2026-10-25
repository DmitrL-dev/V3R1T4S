# Binary deletion codes: improve the best size at length 15 or 16, correcting two or three deletions

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★★★☆ · compute: laptop-hours to laptop-days for local clique/independent-set search on 32768 or 65536 candidate words; certificate verification is seconds to minutes · open as of 2026-10-25

## The problem

Franziska Weindel and Reinhard Heckel, LLM-Guided Search for Deletion-Correcting Codes, arXiv:2504.00613v2 (5 June 2026), Table 2, gives best-known construction sizes and unresolved upper bounds. Maxima across every reported row are (n,s)=(15,2):136, (16,2):215, (15,3):30 and (16,3):42. The LP upper bounds are 277,487,61,99. A binary code corrects s adversarial deletions when distinct codewords have disjoint sets of length n-s subsequences. These unrestricted nonlinear deletion codes differ from the bank's Hamming-metric constant-weight codes and from quaternary edit-metric DNA codes (edit-metric-dna-codes-gc). Checked 2026-10-25: v2 is the latest version.

## What counts as a win

Provide an explicit set of distinct binary words with respectively at least 137, 216, 31 or 43 codewords for any one of the four specified (n,s) cells, with pairwise disjoint s-deletion subsequence sets. No linearity, constant-weight or decoder-efficiency assumption is imposed. The complete codebook is the certificate. Also strictly improve the best comparable published result at claim time, including compatible compositions of published objects. State whether the candidate is a composition and identify its components. Values in unmerged pull requests do not set the bar.

## How a win is checked

For every word enumerate all choices of s deleted positions, deduplicate the resulting length n−s strings within that word, and insert each string into a map from received string to originating codeword. Reject if a string occurs for two distinct words. Check word length, alphabet and uniqueness, then compare code size to the frozen threshold. Independently cross-check with pairwise dynamic-programming longest common subsequences: LCS(x,y)<n−s. At these four thresholds fewer than 30000 deletion-pattern evaluations suffice for the smallest winning certificates.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2504.00613>

## Sources

- <https://arxiv.org/abs/2504.00613>
- <https://arxiv.org/pdf/2504.00613v2>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Use penalty-guided clique search, but maintain deletion-conflict sets implicitly instead of materializing a dense graph.
- Start with the best conventional solver codebooks, then use k-for-(k+1) exchanges and component-wise exact search.
- Try priority functions trained jointly on shorter deletion counts and lengths; score the final explicit code with the exact checker.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Beating only the learned-method row is insufficient; take maxima over all rows and comparable later constructions.
- Hamming distance alone does not certify deletion correction.
- Repeated subsequences within one word are harmless and must be deduplicated.
- Naive concatenation need not preserve correction of adversarial deletions across block boundaries.
- The June 2026 paper is the numerical source; search for later record literature before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/short-binary-multiple-deletion-code-records.md
```

Already set up? Say `run V3R1T4S on short-binary-multiple-deletion-code-records`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `short-binary-multiple-deletion-code-records`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
