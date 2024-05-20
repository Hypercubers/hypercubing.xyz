# F2L

<script src="/assets/animcube/AnimCube3.js"></script>

!!! example "3^3^ with the F2L step completed"
<div style="width:200px; height:219px">
    <script>AnimCube3("config=/docs/assets/animcube/AnimCube3.txt")</script>
</div>

First 2 Layers (F2L) is a solving technique for cubes and some other puzzles that involves pairing pieces and inserting those pairs into slots to build up the first 2 layers (of a 3-layered puzzle). The first known [description of this technique](https://www.cubinghistory.com/3x3/Methods/CFOP#first-two-layers) was by [John Conway](https://en.wikipedia.org/wiki/John_Horton_Conway) in 1979, but is most commonly credited to Jessica Fridrich due to the massive popularity her website describing the CFOP method had in the early 1990s.

!!! warning ""
    The goal of this page is to give you a generalized understanding of higher dimensional F2L, not to hand out algorithms for certain cases. There are so many cases for higher dimensional F2L that it would be nearly impossible to list out all the cases. It's recommended to have a fairly strong intuitive understanding of 3D F2L before reading this page.

In 3D when you twist the side axis only a single F2L slot goes to the top. In 4D however, 3 slots come to the top, that being an F2L-a slot and 2 F2L-b slots. This pattern extends to higher dimensions.

## Terminology

To talk about F2L in a dimensionally neutral way, we need some more terms:

- **Head**: the piece in the pair with the most colours (corner in 3D)
- **Body**. the piece in the pair with one less colour (edge in 3D)
- push
- pull
- hide
- reveal
- cap
- uncap
- top
- base

## 4D F2L

For 4D CFOP, you always have to be careful of breaking the cross, so the ways you can build F2L pairs are limited. However if using the 3-block method, you have much more freedom while building the first half of the pairs.

### F2L-a

!!! example inline
    ![F2L-4a hide reveal pair](https://assets.hypercubing.xyz/img/virt/F2L/F2L-4a_3.png)
    Normal F2L insert: `IU RU IU' RU'`
!!! example inline
    ![F2L-4a hide reveal pair](https://assets.hypercubing.xyz/img/virt/F2L/F2L-4a_1.png)

    - Notice: same color on top
    - Push head to hide it
    - Move body next to where head will be
    - Reveal head to pair

!!! example inline
    ![F2L-4a hide reveal pair](https://assets.hypercubing.xyz/img/virt/F2L/F2L-4a_4.png)
    3-move insert. Still works if the body is at IU, IF, or ID except you'll just need an extra RKT move.

!!! example inline
    ![F2L-4a hide reveal pair](https://assets.hypercubing.xyz/img/virt/F2L/F2L-4a_2.png)

    - Body stuck in slot, solved
    - Head has base color on top
    - Cap head on top of body
    - Push, rotate pair, pull
    - Solution: `IU2 IF RU IR2 RU'`