---
search:
  exclude: true
---

### RKT rank

As above, the existence of RKT was caused by the existence of a certain stabilizer of two grips. However, not all such stabilizers will enable RKT. On the 3×3×3 grip system, there is a stabilizer of `R` and `L` that can only rotate the anti-middle layer (the intersection of the `R` and `L` layers) and cannot cause the `R` layer to emulate another puzzle. In order for the emulation to work, there must be a twist whose axis is `R` that does not fix `L`. In general, RKT is possible on a puzzle when there are two grips $a$ and $b$ where there is a non-identity element that fixes $a$ and $b$, and a different element that fixes $a$ but moves $b$.

This can be generalized even further. We can define an RKT rank-0 puzzle to be one with no twists, i.e. one where the stabilizer of any grip is the whole group. Then, we proceed recursively: an RKT rank-$(n+1)$ puzzle is one where there is some grip $a$ such that the $a$-stabilizer of the grip group is an RKT rank-$n$ puzzle, after removing grips that are stabilized by every element of the stabilizer. This definition correlates with the geometric rank of a puzzle; the RKT rank of a 3^n^ puzzle is $n-2$ for $n\geq 2$.

TODO THIS NEEDS DEVELOPMENT
