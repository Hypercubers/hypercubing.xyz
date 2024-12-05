# Notation

!!! warning
    This page explains notation specifically for cell-turning virtual hypercube puzzles. Notation pages for other puzzles coming soon™️...

## Cells

!!! info inline end "Yellow cell rotating"
    <video autoplay loop muted width="300">
    <source type="video/mp4" src="https://assets.hypercubing.xyz/vid/yellow_cell_rotating.mp4">
    </video>

Each side of an n^4^ hypercube is called a *cell*, and consists of a cubic grid of n^3^ stickers. Because each side is cubic, they can be rotated with cubic symmetry. A cube has 24 different possible orientations, meaning that each side of a 4D puzzle can be oriented in 24 different ways.

There are 8 cells, six of them using the same letters as that in the 3^3^: `U` (up), `D` (down), `F` (front), `B` (back), `R` (right), `L` (left). The one that you can see on the inside is called `I` (inside), and the one opposite of that (which is hidden) is called `O` (outside). This means we use the letters `R` `L` `U` `D` `F` `B` `O` `I`.

## Pieces

Cell-turning hypercubes have 4 different types of pieces (with some slight variations for big hypercubes). These are the 1c (1-colored) centers, 2c ridges, 3c edges, and 4c corners. You can label each piece based on which cells it is on. The 3c piece that has stickers on the `I`nside, `R`ight, and `U`p cells would be called the `IUR` piece.

## Twists

Twists are notated based on which piece you click on to do the turn, with the first letter determining which sticker of that piece to click on. For example:

- `RO'` means to left click the R cell sticker of the RO piece.
- `IUR` means to left click the I sticker of the IUR piece (edge twists are symmetrical, so it doesn't matter if you left or right click).
- `FRUI` means to right click the F sticker of the FRUI piece.

For the slice layers, we use `M` `E` `S` `P`, where P is the slice that follows `O` (although with notation for n^5^ puzzles beginning to be fleshed out, P may end up being used by the new 5D sides of Posterior/Anterior). Wide moves are tricky, as we are now using the letter `w` for the 4th dimension axis. One way to get around this is to write the numbers you hold down on the keyboard (in MC4D/MPU etc) while clicking on a piece. On a 3-layered puzzle, holding down 2 does a slice move, and holding down 1 and 2 will do a wide move.

- `{2}RO` means to hold <kbd>2</kbd> while doing an RO move (essentially an M move).
- `{2-3}UO'` means to hold <kbd>2</kbd> and <kbd>3</kbd> while doing a UO' move.
- `{2-4}IF` means to hold <kbd>2</kbd>, <kbd>3</kbd>, and <kbd>4</kbd>

### Commutators

Many algorithms are constructed using commutators and conjugates, so there is a compact notation for them using square brackets. See [Commutators - Notation](/techniques/commutators#notation).

## Algorithms

A shorter notation was developed to write specific algorithms, such as RKT cancels. All letters besides `I` and `O` correspond to their -O variants. `R U R' U'` would mean `RO UO RO' UO'`. For the wide O cell flips, they are notated with 3D rotations, such as `{1-2}Oxz2`. Using 3D rotations in this way is totally arbitrary, and its only purpose is for execution.

## Rotations

3D notation for rotations doesn't really generalize to higher dimensions. For example, we call an `x` rotation x because it rotates the puzzle "around the x-axis". However, this is unhelpful because rotations don't actually happen around an axis. Instead it's better to think of rotations as happening within a 2D plane. When you're doing an `x`, the whole puzzle is really being rotated within the zy plane. And writing rotations like this generalizes to higher dimensions, so that is what we use.

First, we make a certain side from each axis be the "positive" side. There are standards for this in 3D (such as the [right-handed rule](https://en.wikipedia.org/wiki/Right-hand_rule)). On the x-axis, going to the right is positive and going left is negative. This makes `R` the positive side from the x-axis. The same goes for the other axes: `U`, and `F` are the positive sides in 3D. In 4D we add two new sides, and have to decide which one is positive and which one is negative. Because of the projection, the side that we can't see is closer to the 4D camera, making `O` the positive w-axis cell, and `I` the negative.

To actually notate the rotations, write the letters of the 2 axes that form the plane that the puzzle is rotating in, in the order of which positive side on that axis goes to the positive side of the other axis. For example: rotating the positive y-axis side to the positive x-axis side (rotating U to R) would be written `yx` (and looks like `z` in 3D notation).

- `yw`: bring +y to +w (rotate U to O)
- `xz`: bring +x to +z (rotate R to F (this is called `y` in 3D rotation notation))

Note how we don't have to use the `'` prime symbol because you can just swap the letters (wy is the inverse of yw). You can also add a `2` to the end for double rotations, e.g. `wx2`, `yz2` etc.

This makes it a really nice system because it only ever uses 2 letters, no matter how many dimensions. You can also use it on n^3^ puzzles in order for more multi-dimensional consistency: `xy` means move x+ to y+ (R to U \[z' rotation]).

## Turn metrics

There are many different ways to count the number of twists performed during a solve. All of these metrics (besides ETM) have their own Quarter Turn counterparts, where twists are broken up into 90° twists. For example, a 180° face twist takes two 90° twists, while a 120° edge twist takes three. Listed below are the metrics used by HSC. STM is used the most, but others are sometimes relevant.

??? info "ATM"
    - Consecutive twists of the same axis are combined, even with different layers.
    - Whole-puzzle rotations are not counted.

??? info "ETM"
    - Twists are counted as they are executed, including whole-puzzle rotations.

??? info "STM"
    - Whole-puzzle rotations are not counted.
    - Slice twists count as one move.
    - Consecutive twists of the same axis and layers are combined.

??? info "BTM"
    - Whole-puzzle rotations are not counted.
    - Noncontiguous slice twists are split into contiguous slice twists.
    - Consecutive twists of the same axis and layers are combined.

??? info "OBTM"
    - Whole-puzzle rotations are not counted.
    - Slice twists are split into contiguous outer-block twists.
    - Consecutive twists of the same axis and layers are combined.

??? info "MC4DTM"
    a.k.a. "whatever MC4D says"

    - Twists are counted as they are executed.
    - Whole-puzzle rotations counted only if they are executed as moves.
    - Double rotations and certain reorientations are impossible to execute as one move.
    - Any move that counts as 1 STM is possible with 1 or 2 MC4DTM moves.[^2ct]

[^2ct]: This is due to the 2-click theorem.^\[citation needed]^
