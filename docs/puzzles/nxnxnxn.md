# NxNxNxN

!!! info inline end "4x4x4x4"
    ![3x3x3x3 in Hyperspeedcube](https://cloud.hypercubing.xyz/assets/img/virt/hsc_4x4x4x4.png)

    **Shape:** Tesseract

NxNxNxN, or N^4^ is a generic term for a 4-dimensional twisty puzzle in the shape of a hypercube with N layers per axis. It is a direct higher dimensional analogy of the NxNxN Rubik's Cube.

This page is concerned with the case where N is greater than 3. The [2x2x2x2](/puzzles/2x2x2x2) and [3x3x3x3](/puzzles/3x3x3x3) have their own pages.

## Pieces

The N^4^ has $N^4 - (N-2)^4$ hypercubies. If N is even, all hypercubies are movable, and if N is odd, all but 8 are movable. It has $8(N-2)^3$ 1c, $24(N-2)^2$ 2c, $32(N-2)$ 3c, and $16$ 4c pieces. These pieces come in many subtypes.

- 1c
    - Centers: These pieces are at the centers of the facets. When $N \geq 3$ is odd, 8 of these pieces exist and they are immovable. They are not present when $N$ is even.
    - T-centers: These pieces exist in orbits of 48 between the facet centers and the ridge centers. When $N \geq 5$ is odd, there are $\frac{N-3}{2}$ orbits. They are not present when $N$ is even.
    - Y-centers: These pieces exist in orbits of 96 between the facet centers and the edge centers. When $N \geq 5$ is odd, there are $\frac{N-3}{2}$ orbits. They are not present when $N$ is even.
    - X-centers: These pieces exist in orbits of 64 between the facet centers and the corners. When $N \geq 5$ is odd, there are $\frac{N-3}{2}$ orbits. When $N \geq 4$ is even, there are $\frac{N-2}{2}$ orbits.
    - Semi-oblique centers: These pieces exist in orbits of 192. There are several subtypes, each of which have $\frac{(N-3)(N-5)}{4}$ orbits when $N \geq 7$ is odd, and $\frac{(N-2)(N-4)}{4}$ when $N \geq 6$ is even.
        - TY-centers: These pieces are between the facet centers, ridge centers, and edge centers.
        - TX-centers: These pieces are between the facet centers, ridge centers, and corners.
        - YX-centers: These pieces are between the facet centers, edge centers, and corners.
    - Oblique centers: These pieces exist in orbits of 192 off all hyperplanes of symmetry. They come in two chiralities. When $N \geq 9$ is odd, there are $\frac{(N-3)(N-5)(N-7)}{8}$ orbits of each chirality. When $N \geq 8$ is even, there are $\frac{(N-2)(N-4)(N-6)}{8}$ orbits of each chirality.
- 2c
    - Middle ridges: These pieces are at the centers of the ridges. When $N \geq 3$ is odd, they come in one orbit of 24. They are not present when $N$ is even.
    - T-ridges: These pieces exist in orbits of 96 between the ridge centers and the edge centers. When $N \geq 5$ is odd, there are $\frac{N-3}{2}$ orbits. They are not present when $N$ is even.
    - X-ridges: These pieces exist in orbits of 96 between the ridge centers and the corners. When $N \geq 5$ is odd, there are $\frac{N-3}{2}$ orbits. When $N \geq 4$ is even, there are $\frac{N-2}{2}$ orbits.
    - Oblique ridges: These pieces exist in orbits of 192, but they are not chiral. When $N \geq 7$ is odd, there are $\frac{(N-3)(N-5)}{4}$ orbits of each chirality. When $N \geq 6$ is even, there are $\frac{(N-2)(N-4)}{4}$ orbits of each chirality.
- 3c
    - Middle edges: These pieces are at the centers of the edges. When $N \geq 3$ is odd, they come in one orbit of 32. They are not present when $N$ is even.
    - Wings: These pieces exist in orbits of 64 between the edge centers and the corners. When $N \geq 5$ is odd, there are $\frac{N-3}{2}$ orbits. When $N \geq 4$ is even, there are $\frac{N-3}{2}$ orbits of each chirality.
- 4c
    - Corners: These pieces are at the corners. When $N \geq 2$, they come in one orbit of 16.

## Turning

Each turn of the N^4^ is a rotation of one of its cubic cells, or a slice layer between two parallel cuts. Each layer turned can be oriented in any of 24 orientations of a cube.
