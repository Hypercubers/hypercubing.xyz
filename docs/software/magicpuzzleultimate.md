# Magic Puzzle Ultimate

[Magic Puzzle Ultimate](https://superliminal.com/andrey/mpu/) (MPU or MPUlt) is a higher-dimensional puzzle simulator developed by [Andrey Astrelin](https://superliminal.com/andrey/) that can simulate nearly any symmetric doctrinaire puzzle and supports, including user-defined ones.

[Download MPU](https://superliminal.com/andrey/mpu/MPUlt.zip){ .md-button .md-button--primary }

<figure markdown="span">
  ![32-cell in MPU](https://assets.hypercubing.xyz/img/virt/mpu_32cell.png)
  <figcaption>32-cell puzzle in MPU</figcaption>
</figure>

## Records

Some records for the shortest and first solutions of a puzzle are kept on the [Superliminal Wiki page](http://superliminal.com/cube/wiki/MPUlt_Records.html).

## Puzzle file format

All puzzles in MagicPuzzleUltimate are stored in `MPUlt_puzzles.txt`, which is in the same directory as the EXE.

### Syntax

Each nonempty line is contains a **statement**, which consists of a **command** followed by any number of **values**. Commands and values within a statement are separated by spaces. Values may be **strings** (unquoted text with no spaces), **numbers** (floating-point), **vectors** (comma-separated numbers with no spaces), or **transforms** (slash-separated vectors with no spaces).

A transform is represented as a list of vectors, each specifying the normal vector of a mirror plane. These mirrors are composed to form arbitrary isometries that fix the origin. The vectors do not need to be normalized; e.g., `1,0,0` and `2,0,0` define equivalent transforms.

### Menu structure

Puzzles are organized into a nested menu structure.

- `Block <string>` begins a (sub)menu. It takes the name of the menu.
- `EndBlock` ends a (sub)menu. It takes no values.

### Puzzle definitions

- `Puzzle <string>` begins a puzzle. It takes the name of the puzzle.
- `Dim <number>` sets the number of dimensions.
- `NAxis <number>` sets the number of axis orbits. It takes a **number**.
- `Faces <vector list>` defines the pole vectors[^facet-pole] of the facets. Each vector defines an orbit by the pole of one facet in that orbit.
- `Simplified` is optional and removes pieces of the puzzle that do not correspond to polytope elements.
- `Group <transform list>` defines the symmetry group used for `Faces`, `Axis`, `Twists`, and `Cuts`. It takes a list of generators for the symmetry group.
- `Axis <vector>` defines an axis orbit by the vector of one axis in that orbit.
- `Twists <transform list>` defines the twists for an axis orbit, using the axis specified by `Axis` as a reference point. It takes a list of **transforms**, each of which defines one unique twist.
- `Cuts <number list>` defines the cut depths for an axis, which are distances from the origin along the axis vector in descending order.
- `FixedMask <number>` is unknown. It may have something to do with layer masks
- A blank line ends a puzzle definition.

`Axis`, `Twists`, and `Cuts` must be repeated the number of times specified by `NAxis`.

[^facet-pole]: The **pole vector** of a plane is the vector from the origin to the closest point on the plane. The pole vector of a plane is normal to the plane and has magnitude equal to the distance of the plane from the origin. A plane that does not contain the origin always has a unique pole vector, and a nonzero pole vector always corresponds to a unique plane.

??? question "Unknowns that other community members may know the answers to"

    - What does `FixedMask` do?
    - Is the above description of `Simplified` accurate?
    - Is `NAxis 0` valid?
    - Why are negative cut depths sometimes included for symmetric puzzles?
    - Do cut depths need to be sorted in descending order?
    - If the axis vector is not normalized, does that affect the cut depths?

### Example puzzles

For some definitions of various hypercuboids, see [hypercuboids](https://hypercubing.xyz/puzzles/hypercuboids/).

??? abstract "3D Puzzles"

    ??? info "3x3x3"
        ``` title="3x3x3"
        Puzzle 3x3x3
        Dim 3
        NAxis 1
        Faces 1,0,0
        Group 1,0,0/1,1,0 1,0,0/1,0,1
        Axis 1,0,0
        Twists 0,1,0/0,1,1
        Cuts -0.33 0.33
        ```

    ??? info "Skewb"
        ``` title="Skewb"
        Puzzle Skewb
        Dim 3
        NAxis 1
        Faces 1,0,0
        Group 1,0,0/1,1,0 1,0,0/1,0,1
        Axis 1,1,1
        Twists 1,-1,0/1,0,-1
        Cuts 0
        ```

    ??? info "Compy Rainbow"
        ``` title="Compy Rainbow"
        Puzzle Compy_Rainbow
        Dim 3
        NAxis 1
        Faces 1,0,0 0.6667,0.6667,0.6667
        Group 1,0,0/1,1,0 1,0,0/1,0,1
        Axis 1,1,1
        Twists 1,-1,0/1,0,-1
        Cuts -0.45 0.45
        FixedMask 2
        ```

    ??? info "Cuboctahedron"
        ``` title="Cuboctahedron"
        Puzzle Cuboctahedron
        Dim 3
        NAxis 2
        Faces 1,0,0 0.667,0.667,0.667
        Group 1,0,0/1,1,0 1,0,0/1,0,1
        Axis 1,0,0
        Twists 0,1,0/0,1,1
        Cuts 0.5 -0.5
        Axis 1,1,1
        Twists 1,-1,0/1,0,-1
        Cuts 0.5 -0.5
        ```

??? abstract "4D Puzzles"

    ??? abstract "Tesseract Family"

        ??? info "2x2x1x1"
            ``` title="2x2x1x1"
            Puzzle 2x2x1x1
            Dim 0
            NAxis 2
            Faces 1,0,0,0 0,0,0,0.5
            Group 1,0,0,0/1,1,0,0 1,0,0,0/0,0,1,0 1,0,0,0/0,0,0,1 0,1,0,0/0,0,1,0 0,1,0,0/0,0,0,1 0,0,1,0/0,0,1,1
            ```

        ??? info "2x2x2x1"
            ``` title="2x2x2x1"
            Puzzle 2x2x2x1
            Dim 4
            NAxis 2
            Faces 1,0,0,0 0,0,0,0.5
            Group 1,0,0,0/1,1,0,0 1,0,0,0/1,0,1,0 1,0,0,0/0,0,0,1
            Axis 1,0,0,0
            Twists 0,1,0,0/0,1,1,0 0,1,0,0/0,0,0,1
            Cuts 0 0
            Axis 0,0,0,1
            Twists 1,0,0,0/1,1,0,0 1,0,0,0/1,0,1,0
            Cuts
            ```

        ??? info "2x2x2x3"
            ``` title="2x2x2x3"
            Puzzle 2x2x2x3
            Dim 4
            NAxis 2
            Faces 1,0,0,0 0,0,0,1.5
            Group 1,0,0,0/1,1,0,0 1,0,0,0/1,0,1,0 1,0,0,0/0,0,0,1
            Axis 1,0,0,0
            Twists 0,1,0,0/0,1,1,0 0,1,0,0/0,0,0,1
            Cuts 0
            Axis 0,0,0,1
            Twists 1,0,0,0/1,1,0,0 1,0,0,0/1,0,1,0
            Cuts 0.5 -0.5
            ```

        ??? info "2x2x3x3"
            ``` title="2x2x3x3"
            Puzzle 2x2x3x3
            Dim 4
            NAxis 2
            Faces 1,0,0,0 0,0,1.5,0
            Group 1,0,0,0/1,1,0,0 1,0,0,0/0,0,1,0 0,0,1,0/0,0,1,1
            Axis 1,0,0,0
            Twists 0,0,1,0/0,0,1,1 0,1,0,0/0,0,1,0 0,1,0,0/0,0,1,1
            Cuts 0
            Axis 0,0,1,0
            Twists 1,0,0,0/1,1,0,0 0,0,0,1/1,0,0,0 0,0,0,1/1,1,0,0
            Cuts 0.5 -0.5
            ```

        ??? info "2x2x3x4"
            ``` title="2x2x3x4"
            Puzzle 2x2x3x4
            Dim 4
            NAxis 3
            Faces 1,0,0,0 0,0,1.5,0 0,0,0,2
            Group 1,0,0,0/1,1,0,0 1,0,0,0/0,0,1,0 1,0,0,0/0,0,0,1
            Axis 1,0,0,0
            Twists 0,1,0,0/0,0,1,0 0,1,0,0/0,0,0,1 0,0,1,0/0,0,0,1
            Cuts 0
            Axis 0,0,1,0
            Twists 1,0,0,0/1,1,0,0 1,0,0,0/0,0,0,1 0,0,0,1/0,1,0,0
            Cuts 0.5 -0.5
            Axis 0,0,0,1
            Twists 1,0,0,0/1,1,0,0 1,0,0,0/0,0,1,0 0,0,1,0/0,1,0,0
            Cuts 1 0 -1
            ```

        ??? info "2x3x4x5"
            ``` title="2x3x4x5"
            Puzzle 2x3x4x5
            Dim 4
            NAxis 4
            Faces 1,0,0,0 0,1.5,0,0 0,0,2,0 0,0,0,2.5
            Group 1,0,0,0/0,1,0,0 1,0,0,0/0,0,1,0 1,0,0,0/0,0,0,1
            Axis 1,0,0,0
            Twists 0,1,0,0/0,0,1,0 0,1,0,0/0,0,0,1 0,0,1,0/0,0,0,1
            Cuts 0
            Axis 0,1,0,0
            Twists 1,0,0,0/0,0,1,0 1,0,0,0/0,0,0,1 0,0,1,0/0,0,0,1
            Cuts 0.5 -0.5
            Axis 0,0,1,0
            Twists 1,0,0,0/0,1,0,0 1,0,0,0/0,0,0,1 0,0,0,1/0,1,0,0
            Cuts 1 0 -1
            Axis 0,0,0,1
            Twists 1,0,0,0/0,1,0,0 1,0,0,0/0,0,1,0 0,0,1,0/0,1,0,0
            Cuts 1.5 0.5 -0.5 -1.5
            ```

        ??? info "3x3x3x1"
            ``` title="3x3x3x1"
            Puzzle 3x3x3x1
            Dim 4
            NAxis 2
            Faces 1.5,0,0,0 0,0,0,0.5
            Group 1,0,0,0/1,1,0,0 1,0,0,0/1,0,1,0 1,0,0,0/0,0,0,1
            Axis 1,0,0,0
            Twists 0,1,0,0/0,1,1,0 0,1,0,0/0,0,0,1
            Cuts 0.5 -0.5
            Axis 0,0,0,1
            Twists 1,0,0,0/1,1,0,0 1,0,0,0/1,0,1,0
            Cuts
            ```

        ??? info "3x3x3x2"
            ``` title="3x3x3x2"
            Puzzle 3x3x3x2
            Dim 4
            NAxis 2
            Faces 1.5,0,0,0 0,0,0,1
            Group 1,0,0,0/1,1,0,0 1,0,0,0/1,0,1,0 1,0,0,0/0,0,0,1
            Axis 1,0,0,0
            Twists 0,1,0,0/0,1,1,0 0,1,0,0/0,0,0,1
            Cuts -0.5 0.5
            Axis 0,0,0,1
            Twists 1,0,0,0/1,1,0,0 1,0,0,0/1,0,1,0
            Cuts 0
            ```

        ??? info "4x4x4x4"
            ``` title="4x4x4x4"
            Puzzle 4^4
            Dim 4
            NAxis 1
            Faces 1,0,0,0
            Group 1,0,0,0/1,1,0,0 1,0,0,0/1,0,1,0 1,0,0,0/1,0,0,1
            Axis 1,0,0,0
            Twists 0,1,0,0/0,1,1,0 0,1,-1,0/0,0,0,1 0,2,-1,-1/0,1,1,-2
            Cuts 0.5 0 -0.5
            ```

    ??? abstract "Other"

        ??? info "{4}x{4} 3"
            ``` title="{4}x{4} 3"
            Puzzle {4}x{4} 3
            Dim 4
            NAxis 2
            Faces 1,0,0,0 0,0,1,0
            Group 1,0,0,0/1,1,0,0 1,0,0,0/0,0,1,0 0,0,1,0/0,0,1,1
            Axis 1,0,0,0
            Twists 0,1,0,0/0,0,1,0 0,0,1,0/0,0,1,1
            Cuts 0.5 -0.5
            Axis 0,0,1,0
            Twists 1,0,0,0/1,1,0,0 1,0,0,0/0,0,0,1
            Cuts 0.5 -0.5
            ```

        ??? info "3^4 Skewb"
            ``` title="3^4 Skewb"
            Puzzle 3^4 Skewb
            Dim 4
            NAxis 1
            Faces 1,0,0,0
            Simplified
            Group 1,0,0,0/1,1,0,0 1,0,0,0/1,0,1,0 1,0,0,0/1,0,0,1
            Axis 1,1,1,1
            Twists 0,2,-1,-1/0,1,1,-2 1,-1,0,0/0,0,1,-1
            Cuts 0
            ```

        ??? info "5-5_Duotegum"
            ``` title="5-5_Duotegum"
            Puzzle 5-5_Duotegum
            Dim 4
            NAxis 1
            Faces -1,1,0,0
            Group 1,0,0,0/0.809016994,0,0.587785252,0 1,1,0,0/0,0,1,1
            Axis -1,1,0,0
            Twists 0,0,1,0/0,0,0,1 1,1,0,0/0,0,1,1 1,1,0,0/0,0,-1,1
            Cuts 0.65
            ```

        ??? info "16-cell Face Turning"
            ``` title="16-cell Face Turning"
            Puzzle 16-cell_FT
            Dim 4
            NAxis 1
            Faces 1,1,1,1
            Group 1,0,0,0/1,1,0,0 1,0,0,0/1,0,1,0 1,0,0,0/1,0,0,1
            Axis 1,1,1,1
            Twists 0,2,-1,-1/0,1,1,-2 1,-1,0,0/0,0,1,-1
            Cuts 0.6 -0.6
            FixedMask 2
            ```

        ??? info "Chamfered Pentagonal Duoprism"
            ``` title="Chamfered Pentagonal Duoprism"
            Puzzle Chamfered_Pentagonal_Duoprism
            Dim 4
            NAxis 2
            Faces -1.41429,0,0,0 1.41429,0,0,0 -1,1,0,0
            Group 1,0,0,0/0.809016994,0,0.587785252,0 1,1,0,0/0,0,1,1
            Axis -1,0,0,0
            Twists 0,1,0,0/0,0.809016994,0,0.587785252 0,0,1,0/0,0,0,1
            Cuts 1.3 -1.23
            Axis -1,1,0,0
            Twists 0,0,1,0/0,0,0,1 1,1,0,0/0,0,1,1 1,1,0,0/0,0,-1,1
            Cuts 0.85
            ```

        ??? info "Chamfered Tesseract"
            ``` title="Chamfered Tesseract"
            Puzzle Chamfered_Tesseract
            Dim 4
            NAxis 2
            Faces 1,0,0,0 0.70710678,0.70710678,0,0
            Group 1,0,0,0/1,1,0,0 1,0,0,0/1,0,1,0 1,0,0,0/1,0,0,1
            Axis 1,0,0,0
            Twists 0,1,0,0/0,1,1,0 0,1,0,0/0,1,0,1 0,0,1,0/0,0,1,1
            Cuts 0.85 -0.85
            Axis 1,1,0,0
            Twists 0,0,1,0/0,0,1,1 1,-1,0,0/0,0,1,0 1,-1,0,0/0,0,1,1
            Cuts 0.57 -0.57
            ```

        ??? info "Octahedral Prism"
            ``` title="Octahedral Prism"
            Puzzle Octahedral_Prism
            Dim 4
            NAxis 2
            Faces 1,0,0,0 0,1,1,1
            Group 1,0,0,0/0,1,0,0 0,1,0,0/0,1,1,0 0,1,0,0/0,1,0,1
            Axis 1,0,0,0
            Twists 0,1,0,0/0,1,1,0 0,1,1,0/0,0,1,1 0,1,0,0/0,0,1,1
            Cuts 0.5 -0.5
            Axis 0,1,1,1
            Twists 0,1,-1,0/0,1,0,-1 1,0,0,0/0,1,-1,0
            Cuts 0.5 -0.5
            ```

        ??? info "Snub 24-cell"
            ``` title="Snub 24-cell"
            Puzzle Snub24cell
            Dim 4
            NAxis 2
            Faces 1,0,0,0 0.809017,0.809017,0,0 0.9045085,0.6545085,0.25,0
            #Faces 1,0,0,0 0.809017,0.809017,0,0 0.9045085,0.6545085,0.25,0 0.9045085,0.6545085,-0.25,0
            Group 0,2,-1,-1/0,1,1,-2 0,1,1,2/0,2,-1,1 2,-2,-2,0/1,-1,-1,3
            Axis 1,0,0,0
            Twists 0,2,-1,-1/0,1,1,-2 0,0,1,0/0,0,0,1 0,1,1,2/0,2,-1,1
            Cuts 0.9 -0.9
            FixedMask 2
            Axis 0.809017,0.809017,0,0
            Twists 2,-2,-2,0/1,-1,-1,3 1,-1,-1,-3/2,-2,-2,0 0,0,0,1/0,0,1,0
            Cuts 0.95 -0.95
            FixedMask 2
            ```

        ??? info "Square Antiprism Prism"
            ``` title="Square Antiprism Prism"
            Puzzle Square_Antiprism_Prism
            Dim 4
            NAxis 3
            Faces -0.5,0,0,0 0,0,0.42044820,0 0,0.56903559,0.14014940,0
            Group 0,0,1,0/0,0.38268343,0,0.92387953 0,0,0,1/0,1,0,1 1,0,0,0/0,0,0,1
            Axis 1,0,0,0
            Twists 0,1,0,0/0,1,0,1 0,0,1,0/0,0.38268343,0,0.92387953 0,0,1,0/0,-0.38268343,0,0.92387953
            Cuts 0.1666 -0.1666
            Axis 0,0,1,0
            Twists 0,1,0,0/0,1,0,1 1,0,0,0/0,1,0,0 1,0,0,0/0,1,0,1
            Cuts 0.1235 -0.1235
            Axis 0,0.56903559,0.14014940,0
            Twists 1,0,0,0/0,0,0,1
            Cuts 0.621
            ```

        ??? info "Triangular Antitegmatic Icoschoron"
            ``` title="Triangular Antitegmatic Icosachoron"
            Puzzle Triangular-antitegmatic_Icosachoron
            Dim 4
            NAxis 1
            Faces 1,0,0,0
            Group 1,0,0,0/0.5,0.866025404,0,0 0,0.577350269,0.816496581,0/0,0,0.612372436,0.790569415
            #1,0,0,0/0.5,sqrt(3)/2,0,0 0,1/sqrt(3),sqrt(2/3),0/0,0,1/sqrt(6),sqrt(5/6)
            Axis 1,0,0,0
            Twists 0,0.577350269,0.816496581,0/0,0,0.612372436,0.790569415 0,0.790569,-0.559017,0.25/0,0.57735,1.22474,0.912871
            Cuts 0.75 -0.75
            ```

??? abstract "5D Puzzles"

    ??? abstract "Penteract Family"

        ??? info "1x1x1x1x2"
            ``` title="1x1x1x1x2"
            Puzzle 1x1x1x1x2
            Dim 5
            NAxis 2
            Faces 0.5,0,0,0,0 0,0,0,0,1
            Group 1,0,0,0,0/1,1,0,0,0 1,0,0,0,0/1,0,1,0,0 1,0,0,0,0/1,0,0,1,0 1,0,0,0,0/0,0,0,0,1
            Axis 1,0,0,0,0
            Twists 0,1,0,0,0/0,1,1,0,0 0,1,0,0,0/0,0,0,0,1
            Cuts
            Axis 0,0,0,0,1
            Twists 1,0,0,0,0/1,1,0,0,0
            Cuts 0
            ```

        ??? info "1x1x1x2x2"
            ``` title="1x1x1x2x2"
            Puzzle 1x1x1x2x2
            Dim 5
            NAxis 2
            Faces 0.5,0,0,0,0 0,0,0,1,0
            Group 1,0,0,0,0/1,1,0,0,0 1,0,0,0,0/1,0,1,0,0 1,0,0,0,0/0,0,0,1,0 0,0,0,1,0/0,0,0,1,1
            Axis 1,0,0,0,0
            Twists 0,1,0,0,0/0,1,1,0,0 0,1,0,0,0/0,0,0,1,0 0,0,0,1,0/0,0,0,1,1
            Cuts
            Axis 0,0,0,1,0
            Twists 1,0,0,0,0/1,1,0,0,0 1,0,0,0,0/1,0,1,0,0 1,0,0,0,0/0,0,0,0,1
            Cuts 0
            ```

        ??? info "1x1x2x2x2"
            ``` title="1x1x2x2x2"
            Puzzle 1x1x2x2x2
            Dim 5
            NAxis 2
            Faces 0.5,0,0,0,0 0,0,1,0,0
            Group 1,0,0,0,0/1,1,0,0,0 1,0,0,0,0/0,0,1,0,0 0,0,1,0,0/0,0,1,1,0 0,0,1,0,0/0,0,1,0,1
            Axis 1,0,0,0,0
            Twists 0,1,0,0,0/0,0,1,0,0 0,0,1,0,0/0,0,1,1,0
            Cuts
            Axis 0,0,1,0,0
            Twists 1,0,0,0,0/1,1,0,0,0 1,0,0,0,0/0,0,0,1,0 0,0,0,1,0/0,0,0,1,1
            Cuts 0
            ```

        ??? info "1x2x2x2x2"
            ``` title="1x2x2x2x2"
            Puzzle 1x2x2x2x2
            Dim 5
            NAxis 2
            Faces 0.5,0,0,0,0 0,1,0,0,0
            Group 1,0,0,0,0/0,1,0,0,0 0,1,0,0,0/0,1,1,0,0 0,1,0,0,0/0,1,0,1,0 0,1,0,0,0/0,1,0,0,1
            Axis 1,0,0,0,0
            Twists 0,1,0,0,0/0,1,1,0,0
            Cuts
            Axis 0,1,0,0,0
            Twists 1,0,0,0,0/0,0,1,0,0 0,0,1,0,0/0,0,1,1,0
            Cuts 0
            ```

        ??? info "2x2x2x2x2"
            ``` title="2x2x2x2x2"
            Puzzle 2^5
            Dim 5
            NAxis 1
            Faces 1,0,0,0,0
            Group 1,0,0,0,0/1,1,0,0,0 1,0,0,0,0/1,0,1,0,0 1,0,0,0,0/1,0,0,1,0 1,0,0,0,0/1,0,0,0,1
            Axis 1,0,0,0,0
            Twists 0,1,0,0,0/0,1,1,0,0
            Cuts 0
            ```


    ??? abstract "Other"

        ??? info "Simplex Prism"
            ``` title="Simplex Prism"
            Puzzle Simplex_Prism
            Dim 5
            NAxis 2
            Faces 0,0,0,0,1 1,0,0,0,0
            Group 1,0,0,0,0 0,0,1,1,0/0,0,1,-1,0 0,2,-1,-1,0/0,1,1,-2,0 0,2,-2,0,0/0,1,1,-1,-2.236068
            Axis 0,0,0,0,1
            Twists 1,0,0,0,0/0,1,-1,0,0 0,0,1,1,0/0,0,1,-1,0 0,2,-1,-1,0/0,1,1,-2,0
            Cuts 0
            Axis 1,0,0,0,0
            Twists 0,2,-1,-1,0/0,1,1,-2,0
            Cuts 0
            ```

        ??? info "{3,3}x{4}"
            ``` title="{3,3}x{4}"
            Puzzle {3,3}x{4}
            Dim 5
            NAxis 2
            Faces 1,1,1,0,0 0,0,0,1.73205081,0
            Group 1,1,0,0,0/1,0,-1,0,0 1,1,0,0,0/0,1,-1,0,0 0,0,0,1,0/0,0,0,1,1
            Axis 1,1,1,0,0
            Twists 0,0,0,1,0/0,0,0,1,1 1,-1,0,0,0/1,0,-1,0,0 1,-1,0,0,0/0,0,0,1,0
            Cuts -0.33333
            Axis 0,0,0,1,0
            Twists 1,1,0,0,0/1,0,-1,0,0 0,0,0,0,1/1,-1,0,0,0
            Cuts 0
            ```

Below is also a general formula for 4D polygonal duoprism puzzles, made by Luna:

``` title="{p}x{q}"
Puzzle {p}x{q}
Dim 4
NAxis 2
Faces 1,0,0,0 0,0,1,0
Group 1,0,0,0/1,tan(pi/p),0,0 0,0,1,0/0,0,1,tan(pi/q)
Axis 1,0,0,0
Twists 0,1,0,0/0,0,0,1 0,0,1,0/0,0,1,tan(pi/q)
Cuts ...
Axis 0,0,1,0
Twists 0,0,0,1/0,1,0,0 1,0,0,0/1,tan(pi/p),0,0
Cuts ...
```
