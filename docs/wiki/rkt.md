# RKT

!!! warning "Learn [Notation](notation.md) first"


??? question "Where does the name RKT come from?"
    In the old notation, the I/O cells were called T/K (Top and Kata). Typically different move sets are notated like ```<RK,T>```, but the term was shortened to RKT. Using I/O notation, it should be called ROI, but the old name stuck.

RKT is a technique to treat a single side of an n<sup>d</sup> puzzle like an n<sup>d-1</sup> puzzle. On 3x3x3x3, this is done by using RO moves to do an R move to the I cell. Then you can rotate the I cell in any direction you want to do moves on it.

Let's start by translating the Sune OCLL algorithm ```R U R' U R U2 R'``` into RKT.

1. Translate the algorithm to only use rotations and R moves:
2. ```R U R' U R U2 R'``` becomes ```R z R z' R' z R z' R z R2 z' R'```.
3. R moves become RO turns.
4. Any rotations in the algorithm ```x, y, or z```, become their respective I cell rotation ```IR, IU, IF```.
5. Putting this all together, we have ```RO IF RO IF' RO' IF RO IF' RO IF RO2 IF' RO'```

<iframe width="250" height="380" style="width: 250px; height: 380px; overflow: hidden;" src="https://ruwix.com/widget/3d/?label=RU%20Sune&alg=R%20U%20R'%20U%20R%20U2%20R'&flags=showalg" scrolling="no"></iframe>
<iframe width="250" height="380" style="width: 250px; height: 380px; overflow: hidden;" src="https://ruwix.com/widget/3d/?label=Rz%20Sune&alg=R%20z%20R%20z'%20R'%20z%20R%20z'%20R%20z%20R2%20z'%20R'&flags=showalg" scrolling="no"></iframe>

<video autoplay loop muted>
<source type="video/mp4" src="https://i.imgur.com/WpAqiCo.mp4">
</video>

!!! note
    Even though this technique is called RKT, it is not limited to those types of turns. Thus, you can use LO and I- moves instead, or rotate your view and use RU and D- instead of RK and I-.

This can definitely be very confusing and disorienting to beginners, as you have to think about 3x3x3 moves with only R moves and rotations. It takes a lot of practice to get comfortable with RKT, but it is an **extremely** powerful technique.

Another popular way to do this is to use -K moves (treating the puzzle like a big 3x3x3), and wide O cell turns. This means that you can turn the I cell and make it look like a normal cube, you just have to worry about moving the wide O layer to do the turns. Essentially, this is the same exact thing, we're just looking at it from another angle. Think of how doing ```Lw x'``` is the same thing as doing ```R```.

## Parity
RKT parity is a state you can get to that appears to rotate a single layer of a cell by 180°. 
If you try and fix this with RKT, then you will have debt. This means that you must use an algorithm to solve it.

You can use a 3D algorithm that rotates the U center 180° (`R U R' U`x5, or `L R U2 R' L' U`x2).
Harder to memorize (but much lower in movecount) is the optimal 9-mover RKT parity alg:
`IU UR IU' IF' UO' IF RF UR RF' UIR`, found by Tetrian22.

On 2<sup>4</sup>, the algorithm is shorter because it doesn't have to worry about messing up edges. A commonly used one is ```R2 B2 R2 U R2 B2 R2 U'```<sub>RKT</sub>.

On bigger n<sup>4</sup> puzzles (n>3), it can look like a single _slice_ layer of a cell is off by 180°. An intuitive way to solve this is to do the 2x2x2x2 RKT parity algorithm with wide moves, and then the normal 3<sup>4</sup> RKT parity algorithm. It can also be avoided by just lining up your slice the same way you line up centers in 3D before finishing last 4 edges (when using freeslice).

```[f' r': [[r' U' l': D2], Iy2]]```(swaps UF and UR) 

## Debt
RKT Debt is when the R cell isn't aligned with the rest of the puzzle. For example, after executing a T perm algorithm with RKT, the R cell will be misaligned by 90°.
RKT Debt always has to be paid back at some point during the solve. During complicated setup moves for fancy inserts, RKT debt can be used as "ammo". That is, undoing the debt in a useful way to help solve the puzzle.

## Cancels

<video autoplay loop muted>
<source type="video/mp4" src="https://i.imgur.com/4FThVZx.mp4">
</video>

RKT cancelling is a newer technique that reduces the move count of RKT algorithm by abusing symmetries of the tesseract. HactarCE made a program called RocKeT to find cancels for algorithms. Often, it just involves inserting some flipping moves at random points throughout the algorithm.
