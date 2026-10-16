# Real subprocess receipt qualification on synthetic arithmetic

From the repository root:

    python3 -m unittest discover -s kit/tests -p test_run_receipts_subprocess.py -v

Full suite:

    python3 -m unittest discover -s kit/tests -p 'test_*.py' -v

This adds four tests using actual local shell/Python subprocesses, with no mocked
execution or downloaded package code. The inspected test_check_run fixture checks
three four-bit words for exactly two ones each. A locally authored adaptation
adds an explicit 0/1 exit status to its printed verdict. The existing digit
mutation violates that arithmetic criterion and produces a real FAIL/1.
The timeout fixture is a locally authored sleep(2) under the gate's one-second
timeout. Its shell uses exec, so timeout terminates the sleeper itself.

Each case runs without and with --receipt-json:

- Clean plus mutation: two launches per invocation; PASS/0 then FAIL/1;
  both COMPLETED, gate exit 0.
- No-exec: zero launches; both NOT_RUN, gate exit 0.
- Clean failure: one launch; FAIL/1, mutation NOT_RUN, gate exit 1.
- Actual timeout: one launch; TIMEOUT with null receipt exit, mutation NOT_RUN,
  gate exit 1. All captured child processes must be reaped.

The four tests make eight actual package process launches in total. Audit and
profiling hooks observe real launches/returns without replacing subprocess code.
They assert receipt opt-in adds no launches and preserves gate output and exit.
Receipts are mode 0600, outside package/workspace, checked for unexpected paths
or fixture content, and removed with their own temporary fixture directories.
No raw logs, transient PIDs or workspace paths are stored in the repository.
The tests require POSIX shell/exec semantics and python3, and otherwise skip.

## Recorded local result and limits

Initial qualification used draft PR #11 HEAD
ac5bb71b2796d692e0c913efa573378bbd653540, checker Git blob
94e78b833525b2405c23fe46d507f84d6a887264. All four cases passed with eight actual
launches and approximately 2.15 seconds total invocation wall time, mostly sleep.
Every child was reaped and every owned fixture directory removed. This adds to
the earlier 68-test standalone synthetic suite. The combined suite passed all
72 tests in 2.562 seconds. A separate PR199 + PR30 compatibility copy passed all
143 tests in 4.020 seconds; those pending changes are not included in this patch.

This is actual tool execution on synthetic arithmetic, not a scientific
benchmark, new research result, third-party checker validation, signature or
proof of authorship. Imported receipts remain unattested statements. A manifest
hash identifies only that file, not verified complete input identity.
No production defect was found and this follow-up changes only tests/docs.
