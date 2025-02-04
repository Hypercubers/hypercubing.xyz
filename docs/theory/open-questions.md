# Open Questions

These are open questions in Hypercubing puzzle theory. They are sometimes written in specific ways, but really we want to solve the general case.

- What puzzle property preconditions exist for certain algorithms?
    - How do we express them?
- How do we simplify twist applications to pieces?
    - E.g., On 3^3^, `R U' R' F` applied to the DFR corner simplifies to the identity
    - E.g., On 3^3^, `D' L2 U R2` applied to the DFR corner simplifies to the identity
- For a positive integer N, consider the symmetric [two-disk] puzzle with the lowest twist order that contains the N-acron. Consider the shallowest such puzzle (up to isomorphism) that still contains the N-acron. What is the order of `[R, L]`?
- How do we rigorously define "N-acron" or "\<shape\>-acron"?
    - "N-acron" roughly means "piece with N grips symmetrically in a ring" but there's nuance
        - Do the grips need to be exchangeable?
        - What if there are 2N grips (as in non-symmetric [two-disk] puzzles)?
- Special positions: what do they look like, are all paths through a puzzle's state space homotopic to a special path, and can this formalize 4D jumbling?

## Missing terminology

!!! warning "DO NOT just come up with new words for these"

    We want terms that are meaningful and tie in well with the rest of the theory. Some of these concepts may be well-described by some combination of words, but it's challenging to come up with a good combination of such words.

    In other words, we're looking for a ["basis"](https://en.wikipedia.org/wiki/Basis_(linear_algebra)) for the space of concepts.

- More piece types
- "For a positive integer N, consider the symmetric [two-disk] puzzle with the lowest twist order that contains the N-acron. Consider the shallowest such puzzle (up to isomorphism) that still contains the N-acron."
- cut depth equivalence classes ([Orb] phase diagram)
- "shallowest such puzzle up to isomorphism"

## Missing formalisms

- Connectivity of grips
    - can exchange grips A & B on a single piece
    - can interact (depends on piece types)
- Accessible grips
    - i.e., what grips exist as axes on the puzzle (only 2 on [two-disk] puzzles)

[two-disk]: https://www.twodisks.org/play/
[Orb]: https://milojacquet.com/twisty/orb
