# How we found it (contributor text, unverified)

We were hunting cells of Markus Grassl's table of entanglement-assisted qutrit codes, which are built from codes
over GF(9). After the extended one-point Hermitian codes of length 28 gave a confirmed cell, we scanned Construction
X: take two nested one-point codes C(D,aP) ⊂ C(D,bP) on the 27 affine points of the Hermitian curve y^3 + y = x^4,
and glue a short Reed-Solomon code onto the extra rows. The scan covered every nested pair and every tail length up
to 9, with exact minimum distances.

One code, a = 17, b = 20 with a tail of length 4, came out with minimum distance 10, one above what the
Construction X bound promises. Its qutrit cell was new, but the classical code itself looked unusual, so we read the
codetables.de cell for [31,18] over GF(9): lower bound 9, unchanged since 2001-12-17. In a second run we checked it
three different exact ways (Brouwer-Zimmermann, a certificate over all 9-subsets of the affine coordinates, and a
new program over all 9-subsets of all 31 coordinates), searched the literature, tried its neighbors (every
puncture has d = 9 and every shortening d = 10, both ties with the table), and sent it to a three-skeptic panel.
That run was cut off before the panel finished; a third run ran all three skeptics, one at a time, and the
criterion skeptic added a fifth exact check (all 9^13 dual codewords with the MacWilliams identities), which gives
the whole weight distribution: no word of weight 1 to 9 and 24864 of weight 10.

What failed: other nested pairs aimed at [30,18], [31,19] and [32,19] reach at most the table's 9.
