# Opt-in package run receipts (schema 1)

Example from the repository root:

    python3 kit/check_run.py --package /path/to/package --workdir /path/to/workspace --receipt-json /outside/both/receipt.json

The command runs the same checks as without the option. Add `--no-exec` to keep
both executable checks explicitly `NOT_RUN`. Receipt export never launches an
additional command, changes gate policy, or changes the gate exit status.
The final stdout gate line is unchanged; export omissions are reported on stderr
as `RECEIPT: omitted (reason)`. A successful gate exit does not guarantee an
export: callers must also check that their previously nonexistent receipt exists
and that no omission was reported. Bytes are written and closed in a restrictive
temporary file before atomic no-overwrite publication. Existing files are never
replaced. A failed write cannot expose an incomplete final receipt.

## Scope and disclosure

Export requires a normal package with exactly one INDEX data row, one target_id
column, a matching row width, no bank-loading errors or duplicate raw bank target
IDs, and a bank target explicitly
marked `disclosure: open`. Workspace mode, sealed envelopes, commit-only targets,
unknown targets and ambiguous/malformed INDEX files omit export. These are export
restrictions, not new validation decisions. A declaration of open disclosure is
not proof that arbitrary package content is safe to publish. No automatic upload
or sharing is performed.

The resolved destination must be outside both the package and the supplied
workspace. Parent symlink aliases are resolved. A mode-0600 temporary file is
closed before hard-link creation atomically publishes the new final name without
replacing existing files or following a final symlink. The temporary name is
cleaned up on success or failure; cleanup is best-effort if the filesystem itself
fails. Filesystems lacking hard-link support omit export without a weaker fallback.
These are static checks, not a sandbox or a guarantee against
concurrent parent-directory changes. Keep these directories under your control.
Putting a receipt inside the validated package would change its manifest inputs
and is deliberately unsupported.

## Exact schema

- `schema_version`: integer 1.
- `provenance`: constant `local_observation_unattested`.
- `mode`: `{kind: "package", execute: boolean, timeout_seconds: integer}`.
- `checker_sha256`: SHA-256 of the current check_run.py bytes, including the
  receipt writer. This is a file identity, not a trusted build or signature.
- `input_manifest_sha256`: SHA-256 of the SHA256SUMS file bytes read before
  package execution. This identifies only that file. It does **not** establish
  complete or verified input identity, bind every byte read by the checker,
  identify mutated inputs, or exclude concurrent mutation. Missing, symlinked,
  unreadable or over-limit manifests cause export omission.
- `checks`: exactly two entries, in order `clean`, `mutated_object`.
  - `id`: one of those fixed IDs; no target names or paths.
  - `execution`: `NOT_RUN`, `COMPLETED`, `TIMEOUT`, or `INCONCLUSIVE`.
  - `exit_status`: observed integer process return code, or null if unavailable.
  - `reported_terminal`: exact stripped last nonempty line `PASS` or `FAIL`,
    `OTHER` for any other completed/captured output, or null if not observed.
  - `reason`: null or a fixed token: `not_reached`, `execution_disabled`,
    `shell_unavailable`, `timeout`, `signal`, `launch_error`.
- `gate_exit_status`: the original gate's integer exit status, 0 or 1.

Both checks start as `NOT_RUN`, even if the first check fails. `not_reached` also
covers a missing script, early return, or inability to construct the existing
generic mutation. `TIMEOUT` is recorded at the actual TimeoutExpired exception;
neither literal output `TIMEOUT` nor exit -1 is sufficient. Negative process
return codes are `INCONCLUSIVE`; missing shell is `NOT_RUN`. A launch OSError
is recorded as `INCONCLUSIVE` with reason `launch_error` and null process status
and terminal token. The runner preserves upstream
`8b5ba829baa4711791f2dda18e139ae2bd3beeff` handling: it returns an execution-error
sentinel, so a clean launch error fails the gate and a mutation launch error
produces an inconclusive warning. An otherwise eligible receipt can still export.
No attempt is made to guess the scientific meaning of a crash or output.

`COMPLETED` means only the process returned a nonnegative status. It can include
malformed output, contradictory status/output, or an ordinary failure. Even an
exact `PASS` or `FAIL` is a reported token, not authenticated evidence. Existing
gate interpretations can differ from exact receipt labels; they are unchanged.
In particular, the baseline gate can still exit 0 after a mutation-probe timeout;
the gate warns that the probe is inconclusive, and the receipt records TIMEOUT
without promoting it to a rejection. Mutation rejection requires a positive exit
status and exact terminal `FAIL`; unusual positive codes remain valid under the
upstream protocol. These observations do not prove scientific rejection.

No stdout/stderr text, target identifiers, environment variables, absolute paths,
private file content, or author claims are serialized. JSON can be fabricated
or edited: this is neither a signature nor proof of execution, measurement,
authorship, reproduction, or scientific truth. Treat imported receipts as
untrusted statements. This feature does not import receipts into the gate.

## Tests

    python3 -m unittest discover -s kit/tests -p test_run_receipts.py -v

These tests use tiny temporary fixtures and mock every subprocess. They do not
run scientific scripts or downloaded package code. The root SHA256SUMS is left
unchanged for the maintainer to regenerate against the eventual integrated tree.
