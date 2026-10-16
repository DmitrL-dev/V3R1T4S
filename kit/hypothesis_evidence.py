#!/usr/bin/env python3
"""Opt-in documentation audit. Never a scientific verdict or package gate."""
from __future__ import annotations

import argparse
from datetime import datetime
import json
from pathlib import Path
import re
import sys

SCHEMA_VERSION = 1
MAX_INPUT_BYTES = 1_048_576
MAX_JSON_DEPTH = 32
SECTIONS = (
    "claim", "preregistered_prediction", "heldout_split", "interventions",
    "counterexamples", "scope",
)
UNVERIFIED = {
    "scientific_validity": "UNQUALIFIED",
    "historical_preregistration": "NOT_ASSESSED",
    "independent_heldout": "NOT_ASSESSED",
    "causal_identification": "NOT_ASSESSED",
    "evidence_content": "NOT_ASSESSED",
    "hypothesis_outcome": "NOT_ASSESSED",
}


def audit(document: object) -> dict:
    """Check records only; references are opaque and are never opened/executed.

    Missing data and declared unperformed work remain explicit gaps. Even a
    complete record cannot change any value in ``qualification``.
    """
    errors: list[dict] = []
    gaps: list[dict] = []
    reference_bindings: dict[str, str] = {}

    def issue(target, path, code):
        target.append({"path": path, "code": code})

    def mapping(value, path, required, optional=()):
        if not isinstance(value, dict):
            issue(errors, path, "expected_object")
            return None
        if any(not isinstance(key, str) for key in value):
            issue(errors, path, "non_string_key")
            return None
        allowed = set(required) | set(optional)
        # Never include arbitrary unknown key contents in diagnostic strings.
        if set(value) - allowed:
            issue(errors, path, "unknown_field")
        for key in required:
            if key not in value:
                issue(gaps, path + "." + key, "missing_field")
        return value

    def text(value, path):
        if not isinstance(value, str) or not value.strip():
            issue(errors, path, "expected_nonempty_text")
            return False
        return True

    def fields_text(value, path, names):
        for name in names:
            if name in value:
                text(value[name], path + "." + name)

    def texts(value, path):
        if not isinstance(value, list):
            issue(errors, path, "expected_list")
            return None
        if not value:
            issue(gaps, path, "empty_list")
        for item in value:
            text(item, path + "[]")
        return value

    def reference(value, path):
        ref = mapping(value, path, ("id", "sha256"))
        if ref is None:
            return
        fields_text(ref, path, ("id",))
        if "sha256" in ref and (
            not isinstance(ref["sha256"], str)
            or re.fullmatch(r"[0-9a-f]{64}", ref["sha256"]) is None
        ):
            issue(errors, path + ".sha256", "expected_lowercase_sha256")
        elif isinstance(ref.get("id"), str) and ref["id"].strip() and "sha256" in ref:
            if ref["id"] in reference_bindings and reference_bindings[ref["id"]] != ref["sha256"]:
                issue(errors, path, "conflicting_reference_digest")
            else:
                reference_bindings[ref["id"]] = ref["sha256"]

    def references(value, path, names):
        for name in names:
            if name in value:
                reference(value[name], path + "." + name)

    def identifiers(value, path):
        items = texts(value, path)
        if items is None or not all(isinstance(item, str) for item in items):
            return set()
        if len(set(items)) != len(items):
            issue(errors, path, "duplicate_identifier")
        return set(items)

    def timestamp(value, path):
        if not isinstance(value, str):
            issue(errors, path, "expected_timestamp_with_timezone")
            return None
        try:
            result = datetime.fromisoformat(value.replace("Z", "+00:00"))
        except ValueError:
            result = None
        if result is None or result.tzinfo is None:
            issue(errors, path, "expected_timestamp_with_timezone")
            return None
        return result

    def section(name, required):
        if not isinstance(document, dict) or name not in document:
            return None
        return mapping(document[name], name, required)

    root = mapping(document, "$", ("schema_version",) + SECTIONS)
    if root is not None and "schema_version" in root:
        if type(root["schema_version"]) is not int or root["schema_version"] != SCHEMA_VERSION:
            issue(errors, "$.schema_version", "unsupported_schema_version")
            return {
                "audit_schema_version": 1,
                "documentation_complete": False,
                "qualification": dict(UNVERIFIED),
                "sections": {name: "NOT_ASSESSED" for name in SECTIONS},
                "errors": sorted(errors, key=lambda entry: (entry["path"], entry["code"])),
                "gaps": sorted(gaps, key=lambda entry: (entry["path"], entry["code"])),
            }

    claim = section("claim", ("id", "text"))
    if claim is not None:
        fields_text(claim, "claim", ("id", "text"))

    prediction = section("preregistered_prediction", (
        "text", "registration_reference", "registered_at", "first_outcome_observed_at",
    ))
    if prediction is not None:
        path = "preregistered_prediction"
        fields_text(prediction, path, ("text",))
        references(prediction, path, ("registration_reference",))
        times = [timestamp(prediction[key], path + "." + key) if key in prediction else None
                 for key in ("registered_at", "first_outcome_observed_at")]
        if all(times) and times[0] >= times[1]:
            issue(gaps, path, "declared_registration_not_before_observation")

    heldout_groups: set[str] = set()
    split = section("heldout_split", (
        "development_group_ids", "heldout_group_ids", "grouping_policy",
        "independence", "independence_reference",
    ))
    if split is not None:
        path = "heldout_split"
        fields_text(split, path, ("grouping_policy",))
        references(split, path, ("independence_reference",))
        development = identifiers(split["development_group_ids"], path + ".development_group_ids") if "development_group_ids" in split else set()
        heldout_groups = identifiers(split["heldout_group_ids"], path + ".heldout_group_ids") if "heldout_group_ids" in split else set()
        if development & heldout_groups:
            issue(errors, path, "overlapping_group_identifiers")
        if "independence" in split:
            if split["independence"] not in ("declared", "not_established", "not_independent"):
                issue(errors, path + ".independence", "unknown_independence_status")
            elif split["independence"] != "declared":
                issue(gaps, path + ".independence", "independence_not_declared")

    interventions = section("interventions", (
        "protocol_reference", "assignment_reference", "records",
    ))
    if interventions is not None:
        path = "interventions"
        references(interventions, path, ("protocol_reference", "assignment_reference"))
        records = interventions.get("records", [])
        arms, ids = set(), set()
        if not isinstance(records, list):
            issue(errors, path + ".records", "expected_list")
            records = []
        for index, value in enumerate(records):
            item_path = path + ".records[" + str(index) + "]"
            record = mapping(value, item_path, (
                "id", "arm", "heldout_group_id", "execution", "outcome_reference",
            ))
            if record is None:
                continue
            fields_text(record, item_path, ("id", "heldout_group_id"))
            if isinstance(record.get("id"), str):
                if record["id"] in ids:
                    issue(errors, item_path + ".id", "duplicate_identifier")
                ids.add(record["id"])
            arm = record.get("arm")
            if "arm" in record and arm not in ("intervention", "sham"):
                issue(errors, item_path + ".arm", "unknown_arm")
            elif arm in ("intervention", "sham"):
                arms.add(arm)
            if "heldout_group_id" in record and (
                not isinstance(record["heldout_group_id"], str)
                or record["heldout_group_id"] not in heldout_groups
            ):
                issue(errors, item_path + ".heldout_group_id", "unknown_heldout_group")
            execution = record.get("execution")
            if "execution" in record and execution not in ("COMPLETED", "NOT_RUN", "TIMEOUT", "INCONCLUSIVE"):
                issue(errors, item_path + ".execution", "unknown_execution_status")
            elif execution != "COMPLETED":
                issue(gaps, item_path + ".execution", "execution_not_completed")
            if "outcome_reference" in record:
                if record["outcome_reference"] is None:
                    issue(gaps, item_path + ".outcome_reference", "missing_outcome_reference")
                else:
                    reference(record["outcome_reference"], item_path + ".outcome_reference")
        for arm in ("intervention", "sham"):
            if arm not in arms:
                issue(gaps, path + ".records", "missing_" + arm + "_arm")

    counterexamples = section("counterexamples", ("search_reference", "outcome", "records"))
    if counterexamples is not None:
        path = "counterexamples"
        references(counterexamples, path, ("search_reference",))
        outcome = counterexamples.get("outcome")
        if "outcome" in counterexamples and outcome not in ("found", "none_observed", "not_searched"):
            issue(errors, path + ".outcome", "unknown_search_outcome")
        elif outcome == "not_searched":
            issue(gaps, path + ".outcome", "counterexamples_not_searched")
        records = counterexamples.get("records", [])
        if not isinstance(records, list):
            issue(errors, path + ".records", "expected_list")
            records = []
        ids = set()
        for index, value in enumerate(records):
            item_path = path + ".records[" + str(index) + "]"
            record = mapping(value, item_path, ("id", "description", "evidence_reference"))
            if record is None:
                continue
            fields_text(record, item_path, ("id", "description"))
            references(record, item_path, ("evidence_reference",))
            if isinstance(record.get("id"), str):
                if record["id"] in ids:
                    issue(errors, item_path + ".id", "duplicate_identifier")
                ids.add(record["id"])
        if outcome == "found" and not records:
            issue(gaps, path + ".records", "missing_counterexample_records")
        if outcome in ("none_observed", "not_searched") and records:
            issue(errors, path + ".records", "contradictory_search_outcome")

    scope = section("scope", ("in_scope", "out_of_scope", "limitations"))
    if scope is not None:
        for key in ("in_scope", "out_of_scope", "limitations"):
            if key in scope:
                texts(scope[key], "scope." + key)

    section_status = {}
    for name in SECTIONS:
        related = lambda entry: entry["path"] == name or entry["path"].startswith(name + ".")
        if not isinstance(document, dict) or name not in document:
            section_status[name] = "MISSING"
        elif any(map(related, errors)):
            section_status[name] = "INVALID_RECORD"
        elif any(map(related, gaps)):
            section_status[name] = "INCOMPLETE_RECORD"
        else:
            section_status[name] = "RECORDED_UNVERIFIED"
    return {
        "audit_schema_version": 1,
        "documentation_complete": not errors and not gaps,
        "qualification": dict(UNVERIFIED),
        "sections": section_status,
        "errors": sorted(errors, key=lambda entry: (entry["path"], entry["code"])),
        "gaps": sorted(gaps, key=lambda entry: (entry["path"], entry["code"])),
    }


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate_json_key")
        result[key] = value
    return result


def load_document(path: Path):
    with path.open("rb") as handle:
        raw = handle.read(MAX_INPUT_BYTES + 1)
    if len(raw) > MAX_INPUT_BYTES:
        raise ValueError("input_too_large")
    # JSON's non-standard NaN/Infinity values are not part of this contract.
    def reject_constant(_value):
        raise ValueError("nonfinite_json_number")
    document = json.loads(raw.decode("utf-8"), object_pairs_hook=_unique_object,
                          parse_constant=reject_constant)
    pending = [(document, 0)]
    while pending:
        value, depth = pending.pop()
        if depth > MAX_JSON_DEPTH:
            raise ValueError("json_too_deep")
        if isinstance(value, dict):
            pending.extend((child, depth + 1) for child in value.values())
        elif isinstance(value, list):
            pending.extend((child, depth + 1) for child in value)
    return document


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("record", type=Path)
    args = parser.parse_args(argv)
    try:
        report = audit(load_document(args.record))
    except (OSError, ValueError, RecursionError):
        # No untrusted contents, filesystem paths, or exception text are echoed.
        print(json.dumps({"input_status": "UNREADABLE_OR_INVALID_JSON",
                          "qualification": dict(UNVERIFIED)}, sort_keys=True))
        return 2
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["documentation_complete"] else 1


if __name__ == "__main__":
    sys.exit(main())
