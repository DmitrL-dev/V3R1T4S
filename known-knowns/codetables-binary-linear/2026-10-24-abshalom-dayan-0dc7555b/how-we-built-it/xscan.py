"""Construction X on nested plain one-point Hermitian codes C(D,aP) ⊂ C(D,bP) (27 affine points of y^3+y=x^4 over
GF(9)) with an auxiliary Reed-Solomon [l, r = K_b - K_a, l - r + 1]_9 code (evaluation points 0..l-1 in the a+3b
encoding), n = 27 + l <= 36. For each code: hull maximised over sign patterns of the l auxiliary columns (2^l),
exact d (bz9w), seed [[n, K - h, d; n - K - h]]; report listed cells beaten by closure({seed}) and not already beaten
by closure(literature family + the five n = 28 codes + repo/PR cells #331, #363, #403, #404, #405) or by the table
itself; only cells with k >= 1 and c >= 1 count (PREREG).
Round 3: optional amin (skip pairs with a < amin, already scanned) and a per-call bz9w time cap; on a timeout the
seed uses the proved Construction X lower bound d >= min(27 - a, 27 - b + l - r + 1) and is listed as UNDECIDED if
the Singleton bound n - K + 1 could still beat a new cell. One progress line per (a, b) pair. The natural E_14
seed [[28,6,14;10]] is in the baseline, so its (32,6,10) consequence is not reported again.
Round 4: pruning by proved bounds with exact inner distances (bz9 on the [27, K] plain codes, cached):
  d >= dlb = min(d(C(D,aP)), d(C(D,bP)) + l - r + 1)   (Construction X bound),
  d <= dub = min(d(C(D,aP)), d(C(D,bP)) + l, n - K + 1)   (a min-weight word of C(D,aP) has a zero tail; deleting
  the tail maps into C(D,bP); Singleton).
A code whose dub beats no new listed cell is skipped (provably no new cell). Otherwise T = the smallest useful d and
bz9t T runs (stops at the first word of weight < T); a timeout is printed as UNDECIDED.
Usage: xscan.py cells.csv bz9t lmax [amin cap_seconds]"""
import sys, os, csv, itertools, subprocess
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..', '..', 'constructor', 'code'))
sys.path.insert(0, os.path.join(H, '..', '..', 'already-settled', 'code'))
from hermitian import pts, pw
from gf9lib import MUL, gram_rank, rref9
from closure_exact import close
listed = {}
for r in csv.DictReader(open(sys.argv[1])):
    listed[(int(r['n']), int(r['k']), int(r['c']))] = (int(r['d_lower']), int(r['d_upper']), r['title'])
bz9, lmax = sys.argv[2], int(sys.argv[3])
amin = int(sys.argv[4]) if len(sys.argv) > 4 else 0
cap = float(sys.argv[5]) if len(sys.argv) > 5 else None
import time
lit_seeds = [(27, 0, 19, 21), (27, 0, 17, 20), (27, 1, 16, 19), (27, 1, 14, 18), (27, 2, 13, 17), (27, 4, 13, 16),
             (27, 4, 11, 15), (27, 4, 9, 14), (27, 6, 9, 13), (27, 6, 7, 12), (27, 7, 6, 11), (27, 9, 6, 10),
             (27, 9, 4, 9), (27, 11, 4, 8), (27, 13, 4, 7), (27, 13, 2, 6), (27, 14, 1, 6), (27, 16, 1, 4)]
five = [(28, 5, 11, 15), (28, 7, 9, 13), (28, 7, 11, 14), (28, 6, 6, 12), (28, 9, 7, 11)]
taken = [(14, 3, 5, 8), (14, 0, 2, 8), (13, 0, 3, 8), (12, 0, 4, 8), (11, 0, 5, 8), (16, 4, 4, 8),
         (34, 2, 24, 24), (33, 3, 24, 23), (33, 1, 24, 31)]   # same list as already-settled/code/closure_exact.py
base = close(lit_seeds + five + taken + [(28, 6, 10, 14)])
def newly_beaten(seed):
    return {key: d for key, d in close([seed]).items() if key in listed and key[1] >= 1 and key[2] >= 1 and d > listed[key][0] and d > base.get(key, 0)}
def run_bz(G, T=None, limit='cap'):
    inp = f"{len(G)} {len(G[0])}\n" + "\n".join(" ".join(map(str, r)) for r in G) + "\n"
    try:
        return subprocess.run([bz9] + ([str(T)] if T else []), input=inp.encode(), stdout=subprocess.PIPE, timeout=cap if limit == 'cap' else None).stdout.decode().strip()
    except subprocess.TimeoutExpired:
        return None
mons = sorted([(i, j) for j in range(3) for i in range(30) if 3 * i + 4 * j <= 26], key=lambda t: 3 * t[0] + 4 * t[1])
rows = [[MUL[pw(x, i)][pw(y, j)] for x, y in pts] for i, j in mons]
pole = [3 * i + 4 * j for i, j in mons]
nongaps = sorted(set(pole))
dcache = {}
def dplain(m):
    if m not in dcache:
        dcache[m] = int(run_bz([rows[i] for i in range(len(pole)) if pole[i] <= m], limit=None).split()[2].split('=')[1])
    return dcache[m]
hits = 0; scanned = 0; undecided = 0; pruned = 0; below = 0
def progress(a, b, t0):
    print(f"# pair a={a} b={b} done {time.strftime('%H:%M:%SZ', time.gmtime())} ({time.time() - t0:.0f} s)", flush=True)
for a, b in itertools.combinations(nongaps, 2):
    Ka = sum(1 for p in pole if p <= a); Kb = sum(1 for p in pole if p <= b); r = Kb - Ka
    if Ka < 1 or Kb > 24 or a < amin: continue
    t0 = time.time()
    for l in range(r, lmax + 1):
        if l > 9: break
        aux = [[pw(e, t) if not (e == 0 and t == 0) else 1 for e in range(l)] for t in range(r)]   # RS: rows e^t, 0^0 = 1
        best = None
        for signs in itertools.product((1, 3), repeat=l):   # 3 encodes w (norm -1)
            G = [rows[i] + [0] * l for i in range(Ka)] + [rows[Ka + t] + [MUL[signs[e]][aux[t][e]] for e in range(l)] for t in range(r)]
            h = Kb - gram_rank(G)
            if best is None or h > best[0]: best = (h, signs, G)
        h, signs, G = best
        if len(rref9(G)[0]) < Kb: continue
        n = 27 + l; k, c = Kb - h, n - Kb - h; scanned += 1
        if k < 0 or c < 0: continue
        dlb = min(dplain(a), dplain(b) + l - r + 1); dub = min(dplain(a), dplain(b) + l, n - Kb + 1)
        if not newly_beaten((n, k, c, dub)):
            pruned += 1; continue
        if newly_beaten((n, k, c, dlb)):
            d = dlb   # proved lower bound already beats a new cell
        else:
            T = min(t for t in range(dlb, dub + 1) if newly_beaten((n, k, c, t)))
            out = run_bz(G, T)
            if out is None:
                undecided += 1
                print(f"UNDECIDED X(a={a},b={b},l={l}) [{n},{Kb}] hull {h} -> [[{n},{k},d;{c}]], {dlb} <= d <= {dub}, needs d >= {T}: bz9t over {cap:.0f} s", flush=True)
                continue
            if "BELOW" in out:
                below += 1; continue
            d = int(out.split()[2].split('=')[1])
        nb = newly_beaten((n, k, c, d))
        if nb:
            hits += 1
            print(f"X(a={a},b={b},l={l}) [{n},{Kb},{d}] hull {h} signs {''.join('+' if s == 1 else '-' for s in signs)} -> [[{n},{k},{d};{c}]] newly beats {len(nb)}: "
                  + ", ".join(f"({p},{q},{s}) {dd}>{listed[(p,q,s)][0]}" for (p, q, s), dd in sorted(nb.items())[:10]), flush=True)
    progress(a, b, t0)
print(f"scanned {scanned} codes, {hits} with newly beaten listed cells; {pruned} pruned by the upper bound, {below} decided by bz9t (word below target), {undecided} undecided (bz9t capped)")
