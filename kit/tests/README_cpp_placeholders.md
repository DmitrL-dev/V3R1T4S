# Bounded C++ include recognition

Run from the repository root:

    python3 -m unittest discover -s kit/tests -p 'test_*.py' -v

This change is stacked on the content-based package scanning in fork PR #2, exact base `d1e6d529c43ed1829e72fb76460c125f82b80c73`. Do not present the full stack as an independent change against old upstream main.

Only known standard-header operands in recognized `#include` directives in `.cpp`, `.hpp`, and `.h` receive a placeholder exemption. Other text on the same line, comments, literals, hidden files, and all original-text leak/private-string checks remain scanned. Synthetic fixtures cover genuine includes, adjacent placeholders, fake directives in comments/literals, literal suffixes, digit separators, malformed raw strings, initial BOM, and hidden files.

This is a conservative lexical recognizer, not a C++ parser. It declines all include exemptions in a file containing line-splice spellings (including whitespace before LF/CR), legacy `??/`, universal-character spellings `\u`, `\U`, or `\N`, or unsupported Unicode preprocessing-number forms. Other extensions, `%:` digraph directives, unusual directive whitespace, and macro-computed headers are not supported. These cases retain existing placeholder false positives rather than widening acceptance. Unknown-extension content scanning depends on PR #2.

Attribution: adapted from rfreel's unintegrated checker-fix proposal within upstream PR #8, commit `eb9d15e25464fd854a18f3151be7c7db05bb83c2`:
https://github.com/rfreel/V3R1T4S/blob/eb9d15e25464fd854a18f3151be7c7db05bb83c2/review-proposals/a34-603-18b44fac/checker-fix/check_run_cpp_includes.patch
The standard-header list and masking approach derive from that proposal; additional fail-closed lexical regressions and fixes were added during independent review. This tool fix makes no scientific claim about that submission.

Before integration, maintainers must reconcile the root `SHA256SUMS` with the complete final tree, checking coverage of all changed/new files and their hashes. The root release manifest is intentionally unchanged in this draft. Local synthetic tests and independent code review are not remote CI or release qualification.
