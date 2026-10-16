# V3R1T4S small mathematical regression

Standard-library-only VD-CPU-01 r2. Read PROTOCOL.md before interpreting results.

Commands (Linux, Python 3.10+):

    python -m unittest -v
    python benchmark.py freeze
    # Only after root confirms Spectorn heavy test completed:
    python benchmark.py run --spectorn-finished

The freeze command does not generate or evaluate the dataset. Run verifies source hashes and refuses to replace results. Outputs: results/dataset.json and results/report.json. Preserve the source files and freeze.json alongside results for reproduction. Copy frozen sources to a new directory without results to reproduce. Canonicalization excludes vertex/coordinate-permuted duplicate bases from crossing splits. All splits remain OPEN.

No third-party package, network, GPU, scientific diversity claim, publication, or changes to existing repositories.
