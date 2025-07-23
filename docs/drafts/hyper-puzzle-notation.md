# Hyper Puzzle Notation Standard (HPN)

!!! warning "This is a draft"

    This document is NOT final and might be outdated! Before making anything based on this (including software, documentation, or learning resources), please ping Hactar and/or Luna.

This spec describes conventions used in the hypercubing community. As usual with our documentation, this is sourced from a few places:

- Notation that is already in use (descriptive)
- Notation that addresses existing unmet needs (prescriptive)
- Notation that addresses known future needs (speculative)

Parts of the guide are notated as falling into one of these three categories.

- **Descriptive** notation is probably very difficult to change because it is already in use in conversation, learning resources, and file formats.
- **Prescriptive** notation is somewhat difficult to change because it will probably start being used shortly after this draft has been published.
- **Speculative** notation is relatively easy to change because it will probably not see use until some future time, particularly when [Hyperspeedcube 2](github.com/HactarCE/Hyperspeedcube) supports such puzzles.[^hsc2]

[^hsc2]: Most puzzle programs store log files using internal IDs; Hyperspeedcube uses plaintext notation to leave room for changing how puzzles are generated in ways that may result in different ID assignments. In other words, log file compatibility should _not_ depend the implementation details of the puzzle generator and simulator; therefore every puzzle needs some stable plaintext notation scheme, ideally one that is usable by humans as well.

## Syntax

### EBNF

Syntax descriptions in this document use [EBNF](https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form). Summary:

- `symbol?` is an optional `symbol`
- `symbol+` is at least one of `symbol`
- `symbol*` is zero or more of `symbol`
- `a | b` is either `a` or `b`
- `"~"` is the literal character `~` (and similarly for another other string of characters)

We use the following character classes:

- `[1-9]` is one of the digits `123456789`
- `[0-9]` is one of the digits `0123456789`
- `letter` SHOULD be one character from the Unicode "Letter" [character classes](https://www.compart.com/en/unicode/category)
    - It MUST include the following:
        - `ABCDEFGHIJKLMNOPQRSTUVWXYZ` (uppercase Latin)
        - `abcdefghijklmnopqrstuvwxyz` (lowercase Latin)
        - `ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ` (subset of uppercase Greek)
        - `αβγδεζηθικλμνξοπρστυφχψω` (subset of lowercase Greek)
    - It MUST exclude all non-letter Unicode characters (particularly non-alphabetic ASCII characters: control codes, whitespace, punctuation, and numbers)
- `space` is one character from the set ` ` (space, U+0020), horizontal tab (U+0009), carriage return (U+000D), or newline (U+000A)

### Move syntax

```
underscore = "_"
hyphen = "-"
apostrophe = "'"
comma = ","
dotdot = ".."
caret = "^"
tilde = "~"
dot = "."
arrow = "->"
at-sign = "@"

positive-int = [1-9] [0-9]*
nonnegative-int = "0" | positive-int
int = hyphen? positive-int

move-family = (letter | underscore)+

multiplier = nonnegative-int? apostrophe?
layer-range = int (dotdot int)?
uninverted-layer-mask = "" |
                        positive-int (hyphen positive-int)? |
                        "{" layer_range (comma layer_range)* "}"
layer-mask = tilde? uninverted-layer-mask
transform-constraint = move-family |
                       move-family arrow move-family |
transform = "[" transform-constraint (comma transform-constraint)* "]"

twist = layer-mask move-family transform? multiplier
rotation = at-sign (move-family | transform) multiplier
move = twist | rotation
```

Notes:

- `~` inverts the layer mask for the subsequent move

Examples of transforms:

- `[F,I,R->U]` on 3^4 describes a transform that keeps `F` and `I` fixed and takes `R` to `U`
- `[R->U]` on 3^n describes a transform in the plane of `R` and `U` that takes `R` to `U`
- `[R->L]` on 3^3 is ambiguous
- `[R->L,U->F]` on 3^3 describes a 180-degree rotation that takes `R` to `L` and takes `U` to `F`

#### Examples of moves

- `R`
- `R'`
- `R2`
- `R2'`
- `IF2`
- `3Bw'`
- `2-6QwErTy`
- `13L`
- `{1..3,5..7}UR2'`
- `{2..-2}L` = generalized `M` move
- `U[R->L]` = `U2` or `U2'`
- `@[U->R]` = `z`
- `@F` = `z`

### Move sequence syntax

```
prefix-symbol = "" | "!" | "&" | "^"

repeatable-unit = move |
                  group |
                  commutator |
                  conjugate |
                  dot

repeated-unit = repeatable-unit multiplier

move-sequence = space* (repeated-unit (space+ repeated-unit)*)? space*

group = prefix-symbol "(" move-sequence ")"
conjugate = "[" move-sequence ":" move-sequence "]"
commutator = "[" move-sequence "," move-sequence "]"
```

Notes:

- `.` as a repeatable unit indicates a pause _(**descriptive** from other communities for solve reconstructions)_
- `[A, B]` and `[A: B]` are [commutator notation](https://www.speedsolving.com/wiki/index.php/Commutators_and_Conjugates) _(**descriptive**)_

Additionally, `//` and any characters after it are ignored. (This can be used to add comments.) _(**descriptive** from other communities for solve reconstructions)_

Group prefix symbols:

- `&` = simultaneous move group (animate simultaneously; undo/redo in one step) _(**prescriptive**)_
- `!` = macro (animate quickly or skip animation; undo/redo in one step) _(**prescriptive**)_
- `^` = NISS (do not execute normally; execute inverse at end) _(**prescriptive** from Lucas Garron for 3D FMC)_

Note that the parens are required after group prefix symbols. `^[R, U]` and `^R` are INVALID and must instead be written as `^([R, U])` and `^(R)` respectively.

## Move family conventions

This section defines common conventions for move families. These should be considered when developing notation for new puzzles. These are not strict rules.

- Uppercase Latin alphabet: `ABCDEFGHIJKLMNOPQRSTUVWXYZ`
- Uppercase Greek alphabet: `ΓΔΘΛΞΠΣΦΨΩ` (excluded letters that are similar to Latin letters)
- Lowercase Latin alphabet: `abcdefghijklmnopqrstuvwyxz`
- Lowercase Greek alphabet
    - Large lowercase: `βδζθλξ`
    - Small lowercase: `αεηκμπτφχψω` (excluding letters that are similar to Latin letters)

Other Greek letters are recommended to NOT be used because they are too similar in appearance to Latin letters.

### Uppercase Latin alphabet (semantic)

_This section is **descriptive**._

| Letter | Common uses             |
| ------ | ----------------------- |
| A      | Anterior (5D+)          |
| B      | Back (3D-)              |
| C      |                         |
| D      | Down (2D-)              |
| E      | Equitorial (2D slice)   |
| F      | Front (3D+)             |
| G      |                         |
| H      |                         |
| I      | In (4D-)                |
| J      |                         |
| K      |                         |
| L      | Left (1D-)              |
| M      | Middle (1D slice)       |
| N      |                         |
| O      | Out (4D+)               |
| P      | Posterior (5D-)         |
| Q      |                         |
| R      | Right (1D-)             |
| S      | Standing (3D slice)     |
| T      | "Top" (generalized F2L) |
| U      | Up (2D+), 6th axis      |
| V      |                         |
| W      |                         |
| X      |                         |
| Y      |                         |
| Z      |                         |

The unused letters here are reserved for execution notation, for variable names, for ad-hoc notation, or for specific puzzles (e.g., `X` and `Y` in 120-cell notation).

Other possible **prescriptive** uses:

- For megaminx, prefix `P` meaning "para-"
- For icosahedron, `P` meaning "portside" and `S` meaning "starboard"

Other possible **speculative** uses:

- For 120-cell, `X` and `Y`[^120cell]

[^120cell]: The facets of the 120-cell can be divided into eight 15-cell clusters, each containing 12 facets corresponding to faces of a dodecahedron plus three extra ones. Those three extra ones are called `I` ("In"), `X` and `Y`. Each cluster corresponds to one facet of a hypercube.

### Uppercase alphabet (sequential)

_This section is **speculative**._

The uppercase letters `A`-`Z` are often used to name elements in an ordered sequence, such as the rectangular faces of a polygonal prism. If there are more than 26 names needed, a single letter from the uppercase Greek alphabet may be added as a prefix, in the order `ΓΔΘΛΞΠΣΦΨΩ`:

| Letter sequence | Number |
| --------------- | ------ |
| A               | 1      |
| B               | 2      |
| ...             | ...    |
| Z               | 26     |
| ΓA              | 27     |
| ΓB              | 28     |
| ...             | ...    |
| ΓZ              | 52     |
| ΔA              | 53     |
| ...             | ...    |
| ΩZ              | 286    |

The {100}x{4} duoprism serves as an example of a puzzle that requires more than 26 sequential names.[^hundredagonal-duoprism]

[^hundredagonal-duoprism]: This puzzle was created as a joke but has actually been solved. It has 104 cells, which in this proposal would be named `αA`, `αB`, ..., `αΘU`, `αΘV`, `γA`, `γB`, `γC`, `γD`

### Lowercase Latin alphabet (semantic)

_This section is **descriptive**, except for jumbling notation which is **speculative**._

- Specialty uses in 3D notation (`rludfb`, `mes`)
- 3D whole-puzzle rotations (one letter from `xyz`)
- 4D+ whole-puzzle rotations (two letters from `xyzwvu...`)

| Letter | Common uses                                          |
| ------ | ---------------------------------------------------- |
| a      |                                                      |
| b      | `2Bw`                                                |
| c      |                                                      |
| d      | `2Dw`                                                |
| e      | `{2..-2}E`                                           |
| f      | `2Fw`                                                |
| g      |                                                      |
| h      | Half turn (jumbling)                                 |
| i      |                                                      |
| j      | First jumble angle                                   |
| k      | Second jumble angle                                  |
| l      | `2Lw`                                                |
| m      | `{2..-2}M`                                           |
| n      |                                                      |
| o      |                                                      |
| p      |                                                      |
| q      |                                                      |
| r      | `2Rw`                                                |
| s      | `{2..-2}S`                                           |
| t      |                                                      |
| u      | `2Uw`                                                |
| v      | Whole-puzzle rotation around twist/element, 5th axis |
| w      | Wide move suffix, 4th axis                           |
| x      | 1st axis                                             |
| y      | 2nd axis                                             |
| z      | 3rd axis                                             |

See [Jumbling notation](#jumbling-notation) for more about `h`, `j`, and `k`.

In 3D, a single axis letter indicates a rotation around that axis. E.g., `y` is a rotation around the Y axis from +X to +Z; its inverse is `y'`.

In 4D+, two axis letters indicates a rotation in that plane from one axis to the other. E.g., `zw` is a rotation from +Z to +W; its inverse is `zw'` or `wz`.

In 5D, two axis letters may be used after an axis name for [execution notation](#execution-notation).

### Lowercase Greek alphabet (sequential)

_This section is **speculative**._

For when there are multiple Latin groups, they can be distinguished using a small lowercase Greek prefix. For example:

| Group | Names                 |
| ----- | --------------------- |
| 1     | `αA`, `αB`, `αC`, ... |
| 2     | `γA`, `γB`, `γC`, ... |
| 3     | `εA`, `εB`, `εC`, ... |

### Cube axes

_This section is **descriptive**. The use of Greek letters is thus far only used in [Flat Hypercube](https://github.com/milojacquet/flat-hypercube) and is more pliable than other descriptive choices._

Cube axes use the following symbols:

| Dimension | Axis name | Side (+/-) |
| --------- | --------- | ---------- |
| 1         | X         | R, L       |
| 2         | Y         | U, D       |
| 3         | Z         | F, B       |
| 4         | W         | O, I       |
| 5         | V         | A, P       |
| 6         | U         | Γ, Δ       |
| 7         |           | Θ, Λ       |
| 8         |           | Ξ, Π       |
| 9         |           | Σ, Φ       |
| 10        |           | Ψ, Ω       |

These can also serve as letters or letter pairs for when a handful of additional axes are needed and the preferred uppercase Latin letters are unavailable. For example, a megaminx prism (4D) uses `I` and `O` for the two additional axes, but if some other 3D puzzle already used those letters then a 4D prism of it could use `Γ` and `Δ` for the two additional axes.

### Execution notation

_This section is **descriptive**._

Keybinds for high-dimensional puzzles typically assign short (1-2 letter) uppercase names to axes and short (1-2 letter) lowercase names to **twist directions**. An axis and a twist direction can be combined to specify a move.

Examples:
- 3^4 uses the letters `x`, `y`, and `z` after an axis name to specify a twist.
- Polygonal duoprisms reuse the hypercube letters `I`, `U`, `D`, `F`, `R`, `L` (all except `O` and `B`)

### Jumbling notation

_This section is **speculative**._

- `h` indicates half of a doctrinaire turn (common on Bagua and mixup cubes)
- `j` indicates some other jumbling angle
- `k` indicates a second jumbling angle, for when `j` is already taken

## Rationale

### Why use Greek letters?

_The use of non-ASCII letters is largely **speculative**._

In high dimensions, Greek letters become useful.

- Greek letters provide an extension to the Latin alphabet with more nuanced aesthetics, aiding readability.
    - Greek uppercase letters fit in well with Latin uppercase letters.
    - Greek lowercase letters contrast very strongly with Latin uppercase letters.
        - Small lowercase letters provide a good set of prefixes.
        - Large lowercase letters are reserved for future use.
- We want to avoid lowercase letters, because this conflicts with 3D conventions that use lowercase letters for wide moves or inner moves. We also want to avoid uppercase letters with existing uses (M, E, S, P, x, y, z, w, v).
    - This is partially a compatibility concern, but mostly a psychological semantic one. Humans reading lowercase letters may have misconceptions about their uses based on uses in other cubing notation.
- Greek letters allow us to keep facet names [prefix-free](https://en.wikipedia.org/wiki/Prefix_code) while still using single-character names for sequences of 26 elements of fewer.
    - Using only the Latin alphabet, we would get `A`, `B`, ..., `Z`, `AA` (not prefix-free!)
    - We could force names to be 2 letters long when there's more than 26 of them, but now the rule becomes more complicated.
    - This especially simplifies code to generate these puzzles; `generate_nth_uppercase_name()` is now a pure function depending only on `n` and not the total number of names.
- We want to preserve uppercase letters for ad-hoc definitions, both for nonrigorous communication between humans and for rigorous move input.
- Writing moves manually using Greek letters is likely to be extremely rare outside a handful of people.
    - E.g., Duoprisms have ASCII execution notation for a common subset of moves.
- Flat Hypercube already uses greek letters for hypercubes of dimension 6+:
- We want to preserve certain letters for mathematical notation.
    - E.g., $G$ for the grip group
    - E.g., $S$ for "$S$-doctrinaire"

### Why curly-brace layer sets?

_Curly-brace layer sets are **descriptive**._

It is a very common convention in hypercubing software to hold down any set of number keys to apply a "layer mask" to a move. Given that individual moves may require many characters to write (such as `I[F->B,U->R]`) it is very awkward to require duplicating this many times.

- E.g., Suppose we want to write the 7^4 move `{1,3,5,7}IUR` using only ridge turns. (This is a contrived example because we _do_ have a way to write edge turns on n^4, but no some puzzles these moves can only be easily written using simultaneous move notation.) With layer sets, we can write `&({1,3,5,7}IF {1,3,5,7}IR2)`; without layer sets, we must write `&(IF 3IF 5IF 7IF IR2 3IR2 5IR2 7IR2)`.
    - We _could_ write it the long way, but we lose important semantics and it becomes much less readable.
    - Transform notation makes this problem even worse: `{1,3,5,7}I[U->R,F->B]` vs. `&(I[U->R,F->B] 3I[U->R,F->B] 5I[U->R,F->B] 7I[U->R,F->B])`
    - Any layer mask can be used for a single move in hypercubing software, and we treat it as a single move! It should be possible to express concisely in notation
- Checkerboard patterns on big cubes are a major example where this problem appears.
- Negative numbers count from the other side (generalized big cube algorithms!)
    - Generic middle slice on big cubes: `~{1,-1}R` or `{2..-2}R`

### Why invert layer masks?

_`~` is **speculative**._

- Complex 3^3 has an anti-`R` move (equivalent to `&(R x')`) that is _distinct_ from `Lw` (which does not exist) because `R` and `L` are no longer opposites.
    - Technically you could do `2R` by assuming the 6-axis 2-layer laminated construction but that's very unintuitive and does not generalize to ordinary 3^3.
- RKT cancels use "everything except `I`" extensively
    - E.g., `~IUR` for "the UR flip," which appears _constantly_ in RKT cancel algorithms.
- Another tool for notation that is generic with respect to number of layers in the puzzle.

### Why not `v` suffix for whole-puzzle rotations?

- `v` doesn't actually apply to twists; it applies to _elements_.
    - `URv` is a rotation around the `UR` edge, but software might not know how to concatenate two axes.
    - This doesn't generalize at all in higher dimensions.
    - This doesn't generalize to many shapes; e.g., most edges and all vertices on a polygonal prism do not correspond to rotations that preserve the puzzle symmetry.
- Syntax for rotations using arbitrary transforms is unclear.
    - `U[R->F]v`?
    - `Uv[R->F]`?
    - `v[R->F]`
    - `[R->F]v`?
- Lowercase `v` may refer to the 5th dimension, particularly in execution notation. (e.g., `xv` for the rotation from +X to +V)

### Why use `@` for whole-puzzle rotations?

_`@` is **speculative**._

- `~` on its own is more useful to mean "all except the first layer"
    - e.g., `~IUR` for the very common "UR flip" in RKT cancels on 3^4 (otherwise expressed as `{2..-1}IUR` or `{1..-2}OUR`)
- `*` is already used colloquially as a wildcard.
    - e.g., "You can do RKT using either `<RO*, I*>` or `<*O, ~I*>`."
- `@` has the mnemonic "all"

### Why have execution notation in addition to general notation?

_Execution notation is **descriptive**. The term "execution notation" itself is **prescriptive**._

- Execution notation is usually optimized for particular puzzles and particular viewpoints.
    - Execution notation often lacks access to certain moves.
- Execution notation might be more compact or require fewer symbols, making it easier to translate to/from keybinds.
- Execution notation may provide a way to translate moves between puzzles; e.g., `Uy` has meaning on both 3^4 and polygonal duoprisms even though these puzzles are very different.
- Execution notation can be defined ad-hoc.

## Open questions

- Some way to encode direction of 180-degree transforms
    - E.g., `@[R-U>L]` equivalent to `@F2'` (as opposed to `[R->L,U->D]` which unambiguously describes a transformation but does not specify the direction of rotation)
    - This doesn't matter for getting to a puzzle state, but does matter for animation in software.
- Allow spaces in transforms? `[R->F,U->D]` vs. `[R -> F, U -> D]`
- `*` for wildcard (machines do not need to be able to parse this, but it should be documented for humans)
    - layer mask wildcard: `*Rw`
    - partial move family wildcard: `*O` or `~I*`
    - multiplier wildcard: `RO*`
    - Exact usage is ambiguous! This is probably ok for colloquial use, but should be noted.
- Exact layer range semantics
    - Do layers have to be in order? `1-3R` vs. `3-1R`, `{1..3}R` vs. `{3..1}R`
    - Should we allow open ranges, such as `{2..}`, `{..3}`, `{..-2}`, or `{-1..}`? What are the semantics there?
