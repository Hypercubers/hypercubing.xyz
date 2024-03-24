# 4D Skewb

There are many puzzles that could be called a '4D skewb'. Each one has some characteristics similar to the skewb. By constructing the skewb in a certain way, and replacing 3D objects of the definition with similar 4D objects, you can construct a 4D puzzle that has some things in common with the skewb.

## Cube-like

### Vertex turning hypercube

!!! example inline end "Vertex turning hypercube"
    ![Vertex turning hypercube](https://cloud.hypercubing.xyz/assets/img/virt/4d_skewb/vertex_turning.png)

The skewb is a vertex-turning cube with the cuts passing through the origin. If you replace the 3D cube in the definition with the 4D hypercube, you get the half-cut vertex-turning hypercube. This puzzle has 32 edge pieces, 64 Y-centers, and 8 center pieces. Both the Y-centers and the centers are 1c pieces. 

In three dimensions, a plane perpendicular to the vertex axis passes through 1 corner, then 3, then 3, then 1 corner. This causes a plane passing through the origin to go between the two layers of 3 corners, which is why the skewb has corners. In four dimensions, a hyperplane perpendicular to the vertex axis passes through 1, 4, 6, 4, then 1 corner. Therefore, a hyperplane passing through the origin passes directly through 6 vertices, and there are no corner pieces on this 4D puzzle. Similarly, the pattern of cuts on one cell of the puzzle looks like a dino cube, not a skewb.

### Skewb lookalike

!!! example inline end "Skewb lookalike"
    ![Skewb lookalike](https://cloud.hypercubing.xyz/assets/img/virt/4d_skewb/skewb_lookalike.png)

You can place a cut to pass between the layers of 4 and 6 corners. If you do this, you get two cuts per axis and three layers per axis. This puzzle has 16 vertex pieces, 64 Y-centers, and 24 ridge pieces. Like the skewb, the vertex pieces are separated into two orbits, but this puzzle has a middle layer on each axis. The cut pattern on the cells of this puzzle resembles a 3D skewb with additional trivial tips. 

By rectifying the hypercube, the trivial tip cuts on the cut patterns of the cells are removed, meaning the cells look like cuboctahedral skewbs.

### Demi vertex turning hypercube

!!! example inline end "Demi vertex turning hypercube"
    ![Demi vertex turning hypercube](https://cloud.hypercubing.xyz/assets/img/virt/4d_skewb/demi_vertex_turning.png)

On the cube, the vertices can be separated into two tetrahedral subsets (the orbits of the skewb's corners). Each cut corresponds to one corner in the tetrahedron. On the hypercube, a similar partitioning of the vertices results in two sets of 8, each at the vertices of the 16-cell, or dually, the facets of a differently-oriented hypercube. If you only cut along vertex axes corresponding to these cuts, you will get a puzzle with only 4 cuts, half as many as the vertex turning hypercube. This puzzle has 8 corners and 8 centers. Unlike on the skewb, only half of the vertices of the hypercube have a corner piece, and all the corner pieces are in one orbit.

### Demi skewb lookalike

!!! example inline end "Demi skewb lookalike"
    ![Demi skewb lookalike](https://cloud.hypercubing.xyz/assets/img/virt/4d_skewb/demi_skewb_lookalike.png)

If you only use the axes along half the vertices as above, but you use the cut depths of the skewb lookalike, it results in a puzzle that still has three layers per axis, but only half as many axes. The cut pattern on the cells of this puzzle also resembles a 3D skewb, but with only 4 trivial tips per cell. The puzzle has 8 corner pieces, 8 dual corner pieces of a different shape, 32 Y-centers, and 24 ridge pieces.

As before, the hypercube can be rectified, which removes the trivial tips from the cut patterns of the cells.

<br>

??? info "Extra turns"
    In the two demi puzzles, the 8 vertices are arranged like the cells of a hypercube. This means they are actually shapemods of hypercubic puzzles. As such, they have an additional shapeshifting move in which you turn one layer by 90°. There is no analogous move on the skewb. In particular, the demi vertex turning hypercube is a shapemod of a [2x2x2x2](/puzzles/2x2x2x2), and the demi skewb lookalike is a shapemod of a [3x3x3x3](/puzzles/3x3x3x3), but with the 8 corner pieces that would be at the center of the cells missing.

    Because the 16-cell axis system, or the vertex turning hypercube system, is composed of two disjoint hypercube axis systems, these puzzles also have additional shapeshifting moves in which you turn a layer 90°. Unlike those in the previous section, though, performing one of these turns would bandage the puzzle. If you unbandaged these puzzles, you would get additional cuts parallel to the cells, resulting in the axis system of a 24-cell.

## Simplex-like

The skewb can be constructed in a different way: take four axes corresponding to a tetrahedron, and cut perpendicular to each axis through the origin. The tetrahedron is the 3D simplex, so if you replace it with the 5-cell, the 4D simplex, you get a new puzzle in 4D. This puzzle has several types of pieces, but since the shape of the puzzle does not yet exist, we can't name them after their position. Thus, we will name the pieces by how many layers they are turned by. For the skewb, there are 4 pieces that are in one layer, 6 pieces that are in two layers, and 4 pieces that are in three layers. We will call these 1g, 2g, and 3g pieces. This 4D puzzle will have 5 1g pieces, 10 2g pieces, 10 3g pieces, and 5 4g pieces. The skewb has a symmetry (90° rotation of the puzzle) that swaps 1g and 3g pieces and sends 2g to 2g pieces, and like it, this 4D puzzle has a symmetry that swaps 1g and 4g pieces and swaps 2g and 3g pieces. Like the skewb, the cuts on this puzzle can each be offset in a consistent direction while preserving the functionality of the puzzle.

Constructing the skewb like this, we can describe how to construct its cubic shape. On each face of the cube, there is one 2g piece in its center. Thus, given our abstractly constructed skewb, we can construct a plane perpendicular to each 2g piece's axis of symmetry. The shape bounded by all 6 of these planes is a cube.

### 2g carved simplex

!!! example inline end "2g carved simplex"
    ![2g carved simplex](https://cloud.hypercubing.xyz/assets/img/virt/4d_skewb/2g_carved.png)

Like in 3D, you can put a hyperplane perpendicular to the symmetry axis of each 2g piece. Since there are 10 2g pieces, this creates a polychoron with 10 triangular-bipyramidal cells called the [joined 5-cell](https://polytope.miraheze.org/wiki/Joined_pentachoron). On this puzzle, the 1g pieces are 4c at the tetrahedral vertices, the 2g pieces are 1c at the cell centers, the 3g pieces are 3c at the triangular edges, and the 4g pieces are 6c at the triangular-bipyramidal vertices. Unlike on the skewb, where the 1g and 3g pieces look alike, here, the 1g and 4g pieces are distinguishable by their number of colors, and so are the 2g and 3g pieces.

### 2g-3g carved simplex

!!! example inline end "2g-3g carved simplex"
    ![2g-3g carved simplex](https://cloud.hypercubing.xyz/assets/img/virt/4d_skewb/2g_3g_carved.png)

You can also put hyperplanes perpendicular to the symmetry axis of both the 2g and 3g pieces. This gives the puzzle a 20-celled shape called the [bijungato-10-cell](https://polytope.miraheze.org/wiki/Bijungatodecachoron). On this puzzle, the 1g and 4g pieces are both 4c at tetrahedral vertices, and the 2g and 3g pieces are both 1c at the cell centers. Unlike the previous shape but like the skewb, full symmetry of the puzzle is reflected in the shape.

Each cell of the puzzle either has two 1g and one 2g pieces, or two 4g and one 3g pieces. These two orbits of cells are only adjacent across the 2g-3g boundary. Because of this, this puzzle has multiple solved states, where each cell is a solid color, but the color schemes of the two orbits are rotated relative to each other.

### 2g-3g carved simplex, hemi colors

The puzzle can be recolored with 10 colors by giving opposite cells the same color. By asserting that the solved state has to have the two same-colored cells opposite to each other, it restricts the relative orientations of the two orbits to only one configuration, leading to there being only one solved state. Because of the geometry of the puzzle, a 1g-2g cell is opposite a 4g-3g cell, so the pieces on these cells are not swappable and coloring these two cells the same color leads to no ambiguity in the position.


### 2g-3g ridge carved simplex

!!! example inline end "2g-3g ridge carved simplex"
    ![2g-3g ridge carved simplex](https://cloud.hypercubing.xyz/assets/img/virt/4d_skewb/ridge_carved.png)

There are 30 square ridges between the 2g and 3g pieces. By constructing a shape bounded by the hyperplanes perpendicular to the symmetry axes of these ridges, you get a 30-cell shape with disphenoidal cells called the [bi-10-cell](https://polytope.miraheze.org/wiki/Bidecachoron). The 1g and 4g pieces are 12c at triakis-tetrahedral vertices, and the 2g and 3g pieces are 3c at triangular ridges. This shape of the puzzle also reflects the symmetry that swaps 1g and 4g and swaps 2g and 3g.

## Prism

!!! example inline end "Prism"
    ![Prism](https://cloud.hypercubing.xyz/assets/img/virt/4d_skewb/prism.png)

By starting with a skewb, you can extend it into the fourth dimension by taking the cartesian product of it with a line segment. This extends the cube to a cubic prism, and the skewb cut planes to hyperplanes all perpendicular to the original cube. This creates a skewb prism, which has exactly the same pieces as the skewb but with shapes that are the prisms of the originals. It allows all the moves of the skewb, and an additional set of moves that involve flipping the new dimension, which appear as reflection moves on the original skewb. By adding more cuts parallel to the original skewb, you can create multi-layer skewb prisms.

## 24-cell-like

### 24-cell skewb diamond lookalike

!!! example inline end "24-cell skewb diamond lookalike"
    ![24-cell skewb diamond lookalike](https://cloud.hypercubing.xyz/assets/img/virt/4d_skewb/24_diamond_lookalike.png)

The 24-cell's cells are octahedra, which have the same symmetry as the skewb, and its dual the skewb diamond. Construct cutting planes parallel to the cells which pass through the centers of the adjacent cells. This creates a puzzle with 24 vertex pieces, 96 ridge pieces, and 144 Y-centers. This puzzle is not half-cut, but each cell's cut pattern looks like a skewb diamond with trivial tips. It is possible to apply [RKT](/techniques/rkt) to a cell of this puzzle, in which case it acts like a skewb diamond.

By rectifying the 24-cell, the trivial tip cuts on the cut patterns of the cells are removed, meaning the cells look like cuboctahedral skewbs.

### 24-cell skewb diamond lookalike, 16-cell cuts

!!! example inline end "24-cell skewb diamond lookalike, 16-cell cuts"
    ![24-cell skewb diamond lookalike, 16-cell cuts](https://cloud.hypercubing.xyz/assets/img/virt/4d_skewb/24_diamond_16.png)

The 24-cell has a subset of cells that correspond to the cells of the 16-cell. If you only keep those cuts, you get a puzzle similar to the one above, but where 8 of the cells no longer appear to have trivial tips in their cut patterns. This puzzle has 16 large corner pieces, 8 small corner pieces, 96 ridge pieces, and 144 Y-centers. Like before, RKT can be applied.

<br>
<br>
<br>

### 24-cell skewb diamond lookalike, 8-cell cuts

!!! example inline end "24-cell skewb diamond lookalike, 8-cell cuts"
    ![24-cell skewb diamond lookalike, 8-cell cuts](https://cloud.hypercubing.xyz/assets/img/virt/4d_skewb/24_diamond_8.png)

The 24-cell also has a subset of cells that correspond to the cells of the 8-cell, or hypercube. If you only keep those cuts, you get another puzzle similar to the one above, but where 16 of the cells do not appear to have trivial tips in their cut patterns, and 8 of the cells appear to have only the trivial tip cuts. This puzzle has 8 large corner pieces, 16 small corner pieces, 32 ridge pieces, and 8 center pieces. Unlike before, RKT cannot be applied to the skewb diamond cells. This puzzle is a shapemod of the [3x3x3x3](/puzzles/3x3x3x3) without corner pieces.
