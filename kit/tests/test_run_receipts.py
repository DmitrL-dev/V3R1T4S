# SPDX-License-Identifier: AGPL-3.0-or-later
"""Tiny synthetic fixtures. Every subprocess is mocked; no package code executes."""
import contextlib
import hashlib
import io
import json
import os
from pathlib import Path
from types import SimpleNamespace
import unittest
from unittest import mock
from test_check_run import Base, w, check_run as c


class RunReceipts(Base):
    def invoke(self, package, results=(), extra=(), destination=None, shell=True):
        dest = destination or os.path.join(self.tmp, "receipt.json")
        stdout, stderr = io.StringIO(), io.StringIO()
        with mock.patch.object(c.shutil, "which", return_value="sh" if shell else None), \
                mock.patch.object(c.subprocess, "run", side_effect=list(results)) as process, \
                contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            status = c.main(["--package", package, "--workdir", self.W,
                             "--receipt-json", dest] + list(extra))
        receipt = json.loads(Path(dest).read_text()) if os.path.isfile(dest) else None
        return status, receipt, process.call_count, stdout.getvalue(), stderr.getvalue()

    def result(self, code, text):
        return SimpleNamespace(returncode=code, stdout=text.encode())

    def test_completed_and_minimal_identity(self):
        package = self.package()
        status, data, count, out, err = self.invoke(package, [self.result(0, "detail\nPASS"), self.result(1, "FAIL")])
        self.assertEqual((status, count, err), (0, 2, ""))
        self.assertEqual([i["execution"] for i in data["checks"]], ["COMPLETED", "COMPLETED"])
        self.assertEqual([i["reported_terminal"] for i in data["checks"]], ["PASS", "FAIL"])
        self.assertEqual(data["input_manifest_sha256"], hashlib.sha256(Path(package, "SHA256SUMS").read_bytes()).hexdigest())
        self.assertEqual(data["checker_sha256"], hashlib.sha256(Path(c.__file__).read_bytes()).hexdigest())
        self.assertEqual(data["provenance"], "local_observation_unattested")
        self.assertEqual(data["gate_exit_status"], status)
        self.assertEqual(os.stat(os.path.join(self.tmp, "receipt.json")).st_mode & 0o777, 0o600)
        text = json.dumps(data)
        for forbidden in (self.tmp, "toy-record", "detail", "CONFIRMED", "environment"):
            self.assertNotIn(forbidden, text)

    def test_no_exec(self):
        status, data, count, _, _ = self.invoke(self.package(), extra=["--no-exec"])
        self.assertEqual((status, count), (0, 0))
        self.assertEqual([i["execution"] for i in data["checks"]], ["NOT_RUN", "NOT_RUN"])
        self.assertEqual([i["reason"] for i in data["checks"]], ["execution_disabled"] * 2)

    def test_clean_failure_mutation_not_run(self):
        status, data, count, _, _ = self.invoke(self.package(), [self.result(1, "FAIL")])
        self.assertEqual((status, count), (1, 1))
        self.assertEqual(data["checks"][1]["execution"], "NOT_RUN")

    def test_timeout_observed_not_inferred(self):
        for result, expected, code in [(c.subprocess.TimeoutExpired("sh", 1), "TIMEOUT", None),
                                       (self.result(-1, "TIMEOUT"), "INCONCLUSIVE", -1),
                                       (self.result(1, "TIMEOUT"), "COMPLETED", 1)]:
            with self.subTest(expected=expected):
                dest = os.path.join(self.tmp, expected + ".json")
                status, data, count, _, _ = self.invoke(self.package(), [result], destination=dest)
                self.assertEqual((status, count), (1, 1))
                self.assertEqual(data["checks"][0]["execution"], expected)
                self.assertEqual(data["checks"][0]["exit_status"], code)

    def test_mutation_timeout_does_not_change_existing_gate(self):
        status, data, count, _, _ = self.invoke(self.package(), [self.result(0, "PASS"), c.subprocess.TimeoutExpired("sh", 1)])
        self.assertEqual((status, count), (0, 2))  # existing gate policy, not scientific success
        self.assertEqual(data["checks"][1]["execution"], "TIMEOUT")

    def test_shell_missing(self):
        status, data, count, _, _ = self.invoke(self.package(), shell=False)
        self.assertEqual((status, count), (0, 0))
        self.assertEqual(data["checks"][0]["reason"], "shell_unavailable")
        self.assertEqual(data["checks"][0]["execution"], "NOT_RUN")

    def test_exact_terminal_classification_only(self):
        status, data, count, _, _ = self.invoke(self.package(), [self.result(0, "NOT PASS"), self.result(1, "NOT FAIL")])
        self.assertEqual((status, count), (0, 2))  # do not silently tighten existing policy
        self.assertEqual([i["reported_terminal"] for i in data["checks"]], ["OTHER", "OTHER"])

    def test_launch_errors_preserve_upstream_gate_and_observe_inconclusive(self):
        for mutation in (False, True):
            with self.subTest(mutation=mutation):
                package = self.package()
                results = ([self.result(0, "PASS")] if mutation else []) + [OSError("synthetic launch error")]
                stdout = io.StringIO()
                with mock.patch.object(c.shutil, "which", return_value="sh"), \
                        mock.patch.object(c.subprocess, "run", side_effect=results) as process, \
                        contextlib.redirect_stdout(stdout):
                    expected = c.main(["--package", package, "--workdir", self.W])
                status, data, count, out, err = self.invoke(package, results,
                    destination=os.path.join(self.tmp, "launch%d.json" % mutation))
                self.assertEqual((status, count, out, err),
                                 (expected, process.call_count, stdout.getvalue(), ""))
                self.assertEqual((status, count), (0, 2) if mutation else (1, 1))
                observation = data["checks"][int(mutation)]
                self.assertEqual(observation, {"id": "mutated_object" if mutation else "clean",
                    "execution": "INCONCLUSIVE", "exit_status": None,
                    "reported_terminal": None, "reason": "launch_error"})
                self.assertNotIn("a corrupted copy of the object is rejected", out)
                if mutation:
                    self.assertIn("corrupted-copy check is inconclusive", out)
                else:
                    self.assertEqual(data["checks"][1]["execution"], "NOT_RUN")

    def test_mutation_protocol_matrix_receipts_do_not_change_diagnostics(self):
        cases = [(1, "FAIL", True), (127, "FAIL", True), (139, "detail\r\nFAIL\r\n\r\n", True),
                 (0, "FAIL", False), (1, "PASS", False), (-11, "FAIL", False),
                 (127, "missing dependency", False), (1, "", False),
                 (1, "NOT FAIL", False), (1, "FAIL\ntrailing noise", False),
                 (0, "PASS", False)]
        package = self.package()
        for number, (code, output, rejected) in enumerate(cases):
            with self.subTest(code=code, output=output):
                results = [self.result(0, "PASS"), self.result(code, output)]
                stdout = io.StringIO()
                with mock.patch.object(c.shutil, "which", return_value="sh"), \
                        mock.patch.object(c.subprocess, "run", side_effect=results) as process, \
                        contextlib.redirect_stdout(stdout):
                    expected = c.main(["--package", package, "--workdir", self.W])
                status, data, count, out, err = self.invoke(package, results,
                    destination=os.path.join(self.tmp, "matrix%d.json" % number))
                self.assertEqual((status, count, out, err),
                                 (expected, process.call_count, stdout.getvalue(), ""))
                self.assertEqual((status, count), (0, 2))
                self.assertEqual("a corrupted copy of the object is rejected" in out, rejected)
                observation = data["checks"][1]
                self.assertEqual(observation["execution"], "COMPLETED" if code >= 0 else "INCONCLUSIVE")
                self.assertEqual(observation["exit_status"], code)
                if not rejected and (code, output) != (0, "PASS"):
                    self.assertIn("corrupted-copy check is inconclusive", out)

    def test_missing_script_and_unbuildable_mutation(self):
        package = self.package()
        Path(package, "object/code.txt").write_text("letters only")
        self.sums(package)
        _, data, count, _, _ = self.invoke(package, [self.result(0, "PASS")], destination=os.path.join(self.tmp, "letters.json"))
        self.assertEqual(count, 1)
        self.assertEqual(data["checks"][1]["execution"], "NOT_RUN")
        Path(package, "verify-it-yourself/run_checks.sh").unlink()
        self.sums(package)
        status, data, count, _, _ = self.invoke(package)
        self.assertEqual((status, count), (1, 0))
        self.assertEqual([i["execution"] for i in data["checks"]], ["NOT_RUN"] * 2)

    def test_nonopen_and_ambiguous_omitted(self):
        for target in ("toy-cipher", "unknown"):
            with self.subTest(target=target):
                status, data, count, _, err = self.invoke(self.package(target=target), extra=["--no-exec"])
                self.assertIsNone(data)
                self.assertIn("unsupported_or_nonopen_package", err)
        package = self.package()
        index = Path(package, "INDEX.csv")
        index.write_text(index.read_text() + index.read_text().splitlines()[1] + "\n")
        self.sums(package)
        _, data, _, _, err = self.invoke(package, extra=["--no-exec"])
        self.assertIsNone(data)
        self.assertIn("omitted", err)

    def test_envelope_omitted(self):
        package = self.package()
        w(os.path.join(package, "envelope.md"), "# Sealed envelope sample\n")
        _, data, _, _, err = self.invoke(package, extra=["--no-exec"])
        self.assertIsNone(data)
        self.assertIn("unsupported_or_nonopen_package", err)

    def test_destination_boundaries_and_alias(self):
        package = self.package()
        alias = os.path.join(self.tmp, "alias")
        os.symlink(package, alias)
        for root in (package, self.W, alias):
            with self.subTest(root=root):
                dest = os.path.join(root, "receipt.json")
                status, data, _, _, err = self.invoke(package, extra=["--no-exec"], destination=dest)
                self.assertEqual(status, 0)
                self.assertIsNone(data)
                self.assertIn("destination_inside_input", err)

    def test_existing_file_and_symlink_never_overwritten(self):
        package = self.package()
        existing = Path(self.tmp, "existing.json")
        existing.write_text("{}")
        alias = Path(self.tmp, "link.json")
        alias.symlink_to(existing)
        for dest in (existing, alias):
            status, _, _, _, err = self.invoke(package, extra=["--no-exec"], destination=str(dest))
            self.assertEqual(status, 0)
            self.assertIn("export_failed", err)
            self.assertEqual(existing.read_text(), "{}")

    def test_workspace_omitted_without_extra_execution(self):
        err = io.StringIO()
        with mock.patch.object(c, "check_workspace") as check, contextlib.redirect_stderr(err), contextlib.redirect_stdout(io.StringIO()):
            status = c.main([self.W, "--no-exec", "--receipt-json", os.path.join(self.tmp, "receipt.json")])
        self.assertEqual(status, 0)
        self.assertEqual(check.call_count, 1)
        self.assertIn("workspace_mode_unsupported", err.getvalue())
        self.assertFalse(os.path.exists(os.path.join(self.tmp, "receipt.json")))

    def test_no_flag_leaves_observer_disabled(self):
        with mock.patch.object(c, "RunReceipt", side_effect=AssertionError("not requested")):
            self.assertEqual(self.run_check("--package", self.package(), "--workdir", self.W, "--no-exec"), 0)

    def test_duplicate_raw_bank_ids_omit_without_changing_gate(self):
        bank = Path(self.W, "repo/bank/targets.json")
        data = json.loads(bank.read_text())
        data["targets"].insert(0, dict(data["targets"][0], disclosure="commit-only"))
        bank.write_text(json.dumps(data))
        package = self.package()
        # Existing last-entry-wins bank semantics remain unchanged.
        original = self.run_check("--package", package, "--workdir", self.W, "--no-exec")
        status, receipt, _, _, err = self.invoke(package, extra=["--no-exec"])
        self.assertEqual((original, status), (0, 0))
        self.assertIsNone(receipt)
        self.assertIn("bank_ambiguous_or_unavailable", err)

    def test_failed_write_never_publishes_partial_final(self):
        real_fdopen = c.os.fdopen
        @contextlib.contextmanager
        def failing_writer(fd, mode):
            with real_fdopen(fd, mode) as handle:
                class Writer:
                    def write(self, payload):
                        handle.write(payload[:10])
                        raise OSError("synthetic full disk")
                yield Writer()
        with mock.patch.object(c.os, "fdopen", side_effect=failing_writer):
            status, receipt, count, _, err = self.invoke(self.package(), extra=["--no-exec"])
        self.assertEqual((status, count), (0, 0))
        self.assertIsNone(receipt)
        self.assertEqual(err, "RECEIPT: omitted (export_failed)\n")
        self.assertEqual(list(Path(self.tmp).glob(".run-receipt-*")), [])

    def test_publication_failure_cleans_temporary(self):
        with mock.patch.object(c.os, "link", side_effect=OSError("synthetic unsupported filesystem")):
            status, receipt, _, _, err = self.invoke(self.package(), extra=["--no-exec"])
        self.assertEqual(status, 0)
        self.assertIsNone(receipt)
        self.assertEqual(err, "RECEIPT: omitted (export_failed)\n")
        self.assertEqual(list(Path(self.tmp).glob(".run-receipt-*")), [])

    def test_opt_in_leaves_gate_output_and_command_count_unchanged(self):
        package = self.package()
        cases = [(self.result(0, "PASS"), self.result(1, "FAIL")),
                 (self.result(1, "FAIL"),),
                 (self.result(0, "PASS"), c.subprocess.TimeoutExpired("sh", 1))]
        for number, results in enumerate(cases):
            with self.subTest(case=number):
                stdout = io.StringIO()
                with mock.patch.object(c.shutil, "which", return_value="sh"), \
                        mock.patch.object(c.subprocess, "run", side_effect=list(results)) as process, \
                        contextlib.redirect_stdout(stdout):
                    expected = c.main(["--package", package, "--workdir", self.W])
                status, _, count, out, err = self.invoke(package, results,
                    destination=os.path.join(self.tmp, "comparison%d.json" % number))
                self.assertEqual((status, count, out, err),
                                 (expected, process.call_count, stdout.getvalue(), ""))


if __name__ == "__main__":
    unittest.main()
