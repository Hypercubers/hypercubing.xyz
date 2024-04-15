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

God's number for 2^4^ is definitely between 10 and 39 inclusive, and probably $\sim 15 \pm 5$.

!!! question "Could this be improved?"

    - A better method or lots of compute time might improve slightly on the upper bound
    - Unless there is some fundamental breakthrough in our understanding of computation, there's basically no way to improve on the lower bound or estimate.

    If you're an expert in quantum computing then perhaps you can devise some clever quantum algorithm to help, but as of 2023 quantum computers haven't solved a single real-world problem faster than a classical computer so we remain skeptical.

## 3×3×3×3

### Lower bound

We can compute a lower bound of 56 in the OBTM. This begins by showing that algorithms of limited length can generate, at most, only a subset of the possible positions on the 3^4^. We then optimize the argument by showing that some positions were over counted.

??? abstract "Lower Bound, Winning Ways Method"

	Moves here will be measured using something equivalent (as far as this discussion is concerned) to OBTM. Our focus here is on positions that can be reached by algorithms of a certain length. Wide moves contribute to algorithm length in the same way that single cell turns do (wide move = single cell move + cube rotation, where cube rotations count as 0 moves), so we will make a simplification by restricting to single cell turns. There are 23 moves on each of the 8 cells, so 184 one move algorithms are possible at any given time.
	
	We know the \(3^4\) can be scrambled in over 1.7 novemtrigintillion ways. When solving, we have 184 choices for the first turn, and 161 (non cancelling) choices for the following turns. The number of positions reachable by 54 turns or fewer is at most
	
	\[1 + 184 \times \sum_{n=0}^{53} 161^n \approx 1.695 \times 10^{119} < 1.757 \times 10^{120}.\]
	
	This shows that there exist positions on the \(3^4\) that require 55 or more turns to solve.

	In the book _Winning_ _Ways_ _for_ _Your_ _Mathematical_ _Plays_ _Vol._ _4_, the authors optimize this argument (as it applies to Rubik's Cube in the half turn metric) by accounting for relations like \(LR = RL\). We can apply a similar optimization for the \(3^4\).
	
	We will refer to the number of possible \(3^4\) positions after \(n\) moves as \(u_n\). It is not too hard to convince ourselves that \(u_1 = 184\). After turning one cell, moving the same cell again is what we might call a ``cancelling move'', since the two moves could have been measured as a single move. So, we have \(161\) non cancelling choices for a second move. We should be able to reduce that \(161\) further by avoiding double counting positions reachable by two algorithms which differ only by the order of commuting elements.
	
	There are different ways that a pair of moves can commute on \(3^4\). One is by the cell turns affecting completely distinct subsets of pieces, which happens when turning _opposite_ cells, like \(OL\ IL = IL\ OL\). This is analogous to the commuting cases on Rubik's Cube as addressed in _Winning Ways_. There is at least one more way, which can involve certain adjacent cell moves. \(OL\ LO = LO\ OL\) is one example. We have not yet reached a description of all commuting cases of this kind. Accounting for these may allow us to further improve the lower bound. For now, we will factor out the commutativities that we _can_ describe, which we will call ``opposite commuting'' moves.

	First, there are \(161-23= 138\) possible non cancelling, _non_ _opposite_ _commuting_ choices for the second move. We'll add the opposite commuting cases separately.
	
	There are four ``flavors'' of opposite commuting cases: I cell moves with O cell moves, R moves with L moves, U moves with D moves, and B moves with F moves. In any of these, choose any one of the 23 moves possible on each cell (order doesn't matter), so there are \(23 \times 23 = 529\) opposite commuting cases of each flavor. Then across the four flavors, we have \(529\times 4 = 2,116\) distinct cases after the second move, when it opposite commuted with the first. So we have that the number of \(3^4\) positions after \(n\) moves is_at_ _most_  \(138u_1 + 2,116 = 27,508\). That is, we can say \(u_2 \leq 27,508\).
	
	As a sanity check, we could note at this point the \(27,508\) positions after two turns is better than the \(184\times 161 = 29,624\) positions we would have estimated without accounting for opposite commutativity of two successive turns here.
	
	To complete the argument, we can derive a recurrence relation (more accurately a recurrence _estimate_) that gives us an upper bound on the size of \(u_{n+2}\) in terms of \(u_n\) and \(u_{n+1}\)
	
	In the case where the \(n+2\)th move will _not_ opposite commute (or cancel) with the \(n+1\)th move, we have \(138u_{n+1}\) possible puzzle states. If the \(n+2\)th move _is_ goinig to opposite commute with the \(n+1\)th move, we might have \(529\times 4 = 2,116\) cases to follow up the \(nth\) move. However, one of those four flavors of opposite commuting cases would have cancelled with the \(n\)th move, so this time we only have \(529 \times 3 = 1,587\) cases to follow the \(n\)th move. This gives us the recurrence estimate \(u_{n+2} \leq 138u_{n+1} + 1,587u_{n}\).
	
	Note that as we have defined it, \(u_n\) is the number of positions accessible by _exactly_ n moves. If we _sum_ the \(u_n\)s from 1 to \(N\), that will gives us (an upper bound on) the number of positions accessible by n moves _or_ _fewer_.
	
	In this case, our recurrence estimate is an order 2 linear recurrence with constant coefficients. There exists a method to derive a general formula for \(u_n\). In the end, we find 
	
	\[u_n = C\lambda_1^n + D\lambda_2^n,\]
	
	where
	
	
	\[
	\begin{array}{c c}
	l_{1}=69+46\sqrt{3}, & l_{2}=69-46\sqrt{3}, \\
	C=\displaystyle \frac{1}{4}\left(-22+13\sqrt{3}\right), & D=\displaystyle \frac{1}{4}\left(-22-13\sqrt{3}\right). \\
	\end{array}
	\]
	
	Finally, the number of positions reachable by 55 turns or fewer is at most

	\[1\ +\ \sum_{n=1}^{55}u_n \approx 3.865 \times 10^{118} < 1.757 \times 10^{120}.\] 

	This shows that there exist positions on the \(3^4\) that require 56 or more turns to solve.
	
	We should address the other side of the inequality,

	\[1.757 \times 10^{120} <1\ +\ \sum_{n=1}^{56}u_n \approx 5.746 \times 10^{120}.\]

	So, the argument as applied here can't necessarily show that there are positions requiring 57 or more turns to solve.
	
### Upper bound

Hactar computed a generous upper bound of 570 STM using CFOP.

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
