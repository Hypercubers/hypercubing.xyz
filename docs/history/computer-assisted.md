# Computer-Assisted Solving

This page documents the history of automated solvers and computer-assisted fewest-moves records for high-dimensional twisty puzzles.

On this page, the "contributors" column in the table includes the following:

- authors of puzzle-solving software used during the solving process
- anyone who contributed directly to the individual solve

Other contributions (e.g., algorithmic and solving-method innovations) are noted as well in the extended descriptions, but not listed in the tables.

[MagicCubeNdSolve]: https://www.plunk.org/~hatch/MagicCubeNdSolve/
[Hypersolve]: https://github.com/ajtaurence/Hypersolve/
[robodoan]: https://github.com/HactarCE/robodoan/
[Cube Explorer]: https://kociemba.org/cube.htm
[Flat Hypercube]: https://github.com/milojacquet/flat-hypercube/

[^kociemba]: Herbert Kociemba authored [Cube Explorer], used to find optimal or near-optimal 3^3^ solutions.

## 3^4

### Shortest solutions

| Date       | Move count + log file link        | Contributors                                            |
| ---------- | --------------------------------- | ------------------------------------------------------- |
| 2021-07-29 | [195 STM (204 MC4DTM)][doan-34-1] | Charles Doan, Herbert Kociemba[^kociemba]               |
| 2021-07-30 | [188 STM (194 MC4DTM)][doan-34-2] | Charles Doan, Herbert Kociemba[^kociemba]               |
| 2025-09-24 | [125 STM][farkas-34-1]            | Andrew Farkas, Luna Harran, Herbert Kociemba[^kociemba] |
| 2025-09-24 | [122 STM][farkas-34-2]            | Andrew Farkas, Luna Harran, Herbert Kociemba[^kociemba] |

[doan-34-1]: https://assets.hypercubing.xyz/solves/3x3x3x3/[3^4]_ShortAttempt11.log
[doan-34-2]: https://assets.hypercubing.xyz/solves/3x3x3x3/[3^4]_ShortAttempt12.log
[farkas-34-1]: https://assets.hypercubing.xyz/solves/3x3x3x3/2025-09-24_computer_assisted_fmc_wr_125stm_andrew_farkas_and_luna_harran.hsc
[farkas-34-2]: https://assets.hypercubing.xyz/solves/3x3x3x3/2025-09-24_computer_assisted_fmc_wr_122stm_andrew_farkas_and_luna_harran.hsc

### History

#### 2021

The earliest computer-assisted 3^4^ solve with surviving evidence is 195 STM[^195-rescored], submitted by Charles Doan on 2021-07-29 via email to Melinda Green.

[^195-rescored]: The solve was originally scored as 201 moves using MC4DTM, the standard at the time. Later it was rescored as 195 STM. The email mentions an earlier[^earlier-solves] solve as well, but the log file for that one has been lost to time.

!!! quote "Email submission from Charles Doan to Melinda Green"

    Hello Melinda,

    Recently, I have optimized my Computer-Assisted shortest solution (204 twists) to 201[^195-rescored] twists.

    The log file is attached below.

    Thanks!

    Charles Doan

    [[3^4]_ShortAttempt11.log][doan-34-1]

[^earlier-solves]: The filename convention suggests that there were 10 earlier attempts. We do not have log files or move count information for any of them, except that the 10th seems to have been 204 MC4DTM.

The next day, on 2021-07-30, Charles improved the solve to 188 STM.

Both solves used the following method (move counts from the 188 STM solve):

1. Blockbuilding F2L, unassisted (114 STM)
2. OLC, unassisted (38 STM)
3. 2c PLC skip (0 STM)
4. RKT PLC, using an efficient 3^3^ solution found using [Cube Explorer] (36 STM)

Incredibly, a few months later, on 2021-11-13, Charles [tied his own computer-assisted solve without any computer assistance](https://lb.hypercubing.xyz/solve?id=939)[^tied].

[^tied]: At the time, the solves were measured using MC4DTM rather than STM, in which the unassisted solve actually scored 4 moves _better_ (191 STM unassisted compared to 195 STM computer-assisted).

#### 2025

On 2025-09-24, Hactar and Luna Harran completed a 125 STM solve using [robodoan](#robodoan). The methodology is described in the email submission.

!!! quote "Email submission from Hactar to the Hypercubing Google Group"

    For the last couple weeks I've been working on [robodoan], an automated solver for 3^4 using incremental blockbuilding. Although it can't yet do a full solve, it's able to reliably compute a 60-75 STM solution to the first two layers in under 10 seconds on my laptop. For comparison, the previous shortest solution by Charles Doan (188 STM) completed F2L in 114 STM. It \[robodoan] works by pairing blocks one at a time, brute-force searching ahead by up to 5 moves (usually ≤3) to pair blocks using some heuristics. To get short solutions, it tracks up to ~10,000 possible solutions at once and picks the best ones at each step. See [the README](https://github.com/HactarCE/robodoan?tab=readme-ov-file#robodoan) for more details.

    Attached is a 125 STM solve Luna Harran and I did in 4 stages:

    1. **F2L (63 STM, automatic)** - We generated 5 scrambles using MC4D, loaded them into robodoan, and manually reviewed several of the generated solutions. The shortest F2L solution was 61 STM, but it had a poor OLC. We found one that was 63 STM and had a decent OLC (orient last cell).
    2. **OLC (21 STM, manual)** - We solved OLC using 2 algorithm executions, including a [slice RKT-canceled](/docs/techniques/rkt.md#cancels) fat sune and a 6-move 4D OLC algorithm.
    3. **2cPLC (8 STM, manual)** - We solved 2cPLC (permute last cell) using an [adjacent 3-cycle](/docs/methods/3x3x3x3/cfop.md#2c-pll-4) that canceled into the last OLC algorithm.
    4. **PLC (33 STM, computer-assisted)** - We entered the final cube state into [Cube Explorer] to get a 3D solution and then manually found a decent RKT-cancel for it.

    \[...]

    I'd like to thank Luna Harran for her help with teaching me the [grip-theoretic foundations of blockbuilding](/docs/theory/grip-theory/index.md) and with tuning the search parameters.

## 2^4

### Shortest solutions

| Date       | Move count          | Contributors      |
| ---------- | ------------------- | ----------------- |
| 2023-06-10 | [19][taurence-24-1] | Anderson Taurence |

[taurence-24-1]: https://assets.hypercubing.xyz/solves/2x2x2x2/hypersolve_random_state.hsc

### History

#### 2023

On 2023-06-10, Anderson Taurence, author of [Hypersolve](#hypersolve), posted a 19-move solution to a random-state scramble found using Hypersolve in "only a few minutes" to the Hypercubers Discord server.

## Software

### Cube Explorer

[Cube Explorer] is a Pascal program that finds a complete solution to a 3^3^ puzzle. It uses a 2-phase method, where each phase is solved using [IDS] with pruning tables. For a full scramble, it typically finds a solution of 18-21 moves within a few seconds on modern hardware. The first version was written by Herbert Kociemba at least as early as 2001[^cube-explorer-2001], although an early implementation of the 2-phase algorithm probably dates back to 1995[^cube-explorer-1995] at the latest.

[^cube-explorer-2001]: https://github.com/hkociemba/CubeExplorer/blob/master/readme.txt
[^cube-explorer-1995]: https://cube20.org/

### MagicCubeNdSolve

[MagicCubeNdSolve] is a Java program that finds complete solutions to _any_ n^d puzzle. It solves each piece type individually, first permuting and then orienting pieces. It runs very quickly (<0.1 seconds for 3^4^ on modern hardware) but produces relatively long solutions. It was written by Don Hatch circa 2006[^mcnds-2006]. It takes input as a [Flat Hypercube]-style projection and outputs moves using a generic 3-letter notation.

[^mcnds-2006]: The source code and web page both have a last-modified date of June 8, 2006. It's possible the program was written earlier.

As far as we know, MagicCubeNdSolve is the first computer program to automatically solve a 4D+ twisty puzzle, and as of 2026 it is the only computer program capable of generating a complete solution to a 4D+ twisty puzzle other than 2^4^.

??? example
    Sample input, generated using Flat Hypercube:

    ```
             U B F      D D F      L F F
             L L I      L R D      F B I
             F I D      D U I      D B B

             R O I      R R D      U O O
    F R D  O       L  I       O  I       L  F R D
    B B R  I       B  O       F  L       L  I D D
    I R I  U       L  O       U  I       U  R D R
             R U B      R I B      B L I

             D L L      R B R      D I R
    B F B  O       U  U       F  F       U  I F F
    L O B  I       O  U       D  O       O  U I R
    I L O  U       L  U       I  R       L  B O U
             F D D      L F R      D F O

             U L O      B B U      F D B
    L F R  B       B  U       O  I       I  D L U
    U R O  I       B  I       O  L       I  U B R
    O O B  L       R  I       D  B       F  O U R
             U U U      D F R      D B D

             O O D      R U R      R F L
             L B L      D L D      F I F
             F F O      B U F      L O O
    ```

    Sample output (word-wrapped):
    ```
    n = 3
    d = 4
        Figuring out where cubies want to be... done.
        Checking for inside-outedness of corner cubies... 0/16 corners inside-out.
        Checking permutation parity on 2-sticker cubies... odd; applying one twist
        Checking permutation parity on 2-sticker cubies... even.
        Checking flip parity on 2-sticker cubies... even.
        Checking permutation parity on 3-sticker cubies... even.
        Checking flip parity on 3-sticker cubies... even.
        Checking permutation parity on 4-sticker cubies... even.
        Checking twirl parity on 4-sticker cubies... zero mod 3.
        Puzzle is solvable.

        It's odd, applying one twist to fix parity...                 0.006 secs
        Positioning 2-sticker cubies...   + 176 = 177 moves  + 0.002 = 0.008 secs
            applying...        done.                          + 0.006 = 0.014 secs
        Orienting 2-sticker cubies...     + 144 = 321 moves  + 0.001 = 0.015 secs
            applying...        done.                          + 0.003 = 0.018 secs
        Positioning 3-sticker cubies...   + 268 = 589 moves  + 0.001 = 0.019 secs
            applying...        done.                          + 0.002 = 0.021 secs
        Orienting 3-sticker cubies...     + 440 = 1029 moves  + 0.001 = 0.022 secs
            applying...        done.                          + 0.003 = 0.025 secs
        Positioning 4-sticker cubies...   + 176 = 1205 moves  + 0.0 = 0.025 secs
            applying...        done.                          + 0.002 = 0.027 secs
        Orienting 4-sticker cubies...     + 650 = 1855 moves  + 0.001 = 0.028 secs
            applying...        done.                          + 0.002 = 0.03 secs
    Solution = "LBO DRB DRB LBU DBR DBR FUR BRO BRO LBO LBO BRO BRO LBO LBO FRU
    DRB DRB LUB DBR DBR IRB IRB LBO DBR DBR FUR BRO BRO LBO LBO BRO BRO LBO LBO
    FRU DRB DRB LOB IBR IBR IRU LOB RBO RBO FRO FRO RBO RBO FRO FRO LBO IUR ORU
    LOB BRO BRO LBO LBO BRO BRO LBO LBO LBO OUR FRU LBO LBO URB FRU BRO BRO LBO
    LBO BRO BRO LBO LBO FUR UBR LOB LOB FUR IUR LBO OBR FRO BRO BRO LBO LBO BRO
    BRO LBO LBO FOR ORB LOB IRU IBR IBR FOR BRO BRO LBO LBO BRO BRO LBO LBO FRO
    IRB IRB FOR LBO LBO FRO FRO BRO BRO LBO LBO BRO BRO LBO LBO FOR FOR LOB LOB
    FRO LBU OUB FRO BRO BRO LBO LBO BRO BRO LBO LBO FOR OBU LUB ORB LOB ORB FRO
    BRO BRO LBO LBO BRO BRO LBO LBO FOR OBR LBO OBR LOU BUR BUR DRB URB URB LUB
    LUB URB URB LUB LUB DBR BRU BRU LUO IRB IRB LOU RUB FUR FUR DRB UBR LBU LBU
    DRB DRB LUB DRB LBU DRB LBU LBU URB FRU DBR FRU RBU LUO IBR IBR BRU LBO LBO
    RBO IBR IBR FRO BOR LOB LOB FRO FRO LBO FRO LOB FRO LOB LOB BRO IRB FOR IRB
    ROB LOB LOB BUR OBU FUO BUR LUB LUB DBR URB FRU FRU DBR DBR FUR DBR FRU DBR
    FRU FRU UBR LBU DRB LBU BRU FOU OUB OUR LUO LUO DOR URO IRU IRU DOR DOR IUR
    DOR IRU DOR IRU IRU UOR LOU DRO LOU ORU BRO FOR LBO LBO IRB OBR BRO BRO IRB
    IRB BOR IRB BRO IRB BRO BRO ORB LOB IBR LOB FRO BOR FRO FRO RBO LOB FRO FRO
    IBR ORB RBO RBO IBR IBR ROB IBR RBO IBR RBO RBO OBR FOR IRB FOR LBO ROB FOR
    FOR DRB LBU IBR FRO FRO OBR ROB ORB LOB OBR RBO ORB LBO FOR FOR IRB LUB DBR
    LOB IBR FRU FOR OBR ROB ORB LOB OBR RBO ORB LBO FRO FUR IRB LBO URO LUB FUR
    FOR OBR ROB ORB LOB OBR RBO ORB LBO FRO FRU LBU UOR LBO FRU FOR OBR ROB ORB
    LOB OBR RBO ORB LBO FRO FUR LOB FRU LUO LOB FUO FRO OBR ROB ORB LOB OBR RBO
    ORB LBO FOR FOU LBO LOU FUR LUO LOB DRB FOU OBR ROB ORB LOB OBR RBO ORB LBO
    FUO DBR LBO LOU DRO LBU IRB FUR FOR OBR ROB ORB LOB OBR RBO ORB LBO FRO FRU
    IBR LUB DOR LOU LOB IBU FRU FOR OBR ROB ORB LOB OBR RBO ORB LBO FRO FUR IUB
    LBO LUO LOU DBR FOU FRO OBR ROB ORB LOB OBR RBO ORB LBO FOR FUO DRB LUO FRO
    LOU LOB URB FRU OBR ROB ORB LOB OBR RBO ORB LBO FUR UBR LBO LUO FOR LUO DRB
    FOU OBR ROB ORB LOB OBR RBO ORB LBO FUO DBR LOU IRB LBU LBO FRU FOR OBR ROB
    ORB LOB OBR RBO ORB LBO FRO FUR LOB LUB IBR LBU IBR FUR FOR OBR ROB ORB LOB
    OBR RBO ORB LBO FRO FRU IRB LUB FOR LBO LBO FUO FRO OBR ROB ORB LOB OBR RBO
    ORB LBO FOR FOU LOB LOB FRO URB LUB DRB FOU OBR ROB ORB LOB OBR RBO ORB LBO
    FUO DBR LBU UBR ORB LOU ORB FRO FUR UBR RUB URB LUB UBR RBU URB LBU FRU FOR
    OBR LUO OBR ORU LOB LUB LUB FRU BUR LUO LUB LBO BRU ROB ROB BUR LOB LBU LOU
    BRU RBO RBO FUR LBU LBU LBO OUR OUR LOB LBU UBR DRB LOB LBU LOU DBR RUO RUO
    DRB LUO LUB LBO DBR ROU ROU URB LUB LBO ORU FRO LUB LOU LOU DRO UOR LOB LOU
    LUB URO RBU RBU UOR LBU LUO LBO URO RUB RUB DOR LUO LUO LBU FOR DRB BRU BUR
    BUO BUO FRU LOU LUB LOB FUR RBO RBO FRU LBO LBU LUO FUR ROB ROB BOU BOU BRU
    BUR DBR IBR LOU LUB URB DBR LBO LUB LOU DRB RUO RUO DBR LUO LBU LOB DRB ROU
    ROU UBR LBU LUO IRB BRO LBO LBO RBO BOU BOR BRU ROB FUR FUR RBO BUR BRO BUO
    ROB FRU FRU LOB LOB BOR BRO LOB LOU LUO URO URO UOB UOB DRO OBR ORU OBU DOR
    IUB IUB DRO OUB OUR ORB DOR IBU IBU UBO UBO UOR UOR LOU LUO LBO BOR DOB IBU
    OBU FRU FOU FOR OUB BRO BRO OBU FRO FUO FUR OUB BOR BOR IUB DBO DOB FUO BUO
    ORU OBU OBR BOU IRB IRB BUO ORB OUB OUR BOU IBR IBR FOU DBO FOU FOU DBO UOB
    FOR FOU FUR UBO BRU BRU UOB FRU FUO FRO UBO BUR BUR DOB FUO FUO IUB IUR IUR
    OBU BUR BUO BOR OUB FRO FRO OBU BRO BOU BRU OUB FOR FOR IRU IRU IBU BUR BOU
    FUO ORU OUB ORB FOU IBR IBR FUO OBR OBU OUR FOU IRB IRB BUO BRU DRB FUR FRU
    FUO FUO BUR ROU RBU RBO BRU LOB LOB BUR ROB RUB RUO BRU LBO LBO FOU FOU FUR
    FRU DBR IBR RUO RUB DRB URB FRO FRU FUO UBR BOU BOU URB FOU FUR FOR UBR BUO
    BUO DBR RBU ROU IRB OUR RUB ROB RBO ORB ORB OBU OBU IRB FRU FOR FUO IBR BOU
    BOU IRB FOU FRO FUR IBR BUO BUO OUB OUB OBR OBR ROB RBO RBU ORU DRO DOB DOB
    URO IRB IRU IUB UOR OBU OBU URO IBU IUR IBR UOR OUB OUB DBO DBO DOR DOR DOB
    DOB UOR ORB ORU OUB URO IBU IBU UOR OBU OUR OBR URO IUB IUB DBO DBO DRO FUR
    RBO ROU ROU OUR IUR URB UOR UBO IRU DOB DOB IUR UOB URO UBR IRU DBO DBO ORU
    RUO RUO ROB FRU IRB ROU RUB UBR DRB RBO RUB ROU DBR LUO LUO DRB RUO RBU ROB
    DBR LOU LOU URB RBU RUO IBR OBR BRO FOR ORU OBR OUB FRO IBU IBU FOR OBU ORB
    OUR FRO IUB IUB BOR ORB LOU LOU URO LUO UOR RUO URO LOU UOR ROU BOR RUO URO
    LUO UOR ROU URO LOU UOR BRO LUO LUO LUB ORU LOU OUR ROU ORU LUO OUR RUO BUR
    ROU ORU LOU OUR RUO ORU LUO OUR BRU LBU LOB FRO UBR FUR URB BUR UBR FRU URB
    BRU ORB BUR UBR FUR URB BRU UBR FRU URB OBR FOR LBO LOU LOU FRO FRO UBR FUR
    URB BUR UBR FRU URB BRU ORB BUR UBR FUR URB BRU UBR FRU URB OBR FOR FOR LUO
    LUO LBO LBO LBU FUR UBR FUR URB BUR UBR FRU URB BRU ORB BUR UBR FUR URB BRU
    UBR FRU URB OBR FRU LUB LOB LOB LBU LBU IRB FOU FOU UBR FUR URB BUR UBR FRU
    URB BRU ORB BUR UBR FUR URB BRU UBR FRU URB OBR FUO FUO IBR LUB LUB FRO LBU
    LBU IBR FRO FRO FUR UBR FUR URB BUR UBR FRU URB BRU ORB BUR UBR FUR URB BRU
    UBR FRU URB OBR FRU FOR FOR IRB LUB LUB FOR DRB LBU LOB LBU LOB LOB LBU RUB
    DRB DRB RBU BUR DRB DRB BRU UBR BUR DRB DRB BRU RUB DRB DRB RBU URB ORB OUB
    UBR RUB DBR DBR RBU BUR DBR DBR BRU URB BUR DBR DBR BRU RUB DBR DBR RBU OBU
    OBR LUB LBO LBO LUB LBO LUB DBR IRB LBO LBU LBO LUB LUB LBO RBO FRO FRO ROB
    OBR FRO FRO ORB BOR OBR FRO FRO ORB RBO FRO FRO ROB BRO DRB DOB BOR RBO FOR
    FOR ROB OBR FOR FOR ORB BRO OBR FOR FOR ORB RBO FOR FOR ROB DBO DBR LOB LBU
    LBU LOB LUB LOB IBR IRB BRO BUO BRU BRU FUR DRB DRB FRU RBU DRB DRB RUB UBR
    RBU DRB DRB RUB FUR DRB DRB FRU URB ORB OUR UBR FUR DBR DBR FRU RBU DBR DBR
    RUB URB RBU DBR DBR RUB FUR DBR DBR FRU ORU OBR BUR BUR BOU BOR IBR DRB BRU
    BOU BRO BUO BUO BOR FOR LBO LBO FRO IBR LBO LBO IRB ROB IBR LBO LBO IRB FOR
    LBO LBO FRO RBO URB URO ROB FOR LOB LOB FRO IBR LOB LOB IRB RBO IBR LOB LOB
    IRB FOR LOB LOB FRO UOR UBR BRO BOU BOU BOR BUO BUR DBR DBR FRU FUO BOU DOB
    DOB BUO IUB DOB DOB IBU UBO IUB DOB DOB IBU BOU DOB DOB BUO UOB ROB ROU UBO
    BOU DBO DBO BUO IUB DBO DBO IBU UOB IUB DBO DBO IBU BOU DBO DBO BUO RUO RBO
    FOU FUR DRB FOR LBO LUO LBO LUO LUO LOB ROB FOR FOR RBO IBR FOR FOR IRB BRO
    IBR FOR FOR IRB ROB FOR FOR RBO BOR DRB DBO BRO ROB FRO FRO RBO IBR FRO FRO
    IRB BOR IBR FRO FRO IRB ROB FRO FRO RBO DOB DBR LBO LOU LOU LOB LOU LOB FRO
    IBR ROU ROU RBO LBO FOR FOR LOB ORB FOR FOR OBR BRO ORB FOR FOR OBR LBO FOR
    FOR LOB BOR DBR DOB BRO LBO FRO FRO LOB ORB FRO FRO OBR BOR ORB FRO FRO OBR
    LBO FRO FRO LOB DBO DRB ROB RUO RUO IRB DRB FUR FRU FRO FUR FUR FRO BRO ROB
    ROB BOR IBR ROB ROB IRB LBO IBR ROB ROB IRB BRO ROB ROB BOR LOB URB UOR LBO
    BRO RBO RBO BOR IBR RBO RBO IRB LOB IBR RBO RBO IRB BRO RBO RBO BOR URO UBR
    FOR FRU FRU FOR FUR FRU DBR OBR ROU ROU ROB FOR FUO FRO FUR FUR FRO BRO ROB
    ROB BOR IBR ROB ROB IRB LBO IBR ROB ROB IRB BRO ROB ROB BOR LOB DRB DOR LBO
    BRO RBO RBO BOR IBR RBO RBO IRB LOB IBR RBO RBO IRB BRO RBO RBO BOR DRO DBR
    FOR FRU FRU FOR FOU FRO RBO RUO RUO ORB DOB UBO IBU IBU UOB FOU IBU IBU FUO
    OUB FOU IBU IBU FUO UBO IBU IBU UOB OBU LBU LBO OUB UBO IUB IUB UOB FOU IUB
    IUB FUO OBU FOU IUB IUB FUO UBO IUB IUB UOB LOB LUB DBO UBR UBO UOB DBO IUB
    IUB DOB FUO IUB IUB FOU OBU FUO IUB IUB FOU DBO IUB IUB DOB OUB LUB LBO OBU
    DBO IBU IBU DOB FUO IBU IBU FOU OUB FUO IBU IBU FOU DBO IBU IBU DOB LOB LBU
    UBO UOB URB IBU IUR IUR ORU DRO DRO OUR LUO DRO DRO LOU UOR LUO DRO DRO LOU
    ORU DRO DRO OUR URO FRO FRU UOR ORU DOR DOR OUR LUO DOR DOR LOU URO LUO DOR
    DOR LOU ORU DOR DOR OUR FUR FOR IRU IRU IUB ORB IRB ROB ROB IBR FRO ROB ROB
    FOR LBO FRO ROB ROB FOR IRB ROB ROB IBR LOB DOR DBR LBO IRB RBO RBO IBR FRO
    RBO RBO FOR LOB FRO RBO RBO FOR IRB RBO RBO IBR DRB DRO OBR"
    ```

### Hypersolve

[Hypersolve] is a Rust program that finds complete solutions to 2^4^ using a 3-phase method, where each phase is solved using [IDS] with pruning tables. For a full scramble, it typically finds a solution of 21-24 within a few seconds on modern hardware. Hypersolve was originally written in Python, but was rewritten in Rust to improve performance. Both versions were written by Anderson Taurence; the Rust version was primarily completed from March to June 2023.

The three solve phases are as follows:

[IDS]: https://en.wikipedia.org/wiki/Iterative_deepening_depth-first_search

1. Orientation along axis 1
2. Orientation along axis 2 + separation along axis 1
3. Permutation

For more details, see the (possibly outdated) [documentation from January 2023](https://assets.hypercubing.xyz/2023-01-04_24_Solver_Description.pdf).

### robodoan

[robodoan] is a Rust program that finds solutions to F2L on 3^4^ using incremental blockbuilding via repeated [IDA*]. For a full scramble using the "fast" profile, it typically finds a solution of 68-71 ETM[^robodoan-etm] in ~8 seconds on a MacBook Pro M2 Max; using the "short" profile, 64-67 ETM in ~17 seconds. It written by Hactar with help from Luna Harran in over the course of a few weeks in September 2025.

[^robodoan-etm]: In rare cases robodoan will fail to cancel moves that could be canceled, but typically robodoan ETM = STM.

[IDA*]: https://en.wikipedia.org/wiki/Iterative_deepening_A*
