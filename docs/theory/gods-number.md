# God's Number

**God's number** is the minimum number of moves that is sufficient to solve a twisty puzzle from any starting position. For 3×3×3, this has [been been proven][cube20] to be 20 HTM (or 26 QTM).

God's number for 3^3^ took [lots of creative mathematical work and 35 years of CPU time][cube20] to scan $\sim 4.3 \times 10^{19}$ states. For comparison, the 2^4^ has $\sim 3.4 \times 10^{27}$ states and 4^3^ has $\sim 7.4 \times 10^{45}$ states. **There isn't a single nontrivial 4D puzzle for which God's number is known, let alone remotely possible to compute.**

There are three strategies we can use to estimate it:

1. Setting a **lower bound** using the branching factor of move sequences
2. Setting an **upper bound** by analyzing the worst-case solution of every stage in a given method
3. **Estimation** by measuring move counts produced by a near-optimal solver

[cube20]: http://cube20.org/

## 2×2×2×2

### Lower bound

There are 92 possibilities for the first move and 69 possibilities for each subsequent move.[^24moves] To even have a chance of reaching $4.3 \times 10^{19}$ states, we need at least that many move sequences. $log_{69}(\frac{4.3 \times 10^{19}}{92}) \approx 9.6$, so God's number for 2^4^ is at least 10.

[^24moves]: Only one cell on each axis matters. Each face has 24 orientations, but one of those is the identity and so doesn't matter. $23 \times 4 = 92$. For subsequent moves, must turn a different axis. $23 \times 3 = 69$ (nice)

### Upper bound

Anderson Taurence wrote a [3-stage 2^4^ solver](https://github.com/ajtaurence/Hypersolve) using a method that has a worst case of 39 STM, so God's number for 2^4^ is at most 39.

### Estimate

Anderson's solver typically produces solutions in the range of 20-30 STM. Note that this solver does not produce optimal solutions[^optimal], and we cannot measure _every_ scramble so it's impossible to use this to put a hard bound on God's number, but God's number for 2^4^ is probably not higher than 20-30.

[^optimal]: It does converge on optimal solutions when run for a very long time, but this is impractical for all but the simplest scrambles.

### Conclusion

God's number for 2^4^ is definitely between 10 and 39 inclusive, and probably $\sim 15 \pm 5$*

!!! question "Could this be improved?"

    - A better method or lots of compute time might improve slightly on the upper bound
    - Unless there is some fundamental breakthrough in our understanding of computation, there's basically no way to improve on the lower bound or estimate.

    If you're an expert in quantum computing then perhaps you can devise some clever quantum algorithm to help, but as of 2023 quantum computers haven't solved a single real-world problem faster than a classical computer so we remain skeptical.

## 3×3×3×3

### Lower bound

We have not yet formally computed a lower bound on God's number for 3^4^ in STM or OBTM. It's somewhere around 55 moves.^\[citation\ needed]^

Note that we can get a slightly better-than-naïve estimate by accounting for commuting moves.

### Upper bound

HactarCE computed a generous upper bound of 570 STM using CFOP.

??? abstract "Step-by-step breakdown"

    - cross: 6 pieces x 4 STM per piece = **24 STM**
    - F2L-a: 12 pairs x 13 STM per pair = **156 STM**
        - 3 STM to put corner on I (with corner first-cell color not on I)
        - 3 STM to put edge on I
        - 3 STM to pair + 2 STM to fix RKT debt
        - 4 STM to insert
    - F2L-b: 8 pairs x 26 STM per pair = **208 STM**
        - 6 STM to put corner on I (with corner first-cell color not on I)
        - 6 STM to put edge on I
        - 4 RKT = 7 STM to pair them and fix RKT debt
        - 7 STM to insert
    - ridge OLC: worst case (all ridges bad) is **17 STM**
    - edge OLC:
        - solve at least 3/4 pieces in each slice using [OCLL]: 3 slices x 11 STM = **33 STM**
        - worst case is 3 unsolved edges remaining: 5 RKT + 9 STM = **18 STM**
            - 2 RKT to arrange any two edges so that they are adjacent in the same slice but do not form a valid 2-corner OLL case
            - 2 RKT to place the last edge in a way that forms a valid 3-corner OLL case
            - 1 RKT to fix RKT debt
            - 9 STM to solve the OLL case (consider OCLLs with at least one corner solved)
    - corner OLC: **58 STM**
        - 11 RKT = 23 STM to solve a 2^3 into a state where the D and U layer each contains a valid 3-corner OLC case
            - if there is exactly one remaining corner unsolved, then misorient two corners when solving one of those 3-corner OLC cases.
            - if there are exactly two remaining corners unsolved, then misorient one corner when solving one of the 3-corner OLC cases.
            - arrange the cases so that the 3 unsolved corners left will form a sune
        - 13 STM to solve each OLL case on U/D using RKT cancels (worst case is double antisune)
        - 9 STM to solve the remaining sune case
    - ridge PLC: **14 STM** (2× U perm in the worst case)
    - PLC: **42 STM**
        - solve a 3^3 using God's algorithm in 20 moves
        - adjust I cell to solve

[OCLL]: https://www.speedsolving.com/wiki/index.php?title=OLL#All_edges_flipped_correctly

## Estimate

We do not have a near-optimal 3^4^ solver. Good FMC speedsolves average 200 STM, so God's number is probably lower than that.

## Conclusion

God's number for 3^4^ is definitely between 55 and 570 inclusive, and probably $\sim 125 \pm 50$^\[citation\ needed]^.

!!! question "Could this be improved?"

    - A better method could easily improve the upper bound, probably to around 300^\[citation\ needed]^.
    - A better manual computation could give a slightly better lower bound.
    - An automated 3^4^ solver or search program could give a much better estimate.
