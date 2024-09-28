# Software

Since building [physical representations](/puzzles/physical/index.md) of higher-dimensional puzzles is challenging, we use computer software to simulate them.

## What program should I download?

We recommend [Hyperspeedcube][hsc] to get started.

If you want macro support (recorded sequences of moves) or other 4D puzzles, [Magic Cube 4D][mc4d] is a good option.

- For 5D+ puzzles: [Magic Cube 5D][mc5d], [Magic Cube 7D][mc7d], and [Magic Puzzle Ultimate][mpu]
- For puzzles in non-Euclidean geometries: [MagicTile][mt]
- For 3D puzzles: [pCubes][pcubes]

For hypercubing on mobile devices, see [Android apps](#android-apps) or [iOS apps](#ios-apps).

## General cubing & hypercubing

<!-- %features{mksftMTcpv} -->
<!-- %platforms{wlab} -->

??? question "What do the icons mean?"
    - :material-mouse: Mouse controls
    - :material-keyboard: Keyboard controls
    - :material-keyboard-settings: Customizable keyboard controls
    - :material-magnify: Find/filter piece by color
    - :material-eye: Find/filter pieces by type
    - :material-timer: Timer
    - :material-script-text-play: Macros
    - :material-form-textbox: Move input
    - :material-palette-swatch: Custom colors
    - :material-pencil-plus: Custom puzzles
    - :material-virtual-reality: VR support

| Program                                     |                                                        Platforms | Features              | Puzzles                 |
| ------------------------------------------- | ---------------------------------------------------------------: | --------------------- | ----------------------- |
| [Hyperspeedcube][hsc]                       |           [:material-language-rust:][hsc-src] • %platforms{wlab} | %features{mKsf___c__} | {1-9}^{3-4}^            |
| [Magic Cube 4D][mc4d]                       |          [:material-language-java:][mc4d-src] • %platforms{wla_} | %features{m____M_cp_} | 4D via Schläfli symbol  |
| [MagicTile][mt]                             |          [:material-language-csharp:][mt-src] • %platforms{wla_} | %features{m____M_cp_} | 2D tilings              |
| [Magic Puzzle Ultimate][mpu]                |         [:material-language-csharp:][mpu-src] • %platforms{w___} | %features{m__ftM_cp_} | 3D+ doctrinaire         |
| [Magic Cube 7D][mc7d]                       |        [:material-language-csharp:][mc7d-src] • %platforms{w___} | %features{m_sftM_c__} | {3-5}^{4-7}^            |
| [Magic Cube 5D][mc5d]                       |           [:material-language-cpp:][mc5d-src] • %platforms{w___} | %features{m_sf_M_c__} | {2-7}^5^                |
| [Magic Cube 4D VR][mc4d-vr]                 |                              :material-unity: • %platforms{wl__} | %features{_________v} | 3^4^                    |
| [Flat Hypercube][flat]                      |          [:material-language-rust:][flat-src] • %platforms{wla_} | %features{_ks_______} | {1-19}^{1-10}^          |
| [Gelatinbrain][gelatinbrain][^gelatinbrain] |                      :material-language-java: • %platforms{wla_} | %features{m_____T___} | many cursed things      |
| [pCubes][pCubes]                            |                                                 %platforms{w___} | %features{m___t___p_} | nearly every 3D puzzle  |
| [Ultimate Magic Cube][umc]                  |                                                 %platforms{w___} | %features{m___t___p_} | platonic 3D             |
| [Ultimate Magic Cube 2][umc]                |                    :material-language-csharp: • %platforms{w___} | %features{m___t_____} | platonic + misc 3D      |
| [Twizzle Explorer][twizzle]                 | [:material-language-javascript:][twizzle-src] • %platforms{___b} | %features{mk____T_p_} | many 3D puzzles         |
| [IsoCubeSim][ics]                           |                      :material-language-java: • %platforms{wla_} | %features{m___t___p_} | AxBxC, N-layer megaminx |
| [Geraniums Pot][gpot]                       | [:material-language-python:][gpot-src] • %platforms{wl__} | %faetures{m_______p_} | rotating-circle puzzles |

[hsc]: /software/hyperspeedcube.md
[hsc-src]: https://github.com/HactarCE/Hyperspeedcube
[mc4d]: /software/magiccube4d.md
[mc4d-src]: https://github.com/cutelyaware/magiccube4d
[mt]: http://roice3.org/magictile/
[mt-src]: https://github.com/roice3/MagicTile
[mpu]: /software/magicpuzzleultimate.md
[mpu-src]: https://github.com/cutelyaware/MPUlt
[mc5d]: http://www.gravitation3d.com/magiccube5d/
[mc5d-src]: https://github.com/roice3/MagicCube5D
[mc7d]: https://superliminal.com/andrey/mc7d/
[mc7d-src]: https://superliminal.com/andrey/mc7d/MC7D-src-orig.zip
[mc4d-vr]: https://store.steampowered.com/app/2413000/Magic_Cube_4D_VR/
[flat]: https://github.com/milojacquet/flat-hypercube
[flat-src]: https://github.com/milojacquet/flat-hypercube
[gelatinbrain]: https://github.com/Hypercubers/gelatinbrain/
[pCubes]: https://twistypuzzles.com/forum/viewtopic.php?t=27054
[umc]: http://www.ultimatemagiccube.com/
[twizzle]: https://alpha.twizzle.net/explore/
[twizzle-src]: https://github.com/cubing/cubing.js
[ics]: https://mzrg.com/rubik/iso/
[gpot]: https://github.com/grigorusha/GeraniumsPot/
[gpot-src]: https://github.com/grigorusha/GeraniumsPot/

[^gelatinbrain]: Full name: gelatinbrain's Virtual Magic Polyhedra (permutationpuzzles)

## Specific puzzles

| Program                                     |                                                 Platforms | Features              | Puzzle                   |
| ------------------------------------------- | --------------------------------------------------------: | --------------------- | ------------------------ |
| [Magic Hyperbolic Tile][mht633]             |                                          %platforms{w___} | %features{m_sftM_c__} | {6,3,3} (7 quotients)    |
| [Magic Simplex 5D][ms5d]                    | [:material-language-csharp:][ms5d-src] • %platforms{w___} | %features{m_sftM_c__} | 5D simplex (+ recuts)    |
| [Magic120Cell][m120c]                       |   [:material-language-cpp:][m120c-src] • %platforms{w___} | %features{m_sf_M_c__} | 120-cell (+ recolorings) |
| [Nan Ma's 11-cell][11cell]                  |               :material-language-java: • %platforms{wla_} | %features{m__f_MTc__} | 11-cell                  |

[ms5d]: https://superliminal.com/andrey/ms5d/
[ms5d-src]: https://superliminal.com/andrey/ms5d/Simplex5dSrc.zip
[m120c]: http://www.gravitation3d.com/magic120cell/
[m120c-src]: https://github.com/roice3/Magic120Cell
[11cell]: https://superliminal.com/cube/ElevenCell.jar
[mht633]: https://superliminal.com/andrey/mht633/

### 1D and 2D puzzles

- [k-Card Game](https://masonhorne.github.io/k-Card-Game/)
- [Loopover](https://loopover.xyz/)
- [Heav's Relocation Puzzle](https://github.com/heav-4/relocation)
- [Slidysim](https://www.slidysim.com/)
- [Luna's "Green" (generalization of Lights Out and Green The Board)](https://github.com/Sonicpineapple/Green)

### Complex & laminated puzzles

- [Complex Loopover](https://milojacquet.com/loopover/complex)
- [Complex Cube](https://twistypuzzles.com/forum/viewtopic.php?f=1&t=22353)
- [Luna's Complex Puzzles](https://sonicpineapple.github.io/Complex-Puzzles/Complex.html)
- [Milo's laminated puzzles](https://github.com/milojacquet/laminated)
- [Ema's Complex Hemicube Puzzle](https://github.com/OneTrickPoro/Complex-Hemicube-Puzzle)

### Other

- [Nan Ma's puzzles](https://www.nan.ma/) (Reflecube, Lollipop, Clockwork Cube, and more)
- [Akkei's physical 3^4^ program][akkei-phys]
- [Rayzchen's 3to4++](https://github.com/rayzchen/3to4pp) (Physical 3^4^)
- [Arnaud Chéritat's Hungarian Rings](https://www.math.univ-toulouse.fr/~cheritat/AppletsDivers/AnneauxHongrois/)
- [Magic Cube 3D](https://github.com/rzhao271/MC3D/releases/latest/)
- [MagmaMcFry's Quaternion Cube](https://magmamcfry.github.io/QuaternionCube/)
- [Banderson's "sus non-associative puzzle"](https://github.com/lopidoff/sus-non-ass-puzzle-family)

[akkei-phys]: https://drive.google.com/drive/folders/1xBEKkGYIFKSAcIgJjPCIx_W0vdJawuZ0

## Android apps

Hypercubing on mobile devices is not recommended; however, if this is your only option, these apps are available for Android:

- [Magic Cube 4D (Raynefork)](https://play.google.com/store/apps/details?id=me.rayzz.magiccube4d) (recommended)
- <strike>[Magic Cube 4D](https://play.google.com/store/apps/details?id=com.superliminal.magiccube4d)</strike> (superceded by Raynefork)
- [The Tesseract Puzzle](https://play.google.com/store/apps/details?id=com.MadMagics.OpenGL_Shaders)
- [4D Hypercube Puzzle](https://play.google.com/store/apps/details?id=com.tesseract_game&hl=en_US&gl=US)

## iOS apps

There are no known apps for hypercubing on iOS.

If you're able to connect an external mouse & keyboard, the [web version of Hyperspeedcube][hsc-web] may work on mobile devices but it's not officially supported.

[hsc-web]: https://hypercubing.xyz/hyperspeedcube/

## Tools

- [Orb](https://milojacquet.com/twisty/orb), for planning puzzle cut depths
- [RocKeT](https://github.com/HactarCE/rocket), for finding RKT cancels for 3D algorithms
- [Hypersolve](https://github.com/ajtaurence/Hypersolve), for generating short 2^4^ solutions and scrambles

## Games

This is not a complete list of 4D games. This is specifically 4D software that hypercubers often recommend for understanding 4D geometry better.

- [4D Blocks](https://www.urticator.net/blocks/)

## Visualizations

- [IMAC2 Rubik4D by Oradimi, melokye, and MMeche](https://github.com/melokye/IMAC2_Rubik4D)
