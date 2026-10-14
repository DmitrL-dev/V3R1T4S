# Package SHA256SUMS identity contract

Run the standard-library synthetic tests from the repository root:

    python3 -m unittest discover -s kit/tests -p 'test_*.py' -v

The focused manifest tests always pass `--no-exec`; they never run submission scripts or scientific checkers.

## Scope and dependency

This package-only change is stacked on fork PR #2, exact base `d1e6d529c43ed1829e72fb76460c125f82b80c73`. It preserves that change's regular-file/directory inventory, hidden-file coverage, and symlink/special-entry rejection. It is independent of the diagnostic and C++ fixes in fork PRs #4 and #5. Do not submit the full dependency stack as an independent diff against old upstream main.

The root repository release manifest is not parsed or changed here.

## Enforced contract

A package manifest must unambiguously cover every other package file. Reject duplicate normalized references (even identical repeated hashes), self-reference to `SHA256SUMS`, malformed records, invalid filename escapes, NUL, outside-package paths, and original paths that do not resolve to a regular file. Preserve filename whitespace and raw filesystem byte identity instead of silently changing the referenced filename.

Normalization alone is insufficient: `missing/../README.md` and `README.md/.` must not become valid references to `README.md`. Existing in-root references such as `object/../README.md` remain accepted when their original path is resolvable. Exact `-` is rejected because GNU checksum checking treats it as standard input; use `./-` to name an actual package file.

Manifest reads remain bounded and read errors/truncation are explicit failures. This does not change package size limits.

## GNU format support and deliberate differences

Supported records use GNU sha256sum's default output format: 64 hex digits, a space, the input-mode marker (space or `*`), and the exact filename. Uppercase/lowercase hex, physical LF/CRLF records, empty records, and comment records beginning with `#` are supported. GNU escaped records use a leading backslash before the hash and filename escapes `\\`, `\n`, and `\r`. Ordinary filenames with spaces, tabs, vertical tabs, form feeds, Unicode separators, or filesystem-surrogateescaped bytes retain their identity.

This is not a complete reimplementation of every format accepted by GNU `sha256sum --check`. BSD tagged records, NUL-delimited input, loose/non-default separators and stdin entries are not supported. Whitespace-only records are malformed, as under GNU `--strict`. Package policy is deliberately stricter about duplicate references and self-entry; GNU may process duplicates individually, but the package requires one unambiguous entry per file.

Tests cover wrong-then-correct duplicate hashes, normalized aliases, malformed records, self-entry, whitespace and byte-decoding collisions, non-directory prefixes, escaped names, stdin spelling, manifest read failure and bounded reads. Small independent synthetic comparisons against installed GNU sha256sum confirmed the original false-PASS cases and the correction; GNU is not needed to run the committed test suite.

## Limits and integration

This verifies local package inventory and checksums, not authenticity, scientific validity, or a malicious contributor's honesty. It provides no security sandbox or TOCTOU/concurrent-filesystem-mutation guarantee. Original-path resolution relies on the existing static symlink-free preflight boundary. Non-UTF-8 filename tests are POSIX-specific and skip on Windows; runtime validation here used Linux/Python 3.12.

Before integration, maintainers must reconcile the maintainer-owned root `SHA256SUMS` against the complete final tree, checking both path coverage (including this README and new test) and every digest. The root manifest is intentionally unchanged in this draft; local test success is not remote CI or release qualification.
