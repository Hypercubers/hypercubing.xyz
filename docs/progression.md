# Progression

This is an outline of how to make your way through the world of hypercubing. Learning puzzles in the wrong order can often lead to confusion, or hindering your understanding in the long run.

!!! quote "Hactar"
    It's very difficult to understand what's really going on in a physical puzzle without first understanding virtual puzzles. We recommend starting with virtual 3^4 for the same reason that 3D cubers typically recommend starting with 3x3x3.

## NxNxNxN's
First, make sure you have good knowledge of the 3x3x3 Rubik's Cube. At the very minimum, how to solve it using a beginner's method, but preferably a more advanced method like CFOP or Roux, and some knowledge of blockbuilding or pairing pieces intuitively.

```mermaid
flowchart LR
    A[3x3x3]
    B[3x3x3x3]
    C[2x2x2x2]
    D[4x4x4x4]
    E[5x5x5x5+]
    F[Physical 2x2x2x2]
    G[Virtual Physical 3x3x3x3]
    A --> B
    B --> C
    C --> D
    C --> F
    D --> E
    F --> G
```

## Other 4D Puzzles
There are many types of 4D puzzles, not just the hypercubes. These include hypercuboids, duoprisms, reqular 4D polytopes, and more. These puzzles require much more knowledge than just the 3x3x3. You'll need to know how to solve 3D cuboids, and generally be able to figure out new puzzles using [commutators](/techniques/commutators).

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
    Z["{5}x{4}"]
    Y["{5}x{3}"]
    X["{5}x{5}"]
    end

    subgraph Hypercuboids
    direction LR
    D[1x3x3x3]
    E[2x3x3x3]
    F[2x2x2x3]
    G[2x2x3x3]
    end

```

## Non-Euclidean Puzzles
While most puzzles in MagicTile aren't 4D, they do share some similar concepts due to their strange geometries.

```mermaid
flowchart LR
    A[Torus Rubik]
    B[Klein Bottle Rubik]
    C[Hyperbolic Rubik]
    D[Other]
    A --> B --> C --> D
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
