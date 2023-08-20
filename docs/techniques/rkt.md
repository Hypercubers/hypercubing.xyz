# RKT

!!! warning "You must know 3^4^ [notation](/notation) in order for this page to make sense!"

RKT is a technique that lets you treat a single cell of a (cell-turning) higher dimensional puzzle as if it were a lower dimensional puzzle. This is very useful to do moves that damage fewer pieces. For example: RKT lets you treat a side of a 3^4^ just like a 3^3^ cube, meaning that you can use all the 3D algorithms you already know to solve the full 4D puzzle.

It has been invented independently several times, but was mainly popularized by Raymond Zhao in his article [here](https://rayzz.me/articles/hypercubing/rkt.html).

## Naming

!!! note inline end "Other proposed names:"
    - SFM (Single Facet Manipulation)
    - FRM (Facet Redution Method)

The name RKT comes from the move set ```<RK,T*>``` on n^4^ puzzles (in the old notation, the Inside and Outside cells were called Top and Kata). In the new notation it should be called ROI, but the old name stuck.

!!! quote "Grant"
    Also it's the part of the solve where you can get ReKT

## Doing moves with RKT (n^4^)

RKT lets us do any n^3^ sequence of moves on one side of an n^4^. The beginner's way to learn this is by "translating" 3D algorithms into RKT (although this is not the best way to think about how RKT works beacuse you can really perform any sequence of moves). Below is a simple 3 step guide to translate your algorithms into RKT.

!!! example inline end "Example: Sune algorithm with RKT"
    Say you want to do the Sune algorithm ```R U R' U R U2 R'``` with RKT. The first step is to try and think of how you can execute the algorithm using only R moves and cube rotations. ```R U R' U R U2 R'``` becomes ```R z R z' R' z R z' R z R2 z' R'```. Now we replace R with RO, and cube rotations with I cell rotations: ```RO IF RO IF' RO' IF RO IF' RO IF RO2 IF' RO'``` 
    
    ![Sune with RKT](/assets/images/SuneRKTgif.gif){width="100%"}
1. Rewrite the algorithm to only use cube rotations and R moves
2. Rewrite cube rotations in this new algorithm (`x`, `y`, or `z`) to their respective I cell rotation (`IR`, `IU`, `IF`)
3. Replace all R moves with their RO counterpart

This can definitely be very confusing and disorienting to beginners, as you have to think about 3x3x3 moves with only R moves and rotations. It takes a lot of practice to get comfortable with RKT, but it is an **extremely** powerful technique.

The best way to learn RKT before doing your first 3^4^ solve is by manually scrambling the last cell using any RO moves and random I cell rotations until it looks scrambled. Then practice doing [PLC](/methods/3x3x3x3/cfop#rkt-plc) by solving it with RKT.


!!! tip
    Even though this technique is called RKT, it is not limited to those types of turns. Thus, you can use LO and I- moves instead, or rotate your view and use RU and D- instead of RK and I-.

Another popular way to do RKT is to use wide O cell turns (instead of normal I cell turns). This has the benefit of keeping the cell you're doing RKT to in the same orientation the entire time. Instead of rotating a side of the I cell to the RI plane, you rotate all the outside layers over the side that you're twisting.

## Parity

!!! warning inline end "RKT Parity"
    ![RKT parity on the last layer of the last cell of a 3x3x3x3](/assets/images/RKT_parity_3333.png)

RKT parity is a state you can get to that appears to rotate a single layer of a cell by 180°. 
If you try and fix this with RKT, then the outer layers will be off by 180°. This means that you must use an algorithm (or intuition) to solve it.

You can use a 3D supercube algorithm that rotates the U center 180° (`5x(R U R' U)`, or `2x(L R U2 R' L' U)`).

Harder to memorize (but much lower in movecount) is this 9-mover RKT parity alg:
`IU UR IU' IF' UO' IF RF UR RF' UIR`, found by Tetrian22.

- [3^4^ Commutators List by Alvin (RKT parity algs are near the bottom)](https://docs.google.com/spreadsheets/d/1fCAhsGl0Ttf7B_ncS8m2Mq_TkPZX2VCaFw23XGSzAKo/edit#gid=0)
- [PLL + RKT parity algs by Eff](https://docs.google.com/spreadsheets/d/1oHNpWKSnR0p6PMiwQT5IciE2f7Wmw2cC-Kfol0XrzG4/edit)

On 2^4^, the algorithm is shorter because it doesn't have to worry about messing up other pieces besides corners. A commonly used one is ```R2 B2 R2 U R2 B2 R2 U'```<sub>RKT</sub>.

On bigger n^4^ puzzles (where $n>3$), it can look like a single _slice_ layer of a cell is off by 180°. An intuitive way to solve this is to do the 2^4^ RKT parity algorithm with wide moves, and then the normal 3^4^ RKT parity algorithm. It can also be avoided by just lining up your slice the same way you line up centers in 3D before finishing last 4 edges (when using freeslice).

```[f' r': [[r' U' l': D2], Iy2]]```(swaps UF and UR) 

## Debt

RKT Debt is when the R cell isn't aligned with the rest of the puzzle aftering performing an algorithm or sequence of moves with RKT. For example: after executing a T perm algorithm with RKT the R cell will be misaligned by 90°. RKT Debt always has to be "paid back" at some point during the solve. During complicated setup moves for fancy inserts, RKT debt can be used as "ammo". That is, undoing the debt in a useful way to help solve the puzzle. An easy way for beginners to "avoid" debt is to just do a move on a layer that you don't care about messing up at that point in the solve. For example: in a [CFOP](/methods/3x3x3x3/CFOP) solve during the final F2L-b pair insertion, you could do any U* move that fixes the debt.

## Cancels

!!! example "Sune with RKT: left = normal RKT, right = RKT cancel"
    ![Sune with RKT](/assets/images/SuneRKTcancel.gif){width="100%"}

RKT cancelling is a technique that reduces the move count of certain RKT algorithms and triggers by abusing symmetry of rotations. HactarCE made a program called [RocKeT](https://github.com/HactarCE/rocket) to find cancels for 3^4^ algorithms. Often, it just involves inserting some flipping moves at certain points throughout the algorithm.

Consider `R U R' U'`. Conventional RKT rotates after every move, but we don't have to do that. We can build up multiple moves of RKT debt and then cancel them later:

- `RO UO` — do `R U` using RKT, building up two moves of RKT debt (`R U`)
- `IF RO'` — do `R'` using RKT, undoing the debt from `U`
- `IF2 UO'` — do  `U'` using RKT, undoing the debt from the `R`

But we can do even better!

- `RO UO` — do `R U` using RKT
- `IUR` — swap `R` with `U`
- `UO' RO'` — do `R' U'` using RKT (because we swapped `R` and `U`), undoing the debt from `R U`

If you squint, you might notice that this is a conjugate `[RO UO: IUR]`. This corresponds to the fact that `R U R' U'` can be written as a conjugate where one part is a pure rotation: `[R U: z x2]`. When executing this algorithm, we apply it to `I` _with_ the rotation (so it's equivalent to `R U R' U'`) and to the outer layers _without_ the rotation (so `[RU: _]` expands to `R U U' R'`, which completely cancels out). This is the fundamental theory behind how to do RKT cancels: by rewriting algorithms as conjugates and commutators with pure rotations.

Recall how in 3D you can replace a `U y'` with `Dw`. We can do the same thing here: replace `IUR` with `{1-2}OUR`, which is a rotation of the outer layers instead of the inner layers. Now it just looks like a normal algorithm with a flip thrown in the middle: `RO UO {1-2}OUR RO' UO'`. So we can notate it a little more simply: `R U {1-2}OUR R' U'`

Here's a more complex example, the Sune algorithm: `RO UO RO' {1-2}OUR UO RO {1-2}OUR UO2 RO'`. This works because you can rewrite Sune using conjugates with rotations: `[R U: [R': z x2] [U: z x2]]`. Notice how if you remove the rotations, the whole thing cancels out. (You don't need to expand the conjugates to see this.)

- For a list of algs, see the [RKT Cancel Algs](/rkt_cancel_algs) page

## Simultaneous RKT

RKT can be done by using 2 opposite sides (e.g. `RO` and `LO` turns) as well as normal I cell turns. This would allow you to execute `<R,U,L>` gen algorithms easier, at the cost of having to fix RKT debt on both layers. Another interesting way to do this is in a method like Belt Method. After solving the belt, orienting opposite sides, and separating the colours, the user is left with solving 2 opposite cells that can be solved simultaneously using RKT. If you turn one of the sides with the belt going through it, it essentially does a twist to both cells. One case that can be annoying is if you want to do a 180° turn on one side, and a 90° turn on the other (you would have to wait until both cells' debt lined up).

## Higher Dimensional RKT

The term Double/Triple/Quadruple/etc... RKT is used to refer to *using* RKT to *do* RKT in 5D+ puzzles. Because RKT lets us treat a single side of an n^d^ like an n^d-1^, using RKT on the 3^5^ lets us treat a single 4D cell as a 3^4^. And if you know how to use RKT to treat a 3^4^ like a 3^3^, then you can do Double RKT. This generalizes to any number of dimensions, but the movecount doubles each time, making it impractical. This is why bigger n^d^ puzzles are mostly solved using [commutators](/techniques/commutators).

## RKT in 3D

If RKT treats a single layer of an n^d^ puzzle like an n^d-1^ puzzle, then technically the last step of the 3^3^ [Roux method](https://www.speedsolving.com/wiki/index.php?title=Roux_method) counts as RKT. The last step of Roux is to permute the M-slice like a 3^2^ (with mirroring moves allowed).

Another thing that "feels like RKT" is solving 3x3xn cuboids where $n>3$. A typical strategy for these is to solve from the innermost layers to the outermost layers, treating it as several nested 3x3x2 puzzles. Doing an R2 on the whole puzzle does an R2 to each of the subpuzzles.




