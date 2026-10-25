# Losing chess (antichess): solve one of White's six first moves still marked Unknown (1.a4, 1.b3, 1.c4, 1.g3, 1.g4, 1.Nh3)

🕸️ **Graphs, games and automata** · standard · tractability ★☆☆☆☆ · compute: needs cluster (published first-move proof files are 4 MB to 1.3 GB of bz2; the final leg of 1.e3 b6 took a few hours on 128 cores); a move that turns out easy could fall in laptop-days · open as of 2026-10-25

## The problem

Losing chess, main variant (captures compulsory, the king is an ordinary piece that can be captured, no check or castling, pawns may promote to king; a player wins by losing all pieces or by being stalemated; fifty-move rule and repetition draws as in chess), was weakly solved by Mark Watkins in October 2016: 1.e3 wins for White under both FICS and International stalemate rules (final proof about 900 million positions; ICGA Journal 39/2). Of White's 20 legal first moves, 13 are known Black wins: 1.e4, 1.d4 and 1.d3 classically; 1.Nc3, 1.Nf3, 1.f4 and 1.h4 (proofs in the Nilatac opening book); 1.b4, 1.c3, 1.f3 and 1.h3 by computer (Nye, Steenhuis); 1.a3 (Klaas Steenhuis, October 2015, via 1...e6) and 1.Na3 (Steenhuis, June 2020, via 1...e6, a 1.3 GB proof file). Wikipedia's 'Losing chess' article names the 13 first moves after which Black is known to win and Watkins' 1.e3, and shows the rest as 'Unknown' in its solution diagram; by elimination these are 1.a4, 1.b3, 1.c4, 1.g3, 1.g4 and 1.Nh3. Task: settle one of these six, either as a forced Black win after it or as a forced White win with it. Status checked 2026-10-25: the Wikipedia article still says a Black win is known after 13 of White's 20 first moves and names them, and Watkins' page (proof files through May 2021) lists no proof after any of the six.

## What counts as a win

CONFIRMED: for one first move X in {1.a4, 1.b3, 1.c4, 1.g3, 1.g4, 1.Nh3} that is still not listed as solved on Wikipedia's 'Losing chess' page and on Watkins' Losing Chess page at verification time, a complete proof tree that the unmodified verifier verify_win.c from Watkins' current source tarball (CombinedJan05.tar on his page, which includes the April 2019 double-en-passant fix) accepts, proving a forced win for one side after 1.X under International stalemate rules (stalemated player wins) AND under FICS rules (stalemate won by the side with fewer pieces, equal counts drawn), as Watkins' 1.e3 proof does; a Black-win proof may use the tarball's NULL-move inversion (proof_invert) as Watkins' 1.h3 and 1.b4 files do. Every tablebase leaf must be resolved by tablebases rebuilt from scratch by the verifier (4- and 5-unit with the 2019 fix) or by a second, independently generated tablebase set, or else expanded to terminal positions. A second check by an independently written antichess move generator over all leaves and a random 1% of internal nodes must agree.

## Partial wins

- **p1:** The same proof for one of the six moves under ONE stalemate ruleset only (International or FICS), verified exactly as in the success criterion and labelled with its ruleset.
- **p2:** An independent re-verification of a published first-move proof that has only been checked with Watkins' own code (for example Na3e6.proof.bz2, a3e6_rev_new.proof.bz2 or c3e5.rev.bz2), using a verifier and tablebases that share no code with Watkins' tarball, with every disagreement (tablebase errors included) reported; or a proof that one of these files is wrong.

## How a win is checked

Download the proof (.bz2) and check its md5. Build Watkins' tarball, regenerate the 4- and 5-unit tablebases with its builder (the Apr 2019 version fixes double en passant), uninvert NULL-move files with ./proof_invert uninvert, and run verify_win. The verifier checks that every reply of the losing side is present, that hash-identified nodes are the same position, and that terminal nodes are wins under the stated ruleset. Then run an independent checker: an antichess move generator (for example python-chess's antichess variant, after confirming its stalemate rule matches the claimed ruleset) regenerates the losing side's moves at every node of a 1% random sample plus all leaves, and an independently built tablebase set (or explicit expansion) scores the leaves.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://en.wikipedia.org/wiki/Losing_chess>

## Sources

- <https://en.wikipedia.org/wiki/Losing_chess>
- <https://magma.maths.usyd.edu.au/~watkins/LOSING_CHESS/>
- <https://magma.maths.usyd.edu.au/~watkins/LOSING_CHESS/LCsolved.pdf>
- <https://chessprogramming.org/Losing_Chess>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Reuse Watkins' machinery (source tarball): an upper-level best-first tree whose leaves are expanded by bounded proof-number searches (1e7 to 1e8 nodes each), N independent pn-searches in parallel, the 'NULL move' trick for Black-win proofs, and 4-6-unit tablebases. On a many-core machine this is the same shape of run that produced 1.e3 b6's final leg in hours on 128 cores.
- Choose the move first: run a strong antichess engine (for example Fairy-Stockfish or the Nilatac book) on each of the six moves and start with the one whose evaluation is most lopsided; a Black win after 1.X needs only one refuting reply, a White win needs all Black replies.
- Look for transpositions into solved territory: many antichess lines become forced capture chains within a few moves; positions reached after 1.X may coincide with nodes of the published 1.e3 or 1.a3/1.Na3 proof trees, whose subtrees can be reused after re-verification.
- Build selective 6-unit tablebases for the endgames the search keeps reaching, as Steenhuis's long 1.a3 and 1.Na3 proofs suggest is necessary.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Stalemate rulesets differ (International, FICS, joint); a proof is valid only for the ruleset it names, and the full win needs both.
- Tablebase bugs: a double-en-passant bug corrupted 40 positions of the 2016 proof (fixed 2019), and Steenhuis reports other wrong 4-piece tablebases. Leaves scored by an unverified tablebase are not proof.
- Inverted (NULL-move) proof files break the verifier unless uninverted first.
- Fifty-move-rule and repetition handling: a line that only 'wins' by a repetition or a 50-move shuffle the rules count as a draw is not a win.
- The six moves may be large: Steenhuis's 1.Na3 proof file is 1.3 GB of bz2, larger than the whole 1.e3 proof, so a week of one machine may only reach partial win p1 or nothing.
- Wikipedia names the 13 Black wins in its text but marks the remaining six as 'Unknown' only in a diagram; confirm on Watkins' page and in recent antichess literature that the chosen move is still unsolved before claiming (asking the antichess community is a human action).

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/antichess-open-first-moves.md
```

Already set up? Say `run V3R1T4S on antichess-open-first-moves`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `antichess-open-first-moves`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
