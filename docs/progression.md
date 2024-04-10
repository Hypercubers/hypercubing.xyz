# Progression

This is an outline of how to make your way through the world of hypercubing. Learning puzzles in another order could lead to confusion or an incomplete understanding in the long run.

!!! quote "Hactar"
    It's very difficult to understand what's really going on in a physical puzzle without first understanding virtual puzzles. We recommend starting with virtual 3^4 for the same reason that 3D cubers typically recommend starting with 3×3×3.

## N×N×N×N's

First, make sure you know how to solve a 3×3×3 Rubik's Cube. At the very minimum, knowing a beginner's method is enough, but knowing more advanced methods, such as CFOP or Roux, or more advanced techniques, such as blockbuilding or intuitive F2L, could make getting into hypercubing easier.

<!-- I can't get × or & times; to work here -->
```mermaid
flowchart LR
    A[3×3×3]
    B[3×3×3×3]
    C[2×2×2×2]
    D[4×4×4×4]
    E[5×5×5×5+]
    F[Physical 2×2×2×2]
    G[Virtual Physical 3×3×3×3]
    A --> B
    B --> C
    B --> D
    C --> F
    D --> E
    F --> G
```

## Other 4D Puzzles

There are many types of 4D puzzles, not just the hypercubes. These include hypercuboids, duoprisms, reqular 4D polytopes, and more. These puzzles require much more knowledge than just the 3×3×3. You'll need to know how to solve 3D cuboids, and generally be able to figure out new puzzles using [commutators](/techniques/commutators).

```mermaid
flowchart LR
    Hypercuboids --> Duoprisms --> Polytopes

    subgraph Polytopes
    direction LR
    Q[5-cell]
    R[16-cell]
    S[24-cell]
    T[120-cell]
    U[600-cell]
    end

    subgraph Duoprisms
    direction LR
    Z["{5}×{4}"]
    Y["{5}×{3}"]
    X["{5}×{5}"]
    end

    subgraph Hypercuboids
    direction LR
    D[1×3×3×3]
    E[2×3×3×3]
    F[2×2×2×3]
    G[2×2×3×3]
    end
```

## Non-Euclidean Puzzles

While most puzzles in MagicTile aren't 4D, they do share some similar concepts due to their strange geometries.

```mermaid
flowchart LR
    A[Torus Rubik]
    B[Klein Bottle Rubik]
    C[Hyperbolic Rubik]
    E[Hemi-Megaminx]
    D[Other]
    A --> B
    A --> C
    B --> E --> D
```

## 5D+ puzzles

```mermaid
flowchart TD
    subgraph 5D
    direction LR
    A["n⁴"]
    B["3⁵"]
    C["2⁵"]
    D["4⁵"]
    E[Other 4D]
    F[5D simplex]
    A --> B --> C --> D
    E --> F
    A --> E
    end
    subgraph 6D
    direction LR
    G["3⁶"]
    H["Other n⁶"]
    G --> H
    end
    subgraph 7D
    direction LR
    V["3⁷"]
    Q["Other n⁷"]
    V --> Q
    end
    5D --> 6D --> 7D
```
