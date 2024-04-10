# Commutators

A commutator (or "comm") is a sequence of moves where you do a sequence A, then a sequence B, then the inverse of A, and finally the inverse of B. Usually, you want the intersection of the pieces affected by sequence A and the pieces affected by sequence B to be small but non-empty. In turn, creating a commutator with those sequences makes it easier to solve a puzzle by only affecting a few specific pieces at a time.

One of the earliest solutions for the 3×3×3×3 was [The Ultimate Solution to a 3×3×3×3](https://superliminal.com/cube/solution/solution.htm) by Roice Nelson, which made heavy use of intuitive setup moves and commutators. Commutators were also much easier to use in MC4D due to its Macro feature, which allowed users to record sequences of moves and then replay them later from any angle.

## Notation

Commutator notation extends traditional twisty puzzle notation by adding the following definitions:

- Commutators are notated `[A, B]`, which expands to `A B A' B'`.
- Conjugates are notated `[A: B]`, which expands to `A B A'`.

Here are some example commutators that can be executed on a 3×3×3:
- `[R, U]` expands to `R U R' U'`.
- `[M', U2]` expands to `M' U2 M U2`, which cycles 3 edges on the M slice.
- `[D: [M', U2]]` expands to `D (M' U2 M U2) D'`, which cycles 3 slightly different edges. Conjugates are often combined with commutators to influence different sets of pieces.
- `[F: [R, U]]` expands to `[F: R U R' U']`, which expands further to `F (R U R' U') F'`.
- `[D, [R, U]]` expands to `D (R U R' U') D' (U R U' R')`, which cycles 3 corners on the D layer.

(Parentheses are added for readability but have no special meaning.)

## Strategy

Once you find commutators for cycling different types of pieces on a puzzle (2c, 3c, etc) then you can almost solve the whole thing! (There may be some situations where you need an algorithm to swap 2 pieces of a type and 2 of a different type.)
