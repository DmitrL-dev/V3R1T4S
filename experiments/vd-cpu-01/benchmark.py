"""VD-CPU-01 r2. Standard library only. OPEN engineering regression."""
import argparse
import collections
import contextlib
import hashlib
import itertools
import json
import math
import pathlib
import random
import resource
import signal
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parent
FROZEN = ('benchmark.py', 'test_benchmark.py', 'PROTOCOL.md', 'README.md')
FAULTS = {'graph': ('omit_degree', 'omit_diameter', 'one_source', 'off_by_one'),
          'code': ('omit_count', 'omit_distance', 'first_pair', 'off_by_one')}


def integer(x):
    return type(x) is int


def valid_a(c):
    if type(c) is not dict or set(c) != {'family', 'object', 'claim'}:
        return False
    o, q = c['object'], c['claim']
    if type(o) is not dict or type(q) is not dict:
        return False
    if c['family'] == 'graph':
        if set(o) != {'n', 'edges'} or set(q) != {'vertices', 'degree', 'diameter'}:
            return False
        n, es = o['n'], o['edges']
        if not integer(n) or not 4 <= n <= 7 or type(es) is not list:
            return False
        seen = set()
        for e in es:
            if type(e) is not list or len(e) != 2 or any(not integer(x) for x in e):
                return False
            a, b = e
            if not 0 <= a < b < n or (a, b) in seen:
                return False
            seen.add((a, b))
        return all(integer(v) and v >= 0 for v in q.values())
    if c['family'] == 'code':
        if set(o) != {'length', 'words'} or set(q) != {'count', 'weight', 'distance'}:
            return False
        n, ws = o['length'], o['words']
        return (integer(n) and 4 <= n <= 8 and type(ws) is list and len(ws) >= 2
                and all(type(w) is str and len(w) == n and set(w) <= {'0', '1'} for w in ws)
                and len(set(ws)) == len(ws) and all(integer(v) and v >= 0 for v in q.values()))
    return False


def valid_b(c):
    # Deliberately separate complete format implementation, not independence evidence.
    try:
        if type(c) != dict or sorted(c) != ['claim', 'family', 'object']:
            return False
        o, q = c['object'], c['claim']
        if type(o) != dict or type(q) != dict:
            return False
        if any(type(v) != int or v < 0 for v in q.values()):
            return False
        if c['family'] == 'graph':
            if sorted(o) != ['edges', 'n'] or sorted(q) != ['degree', 'diameter', 'vertices']:
                return False
            n = o['n']
            if type(n) != int or n not in range(4, 8) or type(o['edges']) != list:
                return False
            pairs = []
            for pair in o['edges']:
                if type(pair) != list or len(pair) != 2:
                    return False
                if any(type(v) != int for v in pair) or not (0 <= pair[0] < pair[1] < n):
                    return False
                pairs.append(tuple(pair))
            return len(set(pairs)) == len(pairs)
        if c['family'] == 'code':
            if sorted(o) != ['length', 'words'] or sorted(q) != ['count', 'distance', 'weight']:
                return False
            n, words = o['length'], o['words']
            if type(n) != int or n not in range(4, 9) or type(words) != list or len(words) < 2:
                return False
            for word in words:
                if type(word) != str or len(word) != n or any(ch not in '01' for ch in word):
                    return False
            return len(words) == len(set(words))
        return False
    except (KeyError, TypeError, ValueError):
        return False


def graph_oracle(o):
    n = o['n']
    adj = [[False] * n for _ in range(n)]
    for u, v in o['edges']:
        adj[u][v] = adj[v][u] = True
    reach = [[i == j for j in range(n)] for i in range(n)]
    diameter = math.inf
    # Boolean matrix multiplication: paths of length at most k.
    for k in range(1, n):
        reach = [[reach[i][j] or any(reach[i][t] and adj[t][j] for t in range(n))
                  for j in range(n)] for i in range(n)]
        if all(all(row) for row in reach):
            diameter = k
            break
    return n, max(map(sum, adj)), diameter


def graph_a(o, source_only=False):
    n = o['n']
    adj = [set() for _ in range(n)]
    for u, v in o['edges']:
        adj[u].add(v)
        adj[v].add(u)
    diam = 0
    for s in range(1 if source_only else n):
        d = {s: 0}
        queue = collections.deque([s])
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if v not in d:
                    d[v] = d[u] + 1
                    queue.append(v)
        if len(d) < n:
            return n, max(map(len, adj)), math.inf
        diam = max(diam, max(d.values()))
    return n, max(map(len, adj)), diam


def graph_b(o):
    n = o['n']
    d = [[0 if i == j else math.inf for j in range(n)] for i in range(n)]
    deg = [0] * n
    for i, j in o['edges']:
        d[i][j] = d[j][i] = 1
        deg[i] += 1
        deg[j] += 1
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return n, max(deg), max(map(max, d))


def code_oracle(o):
    ws = o['words']
    return len(ws), [sum(ch == '1' for ch in w) for w in ws], min(
        sum(a[k] != b[k] for k in range(o['length'])) for a, b in itertools.combinations(ws, 2))


def code_a(o, first_pair=False):
    ints = [int(w, 2) for w in o['words']]
    pairs = [(ints[0], ints[1])] if first_pair else itertools.combinations(ints, 2)
    return len(ints), [x.bit_count() for x in ints], min((a ^ b).bit_count() for a, b in pairs)


def code_b(o):
    sets = [{i for i, ch in enumerate(w) if ch == '1'} for w in o['words']]
    return len(sets), [len(s) for s in sets], min(
        len(a) + len(b) - 2 * len(a.intersection(b)) for a, b in itertools.combinations(sets, 2))


def verify(c, engine='A', fault=None):
    if fault == 'always_pass':
        return True
    if fault == 'always_fail':
        return False
    if not (valid_b(c) if engine == 'B' else valid_a(c)):
        return False
    o, q = c['object'], c['claim']
    tolerance = int(fault == 'off_by_one')
    if c['family'] == 'graph':
        n, degree, diameter = (graph_a(o, fault == 'one_source') if engine == 'A'
                              else graph_b(o) if engine == 'B' else graph_oracle(o))
        return (diameter != math.inf and n == q['vertices']
                and (fault == 'omit_degree' or degree <= q['degree'] + tolerance)
                and (fault == 'omit_diameter' or diameter <= q['diameter'] + tolerance))
    count, weights, distance = (code_a(o, fault == 'first_pair') if engine == 'A'
                               else code_b(o) if engine == 'B' else code_oracle(o))
    return (all(w == q['weight'] for w in weights)
            and (fault == 'omit_count' or abs(count - q['count']) <= tolerance)
            and (fault == 'omit_distance' or distance + tolerance >= q['distance']))


def canonical_graph(o):
    n = o['n']
    es = {tuple(e) for e in o['edges']}
    degrees = [sum(i in e for e in es) for i in range(n)]
    groups = [[i for i in range(n) if degrees[i] == d] for d in sorted(set(degrees))]
    # Isomorphisms preserve degrees; order only within equal-degree blocks.
    return (n, min(tuple(int(tuple(sorted((p[i], p[j]))) in es)
                         for i in range(n) for j in range(i + 1, n))
                   for blocks in itertools.product(*(itertools.permutations(g) for g in groups))
                   for p in [sum((tuple(b) for b in blocks), ())]))


def canonical_code(o):
    # Coordinate permutation = column order; word order = row permutation.
    ws = o['words']
    return o['length'], min(tuple(sorted(''.join(ws[r][j] for r in rows)
                                         for j in range(o['length'])))
                            for rows in itertools.permutations(range(len(ws))))


def generate():
    rng = random.Random(6202601)
    bases = []
    for family in ('graph', 'code'):
        seen = set()
        attempts = 0
        while len(seen) < 24:
            attempts += 1
            if attempts > 10000:
                raise RuntimeError('bounded generation exhausted')
            index = len(seen)
            if family == 'graph':
                n = 4 + index % 4
                edges = {(rng.randrange(v), v) for v in range(1, n)}
                edges.update((u, v) for u in range(n) for v in range(u + 1, n) if rng.random() < .35)
                o = {'n': n, 'edges': [list(e) for e in sorted(edges)]}
                key = canonical_graph(o)
                v, d, dia = graph_oracle(o)
                q = {'vertices': v, 'degree': d, 'diameter': dia}
            else:
                n = 4 + index % 5
                w = rng.randint(1, n - 1)
                pool = [''.join('1' if j in s else '0' for j in range(n))
                        for s in itertools.combinations(range(n), w)]
                ws = sorted(rng.sample(pool, min(len(pool), 2 + index % 4)))
                o = {'length': n, 'words': ws}
                key = canonical_code(o)
                count, weights, distance = code_oracle(o)
                q = {'count': count, 'weight': weights[0], 'distance': distance}
            if key in seen:
                continue
            seen.add(key)
            bases.append({'id': f'{family}-{index:02}', 'split': 'development' if index < 12 else 'regression',
                          'family': family, 'object': o, 'claim': q})
    cases = []
    for b in bases:
        c = {k: b[k] for k in ('family', 'object', 'claim')}
        o = b['object']
        if b['family'] == 'graph':
            p = list(reversed(range(o['n'])))
            transformed = {'n': o['n'], 'edges': sorted([sorted([p[u], p[v]]) for u, v in o['edges']])}
            negative_keys = ('degree', 'diameter')
            delta = -1
        else:
            transformed = {'length': o['length'], 'words': [w[::-1] for w in reversed(o['words'])]}
            negative_keys = ('distance', 'count')
            delta = 1
        variants = [('true', c, True), ('permuted_true', dict(c, object=transformed), True)]
        for key in negative_keys:
            variants.append(('false_' + key, dict(c, claim=dict(c['claim'], **{key: c['claim'][key] + delta})), False))
        for name, claim, expected in variants:
            cases.append({'id': b['id'] + '/' + name, 'base': b['id'], 'split': b['split'],
                          'variant': name, 'expected': expected, 'input': claim})
    return bases, cases


@contextlib.contextmanager
def deadline():
    def expired(signum, frame):
        raise TimeoutError('2 second case limit')
    previous = signal.signal(signal.SIGALRM, expired)
    signal.setitimer(signal.ITIMER_REAL, 2)
    try:
        yield
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, previous)


def evaluate(cases):
    rows = []
    for case in cases:
        with deadline():
            c = case['input']
            a, b, oracle = (verify(c, engine) for engine in ('A', 'B', 'oracle'))
            faults = {}
            for fault in FAULTS[c['family']] + ('always_pass', 'always_fail'):
                mutant = verify(c, 'A', fault)
                faults[fault] = {'A': mutant, 'A_and_B': mutant and b,
                                 'activated': mutant != a, 'A_wrong': mutant != oracle,
                                 'combined_wrong': (mutant and b) != oracle}
            rows.append({**{k: v for k, v in case.items() if k != 'input'},
                         'A': a, 'B': b, 'oracle': oracle, 'faults': faults})
    return rows


def summarize(rows):
    result = {}
    for family in FAULTS:
        for split in ('development', 'regression', 'all'):
            subset = [r for r in rows if r['base'].startswith(family) and (split == 'all' or r['split'] == split)]
            for fault in FAULTS[family] + ('always_pass', 'always_fail'):
                stats = {'activation': 0, 'A_errors': 0, 'combined_errors': 0, 'added_corrections': 0,
                         'A_confusion': dict(TP=0, TN=0, FP=0, FN=0),
                         'combined_confusion': dict(TP=0, TN=0, FP=0, FN=0)}
                for r in subset:
                    f = r['faults'][fault]
                    stats['activation'] += f['activated']
                    stats['A_errors'] += f['A_wrong']
                    stats['combined_errors'] += f['combined_wrong']
                    stats['added_corrections'] += f['A_wrong'] and not f['combined_wrong']
                    for field, dest in [('A', 'A_confusion'), ('A_and_B', 'combined_confusion')]:
                        label = ('T' if f[field] == r['oracle'] else 'F') + ('P' if f[field] else 'N')
                        stats[dest][label] += 1
                stats['unactivated'] = stats['activation'] == 0
                stats['missed_cases'] = [r['id'] for r in subset if r['faults'][fault]['combined_wrong']]
                result[f'{family}/{split}/{fault}'] = stats
    return result


def hashes():
    return {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in FROZEN}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=['freeze', 'run'])
    parser.add_argument('--spectorn-finished', action='store_true', help='Only after root explicitly authorizes run timing')
    args = parser.parse_args()
    manifest = ROOT / 'freeze.json'
    if args.command == 'freeze':
        if manifest.exists():
            raise SystemExit('Freeze exists; no silent overwrite or post-result tuning')
        manifest.write_text(json.dumps({'protocol': 'VD-CPU-01-r2', 'sha256': hashes()}, indent=2) + '\n')
        print('Frozen source only. No dataset or evaluation executed.')
        return
    if not args.spectorn_finished:
        raise SystemExit('Evaluation blocked until root confirms Spectorn heavy test is finished')
    if json.loads(manifest.read_text())['sha256'] != hashes():
        raise SystemExit('Freeze mismatch')
    resource.setrlimit(resource.RLIMIT_AS, (512 * 1024**2,) * 2)
    resource.setrlimit(resource.RLIMIT_CPU, (600, 600))
    started = time.process_time()
    bases, cases = generate()
    rows = evaluate(cases)
    repeat = evaluate(cases)
    groups = collections.defaultdict(list)
    for r in rows:
        groups[r['base']].append(r)
    metamorphic = [{'base': key, 'preserved': group[0]['oracle'] == group[1]['oracle'] == True}
                   for key, group in sorted(groups.items())]
    acceptance = {'size': len(bases) == 48 and len(cases) == 192,
                  'agreement': all(r['A'] == r['B'] == r['oracle'] == r['expected'] for r in rows),
                  'metamorphic': all(m['preserved'] for m in metamorphic), 'deterministic_matrix': rows == repeat,
                  'controls': all(any(r['faults'][f]['A_wrong'] for r in rows if r['base'].startswith(family))
                                  for family in FAULTS for f in ('always_pass', 'always_fail'))}
    report = {'protocol': 'VD-CPU-01-r2', 'freeze': json.loads(manifest.read_text()),
              'python': sys.version, 'platform': sys.platform,
              'acceptance': acceptance, 'summary': summarize(rows), 'metamorphic': metamorphic, 'matrix': rows,
              'cpu_seconds': time.process_time() - started,
              'peak_rss_kib': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    data = json.dumps({'bases': bases, 'cases': cases}, indent=2) + '\n'
    output = json.dumps(report, indent=2) + '\n'
    if len(data.encode()) + len(output.encode()) > 20 * 1024**2:
        raise SystemExit('Artifact budget exceeded')
    out = ROOT / 'results'
    out.mkdir(exist_ok=False)
    (out / 'dataset.json').write_text(data)
    (out / 'report.json').write_text(output)
    print(json.dumps({'acceptance': acceptance, 'cpu_seconds': report['cpu_seconds'], 'results': str(out)}, indent=2))
    raise SystemExit(0 if all(acceptance.values()) else 1)


if __name__ == '__main__':
    main()
