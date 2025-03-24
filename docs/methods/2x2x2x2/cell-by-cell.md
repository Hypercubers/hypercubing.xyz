# Cell by Cell

Cell by Cell is the 4D equivalent of Layer by Layer.


## 1. Solve the first cell

Completely solve one of the sides of the puzzle. You can do this by blockbuilding, or by getting all the same color one on side and then permuting the pieces around until they are solved.

## 2. Solve the last cell

### a. Orient the last cell

In this stage, it is possible to orient the last cell in the same way as you would orient 4c pieces in 3^4^: using [RKT](https://hypercubing.xyz/techniques/rkt/) to set up OCLL cases, and then using RKT to perform those algorithms. However, in 2^4^, because there is no need to preserve 2c and 3c pieces like in 3^4^, there is a lot more flexibility in how pieces can be oriented. Something that can be done is grouping four unoriented corners together in a 1x1x2x2 block; then all four of these pieces can be oriented with just a U OLL case (F R U R’ U’ F’) with big moves. Something similar can be done with the T and L OLL shapes as well. This way of orienting pieces is useful because not only are more pieces oriented at a time, but they don’t take as many moves to do compared to doing the algorithms in RKT. However, if there are less than 4 pieces to orient, then the process from there is largely the same as 3^4^. If there are 3 unoriented pieces, set the pieces into a Sune or Antisune OLL case, and then solve it with RKT. If there are 2 unoriented pieces, set the pieces into a U, T, or L OLL case, and then solve it with RKT. If there is 1 unoriented piece, you can do the monoflip algorithm from 3^4^, though for 2^4^ specifically, a shorter algorithm is to do BR (R U Ozx2 R' U' Ozx2) BL

### b. Permute the last cell

Permute the last cell like a 2^3^ using RKT. You may run into RKT parity in this step, or you can avoid it by using certain last layer algorithms.
