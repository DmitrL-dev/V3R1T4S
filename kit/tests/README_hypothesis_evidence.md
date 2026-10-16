# Opt-in hypothesis evidence records (v1)

This standalone, Python-standard-library-only helper audits the **documentation
of a hypothesis**. It is deliberately not imported by `check_run.py` and does not
change package acceptance, receipt semantics, manifests, or any scientific
qualification. Invoke it only when an evidence record is deliberately supplied:

    python3 kit/hypothesis_evidence.py kit/tests/fixtures/hypothesis_evidence_synthetic.json
    python3 -m unittest discover -s kit/tests -p test_hypothesis_evidence.py -v

Python 3.10+ is required. No package installation, network, external code,
subprocess, or reference resolution is used. The input is read-only and the
report goes to stdout. Exit 0 means documentation completeness only; exit 1 means
record errors/gaps; exit 2 means an unreadable or invalid JSON input. Do not use
these exit codes as a production or scientific acceptance gate.

## Meaning of the report

`documentation_complete: true` means all required records are structurally
present, with no supported declared gaps or detectable contradictions. It does
not mean the hypothesis is true, any control succeeded, the references exist,
the experiment ran, or any scientific check passed. A record retaining a reported
counterexample can be documentation-complete. The example is entirely fabricated,
including its zero digests, and intentionally produces a complete record.

Every report, including malformed-input reports, always keeps:

- `scientific_validity: UNQUALIFIED`
- `historical_preregistration: NOT_ASSESSED`
- `independent_heldout: NOT_ASSESSED`
- `causal_identification: NOT_ASSESSED`
- `evidence_content: NOT_ASSESSED`
- `hypothesis_outcome: NOT_ASSESSED`

Section statuses are `RECORDED_UNVERIFIED`, `MISSING`, `INCOMPLETE_RECORD`, or
`INVALID_RECORD`. Unsupported versions leave every section `NOT_ASSESSED`.
Missing or unperformed checks never default to successful outcomes. There is no
`PASS`, verified, accepted, confidence, significance, or causal-effect verdict.

## Exact record contract

Unknown fields at every object level are rejected. All listed fields are required;
there are no optional extensions in v1. See the synthetic JSON for the full shape.

- `schema_version`: the integer `1`, not a boolean or floating-point number.
- `claim`: nonempty strings `id` and `text`.
- `preregistered_prediction`:
  - `text`: a falsifiable prediction stated before observing its outcome.
  - `registration_reference`: a reference as defined below.
  - `registered_at`, `first_outcome_observed_at`: ISO timestamps with timezones.
    Declared registration must strictly precede declared first observation.
    The tool checks only this claimed ordering, never historical preregistration.
- `heldout_split`:
  - `development_group_ids`, `heldout_group_ids`: nonempty lists of unique
    nonempty strings. No exact ID may appear in both lists.
  - `grouping_policy`: nonempty text explaining how bases, derivatives, aliases,
    related observations, and leakage are handled.
  - `independence`: `declared`, `not_established`, or `not_independent`. The latter
    two remain explicit gaps. `declared` is still entirely unverified.
  - `independence_reference`: a reference to the split/provenance evidence.
- `interventions`:
  - `protocol_reference`: reference describing intervention, sham, endpoint,
    comparable conditions, and intended causal question.
  - `assignment_reference`: reference describing allocation and applicable
    randomization/blinding. Presence does not validate that design.
  - `records`: records covering both `intervention` and `sham` arms. Each record
    has a unique `id`, `arm`, `heldout_group_id` found in the declared heldout
    list, `execution`, and `outcome_reference`.
  - `execution`: `COMPLETED`, `NOT_RUN`, `TIMEOUT`, or `INCONCLUSIVE`. Anything
    except `COMPLETED` is an explicit gap; even `COMPLETED` is only a declaration
    and means no successful control, effect, or valid outcome.
  - `outcome_reference`: a reference, or null for unavailable evidence (a gap).
    The referenced outcome must retain its actual result, including null results,
    adverse observations, and failed controls. This tool never reads that content.
- `counterexamples`:
  - `search_reference`: reference documenting the search procedure and result.
  - `outcome`: `found`, `none_observed`, or `not_searched`.
  - `records`: list of objects with unique `id`, nonempty `description`, and
    `evidence_reference`. `found` requires at least one record. `none_observed`
    and `not_searched` require an empty list. `not_searched` remains a gap.
    `none_observed` cannot establish the absence of counterexamples.
- `scope`: nonempty lists of nonempty strings `in_scope`, `out_of_scope`, and
  `limitations`. The tool checks presence, not adequacy or scientific meaning.

A reference is exactly `{ "id": "opaque locator or citation", "sha256":
"64 lowercase hexadecimal characters" }`. The digest is a claimed content
binding to a referenced artifact; the tool does not fetch the artifact, check
its bytes, validate its timestamp, or establish its author or custody. Reusing one
reference ID with different digests is rejected; reusing the same ID and digest
is permitted (for example, several records may cite one results artifact). IDs and
text are treated as untrusted opaque strings. They are never commands or tool
instructions. Record IDs are unique within their own record list; split IDs are
unique within each split and disjoint across splits. Aliases or content-equivalent
objects under different IDs cannot be detected.

Duplicate JSON keys (at any depth), unknown fields/versions, unsupported enum
values, and malformed types are deterministic errors. Errors/gaps are sorted
by schema path and fixed code; raw input text, unknown field names, reference IDs,
paths, and exceptions are not echoed. CLI input is UTF-8 JSON, limited to 1 MiB
and 32 levels of nesting. Non-standard NaN/Infinity values are rejected. This is
an input boundary, not a filesystem sandbox or a trustworthy execution service.

## Relationship to existing V3R1T4S work

An opt-in run receipt is an unattested process observation. A receipt's hash can
be included in evidence references, but the receipt does not establish scientific
truth or a complete experimental design. This helper does not import or interpret
receipt files. A `NOT_RUN`, `TIMEOUT`, or `INCONCLUSIVE` receipt must not be relabeled
as a completed scientific check by a human preparing a record.

The existing VD-CPU-01 r2 mathematical benchmark is explicitly OPEN engineering
regression. Its development and regression names do not establish independent
heldout data. A shared author/filesystem and existing saved hashes cannot establish
historical preregistration or absence of tuning. It has no intervention/sham causal
experiment. Do not retrofit its outcomes into a qualified independent experiment;
record the missing work and retain its stated limitations.

This contract organizes the records needed for later expert review. A separate
review must verify evidence bytes, historical custody, split independence,
preregistered decisions, control comparability, measurements, counterexamples,
statistics where applicable, and the scope of any conclusion. None is automated
or claimed here.

## Tests and patch scope

Tests are small synthetic fixtures only. They cover absent sections, malformed
fields, unknown versions/fields, duplicate IDs and JSON keys, overlapping split
IDs, timestamp inconsistencies, unavailable outcomes, both missing control arms,
NOT_RUN/TIMEOUT/INCONCLUSIVE controls, counterexamples, unsafe-looking opaque
strings, deterministic results, CLI exit semantics, and input size/depth bounds.

The additive patch introduces only this helper, documentation, synthetic fixture,
and test module. It does not modify existing PRs, `check_run.py`, or root
`SHA256SUMS`. No publication, merge, release, or actual scientific run is performed.
