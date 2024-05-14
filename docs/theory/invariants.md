# Piece invariants

Many puzzles exhibit a phenomenon where the position or orientation of some pieces are determined by the position or orientation of the other pieces. This can often be captured with an invariant, a function of position that does not change when moves are applied, and calculating the invariant can identify whether a position is valid or not. Invariants are useful when computing the total numer of positions of a puzzle.

The most common kinds of invariants are permutation parity and total orientation.

## Permutation parity

The permutation parity of a permutation is the parity of the number of swaps needed to produce it. It is exhibited well in [k-Card Game](https://masonhorne.github.io/k-Card-Game/).

## Monoflip

Monoflip is a phenomenon where a single corner piece on the 3×3×3×3 can be flipped in place, with two 2-swaps of stickers, while all other corners are solved. Conversely, if 15 corners on the puzzle are solved, the last corner must either be solved or in one of 3 orientations of the monoflip. This effect is unique to 4D hypercubes. In 3D, having 7 solved corners implies the last corner must also be solved, and in 5D and above, the orientation of the last corner is independent of the orientations of the others.

The monoflip exists because the group of orientations of a single corner, ignoring others, is $A_4$, and its commutator subgroup is the Klein four-group $\mathbb{Z}_2 \times \mathbb{Z}_2$. Each element of this group corresponds to either the identity or a monoflip. Its quotient in $A_4$ is $\mathbb{Z}_3$, which represents an invariant analogous to total corner twist in 3D. This will allow us to prove that the orientation of the last corner, given that the other 15 are solved, must be identity or monoflip.

First, we construct a particular set of 8 ridges by choosing two sets of 4 parallel ridges which are mutually orthogonal (for instance, choose two disjoint rings of 4 cells each, and select the ridges which lie between two cells of the same ring). We say these ridges are red. We can take two more sets of 8 ridges the same way both disjoint from the first one, and we call those ridges green and blue. Notice that if we perform a monoflip on a corner colored like this, the arrangement of colors does not change.

If we pick a particular corner position, we can call its position even. Then, we specify that positions adjacent to even positions are odd, and positions adjacent to odd positions are even. This is well-defined and unique given our original choice. Coordinate-wise, if the coordinates of the corners are in $\{-1,1\}^4$, corners whose coordinates have product $1$ can be even and those with product $-1$ can be odd. Then, in any position of the 3×3×3×3, we define the variant of a particular corner based on two factors: the color in the solved position of where the red ridge of the corner is, and whether the position of the corner is even or odd.

|       | Even | Odd |
| ----- | ---- | --- |
| Red   | 0    | 0   |
| Green | 1    | 2   |
| Blue  | 2    | 1   |

In effect, in an odd position, the roles of green and blue are swapped. By adding the variant of each corner, we get the invariant of the position.

We now analyze how the invariant changes under turns. Since quarter turns form a generating set, we only need to consider those. Each quarter turn fixes one color of ridge and swaps the other two. It also takes corners in even positions to odd positions and vice versa, which swaps blue and green (for the purposes of computing the variant). Thus, it effectively either keeps all colors fixed or 3-cycles them. This has the effect of adding $k$ to the variants of even-positioned corners and subtracting $k$ from the odd-positioned corners for some $k \in \mathbb{Z}_3$. Thus, the invariant stays fixed. Since the invariant of the solved position is $0$, it is $0$ in any position and so if 15 corners are solved, the last one can only be in a variant-$0$ position, that is, identity or monoflip.