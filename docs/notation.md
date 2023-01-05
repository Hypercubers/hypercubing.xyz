# Notation

(work in progress)

## Cells
Each side of an n<sup>d</sup> is called a ```cell```. On 4-dimensional puzzles, each cell can be rotated with the symmetry of a cube. A cube has 24 different orientations, so each cell can be oriented in 24 different ways.
<iframe width="250" height="380" style="width: 250px; height: 380px; overflow: hidden;" src="https://ruwix.com/widget/3d/?label=Cell%20Rotating&alg=x2%20y2%20z2&hover=2&flags=showalg&colors=U:y%20R:y%20F:y%20D:y%20L:y%20B:y" scrolling="no"></iframe>
The cells are notated:

- `R`: Right
- `L`: Left
- `U`: Up
- `D`: Down
- `F`: Front
- `B`: Back
- `O`: Outside
- `I`: Inside

And the 4 slice layers:

- `M`: Middle slice (parallel to R/L)
- `E`: Equatorial slice (parallel to U/D)
- `S`: Standing slice (parallel to F/B)
- `P`: Planetary slice (parallel to I/O)

## Pieces
Each piece of the puzzle can be labeled based on which cells it is on. The 3c piece that has stickers on the Inside, Right, and Up cells would be called the IUR/IRU/RUI/RIU/UIR/URI piece (the order doesn't matter when referring to the piece as a whole). You can also adapt [NBRS notation](https://sites.google.com/site/athefre/nbrs) to refrence groups or blocks of pieces.

## Moves
This notation was originally invented for the mouse controls used in MC4D, but we use it for all programs now.
The first letter determines the cell to click on. The second letter determines the sticker on the cell (usually a 2c piece) to click on. For example:

- `RO'` means to left click the R cell sticker of the RO piece.
- `IUR` means to click the I sticker of the IUR piece.
- `FRUI` means to right click the F sticker of the FRUI piece.

For slice and wide moves, you write the numbers you hold down on the keyboard while clicking. 

- `[2]RO` Means to hold down 2 on the keyboard while doing an RO move (essentially an M move).
- `[23]UO'` Means to hold down 2 and 3 on the keyboard while doing a UO' move.

Once you know how the notation works with the mouse, then you know what moves to say when you're doing it with a keyboard.

## Rotations

4D rotations work by using the positive sides of each axis (Up, Right, Front, and Outside). You can generalize this to any dimension as long as you always define which side is positive relative to the others.

- `yw`: bring y+ to w+ (rotate U to O)

Note how we don't have to use ' prime symbols because wy is the inverse of yw. This makes it a really nice system because it only ever uses 2 letters. You can also use it on the 3<sup>3</sup>: `xy` means move x+ to y+ (R to U [z rotation]).

In reality though, it's easiest to just say use `x`, `y`, and `z` for rotations that don't change the cells on the W axis. For other ones you can just say `recenter (cell)`. 

## Turn metrics
