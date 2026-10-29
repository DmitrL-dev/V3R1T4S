# Results for (d=30, N=62)

Contributor text. This is the row for (d=30, N=62) from the search agent's results table, trimmed on 2026-10-27 to
this row. The agent's other rows are not part of this claim and are not shown. The minimal angle is corrected: the
agent's table gave 88.207884691079092710 degrees, and arccos of the c* below is 88.2078863822 degrees.

| (d, N) | `/plain` cos (12 decimals) | Our c* (12 decimals) | Our c* (30 digits) | Improvement | Minimal angle (degrees) | Contacts within 1e-9 | Table attribution |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| (30, 62) | 0.031273236170 | 0.031273183364 | 0.031273183363813242615324799071 | 5.280619e-08 | 88.2078863822 | 1437 | Ilmari Vahteristo, annealing solver |

The search code is `sc_opt.c` (Riemannian L-BFGS on a log-sum-exp smoothing of the largest inner product, with
basin-hopping kicks). The candidate was normalised and polished to 30 significant digits by a separate 50-digit script,
which is not shipped. The contact count is the agent's and is not checked by `../verify-it-yourself/`.
