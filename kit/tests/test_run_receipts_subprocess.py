# SPDX-License-Identifier: AGPL-3.0-or-later
"""Actual subprocesses on local synthetic arithmetic, never scientific benchmarks.

    python3 -m unittest discover -s kit/tests -p test_run_receipts_subprocess.py -v
"""
import contextlib
import hashlib
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import unittest
from test_check_run import Base, CHECKER, w, check_run as c

# Adapt the inspected local fixture to return the arithmetic verdict explicitly.
ARITHMETIC = "# Local synthetic arithmetic fixture; no scientific claim.\n" + CHECKER + "sys.exit(0 if ok else 1)\n"
SLEEP = "# Local timeout fixture; no scientific claim.\nimport time\ntime.sleep(2)\nprint('PASS')\n"
_active = None


def _audit(event, args):
    if _active is not None and event == "subprocess.Popen":
        _active["launches"] += 1


def _observe(frame, event, result):
    if _active is None or event != "return":
        return
    if frame.f_code is c._run_checks.__code__:
        _active["runner_results"].append((result[0], c.last_nonempty(result[1])))
    elif frame.f_code is subprocess.Popen.__init__.__code__:
        _active["pids"].append(frame.f_locals["self"].pid)


# Audit hooks cannot be removed; inactive outside each bounded invocation.
sys.addaudithook(_audit)


@unittest.skipUnless(os.name == "posix" and shutil.which("sh") and shutil.which("python3"),
                     "requires POSIX shell/exec semantics and python3")
class ActualReceiptSubprocesses(Base):
    def tearDown(self):
        own_temp = Path(self.tmp)
        self.assertTrue(own_temp.name.startswith("v3r1t4s_test_"))
        super().tearDown()
        self.assertFalse(own_temp.exists())

    def invoke(self, package, destination, enabled, no_exec):
        global _active
        state = {"launches": 0, "runner_results": [], "pids": []}
        argv = ["--package", package, "--workdir", self.W, "--timeout", "1"]
        if no_exec:
            argv.append("--no-exec")
        if enabled:
            argv += ["--receipt-json", str(destination)]
        stdout, stderr = io.StringIO(), io.StringIO()
        previous_profile = sys.getprofile()
        _active = state
        sys.setprofile(_observe)
        try:
            with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
                state["gate_exit_status"] = c.main(argv)
        finally:
            sys.setprofile(previous_profile)
            _active = None
        state["stdout"], state["stderr"] = stdout.getvalue(), stderr.getvalue()
        pids = state.pop("pids")
        self.assertEqual(len(pids), state["launches"])
        for pid in pids:
            with self.assertRaises(ProcessLookupError, msg="fixture child was not reaped"):
                os.kill(pid, 0)
        return state

    def exercise(self, name):
        package = self.package()
        w(os.path.join(package, "verify-it-yourself/check.py"), SLEEP if name == "timeout" else ARITHMETIC)
        # Replace the shell with Python: timeout kills the sleeper, not a parent shell.
        w(os.path.join(package, "verify-it-yourself/run_checks.sh"), "exec python3 verify-it-yourself/check.py\n")
        if name == "clean_failure":
            w(os.path.join(package, "object/code.txt"), "1110\n1010\n0110\n")
        self.sums(package)
        destination = Path(self.tmp) / "receipt.json"
        for root in (package, self.W):
            self.assertNotEqual(os.path.commonpath((str(destination), root)), root)
        without = self.invoke(package, destination, False, name == "no_exec")
        self.assertFalse(destination.exists())
        with_receipt = self.invoke(package, destination, True, name == "no_exec")
        # Real launches, outputs and exits remain identical with receipt opt-in.
        self.assertEqual(without, with_receipt)
        self.assertEqual(with_receipt["stderr"], "")
        receipt = json.loads(destination.read_text())
        expected = {
            "clean_and_negative": (0, 2, ["COMPLETED", "COMPLETED"], [0, 1], ["PASS", "FAIL"], [(0, "PASS"), (1, "FAIL")]),
            "no_exec": (0, 0, ["NOT_RUN", "NOT_RUN"], [None, None], [None, None], []),
            "clean_failure": (1, 1, ["COMPLETED", "NOT_RUN"], [1, None], ["FAIL", None], [(1, "FAIL")]),
            "timeout": (1, 1, ["TIMEOUT", "NOT_RUN"], [None, None], [None, None], [(-1, "TIMEOUT")]),
        }[name]
        checks = receipt["checks"]
        actual = (with_receipt["gate_exit_status"], with_receipt["launches"],
                  [item["execution"] for item in checks], [item["exit_status"] for item in checks],
                  [item["reported_terminal"] for item in checks], with_receipt["runner_results"])
        self.assertEqual(actual, expected)
        self.assertEqual(receipt["gate_exit_status"], expected[0])
        self.assertEqual(receipt["checker_sha256"], hashlib.sha256(Path(c.__file__).read_bytes()).hexdigest())
        self.assertEqual(receipt["input_manifest_sha256"], hashlib.sha256(Path(package, "SHA256SUMS").read_bytes()).hexdigest())
        self.assertEqual(receipt["provenance"], "local_observation_unattested")
        if name == "timeout":
            self.assertEqual(checks[0]["reason"], "timeout")
        self.assertEqual(destination.stat().st_mode & 0o777, 0o600)
        self.assertEqual(list(Path(self.tmp).glob(".run-receipt-*")), [])
        self.assertEqual(set(receipt), {"schema_version", "provenance", "mode", "checker_sha256",
                                        "input_manifest_sha256", "checks", "gate_exit_status"})
        for item in checks:
            self.assertEqual(set(item), {"id", "execution", "exit_status", "reported_terminal", "reason"})
        for token in (self.tmp, package, "toy-record", "environment"):
            self.assertNotIn(token, destination.read_text())

    def test_clean_and_semantic_negative(self):
        self.exercise("clean_and_negative")

    def test_no_exec(self):
        self.exercise("no_exec")

    def test_clean_failure(self):
        self.exercise("clean_failure")

    def test_actual_timeout_and_reaping(self):
        self.exercise("timeout")


if __name__ == "__main__":
    unittest.main()
