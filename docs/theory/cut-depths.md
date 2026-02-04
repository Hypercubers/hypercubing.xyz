# Cut Depths

## 3D puzzles

### Tetrahedron

The tetrahedron is self-dual, so every vertex-turning tetrahedron has an identical facet-turning tetrahedron (and vice versa).

#### Facet-turning cut depths

Assume each facet is at distance $1$ from the origin. Then each vertex is at distance $-3$ along the same vector. Thus each cut is in the range $(-3, 1)$.

| Common Name               | Technical Name | Cut distance                      | Piece types  |
| ------------------------- | -------------- | --------------------------------- | ------------ |
| Halpern-Meier Tetrahedron | 4-Simplex C    | $\left( -\frac{1}{3}, 1 \right)$  | 1g + 2g + 3g |
| Tetraminx                 | 4-Simplex B    | $-\frac{1}{3}$                    | 2g + 3g      |
|                           | 4-Simplex A    | $\left( -1, -\frac{1}{3} \right)$ | 2g + 3g + 4g |
| 2-Layer Pyraminx          |                | $\left( -3, -1 \right]$           | 3g + 4g      |

##### Piece types

| Name     | Grips |
| -------- | ----- |
| Core     | 0     |
| Center   | 1     |
| Edge     | 2     |
| Corner   | 3     |
| Anticore | 4     |

#### Vertex-turning cut depths

Each facet-turning cut distance $d_v$ is equivalent to the facet-turning cut_depth $d_f = -d_v$. Thus each each cut is in the range $(-1, 3)$.

| Common Name               | Technical Name | Cut distance                     | Piece types  |
| ------------------------- | -------------- | -------------------------------- | ------------ |
| 2-Layer Pyraminx          |                | $\left[ 1, 3 \right)$            | 0g + 1g      |
|                           | 4-Simplex A    | $\left( \frac{1}{3}, 1 \right)$  | 0g + 1g + 2g |
| Tetraminx                 | 4-Simplex B    | $\frac{1}{3}$                    | 1g + 2g      |
| Halpern-Meier Tetrahedron | 4-Simplex C    | $\left( -1, \frac{1}{3} \right)$ | 1g + 2g + 3g |

#### 4-Simplex Pyraminx

The 3-Layer 4-Simplex Pyraminx is a combination of the 2-Layer 4-Simplex Pyraminx with 4-Simplex A.

### Dodecahedron

#### Facet-turning cut depths

Assume each facet is at distance $1$ from the origin. Thus each cut is in the range $[0, 1)$.

Note that $\phi = \frac{1 + \sqrt 5}{2}$.

| Name                         | Cut distance                                           | Piece types                            |
| ---------------------------- | ------------------------------------------------------ | -------------------------------------- |
| Megaminx                     | $\left[ \frac{1}{\phi}, 1 \right)$                     | 1g, 2g, 3g                             |
| Megaminx Crystal             | $\left( \frac{1}{\sqrt 5}, \frac{1}{\phi} \right)$     | 1g, 2g, 3g, 4g                         |
| Pyraminx Crystal             | $\frac{1}{\sqrt 5}$                                    | 3g, 4g                                 |
| Litestarminx, Curvy Starminx | $\left( \frac{2}{\phi} - 1, \frac{1}{\sqrt 5} \right)$ | 3g, 4g, 5g, 6g (PU center)             |
| Starminx                     | $\frac{2}{\phi} - 1$                                   | 4g, 5g, 6g (PU center)                 |
| Master Pentultimate          | $\left( 0, \frac{2}{\phi} - 1 \right)$                 | 4g, 5g, 6g (PU center), 6g (PU corner) |
| Pentultimate                 | $0$                                                    | 6g (PU center), 6g (PU corner)         |

##### Piece types

| Name                | Grips             |
| ------------------- | ----------------- |
| Core                | 0                 |
| Megaminx center     | 1                 |
| Megaminx edge       | 2                 |
| Megaminx corner     | 3                 |
| Crystal edge        | 4 (F U R L)       |
| Crystal petal       | 5 (F U R L DR)    |
| Pentultimate center | 6 (F U R L DR DL) |
| Pentultimate corner | 6 (F U R L DR BR) |

### Icosahedron

#### Facet-turning cut depths

Assume each facet is at distance $1$ from the origin. Thus each cut is in the range $[0, 1)$.

Note that $\phi = \dfrac{1 + \sqrt 5}{2}$.

| Name            | Cut distance                                            | Piece types                                                                         |
| --------------- | ------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| Radiolarian 1.5 | $\left( \frac{\sqrt{5}}{3}, 1 \right)$                  | 1g, 2g, 3g, 4g (Wing), 5g (Corner)                                                  |
| Radiolarian 2   | $\frac{\sqrt{5}}{3}$                                    | 2g, 3g, 4g (Wing), 5g (Corner)                                                      |
| Radiolarian 3   | $\left( \frac{1}{\phi}, \frac{\sqrt{5}}{3} \right)$     | 2g, 3g, 4g (Wing), 4g (Center), 5g (Corner)                                         |
| Radiolarian 4   | $\frac{1}{\phi}$                                        | 3g, 4g (Wing), 4g (Center), 5g (Corner)                                             |
| Radiolarian 4.5 | $\left( \frac{4+\sqrt{5}}{11}, \frac{1}{\phi} \right)$  | 3g, 4g (Wing), 4g (Center), 5g (Corner), 5g (Petal), 6g (Edge)                      |
| Radiolarian 5   | $\frac{4+\sqrt{5}}{11} = \frac{\phi^2}{2+\phi^2}$       | 4g (Wing), 4g (Center), 5g (Corner), 5g (Petal), 6g (Edge)                          |
| Radiolarian 6   | $\left( \frac{4+\sqrt{5}}{11}, \frac{1}{\phi} \right)$  | 4g (Wing), 4g (Center), 5g (Corner), 5g (Petal), 6g (Edge), 6g (Petal)              |
| Radiolarian 7   | $5 - 2\sqrt(5)$                                         | 4g (Center), 5g (Corner), 5g (Petal), 6g (Edge), 6g (Petal)                         |
| Radiolarian 8   | $\left[ \frac{3-\sqrt{5}}{2}, 5 - 2\sqrt{5} \right)$    | 4g (Center), 5g (Corner), 5g (Petal), 6g (Edge), 6g (Petal), 7g                     |
| Radiolarian 8.5 | $\left( \frac{1}{3}, \frac{3-\sqrt{5}}{2} \right)$      | 4g (Center), 5g (Corner), 5g (Petal), 6g (Edge), 6g (Petal), 7g, 8g (Edge)          |
| Radiolarian 9   | $\frac{1}{3}$                                           | 5g (Corner), 6g (Petal), 7g, 8g (Edge)                                              |
| Radiolarian 10  | $\left( \frac{1}{\phi^3}, \frac{1}{3} \right)$          | 6g (Petal), 7g, 8g (Edge), 8g (Kite), 9g (Petal), 10g (Center)                      |
| Radiolarian 11  | $\frac{1}{\phi^3} = \sqrt{5}-2$                         | 7g, 8g (Edge), 8g (Kite), 9g (Petal), 10g (Center)                                  |
| Radiolarian 12  | $\left( 1-\frac{2}{\sqrt{5}}, \frac{1}{\phi^3} \right)$ | 7g, 8g (Edge), 8g (Kite), 9g (Petal), 9g (Wing), 10g (Center), 10g (Corner)         |
| Radiolarian 13  | $1-\frac{2}{\sqrt{5}}$                                  | 8g (Edge), 8g (Kite), 9g (Petal), 9g (Wing), 10g (Center), 10g (Corner)             |
| Radiolarian 14  | $\left( 0, 1-\frac{2}{\sqrt{5}} \right)$                | 8g (Edge), 8g (Kite), 9g (Petal), 9g (Wing), 10g (Center), 10g (Corner), 10g (Wing) |
| Radiolarian 15  | $0$                                                     | 10g (Center), 10g (Corner), 10g (Wing)                                              |

##### Piece types

| Name                    | Grips |
| ----------------------- | ----- |
| Core                    | 0     |
| Stationary Center       | 1     |
| Shallow Edge            | 2     |
| Shallow Corner          | 5     |
| Shallow Petal           | 3     |
| Shallow Corner Petal    | 4     |
| Shallow Moving Center   | 4     |
| Intermediate Edge       | 6     |
| Shallow Center Adjacent | 5     |
| Shallow Corner Adjacent | 6     |
| Edge Wing               | 7     |
| Deep Edge               | 8     |
| Deep Center             | 10    |
| Deep Center Adjacent    | 9     |
| Kite                    | 8     |
| Deep Corner             | 10    |
| Deep Edge Wing          | 9     |
| Deep Corner Petal       | 10    |

## 4D puzzles

### 4-Simplex

The 4-simplex is self-dual, so every vertex-turning 4-simplex has an identical facet-turning 4-simplex (and vice versa).

#### Facet-turning cut depths

Assume each facet is at distance $1$ from the origin. Then each vertex is at distance $-4$ along the same vector. Thus each cut is in the range $(-4, 1)$.

| Name                       | Cut distance                                | Piece types       |
| -------------------------- | ------------------------------------------- | ----------------- |
| 4-Simplex D                | $\left( -\frac{1}{4}, 1 \right)$            | 1g + 2g + 3g + 4g |
| 4-Simplex C                | $-\frac{1}{4}$                              | 2g + 3g + 4g      |
| 4-Simplex B                | $\left( -\frac{2}{3}, -\frac{1}{4} \right)$ | 2g + 3g + 4g + 5g |
| 4-Simplex A                | $\left( -\frac{3}{2}, -\frac{2}{3} \right]$ | 3g + 4g + 5g      |
| 2-Layer 4-Simplex Pyraminx | $\left( -4, -\frac{3}{2} \right]$           | 4g + 5g           |

##### Piece types

| Name     | Grips |
| -------- | ----- |
| Core     | 0     |
| Center   | 1     |
| Ridge    | 2     |
| Edge     | 3     |
| Corner   | 4     |
| Anticore | 5     |

#### Vertex-turning cut depths

Each facet-turning cut distance $d_v$ is equivalent to the facet-turning cut_depth $d_f = -d_v$. Thus each each cut is in the range $(-1, 4)$.

| Name                       | Cut distance                            | Piece types       |
| -------------------------- | --------------------------------------- | ----------------- |
| 2-Layer 4-Simplex Pyraminx | $\left[ \frac{3}{2}, 4 \right)$           | 0g + 1g           |
| 4-Simplex A                | $\left[ \frac{2}{3}, \frac{3}{2} \right)$ | 0g + 1g + 2g      |
| 4-Simplex B                | $\left( \frac{1}{4}, \frac{2}{3} \right)$ | 0g + 1g + 2g + 3g |
| 4-Simplex C                | $\frac{1}{4}$                           | 1g + 2g + 3g      |
| 4-Simplex D                | $\left( -1, \frac{1}{4} \right)$          | 1g + 2g + 3g + 4g |

#### 4-Simplex Pyraminx

The 3-Layer 4-Simplex Pyraminx is a combination of the 2-Layer 4-Simplex Pyraminx with 4-Simplex A.
