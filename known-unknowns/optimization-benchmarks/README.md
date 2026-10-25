# 🚚 Optimization benchmarks

Best-known solutions on public routing, scheduling and MIP benchmark libraries.

**14 open problems**, easiest first. Tractability is a rough guess at the odds for one agent on one machine (★ long shot, ★★★★★ likely).

| Odds | Problem | Kind | Compute |
|---|---|---|---|
| ★★★★☆ | [QOBLIB minimum Birkhoff decomposition: an exact decomposition of B5_25_2 with at most 13…](qoblib-birkhoff-small-exact-records.md) | harvest | laptop-hours to laptop-days for search; exact checking takes seconds; 5x5 and 6x6 integer matrices, respectively 120 and 720 possible permutation columns |
| ★★★★☆ | [QOBLIB ten-asset portfolio: close the exact optimum gap for a010_t10_orig_b004_l1e-03](qoblib-portfolio-ten-assets-exact.md) | standard | laptop-hours to laptop-days; 10 assets, 10 periods, 600 position binaries before presolve, plus 110 slack bits; exploit interchangeable unit copies and the four-position budget |
| ★★★☆☆ | [IHTC-2024 competition (m01-m30) instances: lower a best known integrated surgery-admissio…](ihtp-ihtc2024-hidden-m-instances-upper-bounds.md) | harvest | laptop-hours |
| ★★★☆☆ | [Integrated Healthcare Timetabling (IHTC-2024): lower the best known cost of a public (i01…](ihtp-ihtc2024-upper-bounds.md) | harvest | laptop-hours |
| ★★★☆☆ | [SMT-COMP 2026 P4/DFA bit-vector holdouts: one exact SAT model or UNSAT certificate](smt2026-p4-dfa-unknown-certificates.md) | harvest | laptop-hours to laptop-days using alternative preprocessing and solver configurations; require model/proof checking within laptop-hours |
| ★★☆☆☆ | [CVRPLIB VRPTW (Gehring-Homberger, DIMACS truncated-distance objective): beat an open best…](cvrplib-vrptw-gh-dimacs-bks.md) | harvest | laptop-hours |
| ★★☆☆☆ | [CVRPLIB: beat a best-known solution on an open X, XL or Arnold-XXL CVRP instance](cvrplib-x-xl-xxl-bks.md) | harvest | laptop-hours |
| ★★☆☆☆ | [MIPLIB 2017: improve the best known objective of an open collection instance](miplib2017-open-primal-bound.md) | harvest | laptop-hours |
| ★★☆☆☆ | [SINTEF Li & Lim PDPTW benchmark: hierarchically beat a best-known solution on a 600/800/1…](sintef-lilim-pdptw-bks.md) | harvest | laptop-hours |
| ★★☆☆☆ | [Job-shop scheduling: lower the makespan upper bound on an open Taillard / Demirkol / SWV…](jsp-optimizizer-open-upper-bounds.md) | harvest | laptop-hours |
| ★★☆☆☆ | [MINLPLib finance and marketing instances still open: beat saa_2 (strategic asset allocati…](minlplib-finance-open-instances.md) | standard | laptop-hours (saa_2 has 4,408 variables and 400 binaries but may reduce to a few asset weights plus a funding scalar; pricing050 has 50 continuous variables) |
| ★★☆☆☆ | [Nurse rostering benchmark (Curtois / schedulingbenchmarks.org): close an open gap on BCV-…](curtois-nrp-open-gaps-bcv-mer-instance24.md) | standard | laptop-hours |
| ★★☆☆☆ | [PSPLIB J120 (single-mode RCPSP): lower a best known heuristic makespan on an unproven ins…](psplib-j120-rcpsp-upper-bounds.md) | harvest | laptop-hours |
| ★★☆☆☆ | [SAT Competition 2026: first certified solve of a Main-track instance whose result is unkn…](sat-competition-2026-unknown-first-solve.md) | harvest | laptop-days per instance (portfolio of CDCL and local-search solvers, cube-and-conquer on a multi-core machine); an UNSAT proof from a multi-day run can need tens to hundreds of GB of disk |

← [All categories](../README.md)
