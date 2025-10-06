# Glossary

This is a glossary of terms used in the hypercubing community. We take a mostly prescriptivist[^1] approach: terminology has a great effect on how we think about puzzles, and we try to be mindful when naming concepts and inventing notation to ensure that they encourage better understanding of puzzles and are useful in as many contexts as possible.

[^1]: Go ahead, run us over with the [descriptivist bus](https://www.youtube.com/watch?v=46ehrFk-gLk&t=200s).

!!! warning "Before you propose new terminology ..."
    We've wrestled in the past with poor terminology that actively hurt understanding. First, gain hands-on experience and intuition for the thing you want to describe, and _then_ see what terms are actually needed. There's no value in making up words for the pieces on a 7-dimensional puzzle, for example, if there's no need to communicate about them.

## Puzzle elements

A 1-dimensional turning axis is not always well-defined for higher-dimensional puzzles, because rotations generally happen in a plane, not around an axis.

### Polytope elements

For an $N$-dimensional polytope:
(Some of these terms are from [Polytope - Wikipedia](https://en.m.wikipedia.org/wiki/Polytope#Elements))

- **vertex** = rank 0, single point
- **edge** = rank 1, line connecting two vertices
- **face** = rank 2, polygon constructed from edges
- **cell** = rank 3, polyhedron constructed from faces
- ...
- **$N$-face** = rank $N$, polytope constructed from rank $N-1$ elements
- **peak** = $N-3$ face
- **ridge** = $N-2$ face
- **facet** = rank $N-1$, polytope constructed from rank $N-2$ elements

In 4D, we prefer **facet** rather than **cell**. In simple terms: on most puzzles, a **facet** is the thing with a single color.

### Pieces

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

## Puzzle state

- A puzzle's **state graph** is the [graph](https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)) of all its states. Each state of the puzzle has a node, and the nodes are connected by single moves.
- A piece's **attitude** is the transformation from its solved state to its current state. For example, each piece on 3×3×3 has 24 possible attitudes.
- A piece's attitude can be decomposed into its **permutation**, the component that affects its grip signature, and its **orientation**, the component that does not. For example, each corner on a 3×3×3 has 8 permutations and 3 orientations.
- Pieces are **indistinguishable** if swapping them never affects whether the puzzle is solved. For example, the blue center pieces on a standard 4×4×4 are all indistinguishable.
- Pieces are **distinguishable** if swapping them can affect whether the puzzle is solved.
- Piece orientations are **indistinguishable** if changing one orientation to the other never affects whether the puzzle is solved. For example, each center on a standard 3×3×3 has 4 orientations, all of which are indistinguishable.
- Piece orientations are **distinguishable** if changing one orientation to the other can affect whether the puzzle is solved.

Revealing information that distinguishes indistinguishable pieces or orientations makes them no longer distinguishable, thus changes the puzzle.

## Puzzle properties

### Algebraic properties

- A move is **blocked** in a particular puzzle state if there is some feature of the puzzle preventing the move from being applied. Generally this is because there is a piece that is partially inside and partially outside of the region affected by the move.
- **Bandaging** is the process of combining pieces in order to block moves.
- **Unbandaging** is the process of splitting pieces in order to make more moves possible.
- A puzzle is **doctrinaire** or **fully unbandaged** if every move is always accessible.
- A puzzle is **bandaged** if it is not doctrinaire, but can be finitely unbandaged to a doctrinaire puzzle.
- A puzzle is **jumbling** if it has infinitely many [grips](/theory/grip-theory.md). For finite puzzles, this simpler definition is equivalent: A puzzle is **jumbling** if it cannot be finitely unbandaged to a doctrinaire puzzle.

### Visual modifications

- A **sticker mod** of a puzzle is a modification that involves changing the coloring of a puzzle. A sticker mod may have different indistinguishable pieces than the original puzzle.
- A **shape mod** of a puzzle is a modification that involves changing the shape of the puzzle without changing the behavior of pieces. A shape mod may have different indistinguishable pieces than the original puzzle. A shape mod sometimes requires modifying the coloring as well.
- A puzzle is **shapeshifting** if the visible shape of the puzzle depends on its state.

Note that shapeshifting has nothing to do with algebraic properties (doctrinaire/bandaging/jumbling).

- Any puzzle can be made shapeshifting by changing the shape of one of the pieces.
- Any single-core twisty puzzle can be made non-shapeshifting by carving it from a sphere.

### Constructions

- A **solid** is a construction of a puzzle by cutting a finite polytope, possibly with some pieces removed.
- A **tiling** is a construction of a puzzle by cutting a filled space, typically with no pieces removed.
- A **soup** is a construction of a puzzle by adding objects to an initially empty space.

### Physicality

These definitions are bespoke to the hypercubing community, and have been refined over time as we discover more strange cases. Unlike most other terms on this page, these do not have rigid definitions; they may change as more possibilities are discovered.

The exact assignment of "physical" and "mechanical" is a historical quirk inherited from Melinda's "physical" 2^4^.

- The **geometric rank** of a puzzle is the rank of its geometry; that is, the dimension of its stickers/facets plus one. Examples:
    - The Rubik's cube has rank 3.
    - 3^4^ has rank 4.
    - MagicTile puzzles all have rank 3.
    - Circle puzzles have rank 3.
    - Loopover has rank 3.
    - Reflesquare has rank 2.
- A **virtual** puzzle is one simulated on a computer. In hypercubing, this is the closest we can get to the true form of the puzzle.
- A **mechanical** puzzle is one that uses a physical mechanism in a number of dimensions that is the geometric rank of the puzzle, typically using geometric constraints to hold pieces together. For example, a mechanical 3^4^ uses 4 dimensions. A mechanical circle puzzle uses 3 dimensions. The typical Rubik's cube is a mechanical 3^3^.
    - A mechanical puzzle may exist in geometry other than 3D Euclidian space; one may talk about a mechanical face-turning Klein Quartic puzzle in quotiented H3 or H2xE space.
- A **physical** puzzle is one that is built in a dimension lower than its geometric rank, typically ([but not always](https://www.youtube.com/watch?v=C_Wq42L-12M)) using rigid pieces. For example, Melinda's physical 2^4^ uses 3D space. A physical 2^5^ may use 3D or 4D space. A physical 3^3^ uses 2D space. All known physical higher-dimensional puzzles are [documented in this wiki](/puzzles/physical).
    - A physical puzzle must have the same state space and allowed moves as the original, although some moves may take multiple steps to achieve.
- A move is **accessible** on a physical puzzle if it can be performed in one or very few actions.
    - A good physical puzzle has many accessible moves.
- A **gyro** is a multi-step action on a physical puzzle that changes the accessible moves. Gyros often correspond to higher-dimensional rotations.
- A **half gyro** or **partial gyro** is a multi-step action on a physical puzzle that performs an inaccessible move.
- A **virtual physical** ("virt phys") puzzle is a computer simulation of a physical puzzle.

### Completions

- A **real** puzzle is one with all interior pieces. For example, a real 7×7×7 has $7^3=343$ pieces, compared to $7^3-5^3=218$ pieces for a standard 7×7×7.
- A **complex** puzzle is one with a piece for each possible grip signature using the [grip-theoretic construction](/theory/grip-theory.md). These puzzles have $2^n$ pieces, where $n$ is the number of grips on the puzzle.
- A **laminated** puzzle is one with a piece for each possible grip signature using a [laminated construction](/theory/grip-theory.md). A laminated puzzle is a subset of the complex puzzle.
- A **multi** puzzle is one with pieces from several different cut depths. An example is the [Multidodecahedron](https://twistypuzzles.com/app/museum/museum_showitem.php?pkey=2384). A multi puzzle is a subset of the laminated puzzle.
- A **circle** puzzle is one with circles carved into the faces, where pieces inside one or more of the circles do not turn with their face. A circle where all circles behave equivalently is a subset of the complex puzzle. For example, see this [video of a circle 3×3×3](https://www.youtube.com/watch?v=hUX91tXNyeE&t=55s).
- A **super** puzzle is one where all orientations are distinguishable.

Real, complex, and laminated puzzles are often implicitly super. For example, the super real 5×5×5 has 125 pieces, all distinguishable (and with all distinguishable attitudes). It is equivalent to the [Double Circle Real 5×5×5](https://twistypuzzles.com/app/museum/museum_showitem.php?pkey=4823) ([video](https://www.youtube.com/watch?v=WRFNPoAimbM)).

### Cut depths

Cut depth terminology varies by community. Listed here are the definitions we use in hypercubing.

- A **shallow** cut is any cut equivalent to the shallowest possible cut. An example is the [Megaminx](https://twistypuzzles.com/app/museum/museum_showitem.php?pkey=650).
- A **deep** cut is any cut deeper than a shallow cut.
- A **half** cut is a cut that passes through the center of the puzzle into two identical halves. An example is the [Pentultimate](https://twistypuzzles.com/app/museum/museum_showitem.php?pkey=1741).
- A **to-adjacent** cut is a cut that passes through the center of an adjacent face. An example is the [Pyraminx Crystal](https://twistypuzzles.com/app/museum/museum_showitem.php?pkey=652). A to-adjacent cut is exactly the depth required to not have axis pieces (pieces that turn with exactly one grip).
- A **deeper-than-adjacent** cut is any cut deeper than a to-adjacent cut. An example is the [Curvy Starminx](https://twistypuzzles.com/app/museum/museum_showitem.php?pkey=4344) or [Litestarminx](https://twistypuzzles.com/app/museum/museum_showitem.php?pkey=11394).
- A **deeper-than-origin** cut is any cut deeper than a half cut. An example is [Deeper Madness](https://twistypuzzles.com/app/museum/museum_showitem.php?pkey=4007), especially [compared to Shallower Madness](https://youtu.be/YiKXHgn_5Yo). Another example is the [Enabler Cube](https://www.youtube.com/watch?v=n4uppWjWDlo).

### Other cut types

- A cut is **accessible** if there is some move that separates pieces along it.
- A **stored** cut is one that is not accessible from the solved state of the puzzle. For example, the extra cuts present on a [Curvy Copter Plus](https://twistypuzzles.com/app/museum/museum_showitem.php?pkey=1687) are stored cuts; compare to the [Curvy Copter](https://twistypuzzles.com/app/museum/museum_showitem.php?pkey=1574), which has no stored cuts.
- A **wedge cut** is a cut comprised of multiple cut planes, where twists are parallel to both planes. This is only possible in 4D+. An example is the wedge-turning 3^4^.

## Solving

### Actions

An **action** is sequence of moves that preserves invariants of the stage. Usually, an action keeps certain pieces solved. For example, when a 4^n^ has been reduced to a 3^n^ using [big cube reduction](/methods/big-cube-reduction.md), outer layer moves are the only actions. In this case, the actions are **reduced** moves. Another common set of actions is [RKT](/techniques/rkt.md).

### Parity

There is no community consensus on the definitions of **parity**. Below are some proposed definitions:

- **group theory parity** = a case where the puzzle is in an unexpected [coset](https://en.wikipedia.org/wiki/Coset) of a subgroup of index 2
    - It is often more broadly applied to a case where the puzzle is in an unexpected coset of a subgroup of any index.
- **cuber parity** = a case that is difficult to solve that the solver didn't expect
    - Melinda's definition: a local maximum, where the puzzle is largely solved but requires many moves to fix
    - Hactar's definition: a case which cannot be solved using the [actions](#actions) expected at this stage in the solve

None of these definitions are satisfactory. According to most of these definitions, [RKT parity](/techniques/rkt.md#parity) is not parity at all, but is more accurately called "RKT error." According to Melinda's definition, most [PLL](https://www.speedsolving.com/wiki/index.php/PLL) cases are parity. The first definition given for "cuber parity" is highly subjective, but is the only one that captures its current use.

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

### Methods in higher dimensions

In higher and higher dimensions, it gets annoying to have to say stuff like "permuting the last cell of the last cell of the..." etc. To avoid the verbosity, we simply add a hyphen and the rank of the thing you're solving at the end. Examples:

- PLL-4 is the PLL step on a rank-4 object, which permutes a rank-3 object. With CFOP on 3^4^, it consists of permuting the 2c pieces, then permuting the rest like a 3^3^.
- For F2L, you put the number before the letter at the end e.g. F2L-5a, F2L-6d, etc.
- If you were solving a 3^6^ with pure CFOP and you were solving the F2L of the final cube with triple RKT, that would be F2L-3 of PLL-4 of PLL-5 of PLL-6.

## To-do

!!! warning "This section is a work-in-progress."

- Sliding vs. twisting
- Cuboid terms (tower, brick, floppy, domino, pancake)
- Other common puzzle families: weirdling, bubbloid, rotate-gap, sliding-gap (15-puzzle), loopover
