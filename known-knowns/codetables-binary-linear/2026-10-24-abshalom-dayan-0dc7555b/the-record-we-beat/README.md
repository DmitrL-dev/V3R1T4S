# Table snapshot: https://codetables.de/BKLC/BKLC.php?q=9&n=31&k=18

- URL: https://codetables.de/BKLC/BKLC.php?q=9&n=31&k=18 (Markus Grassl, bounds on the minimum distance of linear
  codes, cell [31,18] over GF(9))
- Fetches (one plain GET each, curl, User-Agent naming V3R1T4S, no retries):
  - before the claim (run 2026-10-24-1033's Construction X lens): 2026-10-24T12:09:31Z
  - the panel's NOVELTY skeptic: 2026-10-24T13:21:24Z
  - the panel's CRITERION skeptic: 2026-10-24T13:47:25Z
  - at the honesty gate: 2026-10-24T13:49:51Z
- HTTP status: 200 (all four)
- Selected headers (13:49:51Z gate fetch): `content-type: text/html; charset=UTF-8`, `date: Sat, 24 Oct 2026 13:49:51 GMT`,
  `server: Apache`
- Page size: 3395 bytes (all four)
- Page SHA-256: 1ab4ec8f7b8516b1e52d16ea00ef697c16be779f8e63150c645f7b4d92639c80 (all four)
- Page footer: "Last change: 30.12.2011"; the cell's construction: "last modified: 2001-12-17"

## Extracted cell for (q, n, k) = (9, 31, 18)

```html
<H3>Bounds on linear codes [31,18] over GF(9)</H3><TABLE><TR><TD>lower bound:</TD><TD>9</TD></TR><TR><TD>upper bound:</TD><TD>12</TD></TR></TABLE>
```

- Listed lower bound: 9 (a [41,29,9] BCH code over GF(9), its [41,28,9] subcode, shortened at positions 32..41)
- Listed upper bound: 12 (from Brouwer's table: "Ub(31,18) = 12 is found by considering shortening to: Ub(17,4) = 12")
- Our value: d = 10 (10 > 9, 10 <= 12)
- Neighboring cells (one GET each by the NOVELTY skeptic, 2026-10-24T13:22:05Z to 13:22:06Z), lower-upper:
  [30,17] 10-12, [30,18] 9-11, [31,17] 10-13, [31,19] 9-11, [32,18] 10-13, [32,19] 9-12. None gives [31,18,10] by
  shortening, puncturing, subcode or extension.
