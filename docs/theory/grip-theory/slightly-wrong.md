# Slightly Wrong Explanation of Grip Theory

Grip Theory is actually really simple if you hide all the complicated stuff in footnotes.

- The **attitude** of a piece is its current rotation compared to the solved[^solved-position] position.
- A **grip** is a region of space[^grip] you can[^turnable] turn.
- A **twist** consists of a grip and a rotation that keeps that grip fixed (the rotation "stabilizes" the grip).
- The **grip group** is the set[^group] of all the twist rotations[^rotations] and the rotations you can get by composing[^inverting] them (doing one and then the other).[^transformations] The grip group is the set of possible[^reachable] **attitudes** of a piece.
- A grip is **active** on a piece if the piece is currently affected by twists on that grip. Otherwise the grip is **inactive** on that piece. I call this the **status** of the grip.
- The **grip signature** of a piece is the status of each grip. In particular, the **current grip signature** of a piece is its grip signature in whatever state the puzzle is in right now. As a piece moves around, its current grip signature changes.
- In casual conversation, we say that a piece **has** a grip if that grip is active for the piece.
- The **solved grip signature** or **initial grip signature** of a piece is the grip signature it in its solved position.
- A **puzzle** is defined by a grip group (e.g., rotations of a cube), a set of axes that are permuted by a grip group (e.g., faces of a cube), and a set of pieces. Each piece is defined by its initial grip signature, which dictates how it moves around.
- A **puzzle state** is just an attitude for each piece.
- The current grip signature of each piece can be determined by transforming each member of its initial grip set by the current attitude of the piece.
- To apply a twist to a puzzle: take all the pieces that are active on that grip and update each piece's attitude by composing it with the twist rotation. In other words: rotate all the pieces on that grip.

[^solved-position]: This definition only works for super cubes, where all pieces and attitudes are distinguishable. It's possible to handle indistinguishable pieces/orientations by instead saying the attitude is the set of all indistinguishable rotations.
[^grip]: Actually a grip is just anything that can be permuted by elements from the grip group.
[^turnable]: Some grips might not actually be turnable because they are always blocked. In particular, jumbling puzzles have infinitely many grips but (usually) only finitely many of them can ever be twisted.
[^group]: Actually a [group](https://en.wikipedia.org/wiki/Group_(mathematics)).
[^rotations]: And reflections, sometimes.
[^inverting]: And inverting them.
[^transformations]: Actually the grip group doesn't have to consist of transformations of space. The important thing is just that the grip group permutes grips.
[^reachable]: Not all attitudes may be reachable, particularly in bandaged puzzles or if you've chosen a larger grip group than necessary (e.g., describing an FTO using octahedral symmetry instead of tetrahedral symmetry).

## Bonus round: bandaging

- Besides "active" and "inactive," a grip may be **blocked** on a piece. When a grip is blocked on any piece then that grip cannot be turned.

## Bonus round: fudging

- Just make up a permutation group for your grips. It doesn't have to match up with geometry.

## Bonus round: jumbling

- Oops, our twist rotations (or some composition of them) forms an irrational angle.
- Now our grip group has infinitely many rotations.
- Since rotations from the grip group must permute the grips, we need somewhere for the grips to go. That means we have infinitely many grips!
- Fortunately you don't actually have to specify the active/inactive/blocked status for every one of the infinitely many grips. In practice[^reasonable], almost all of them are always blocked so you can just pretend that those grips are blocked on every piece and you'll end up with an equivalent puzzle.

[^reasonable]: For any reasonable puzzle, anyway.

## Bonus round: lamination

Grip theory technically works for everything, but some puzzles have more structure. For these, we have **Laminated Theory**, which is more advanced. While Grip Theory and Laminated Theory are both capable of describing the same puzzles, sometimes they fit more nicley into one framework or the other.

- When grips have the same stabilizer (e.g., `R` and `L` on 3x3x3) then we can define them instead as distinct **layers** on an **axis**.
    - Even though we usually think of the 3x3x3 as having 3 layers, for Laminated Theory it's more useful to think of it as having 9 layers: `R`/`M`/`L`, `U`/`E`/`D`, `F`/`S`/`B`.
    - The layers of an axis must be disjoint and must fill all of space.
- Instead of permuting grips, the grip group permutes layers.
    - It must permute the layers in a way that can be reduced to permuting axes.[^block-system] In other words: if an element of the grip group takes a layer on axis `A` to a layer on axis `B`, then it must take _all_ layers of axis `A` to layers on axis `B`.
- Instead of having an active/inactive/blocked status on each grip, a grip signature has a set of active layers. (All other layers are inactive.)
- Instead of being defined as a rotation on a grip, a twist is defined as a rotation on a set of layers within one axis that stabilizes[^pointwise] those layers.
- A twist is **blocked** if there is any piece whose grip signature contains at least one layer (on the twist's axis) that _is_ affected by the twist _and_ at least one layer (on the twist's axis) that _is not_ affected by the twist.
- To apply a twist to a puzzle: take all the pieces that are active on any of the layers of the twist and update each piece's attitude by composing it with the twist rotation. In other words: rotate[^rotations][^transformations] all the pieces in those layers.

[^pointwise]: Pointwise-stabilizes, so each layer stays where it is.
[^block-system]: This is called a [block system](https://en.wikipedia.org/wiki/Block_(permutation_group_theory)).
