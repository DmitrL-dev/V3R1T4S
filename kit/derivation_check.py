#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-or-later
"""Is a claimed configuration a near copy, deletion or insertion of a published one? Python 3.8+, standard library only.

    python3 derivation_check.py CLAIM REF [REF ...] [--dim D] [--container box|ball|none] [--tol T | --rel-tol R]
                                [--share S]

Each file lists one point (sphere or circle centre) per line. Lines starting with # are skipped, and only rows with
the most common count of numbers are read, so a radius line drops out. A leading integer counter column and a
trailing constant column are removed (Packomania writes "index x y z radius"); the first D remaining numbers are the
coordinates (D from --dim, else all remaining columns of the claim file).

For every reference file it reports the share of claimed points that lie within the tolerance of a reference point,
and the share of reference points matched, under
  - the identity: deletion, insertion and a local polish keep most points in place;
  - every symmetry of the container about the origin (box: the 2^D D! signed coordinate permutations);
  - the same after mapping each file to its own bounding box (a translated or rescaled copy).
When the two files have the same number of points it also compares their sorted pairwise distances, which no isometry
changes (a copy rotated by any angle, e.g. in a ball); they must agree to --iso-tol (default 1e-6) of the diameter,
because two different packings of the same N can agree to a few per cent. The default tolerance is 0.1 times the reference's minimum
point distance, so a match means the same structural position, not the same digits.

A share at or above --share (default 0.95) for both files is flagged as copy-like, deletion-like or insertion-like.
A flag is not a verdict. It means the claim should name that file as its starting point and credit its author,
and the bar is that file's value, not a new search. Lattice-like packings share positions by construction, so a flag
between two of them is weak evidence. Not covered: a copy rotated by a non-symmetry (in a ball, any rotation) and
then moved by more than --iso-tol, or with points added or removed.

Last line: "DERIVATION_CHECK: FLAG (<n>)" or "DERIVATION_CHECK: NONE". Exit status 0, or 2 with --strict on a flag.
"""
import argparse, itertools, math, os, re, sys

NUM = re.compile(r"[-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?")


def number_rows(path):
    """Rows of numbers of a coordinate file, as strings: lines starting with # are skipped, and only rows of the most
    common length (at least 2 numbers) are kept, so a radius line or a count line drops out. A leading integer counter
    column and a trailing constant column are removed (Packomania writes 'index x y z radius')."""
    rows = []
    with open(path, encoding="utf-8", errors="replace") as f:
        for line in f:
            s = line.strip()
            if s and not s.startswith("#"):
                nums = NUM.findall(s)
                if len(nums) >= 2:
                    rows.append(nums)
    if not rows:
        return []
    lengths = {}
    for r in rows:
        lengths[len(r)] = lengths.get(len(r), 0) + 1
    n = max(lengths, key=lambda k: (lengths[k], k))
    rows = [r for r in rows if len(r) == n]
    first = [r[0] for r in rows]
    if n > 2 and all(re.fullmatch(r"\d+", v) for v in first) and \
            [int(v) for v in first] == list(range(int(first[0]), int(first[0]) + len(first))):
        rows = [r[1:] for r in rows]
    if len(rows[0]) > 2 and len(rows) > 2 and len({float(r[-1]) for r in rows}) == 1:
        rows = [r[:-1] for r in rows]
    return rows


def guess_dim(path):
    rows = number_rows(path)
    if not rows:
        raise SystemExit("no coordinate rows in %s; pass --dim" % path)
    return len(rows[0])


def read_points(path, dim):
    rows = number_rows(path)
    if rows and len(rows[0]) < dim:
        raise SystemExit("%s has %d coordinate columns, fewer than --dim %d" % (path, len(rows[0]), dim))
    return [tuple(float(v) for v in r[:dim]) for r in rows]


def dist(p, q):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p, q)))


def min_distance(pts):
    """Smallest pairwise distance (grid search, about linear time for packings)."""
    n = len(pts)
    if n < 2:
        return float("inf")
    d = len(pts[0])
    lo = [min(p[k] for p in pts) for k in range(d)]
    hi = [max(p[k] for p in pts) for k in range(d)]
    span = max(h - l for l, h in zip(lo, hi)) or 1.0
    h = span / max(1.0, n ** (1.0 / d))
    best = float("inf")
    while True:
        grid = {}
        for i, p in enumerate(pts):
            grid.setdefault(tuple(int(math.floor((p[k] - lo[k]) / h)) for k in range(d)), []).append(i)
        offs = list(itertools.product((-1, 0, 1), repeat=d))
        for key, idx in grid.items():
            for o in offs:
                nb = grid.get(tuple(a + b for a, b in zip(key, o)))
                if not nb:
                    continue
                for i in idx:
                    for j in nb:
                        if j > i:
                            best = min(best, dist(pts[i], pts[j]))
        if best <= h:
            return best
        h *= 2.0  # no pair closer than the cell size found yet: widen the cells and retry


class Index:
    """Points hashed on a grid with cell size tol, for 'is there a point within tol?' queries."""

    def __init__(self, pts, tol):
        self.pts, self.tol = pts, tol
        self.d = len(pts[0])
        self.grid = {}
        for i, p in enumerate(pts):
            self.grid.setdefault(self.key(p), []).append(i)
        self.offs = list(itertools.product((-1, 0, 1), repeat=self.d))

    def key(self, p):
        return tuple(int(math.floor(v / self.tol)) for v in p)

    def nearest(self, p):
        k = self.key(p)
        best, bi = None, -1
        for o in self.offs:
            for i in self.grid.get(tuple(a + b for a, b in zip(k, o)), ()):
                dd = dist(p, self.pts[i])
                if dd <= self.tol and (best is None or dd < best):
                    best, bi = dd, i
        return bi, best


def box_symmetries(d):
    for perm in itertools.permutations(range(d)):
        for signs in itertools.product((1, -1), repeat=d):
            yield perm, signs


def apply(sym, p):
    perm, signs = sym
    return tuple(signs[k] * p[perm[k]] for k in range(len(p)))


def bbox_normalise(pts):
    d = len(pts[0])
    lo = [min(p[k] for p in pts) for k in range(d)]
    hi = [max(p[k] for p in pts) for k in range(d)]
    mid = [(a + b) / 2 for a, b in zip(lo, hi)]
    s = max(b - a for a, b in zip(lo, hi)) or 1.0
    return [tuple((p[k] - mid[k]) / s for k in range(d)) for p in pts]


def match(claim, index, sym=None):
    hit_claim, hit_ref, shift = 0, set(), 0.0
    for p in claim:
        q = apply(sym, p) if sym else p
        i, dd = index.nearest(q)
        if i >= 0:
            hit_claim += 1
            hit_ref.add(i)
            shift = max(shift, dd)
    return hit_claim, len(hit_ref), shift


def sorted_pair_distances(pts):
    out = [dist(p, q) for p, q in itertools.combinations(pts, 2)]
    out.sort()
    return out


def fingerprint_gap(a, b):
    """Largest difference between the sorted pairwise distances of a and b: raw, and after scaling each list by its
    own largest distance. Also returns b's largest distance (its diameter)."""
    da, db = sorted_pair_distances(a), sorted_pair_distances(b)
    raw = max(abs(x - y) for x, y in zip(da, db))
    sa, sb = da[-1] or 1.0, db[-1] or 1.0
    scaled = max(abs(x / sa - y / sb) for x, y in zip(da, db))
    return raw, scaled, sb


def check(claim_path, ref_paths, dim=None, container="box", tol=None, rel_tol=0.1, share=0.95, iso_tol=1e-6,
          out=sys.stdout, max_pairs=2_000_000):
    dim = dim or guess_dim(claim_path)
    claim = read_points(claim_path, dim)
    if not claim:
        raise SystemExit("no points read from %s" % claim_path)
    print("claim: %s (%d points, dim %d)" % (claim_path, len(claim), dim), file=out)
    flags = []
    for rp in ref_paths:
        ref = read_points(rp, dim)
        if not ref:
            print("ref %s: no points read, skipped" % rp, file=out)
            continue
        md = min_distance(ref)
        if md == 0 and not tol:
            print("ref %s: two reference points coincide, so --rel-tol gives no tolerance; pass --tol" % rp, file=out)
            continue
        t = tol if tol else rel_tol * md
        print("ref %s (%d points, min distance %.6g, tolerance %.3g)" % (rp, len(ref), md, t), file=out)
        best = None
        frames = [("identity", claim, ref, [None])]
        if container == "box":
            frames.append(("box symmetry", claim, ref, list(box_symmetries(dim))[1:]))
        cb, rb = bbox_normalise(claim), bbox_normalise(ref)
        t_b = (tol / max(max(p) - min(p) for p in zip(*ref)) if tol else rel_tol * min_distance(rb))
        frames.append(("bounding box", cb, rb, [None] + (list(box_symmetries(dim))[1:] if container == "box" else [])))
        for name, c, r, syms in frames:
            idx = Index(r, t if name != "bounding box" else t_b)
            for sym in syms:
                hc, hr, sh = match(c, idx, sym)
                score = min(hc / len(c), hr / len(r))
                if best is None or score > best[0]:
                    best = (score, name, sym, hc, hr, sh)
        score, name, sym, hc, hr, sh = best
        how = name + ("" if sym is None else " perm=%s signs=%s" % (list(sym[0]), list(sym[1])))
        print("   best: %s: %d/%d claim points matched (%.3f), %d/%d reference points (%.3f), largest shift %.3g"
              % (how, hc, len(claim), hc / len(claim), hr, len(ref), hr / len(ref), sh), file=out)
        kind = None
        if hc / len(claim) >= share and hr / len(ref) >= share:
            kind = "copy-like" if len(claim) == len(ref) else ("deletion-like" if len(claim) < len(ref)
                                                               else "insertion-like")
        elif len(claim) < len(ref) and hc / len(claim) >= share:
            kind = "deletion-like (%d of the reference's points not used)" % (len(ref) - hr)
        elif len(claim) > len(ref) and hr / len(ref) >= share:
            kind = "insertion-like (%d claim points not in the reference)" % (len(claim) - hc)
        if len(claim) == len(ref) >= 2 and len(claim) * (len(claim) - 1) // 2 <= max_pairs:
            raw, scaled, diam = fingerprint_gap(claim, ref)
            print("   sorted pairwise distances: largest gap %.3g (raw), %.3g (both scaled to unit diameter)"
                  % (raw, scaled), file=out)
            if kind is None and (raw <= iso_tol * diam or scaled <= iso_tol):
                kind = "isometric copy (sorted pairwise distances agree)" if raw <= iso_tol * diam else \
                    "similar copy (sorted pairwise distances agree after scaling)"
                score = 1.0
        if kind:
            flags.append((rp, kind, score))
            print("   FLAG: %s" % kind, file=out)
    if len(flags) > 1:
        top = max(flags, key=lambda f: f[2])
        print("closest reference: %s (matched share %.3f)" % (top[0], top[2]), file=out)
    if flags:
        print("DERIVATION_CHECK: FLAG (%d)" % len(flags), file=out)
    else:
        print("DERIVATION_CHECK: NONE", file=out)
    return flags


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("claim")
    ap.add_argument("refs", nargs="+")
    ap.add_argument("--dim", type=int)
    ap.add_argument("--container", choices=("box", "ball", "none"), default="box")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--tol", type=float, help="absolute tolerance (default: --rel-tol times the min distance)")
    g.add_argument("--rel-tol", type=float, default=0.1)
    ap.add_argument("--share", type=float, default=0.95)
    ap.add_argument("--iso-tol", type=float, default=1e-6,
                    help="isometry test: largest gap of the sorted pairwise distances, relative to the diameter")
    ap.add_argument("--strict", action="store_true", help="exit 2 when anything is flagged")
    a = ap.parse_args(argv)
    for p in [a.claim] + a.refs:
        if not os.path.isfile(p):
            raise SystemExit("no such file: %s" % p)
    flags = check(a.claim, a.refs, a.dim, a.container, a.tol, a.rel_tol, a.share, a.iso_tol)
    return 2 if (flags and a.strict) else 0


if __name__ == "__main__":
    sys.exit(main())
