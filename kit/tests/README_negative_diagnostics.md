# Package mutation diagnostics

Run from the repository root:

    python3 -m unittest discover -s kit/tests -p 'test_*.py' -v

The regression suite mocks subprocess results and uses a tiny synthetic object. It does not execute third-party submission scripts or scientific checkers.

After a successful clean package run, the generic one-digit mutation probe cannot distinguish semantic rejection from a crash, missing checker, timeout, or incomplete output. Such results are reported as **inconclusive**. A bare `FAIL` also carries no verified semantic protocol. The tests cover infrastructure errors, malformed/incomplete/wrong-identity example output, bare `FAIL`, and a corrupted sample that still prints terminal `PASS`.

Existing policy is preserved: corrupted `PASS` produces a warning, not a blocking failure. Clean checker failure still fails. On standalone upstream main, the existing word-PASS match on the last nonempty line is preserved; the stricter exact-line PASS contract in fork PR #2 is not part of this patch. The generic mutation probe is not a blocking semantic gate; checker-specific contracts are a separate future change.

This patch can be applied independently to main. Before integrating any toolkit change, maintainers must refresh the root `SHA256SUMS` against the complete final tree and verify both path coverage (including new files) and hashes. This draft intentionally does not modify the release manifest.
