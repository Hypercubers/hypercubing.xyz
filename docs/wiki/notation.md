# Notation

This is notation specifically for n$^4$ virtual puzzles. Notation pages for other puzzles coming soon™️...

## Cells
!!! info inline "Yellow cell rotating"
    <video autoplay loop muted width="300">
    <source type="video/mp4" src="/assets/images/yellowcellrotating.mp4">
    </video>
The sides of a 4D puzzle are called `cells`, each of which is a cubic grid of n$^3$ stickers. Because each side is cubic, they can be rotated with cubic symmetry. A cube has 24 different possible orientations, meaning that each side of a 4D puzzle can be oriented in 24 different ways.




The cells are notated: Right, Left, Up, Down, Front, Back, Outside, Inside.

This means we to use the letters `R` `L` `U` `D` `F` `B` `O` `I`.

For the slice layers, we use `M` `E` `S` `P`, where P is the slice parallel to I/O.

## Pieces
Each piece of the puzzle can be labeled based on which cells it is on. The 3c piece that has stickers on the `I`nside, `R`ight, and `U`p cells would be called the `IUR` piece.

## Moves
The moves are notated based on which piece you click to do the turn in MC4D.
The first letter determines the cell to click on. The second letter determines the sticker on the cell (usually a 2c piece) to click on. For example:

- `RO'` means to left click the R cell sticker of the RO piece.
- `IUR` means to click the I sticker of the IUR piece.
- `FRUI` means to right click the F sticker of the FRUI piece.

For slice and wide moves, you write the numbers you hold down on the keyboard while clicking. 

- `[2]RO` Means to hold down 2 on the keyboard while doing an RO move (essentially an M move).
- `[23]UO'` Means to hold down 2 and 3 on the keyboard while doing a UO' move.

## Rotations

4D rotations work by using the positive sides of each axis (Up, Right, Front, and Outside). You can generalize this to any dimension as long as you always define which side is positive relative to the others.

- `yw`: bring y+ to w+ (rotate U to O)

Note how we don't have to use ' prime symbols because wy is the inverse of yw. This makes it a really nice system because it only ever uses 2 letters. You can also use it on the 3<sup>3</sup>: `xy` means move x+ to y+ (R to U [z rotation]).

In reality though, it's easiest to just say use `x`, `y`, and `z` for rotations that don't change the cells on the W axis. For other ones you can just say `recenter (cell)`. 

## Turn metrics

There are many different ways to count the number of moves. Listed below are the metrics used by HSC.

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

All of these metrics (besides ETM) have their own Quarter Turn counterparts, where 180° twists are counted as two 90° twists.
