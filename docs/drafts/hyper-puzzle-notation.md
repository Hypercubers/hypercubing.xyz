---
search:
  exclude: true
---

# Hyper Puzzle Notation

[metrics]: https://hypercubing.xyz/notation/#turn-metrics

!!! warning "This is a draft"

    This document is NOT final and might be outdated! Before making anything based on this (including software, documentation, or learning resources), please ping Hactar and/or Luna.

## Syntax

Syntax is the same across all puzzles, so that a move sequence may be unambiguously parsed without first selecting a puzzle. Some semantics are shared.

### Node

A **node** is a unit of notation.

Some nodes are **repeatable**, which means that they can be repeated and/or  inverted using a [multiplier](#multiplier) immediately after them.

#### Move

A **move** is a [node](#node) representing a twist or rotation of the puzzle. It has four components:

- [Layer mask](#layer-mask) (optional)
- [Family](#family) (required)
- [Bracketed transform](#bracketed-transform) (optional)

Moves are repeatable.

##### Layer mask

A layer mask is an optional tilde `~` optionally followed by one of the following:

- Positive integer.
    - Example: `3R` means "`R` on the 3rd layer"
- Range of positive integers separated by `-`.
    - Example: `2-4R` means "`R` on layers 2, 3, and 4"
- Curly braces with positive and negative integers and ranges separated by `..`.
    - Example: `{2..4}R` means "`R` on layers 2, 3, and 4" (equivalent to `2-4R`)
    - Example: `{1,3..5,7}R` means "`R` on layers 1, 3, 4, 5, and 7"
    - Example: `{1..-1}R` means "`R` on all layers"
    - Example: `{2..-2}D` is one generalization of `E` to NxNxN puzzles with many layers
    - Example: `{3,-2}R` means "`R` on layer 3 and the 2nd layer from the other side"

Reversed ranges are the same: `{1..-1}` is the same as `{-1..1}` and `1-3` is the same as `3-1`.

##### Family

A **move family** is a string of uppercase or lowercase Latin or Greek letters and underscores.

Move families on 3^3^ include `R`, `F`, `Rw`, `x`, etc. Move families on 3^4^ include `R`, `RO`, `LDBI`, `wz`, etc. Move families on 3^5^ include `U`, `A`, `Azx`, etc.

A move family often represents a complete move (as is the case on 3^3^), but not always. On 3^4^ and 3^5^, move families such as `R` require a [bracketed transform](#bracketed-transform) afterward to specify a complete move.

##### Bracketed transform

A bracketed transform is a set of square brackets `[]` with contents inside consisting of letters, numbers, symbols from the set `'-<>|`, and spaces (no other whitespace). Other symbols may be added to this list in the future.

Different puzzles can use bracketed transforms in different ways. There are two common ways most puzzles use them: [sequential transforms](#sequential-transforms) and [transform constraints](#transform-constraints).

###### Sequential transforms

On some puzzles, a single move is most efficiently written as a composition of two moves on the same axis. For example, `Rj` represents the small jumbling angle ~70.5287794°, so `R[1 j']` is equivalent to `&(R Rj')`.

??? question "Why are sequential transforms necessary?"

    Consider a complex layer mask, like `{1,3,5,7}` (common for checkerboards). Without sequential transforms, we must duplicate the layer mask: `{1,3,5,7}R {1,3,5,7}Rj'`. With sequential transforms, we can write `{1,3,5,7}R[1 j']`.

###### Transform constraints

On some puzzles, moves can only be written using a list of constraints separated by `|`, where each constraint is two axes separated by `->`. For example, `I[F->U | R->P]` represents a [double rotation](https://en.wikipedia.org/wiki/Rotations_in_4-dimensional_Euclidean_space#Double_rotations) twist on 3^5^. When a transform is underconstrained, the "simplest" transform that matches the constraints is typically correct. (This should only be used for moves where there is an obvious answer.)

This also allows writing moves in an abstract or puzzle-general way.

- Example: `R[F->U]` represents an `R` move on 3^3^ and FTO, and an analogous move on all higher-dimensional 3^n^

??? question "Why `|`?"

    - It's not used for anything else in notation.
    - It's unlikely to be useful for anything else.
    - If it is ever useful for anything else, this is only a very narrow context in which it is already used.
    - It's already used to introduce constraints in set-builder notation: $\{ x | x < 5 \}$.
    - Comma `,` and colon `:` are already used for [commutators](#commutator) and [conjugates](#conjugate).

??? warning "Open questions"

    - How to write a fixed axis? Possibilities:
      - `I[R->U | F]`
      - `I[R->U | F->F]`
      - some symbol before `F`

#### Rotation

A [rotation](#rotation) is a [node](#node) representing a rotation of the whole puzzle. It is similar to a move, but it has no [layer mask](#layer-mask) and the [family](#family) is optional. A rotation has three components:

- `@`
- [Family](#family) (optional)
- [Bracketed transform](#bracketed-transform) (optional)

Examples:

- `@R` is a rotation that moves like an `R` move.
- `@[F->U]` is a rotation that takes `F` to `U`.

Rotations are repeatable.

??? question "Why `@`?"

    - It's a mnemonic for "all."
    - It looks round, like a rotation.
    - It's not already in use, and is unlikely to be used for anything else.

#### Pause

A **pause** is a [node](#node) representing a pause. It is written using `.`.

Pauses are sometimes used for reconstruction of speedsolves.

Pauses are _not_ repeatable.

#### Group

A **group** is a sequence of nodes surrounded by parentheses `()`, with an optional symbol before the opening parenthesis. There are four kinds of groups:

- **Simple groups**, which represent a logical grouping
    - Simple groups have no prefix symbol. Example: `(R U R' U')`
    - A simple group's move count should be equivalent to the moves on their own.
    - A simple group should affect animation speed slightly or not at all.
- **Macro groups**, which represent moves done using a macro in software.
    - Macro groups have `!` as a prefix symbol. Example: `!(R U R' U')`
    - A macro group's move count should be equivalent to the moves on their own.
    - A macro group should animate very quickly or not at all.
- **Simultaneous groups**, which represent moves done simultaneously.
    - Simultaneous groups have `&` as a prefix symbol. Example: `&(U D2)`
    - A simultaneous group should count as 1 [ETM][metrics].
    - A simultaneous group should animate simultaneously if possible. It may animate sequentially, but should take the same amount of time as a single move.
- **NISS groups**, which represent moves done on the inverse puzzle state.
    - NISS groups have `^` as a prefix symbol. Example: `^(U F' D2)`
    - A NISS group's move count should be equivalent to the moves on their own.
    - A NISS group's moves may be animated inverted before the scramble (most useful while constructing a solution) or inverted after the forwards solution (most useful while viewing a completed solution). These two might not be equivalent if the combined scramble + forwards solution + NISS solution is not the identity.

Simultaneous groups must not contain any groups. All other groups may contain any group inside them.

Because groups are a kind of [node](#node), they can also have a [multiplier](#multiplier) after them.

??? question "Why don't macros count as 1 ETM?"

    Historically, hypercubing fewest-moves has effectively used ETM in whatever program, subject to the types of moves that program allowed. E.g., "MC4DTM" is a shorthand for "ETM, using only moves accessible in MC4D." This is a common concept that we want to have a name for.

    In software where a single move may take multiple mouse clicks or keypresses, ETM is already detached from the number of interactions, which is really the important metric for speedsolving.

Groups are repeatable.

#### Commutator

A **commutator** is two sequences of moves in square brackets separated by a comma. Example: `[A, B]`. It is equivalent to `A B A' B'`.

Commutators are repeatable.

#### Conjugate

A **conjugate** is two sequences of moves in square brackets separated by a comma. Example: `[A: B]`. It is equivalent to `A B A'`.

Commutators are repeatable.

#### Square-1

Square-1 moves are of the form `(n, d)` (where `n` and `d` are signed integers) and `/`. These cannot be used with layer masks, transforms, or multipliers.

#### Megaminx scrambling

Megaminx scrambling uses the moves `R++`, `R--`, `D++`, and `D--`. These cannot be used with layer masks, transforms, or multipliers.

### Multiplier

A **multiplier** is an optional positive integer and an optional apostrophe `'`, pronounced "prime," which negates the multiplier. `2`, `'`, `2'`, and `42'` are all multipliers.

### Comment

A **line comment** starts with `//` and extends to the next newline. Line comments have no effect on the puzzle.

## Conventions

This section defines common conventions for axes and move families. These should be considered when developing notation for new puzzles. These are not strict rules.

- Uppercase Latin alphabet: `ABCDEFGHIJKLMNOPQRSTUVWXYZ`
- Uppercase Greek alphabet: `ΓΔΘΛΞΠΣΦΨΩ` (Greek letters that are visually similar to Latin letters have been excluded)
- Lowercase Latin alphabet: `abcdefghijklmnopqrstuvwyxz`
- Lowercase Greek alphabet
    - Large lowercase: `βδζθλξ`
    - Small lowercase: `εηκμπτφψω` (Greek letters that are visually similar to Latin letters have been excluded)

Other Greek letters are recommended to NOT be used because they are too similar in appearance to Latin letters.

### Uppercase Latin alphabet (semantic)

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

The unused letters here are reserved for execution notation, for variable names, for ad-hoc notation, or for specific puzzles (e.g., `X` and `Y` in 120-cell notation[^120cell]).

[^120cell]: The facets of the 120-cell can be divided into eight 15-cell clusters, each containing 12 facets corresponding to faces of a dodecahedron plus three extra ones. Those three extra ones are called `I` ("In"), `X` and `Y`. Each cluster corresponds to one facet of a hypercube.

### Lowercase Latin alphabet (semantic)

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

### Sequential alphabet

The letters `A`-`Z` are often used to name elements in an ordered sequence, such as the rectangular faces of a polygonal prism. If there are more than 26 names needed, letters from the uppercase Greek alphabet may be added as a prefix, using a base-10 [bijective numeration](https://en.wikipedia.org/wiki/Bijective_numeration) with the digits `ΓΔΘΛΞΠΣΦΨΩ`:

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

When multiple sets of uppercase letters are needed, they may be distinguished using a lowercase Latin letter as a prefix. If more than 26 prefixes are needed, they may be preceeded by a bijective numeration similar to the uppercaes letters.

The {100}x{4} duoprism serves as an example of a puzzle that requires more than 26 sequential names.[^hundredagonal-duoprism] It has 104 cells, which in this proposal would be named `aA`, `aB`, ..., `aΘU`, `aΘV`, `bA`, `bB`, `bC`, `bD`

[^hundredagonal-duoprism]: This puzzle was created as a joke but has actually been solved.

### Lowercase Greek alphabet (sequential)

For when there are multiple sets of axes assigned Latin letters, they can be distinguished using a small lowercase Greek prefix. For example:

| Group | Names                 |
| ----- | --------------------- |
| 1     | `εA`, `εB`, `εC`, ... |
| 2     | `ηA`, `ηB`, `ηC`, ... |
| 3     | `κA`, `κB`, `κC`, ... |

### Lowercase Greek alphabet (semantic)

The large lowercase Greek letters are reserved for semantic uses. Currently, only `β` has a use. Others are reserved for future use.

| Letter | Use      |
| ------ | -------- |
| `β`    | Opposite |
| `δ`    |          |
| `ζ`    |          |
| `θ`    |          |
| `λ`    |          |
| `ξ`    |          |

For example, `βA` is the axis opposite from `A`, on a puzzle where there is otherwise no convenient semantic name for the axis opposite from `A`. In this usage, `β` comes after small lowercase Greek letters but before uppercase Greek letters.

### Cube axes

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

Keybinds for high-dimensional puzzles typically assign short (1-2 letter) uppercase names to axes and short (1-2 letter) lowercase names to **twist directions**. An axis and a twist direction can be combined to specify a move.

Examples:

- 3^4^ uses the letters `x`, `y`, and `z` after an axis name to specify a twist.
- n^5^ and higher dimensions use two of the letters `x`, `y`, `z`, `w`, `v`, etc. after an axis name to specify a twist
- Polygonal duoprisms reuse the hypercube letters `I`, `U`, `D`, `F`, `R`, `L` (all except `O` and `B`) to refer to a useful subset of axes.

### Jumbling notation

- `h` indicates half of a doctrinaire turn (common on Bagua and mixup cubes)
- `j` indicates some other jumbling angle
- `k` indicates a second jumbling angle, for when `j` is already taken

## Rationale

### Why use Greek letters?

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

### Why curly-brace layer sets?

It is a very common convention in hypercubing software to hold down any set of number keys to apply a "layer mask" to a move. Given that individual moves may require many characters to write (such as `I[F->B,U->R]`) it is very awkward to require duplicating this many times.

- E.g., Suppose we want to write the 7^4^ move `{1,3,5,7}IUR` using only ridge turns. (This is a contrived example because we _do_ have a way to write edge turns on n^4^, but on some puzzles these moves can only be easily written using simultaneous move notation.) With layer sets, we can write `&({1,3,5,7}IF {1,3,5,7}IR2)`; without layer sets, we must write `&(IF 3IF 5IF 7IF IR2 3IR2 5IR2 7IR2)`.
    - We _could_ write it the long way, but we lose important semantics and it becomes much less readable.
    - Transform notation makes this problem even worse: `{1,3,5,7}I[U->R,F->B]` vs. `&(I[U->R,F->B] 3I[U->R,F->B] 5I[U->R,F->B] 7I[U->R,F->B])`
    - Any layer mask can be used for a single move in hypercubing software, and we treat it as a single move! It should be possible to express concisely in notation
- Checkerboard patterns on big cubes are a major example where this problem appears.
- Negative numbers count from the other side (generalized big cube algorithms!)
    - Generic middle slice on big cubes: `~{1,-1}R` or `{2..-2}R`

### Why invert layer masks?

- Complex 3^3^ has an anti-`R` move (equivalent to `&(R x')`) that is _distinct_ from `Lw` (which does not exist) because `R` and `L` are no longer opposites.
    - Technically you could do `2R` by assuming the 6-axis 2-layer laminated construction but that's very unintuitive and does not generalize to ordinary 3^3^.
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

- `~` on its own is more useful to mean "all except the first layer"
    - e.g., `~IUR` for the very common "UR flip" in RKT cancels on 3^4^ (otherwise expressed as `{2..-1}IUR` or `{1..-2}OUR`)
- `*` is already used colloquially as a wildcard.
    - e.g., "You can do RKT using either `<RO*, I*>` or `<*O, ~I*>`."
- `@` has the mnemonic "all"

### Why have execution notation in addition to general notation?

- Execution notation is usually optimized for particular puzzles and particular viewpoints.
    - Execution notation often lacks access to certain moves.
- Execution notation might be more compact or require fewer symbols, making it easier to translate to/from keybinds.
- Execution notation may provide a way to translate moves between puzzles; e.g., `Uy` has meaning on both 3^4^ and polygonal duoprisms even though these puzzles are very different.
- Execution notation can be defined ad-hoc.

## Rust data structure

Below is a draft of a Rust data structure representing the notation.

```rs
pub enum Node {
    Repeated {
        inner: RepeatableNode,
        amount: Option<i32>,
    },

    /// `(n, m)`
    SquanMove(i32, i32),
    /// `/`
    SquanSlash,
    /// `R++`, `R--`, `D++`, `D--`
    MegaminxScrambleMove(MegaminxScrambleMove),
    /// `#`
    Phys24ScrambleRestack,
}

pub enum RepeatableNode {
    Move(Move),
    /// `@`
    Rotation(Rotation),
    /// `.`
    Pause,
    /// Parenthetical group with optional prefix symbol.
    ///
    /// These moves can always be executed in sequence.
    Group {
        layer_mask: Option<LayerMask>,
        kind: GroupKind,
        elements: Vec<Node>,
    },
    /// ^(...)
    ///
    /// This is separate because it requires special handling.
    Niss(Vec<Node>),
    /// `[A, B]`
    Commutator([Vec<Node>; 2]),
    /// `[A: B]`
    Conjugate([Vec<Node>; 2]),

}

pub enum MegaminxScrambleMove {
    Rpp,
    Rmm,
    Dpp,
    Dmm,
}

pub enum GroupKind {
    Basic, // no char
    Simultaneous, // &
    Macro, // !
}

pub struct Move {
    pub layer_mask: LayerMask,
    pub family: String,
    pub transform: Option<BracketedTransformSeq>,
}

pub struct Rotation {
    pub family: Option<String>,
    pub transform: Option<BracketedTransformSeq>,
}

pub struct BracketedTransformSeq {
    /// Sequence of transforms. Each transform can be parsed into a `FamilySuffix` or `ConstraintSet` using [`bracketed_transform_util`] (generally only one will be used depending on the puzzle).
    pub transform_sequence: Vec<String>,
}

mod bracketed_transform_util {
    pub struct FamilySuffix {
        pub family_suffix: String,
        pub multiplier: Option<i32>,
    }

    pub struct ConstraintSet {
        pub constraints: Vec<Constraint>,
    }
    pub enum Constraint {
        Fixed {
            pub element: String,
        },
        Moving {
            pub element_start: String,
            pub element_end: String,
        },
    }
}

impl BracketedTransform {
    pub fn as_family_suffix() -> Option<(String, i32)>;
    pub fn as_constraints() -> Option<ConstraintSet>;
}

pub struct LayerMask {
    pub invert: bool,
    pub ranges: Vec<LayerRange>,
}

/// Layer range
///
/// If start & end are the same, it's a single layer
pub struct LayerRange {
    pub start: i32,
    pub end: i32,
}
```
