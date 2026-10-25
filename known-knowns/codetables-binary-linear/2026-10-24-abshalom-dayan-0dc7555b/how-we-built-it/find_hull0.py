"""Find columns of X(a,b,l,signs) whose scaling by w (norm -1) brings the Hermitian hull to a target h (seeded
random search over subsets of the 27 affine columns). Usage: find_hull0.py a b l signs target seed"""
import sys, os, random, subprocess, json
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..', '..', 'constructor', 'code'))
from gf9lib import MUL, gram_rank
a, b, l, sg, target, seed = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], int(sys.argv[5]), int(sys.argv[6])
tmp = os.path.join(H, '..', 'out', 'tmp_find_hull.json')
subprocess.run([sys.executable, os.path.join(H, 'build_x.py'), a, b, l, sg, tmp, '0'], check=True, stdout=subprocess.DEVNULL)
G0 = json.load(open(tmp))['G9']; os.remove(tmp); K = len(G0)
rnd = random.Random(seed)
for trial in range(1, 5001):
    cols = sorted(rnd.sample(range(27), rnd.randint(1, 14)))
    G = [[MUL[3][v] if t in cols else v for t, v in enumerate(row)] for row in G0]
    h = K - gram_rank(G)
    if h == target:
        print(f"trial {trial}: columns {','.join(map(str, cols))} -> hull {h}"); break
else:
    print("not found in 5000 trials")
