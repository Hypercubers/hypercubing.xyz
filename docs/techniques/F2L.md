# F2L

<center>
<div style="width:200px; height:219px">
    <script>AnimCube3("config=../../assets/animcube/AnimCube3.txt&facelets=lllllllllwwwwwwwwwLRRLRRLRRlooloolooLLLBBBBBBlgglgglgg")</script>   
</div>
</center>

First 2 Layers (F2L) is a solving technique for cubes and some other puzzles that involves pairing pieces and inserting those pairs into slots to build up the first 2 layers (of a 3-layered puzzle). The first known [description of this technique](https://www.cubinghistory.com/3x3/Methods/CFOP#first-two-layers) was by [John Conway](https://en.wikipedia.org/wiki/John_Horton_Conway) in 1979, but is most commonly credited to Jessica Fridrich due to the massive popularity her website describing the CFOP method had in the early 1990s.

!!! warning ""
    The goal of this page is to give you a generalized understanding of higher dimensional F2L, not to hand out algorithms for certain cases. There are so many cases for higher dimensional F2L that it would be nearly impossible to list out all the cases. It's recommended to have a fairly strong intuitive understanding of 3D F2L before reading this page.

**Dimensional Analogy**

In 3D F2L, whenever you twist a side axis to expose a slot, only that one single slot goes to the top layer. In reality it's a line of 2 corners and an edge, but one of the corners will stay on top, so it doesn't matter. The important thing to note is that it brings up that 1D line of pieces to the top layer because in 3D, the intersection of 2 adjacent sides is a 1D line.

In 4 dimensions, 2 adjacent sides intersect at a 2D plane. So when you do a twist you're bringing **3** slots to the top, that being two F2L-b slots and an F2L-a slot. This makes inserting a single pair trickier, because now you need to use more moves to not disturb the other two subslots.

Continuing this analogy into 5D, you bring a whole 3D cube's worth of F2L slots to the top that you mustn't distrub while inserting a single pair. This pattern continues for higher and higher dimensions, meaning that it gets trickier to insert a single pair. Pro solvers of higher dimensional puzzles will wait until they have 3 (or multiples of 3) pairs, then pairs all those pairs into a gigapair, and then insert that gigapair like inserting a lower dimensional pair.

**Terminology**

To talk about F2L in a dimensionally neutral way, we need some more terms. Most importantly, the following:

- **Head**: the piece in the pair with the most colours (corner in 3D)
- **Body**. the piece in the pair with one less colour (edge in 3D)

For more terms, see [the glossary](https://hypercubing.xyz/glossary/).


Regardless of dimension and type of pair, they are broken down into the following categories:

1. both in top, head facing side axes
2. both in top, head facing top axis
3. body in slot, head in top facing side axis
4. body in slot, head in top facing top axis
5. head in slot facing side axis, body in top
6. head in slot facing base axis, body in top
7. both stuck in slot



## F2L-4a

F2L-a pairs consist of a 2c and a 3c, exactly the same as in 3D. The solutions feel very similar to 3D cases, but there are a few extra tricks that are possible.


???+ example "Insert"
    ![F2L-4a hide reveal pair](https://assets.hypercubing.xyz/img/virt/F2L/F2L-4a_3.png){width=256 align=left}

    Normal F2L insert: `IU RU IU' RU'`

???+ example "Hide and reveal"
    ![F2L-4a hide reveal pair](https://assets.hypercubing.xyz/img/virt/F2L/F2L-4a_1.png){width=256 align=left}

    Notice: same color on top. 
    
    Can either use RKT on the I cell to pair it or use hide and reveal (preferred).

    ```
    RU IU RU' //pair
    IU2 RU IU' RU' //insert
    ```

???+ example "3-mover"
    ![F2L-4a hide reveal pair](https://assets.hypercubing.xyz/img/virt/F2L/F2L-4a_4.png){width=256 align=left}
    3-move insert. Still works if the body is at IU, IF, or ID except you'll just need an extra RKT move.

    Notice how the F sticker of the pair matches the F cell colour. (If it doesn't, then the pair will be flipped after inserting!)

???+ example "Capping"
    ![F2L-4a hide reveal pair](https://assets.hypercubing.xyz/img/virt/F2L/F2L-4a_2.png){width=256 align=left}

    - Body stuck in slot, solved
    - Head has base color on top
    - Cap head on top of body
    - Push, rotate pair, pull
    
    Solution: `IU2 IF RU IR2 RU'`