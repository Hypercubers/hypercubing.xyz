# 4-Simplex

The 4-simplex is self-dual, so every vertex-turning 4-simplex has an identical facet-turning 4-simplex (and vice versa).

## Facet-turning cut depths

Assume each facet is at distance $1$ from the origin. Then each vertex is at distance $-4$ along the same vector. Thus each cut is in the range $(-4, 1)$

| Name        | Cut distance                   | Piece types       |
| ----------- | ------------------------------ | ----------------- |
| 4-Simplex D | $\left(-\frac{1}{4}, 1\right)$            | 1g + 2g + 3g + 4g |
| 4-Simplex C | $-\frac{1}{4}$                 | 2g + 3g + 4g      |
| 4-Simplex B | $\left(-\frac{2}{3}, -\frac{1}{4}\right)$ | 2g + 3g + 4g + 5g |
| 4-Simplex A | $\left(-\frac{3}{2}, -\frac{2}{3}\right]$ | 3g + 4g + 5g      |
|             | $\left(-4, -\frac{3}{2}\right]$           | 4g + 5g           |

### Piece types

| Name     | Grips |
| -------- | ----- |
| Core     | 0     |
| Center   | 1     |
| Ridge    | 2     |
| Edge     | 3     |
| Corner   | 4     |
| Anticore | 5     |

## Vertex-turning cut depths

Each facet-turning cut distance $d_v$ is equivalent to the facet-turning cut_depth $d_f = -d_v$. Thus each each cut is in the range $(-1, 4)$.

| Name        | Cut distance                 | Piece types       |
| ----------- | ---------------------------- | ----------------- |
|             | $\left[\frac{3}{2}, 4\right)$           | 0g + 1g           |
| 4-Simplex A | $\left[\frac{2}{3}, \frac{3}{2}\right)$ | 0g + 1g + 2g      |
| 4-Simplex B | $\left(\frac{1}{4}, \frac{2}{3}\right)$ | 0g + 1g + 2g + 3g |
| 4-Simplex C | $\frac{1}{4}$                | 1g + 2g + 3g      |
| 4-Simplex D | $\left(-1, \frac{1}{4}\right)$          | 1g + 2g + 3g + 4g |
