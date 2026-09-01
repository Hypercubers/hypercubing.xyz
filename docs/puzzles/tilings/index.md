# Tiling Puzzles

Tiling puzzles are puzzles created from cutting regular tilings in flat euclidean or hyperbolic space. They are primarily simulated on [MagicTile](http://roice3.org/magictile/).

## Topological Spaces

The familiar 3^3^ Rubik's cube lives in spherical space, with the cube having a Schläfli symbol of {$4,3$}. This means that 3 squares (4 edges) meet at a vertex. This can be abstracted - the Schläfli symbol {$4,4$} is 4 squares meeting at each vertex, something that cannot be represented in spherical space. Instead, it is an infinite tiling of the Euclidean plane. The tiling {$4,5$} is too big to fit within even the Euclidean plane, and resides in hyperbolic space. Below is a visualization of the above tilings.

!!! example "Demonstration of square tilings in different spaces ([Roice Nelson and Henry Segerman, 2016](https://arxiv.org/abs/1511.02851))"
    ![Square tilings {4,3}, {4,4}, and {4,5}](https://assets.hypercubing.xyz/img/virt/tilings/square_tilings.png)

!!! info inline end "Hemimegaminx, a projective plane puzzle"
    ![Hemimegaminx in MagicTile](https://assets.hypercubing.xyz/img/virt/tilings/mt_hemimega.png) 

The [projective plane](https://en.wikipedia.org/wiki/Projective_plane) puzzles in MagicTile are spherical puzzles where the two hemispheres are mapped to each other. The point directly opposite each point on the other hemisphere is the same point. Looking at the hemimegaminx from inside the sphere, the point you are looking at and the point at infinity right behind you are the same.

The torus and Klein bottle puzzles are Euclidean plane puzzles that emerge from the same quotient, but with slightly different properties. The copies of the faces on the torus puzzles all rotate the same way, but the faces on the Klein bottle puzzles alternate their rotation due to the differences in topology. Mathologer has an [introduction](https://www.youtube.com/watch?v=DvZnh7-nslo) to Klein bottle puzzles.

## Quotienting

We can cut these tilings (similar to cutting a cube to make a Rubik's cube) to make puzzles. However, the infinite tilings have to be made finite through quotienting - the act of taking a repeating pattern to create a smaller quotient space. Multiple quotients can exist for the same tiling.

!!! example "Two different puzzles created from different quotients of the hex tiling (MagicTile)"
    ![Hex tiling puzzles](https://assets.hypercubing.xyz/img/virt/tilings/mt_hex_tilings_quotients.png)