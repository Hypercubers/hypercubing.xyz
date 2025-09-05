# Grip Theory

<style>
.spoiler:not(:hover) {
    color: black;
    background: black;
}
</style>

!!! warning "This whole page is under construction"

## Grips

A **grip** is a thing you can turn. Every puzzle has a **grip set**.

On a 3×3×3, the grip set is $\{ R, L, U, D, F, B \}$.

## Twists

A **twist** has two things:

- A grip from the grip set, which we'll call $\gamma$ ("gamma").
- A rearrangement of all the grips in the grip set, which has to keep $\gamma$ in the same place.

For example, on a 3×3×3 the `R'` twist has the grip $R$ and the permutation that cycles $U \to F \to D \to B \to U$ and keeps $R$ and $L$ fixed.

## Pieces

- A **piece** is a thing that moves around. On a 3^3^, there are 27 pieces. Every puzzle has a **piece set**.
- Each piece has a **grip signature**, which is a subset of the puzzle's grip set that determines which twists affect the piece.

For example, the grip signature of the RUF corner is $\{ R, U, F \}$.

Surprisingly, a grip signature is the only thing we need in order to describe where a piece goes after a sequence of moves.

## Applying twists

To apply a twist to a puzzle, take each piece that has the twist's grip in its grip signature and change the grips in the grip signature according to the twist's permutation.

For example, `R'` changes the grip signature of the ${U, R, F}$ corner to ${F, R, D}$. Now that corner will be affected by `F`, `R`, and `D` moves, but not `U` moves.

!!! warning "The rest of this page is under construction"

## Attitudes

## Grip group from twists

## Complex puzzles

### Anti moves

## Indistinguishable pieces

TODO: attitude sets

## Blocked grips

To model bandaging, ...

TODO

## Jumbling

TODO: ouch
