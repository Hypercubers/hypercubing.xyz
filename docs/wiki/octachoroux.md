# Octachoroux

!!! info inline end "Octachoroux"
    - `Algorithms:` 3D Roux + [RKT Parity](rkt.md#parity)
    - `Move count:` way too many
    
This method is Rowan Fortier's attempt to bring the [Roux method](https://www.speedsolving.com/wiki/index.php/Roux_method) to the 3x3x3x3.

## Summary

1. `1st Block` — Solve a 1x2x3x3 block using blockbuilding techniques.
2. `2nd Block` — Solve a 1x2x3x3 block on the other side of the puzzle.
3. `CMLC` — Orient and permute the corners of the U cell.
4. `L/R` — Solve the Left and Right cells.
5. `M slice` - Permute the M slice.

## Steps

### 1st Block

Start with the "cross piece" of the 1st block. Then build four 2c3c and four 3c4c pairs around it, to complete the 1x2x3x3 block. No RKT is needed for this, as none of the other pieces have been solved yet.

### 2nd Block
Use the free M slice to help you build the pairs to make the 2nd 1x2x3x3 block on the opposite side of the puzzle from the 1st block.

### CMLC
Use the same strategies from [CFOP](cfop.md#4c-olc), but only for the 4C pieces. This step feels like solving the last cell of a 2$^4$, except you have to use 3$^4$ algorithms so that you don't mess up other pieces.

### L/R
Insert the UR and UL 2c pieces using setup moves and EPLL algorithms. Now set up the 3c pieces that need to go to L/R into the IDF spot with the L/R colour on the I cell and the U colour on the D cell. Then move the spot where that L/R edge needs to go above that edge and insert that piece using the RKT algorithm of M D2 M' D2 (2RO' IF' RO2 IF 2RO IF' RO2 IF). Repeat this for all of the edges (pretty tedious).

### M slice
Now all that's left to be solve is the M slice of the puzzle. Notice how the M slice is more like a 3$^3$ than the [PLC](cfop.md#rkt-plc) of CFOP. The centers are already permuted too! However, this step is much more painful than normal RKT PLC due to the strange parities that can happen.

!!! warning "tricky situations"
    - A 3c piece can look "mirrored" in place.
    - A single 3c piece can be rotated wrong.

