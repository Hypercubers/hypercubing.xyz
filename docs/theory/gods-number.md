# God's Number

**God's number** is the minimum number of moves that is sufficient to solve a twisty puzzle from any starting position. For 3×3×3, this has [been been proven][cube20] to be 20 HTM (or 26 QTM).

God's number for 3^3^ took [lots of creative mathematical work and 35 years of CPU time][cube20] to prove $\sim 4.3 \times 10^{19}$ states reachable in 20 moves or less. For comparison, the 2^4^ has $\sim 3.4 \times 10^{27}$ states and 4^3^ has $\sim 7.4 \times 10^{45}$ states. **There isn't a single nontrivial 4D puzzle for which God's number is known, let alone remotely possible to compute.**

There are three strategies we can use to estimate it:

1. Setting a **lower bound** using the branching factor of move sequences
2. Setting an **upper bound** by analyzing the worst-case solution of every stage in a given method
3. **Estimation** by measuring move counts produced by a near-optimal solver

[cube20]: http://cube20.org/

## Known Bounds Summary
| Puzzle | Lower Bound | Upper Bound |
| ------ | ----------- | ----------- |
| 2^4^   | 15 STM      | 37 STM      |
| 3^4^   | 51 STM      | 570 STM     |

## 2×2×2×2

### Lower bound

We can compute a lower bound of 15 in the STM by computing a bound on the number of positions reachable by algorithms of a certain length.

??? abstract "Derivation"

	Moves here will be measured using STM. Our focus here is on positions that can be reached by algorithms of a certain length. Note that on the 2^4^, we consider one piece fixed when counting permutations. There are $\sim 3.4 \times 10^{27}$ positions on the 2^4^.

    One position, the solved position, is reachable without making any moves. There are 23 moves on each of the 4 cells that do not affect the fixed piece, so at most 92 one-move positions are reachable by 1 move. For subsequent moves, there are only 69 non-canceling moves since any move on the same axis as the previous move will cancel. Therefore there are at most $92 \times 69^{k-1}$ reachable by exactly $k$ moves (where $k\ge 1$). Let $P_n$ denote the number of positions reachable in $n$ moves or less. Based on the previous analysis,

    \[P_n \le 1+\sum_{k=1}^n 92 \times 69^{k-1} = \frac{23}{17} (69^n-1)+1.\]

    Let $n_G$ be God's number. By definition, $P_{n_G}$ must be equal to the total number of positions. Combining this with the bound on $P_n$, we find

    \[P_{n_G} = 3.4\times 10^{27} \le \frac{23}{17} (69^{n_G}-1)+1,\]

    which implies $n_G \ge 15$.

### Upper bound

We can compute an upper bound of 37 in the STM by computing the worst-case move count of a known method.

??? abstract "Derivation"

    [Hypersolve](https://github.com/ajtaurence/Hypersolve) uses a method that has a worst-case of 39 STM. Furthermore, it has been shown that all cases with move counts more than 37 STM are avoidable. Therefore God's number is at most 37 STM.

### Estimate

[Hypersolve](https://github.com/ajtaurence/Hypersolve) typically produces solutions in the range of 20-30 STM. Note that this solver does not produce optimal solutions[^optimal], but based on this, God's number for 2^4^ is probably not higher than 20-30.

[^optimal]: It does eventually converge on optimal solutions when run for a sufficient amount of time, but this amount of time is impractical for all but the simplest scrambles.

### Conclusion

God's number for 2^4^ is definitely between 15 and 37 inclusive, and probably around $\sim 20 \pm 5$.

!!! question "Could this be improved?"

    - A better method or lots of compute time might improve slightly on the upper bound. More worst-case scenarios can be checked for avoidability.
    - Unless there is some fundamental breakthrough in our understanding of computation, there's likely no way to improve on the lower bound. If you're an expert in quantum computing then perhaps you can devise some clever quantum algorithm to help, but as of 2023 quantum computers haven't solved a single real-world problem faster than a classical computer so we remain skeptical.

## 3×3×3×3

### Lower bound

We can compute a lower bound of 51 in the STM. This works by showing that algorithms of limited length can generate, at most, only a subset of the possible positions on the 3^4^. We will also demonstrate some known optimizations (often useful for other puzzles), although they do not immediately improve the lower bound in the case of 3^4^.

??? abstract "Lower Bound, _Winning Ways_ Method"

	Turns here are measured in the Slice Turn Metric (STM).

	We can describe turns on the \(3^4\) as happening on one of four axes, and with one of three layers. Each layer can be turned in 23 ways, so we have \(4 \times 3 \times 23 = 276\) turns measured as one move in the STM. After turning a layer, we want subsequent turns to be **noncancelling** (turning the same layer twice can be written as a single move), so we have \(276-23=253\) choices for subsequent turns.

	From here, we can proceed without the Winning Ways improvement, where we find the number of positions reachable by 50 turns or fewer is at most

	\[1 + 276 \times \sum_{k=0}^{49}253^k \approx 1.57 \times 10^{120} < \frac{\left(24!\times 2^{24}\right) \times \left(32! \times 6^{32}\right) \times (16! \times 12^{16})}{48} \approx 1.78 \times 10^{120}.\]

	This shows there are positions on the \(3^4\) which require 51 turns or more to solve.
	In the book _Winning Ways for Your Mathematical Plays Vol. 4_, the authors optimize this argument (as it applies to the Rubik's Cube in the half turn metric) by accounting for relations like \(LR = RL\). We can apply a similar optimization for the \(3^4\).

	We will refer to the set of possible _new_ positions reachable after _exactly_ \(n\) turns as \(T_n\). "New" here means that \(T_n\) does not include positions that were in \(T_{n-1}\). "Exactly" means that positions reachable in more than \(n\) turns are not in \(T_n\). The number of elements in \(T_n\) is \(|T_n|\).

	By the computation from before, there are 276 distinct puzzle states after a single turn. So \(|T_1|=276\). Finding \(|T_2|\) is more complicated. First, we need to setup a more detailed way of describing turning axes.

	A **primary** axis is a line through the core of a puzzle in any of the four cardinal directions. Primary axes have three **layers**, which we might label \(-1,\ 0,\) and \(1\). The white-yellow primary axis' three primary layers would correspond to the yellow cell (\(-y\)), white cell (\(y\)), and the slice between the white and yellow cells. A \textbf{secondary} axis is a line through the center of a facet and any of the pieces in that facet. Importantly, the secondary axis can be described using a single cardinal direction when it is through a ridge piece (the \(90^\circ\) degree cell turns and their doubles). A primary axis, secondary axis, and an angle which we turn by is enough to describe any turn in the STM.

	We have just 253 noncancelling chocies for a second turn. Some of these second turns **commute** with a first turn, which means we will overcount postions reachable by two algorithms differing by the order of commuting turns. Noncancelling commuting pairs of turns can happen in two ways:

	1. The first and second turns happen in the same primary axis and on different layers (for example, \(UO\ \ \{2\}UO' = \{2\}UO'\ \ UO\).\\

	2. The first turn has primary and secondary axes \(a\) and \(b\), while the second turn has primary and secondary axes \(b\) and \(a\)  (for example, \(OL\ LO= LO\ OL\)).

	In describing commuting cases of the first kind, the second turn is one that happens on the same primary axis as the first and on a different layer. There are two other layers, and we can make one of \(23\) turns on that layer. This means that after a single turn is made, \(2\times 23 = 46\) of the following turns may lead to commuting cases of the first kind. However, two of these actually lead to single turn puzzle states (like \(UO\ \{2\}UO = DO\)) which were counted in \(T_1\) and should not be part of \(T_2\). So, only 44 of these turns lead to distinct new puzzle states. This means there are \(\frac{44\times 276}{2}\) distinct new puzzle states reachable by two commuting moves of this first kind.

	Commuting cases of the second kind can only happen if the first turn's secondary axis goes through a ridge piece. There are \(108\) turns like this. The second turn's primary/secondary axes are determined by transposing the first turn's primary/secondary axes, and then can happen in one of three ways on one of three layers. So, we have \(\frac{9\times 108}{2}\) distinct new puzzle states reachable by two commuting moves of this second kind. NOTE: If the first turn is one of the \(276-108= 168\) other turns that cannot be followed by a commuting turn of the second kind, those nine second turns happen on a different primary axis and will neither cancel nor commute.

	Now we can compute an upper bound on \(|T_2|\). There are \(\frac{44\times 276}{2}\) distinct new puzzle states reachable by two commuting moves of the first kind, and \(\frac{9\times 108}{2}\) distinct new puzzle states reachable by two commuting moves of the second kind. There are \(276-23-44-9=200\) noncancelling, noncommuting second turns. In total, we have \(|T_2| \leq \frac{44\times 276}{2} + \frac{9\times 108}{2} + 9\times 168 + 200\times 276 = 63,270\). As mentioned in the "NOTE", following one of the other 168 first moves (with secondary axis \textit{not} through a ridge peice) with one of those nine turns suggested by commuting case of the second kind will never cancel or commute, so we add \(9\times 168\) to complement the "leftovers" that were ignored in the \(\frac{9\times 108}{2}\) term.

	To complete the argument, we can derive a recurrence relation (more accurately a recurrence estimate) that gives an upper bound on the size of \(|T_{n+2}|\) in terms of \(|T_n|\) and \(|T_{n+1}|\).

	In the case where the \(n+2\)th turn will not commute or cancel with the \(n+1\)th turn, we have at most \(9\times 168|T_{n}| + 200\times |T_{n+1}|\) possible puzzle states. In the case where the \(n+2\)th turn \textit{will} commute (but still not cancel) with the \(n+1\)th turn, we have at most \(\left(\frac{44\times 253}{2} + \frac{9\times 108}{2}\right)|T_n|\) possible puzzles states. This gives us the estimate \(|T_{n+2}| \leq 200|T_{n+1}| + 7,582|T_n|.\)

	This is an order 2 linear recurrence estimate with constant coefficients. We can show that

	\[|T_n| \leq A\lambda_1^n + B\lambda_2^n,\]

	where

	\[
	\begin{array}{c c}
	\lambda_{1}=100+\sqrt{17,582}, & \lambda_{2}=100-\sqrt{17,582}, \\
	A=\displaystyle \frac{4,035}{7,582}+\frac{160,704}{3,791}\sqrt{\frac{2}{8,791}}, &
	B=\displaystyle \frac{4,035}{7,582}-\frac{160,704}{3,791}\sqrt{\frac{2}{8,791}}. \\
	\end{array}
	\]

	Finally, the number of turns reachable by 50 turns or fewer is at most

	\[1+\sum_{n=1}^{50}|T_n| \leq 2.52\times 10^{118} < \frac{\left(24!\times 2^{24}\right) \times \left(32! \times 6^{32}\right) \times (16! \times 12^{16})}{48} \approx 1.78 \times 10^{120}.\]

	This shows there are positions on the \(3^4\) which require 51 turns or more to solve.

	Unfortunately, we did not improve the lower bound here. It is worth noting that in the estimate from the beginning (with few optimizations), the actual value of the sum on the LHS is quite close to the number of scrambles possible on the \(3^4\) (within the same order of magnitude). Compare this to our new estimate, where the sum is bounded above by a number two orders of magnitude smaller than the number of scrambles possible on the \(3^4\). So as we would have expected, our improvements do reduce the size of the estimate, just not quite enough to bring down the number of turns derived.

Below is an example of a similar argument used to derive a lower bound of 56 turns in the OBTM. Note that this argument is missing some optimizations that were applied in the STM lower bound derivation.

??? abstract "OBTM Lower Bound, Winning Ways Method"

	Moves here will be measured using something equivalent (as far as this discussion is concerned) to OBTM. Our focus here is on positions that can be reached by algorithms of a certain length. Wide moves contribute to algorithm length in the same way that single cell turns do (wide move = single cell move + cube rotation, where cube rotations count as 0 moves), so we will make a simplification by restricting to single cell turns. There are 23 moves on each of the 8 cells, so 184 one-move algorithms are possible at any given time.

	We know the 3^4^ can be scrambled in over 1.7 novemtrigintillion ways. When solving, we have 184 choices for the first turn, and 161 (non cancelling) choices for the following turns. The number of positions reachable by 54 turns or fewer is at most

	\[1 + 184 \times \sum_{n=0}^{53} 161^n \approx 1.695 \times 10^{119} < 1.757 \times 10^{120}.\]

	This shows that there exist positions on the 3^4^ that require 55 or more turns to solve.

	In the book _Winning Ways for Your Mathematical Plays Vol. 4_, the authors optimize this argument (as it applies to the Rubik's Cube in the half turn metric) by accounting for relations like \(LR = RL\). We can apply a similar optimization for the 3^4^.

	We will refer to the number of possible 3^4^ positions after \(n\) moves as \(u_n\). It is not too hard to convince ourselves that \(u_1 = 184\). After turning one cell, moving the same cell again is what we might call a "cancelling move", since the two moves could have been measured as a single move. So, we have \(161\) non cancelling choices for a second move. We should be able to reduce that \(161\) further by avoiding double counting positions reachable by two algorithms which differ only by the order of commuting elements.

	There are different ways that a pair of moves can commute on 3^4^. One is by the cell turns affecting completely distinct subsets of pieces, which happens when turning _opposite_ cells, like \(OL\ IL = IL\ OL\). This is analogous to the commuting cases on the Rubik's Cube as addressed in _Winning Ways_. There is at least one more way, which can involve certain adjacent cell moves. \(OL\ LO = LO\ OL\) is one example. We have not yet reached a description of all commuting cases of this kind. Accounting for these may allow us to further improve the lower bound. For now, we will factor out the commutativities that we _can_ describe, which we will call "opposite-commuting" moves.

	First, there are \(161-23 = 138\) possible non-cancelling, _non-opposite-commuting_ choices for the second move. We'll add the opposite-commuting cases separately.

	There are four "flavors" of opposite-commuting cases: I cell moves with O cell moves, R moves with L moves, U moves with D moves, and B moves with F moves. In any of these, choose any one of the 23 moves possible on each cell (order doesn't matter), so there are \(23 \times 23 = 529\) opposite-commuting cases of each flavor. Then across the four flavors, we have \(529\times 4 = 2,116\) distinct cases after the second move, when it opposite-commuted with the first. So we have that the number of \(3^4\) positions after \(n\) moves is _at most_  \(138u_1 + 2,116 = 27,508\). That is, we can say \(u_2 \leq 27,508\).

	As a sanity check, we could note at this point the \(27,508\) positions after two turns is better than the \(184\times 161 = 29,624\) positions we would have estimated without accounting for opposite-commutativity of two successive turns here.

	To complete the argument, we can derive a recurrence relation (more accurately a recurrence _estimate_) that gives us an upper bound on the size of \(u_{n+2}\) in terms of \(u_n\) and \(u_{n+1}\)

	In the case where the \(n+2\)th move will _not_ opposite-commute (or cancel) with the \(n+1\)th move, we have \(138u_{n+1}\) possible puzzle states. If the \(n+2\)th move _is_ going to opposite-commute with the \(n+1\)th move, we might have \(529\times 4 = 2,116\) cases to follow up the \(n\)th move. However, one of those four flavors of opposite commuting cases would have cancelled with the \(n\)th move, so this time we only have \(529 \times 3 = 1,587\) cases to follow the \(n\)th move. This gives us the recurrence estimate \(u_{n+2} \leq 138u_{n+1} + 1,587u_{n}\).

	Note that as we have defined it, \(u_n\) is the number of positions accessible by _exactly_ \(n\) moves. If we _sum_ the \(u_n\)s from 1 to \(N\), that will gives us (an upper bound on) the number of positions accessible by \(n\) moves _or fewer_.

	In this case, our recurrence estimate is an order 2 linear recurrence with constant coefficients. There exists a method to derive a general formula for \(u_n\). In the end, we find

	\[u_n = C\lambda_1^n + D\lambda_2^n,\]

	where


	\[
	\begin{array}{c c}
	\lambda_{1}=69+46\sqrt{3}, & \lambda_{2}=69-46\sqrt{3}, \\
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

God's number for 3^4^ is definitely between 56 and 570 inclusive, and probably $\sim 125 \pm 50$^\[citation\ needed]^.

!!! question "Could this be improved?"

    - A better method could easily improve the upper bound, probably to around 300^\[citation\ needed]^.
    - A better manual computation could give a slightly better lower bound.
    - An automated 3^4^ solver or search program could give a much better estimate.
