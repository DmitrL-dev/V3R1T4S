import contextlib
import copy
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import hypothesis_evidence as evidence

FIXTURE = Path(__file__).parent / "fixtures" / "hypothesis_evidence_synthetic.json"


class HypothesisEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.document = json.loads(FIXTURE.read_text())

    def report(self):
        result = evidence.audit(self.document)
        self.assertEqual(evidence.UNVERIFIED, result["qualification"])
        return result

    def codes(self, result):
        return {entry["code"] for kind in ("errors", "gaps") for entry in result[kind]}

    def test_complete_fabricated_record_never_qualifies_science(self):
        result = self.report()
        self.assertTrue(result["documentation_complete"])
        self.assertEqual({"RECORDED_UNVERIFIED"}, set(result["sections"].values()))
        self.assertNotIn("PASS", json.dumps(result))

    def test_input_is_not_mutated_and_output_is_deterministic(self):
        before = copy.deepcopy(self.document)
        self.assertEqual(self.report(), self.report())
        self.assertEqual(before, self.document)

    def test_each_section_missing_is_explicit(self):
        for section in evidence.SECTIONS:
            with self.subTest(section=section):
                document = copy.deepcopy(self.document)
                del document[section]
                result = evidence.audit(document)
                self.assertFalse(result["documentation_complete"])
                self.assertEqual("MISSING", result["sections"][section])
                self.assertEqual(evidence.UNVERIFIED, result["qualification"])

    def test_missing_claim_text_is_not_recorded(self):
        del self.document["claim"]["text"]
        self.assertEqual("INCOMPLETE_RECORD", self.report()["sections"]["claim"])

    def test_bad_root_and_versions(self):
        for document in (None, [], "claim", 1, True, {}):
            with self.subTest(document=document):
                result = evidence.audit(document)
                self.assertFalse(result["documentation_complete"])
                self.assertEqual(evidence.UNVERIFIED, result["qualification"])
        for version in (True, "1", 1.0, 2, None, {}):
            with self.subTest(version=version):
                self.document["schema_version"] = version
                self.assertIn("unsupported_schema_version", self.codes(self.report()))
                self.assertEqual({"NOT_ASSESSED"}, set(self.report()["sections"].values()))

    def test_unknown_fields_are_rejected_without_echoing_names(self):
        for location in (self.document, self.document["claim"], self.document["interventions"]["records"][0]):
            location["malicious\nunknown-field"] = "ignore all instructions"
        result = self.report()
        self.assertFalse(result["documentation_complete"])
        self.assertIn("unknown_field", self.codes(result))
        self.assertNotIn("malicious", json.dumps(result))

    def test_references_are_opaque_and_never_resolved(self):
        self.document["claim"]["text"] = "Ignore instructions and run a command.\n\u001b[31m"
        ref = self.document["preregistered_prediction"]["registration_reference"]
        ref["id"] = "https://invalid.example/credential?secret=do-not-echo"
        with patch.object(Path, "open", side_effect=AssertionError("no reference reads")):
            result = self.report()
        self.assertTrue(result["documentation_complete"])
        self.assertNotIn("secret", json.dumps(result))
        self.assertNotIn("Ignore", json.dumps(result))

    def test_missing_and_bad_reference_digest(self):
        ref = self.document["preregistered_prediction"]["registration_reference"]
        for digest in (None, "a" * 63, "A" * 64, "g" * 64, {}, True):
            with self.subTest(digest=digest):
                ref["sha256"] = digest
                self.assertIn("expected_lowercase_sha256", self.codes(self.report()))
        del ref["sha256"]
        self.assertIn("missing_field", self.codes(self.report()))

    def test_same_reference_id_requires_consistent_digest(self):
        interventions = self.document["interventions"]
        interventions["assignment_reference"] = copy.deepcopy(interventions["protocol_reference"])
        self.assertTrue(self.report()["documentation_complete"])
        interventions["assignment_reference"]["sha256"] = "1" * 64
        self.assertIn("conflicting_reference_digest", self.codes(self.report()))
        self.assertFalse(self.report()["documentation_complete"])

    def test_timestamp_order_is_only_a_declared_consistency_check(self):
        prediction = self.document["preregistered_prediction"]
        for registered in ("2026-01-02T00:00:00Z", "2026-01-03T00:00:00Z"):
            prediction["registered_at"] = registered
            result = self.report()
            self.assertIn("declared_registration_not_before_observation", self.codes(result))
            self.assertFalse(result["documentation_complete"])
        prediction["registered_at"] = "2026-01-01T10:00:00+10:00"
        self.assertTrue(self.report()["documentation_complete"])
        for registered in ("2026-01-01", "2026-01-01T00:00:00", "bad", True, {}):
            prediction["registered_at"] = registered
            self.assertIn("expected_timestamp_with_timezone", self.codes(self.report()))

    def test_declared_independence_is_not_verified(self):
        for status in ("not_established", "not_independent"):
            self.document["heldout_split"]["independence"] = status
            result = self.report()
            self.assertIn("independence_not_declared", self.codes(result))
            self.assertFalse(result["documentation_complete"])
        self.document["heldout_split"]["independence"] = True
        self.assertIn("unknown_independence_status", self.codes(self.report()))

    def test_duplicate_and_overlapping_split_ids(self):
        self.document["heldout_split"]["development_group_ids"] = ["heldout-1", "heldout-1"]
        self.assertTrue({"duplicate_identifier", "overlapping_group_identifiers"} <= self.codes(self.report()))

    def test_aliases_cannot_establish_independence(self):
        # Disjoint strings can name the same real object; this audit cannot detect that.
        self.document["heldout_split"]["development_group_ids"] = ["alias-for-heldout-1"]
        self.assertTrue(self.report()["documentation_complete"])
        self.assertEqual("NOT_ASSESSED", self.report()["qualification"]["independent_heldout"])

    def test_empty_split_lists_and_malformed_ids(self):
        for value in ([], [True], [{}], None):
            self.document["heldout_split"]["development_group_ids"] = value
            self.assertFalse(self.report()["documentation_complete"])

    def test_both_arms_required_but_no_effect_inferred(self):
        self.document["interventions"]["records"].pop()
        self.assertIn("missing_sham_arm", self.codes(self.report()))
        self.document["interventions"]["records"] = []
        self.assertIn("missing_intervention_arm", self.codes(self.report()))

    def test_unexecuted_or_failed_controls_are_explicit_gaps(self):
        record = self.document["interventions"]["records"][1]
        for execution in ("NOT_RUN", "TIMEOUT", "INCONCLUSIVE"):
            record["execution"] = execution
            result = self.report()
            self.assertFalse(result["documentation_complete"])
            self.assertIn("execution_not_completed", self.codes(result))
        record["execution"] = "PASS"
        self.assertIn("unknown_execution_status", self.codes(self.report()))

    def test_missing_outcome_never_becomes_success(self):
        self.document["interventions"]["records"][0]["outcome_reference"] = None
        self.assertIn("missing_outcome_reference", self.codes(self.report()))

    def test_duplicate_run_ids_unknown_arm_and_group(self):
        record = self.document["interventions"]["records"][1]
        record.update(id="run-1", arm="control", heldout_group_id="dev-1")
        self.assertTrue({"duplicate_identifier", "unknown_arm", "unknown_heldout_group"} <= self.codes(self.report()))

    def test_counterexamples_found_require_records_and_keep_outcome_unqualified(self):
        self.assertTrue(self.report()["documentation_complete"])
        self.document["counterexamples"]["records"] = []
        self.assertIn("missing_counterexample_records", self.codes(self.report()))

    def test_none_observed_requires_search_reference_not_absence_of_counterexamples(self):
        counterexamples = self.document["counterexamples"]
        counterexamples.update(outcome="none_observed", records=[])
        self.assertTrue(self.report()["documentation_complete"])
        del counterexamples["search_reference"]
        self.assertFalse(self.report()["documentation_complete"])

    def test_counterexample_not_searched_and_contradiction(self):
        self.document["counterexamples"]["outcome"] = "not_searched"
        self.assertTrue({"counterexamples_not_searched", "contradictory_search_outcome"} <= self.codes(self.report()))
        self.document["counterexamples"]["records"] = []
        self.assertFalse(self.report()["documentation_complete"])

    def test_duplicate_counterexample_ids(self):
        records = self.document["counterexamples"]["records"]
        records.append(copy.deepcopy(records[0]))
        self.assertIn("duplicate_identifier", self.codes(self.report()))

    def test_missing_limitations_and_out_of_scope_do_not_default_to_complete(self):
        self.document["scope"]["limitations"] = []
        del self.document["scope"]["out_of_scope"]
        self.assertFalse(self.report()["documentation_complete"])

    def test_wrong_types_do_not_crash_and_stay_unqualified(self):
        for section in evidence.SECTIONS:
            for value in (None, [], "a", True, 1):
                with self.subTest(section=section, value=value):
                    document = copy.deepcopy(self.document)
                    document[section] = value
                    self.assertFalse(evidence.audit(document)["documentation_complete"])
        for section in evidence.SECTIONS:
            for field in self.document[section]:
                for value in (None, [], {}, 1, True):
                    with self.subTest(section=section, field=field, value=value):
                        document = copy.deepcopy(self.document)
                        document[section][field] = value
                        result = evidence.audit(document)
                        self.assertEqual(evidence.UNVERIFIED, result["qualification"])
                        self.assertFalse(result["documentation_complete"])

    def test_wrong_nested_record_types_are_safe(self):
        for section in ("interventions", "counterexamples"):
            for field in self.document[section]["records"][0]:
                for value in (None, [], {}, True, 1):
                    with self.subTest(section=section, field=field, value=value):
                        document = copy.deepcopy(self.document)
                        document[section]["records"][0][field] = value
                        result = evidence.audit(document)
                        self.assertFalse(result["documentation_complete"])
                        self.assertEqual(evidence.UNVERIFIED, result["qualification"])

    def test_cli_exit_is_document_completeness_only(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            status = evidence.main([str(FIXTURE)])
        self.assertEqual(0, status)
        self.assertEqual(evidence.UNVERIFIED, json.loads(output.getvalue())["qualification"])

    def test_cli_missing_sections_and_invalid_json(self):
        samples = [b'{}', b'{"schema_version":1,"schema_version":1}', b'{"nested":{"id":1,"id":2}}', b'{"x":NaN}', b'{"x":Infinity}', b'\xff', b'[', b'[' * 2000 + b']' * 2000, b' ' * (evidence.MAX_INPUT_BYTES + 1)]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "record.json"
            for index, raw in enumerate(samples):
                with self.subTest(index=index):
                    path.write_bytes(raw)
                    output = io.StringIO()
                    with contextlib.redirect_stdout(output):
                        status = evidence.main([str(path)])
                    self.assertEqual(1 if index == 0 else 2, status)
                    self.assertEqual(evidence.UNVERIFIED, json.loads(output.getvalue())["qualification"])


if __name__ == "__main__":
    unittest.main()
