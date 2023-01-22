# 3Block

!!! info inline end "3Block"
    - `Algorithms:` 3D CFOP + [RKT Parity](rkt.md#parity)
    - `Move count:` 300-500


3-Block is a method designed for quickly speedsolving the 3^4^. Many speesolving world records have been set using this method. It was primarily invented by Luna and HactarCE, and has been described as "ZZ without EO". It is most analogous to the 3$^3$ method [FreeFOP], which omits a single cross piece in order to let you pair pieces easier.

!!! warning "Prerequisites"
    - Knowledge of how the 4D puzzle moves
    - [Notation](notation.md)
    - [RKT](rkt.md)
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

## Summary

1. `4-Cross` — Solve 4 out of the 6 cross pieces.
2. `Mid` — Solve 4 2c3c pairs betwen the 4 cross pieces.
3. `Left` — Blockbuild or pair pieces to solve the Left Cell.
4. `Right` — Blockbuild or pair pieces to solve the Right Cell.

## Steps

### 4-Cross

Solve the four 2c cross pieces in a ring in the M slice. Leave the L and R cross pieces unsolved.

### Mid

!!! tip
    For the entirety of F2L, the last layer is held on the I cell, as opposed to [CFOP](cfop.md) where it is held on the U cell. This allows us to see more information at once.

Create and insert 4 F2L-a (2c3c) pairs into the 4/6 cross. This will solve 2/3 of the M slice. Because the Left and Right cells don't have their cross pieces, you can use them to aid with building and inserting the pairs.

### Left

Solve the Left cell. This is done in 3 blocks, hence the name of the method. The first block consists of the cross edge, followed by two 2c3c F2L-a pairs that are opposite of each other. This solves the middle column of the left cell. The final two blocks consist of a 2c3c pair, and two 3c4c pairs.

### Right

Solve the Right cell. This is also done by breaking it up into the 3 blocks, except now you don't have an empty opposite cell to aid you in making pairs. You could just solve the cross edge, and then finish the whole solve using [CFOP](cfop.md) style F2L and Last Cell. You can also do it the 3 blocks way, except having less freedom means that it is slightly trickier to set up the correct cases.

### Last Cell

This is done in the exact same way as [CFOP](cfop.md#olc).

## Big cubes

Solve all the centers, then pair up only the pieces you need during the step of 3-block you're on. For example: after solving centers, pair up 4 cross ridges. For last cell, you can either just orient everything, and then do an RKT 4$^4$ solve, or you can pair everything and end up with an RKT 3^3^ solve.
