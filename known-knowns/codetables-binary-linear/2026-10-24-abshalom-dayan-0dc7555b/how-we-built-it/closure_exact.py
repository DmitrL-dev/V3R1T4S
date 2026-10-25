"""Exact closure under the qutrit page's own propagation rules (as printed in its colour legend):
subcode [[n,k-1,d;c]], lengthening [[n+1,k,d;c]], puncturing [[n-1,k,d-1;c]], quantum shortening [[n-1,k+1,d-1;c]],
increasing dimension [[n,k+1,d;c+1]], length reduction [[n-1,k,d;c+1]] (k >= 0, 0 <= c <= n - k, n <= 36).
For each source set, report every LISTED cell whose d_lower is beaten by something the set implies.
Usage: closure_exact.py cells.csv"""
import sys, csv
listed = {}
for r in (csv.DictReader(open(sys.argv[1])) if __name__ == "__main__" else []):
    listed[(int(r['n']), int(r['k']), int(r['c']))] = (int(r['d_lower']), int(r['d_upper']), r['title'])
def close(seeds, nmax=36):
    best = {}
    def put(n, k, c, d):
        if 1 <= n <= nmax and 0 <= k <= n and 0 <= c <= n - k and d >= 1 and d > best.get((n, k, c), 0):
            best[(n, k, c)] = d; return True
        return False
    for s in seeds: put(*s)
    ch = True
    while ch:
        ch = False
        for (n, k, c), d in list(best.items()):
            for t in ((n, k - 1, c, d), (n + 1, k, c, d), (n - 1, k, c, d - 1), (n - 1, k + 1, c, d - 1),
                      (n, k + 1, c + 1, d), (n - 1, k, c + 1, d)):
                if put(*t): ch = True
    return best
def beaten(best):
    return sorted((key, d, listed[key]) for key, d in best.items() if key in listed and d > listed[key][0])
if __name__ == "__main__":
    cands = {"A [[28,5,15;11]] (claim)": (28, 5, 11, 15), "B [[28,7,13;9]]": (28, 7, 9, 13),
             "C [[28,7,14;11]]": (28, 7, 11, 14), "D [[28,6,12;6]]": (28, 6, 6, 12), "E [[28,9,11;7]]": (28, 9, 7, 11)}
    taken = [(14, 3, 5, 8), (14, 0, 2, 8), (13, 0, 3, 8), (12, 0, 4, 8), (11, 0, 5, 8), (16, 4, 4, 8),
             (34, 2, 24, 24), (33, 3, 24, 23), (33, 1, 24, 31)]
    bt = close(taken)
    print("== implied by repo/PR cells (#331 + consequences, #403, #404, #405, #363):")
    for name, (n, k, c, d) in cands.items():
        print(f"  {name}: best implied d at ({n},{k},{c}) = {bt.get((n, k, c))} -> {'IMPLIED' if bt.get((n, k, c), 0) >= d else 'not implied'}")
    print("== implied by the other candidates (each candidate against the closure of all the others):")
    for name, (n, k, c, d) in cands.items():
        others = [(a, b, e, f) for nm, (a, b, e, f) in cands.items() if nm != name]
        bo = close(others)
        print(f"  {name}: best implied d at ({n},{k},{c}) by the others = {bo.get((n, k, c))} -> {'IMPLIED' if bo.get((n, k, c), 0) >= d else 'not implied'}")
    print("== listed cells each candidate beats on its own (closure of that one code):")
    for name, (n, k, c, d) in cands.items():
        b = beaten(close([(n, k, c, d)]))
        print(f"  {name}: {len(b)} listed cells beaten; n=28: " + ", ".join(f"({a},{bb},{e}) {dd}>{v[0]}" for (a, bb, e), dd, v in b if a == 28))
    allb = beaten(close(list(cands.values())))
    print(f"== all five together: {len(allb)} listed cells beaten")
    for (a, bb, e), dd, v in allb:
        print(f"  ({a},{bb},{e}): {dd} > table {v[0]}-{v[1]} | {v[2][:80]}")
    for name, (n, k, c, d) in cands.items():
        dl, du, t = listed[(n, k, c)]
        print(f"table check {name}: listed {dl}-{du}; candidate d {d}: {'d > d_lower' if d > dl else 'NOT above d_lower'}, {'<= d_upper' if d <= du else 'ABOVE d_upper'}")
