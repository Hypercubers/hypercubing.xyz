# RKT

!!! warning "Learn [Notation](notation.md) first"


??? question "Where does the name RKT come from?"
    In the old notation, the I/O cells were called T/K (Top and Kata). Typically different move sets are notated like ```<RK,T>```, but the term was shortened to RKT. Using I/O notation, it should be called ROI, but the old name stuck.

RKT is a technique to treat a single side of an n^d^ puzzle like an n^d-1^ puzzle. On 3^4^, this is done by using RO moves to do an R move to the I cell. Then you can rotate the I cell in any direction you want to do moves on it.

Let's start by translating the Sune OCLL algorithm ```R U R' U R U2 R'``` into RKT.

1. Translate the algorithm to only use rotations and R moves:
2. ```R U R' U R U2 R'``` becomes ```R z R z' R' z R z' R z R2 z' R'```.
3. R moves become RO turns.
4. Any rotations in the algorithm ```x, y, or z```, become their respective I cell rotation ```IR, IU, IF```.
5. Putting this all together, we have ```RO IF RO IF' RO' IF RO IF' RO IF RO2 IF' RO'```

<iframe width="250" height="380" style="width: 250px; height: 380px; overflow: hidden;" src="https://ruwix.com/widget/3d/?label=RU%20Sune&alg=R%20U%20R'%20U%20R%20U2%20R'&flags=showalg" scrolling="no"></iframe>
<iframe width="250" height="380" style="width: 250px; height: 380px; overflow: hidden;" src="https://ruwix.com/widget/3d/?label=Rz%20Sune&alg=R%20z%20R%20z'%20R'%20z%20R%20z'%20R%20z%20R2%20z'%20R'&flags=showalg" scrolling="no"></iframe>

![Sune with RKT](/assets/images/SuneRKTgif.gif){width="50%"}

!!! note
    Even though this technique is called RKT, it is not limited to those types of turns. Thus, you can use LO and I- moves instead, or rotate your view and use RU and D- instead of RK and I-.

This can definitely be very confusing and disorienting to beginners, as you have to think about 3x3x3 moves with only R moves and rotations. It takes a lot of practice to get comfortable with RKT, but it is an **extremely** powerful technique.

Another popular way to do this is to use -K moves (treating the puzzle like a big 3^3^), and wide O cell turns. This means that you can turn the I cell and make it look like a normal cube, you just have to worry about moving the wide O layer to do the turns. Essentially, this is the same exact thing, we're just looking at it from another angle. Think of how doing ```Lw x'``` is the same thing as doing ```R```.

## Parity
RKT parity is a state you can get to that appears to rotate a single layer of a cell by 180°. 
If you try and fix this with RKT, then you will have debt. This means that you must use an algorithm to solve it.

You can use a 3D algorithm that rotates the U center 180° (`R U R' U`x5, or `L R U2 R' L' U`x2).
Harder to memorize (but much lower in movecount) is this 9-mover RKT parity alg:
`IU UR IU' IF' UO' IF RF UR RF' UIR`, found by Tetrian22.

- [PLL + RKT parity algs by Eff](https://docs.google.com/spreadsheets/d/1oHNpWKSnR0p6PMiwQT5IciE2f7Wmw2cC-Kfol0XrzG4/edit)

On 2^4^, the algorithm is shorter because it doesn't have to worry about messing up other pieces besides corners. A commonly used one is ```R2 B2 R2 U R2 B2 R2 U'```<sub>RKT</sub>.

On bigger n^4^ puzzles (where n>3), it can look like a single _slice_ layer of a cell is off by 180°. An intuitive way to solve this is to do the 2^4^ RKT parity algorithm with wide moves, and then the normal 3^4^ RKT parity algorithm. It can also be avoided by just lining up your slice the same way you line up centers in 3D before finishing last 4 edges (when using freeslice).

```[f' r': [[r' U' l': D2], Iy2]]```(swaps UF and UR) 

## Debt
RKT Debt is when the R cell isn't aligned with the rest of the puzzle. For example, after executing a T perm algorithm with RKT, the R cell will be misaligned by 90°.
RKT Debt always has to be paid back at some point during the solve. During complicated setup moves for fancy inserts, RKT debt can be used as "ammo". That is, undoing the debt in a useful way to help solve the puzzle.

## Cancels

<center>![Sune with RKT](/assets/images/SuneRKTcancel.gif){width="80%"}</center>

RKT cancelling is a newer technique that reduces the move count of RKT algorithms by abusing symmetries. HactarCE made a program called RocKeT to find cancels for algorithms. Often, it just involves inserting some flipping moves at certain points throughout the algorithm.

## Simultaneous RKT

RKT can be done by using 2 opposite sides (e.g. `RO` and `LO` turns) as well as normal I cell turns. This would allow you to execute `<R,U,L>` gen algorithms easier, at the cost of having to fix RKT debt on both layers. Another interesting way to do this is in a method like Belt Method. After solving the belt, orienting opposite sides, and separating the colours, the user is left with solving 2 opposite cells that can be solved simultaneously using RKT. If you turn one of the sides with the belt going through it, it essentially does a twist to both cells. One case that can be annoying is if you want to do a 180° turn on one side, and a 90° turn on the other (you would have to wait until both cells' debt lined up).

## Double RKT +

The term Double/Triple/Quadruple/etc... RKT is used to refer to *using* RKT to *do* RKT in 5D+ puzzles. Because RKT lets us treat a single side of an n^d^ like an n^d-1^, using RKT on the 3^5^ lets us treat a single 4D cell as a 3^4^. And if you know how to use RKT to treat a 3^4^ like a 3^3^, then you can do Double RKT. This generalizes to any number of dimensions, but the movecount doubles each time, making it impractical. This is why bigger n^d^ puzzles are mostly solved using [commutators](commutators.md).
