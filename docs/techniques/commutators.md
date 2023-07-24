# Commutators

A commutator (or comm) is a sequence of moves where you do a sequence A, then a sequence B, then the inverse of A, and finally the inverse of B. After completion, only specific pieces are affected, making it easier to solve the puzzle.

One of the earliest solutions for the 3x3x3x3 was [The Ultimate Solution to a 3x3x3x3](https://superliminal.com/cube/solution/solution.htm) by Roice Nelson, which made heavy use of intuitive setup moves and commutators. Commutators were also much easier to use in MC4D due to the Macro feature, which could automatically execute any sequence of moves that you defined.

## Notation

Commutators are notated `[A, B]`, which means to do `A B A' B'`.

For example, the commutator `[M', U2]` cycles 3 edges in the M layer of a 3x3x3. Written out, it would be `M' U2 M U2`. 

Commutators can also be nested within commutators, such as `[D, [R, U]]`, which is a cycle of 3 corners, `D R U R' U' D' U R U' R'`.

## Strategy

Once you find commutators for cycling different types of pieces on a puzzle (2c, 3c, etc) then you can almost solve the whole thing! (There may be some situations where you need an algorithm to swap 2 pieces of a type and 2 of a different type.)
