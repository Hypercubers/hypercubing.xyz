# 3-Block

3-Block is a method designed for quickly speedsolving the 3^4^. Many speedsolving world records have been set using this method. It was primarily invented by Luna and HactarCE, and has been described as "ZZ without EO". 3-Block is most analogous to the 3^3^ method [FreeFOP] (which omits a single cross piece in order to pair pieces easier). Compared to [4D CFOP](/methods/3x3x3x3/cfop.md), 3-Block uses ~20% fewer moves.

!!! warning "Prerequisites"
    - Knowledge of how the 3^4^ moves
    - [Notation](/notation.md)
    - [RKT](/techniques/rkt.md)
    - [3D CFOP](https://jperm.net/3x3/cfop) with 2-look OLL & PLL

[FreeFOP]: https://www.speedsolving.com/wiki/index.php/FreeFOP

??? abstract "HSC Piece filters"
    === "Pink cross"
        ```yaml
        - preset_name: 4-cross
          visible_pieces: 000200080a5010284280
        - preset_name: Mid (back)
          visible_pieces: 000200084a5090294284
        - preset_name: Mid
          visible_pieces: 000200094a5294294294
        - preset_name: Left (cross)
          visible_pieces: 000200094a5294296294
        - preset_name: Left
          visible_pieces: 0002000d4a5a943962d4
        - preset_name: BL-a
          visible_pieces: 0002000d4a7a943963d4
        - preset_name: BL
          visible_pieces: 0002000d6a7ad4b963d6
        - preset_name: FL-a
          visible_pieces: 0002000d6b7ad4bd63d6
        - preset_name: FL
          visible_pieces: 0002008d6b7bd6bd6bd6
        - preset_name: Right (cross)
          visible_pieces: 0002008d6b7bd6bdebd6
        - preset_name: Right
          visible_pieces: 0002008d7b7bf6fdebd7
        - preset_name: BR-a
          visible_pieces: 0002008d7bfbf6fdefd7
        - preset_name: BR
          visible_pieces: 0002008dfbfbf7ffefdf
        - preset_name: FR-a
          visible_pieces: 0002008dfffbf7ffffdf
        - preset_name: FR
          visible_pieces: 0002008fffffffffffff
        - preset_name: OLC 2c
          visible_pieces: "01471400000000000000"
        - preset_name: OLC 3c
          visible_pieces: aaa8aa20000000000000
        - preset_name: OLC 4c
          visible_pieces: "54104150000000000000"
        - preset_name: OLC
          visible_pieces: ffffff70000000000000
        - preset_name: PLC 2c
          visible_pieces: 014714080a5010004000
        - preset_name: PLC cross
          visible_pieces: "01479e20000000000000"
        - preset_name: PLC F2L
          visible_pieces: 01efff70000000000000
        - preset_name: PLC
          visible_pieces: ffffff70000000000000
        - preset_name: End
          visible_pieces: ffffffffffffffffffff
        ```
    === "Rowan's filters (white cross)"
        ```yaml
        - preset_name: 4/6Cross
          visible_pieces: 000204080a5830004080
        - preset_name: Middle 1
          visible_pieces: 00070e080a5830004080
        - preset_name: Middle 2
          visible_pieces: 00070e080a583000e0c1
        - preset_name: Left Block 1
          visible_pieces: 00478e080a5a3008e0d1
        - preset_name: Left Block 2
          visible_pieces: 00478e080e5e3008e0d1
        - preset_name: Left Block 3
          visible_pieces: 00c78f080e5e3008e0d1
        - preset_name: Left Block 4
          visible_pieces: 00c78f080e5e3008f0f1
        - preset_name: Left Block 5
          visible_pieces: 00c78f080f5f3008f0f1
        - preset_name: Left Block 6
          visible_pieces: 00e7cf080f5f3008f0f1
        - preset_name: Left Block 7
          visible_pieces: 00e7cf080f5f300cf8f1
        - preset_name: Right Block 1
          visible_pieces: 00e7df280f5fb00cfaf5
        - preset_name: Right Block 2
          visible_pieces: 00e7df280fdfb10cfaf5
        - preset_name: Right Block 3
          visible_pieces: 00e7ff680fdfb10cfaf5
        - preset_name: Right Block 4
          visible_pieces: 00e7ff680fdfb10cfefd
        - preset_name: Right Block 5
          visible_pieces: 00e7ff680ffff10cfefd
        - preset_name: Right Block 6
          visible_pieces: 00efff780ffff10cfefd
        - preset_name: Right Block 7
          visible_pieces: 00efff780ffff10cffff
        - preset_name: 2c OLC
          visible_pieces: 01efff7d5ffff12cffff
        - preset_name: 3c OLC
          visible_pieces: abeffffffffff57dffff
        - preset_name: 4c OLC
          visible_pieces: 54ffff700ffffb8effff
        - preset_name: 2c PLC
          visible_pieces: 01efff7d5ffff12cffff
        - preset_name: RKT PLC Cross
          visible_pieces: ab00000d500000204000
        - preset_name: RKT PLC F2L
          visible_pieces: ff10008ff00000204000
        - preset_name: RKT PLC LL
          visible_pieces: ff10008ff0000ef30000
        ```
    === "Rowan's new filters (pink cross)"
        ```yaml
        - preset_name: 4-cross
          visible_pieces: 000200080a5010284280
        - preset_name: odM
          visible_pieces: 000200094a5014294280
        - preset_name: ouM
          visible_pieces: 000200094a5294294294
        - preset_name: OLES
          visible_pieces: 000200094a5294296294
        - preset_name: oLS
          visible_pieces: 0002000d4a5a943962d4
        - preset_name: oBLE
          visible_pieces: 0002000d4a7a943963d4
        - preset_name: oDBL
          visible_pieces: 0002000d6a7a94b963d4
        - preset_name: oUBL
          visible_pieces: 0002000d6a7ad4b963d6
        - preset_name: oFLE
          visible_pieces: 0002000d6b7ad4bd63d6
        - preset_name: oDFL
          visible_pieces: 0002008d6b7ad6bd63d6
        - preset_name: oUFL
          visible_pieces: 0002008d6b7bd6bd6bd6
        - preset_name: ORES
          visible_pieces: 0002008d6b7bd6bdebd6
        - preset_name: oRS
          visible_pieces: 0002008d7b7bf6fdebd7
        - preset_name: oBRE
          visible_pieces: 0002008d7bfbf6fdefd7
        - preset_name: oDBR
          visible_pieces: 0002008dfbfbf6ffefd7
        - preset_name: oUBR
          visible_pieces: 0002008dfbfbf7ffefdf
        - preset_name: oFRE
          visible_pieces: 0002008dfffbf7ffffdf
        - preset_name: oDFR
          visible_pieces: 0002008ffffbffffffdf
        - preset_name: oUFR
          visible_pieces: 0002008fffffffffffff
        - preset_name: OLC 2c
          visible_pieces: "01471400000000000000"
        - preset_name: OLC 3c
          visible_pieces: aaa8aa20000000000000
        - preset_name: OLC 4c
          visible_pieces: "54104150000000000000"
        - preset_name: PLC 2c
          visible_pieces: 014714080a5010004000
        - preset_name: PLC cross
          visible_pieces: "01479e20000000000000"
        - preset_name: PLC F2L
          visible_pieces: 01efff70000000000000
        - preset_name: PLC
          visible_pieces: ffffff70000000000000
        - preset_name: End
          visible_pieces: ffffffffffffffffffff
        ```
    === "Triplets instead of pairs"
        ```yaml
        - preset_name: 4-cross
          visible_pieces: 000200080a5010284280
        - preset_name: odM
          visible_pieces: 000200094a5014294280
        - preset_name: ouM
          visible_pieces: 000200094a5294294294
        - preset_name: OLES
          visible_pieces: 000200094a5294296294
        - preset_name: oLS
          visible_pieces: 0002000d4a5a943962d4
        - preset_name: triplet 1
          visible_pieces: 0002000d6a7ad43962d4
        - preset_name: triplet 2
          visible_pieces: 0002000d6a7ad4b963d6
        - preset_name: triplet 3
          visible_pieces: 0002008d6b7bd4b963d6
        - preset_name: triplet 4
          visible_pieces: 0002008d6b7bd6bd6bd6
        - preset_name: ORES
          visible_pieces: 0002008d6b7bd6bdebd6
        - preset_name: oRS
          visible_pieces: 0002008d7b7bf6fdebd7
        - preset_name: triplet 5
          visible_pieces: 0002008dfbfbf7fdebd7
        - preset_name: triplet 6
          visible_pieces: 0002008dfbfbf7ffefdf
        - preset_name: triplet 7
          visible_pieces: 0002008ffffff7ffefdf
        - preset_name: triplet 8
          visible_pieces: 0002008fffffffffffff
        - preset_name: OLC 2c
          visible_pieces: "01471400000000000000"
        - preset_name: OLC 3c
          visible_pieces: aaa8aa20000000000000
        - preset_name: OLC 4c
          visible_pieces: "54104150000000000000"
        - preset_name: PLC 2c
          visible_pieces: 014714080a5010004000
        - preset_name: PLC cross
          visible_pieces: "01479e20000000000000"
        - preset_name: PLC F2L
          visible_pieces: 01efff70000000000000
        - preset_name: PLC
          visible_pieces: ffffff70000000000000
        - preset_name: End
          visible_pieces: ffffffffffffffffffff
        ```

## Summary

1. **4-Cross** — Solve 4 out of the 6 cross pieces
2. **Middle Block** — Solve 4 2c3c pairs betwen the 4 cross pieces
3. **Left Block** — Blockbuild or pair pieces to solve the Left Cell
4. **Right Block** — Blockbuild or pair pieces to solve the Right Cell
5. **OLL-4** - Orient LC 2c, 3c, and 4c pieces using 3D algorithms
6. **PLL-4** - Permute LC 2c, 3c, and 4c pieces using 3D techniques

## Steps

### 4-Cross

Solve the four 2c cross pieces in a ring in the M slice. Leave the L and R cross pieces unsolved.

<center>![4-cross](https://cloud.hypercubing.xyz/assets/img/virt/3block/4cross.png){width="50%"}</center>

### Middle Block

!!! tip
    For the entirety of F2L, the last layer is held on the I cell, as opposed to [CFOP](/methods/3x3x3x3/cfop.md) where it is held on the U cell. This allows us to see more information at once.

Create and insert 4 F2L-a (2c3c) pairs into the 4/6 cross. This will solve 2/3 of the M slice. Because the Left and Right cells don't have their cross pieces, you can use them to aid with building and inserting the pairs.

<center>![Middle block](https://cloud.hypercubing.xyz/assets/img/virt/3block/middle_block.png){width="50%"}</center>

### Left Block

Solve the Left cell. This is done in 3 blocks, hence the name of the method. The first block consists of the cross edge, followed by two 2c3c F2L-a pairs that are opposite of each other. This solves the middle column of the left cell. The final two blocks consist of a 2c3c pair, and two 3c4c pairs.

<center>![Left block](https://cloud.hypercubing.xyz/assets/img/virt/3block/left_block.png){width="50%"}</center>

### Right Block

Solve the Right cell. This is also done by breaking it up into the 3 blocks, except now you don't have an empty opposite cell to aid you in making pairs. You could just solve the cross edge, and then finish the whole solve using [CFOP](/methods/3x3x3x3/cfop.md) style F2L and Last Cell. You can also do it the 3 blocks way, except having less freedom means that it is slightly trickier to set up the correct cases.

<center>![Right block](https://cloud.hypercubing.xyz/assets/img/virt/3block/right_block.png){width="50%"}</center>

### Last Layer

This is done in the exact same way as [CFOP](/methods/3x3x3x3/cfop.md#oll-4).

## Big cubes

Solve all the centers, then pair up only the pieces you need during the step of 3-block you're on. For example: after solving centers, pair up 4 cross ridges. For last cell, you can either just orient everything, and then do an RKT 4^4^ solve, or you can pair everything and end up with an RKT 3^3^ solve.
