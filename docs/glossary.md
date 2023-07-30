# Glossary

This is a glossary of terms used in the hypercubing community. We take a mostly prescriptivist[^1] approach: terminology has a great effect on how we think about puzzles, and we try to be mindful when naming concepts and inventing notation to ensure that they encourage better understanding of puzzles and are useful in as many contexts as possible.

[^1]: Go ahead, run us over with the [descriptivist bus](https://www.youtube.com/watch?v=46ehrFk-gLk&t=200s).

!!! warning "Before you propose new terminology ..."
    We've wrestled in the past with poor terminology that actively hurt understanding. First, gain hands-on experience and intuition for the thing you want to describe, and _then_ see what terms are actually needed. There's no value in making up words for the pieces on a 7-dimensional puzzle, for example, if there's no need to communicate about them.

## Puzzle elements

A 1-dimensional turning axis is not always well-defined for higher-dimensional puzzles, because rotations generally happen in a plane, not around an axis.

### Polytope elements

For an $N$-dimensional polytope:

- **vertex** = rank 0, single point
- **edge** = rank 1, line connecting two vertices
- **face** = rank 2, polygon constructed from edges
- **cell** = rank 3, polyhedron constructed from faces
- ...
- **$n$-face** = rank $n$, polytope constructed from rank $n-1$ elements
- ...
- **facet** = rank $N-1$, polytope constructed from rank $N-2$ elements

In 4D, we prefer **facet** rather than **cell**. In simple terms: on most puzzles, a **facet** is the thing with a single color.

### Pieces

Some of these terms are from [Polytope - Wikipedia](https://en.m.wikipedia.org/wiki/Polytope#Elements).

Basic definitions for an $N$-dimensional hypercubic puzzle:

- **corner** = piece with $N$ colors (4 colors in 4D)
- **edge** = piece with $N-1$ colors (3 colors in 4D)
- **peak** or **3c** = piece with 3 colors (5D+)
- **ridge** or **2c** = piece with 2 colors (4D+)
- **center** or **1c** = piece with 1 color

We prefer words rather than 1c, 2c, etc. because the words generalize better to other, non-facet-turning puzzles and describe how a piece _behaves_ rather than how it _looks_.

### Moves

- **axis** or **turning axis** = ray start from the center of the puzzle, around which puzzle elements rotate during twists
- **twist** or **move** or **turn** = movement of pieces that changes the puzzle state
- **rotation** or **full-puzzle rotation** = rotation of the whole puzzle that does not change its state

## Solving

### Actions

An **action** is sequence of moves that preserves invariants of the stage. Usually, an action keeps certain pieces solved. For example, when a 4^n^ has been reduced to a 3^n^ using [big cube reduction](/methods/big-cube-reduction), outer layer moves are the only actions. In this case, the actions are **reduced** moves. Another common set of actions is [RKT](/techniques/rkt).

### Parity

There is no community consensus on the definitions of **parity**. Below are some proposed definitions:

- **group theory parity** = a case where the puzzle is in an unexpected [coset](https://en.wikipedia.org/wiki/Coset)
- **cuber parity** = a case that is difficult to solve that the solver didn't expect
    - Melinda's definition: a local maximum, where the puzzle is largely solved but requires many moves to fix
    - Hactar's definition: a case which cannot be solved using the [actions](#actions) expected at this stage in the solve

None of these definitions are satisfactory. According to most of these definitions, [RKT parity](/techniques/rkt#parity) is not parity at all, but is more accurately called "RKT error." According to Melinda's definition, most [PLL](https://www.speedsolving.com/wiki/index.php/PLL) cases are parity. The first definition given for "cuber parity" is highly subjective, but is the only one that captures its current use.

!!! question "Open questions"
    - Is there a definition for "cuber parity" that captures the way it's naturally used?
    - Is there a catchy term we can use instead of "RKT parity"? Melinda proposes "RKT error."

### F2L

**F2L** is a very general solving strategy that works by building a small block of pieces and then inserting the block into its solved position. F2L stands for "first two layers" because it was originally developed to solve the first two layers of 3^3^, but in hypercubing we use it for many other puzzles.

#### F2L axes

- **free** axes = axes which affect only unsolved pieces; can be turned freely
- **side** axes = axes which affect some unsolved pieces and some solved pieces; can be turned, but must be turned back to restore solved pieces
- **base** axes = non-free and non-side axis that is not completely solved; usually mostly solved, rarely turned during F2L
- **top** axis = the free axis currently being worked on

!!! example "Examples"
    - In F2L on a 3^3^, `D` is the only base axis, `U` is the top axis (the only free axis), and `R`, `L`, `F`, & `B` are all side axes.
    - When beginning F2L on a megaminx there are, 6 free axes, 5 side axes, and 1 base axis.
    - Near the end of F2L on a megaminx there are, 1 free axis, 5 side axes, and 5 base axes.

We use the letter `T` to represent the top axis, `R` & `F` to represent intersecting side axes, and `R` & `L` to represent non-intersecting side axes.

#### F2L blocks

An **F2L block** or **pair** is a group of pieces that is **paired** and solved as one unit. There's usually a **head** and **body**, where the head intersects with more twisting axes than the body.

The **base sticker** of a head is the sticker which will be facing the base axis when it is solved. The **facing** direction of the head of a block is whatever direction its base sticker is facing. The facing direction of the body of a block is the same as the head, when they are paired. This notion of which direction a head or body faces gives a way to describe edge orientation before the pieces have been paired, which is helpful especially in 4D+ where edge orientation is otherwise difficult to define.

!!! example "Examples"
    - On the 3^3^ an F2L pair consists of a corner (the head) and an edge (the body).
    - On the 3^4^, an F2L-a pair consists of an edge (the head) and a ridge (the body).

- **paired** = fully assembled
- **split pair** = one move away from paired, or can be paired as part of inserting the block

#### F2L action terminology

- **breaking the base** = unsolving some pieces that were solved
- **restoring the base** = re-solving some pieces
- **push** = a twist of a side axis that breaks the base and puts new pieces on top
- **pull** = a twist of a side axis that restores the base and puts new pieces on top
- **overpush** = push again after pushing (e.g., R U **R** U R2')
- **overpull** = push as a continuation of a pull (e.g., R U **R2'** U' R)
- **push pair** = formation of a pair via a push
- **pull pair** = formation of a pair via a pull
- **hide** = to remove a piece from the top (using a push or pull)
- **reveal** = to bring a piece to the top (using a push or pull)
- **rebase** or **reorient** = to reorient a piece to face a different direction (i.e., change where its base sticker is facing)
- **cap** = to twist `T` to form a pair (where the head is on top and the body is not on the top)
- **uncap** = to separate the head and body of a pair by twisting `T`

!!! question "Open question"
    What should we call a move like `RT` on 3^4^, which doesn't change the set of pieces on `T` and might or might not unsolve some pieces?

## Puzzle descriptors

!!! warning "This section is a work-in-progress."

- Solid vs. tiling vs. soup
- Doctrinaire
- Reduced
- Bandaged
- Unbandaged
- Shapeshifting
- Sliding vs. twisting
- Circle
- Super
- Real
- Complex
- Stickermod
- Shapemod
- Cuboid terms (tower, brick, floppy, domino, pancake)
- Other common puzzle families: weirdling, bubbloid, rotate-gap, sliding-gap (15-puzzle), loopover

### Cut depth

!!! warning "This section is a work-in-progress."

- Shallow cut
- Half cut
- Deep cut
    - Deeper than adjacent
    - Deeper than origin
- Semideep cut?
