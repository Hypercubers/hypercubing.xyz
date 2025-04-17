# 3-Block

3-Block is a method designed for quickly speedsolving the 3^4^. Many speedsolving world records have been set using this method. It was primarily invented by Luna and HactarCE, and has been described as "ZZ without EO". 3-Block is most analogous to the 3^3^ method [FreeFOP] (which omits a single cross piece in order to pair pieces easier). Compared to [4D CFOP](/methods/3x3x3x3/cfop.md), 3-Block uses ~20% fewer moves.

!!! warning "Prerequisites"
    - Knowledge of how the 3^4^ moves
    - [Notation](/notation.md)
    - [RKT](/techniques/rkt.md)
    - [3D CFOP](https://jperm.net/3x3/cfop) with 2-look OLL & PLL

[FreeFOP]: https://www.speedsolving.com/wiki/index.php/FreeFOP

??? abstract "HSC Piece filters (3^4^)"
    === "Hactar's filters (pink cross)"
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

??? abstract "HSC Piece filters (4^4^, 5^4^, 6^4^, 7^4^)"
    These are all Hactar's filters, which use pink cross.
    === "4^4^"
        ```yaml
        - preset_name: U center
          visible_pieces: "000000000000000000000000000660000000000006600000000000000000"
        - preset_name: D center
          visible_pieces: "000000000000000006600000000660066000000006600000000000000000"
        - preset_name: B center
          visible_pieces: "000000000000000006600060060660066000600606600000000000000000"
        - preset_name: F center
          visible_pieces: "000000000000000006606066060660066060660606600000000000000000"
        - preset_name: First 5 centers
          visible_pieces: "000000000000000006606066060660066060660606600000066006600000"
        - preset_name: D cross ridge
          visible_pieces: "000000000000000006606066060660066060660606600660066006600000"
        - preset_name: B cross ridge
          visible_pieces: "000000000000000006606066060660066060660606600660066606660000"
        - preset_name: U cross ridge
          visible_pieces: "000000000000000006606066060660066060660606600660066606660660"
        - preset_name: 4-cross
          visible_pieces: "000000000000000006606066060660066060660606600660666666660660"
        - preset_name: Belt 1/4
          visible_pieces: "000000000000000006666066060660066660660606600666666666660660"
        - preset_name: Belt 2/4
          visible_pieces: "000000000000000006666066060666066660660606660666666666660666"
        - preset_name: Belt 3/4
          visible_pieces: "000000000000000066666066060666666660660606666666666666660666"
        - preset_name: Belt
          visible_pieces: "000000000000000066666066066666666660660666666666666666666666"
        - preset_name: L center
          visible_pieces: "000000000000000066666566566666666665665666666666666666666666"
        - preset_name: L 1/3
          visible_pieces: "000000000000000066666566566666666665665666666666677667766666"
        - preset_name: L 2/3
          visible_pieces: "000000000000000067766566566666677665665666666776677667766666"
        - preset_name: L 3/3
          visible_pieces: "000000000000000067766566566776677665665667766776677667766776"
        - preset_name: BL 1/3
          visible_pieces: "000000000000000067766576576776677665765767766776677767776776"
        - preset_name: BL 2/3
          visible_pieces: "000000000000000067776576576776677765765767766777677767776776"
        - preset_name: BL 3/3
          visible_pieces: "000000000000000067776576576777677765765767776777677767776777"
        - preset_name: FL 1/3
          visible_pieces: "000000000000000067777577576777677775775767776777777777776777"
        - preset_name: FL 2/3
          visible_pieces: "000000000000000077777577576777777775775767777777777777776777"
        - preset_name: FL 3/3
          visible_pieces: "000000000000000077777577577777777775775777777777777777777777"
        - preset_name: R center
          visible_pieces: 000000000000000077777f77f7777777777f77f777777777777777777777
        - preset_name: R 1/3
          visible_pieces: 000000000000000077777f77f7777777777f77f7777777777ff77ff77777
        - preset_name: R 2/3
          visible_pieces: 00000000000000007ff77f77f777777ff77f77f777777ff77ff77ff77777
        - preset_name: R 3/3
          visible_pieces: 00000000000000007ff77f77f77ff77ff77f77f77ff77ff77ff77ff77ff7
        - preset_name: BR 1/3
          visible_pieces: 00000000000000007ff77ff7ff7ff77ff77ff7ff7ff77ff77fff7fff7ff7
        - preset_name: BR 2/3
          visible_pieces: 00000000000000007fff7ff7ff7ff77fff7ff7ff7ff77fff7fff7fff7ff7
        - preset_name: BR 3/3
          visible_pieces: 00000000000000007fff7ff7ff7fff7fff7ff7ff7fff7fff7fff7fff7fff
        - preset_name: FR 1/3
          visible_pieces: 00000000000000007fffffffff7fff7fffffffff7fff7fffffffffff7fff
        - preset_name: FR 2/3
          visible_pieces: 0000000000000000ffffffffff7fffffffffffff7fffffffffffffff7fff
        - preset_name: FR 3/3
          visible_pieces: 0000000000000000ffffffffffffffffffffffffffffffffffffffffffff
        - preset_name: RLC 1/6
          visible_pieces: "000006600660066000000000000000000000000000000000000000000000"
        - preset_name: RLC 2/6
          visible_pieces: "000006660666066000000000000000000000000000000000000000000000"
        - preset_name: RLC 3/6
          visible_pieces: "066006660666066000000000000000000000000000000000000000000000"
        - preset_name: RLC 4/6
          visible_pieces: "066007760776066000000000000000000000000000000000000000000000"
        - preset_name: RLC 6/6
          visible_pieces: 06606ff66ff6066000000000000000000000000000000000000000000000
        - preset_name: ELC 2/12
          visible_pieces: "000600000000000600000000000000000000000000000000000000000000"
        - preset_name: ELC 4/12
          visible_pieces: "600600000000600600000000000000000000000000000000000000000000"
        - preset_name: ELC 6/12
          visible_pieces: "611600000000611600000000000000000000000000000000000000000000"
        - preset_name: ELC 8/12
          visible_pieces: "611610011001611600000000000000000000000000000000000000000000"
        - preset_name: ELC 10/12
          visible_pieces: "699610011001699600000000000000000000000000000000000000000000"
        - preset_name: ELC 12/12
          visible_pieces: "699690099009699600000000000000000000000000000000000000000000"
        - preset_name: OLC
          visible_pieces: ffffffffffffffff00000000000000000000000000000000000000000000
        - preset_name: PLC 2c
          visible_pieces: 06606ff66ff6066006606f66f6066006606f66f606600000066006600000
        - preset_name: PLC cross
          visible_pieces: 06606ff66ff66ff600000000000000000000000000000000000000000000
        - preset_name: PLC F2L
          visible_pieces: 0660ffffffffffff00000000000000000000000000000000000000000000
        - preset_name: PLC
          visible_pieces: ffffffffffffffff00000000000000000000000000000000000000000000
        - preset_name: Done
          visible_pieces: ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ```
    === "5^4^"
        ```yaml
        - preset_name: U center
          visible_pieces: 0000000000000004000000000000000000000000000000000007ec100080000000481200000c9370000000000000000000007ec100000000000000002000000000000000
        - preset_name: D center
          visible_pieces: 00000000000000040000000000000000837e0000000000000007ec100ec9300000481200000c93700837e0000000000000007ec100000000000000002000000000000000
        - preset_name: B center
          visible_pieces: 00000000000000040000000000000000837e0000c100c100c107ec100ec9300007481700070c93700837e0000c100c100c107ec100000000000000002000000000000000
        - preset_name: F center
          visible_pieces: 00000000000000040000000000000000837e0830c930c930c107ec100ec930e007e817e0070c93700837e0830c930c930c107ec100000000000000002000000000000000
        - preset_name: O center
          visible_pieces: 00000000000000040000000000000000837e0830c930c930c107ec100ec930e007e817e0070c93700837e0830c930c930c107ec100000000c93700837e0007ec10000000
        - preset_name: 4-cross D center
          visible_pieces: 00000000000000040000000000000000837e0830c930c930c107ec100ec930e007e817e0070c93700837e0830c930c930c107ec100080000c93700837e0007ec10000000
        - preset_name: 4-cross D
          visible_pieces: 00000000000000040000000000000000837e0830c930c930c107ec100ec930e007e817e0070c93700837e0830c930c930c107ec100ec9300c93700837e0007ec10000000
        - preset_name: 4-cross B center
          visible_pieces: 00000000000000040000000000000000837e0830c930c930c107ec100ec930e007e817e0070c93700837e0830c930c930c107ec100ec9300c93700837e8007ec10000000
        - preset_name: 4-cross B
          visible_pieces: 00000000000000040000000000000000837e0830c930c930c107ec100ec930e007e817e0070c93700837e0830c930c930c107ec100ec9300c937e0837ec107ec93000000
        - preset_name: 4-cross U center
          visible_pieces: 00000000000000040000000000000000837e0830c930c930c107ec100ec930e007e817e0070c93700837e0830c930c930c107ec100ec9300c937e0837ec107ec93008000
        - preset_name: 4-cross U
          visible_pieces: 00000000000000040000000000000000837e0830c930c930c107ec100ec930e007e817e0070c93700837e0830c930c930c107ec100ec9300c937e0837ec107ec930ec930
        - preset_name: 4-cross F center
          visible_pieces: 00000000000000040000000000000000837e0830c930c930c107ec100ec930e007e817e0070c93700837e0830c930c930c107ec100ec9300c937e8837ec107ec930ec930
        - preset_name: 4-cross F
          visible_pieces: 00000000000000040000000000000000837e0830c930c930c107ec100ec930e007e817e0070c93700837e0830c930c930c107ec100ec930ec937ec937ec937ec930ec930
        - preset_name: Mid DB ridge center
          visible_pieces: 00000000000000040000000000000000837e0830c930c930c107ec100ec932e007e817e0070c93700837e0830c930c930c107ec100ec930ec937ec937ec937ec930ec930
        - preset_name: Mid DB ridge
          visible_pieces: 00000000000000040000000000000000837ec930c930c930c107ec100ec937e007e817e0070c93700837ec930c930c930c107ec100ec930ec937ec937ec937ec930ec930
        - preset_name: Mid DB
          visible_pieces: 00000000000000040000000000000000837ec930c930c930c107ec100ec937e007e817e0070c93700837ec930c930c930c107ec100ec937ec937ec937ec937ec930ec930
        - preset_name: Mid UB ridge center
          visible_pieces: 00000000000000040000000000000000837ec930c930c930c107ec100ec937e007e817e0070c93740837ec930c930c930c107ec100ec937ec937ec937ec937ec930ec930
        - preset_name: Mid UB ridge
          visible_pieces: 00000000000000040000000000000000837ec930c930c930c107ec930ec937e007e817e0070c937e0837ec930c930c930c107ec930ec937ec937ec937ec937ec930ec930
        - preset_name: Mid UB
          visible_pieces: 00000000000000040000000000000000837ec930c930c930c107ec930ec937e007e817e0070c937e0837ec930c930c930c107ec930ec937ec937ec937ec937ec930ec937
        - preset_name: Mid DF ridge center
          visible_pieces: 00000000000000040000000000000000837ec930c930c930c107ec932ec937e007e817e0070c937e0837ec930c930c930c107ec930ec937ec937ec937ec937ec930ec937
        - preset_name: Mid DF ridge
          visible_pieces: 0000000000000004000000000000000c937ec930c930c930c107ec937ec937e007e817e0070c937ec937ec930c930c930c107ec930ec937ec937ec937ec937ec930ec937
        - preset_name: Mid DF
          visible_pieces: 0000000000000004000000000000000c937ec930c930c930c107ec937ec937e007e817e0070c937ec937ec930c930c930c107ec937ec937ec937ec937ec937ec930ec937
        - preset_name: Mid UF ridge center
          visible_pieces: 0000000000000004000000000000000c937ec930c930c930c107ec937ec937e007e817e0074c937ec937ec930c930c930c107ec937ec937ec937ec937ec937ec930ec937
        - preset_name: Mid UF ridge
          visible_pieces: 0000000000000004000000000000000c937ec930c930c930c937ec937ec937e007e817e007ec937ec937ec930c930c930c937ec937ec937ec937ec937ec937ec930ec937
        - preset_name: Mid UF
          visible_pieces: 0000000000000004000000000000000c937ec930c930c930c937ec937ec937e007e817e007ec937ec937ec930c930c930c937ec937ec937ec937ec937ec937ec937ec937
        - preset_name: L center
          visible_pieces: 0000000000000000000000000000000c937ec9bac9bac9bac937ec937ec937ea27ea27ea27ec937ec937ec9bac9bac9bac937ec937ec937ec937ec937ec937ec937ec937
        - preset_name: L cross ridge center
          visible_pieces: 0000000000000000000000000000000c937ec9bac9bac9bac937ec937ec937ea27ea27ea27ec937ec937ec9bac9bac9bac937ec937ec937ec937ec9b7ec937ec937ec937
        - preset_name: L cross ridge
          visible_pieces: 0000000000000000000000000000000c937ec9bac9bac9bac937ec937ec937ea27ea27ea27ec937ec937ec9bac9bac9bac937ec937ec937eedb7ecdb7fc9b7fe937ec937
        - preset_name: L D ridge center
          visible_pieces: 0000000000000000000000000000000c937ec9bac9bac9bac937ec937ee937ea27ea27ea27ec937ec937ec9bac9bac9bac937ec937ec937eedb7ecdb7fc9b7fe937ec937
        - preset_name: L D ridge
          visible_pieces: 0000000000000000000000000000000cdb7fc9bac9bac9bac937ec937fed37ea27ea27ea27ec937ecdb7fc9bac9bac9bac937ec937ec937eedb7ecdb7fc9b7fe937ec937
        - preset_name: L D
          visible_pieces: 0000000000000000000000000000000cdb7fc9bac9bac9bac937ec937fed37ea27ea27ea27ec937ecdb7fc9bac9bac9bac937ec937fed37eedb7ecdb7fc9b7fe937ec937
        - preset_name: L U ridge center
          visible_pieces: 0000000000000000000000000000000cdb7fc9bac9bac9bac937ec937fed37ea27ea27ea27ecd37ecdb7fc9bac9bac9bac937ec937fed37eedb7ecdb7fc9b7fe937ec937
        - preset_name: L U ridge
          visible_pieces: 0000000000000000000000000000000cdb7fc9bac9bac9bac9b7fe937fed37ea27ea27ea27eedb7ecdb7fc9bac9bac9bac9b7fe937fed37eedb7ecdb7fc9b7fe937ec937
        - preset_name: L U
          visible_pieces: 0000000000000000000000000000000cdb7fc9bac9bac9bac9b7fe937fed37ea27ea27ea27eedb7ecdb7fc9bac9bac9bac9b7fe937fed37eedb7ecdb7fc9b7fe937fed37
        - preset_name: L B ridge center
          visible_pieces: 0000000000000000000000000000000cdb7fc9bac9bac9bac9b7fe937fed37ea27eaa7ea27eedb7ecdb7fc9bac9bac9bac9b7fe937fed37eedb7ecdb7fc9b7fe937fed37
        - preset_name: L B ridge
          visible_pieces: 0000000000000000000000000000000cdb7fc9bae9bae9bae9b7fe937fed37eaa7eaa7eaa7eedb7ecdb7fc9bae9bae9bae9b7fe937fed37eedb7ecdb7fc9b7fe937fed37
        - preset_name: L B
          visible_pieces: 0000000000000000000000000000000cdb7fc9bae9bae9bae9b7fe937fed37eaa7eaa7eaa7eedb7ecdb7fc9bae9bae9bae9b7fe937fed37eedb7fcdb7fe9b7fed37fed37
        - preset_name: L DB
          visible_pieces: 0000000000000000000000000000000cdb7fe9bae9bae9bae9b7fe937fedb7eaa7eaa7eaa7eedb7ecdb7fe9bae9bae9bae9b7fe937fedb7eedb7fcdb7fe9b7fed37fed37
        - preset_name: L UB
          visible_pieces: 0000000000000000000000000000000cdb7fe9bae9bae9bae9b7fed37fedb7eaa7eaa7eaa7eedb7fcdb7fe9bae9bae9bae9b7fed37fedb7eedb7fcdb7fe9b7fed37fedb7
        - preset_name: L F ridge center
          visible_pieces: 0000000000000000000000000000000cdb7fe9bae9bae9bae9b7fed37fedb7eaa7faa7eaa7eedb7fcdb7fe9bae9bae9bae9b7fed37fedb7eedb7fcdb7fe9b7fed37fedb7
        - preset_name: L F ridge
          visible_pieces: 0000000000000000000000000000000cdb7fedbaedbaedbae9b7fed37fedb7faa7faa7faa7eedb7fcdb7fedbaedbaedbae9b7fed37fedb7eedb7fcdb7fe9b7fed37fedb7
        - preset_name: L F
          visible_pieces: 0000000000000000000000000000000cdb7fedbaedbaedbae9b7fed37fedb7faa7faa7faa7eedb7fcdb7fedbaedbaedbae9b7fed37fedb7fedb7fedb7fedb7fed37fedb7
        - preset_name: L DF
          visible_pieces: 0000000000000000000000000000000edb7fedbaedbaedbae9b7fedb7fedb7faa7faa7faa7eedb7fedb7fedbaedbaedbae9b7fedb7fedb7fedb7fedb7fedb7fed37fedb7
        - preset_name: L UF
          visible_pieces: 0000000000000000000000000000000edb7fedbaedbaedbaedb7fedb7fedb7faa7faa7faa7fedb7fedb7fedbaedbaedbaedb7fedb7fedb7fedb7fedb7fedb7fedb7fedb7
        - preset_name: R center
          visible_pieces: 0000000000000000000000000000000edb7fedbffdbffdbffdb7fedb7fedb7fef7fef7fef7fedb7fedb7fedbffdbffdbffdb7fedb7fedb7fedb7fedb7fedb7fedb7fedb7
        - preset_name: R cross ridge center
          visible_pieces: 0000000000000000000000000000000edb7fedbffdbffdbffdb7fedb7fedb7fef7fef7fef7fedb7fedb7fedbffdbffdbffdb7fedb7fedb7fedb7fedbffedb7fedb7fedb7
        - preset_name: R cross ridge
          visible_pieces: 0000000000000000000000000000000edb7fedbffdbffdbffdb7fedb7fedb7fef7fef7fef7fedb7fedb7fedbffdbffdbffdb7fedb7fedb7feffffedffffdbffffb7fedb7
        - preset_name: R D ridge center
          visible_pieces: 0000000000000000000000000000000edb7fedbffdbffdbffdb7fedb7fefb7fef7fef7fef7fedb7fedb7fedbffdbffdbffdb7fedb7fedb7feffffedffffdbffffb7fedb7
        - preset_name: R D ridge
          visible_pieces: 0000000000000000000000000000000edffffdbffdbffdbffdb7fedb7ffff7fef7fef7fef7fedb7fedffffdbffdbffdbffdb7fedb7fedb7feffffedffffdbffffb7fedb7
        - preset_name: R D
          visible_pieces: 0000000000000000000000000000000edffffdbffdbffdbffdb7fedb7ffff7fef7fef7fef7fedb7fedffffdbffdbffdbffdb7fedb7ffff7feffffedffffdbffffb7fedb7
        - preset_name: R U ridge center
          visible_pieces: 0000000000000000000000000000000edffffdbffdbffdbffdb7fedb7ffff7fef7fef7fef7fedf7fedffffdbffdbffdbffdb7fedb7ffff7feffffedffffdbffffb7fedb7
        - preset_name: R U ridge
          visible_pieces: 0000000000000000000000000000000edffffdbffdbffdbffdbffffb7ffff7fef7fef7fef7feffffedffffdbffdbffdbffdbffffb7ffff7feffffedffffdbffffb7fedb7
        - preset_name: R U
          visible_pieces: 0000000000000000000000000000000edffffdbffdbffdbffdbffffb7ffff7fef7fef7fef7feffffedffffdbffdbffdbffdbffffb7ffff7feffffedffffdbffffb7ffff7
        - preset_name: R B ridge center
          visible_pieces: 0000000000000000000000000000000edffffdbffdbffdbffdbffffb7ffff7fef7fefffef7feffffedffffdbffdbffdbffdbffffb7ffff7feffffedffffdbffffb7ffff7
        - preset_name: R B ridge
          visible_pieces: 0000000000000000000000000000000edffffdbfffbfffbfffbffffb7ffff7fefffefffefffeffffedffffdbfffbfffbfffbffffb7ffff7feffffedffffdbffffb7ffff7
        - preset_name: R B
          visible_pieces: 0000000000000000000000000000000edffffdbfffbfffbfffbffffb7ffff7fefffefffefffeffffedffffdbfffbfffbfffbffffb7ffff7fefffffdfffffbfffff7ffff7
        - preset_name: R DB
          visible_pieces: 0000000000000000000000000000000edfffffbfffbfffbfffbffffb7ffffffefffefffefffeffffedfffffbfffbfffbfffbffffb7ffffffefffffdfffffbfffff7ffff7
        - preset_name: R UB
          visible_pieces: 0000000000000000000000000000000edfffffbfffbfffbfffbfffff7ffffffefffefffefffefffffdfffffbfffbfffbfffbfffff7ffffffefffffdfffffbfffff7fffff
        - preset_name: R F ridge center
          visible_pieces: 0000000000000000000000000000000edfffffbfffbfffbfffbfffff7ffffffefffffffefffefffffdfffffbfffbfffbfffbfffff7ffffffefffffdfffffbfffff7fffff
        - preset_name: R F ridge
          visible_pieces: 0000000000000000000000000000000edfffffffffffffffffbfffff7ffffffffffffffffffefffffdfffffffffffffffffbfffff7ffffffefffffdfffffbfffff7fffff
        - preset_name: R F
          visible_pieces: 0000000000000000000000000000000edfffffffffffffffffbfffff7ffffffffffffffffffefffffdfffffffffffffffffbfffff7ffffffffffffffffffffffff7fffff
        - preset_name: R DF
          visible_pieces: 0000000000000000000000000000000effffffffffffffffffbffffffffffffffffffffffffefffffffffffffffffffffffbffffffffffffffffffffffffffffff7fffff
        - preset_name: R UF
          visible_pieces: 0000000000000000000000000000000effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        - preset_name: 2c OLC
          visible_pieces: 000100000200012f901008000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: RLC 1/6
          visible_pieces: 00000000000000000000000000c9370000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: RLC 2/6
          visible_pieces: 0c937000000000000000000000c9370000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: RLC 3/6
          visible_pieces: 0c937000000c10000830000070c9370000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: RLC 4/6
          visible_pieces: 0c9370c1000c93000837000070c9370000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: RLC 6/6
          visible_pieces: 0c9370c5c81d9b813a37136470c9370000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: ELC 1/12
          visible_pieces: "0000000000000000000000000e00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
        - preset_name: ELC 2/12
          visible_pieces: 0000000000000000000000000e0000e000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: ELC 3/12
          visible_pieces: 0000000000000000000000000e0248e000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: ELC 4/12
          visible_pieces: 0000000000000000000000000e26c8e000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: ELC 5/12
          visible_pieces: e000000000000000000000000e26c8e000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: ELC 6/12
          visible_pieces: e0000e0000000000000000000e26c8e000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: ELC 7/12
          visible_pieces: e0248e0000000000000000000e26c8e000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: ELC 8/12
          visible_pieces: e26c8e0000000000000000000e26c8e000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: ELC 9/12
          visible_pieces: e26c8e0200000400000800000e26c8e000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: ELC 10/12
          visible_pieces: e26c8e0200002400004800008e26c8e000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: ELC 11/12
          visible_pieces: e26c8e220000640000c800008e26c8e000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: ELC 12/12
          visible_pieces: e26c8e220002640004c800088e26c8e000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: OLC
          visible_pieces: fffffffffffffffffffffffffffffff100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: 2c PLC
          visible_pieces: 000100000200012f901008000000100000200000001680000000400004c1104812ee77481208832000020000000168000000040000000000001000017400004000000000
        - preset_name: PLC cross
          visible_pieces: 0c9370cdfffd9bfbfb37fff77eefffe000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: PLC F2L
          visible_pieces: 0c9370effffffffffffffffffffffff100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: PLC
          visible_pieces: fffffffffffffffffffffffffffffff100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: Done
          visible_pieces: ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ```
    === "6^4^"
        ```yaml
        - preset_name: U center
          visible_pieces: 0000000000000004000000000000000000000000000000000007ec100080000000481200000c9370000000000000000000007ec100000000000000002000000000000000
        - preset_name: D center
          visible_pieces: 00000000000000040000000000000000837e0000000000000007ec100ec9300000481200000c93700837e0000000000000007ec100000000000000002000000000000000
        - preset_name: B center
          visible_pieces: 00000000000000040000000000000000837e0000c100c100c107ec100ec9300007481700070c93700837e0000c100c100c107ec100000000000000002000000000000000
        - preset_name: F center
          visible_pieces: 00000000000000040000000000000000837e0830c930c930c107ec100ec930e007e817e0070c93700837e0830c930c930c107ec100000000000000002000000000000000
        - preset_name: O center
          visible_pieces: 00000000000000040000000000000000837e0830c930c930c107ec100ec930e007e817e0070c93700837e0830c930c930c107ec100000000c93700837e0007ec10000000
        - preset_name: 4-cross D center
          visible_pieces: 00000000000000040000000000000000837e0830c930c930c107ec100ec930e007e817e0070c93700837e0830c930c930c107ec100080000c93700837e0007ec10000000
        - preset_name: 4-cross D
          visible_pieces: 00000000000000040000000000000000837e0830c930c930c107ec100ec930e007e817e0070c93700837e0830c930c930c107ec100ec9300c93700837e0007ec10000000
        - preset_name: 4-cross B center
          visible_pieces: 00000000000000040000000000000000837e0830c930c930c107ec100ec930e007e817e0070c93700837e0830c930c930c107ec100ec9300c93700837e8007ec10000000
        - preset_name: 4-cross B
          visible_pieces: 00000000000000040000000000000000837e0830c930c930c107ec100ec930e007e817e0070c93700837e0830c930c930c107ec100ec9300c937e0837ec107ec93000000
        - preset_name: 4-cross U center
          visible_pieces: 00000000000000040000000000000000837e0830c930c930c107ec100ec930e007e817e0070c93700837e0830c930c930c107ec100ec9300c937e0837ec107ec93008000
        - preset_name: 4-cross U
          visible_pieces: 00000000000000040000000000000000837e0830c930c930c107ec100ec930e007e817e0070c93700837e0830c930c930c107ec100ec9300c937e0837ec107ec930ec930
        - preset_name: 4-cross F center
          visible_pieces: 00000000000000040000000000000000837e0830c930c930c107ec100ec930e007e817e0070c93700837e0830c930c930c107ec100ec9300c937e8837ec107ec930ec930
        - preset_name: 4-cross F
          visible_pieces: 00000000000000040000000000000000837e0830c930c930c107ec100ec930e007e817e0070c93700837e0830c930c930c107ec100ec930ec937ec937ec937ec930ec930
        - preset_name: Mid DB ridge center
          visible_pieces: 00000000000000040000000000000000837e0830c930c930c107ec100ec932e007e817e0070c93700837e0830c930c930c107ec100ec930ec937ec937ec937ec930ec930
        - preset_name: Mid DB ridge
          visible_pieces: 00000000000000040000000000000000837ec930c930c930c107ec100ec937e007e817e0070c93700837ec930c930c930c107ec100ec930ec937ec937ec937ec930ec930
        - preset_name: Mid DB
          visible_pieces: 00000000000000040000000000000000837ec930c930c930c107ec100ec937e007e817e0070c93700837ec930c930c930c107ec100ec937ec937ec937ec937ec930ec930
        - preset_name: Mid UB ridge center
          visible_pieces: 00000000000000040000000000000000837ec930c930c930c107ec100ec937e007e817e0070c93740837ec930c930c930c107ec100ec937ec937ec937ec937ec930ec930
        - preset_name: Mid UB ridge
          visible_pieces: 00000000000000040000000000000000837ec930c930c930c107ec930ec937e007e817e0070c937e0837ec930c930c930c107ec930ec937ec937ec937ec937ec930ec930
        - preset_name: Mid UB
          visible_pieces: 00000000000000040000000000000000837ec930c930c930c107ec930ec937e007e817e0070c937e0837ec930c930c930c107ec930ec937ec937ec937ec937ec930ec937
        - preset_name: Mid DF ridge center
          visible_pieces: 00000000000000040000000000000000837ec930c930c930c107ec932ec937e007e817e0070c937e0837ec930c930c930c107ec930ec937ec937ec937ec937ec930ec937
        - preset_name: Mid DF ridge
          visible_pieces: 0000000000000004000000000000000c937ec930c930c930c107ec937ec937e007e817e0070c937ec937ec930c930c930c107ec930ec937ec937ec937ec937ec930ec937
        - preset_name: Mid DF
          visible_pieces: 0000000000000004000000000000000c937ec930c930c930c107ec937ec937e007e817e0070c937ec937ec930c930c930c107ec937ec937ec937ec937ec937ec930ec937
        - preset_name: Mid UF ridge center
          visible_pieces: 0000000000000004000000000000000c937ec930c930c930c107ec937ec937e007e817e0074c937ec937ec930c930c930c107ec937ec937ec937ec937ec937ec930ec937
        - preset_name: Mid UF ridge
          visible_pieces: 0000000000000004000000000000000c937ec930c930c930c937ec937ec937e007e817e007ec937ec937ec930c930c930c937ec937ec937ec937ec937ec937ec930ec937
        - preset_name: Mid UF
          visible_pieces: 0000000000000004000000000000000c937ec930c930c930c937ec937ec937e007e817e007ec937ec937ec930c930c930c937ec937ec937ec937ec937ec937ec937ec937
        - preset_name: L center
          visible_pieces: 0000000000000000000000000000000c937ec9bac9bac9bac937ec937ec937ea27ea27ea27ec937ec937ec9bac9bac9bac937ec937ec937ec937ec937ec937ec937ec937
        - preset_name: L cross ridge center
          visible_pieces: 0000000000000000000000000000000c937ec9bac9bac9bac937ec937ec937ea27ea27ea27ec937ec937ec9bac9bac9bac937ec937ec937ec937ec9b7ec937ec937ec937
        - preset_name: L cross ridge
          visible_pieces: 0000000000000000000000000000000c937ec9bac9bac9bac937ec937ec937ea27ea27ea27ec937ec937ec9bac9bac9bac937ec937ec937eedb7ecdb7fc9b7fe937ec937
        - preset_name: L D ridge center
          visible_pieces: 0000000000000000000000000000000c937ec9bac9bac9bac937ec937ee937ea27ea27ea27ec937ec937ec9bac9bac9bac937ec937ec937eedb7ecdb7fc9b7fe937ec937
        - preset_name: L D ridge
          visible_pieces: 0000000000000000000000000000000cdb7fc9bac9bac9bac937ec937fed37ea27ea27ea27ec937ecdb7fc9bac9bac9bac937ec937ec937eedb7ecdb7fc9b7fe937ec937
        - preset_name: L D
          visible_pieces: 0000000000000000000000000000000cdb7fc9bac9bac9bac937ec937fed37ea27ea27ea27ec937ecdb7fc9bac9bac9bac937ec937fed37eedb7ecdb7fc9b7fe937ec937
        - preset_name: L U ridge center
          visible_pieces: 0000000000000000000000000000000cdb7fc9bac9bac9bac937ec937fed37ea27ea27ea27ecd37ecdb7fc9bac9bac9bac937ec937fed37eedb7ecdb7fc9b7fe937ec937
        - preset_name: L U ridge
          visible_pieces: 0000000000000000000000000000000cdb7fc9bac9bac9bac9b7fe937fed37ea27ea27ea27eedb7ecdb7fc9bac9bac9bac9b7fe937fed37eedb7ecdb7fc9b7fe937ec937
        - preset_name: L U
          visible_pieces: 0000000000000000000000000000000cdb7fc9bac9bac9bac9b7fe937fed37ea27ea27ea27eedb7ecdb7fc9bac9bac9bac9b7fe937fed37eedb7ecdb7fc9b7fe937fed37
        - preset_name: L B ridge center
          visible_pieces: 0000000000000000000000000000000cdb7fc9bac9bac9bac9b7fe937fed37ea27eaa7ea27eedb7ecdb7fc9bac9bac9bac9b7fe937fed37eedb7ecdb7fc9b7fe937fed37
        - preset_name: L B ridge
          visible_pieces: 0000000000000000000000000000000cdb7fc9bae9bae9bae9b7fe937fed37eaa7eaa7eaa7eedb7ecdb7fc9bae9bae9bae9b7fe937fed37eedb7ecdb7fc9b7fe937fed37
        - preset_name: L B
          visible_pieces: 0000000000000000000000000000000cdb7fc9bae9bae9bae9b7fe937fed37eaa7eaa7eaa7eedb7ecdb7fc9bae9bae9bae9b7fe937fed37eedb7fcdb7fe9b7fed37fed37
        - preset_name: L DB
          visible_pieces: 0000000000000000000000000000000cdb7fe9bae9bae9bae9b7fe937fedb7eaa7eaa7eaa7eedb7ecdb7fe9bae9bae9bae9b7fe937fedb7eedb7fcdb7fe9b7fed37fed37
        - preset_name: L UB
          visible_pieces: 0000000000000000000000000000000cdb7fe9bae9bae9bae9b7fed37fedb7eaa7eaa7eaa7eedb7fcdb7fe9bae9bae9bae9b7fed37fedb7eedb7fcdb7fe9b7fed37fedb7
        - preset_name: L F ridge center
          visible_pieces: 0000000000000000000000000000000cdb7fe9bae9bae9bae9b7fed37fedb7eaa7faa7eaa7eedb7fcdb7fe9bae9bae9bae9b7fed37fedb7eedb7fcdb7fe9b7fed37fedb7
        - preset_name: L F ridge
          visible_pieces: 0000000000000000000000000000000cdb7fedbaedbaedbae9b7fed37fedb7faa7faa7faa7eedb7fcdb7fedbaedbaedbae9b7fed37fedb7eedb7fcdb7fe9b7fed37fedb7
        - preset_name: L F
          visible_pieces: 0000000000000000000000000000000cdb7fedbaedbaedbae9b7fed37fedb7faa7faa7faa7eedb7fcdb7fedbaedbaedbae9b7fed37fedb7fedb7fedb7fedb7fed37fedb7
        - preset_name: L DF
          visible_pieces: 0000000000000000000000000000000edb7fedbaedbaedbae9b7fedb7fedb7faa7faa7faa7eedb7fedb7fedbaedbaedbae9b7fedb7fedb7fedb7fedb7fedb7fed37fedb7
        - preset_name: L UF
          visible_pieces: 0000000000000000000000000000000edb7fedbaedbaedbaedb7fedb7fedb7faa7faa7faa7fedb7fedb7fedbaedbaedbaedb7fedb7fedb7fedb7fedb7fedb7fedb7fedb7
        - preset_name: R center
          visible_pieces: 0000000000000000000000000000000edb7fedbffdbffdbffdb7fedb7fedb7fef7fef7fef7fedb7fedb7fedbffdbffdbffdb7fedb7fedb7fedb7fedb7fedb7fedb7fedb7
        - preset_name: R cross ridge center
          visible_pieces: 0000000000000000000000000000000edb7fedbffdbffdbffdb7fedb7fedb7fef7fef7fef7fedb7fedb7fedbffdbffdbffdb7fedb7fedb7fedb7fedbffedb7fedb7fedb7
        - preset_name: R cross ridge
          visible_pieces: 0000000000000000000000000000000edb7fedbffdbffdbffdb7fedb7fedb7fef7fef7fef7fedb7fedb7fedbffdbffdbffdb7fedb7fedb7feffffedffffdbffffb7fedb7
        - preset_name: R D ridge center
          visible_pieces: 0000000000000000000000000000000edb7fedbffdbffdbffdb7fedb7fefb7fef7fef7fef7fedb7fedb7fedbffdbffdbffdb7fedb7fedb7feffffedffffdbffffb7fedb7
        - preset_name: R D ridge
          visible_pieces: 0000000000000000000000000000000edffffdbffdbffdbffdb7fedb7ffff7fef7fef7fef7fedb7fedffffdbffdbffdbffdb7fedb7fedb7feffffedffffdbffffb7fedb7
        - preset_name: R D
          visible_pieces: 0000000000000000000000000000000edffffdbffdbffdbffdb7fedb7ffff7fef7fef7fef7fedb7fedffffdbffdbffdbffdb7fedb7ffff7feffffedffffdbffffb7fedb7
        - preset_name: R U ridge center
          visible_pieces: 0000000000000000000000000000000edffffdbffdbffdbffdb7fedb7ffff7fef7fef7fef7fedf7fedffffdbffdbffdbffdb7fedb7ffff7feffffedffffdbffffb7fedb7
        - preset_name: R U ridge
          visible_pieces: 0000000000000000000000000000000edffffdbffdbffdbffdbffffb7ffff7fef7fef7fef7feffffedffffdbffdbffdbffdbffffb7ffff7feffffedffffdbffffb7fedb7
        - preset_name: R U
          visible_pieces: 0000000000000000000000000000000edffffdbffdbffdbffdbffffb7ffff7fef7fef7fef7feffffedffffdbffdbffdbffdbffffb7ffff7feffffedffffdbffffb7ffff7
        - preset_name: R B ridge center
          visible_pieces: 0000000000000000000000000000000edffffdbffdbffdbffdbffffb7ffff7fef7fefffef7feffffedffffdbffdbffdbffdbffffb7ffff7feffffedffffdbffffb7ffff7
        - preset_name: R B ridge
          visible_pieces: 0000000000000000000000000000000edffffdbfffbfffbfffbffffb7ffff7fefffefffefffeffffedffffdbfffbfffbfffbffffb7ffff7feffffedffffdbffffb7ffff7
        - preset_name: R B
          visible_pieces: 0000000000000000000000000000000edffffdbfffbfffbfffbffffb7ffff7fefffefffefffeffffedffffdbfffbfffbfffbffffb7ffff7fefffffdfffffbfffff7ffff7
        - preset_name: R DB
          visible_pieces: 0000000000000000000000000000000edfffffbfffbfffbfffbffffb7ffffffefffefffefffeffffedfffffbfffbfffbfffbffffb7ffffffefffffdfffffbfffff7ffff7
        - preset_name: R UB
          visible_pieces: 0000000000000000000000000000000edfffffbfffbfffbfffbfffff7ffffffefffefffefffefffffdfffffbfffbfffbfffbfffff7ffffffefffffdfffffbfffff7fffff
        - preset_name: R F ridge center
          visible_pieces: 0000000000000000000000000000000edfffffbfffbfffbfffbfffff7ffffffefffffffefffefffffdfffffbfffbfffbfffbfffff7ffffffefffffdfffffbfffff7fffff
        - preset_name: R F ridge
          visible_pieces: 0000000000000000000000000000000edfffffffffffffffffbfffff7ffffffffffffffffffefffffdfffffffffffffffffbfffff7ffffffefffffdfffffbfffff7fffff
        - preset_name: R F
          visible_pieces: 0000000000000000000000000000000edfffffffffffffffffbfffff7ffffffffffffffffffefffffdfffffffffffffffffbfffff7ffffffffffffffffffffffff7fffff
        - preset_name: R DF
          visible_pieces: 0000000000000000000000000000000effffffffffffffffffbffffffffffffffffffffffffefffffffffffffffffffffffbffffffffffffffffffffffffffffff7fffff
        - preset_name: R UF
          visible_pieces: 0000000000000000000000000000000effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        - preset_name: 2c OLC
          visible_pieces: 000100000200012f901008000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: RLC 1/6
          visible_pieces: 00000000000000000000000000c9370000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: RLC 2/6
          visible_pieces: 0c937000000000000000000000c9370000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: RLC 3/6
          visible_pieces: 0c937000000c10000830000070c9370000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: RLC 4/6
          visible_pieces: 0c9370c1000c93000837000070c9370000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: RLC 6/6
          visible_pieces: 0c9370c5c81d9b813a37136470c9370000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: ELC 1/12
          visible_pieces: "0000000000000000000000000e00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
        - preset_name: ELC 2/12
          visible_pieces: 0000000000000000000000000e0000e000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: ELC 3/12
          visible_pieces: 0000000000000000000000000e0248e000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: ELC 4/12
          visible_pieces: 0000000000000000000000000e26c8e000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: ELC 5/12
          visible_pieces: e000000000000000000000000e26c8e000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: ELC 6/12
          visible_pieces: e0000e0000000000000000000e26c8e000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: ELC 7/12
          visible_pieces: e0248e0000000000000000000e26c8e000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: ELC 8/12
          visible_pieces: e26c8e0000000000000000000e26c8e000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: ELC 9/12
          visible_pieces: e26c8e0200000400000800000e26c8e000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: ELC 10/12
          visible_pieces: e26c8e0200002400004800008e26c8e000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: ELC 11/12
          visible_pieces: e26c8e220000640000c800008e26c8e000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: ELC 12/12
          visible_pieces: e26c8e220002640004c800088e26c8e000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: OLC
          visible_pieces: fffffffffffffffffffffffffffffff100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: 2c PLC
          visible_pieces: 000100000200012f901008000000100000200000001680000000400004c1104812ee77481208832000020000000168000000040000000000001000017400004000000000
        - preset_name: PLC cross
          visible_pieces: 0c9370cdfffd9bfbfb37fff77eefffe000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: PLC F2L
          visible_pieces: 0c9370effffffffffffffffffffffff100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: PLC
          visible_pieces: fffffffffffffffffffffffffffffff100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: Done
          visible_pieces: ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ```
    === "7^4^"
        ```yaml
        - preset_name: Centers
          visible_pieces: "000000000000000000000000000000000000000000800000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000008000000000000000000808101000000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000"
        - preset_name: 3x3 Centers
          visible_pieces: 0000000000000000000000000000c1e07000000083c1e00000000783c100000000000000000000000000000000000000000000000000000000000000000000000000000000000000e0783000000000078f1e078f1e078f1e0000000000c1e07000000083c1e0000000000c1e783c1e783c1e7830000000000783c10000000e0783000000000078f1e078f1e078f1e0000000000c1e070000000000000000000000000000000000000000000000000000000000000000000000000000000000000083c1e00000000783c10000000e07830000000000000000000000000000
        - preset_name: 5x5 Centers
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e30000000000000008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e308fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc70008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e308fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc70008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000000000000000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e3000c7e3f9fc700000000000000
        - preset_name: Ridges
          visible_pieces: "000000100000000000000000000000000000040000140000100000000000000000000000000000040000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000400001400001000000000000140028000000000000800002800002000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000008000028000020000000000000000000000000000008000000"
        - preset_name: 3x3 Ridges
          visible_pieces: 0000783c100000000000000007001c06010c1e00281c02083c104038140070000000000000000c1e07000000000000000000000000000000000000000000000000000000000083080603800e00000040108060108060108020000007001c06010c1e00281c02083000000140028140028140028000000c1040381400783080603800e00000040108060108060108020000007001c06010c10000000000000000000000000000000000000000000000000000000000e07830000000000000000e00281c02083c1040381400783080603800e000000000000000083c1e0000
        - preset_name: 5x5 Ridges
          visible_pieces: 00f9fc7e3f10c71c0603814f9f281c06038e3f50381c060d7eb060381c0afc71c0603814f10c7e3f9fc700f50381c060d7140028140028140028140028140028eb060381c0afc71c0603814f501080601080601080601080601080af281c06038e3f50381c060d7140028140028140028140028140028eb060381c0afc71c0603814f501080601080601080601080601080af281c06038e3f50381c060d7140028140028140028140028140028eb060381c0af00e3f9fc7e308f281c06038e3f50381c060d7eb060381c0afc71c0603814f9f281c06038e308fc7e3f9f00
        - preset_name: 3x3 Edges
          visible_pieces: c10403814007000000000000401000000001c02000000002814000000004010000000000007001c06010c1000000000000000000000000000000000000000000000000000000280000000080200000000000000000000000000000401000000001c020000000028000000000000000000000000000000140000000040380000000080200000000000000000000000000000401000000001400000000000000000000000000000000000000000000000000000083080603800e00000000000080200000000281400000000403800000000802000000000000e00281c02083
        - preset_name: 5x5 Edges
          visible_pieces: eb060381c0af280000000080601000000001c020000000028140000000040380000000080af281c06038eb020000000028000000000000000000000000000000140000000040380000000080200000000000000000000000000000401000000001c020000000028000000000000000000000000000000140000000040380000000080200000000000000000000000000000401000000001c020000000028000000000000000000000000000000140000000040d71c0603814f501000000001c0200000000281400000000403800000000806010000000014f50381c060d7
        - preset_name: Mid 1.1.1
          visible_pieces: 0000000000000000000000000000000000000000008000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000080000000000000000008081010000000000000000001000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000083c1e00000000783c10000000e07830000000000000000000000000000
        - preset_name: Mid 1.1.2
          visible_pieces: 0000000000000000000000000000c1e07000000083c1e00000000783c100000000000000000000000000000000000000000000000000000000000000000000000000000000000000e0783000000000078f1e078f1e078f1e0000000000c1e07000000083c1e0000000000c1e783c1e783c1e7830000000000783c10000000e0783000000000078f1e078f1e078f1e0000000000c1e07000000000000000000000000000000000000000000000000000000000000000000000000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e3000c7e3f9fc700000000000000
        - preset_name: Mid 1.2.1
          visible_pieces: 000000000000000000000000000000000000000000800000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000c1e0700000000080000000000000000008081010000000000000000783c10000000000000000000000000000000000000000000000000c1e07000000000000000000000000000000000000000000000000000000000000000000000000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e3000c7e3f9fc700000000000000
        - preset_name: Mid 1.2.2
          visible_pieces: 0000000000000000000000000000c1e07000000083c1e00000000783c1000000000000000000000000000000000000000000000000000000000000000000000000f9fc7e3f100000e0783000000000078f1e078f1e078f1e00000000c7e3f9fc70000083c1e0000000000c1e783c1e783c1e78300000000f9fc7e3f100000e0783000000000078f1e078f1e078f1e00000000c7e3f9fc70000000000000000000000000000000000000000000000f9fc7e3f1000000000000000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e3000c7e3f9fc700000000000000
        - preset_name: Mid 1.3.1
          visible_pieces: 0000000000000000000000000000000000000000008000000000000000000000000000000000000000000000000000000000000000000000000000000000000000f9fc7e3f100000e078300000000000000000000000000000000000c7e3f9fc70000083c1e000000000000000080810100000000000000f9fc7e3f100000e078300000000000000000000000000000000000c7e3f9fc70000000000000000000000000000000000000000000000f9fc7e3f1000000000000000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e3000c7e3f9fc700000000000000
        - preset_name: Mid 1.3.2
          visible_pieces: 0000000000000000000000000000c1e07000000083c1e00000000783c1000000000000000000000000000008fc7e3f9f0000000000000000000000000000000000f9fc7e3f1000e3f9fc7e30000000078f1e078f1e078f1e00000000c7e3f9fc70008fc7e3f9f00000000c1e783c1e783c1e78300000000f9fc7e3f1000e3f9fc7e30000000078f1e078f1e078f1e00000000c7e3f9fc70008fc7e3f9f0000000000000000000000000000000000f9fc7e3f1000000000000000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e3000c7e3f9fc700000000000000
        - preset_name: Mid 1.4.1
          visible_pieces: 0000000000000000000000000000000000000000008000000000000000000000000000000000000000000008fc7e3f9f0000000000000000000000000000000000f9fc7e3f1000e3f9fc7e3000000000000e00000e00000e00000000c7e3f9fc70008fc7e3f9f0000000000008380818300008300000000f9fc7e3f1000e3f9fc7e3000000000000e00000e00000e00000000c7e3f9fc70008fc7e3f9f0000000000000000000000000000000000f9fc7e3f1000000000000000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e3000c7e3f9fc700000000000000
        - preset_name: Mid 1.4.2
          visible_pieces: 0000000000000000000000000000c1e07000000083c1e00000000783c1000000000000000000000000000008fc7e3f9f000000c70000c70000c70000c70000c700f9fc7e3f1000e3f9fc7e3000000f178f1f178f1f178f1f10000f10c7e3f9fc70008fc7e3f9f000000c7c1e7c7c1e7c7c1e7c70000c700f9fc7e3f1000e3f9fc7e3000000f178f1f178f1f178f1f10000f10c7e3f9fc70008fc7e3f9f000000c70000c70000c70000c70000c700f9fc7e3f1000000000000000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e3000c7e3f9fc700000000000000
        - preset_name: Mid 1.5.1
          visible_pieces: 0000000000000000000000000000000000000000008000000000000000000000000000000000000000000008fc7e3f9f000000c70000c70000c70000c70000c700f9fc7e3f1000e3f9fc7e3000000f17000f17000f17000f10000f10c7e3f9fc70008fc7e3f9f000000c7c100c7c181c7c100c70000c700f9fc7e3f1000e3f9fc7e3000000f17000f17000f17000f10000f10c7e3f9fc70008fc7e3f9f000000c70000c70000c70000c70000c700f9fc7e3f1000000000000000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e3000c7e3f9fc700000000000000
        - preset_name: Mid 1.5.2
          visible_pieces: 0000000000000000000000000000c1e07000000083c1e00000000783c1000000000000000000000000000008fc7e3f9f00e300c7e300c7e300c7e300c7e300c700f9fc7e3f1000e3f9fc7e308f000f9f8f1f9f8f1f9f8f1f9f000f10c7e3f9fc70008fc7e3f9f00e300c7e3e7c7e3e7c7e3e7c7e300c700f9fc7e3f1000e3f9fc7e308f000f9f8f1f9f8f1f9f8f1f9f000f10c7e3f9fc70008fc7e3f9f00e300c7e300c7e300c7e300c7e300c700f9fc7e3f1000000000000000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e3000c7e3f9fc700000000000000
        - preset_name: Mid 2.1.1
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e30000000000000008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e308fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc70008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e308fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc70008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000000000000000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e3000c7e3f9fc700000008000000
        - preset_name: Mid 2.1.2
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e30000000000000008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e308fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc70008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e308fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc70008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000000000000000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e3000c7e3f9fc70000083c1e0000
        - preset_name: Mid 2.1.3
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e30000000000000008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e308fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc70008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e308fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc70008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000000000000000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e3000c7e3f9fc70008fc7e3f9f00
        - preset_name: Mid 2.2.1
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e30000000000000008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e308fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc70008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e308fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc70008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000000020000000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e3000c7e3f9fc70008fc7e3f9f00
        - preset_name: Mid 2.2.2
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e30000000000000008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e308fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc70008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e308fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc70008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f100000e078300000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e3000c7e3f9fc70008fc7e3f9f00
        - preset_name: Mid 2.2.3
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e30000000000000008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e308fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc70008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e308fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc70008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e3000c7e3f9fc70008fc7e3f9f00
        - preset_name: Mid 2.3.1
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e30000000000000008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e308fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc70008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e308fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc70008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1200e3f9fc7e3000c7e3f9fc70008fc7e3f9f00
        - preset_name: Mid 2.3.2
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e30000000000000008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e308fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc70008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e308fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc70008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e3000c7e3f9fc70008fc7e3f9f8300f9fc7e3f1700e3f9fc7e3e00c7e3f9fc70008fc7e3f9f00
        - preset_name: Mid 2.3.3
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e30000000000000008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e308fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc70008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e308fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc70008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e3000c7e3f9fc7e308fc7e3f9fc700f9fc7e3f9f00e3f9fc7e3f10c7e3f9fc7e308fc7e3f9f00
        - preset_name: Mid 2.4.1
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e30000000000000008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e308fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc70008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e308fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc70008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e3000c7e3f9fc7e308fc7e3f9fc780f9fc7e3f9f00e3f9fc7e3f10c7e3f9fc7e308fc7e3f9f00
        - preset_name: Mid 2.4.2
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e30000000000000008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e308fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc70008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e308fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc70008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e3000c7e3f9fc7e3e8fc7e3f9fc7c1f9fc7e3f9f83e3f9fc7e3f10c7e3f9fc7e308fc7e3f9f00
        - preset_name: Mid 2.4.3
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e30000000000000008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e308fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc70008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e308fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc70008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e308fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e308fc7e3f9f00
        - preset_name: Mid 3.1.1
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e30000000000000008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e308fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc70008fc7e3f9f01ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e308fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc70008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e308fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e308fc7e3f9f00
        - preset_name: Mid 3.1.2
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e30000000000000008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e3e8fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc70008fc7e3f9f83ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e3e8fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc70008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e308fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e308fc7e3f9f00
        - preset_name: Mid 3.1.3
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e30000000000000008fc7e3f9fc7ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e3f9fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc70008fc7e3f9fc7ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e3f9fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc70008fc7e3f9fc7ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e308fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e308fc7e3f9f00
        - preset_name: Mid 3.1.4
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e30000000000000008fc7e3f9fc7ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e3f9fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc70008fc7e3f9fc7ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e3f9fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc70008fc7e3f9fc7ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e308fc7e3f9f00
        - preset_name: Mid 3.2.1
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e30000000000000008fc7e3f9fc7ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e3f9fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc70008fc7e3f9fc7ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1200e3f9fc7e3f9fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc70008fc7e3f9fc7ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e308fc7e3f9f00
        - preset_name: Mid 3.2.2
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e30000000000000008fc7e3f9fc7ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e3f9fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc7c108fc7e3f9fc7ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1700e3f9fc7e3f9fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc7c108fc7e3f9fc7ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e308fc7e3f9f00
        - preset_name: Mid 3.2.3
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e30000000000000008fc7e3f9fc7ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f9f00e3f9fc7e3f9fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc7e308fc7e3f9fc7ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f9f00e3f9fc7e3f9fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc7e308fc7e3f9fc7ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f9f00e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e308fc7e3f9f00
        - preset_name: Mid 3.2.4
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e30000000000000008fc7e3f9fc7ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f9f00e3f9fc7e3f9fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc7e308fc7e3f9fc7ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f9f00e3f9fc7e3f9fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc7e308fc7e3f9fc7ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f9f00e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e308fc7e3f9fc7
        - preset_name: Mid 3.3.1
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e30000000000000008fc7e3f9fc7ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f9f00e3f9fc7e3f9fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc7e348fc7e3f9fc7ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f9f00e3f9fc7e3f9fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc7e308fc7e3f9fc7ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f9f00e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e308fc7e3f9fc7
        - preset_name: Mid 3.3.2
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e30000000000000008fc7e3f9fc7ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f9f83e3f9fc7e3f9fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc7e3e8fc7e3f9fc7ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f9f83e3f9fc7e3f9fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc7e308fc7e3f9fc7ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f9f00e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e308fc7e3f9fc7
        - preset_name: Mid 3.3.3
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e300000000000000f9fc7e3f9fc7ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f9fc7e3f9fc7e3f9fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc7e3f9fc7e3f9fc7ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f9fc7e3f9fc7e3f9fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc7e3f9fc7e3f9fc7ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f9f00e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e308fc7e3f9fc7
        - preset_name: Mid 3.3.4
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e300000000000000f9fc7e3f9fc7ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f9fc7e3f9fc7e3f9fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc7e3f9fc7e3f9fc7ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f9fc7e3f9fc7e3f9fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc7e3f9fc7e3f9fc7ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e308fc7e3f9fc7
        - preset_name: Mid 3.4.1
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e300000000000000f9fc7e3f9fc7ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f9fc7e3f9fc7e3f9fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc7e3f9fc7e3f9fc7ebffd7ebffd7ebffd7ebffd7ebffd780f9fc7e3f9fc7e3f9fc7e3f9fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc7e3f9fc7e3f9fc7ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e308fc7e3f9fc7
        - preset_name: Mid 3.4.2
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e300000000000000f9fc7e3f9fc7ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f9fc7e3f9fc7e3f9fef7f9fef7f9fef7f9fef7f9fef7f17c7e3f9fc7e3f9fc7e3f9fc7ebffd7ebffd7ebffd7ebffd7ebffd7c1f9fc7e3f9fc7e3f9fc7e3f9fef7f9fef7f9fef7f9fef7f9fef7f17c7e3f9fc7e3f9fc7e3f9fc7ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e308fc7e3f9fc7
        - preset_name: Mid 3.4.3
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e300000000000000f9fc7e3f9fc7ebffd7ebffd7ebffd7ebffd7ebffd7e3f9fc7e3f9fc7e3f9fc7e3f9fef7f9fef7f9fef7f9fef7f9fef7f9fc7e3f9fc7e3f9fc7e3f9fc7ebffd7ebffd7ebffd7ebffd7ebffd7e3f9fc7e3f9fc7e3f9fc7e3f9fef7f9fef7f9fef7f9fef7f9fef7f9fc7e3f9fc7e3f9fc7e3f9fc7ebffd7ebffd7ebffd7ebffd7ebffd7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e308fc7e3f9fc7
        - preset_name: Mid 3.4.4
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e300000000000000f9fc7e3f9fc7ebffd7ebffd7ebffd7ebffd7ebffd7e3f9fc7e3f9fc7e3f9fc7e3f9fef7f9fef7f9fef7f9fef7f9fef7f9fc7e3f9fc7e3f9fc7e3f9fc7ebffd7ebffd7ebffd7ebffd7ebffd7e3f9fc7e3f9fc7e3f9fc7e3f9fef7f9fef7f9fef7f9fef7f9fef7f9fc7e3f9fc7e3f9fc7e3f9fc7ebffd7ebffd7ebffd7ebffd7ebffd7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7
        - preset_name: Left 1.1.1
          visible_pieces: 00000000000000000000000000000000000000000080000000000000000000000000000000000000000000f9fc7e3f9fc7e300c7e300c7e300c7e300c7e300c7e3f9fc7e3f9fc7e3f9fc7e3f9f000f9f8a0f9f8a0f9f8a0f9f000f9fc7e3f9fc7e3f9fc7e3f9fc7e300c7e3a2c7e3a3c7e3a2c7e300c7e3f9fc7e3f9fc7e3f9fc7e3f9f000f9f8a0f9f8a0f9f8a0f9f000f9fc7e3f9fc7e3f9fc7e3f9fc7e300c7e300c7e300c7e300c7e300c7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7
        - preset_name: Left 1.1.2
          visible_pieces: 0000000000000000000000000000c1e07000000083c1e00000000783c10000000000000000000000000000f9fc7e3f9fc7ebaac7ebaac7ebaac7ebaac7ebaac7e3f9fc7e3f9fc7e3f9fc7e3f9faa2f9faf3f9faf3f9faf3f9faa2f9fc7e3f9fc7e3f9fc7e3f9fc7ebaac7ebefc7ebefc7ebefc7ebaac7e3f9fc7e3f9fc7e3f9fc7e3f9faa2f9faf3f9faf3f9faf3f9faa2f9fc7e3f9fc7e3f9fc7e3f9fc7ebaac7ebaac7ebaac7ebaac7ebaac7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7
        - preset_name: Left 1.2.1
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e300000000000000f9fc7e3f9fc7ebffd7ebffd7ebffd7ebffd7ebffd7e3f9fc7e3f9fc7e3f9fc7e3f9fef7f9fef7f9fef7f9fef7f9fef7f9fc7e3f9fc7e3f9fc7e3f9fc7ebffd7ebffd7ebffd7ebffd7ebffd7e3f9fc7e3f9fc7e3f9fc7e3f9fef7f9fef7f9fef7f9fef7f9fef7f9fc7e3f9fc7e3f9fc7e3f9fc7ebffd7ebffd7ebffd7ebffd7ebffd7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fe7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7
        - preset_name: Left 1.2.2
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e300000000000000f9fc7e3f9fc7ebffd7ebffd7ebffd7ebffd7ebffd7e3f9fc7e3f9fc7e3f9fc7e3f9fef7f9fef7f9fef7f9fef7f9fef7f9fc7e3f9fc7e3f9fc7e3f9fc7ebffd7ebffd7ebffd7ebffd7ebffd7e3f9fc7e3f9fc7e3f9fc7e3f9fef7f9fef7f9fef7f9fef7f9fef7f9fc7e3f9fc7e3f9fc7e3f9fc7ebffd7ebffd7ebffd7ebffd7ebffd7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fe7fbf9fc7e3fdfe7f3f9fc7ebfdfe7e3f9fc7e3f9fc7e3f9fc7e3f9fc7
        - preset_name: Left 1.2.3
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e300000000000000f9fc7e3f9fc7ebffd7ebffd7ebffd7ebffd7ebffd7e3f9fc7e3f9fc7e3f9fc7e3f9fef7f9fef7f9fef7f9fef7f9fef7f9fc7e3f9fc7e3f9fc7e3f9fc7ebffd7ebffd7ebffd7ebffd7ebffd7e3f9fc7e3f9fc7e3f9fc7e3f9fef7f9fef7f9fef7f9fef7f9fef7f9fc7e3f9fc7e3f9fc7e3f9fc7ebffd7ebffd7ebffd7ebffd7ebffd7e3f9fc7e3f9fc7e3f9fc7e3f9fe7fbfdfe7e3fdfe7fbfdfc7ebfdfe7fbf9fc7fbfdfe7f3f9fe7fbfdfe7e3f9fc7e3f9fc7
        - preset_name: Left 1.3.1
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e300000000000000f9fc7e3f9fc7ebffd7ebffd7ebffd7ebffd7ebffd7e3f9fc7e3f9fc7e3f9fc7e3f9fef7f9fef7f9fef7f9fef7f9fef7f9fc7e3f9fc7e3f9fc7f3f9fc7ebffd7ebffd7ebffd7ebffd7ebffd7e3f9fc7e3f9fc7e3f9fc7e3f9fef7f9fef7f9fef7f9fef7f9fef7f9fc7e3f9fc7e3f9fc7e3f9fc7ebffd7ebffd7ebffd7ebffd7ebffd7e3f9fc7e3f9fc7e3f9fc7e3f9fe7fbfdfe7e3fdfe7fbfdfc7ebfdfe7fbf9fc7fbfdfe7f3f9fe7fbfdfe7e3f9fc7e3f9fc7
        - preset_name: Left 1.3.2
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e300000000000000f9fc7e3f9fc7ebffd7ebffd7ebffd7ebffd7ebffd7e3f9fc7e3f9fc7ebfdfe7e3f9fef7f9fef7f9fef7f9fef7f9fef7f9fc7e3f9fc7e3f9fe7fbf9fc7ebffd7ebffd7ebffd7ebffd7ebffd7e3f9fc7e3f9fc7ebfdfe7e3f9fef7f9fef7f9fef7f9fef7f9fef7f9fc7e3f9fc7e3f9fc7e3f9fc7ebffd7ebffd7ebffd7ebffd7ebffd7e3f9fc7e3f9fc7e3f9fc7e3f9fe7fbfdfe7e3fdfe7fbfdfc7ebfdfe7fbf9fc7fbfdfe7f3f9fe7fbfdfe7e3f9fc7e3f9fc7
        - preset_name: Left 1.3.3
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e300000000000000fdfe7fbfdfc7ebffd7ebffd7ebffd7ebffd7ebffd7e3f9fc7e3f9fc7fbfdfe7f3f9fef7f9fef7f9fef7f9fef7f9fef7f9fc7e3f9fc7e3fdfe7fbfdfc7ebffd7ebffd7ebffd7ebffd7ebffd7e3f9fc7e3f9fc7fbfdfe7f3f9fef7f9fef7f9fef7f9fef7f9fef7f9fc7e3f9fc7e3fdfe7fbfdfc7ebffd7ebffd7ebffd7ebffd7ebffd7e3f9fc7e3f9fc7e3f9fc7e3f9fe7fbfdfe7e3fdfe7fbfdfc7ebfdfe7fbf9fc7fbfdfe7f3f9fe7fbfdfe7e3f9fc7e3f9fc7
        - preset_name: Left 1.3.4
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e300000000000000fdfe7fbfdfc7ebffd7ebffd7ebffd7ebffd7ebffd7e3f9fc7e3f9fc7fbfdfe7f3f9fef7f9fef7f9fef7f9fef7f9fef7f9fc7e3f9fc7e3fdfe7fbfdfc7ebffd7ebffd7ebffd7ebffd7ebffd7e3f9fc7e3f9fc7fbfdfe7f3f9fef7f9fef7f9fef7f9fef7f9fef7f9fc7e3f9fc7e3fdfe7fbfdfc7ebffd7ebffd7ebffd7ebffd7ebffd7e3f9fc7e3f9fc7fbfdfe7f3f9fe7fbfdfe7e3fdfe7fbfdfc7ebfdfe7fbf9fc7fbfdfe7f3f9fe7fbfdfe7e3f9fc7e3f9fc7
        - preset_name: Left 1.4.1
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e300000000000000fdfe7fbfdfc7ebffd7ebffd7ebffd7ebffd7ebffd7e3f9fc7e3f9fc7fbfdfe7f3f9fef7f9fef7f9fef7f9fef7f9fef7f9fc7e3f9fc7e3fdfe7fbfdfc7ebffd7ebffd7ebffd7ebffd7ebffd7e3f9fe7e3f9fc7fbfdfe7f3f9fef7f9fef7f9fef7f9fef7f9fef7f9fc7e3f9fc7e3fdfe7fbfdfc7ebffd7ebffd7ebffd7ebffd7ebffd7e3f9fc7e3f9fc7fbfdfe7f3f9fe7fbfdfe7e3fdfe7fbfdfc7ebfdfe7fbf9fc7fbfdfe7f3f9fe7fbfdfe7e3f9fc7e3f9fc7
        - preset_name: Left 1.4.2
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e300000000000000fdfe7fbfdfc7ebffd7ebffd7ebffd7ebffd7ebffd7e3f9fc7e3f9fc7fbfdfe7f3f9fef7f9fef7f9fef7f9fef7f9fef7f9fc7fbfdfc7e3fdfe7fbfdfc7ebffd7ebffd7ebffd7ebffd7ebffd7e3fdfe7f3f9fc7fbfdfe7f3f9fef7f9fef7f9fef7f9fef7f9fef7f9fc7fbfdfc7e3fdfe7fbfdfc7ebffd7ebffd7ebffd7ebffd7ebffd7e3f9fc7e3f9fc7fbfdfe7f3f9fe7fbfdfe7e3fdfe7fbfdfc7ebfdfe7fbf9fc7fbfdfe7f3f9fe7fbfdfe7e3f9fc7e3f9fc7
        - preset_name: Left 1.4.3
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e300000000000000fdfe7fbfdfc7ebffd7ebffd7ebffd7ebffd7ebffd7ebfdfe7fbf9fc7fbfdfe7f3f9fef7f9fef7f9fef7f9fef7f9fef7f9fe7fbfdfe7e3fdfe7fbfdfc7ebffd7ebffd7ebffd7ebffd7ebffd7ebfdfe7fbf9fc7fbfdfe7f3f9fef7f9fef7f9fef7f9fef7f9fef7f9fe7fbfdfe7e3fdfe7fbfdfc7ebffd7ebffd7ebffd7ebffd7ebffd7ebfdfe7fbf9fc7fbfdfe7f3f9fe7fbfdfe7e3fdfe7fbfdfc7ebfdfe7fbf9fc7fbfdfe7f3f9fe7fbfdfe7e3f9fc7e3f9fc7
        - preset_name: Left 1.4.4
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e300000000000000fdfe7fbfdfc7ebffd7ebffd7ebffd7ebffd7ebffd7ebfdfe7fbf9fc7fbfdfe7f3f9fef7f9fef7f9fef7f9fef7f9fef7f9fe7fbfdfe7e3fdfe7fbfdfc7ebffd7ebffd7ebffd7ebffd7ebffd7ebfdfe7fbf9fc7fbfdfe7f3f9fef7f9fef7f9fef7f9fef7f9fef7f9fe7fbfdfe7e3fdfe7fbfdfc7ebffd7ebffd7ebffd7ebffd7ebffd7ebfdfe7fbf9fc7fbfdfe7f3f9fe7fbfdfe7e3fdfe7fbfdfc7ebfdfe7fbf9fc7fbfdfe7f3f9fe7fbfdfe7e3fdfe7fbfdfc7
        - preset_name: Left 2.1.1
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e300000000000000fdfe7fbfdfc7ebffd7ebffd7ebffd7ebffd7ebffd7ebfdfe7fbf9fc7fbfdfe7f3f9fef7f9fef7f9fef7f9fef7f9fef7f9fe7fbfdfe7e3fdfe7fbfdfc7ebffd7ebffd7ebfff7ebffd7ebffd7ebfdfe7fbf9fc7fbfdfe7f3f9fef7f9fef7f9fef7f9fef7f9fef7f9fe7fbfdfe7e3fdfe7fbfdfc7ebffd7ebffd7ebffd7ebffd7ebffd7ebfdfe7fbf9fc7fbfdfe7f3f9fe7fbfdfe7e3fdfe7fbfdfc7ebfdfe7fbf9fc7fbfdfe7f3f9fe7fbfdfe7e3fdfe7fbfdfc7
        - preset_name: Left 2.1.2
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e300000000000000fdfe7fbfdfc7ebffd7ebffd7ebffd7ebffd7ebffd7ebfdfe7fbf9fc7fbfdfe7f3f9fef7f9fefff9fefff9fefff9fef7f9fe7fbfdfe7e3fdfe7fbfdfc7ebffd7ebfff7ebfff7ebfff7ebffd7ebfdfe7fbf9fc7fbfdfe7f3f9fef7f9fefff9fefff9fefff9fef7f9fe7fbfdfe7e3fdfe7fbfdfc7ebffd7ebffd7ebffd7ebffd7ebffd7ebfdfe7fbf9fc7fbfdfe7f3f9fe7fbfdfe7e3fdfe7fbfdfc7ebfdfe7fbf9fc7fbfdfe7f3f9fe7fbfdfe7e3fdfe7fbfdfc7
        - preset_name: Left 2.1.3
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e300000000000000fdfe7fbfdfc7ebfff7ebfff7ebfff7ebfff7ebfff7ebfdfe7fbf9fc7fbfdfe7f3f9fefff9fefff9fefff9fefff9fefff9fe7fbfdfe7e3fdfe7fbfdfc7ebfff7ebfff7ebfff7ebfff7ebfff7ebfdfe7fbf9fc7fbfdfe7f3f9fefff9fefff9fefff9fefff9fefff9fe7fbfdfe7e3fdfe7fbfdfc7ebfff7ebfff7ebfff7ebfff7ebfff7ebfdfe7fbf9fc7fbfdfe7f3f9fe7fbfdfe7e3fdfe7fbfdfc7ebfdfe7fbf9fc7fbfdfe7f3f9fe7fbfdfe7e3fdfe7fbfdfc7
        - preset_name: Left 2.1.4
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e300000000000000fdfe7fbfdfc7ebfff7ebfff7ebfff7ebfff7ebfff7ebfdfe7fbf9fc7fbfdfe7f3f9fefff9fefff9fefff9fefff9fefff9fe7fbfdfe7e3fdfe7fbfdfc7ebfff7ebfff7ebfff7ebfff7ebfff7ebfdfe7fbf9fc7fbfdfe7f3f9fefff9fefff9fefff9fefff9fefff9fe7fbfdfe7e3fdfe7fbfdfc7ebfff7ebfff7ebfff7ebfff7ebfff7ebfdfe7fbf9fc7fbfdfe7f3f9fe7fbfdfe7f3fdfe7fbfdfe7ebfdfe7fbfdfc7fbfdfe7fbf9fe7fbfdfe7f3fdfe7fbfdfc7
        - preset_name: Left 2.2
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e300000000000000fdfe7fbfdfe7ebfff7ebfff7ebfff7ebfff7ebfff7ebfdfe7fbf9fc7fbfdfe7fbf9fefff9fefff9fefff9fefff9fefff9fe7fbfdfe7e3fdfe7fbfdfe7ebfff7ebfff7ebfff7ebfff7ebfff7ebfdfe7fbf9fc7fbfdfe7fbf9fefff9fefff9fefff9fefff9fefff9fe7fbfdfe7e3fdfe7fbfdfe7ebfff7ebfff7ebfff7ebfff7ebfff7ebfdfe7fbf9fc7fbfdfe7fbf9fe7fbfdfe7f3fdfe7fbfdfe7ebfdfe7fbfdfc7fbfdfe7fbf9fe7fbfdfe7f3fdfe7fbfdfc7
        - preset_name: Left 2.3
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e300000000000000fdfe7fbfdfe7ebfff7ebfff7ebfff7ebfff7ebfff7ebfdfe7fbfdfc7fbfdfe7fbf9fefff9fefff9fefff9fefff9fefff9fe7fbfdfe7f3fdfe7fbfdfe7ebfff7ebfff7ebfff7ebfff7ebfff7ebfdfe7fbfdfc7fbfdfe7fbf9fefff9fefff9fefff9fefff9fefff9fe7fbfdfe7f3fdfe7fbfdfe7ebfff7ebfff7ebfff7ebfff7ebfff7ebfdfe7fbfdfc7fbfdfe7fbf9fe7fbfdfe7f3fdfe7fbfdfe7ebfdfe7fbfdfc7fbfdfe7fbf9fe7fbfdfe7f3fdfe7fbfdfe7
        - preset_name: Left 3.1.1
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e300000000000000fdfe7fbfdfe7ebfff7ebfff7ebfff7ebfff7ebfff7ebfdfe7fbfdfc7fbfdfe7fbf9fefff9fefff9fefff9fefff9fefff9fe7fbfdfe7f3fdfe7fbfdfe7ebfff7ebfff7fbfff7ebfff7ebfff7ebfdfe7fbfdfc7fbfdfe7fbf9fefff9fefff9fefff9fefff9fefff9fe7fbfdfe7f3fdfe7fbfdfe7ebfff7ebfff7ebfff7ebfff7ebfff7ebfdfe7fbfdfc7fbfdfe7fbf9fe7fbfdfe7f3fdfe7fbfdfe7ebfdfe7fbfdfc7fbfdfe7fbf9fe7fbfdfe7f3fdfe7fbfdfe7
        - preset_name: Left 3.1.2
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e300000000000000fdfe7fbfdfe7ebfff7ebfff7ebfff7ebfff7ebfff7ebfdfe7fbfdfc7fbfdfe7fbf9fefffdfefffdfefffdfefff9fefff9fe7fbfdfe7f3fdfe7fbfdfe7ebfff7fbfff7fbfff7fbfff7ebfff7ebfdfe7fbfdfc7fbfdfe7fbf9fefffdfefffdfefffdfefff9fefff9fe7fbfdfe7f3fdfe7fbfdfe7ebfff7ebfff7ebfff7ebfff7ebfff7ebfdfe7fbfdfc7fbfdfe7fbf9fe7fbfdfe7f3fdfe7fbfdfe7ebfdfe7fbfdfc7fbfdfe7fbf9fe7fbfdfe7f3fdfe7fbfdfe7
        - preset_name: Left 3.1.3
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e300000000000000fdfe7fbfdfe7fbfff7fbfff7fbfff7fbfff7fbfff7ebfdfe7fbfdfc7fbfdfe7fbfdfefffdfefffdfefffdfefffdfefff9fe7fbfdfe7f3fdfe7fbfdfe7fbfff7fbfff7fbfff7fbfff7fbfff7ebfdfe7fbfdfc7fbfdfe7fbfdfefffdfefffdfefffdfefffdfefff9fe7fbfdfe7f3fdfe7fbfdfe7fbfff7fbfff7fbfff7fbfff7fbfff7ebfdfe7fbfdfc7fbfdfe7fbf9fe7fbfdfe7f3fdfe7fbfdfe7ebfdfe7fbfdfc7fbfdfe7fbf9fe7fbfdfe7f3fdfe7fbfdfe7
        - preset_name: Left 3.1.4
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e300000000000000fdfe7fbfdfe7fbfff7fbfff7fbfff7fbfff7fbfff7ebfdfe7fbfdfc7fbfdfe7fbfdfefffdfefffdfefffdfefffdfefff9fe7fbfdfe7f3fdfe7fbfdfe7fbfff7fbfff7fbfff7fbfff7fbfff7ebfdfe7fbfdfc7fbfdfe7fbfdfefffdfefffdfefffdfefffdfefff9fe7fbfdfe7f3fdfe7fbfdfe7fbfff7fbfff7fbfff7fbfff7fbfff7ebfdfe7fbfdfc7fbfdfe7fbfdfe7fbfdfe7fbfdfe7fbfdfe7fbfdfe7fbfdfe7fbfdfe7fbfdfe7fbfdfe7f3fdfe7fbfdfe7
        - preset_name: Left 3.2
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e300000000000008fdfe7fbfdfe7fbfff7fbfff7fbfff7fbfff7fbfff7ebfdfe7fbfdfe7fbfdfe7fbfdfefffdfefffdfefffdfefffdfefff9fe7fbfdfe7fbfdfe7fbfdfe7fbfff7fbfff7fbfff7fbfff7fbfff7ebfdfe7fbfdfe7fbfdfe7fbfdfefffdfefffdfefffdfefffdfefff9fe7fbfdfe7fbfdfe7fbfdfe7fbfff7fbfff7fbfff7fbfff7fbfff7ebfdfe7fbfdfe7fbfdfe7fbfdfe7fbfdfe7fbfdfe7fbfdfe7fbfdfe7fbfdfe7fbfdfe7fbfdfe7fbfdfe7f3fdfe7fbfdfe7
        - preset_name: Left 3.3
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e300000000000008fdfe7fbfdfe7fbfff7fbfff7fbfff7fbfff7fbfff7fbfdfe7fbfdfe7fbfdfe7fbfdfefffdfefffdfefffdfefffdfefffdfe7fbfdfe7fbfdfe7fbfdfe7fbfff7fbfff7fbfff7fbfff7fbfff7fbfdfe7fbfdfe7fbfdfe7fbfdfefffdfefffdfefffdfefffdfefffdfe7fbfdfe7fbfdfe7fbfdfe7fbfff7fbfff7fbfff7fbfff7fbfff7fbfdfe7fbfdfe7fbfdfe7fbfdfe7fbfdfe7fbfdfe7fbfdfe7fbfdfe7fbfdfe7fbfdfe7fbfdfe7fbfdfe7fbfdfe7fbfdfe7
        - preset_name: Right 1.1.1
          visible_pieces: 0000000000000000000000000000c1e07000000083c1e00000000783c10000000000000000000000000008fdfe7fbfdfe7fbaae7fbaae7fbaae7fbaae7fbaae7fbfdfe7fbfdfe7fbfdfe7fbfdfaaafdfafbfdfafbfdfafbfdfaaafdfe7fbfdfe7fbfdfe7fbfdfe7fbaae7fbefe7fbefe7fbefe7fbaae7fbfdfe7fbfdfe7fbfdfe7fbfdfaaafdfafbfdfafbfdfafbfdfaaafdfe7fbfdfe7fbfdfe7fbfdfe7fbaae7fbaae7fbaae7fbaae7fbaae7fbfdfe7fbfdfe7fbfdfe7fbfdfe7fbfdfe7fbfdfe7fbfdfe7fbfdfe7fbfdfe7fbfdfe7fbfdfe7fbfdfe7fbfdfe7fbfdfe7
        - preset_name: Right 1.1.2
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e300000000000008fdfe7fbfdfe7fbfff7fbfff7fbfff7fbfff7fbfff7fbfdfe7fbfdfe7fbfdfe7fbfdfefffdfefffdfefffdfefffdfefffdfe7fbfdfe7fbfdfe7fbfdfe7fbfff7fbfff7fbfff7fbfff7fbfff7fbfdfe7fbfdfe7fbfdfe7fbfdfefffdfefffdfefffdfefffdfefffdfe7fbfdfe7fbfdfe7fbfdfe7fbfff7fbfff7fbfff7fbfff7fbfff7fbfdfe7fbfdfe7fbfdfe7fbfdfe7fbfdfe7fbfdfe7fbfdfe7fbfdfe7fbfdfe7fbfdfe7fbfdfe7fbfdfe7fbfdfe7fbfdfe7
        - preset_name: Right 1.1.3
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e300000000000008fdfe7fbfdfe7fbfff7fbfff7fbfff7fbfff7fbfff7fbfdfe7fbfdfe7fbfdfe7fbfdfefffdfefffdfefffdfefffdfefffdfe7fbfdfe7fbfdfe7fbfdfe7fbfff7fbfff7fbfff7fbfff7fbfff7fbfdfe7fbfdfe7fbfdfe7fbfdfefffdfefffdfefffdfefffdfefffdfe7fbfdfe7fbfdfe7fbfdfe7fbfff7fbfff7fbfff7fbfff7fbfff7fbfdfe7fbfdfe7fbfdfe7fbfdfefffffffffbfdfffffffff7fbffffffffffe7ffffffffffdfefffffffffbfdfe7fbfdfe7
        - preset_name: Right 1.2.1
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e300000000000008fdfe7fbfdfe7fbfff7fbfff7fbfff7fbfff7fbfff7fbfdfe7fbfdfe7fbfdfe7fbfdfefffdfefffdfefffdfefffdfefffdfe7fbfdfe7fbfdfe7fffdfe7fbfff7fbfff7fbfff7fbfff7fbfff7fbfdfe7fbfdfe7fbfdfe7fbfdfefffdfefffdfefffdfefffdfefffdfe7fbfdfe7fbfdfe7fbfdfe7fbfff7fbfff7fbfff7fbfff7fbfff7fbfdfe7fbfdfe7fbfdfe7fbfdfefffffffffbfdfffffffff7fbffffffffffe7ffffffffffdfefffffffffbfdfe7fbfdfe7
        - preset_name: Right 1.2.2
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e300000000000008fdfe7fbfdfe7fbfff7fbfff7fbfff7fbfff7fbfff7fbfdfe7fbfdfe7fbffffffbfdfefffdfefffdfefffdfefffdfefffdfe7fbfdfe7fbfdfeffffffe7fbfff7fbfff7fbfff7fbfff7fbfff7fbfdfe7fbfdfe7fbffffffbfdfefffdfefffdfefffdfefffdfefffdfe7fbfdfe7fbfdfe7fbfdfe7fbfff7fbfff7fbfff7fbfff7fbfff7fbfdfe7fbfdfe7fbfdfe7fbfdfefffffffffbfdfffffffff7fbffffffffffe7ffffffffffdfefffffffffbfdfe7fbfdfe7
        - preset_name: Right 1.2.3
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e300000000000008fdfffffffff7fbfff7fbfff7fbfff7fbfff7fbfff7fbfdfe7fbfdfe7ffffffffffdfefffdfefffdfefffdfefffdfefffdfe7fbfdfe7fbfdfffffffff7fbfff7fbfff7fbfff7fbfff7fbfff7fbfdfe7fbfdfe7ffffffffffdfefffdfefffdfefffdfefffdfefffdfe7fbfdfe7fbfdfffffffff7fbfff7fbfff7fbfff7fbfff7fbfff7fbfdfe7fbfdfe7fbfdfe7fbfdfefffffffffbfdfffffffff7fbffffffffffe7ffffffffffdfefffffffffbfdfe7fbfdfe7
        - preset_name: Right 1.2.4
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e300000000000008fdfffffffff7fbfff7fbfff7fbfff7fbfff7fbfff7fbfdfe7fbfdfe7ffffffffffdfefffdfefffdfefffdfefffdfefffdfe7fbfdfe7fbfdfffffffff7fbfff7fbfff7fbfff7fbfff7fbfff7fbfdfe7fbfdfe7ffffffffffdfefffdfefffdfefffdfefffdfefffdfe7fbfdfe7fbfdfffffffff7fbfff7fbfff7fbfff7fbfff7fbfff7fbfdfe7fbfdfe7ffffffffffdfefffffffffbfdfffffffff7fbffffffffffe7ffffffffffdfefffffffffbfdfe7fbfdfe7
        - preset_name: Right 1.3.1
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e300000000000008fdfffffffff7fbfff7fbfff7fbfff7fbfff7fbfff7fbfdfe7fbfdfe7ffffffffffdfefffdfefffdfefffdfefffdfefffdfe7fbfdfe7fbfdfffffffff7fbfff7fbfff7fbfff7fbfff7fbfff7fbfdfeffbfdfe7ffffffffffdfefffdfefffdfefffdfefffdfefffdfe7fbfdfe7fbfdfffffffff7fbfff7fbfff7fbfff7fbfff7fbfff7fbfdfe7fbfdfe7ffffffffffdfefffffffffbfdfffffffff7fbffffffffffe7ffffffffffdfefffffffffbfdfe7fbfdfe7
        - preset_name: Right 1.3.2
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e300000000000008fdfffffffff7fbfff7fbfff7fbfff7fbfff7fbfff7fbfdfe7fbfdfe7ffffffffffdfefffdfefffdfefffdfefffdfefffdfe7ffffff7fbfdfffffffff7fbfff7fbfff7fbfff7fbfff7fbfff7fbfdffffffdfe7ffffffffffdfefffdfefffdfefffdfefffdfefffdfe7ffffff7fbfdfffffffff7fbfff7fbfff7fbfff7fbfff7fbfff7fbfdfe7fbfdfe7ffffffffffdfefffffffffbfdfffffffff7fbffffffffffe7ffffffffffdfefffffffffbfdfe7fbfdfe7
        - preset_name: Right 1.3.3
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e300000000000008fdfffffffff7fbfff7fbfff7fbfff7fbfff7fbfff7fbffffffffffe7ffffffffffdfefffdfefffdfefffdfefffdfefffdfefffffffffbfdfffffffff7fbfff7fbfff7fbfff7fbfff7fbfff7fbffffffffffe7ffffffffffdfefffdfefffdfefffdfefffdfefffdfefffffffffbfdfffffffff7fbfff7fbfff7fbfff7fbfff7fbfff7fbffffffffffe7ffffffffffdfefffffffffbfdfffffffff7fbffffffffffe7ffffffffffdfefffffffffbfdfe7fbfdfe7
        - preset_name: Right 1.3.4
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e300000000000008fdfffffffff7fbfff7fbfff7fbfff7fbfff7fbfff7fbffffffffffe7ffffffffffdfefffdfefffdfefffdfefffdfefffdfefffffffffbfdfffffffff7fbfff7fbfff7fbfff7fbfff7fbfff7fbffffffffffe7ffffffffffdfefffdfefffdfefffdfefffdfefffdfefffffffffbfdfffffffff7fbfff7fbfff7fbfff7fbfff7fbfff7fbffffffffffe7ffffffffffdfefffffffffbfdfffffffff7fbffffffffffe7ffffffffffdfefffffffffbfdfffffffff7
        - preset_name: Right 2.1.1
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e300000000000008fdfffffffff7fbfff7fbfff7fbfff7fbfff7fbfff7fbffffffffffe7ffffffffffdfefffdfefffdfefffdfefffdfefffdfefffffffffbfdfffffffff7fbfff7fbfff7fbfffffbfff7fbfff7fbffffffffffe7ffffffffffdfefffdfefffdfefffdfefffdfefffdfefffffffffbfdfffffffff7fbfff7fbfff7fbfff7fbfff7fbfff7fbffffffffffe7ffffffffffdfefffffffffbfdfffffffff7fbffffffffffe7ffffffffffdfefffffffffbfdfffffffff7
        - preset_name: Right 2.1.2
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e300000000000008fdfffffffff7fbfff7fbfff7fbfff7fbfff7fbfff7fbffffffffffe7ffffffffffdfefffdfefffffefffffefffffefffdfefffffffffbfdfffffffff7fbfff7fbfffffbfffffbfffffbfff7fbffffffffffe7ffffffffffdfefffdfefffffefffffefffffefffdfefffffffffbfdfffffffff7fbfff7fbfff7fbfff7fbfff7fbfff7fbffffffffffe7ffffffffffdfefffffffffbfdfffffffff7fbffffffffffe7ffffffffffdfefffffffffbfdfffffffff7
        - preset_name: Right 2.1.3
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e300000000000008fdfffffffff7fbfffffbfffffbfffffbfffffbfffffbffffffffffe7ffffffffffdfefffffefffffefffffefffffefffffefffffffffbfdfffffffff7fbfffffbfffffbfffffbfffffbfffffbffffffffffe7ffffffffffdfefffffefffffefffffefffffefffffefffffffffbfdfffffffff7fbfffffbfffffbfffffbfffffbfffffbffffffffffe7ffffffffffdfefffffffffbfdfffffffff7fbffffffffffe7ffffffffffdfefffffffffbfdfffffffff7
        - preset_name: Right 2.1.4
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e300000000000008fdfffffffff7fbfffffbfffffbfffffbfffffbfffffbffffffffffe7ffffffffffdfefffffefffffefffffefffffefffffefffffffffbfdfffffffff7fbfffffbfffffbfffffbfffffbfffffbffffffffffe7ffffffffffdfefffffefffffefffffefffffefffffefffffffffbfdfffffffff7fbfffffbfffffbfffffbfffffbfffffbffffffffffe7ffffffffffdfefffffffffffdfffffffffffbfffffffffff7ffffffffffffefffffffffffdfffffffff7
        - preset_name: Right 2.2
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e300000000000008fdfffffffffffbfffffbfffffbfffffbfffffbfffffbffffffffffe7ffffffffffffefffffefffffefffffefffffefffffefffffffffbfdfffffffffffbfffffbfffffbfffffbfffffbfffffbffffffffffe7ffffffffffffefffffefffffefffffefffffefffffefffffffffbfdfffffffffffbfffffbfffffbfffffbfffffbfffffbffffffffffe7ffffffffffffefffffffffffdfffffffffffbfffffffffff7ffffffffffffefffffffffffdfffffffff7
        - preset_name: Right 2.3
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e300000000000008fdfffffffffffbfffffbfffffbfffffbfffffbfffffbfffffffffff7ffffffffffffefffffefffffefffffefffffefffffefffffffffffdfffffffffffbfffffbfffffbfffffbfffffbfffffbfffffffffff7ffffffffffffefffffefffffefffffefffffefffffefffffffffffdfffffffffffbfffffbfffffbfffffbfffffbfffffbfffffffffff7ffffffffffffefffffffffffdfffffffffffbfffffffffff7ffffffffffffefffffffffffdffffffffff
        - preset_name: Right 3.1.1
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e300000000000008fdfffffffffffbfffffbfffffbfffffbfffffbfffffbfffffffffff7ffffffffffffefffffefffffefffffefffffefffffefffffffffffdfffffffffffbfffffbfffffffffffbfffffbfffffbfffffffffff7ffffffffffffefffffefffffefffffefffffefffffefffffffffffdfffffffffffbfffffbfffffbfffffbfffffbfffffbfffffffffff7ffffffffffffefffffffffffdfffffffffffbfffffffffff7ffffffffffffefffffffffffdffffffffff
        - preset_name: Right 3.1.2
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e300000000000008fdfffffffffffbfffffbfffffbfffffbfffffbfffffbfffffffffff7ffffffffffffefffffffffffffffffffffffefffffefffffffffffdfffffffffffbfffffffffffffffffffffffbfffffbfffffffffff7ffffffffffffefffffffffffffffffffffffefffffefffffffffffdfffffffffffbfffffbfffffbfffffbfffffbfffffbfffffffffff7ffffffffffffefffffffffffdfffffffffffbfffffffffff7ffffffffffffefffffffffffdffffffffff
        - preset_name: Right 3.1.3
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e300000000000008fdfffffffffffffffffffffffffffffffffffffffffbfffffffffff7ffffffffffffffffffffffffffffffffffffffffffefffffffffffdfffffffffffffffffffffffffffffffffffffffffbfffffffffff7ffffffffffffffffffffffffffffffffffffffffffefffffffffffdfffffffffffffffffffffffffffffffffffffffffbfffffffffff7ffffffffffffefffffffffffdfffffffffffbfffffffffff7ffffffffffffefffffffffffdffffffffff
        - preset_name: Right 3.1.4
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e300000000000008fdfffffffffffffffffffffffffffffffffffffffffbfffffffffff7ffffffffffffffffffffffffffffffffffffffffffefffffffffffdfffffffffffffffffffffffffffffffffffffffffbfffffffffff7ffffffffffffffffffffffffffffffffffffffffffefffffffffffdfffffffffffffffffffffffffffffffffffffffffbfffffffffff7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffdffffffffff
        - preset_name: Right 3.2
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e300000000000008fffffffffffffffffffffffffffffffffffffffffffbffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffffffffffffffffffffffffffffffffffffffffffffffffffbffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffffffffffffffffffffffffffffffffffffffffffffffffffbfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffdffffffffff
        - preset_name: Right 3.3
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e300000000000008ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        - preset_name: RLC 1
          visible_pieces: 00000000000000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e3000c7e3f9fc70008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e308fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc70008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e308fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc70008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000000000000000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e3000c7e3f9fc700000000000000
        - preset_name: RLC 2
          visible_pieces: 00f9fc7e3f1000e3f9fc7e3000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e3000c7e3f9fc70008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e308fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc70008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e308fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc70008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000000000000000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e3000c7e3f9fc700000000000000
        - preset_name: RLC 3
          visible_pieces: 00f9fc7e3f1000e3f9fc7e3f10c7e3f9fc7e308fc7e3f9fc700f9fc7e3f9f00e3f9fc7e3f10c7e3f9fc70008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e308fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc70008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e308fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc70008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000000000000000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e3000c7e3f9fc700000000000000
        - preset_name: RLC 4
          visible_pieces: 00f9fc7e3f10c7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f9fc7e3f10c7e3f9fc70008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e308fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc70008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e308fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc70008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000000000000000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e3000c7e3f9fc700000000000000
        - preset_name: RLC 5
          visible_pieces: 00f9fc7e3f10c7ffffffff7f9feffffffffe3fdffffffffd7ebffffffffbfc7ffffffff7f10c7e3f9fc70008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e308fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc70008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000e3f9fc7e308fef7f9fef7f9fef7f9fef7f9fef7f10c7e3f9fc70008fc7e3f9f00ebffd7ebffd7ebffd7ebffd7ebffd700f9fc7e3f1000000000000000c7e3f9fc70008fc7e3f9f0000f9fc7e3f1000e3f9fc7e3000c7e3f9fc700000000000000
        - preset_name: ELC 1
          visible_pieces: 00000000000000000000000000000000000000000000000000000000000000000000000008f00000000008f70381c060ff140028140028140028140028140028ff060381c0efff1c060381cf701080601080601080601080601080ef381c06038fff70381c060ff140028140028140028140028140028ff060381c0efff1c060381cf701080601080601080601080601080ef381c06038fff70381c060ff140028140028140028140028140028ff060381c0ef10000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: ELC 2
          visible_pieces: 00000000000000000000000000000000000000000000000000000000000000000000000008f20180402008f70381c060ff140028140028140028140028140028ff060381c0efff1c060381cf701080601080601080601080601080ef381c06038fff70381c060ff140028140028140028140028140028ff060381c0efff1c060381cf701080601080601080601080601080ef381c06038fff70381c060ff140028140028140028140028140028ff060381c0ef10000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: ELC 3
          visible_pieces: 00000000000000000000000000000000000000000000000000000000000000000000000008f201804020ebf70381c060ff140028140028140028140028140028ff060381c0efff1c060381cf701080601080601080601080601080ef381c06038fff70381c060ff140028140028140028140028140028ff060381c0efff1c060381cf701080601080601080601080601080ef381c06038fff70381c060ff140028140028140028140028140028ff060381c0ef10000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: ELC 4
          visible_pieces: 00000000000000000000000000000000000000000000000000000000000000000000000008f281c06038ebf70381c060ff140028140028140028140028140028ff060381c0efff1c060381cf701080601080601080601080601080ef381c06038fff70381c060ff140028140028140028140028140028ff060381c0efff1c060381cf701080601080601080601080601080ef381c06038fff70381c060ff140028140028140028140028140028ff060381c0ef10000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: ELC 5
          visible_pieces: e3000000000000000000000000000000000000000000000000000000000000000000000008f281c06038ebf70381c060ff140028140028140028140028140028ff060381c0efff1c060381cf701080601080601080601080601080ef381c06038fff70381c060ff140028140028140028140028140028ff060381c0efff1c060381cf701080601080601080601080601080ef381c06038fff70381c060ff140028140028140028140028140028ff060381c0ef10000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: ELC 6
          visible_pieces: eb040201800000000000000000000000000000000000000000000000000000000000000008f281c06038ebf70381c060ff140028140028140028140028140028ff060381c0efff1c060381cf701080601080601080601080601080ef381c06038fff70381c060ff140028140028140028140028140028ff060381c0efff1c060381cf701080601080601080601080601080ef381c06038fff70381c060ff140028140028140028140028140028ff060381c0ef10000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: ELC 7
          visible_pieces: eb040201808f00000000000000000000000000000000000000000000000000000000000008f281c06038ebf70381c060ff140028140028140028140028140028ff060381c0efff1c060381cf701080601080601080601080601080ef381c06038fff70381c060ff140028140028140028140028140028ff060381c0efff1c060381cf701080601080601080601080601080ef381c06038fff70381c060ff140028140028140028140028140028ff060381c0ef10000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: ELC 8
          visible_pieces: eb060381c0af00000000000000000000000000000000000000000000000000000000000008f281c06038ebf70381c060ff140028140028140028140028140028ff060381c0efff1c060381cf701080601080601080601080601080ef381c06038fff70381c060ff140028140028140028140028140028ff060381c0efff1c060381cf701080601080601080601080601080ef381c06038fff70381c060ff140028140028140028140028140028ff060381c0ef10000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: ELC 9
          visible_pieces: eb060381c0af08000000000000100000000000200000000000400000000000800000000008f281c06038ebf70381c060ff140028140028140028140028140028ff060381c0efff1c060381cf701080601080601080601080601080ef381c06038fff70381c060ff140028140028140028140028140028ff060381c0efff1c060381cf701080601080601080601080601080ef381c06038fff70381c060ff140028140028140028140028140028ff060381c0ef10000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: ELC 10
          visible_pieces: eb060381c0af28000000000040100000000080200000000001400000000002800000000008f281c06038ebf70381c060ff140028140028140028140028140028ff060381c0efff1c060381cf701080601080601080601080601080ef381c06038fff70381c060ff140028140028140028140028140028ff060381c0efff1c060381cf701080601080601080601080601080ef381c06038fff70381c060ff140028140028140028140028140028ff060381c0ef10000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: ELC 11
          visible_pieces: eb060381c0af28000000008040100000000180200000000201400000000402800000000808f281c06038ebf70381c060ff140028140028140028140028140028ff060381c0efff1c060381cf701080601080601080601080601080ef381c06038fff70381c060ff140028140028140028140028140028ff060381c0efff1c060381cf701080601080601080601080601080ef381c06038fff70381c060ff140028140028140028140028140028ff060381c0ef10000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: ELC 12
          visible_pieces: eb060381c0af280000000080601000000001c020000000028140000000040380000000080af281c06038ebf70381c060ff140028140028140028140028140028ff060381c0efff1c060381cf701080601080601080601080601080ef381c06038fff70381c060ff140028140028140028140028140028ff060381c0efff1c060381cf701080601080601080601080601080ef381c06038fff70381c060ff140028140028140028140028140028ff060381c0ef10000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: OLC
          visible_pieces: fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff70000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: 2c PLC
          visible_pieces: 000000100000000000200000000000400000040201f7402010000001000000000002000000000004000000000008000000000000000000808101000000000000000000100000000000200000000000000000020604000000000000000000400000000201e340200808101808101ebffd780810180810100402c7804000000002000000000000000000206040000000000000000004000000000008000000000000000000808101000000000000000000100000000000000000000000400000000000800000000402c7804000000002000000000004000000000000000000
        - preset_name: PLC cross
          visible_pieces: 000000000000c7ffffffff7f9feffffffffe3fdffffffffd7ebffffffffbfc7ffffffff7f9feffffffffe30000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: PLC F2L
          visible_pieces: 000000000000effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff70000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: PLC LL
          visible_pieces: fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff70000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        - preset_name: Done
          visible_pieces: ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ```

## Summary

1. **4-Cross** — Solve four out of the six cross pieces
2. **Middle Block** — Solve four 2c3c pairs between the four cross pieces
3. **Left Block** — Blockbuild or pair pieces to solve the Left Cell
4. **Right Block** — Blockbuild or pair pieces to solve the Right Cell
5. **OLL-4** - Orient LC 2c, 3c, and 4c pieces using 3D algorithms
6. **PLL-4** - Permute LC 2c, 3c, and 4c pieces using 3D techniques

## Steps

### 4-Cross

Solve the four 2c cross pieces in a ring in the M slice. Leave the L and R cross pieces unsolved.

<figure markdown="span">
  ![4-cross](https://assets.hypercubing.xyz/img/virt/3block/4cross.png){width="50%"}
</figure>

### Middle Block

!!! tip
    For the entirety of F2L, the last layer is held on the I cell, as opposed to [CFOP](/methods/3x3x3x3/cfop.md) where it is held on the U cell. This allows us to see more information at once.

Create and insert 4 F2L-a (2c3c) pairs into the 4/6 cross. This will solve 2/3 of the M slice. Because the Left and Right cells don't have their cross pieces, you can use them to aid with building and inserting the pairs.

<figure markdown="span">
  ![Middle block](https://assets.hypercubing.xyz/img/virt/3block/middle_block.png){width="50%"}
</figure>

### Left Block

Solve the Left cell. This is done in 3 blocks, hence the name of the method. The first block consists of the cross edge, followed by two 2c3c F2L-a pairs that are opposite of each other. This solves the middle column of the left cell. The final two blocks consist of a 2c3c pair, and two 3c4c pairs.

<figure markdown="span">
  ![Left block](https://assets.hypercubing.xyz/img/virt/3block/left_block.png){width="50%"}
</figure>

### Right Block

Solve the Right cell. This is also done by breaking it up into the 3 blocks, except now you don't have an empty opposite cell to aid you in making pairs. You could just solve the cross edge, and then finish the whole solve using [CFOP](/methods/3x3x3x3/cfop.md) style F2L and Last Cell. You can also do it the 3 blocks way, except having less freedom means that it is slightly trickier to set up the correct cases.

<figure markdown="span">
  ![Right block](https://assets.hypercubing.xyz/img/virt/3block/right_block.png){width="50%"}
</figure>

### Last Layer

This is done in the exact same way as [CFOP](/methods/3x3x3x3/cfop.md#oll-4).

## Big cubes

Pair up only the pieces you need during the step of 3-block you're on. For example: after solving 4 centers, pair up 4 cross ridges. For last cell, you can either just orient everything, and then do an RKT 4^3^ solve, or you can pair everything and end up with an RKT 3^3^ solve.
