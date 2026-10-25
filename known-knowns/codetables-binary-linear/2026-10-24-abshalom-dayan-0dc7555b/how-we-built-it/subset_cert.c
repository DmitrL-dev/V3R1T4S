/* Theory-free certificate that a code has no nonzero word of weight <= W, for codes whose first NA coordinates are
   the "affine" part (here the 27 Hermitian points) and the rest a tail. Every word c = mG of total weight <= W has
   affine weight <= W, so its affine support lies in some W-subset S of the NA affine coordinates; then m lies in the
   left null space of G restricted to the affine columns outside S. The program visits every W-subset S, computes that
   null space exactly over GF(9) (own arithmetic: GF(3)[w]/(w^2 - w - 1), a + b*w stored as a + 3b), enumerates every
   nonzero vector in it, and records the minimum total weight seen and how many words of weight <= W exist.
   Usage: subset_cert NA W < code   (code: "K n" then K rows of n entries 0..8)
   Output: "subsets=.. nonzero_nullspaces=.. max_dim=.. words_le_W=.. min_weight_seen=.." */
#include <stdio.h>
#include <stdlib.h>
static int AD[9][9], MU[9][9], NE[9], IV[9];
static void gf(void) {
  for (int x = 0; x < 9; x++) for (int y = 0; y < 9; y++) {
    int a1 = x % 3, b1 = x / 3, a2 = y % 3, b2 = y / 3;
    AD[x][y] = (a1 + a2) % 3 + 3 * ((b1 + b2) % 3);
    MU[x][y] = (a1 * a2 + b1 * b2) % 3 + 3 * ((a1 * b2 + a2 * b1 + b1 * b2) % 3);   /* w^2 = w + 1 */
  }
  for (int x = 0; x < 9; x++) { NE[x] = (3 - x % 3) % 3 + 3 * ((3 - x / 3) % 3); IV[x] = 0; for (int y = 1; y < 9; y++) if (MU[x][y] == 1) IV[x] = y; }
}
static int K, n, NA, W, G[64][64];
int main(int argc, char **argv) {
  if (argc < 3) { fprintf(stderr, "usage: subset_cert NA W < code\n"); return 2; }
  gf(); NA = atoi(argv[1]); W = atoi(argv[2]);
  if (scanf("%d %d", &K, &n) != 2 || K > 64 || n > 64 || NA > n) { printf("bad input\n"); return 2; }
  for (int i = 0; i < K; i++) for (int t = 0; t < n; t++) if (scanf("%d", &G[i][t]) != 1) { printf("bad input\n"); return 2; }
  for (int x = 1; x < 9; x++) if (MU[x][IV[x]] != 1) { printf("field error\n"); return 3; }
  int S[64]; for (int i = 0; i < W; i++) S[i] = i;
  long long subsets = 0, nonzero = 0, small = 0; int maxdim = 0, minw = 1 << 20;
  while (1) {
    subsets++;
    int in[64] = {0}; for (int i = 0; i < W; i++) in[S[i]] = 1;
    /* rows = affine columns outside S (as equations), unknowns = m (K). Matrix E[c][i] = G[i][col]. */
    int E[64][64], nr = 0;
    for (int t = 0; t < NA; t++) if (!in[t]) { for (int i = 0; i < K; i++) E[nr][i] = G[i][t]; nr++; }
    int piv[64], pc[64] = {0}, r = 0;
    for (int col = 0; col < K && r < nr; col++) {
      int p = -1; for (int i = r; i < nr; i++) if (E[i][col]) { p = i; break; }
      if (p < 0) continue;
      for (int j = 0; j < K; j++) { int tmp = E[r][j]; E[r][j] = E[p][j]; E[p][j] = tmp; }
      int iv = IV[E[r][col]]; for (int j = 0; j < K; j++) E[r][j] = MU[E[r][j]][iv];
      for (int i = 0; i < nr; i++) if (i != r && E[i][col]) { int f = E[i][col]; for (int j = 0; j < K; j++) E[i][j] = AD[E[i][j]][NE[MU[f][E[r][j]]]]; }
      piv[r] = col; pc[col] = 1; r++;
    }
    int dim = K - r;
    if (dim > 0) {
      nonzero++; if (dim > maxdim) maxdim = dim;
      if (dim > 6) { printf("null space too large (dim %d)\n", dim); return 4; }
      int fr[64], nf = 0; for (int j = 0; j < K; j++) if (!pc[j]) fr[nf++] = j;
      long long tot = 1; for (int i = 0; i < dim; i++) tot *= 9;
      for (long long code = 1; code < tot; code++) {
        int m[64] = {0}; long long cc = code;
        for (int i = 0; i < dim; i++) { m[fr[i]] = cc % 9; cc /= 9; }
        for (int i = 0; i < r; i++) { int s = 0; for (int j = 0; j < K; j++) if (!pc[j]) s = AD[s][MU[E[i][j]][m[j]]]; m[piv[i]] = NE[s]; }
        int w = 0;
        for (int t = 0; t < n; t++) { int s = 0; for (int i = 0; i < K; i++) s = AD[s][MU[m[i]][G[i][t]]]; if (s) w++;
          if (t < NA && in[t] == 0 && s) { printf("solver error\n"); return 5; } }
        if (w < minw) minw = w;
        if (w <= W) small++;
      }
    }
    int i = W - 1; while (i >= 0 && S[i] == NA - W + i) i--;
    if (i < 0) break;
    S[i]++; for (int j = i + 1; j < W; j++) S[j] = S[j - 1] + 1;
  }
  printf("subsets=%lld nonzero_nullspaces=%lld max_dim=%d words_le_W=%lld min_weight_seen=%d\n", subsets, nonzero, maxdim, small, minw);
  return 0;
}
