# 4tega

4tega is the 4-dimensional equivalent of the [Ortega Method](https://www.speedsolving.com/wiki/index.php/Ortega_Method) on 2^3^. There are 2 main variants, as there is no perfect way to generalize this method to 4d.

## Variant 1

### Orient Both Cells
Start by orienting a single side, using either colour from that side or its opposite side. This can easily be done without [RKT](/techniques/rkt.md) by using blockbuilding. Next, use 2^4^ OLC strategies to orient the other cell. Because the first cell isn't solved, you don't have to worry about messing it up, allowing you to save moves.

### Separate colors
Separate the colors of the cells that are oriented, leaving you with 2 2^3^ solves.

### Permute Both Cells
Solve the first cell like a 2^3^ without RKT, then solve the other cell like a 2^3^, but using RKT.

## Variant 2

### Orient Both Cells
Same as in Variant 1.

### Separate colors
Same as in Variant 1.

### Orient Both Layers of Both Cells
Use RKT to orient both layers of both cells, just like OBL in 3D Ortega. This can be done using the OCLL algorithms.

### P4L/PBLBC
Permtue all 4 layers of both cells at once using algorithms. Some algorithms can be found [here](https://docs.google.com/document/d/12CriaqJ1dYtAMpeY3c0dyLSCG9j37DEPKRWr4cl5i9U/edit?usp=sharing).
