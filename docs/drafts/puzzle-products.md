---
search:
  exclude: true
---

# Puzzle products

Just as many [polytopes](https://polytope.miraheze.org/wiki/Blog:Introduction_to_polytopes) (polygons, polyhedra, polychora, etc.) can be constructed from applying operations on other polytopes, twisty puzzles can also be constructed from other twisty puzzles.

Research in this area is ongoing, but we've already discovered one very powerful tool: the **puzzle product**, analogous to the [prism product](https://polytope.miraheze.org/wiki/Prism_product) on polytopes. We'll start with the formal definitions, then move into examples to illustrate how it works.

## Background

Feel free to skip each section if you are already comfortable with the concept.

??? abstract "Cartesian product"

    The **cartesian product** of two sets $A$ and $B$ (written $A \times B$) is the set of all pairs $(a,b)$ where $a \in A$ and $b \in B$. For example, $\{ x, y, z \} \times \{ 1, 2, 3 \}$ is illustrated below:

    ![Cartesian product of the sets {x,y,z} and {1,2,3}](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Cartesian_Product_qtl1.svg/330px-Cartesian_Product_qtl1.svg.png)

??? abstract "Disjoint union"

    The **disjoint union** of two sets $A$ and $B$ (written $A \sqcup B$) is the set of all the elements in $A$ _and_ all the elements in $B$, with elements distinguished so every element in $A \sqcup B$ is a member of only $A$ or only $B$. For example, notice how in the example below there are multiple copies of identical shapes, each labeled based on the set it come from:

    ![Disjoint union of two sets of polygons](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/PolygonsSetDisjointUnion.svg/330px-PolygonsSetDisjointUnion.svg.png)

??? abstract "Symmetry group"

    The **symmetry group** of an object is all the ways it can be transformed while remaining indistinguishable. The **orientation** of an object is whether it has been reflected.[^orientability] For our purposes, **rotations** are transformations that preserve the orientation, while **reflections** do not. For example, the symmetry-group regular pentagon has 5 **rotations** (including the trivial "rotation" that does nothing) and 5 **reflections**.

    [^orientability]: A "non-orientable" shape is one where orientation cannot be determined. Typically this is because a reflection can be undone using only rotations.

    Another example: the symmetry group of the cube has 48 elements: 24 rotations (including the trivial "rotation" where it doesn't move) and 24 reflections.

### Puzzle construction

We will the **Laminated Theory** construction for puzzles. See the [Slightly Wrong Explanation of Grip Theory](/theory/grip-theory/slightly-wrong.md) if you haven't yet. In particular, recall that:

- A **puzzle** is defined by a **grip group** $G$, a set of **layers** $L$ partitioned into **axes** $A$, and a set of **pieces** $P$.
- The grip group acts on the set of **layers**.
- The set of **axes** forms a [block system](https://en.wikipedia.org/wiki/Block_(permutation_group_theory)) for the action of the grip group on layers.
- A **piece** is defined by its grip signature, which is a subset of layers.

## Definition

The **puzzle product** $\alpha \times \beta$ of two factor puzzles $\alpha$ and $\beta$ is defined as follows:

- $G_{\alpha \times \beta} = G_\alpha \times G_\beta$
- $A_{\alpha \times \beta} = A_\alpha \sqcup A_\beta$
- $L_{\alpha \times \beta} = L_\alpha \sqcup L_\beta$
- $P_{\alpha \times \beta} = P_\alpha \times P_\beta$

It's really that simple!

Of course, the pedantic among you will want to know _how_ $G_{\alpha \times \beta}$ acts on $L_{\alpha \times \beta}$ and exactly what the grip signature is for each piece in $P_{\alpha \times \beta}$:

- Given $g_\alpha \in G_\alpha$, $g_\beta \in G_\beta$, $l_\alpha \in L_\alpha$, and $l_\beta \in L_\beta$, then $(g_\alpha, g_\beta)(l_\alpha, l_\beta) = (g_\alpha l_\alpha, g_\beta l_\beta)$.
- $P_{\alpha \times \beta} = \{ p_\alpha \sqcup p\beta \mid p_\alpha \in P_\alpha \ \mbox{ and } \ p_\beta \in P_\beta \}$.

### Stickering

We typically sticker puzzles using **stickers**, which are partitioned into **colors**.

Colors are simple. If $C$ is the set of colors on a puzzle, then $C_{\alpha \times \beta} = C_\alpha \sqcup C_\beta$.

Stickers are more complicated. If $S_p$ is the set of stickers for a piece $p$, then $S_\{p_\alpha \times p_\beta\} = S_{p_\alpha} \sqcup S_{p_\beta}$. In other words: the set of stickers for a piece in the product puzzle is the disjoint union of the stickers for each corresponding piece in the factor puzzles.

## Example: canon-cut FT pentagonal prism

This will all be much clearer with an example. First, let's define our **factor puzzles**:

!!! example "3-layer line"

    ![](https://assets.hypercubing.xyz/img/virt/product/line_3.png){ align=right width=192 }

    - $G$ = symmetries of a line (2 elements) = [Coxeter group] $A_1$
    - $A$ = 1 axis
    - $L$ = 3 layers
    - $P$ = 3 pieces
        - 1 core with 0 stickers
        - 2 endpoints with 1 sticker each

!!! example "Shallow edge-turning pentagon"

    ![](https://assets.hypercubing.xyz/img/virt/product/ngon_ft_shallow_5_3.png){ align=right width=192 }

    - $G$ = symmetries of a pentagon (10 elements) = [Coxeter group] $I_5$
    - $A$ = 5 pentagon edges
    - $L$ = 10 layers (2 per axis)
    - $P$ = 11 pieces
        - 1 core with 0 stickers
        - 5 centers with 1 sticker each
        - 5 corners with 2 stickers each

[Coxeter group]: https://en.wikipedia.org/wiki/Coxeter_group

Now we can construct their product:

!!! example "Canon-cut FT pentagonal prism"

    ![](https://assets.hypercubing.xyz/img/virt/product/pentagonal_prism_ft_3_3.png){ align=right width=192 }

    - $G$ = symmetries of a pentagonal prism (20 elements) = Coxeter group $I_5 \times A_1$
    - $A$ = 6 axes (5 from the pentagon, 1 from the line)
    - $L$ = 13 layers (10 from the pentagon, 3 from the line)
    - $P$ = 33 pieces

    | Piece type             | Where it comes from                          | Stickers per piece                |
    | ---------------------- | -------------------------------------------- | --------------------------------- |
    | 1 core                 | 1 pentagon core $\times$ 1 line core         | 0                                 |
    | 5 side centers         | 5 pentagon centers $\times$ 1 line core      | 1 (1 from pentagon)               |
    | 5 side-side edges      | 5 pentagon corners $\times$ 1 line core      | 2 (2 from pentagon)               |
    | 2 pentagon centers     | 1 pentagon core $\times$ 2 line endpoints    | 1 (1 from line)                   |
    | 10 pentagon-side edges | 5 pentagon centers $\times$ 2 line endpoints | 2 (1 from pentagon + 1 from line) |
    | 10 corners             | 5 pentagon corners $\times$ 2 line endpoints | 3 (2 from pentagon + 1 from line) |

Note that even though the core makes no difference for solving, we must include it in the factor puzzles in order to get the centers and middle layer pieces of the product.

## The reflection problem

I lied to you. We have not actually constructed the standard canon-cut FT pentagonal prism. We have constructed the _refle_ canon-cut FT pentagonal prism, which is exactly the same except that it allows reflection moves, like the ["mirror & twist" reflecube](https://www.nan.ma/reflecube/).

If we remove the reflections from either of the factor puzzles then we lose the 180° twists on the rectangular side faces, because the 180° rotation is generated by composing the line reflection with a pentagon reflection. If we want to generate the _rotational_ canon-cut FT pentagonal prism, which only allows rotations as twists, then we need to get more creative.

We could say that the FT pentagonal prism is the _rotational subpuzzle_ of product of an ET pentagon with a 3-layer line, but there's a few different ways to define "rotational subpuzzle."

### Option 1: Pick a different grip group

We could define the **rotational subpuzzle** of a puzzle as the puzzle with only the orientation-preserving elements of the grip group, and everything else the same. This works for our pentagonal prism example; however, it does not work for puzzles such as the [Hemimegaminx](/puzzles/hemimegaminx.md) and [Klein Bottle Rubik](https://www.youtube.com/watch?v=DvZnh7-nslo), which are constructed in non-orientable spaces. The grip group for each of those puzzles has no subgroup we can choose that will contain only rotational twists.

## Option 2: Add a twist subset

We could add a **twist subset** for the whole puzzle. This is a subset of possible twists that are actually allowed to be performed.

Then the **rotational subpuzzle** of a puzzle is simply one where the set of twists has had all the reflections removed. This works!

## Option 3: Add axis subgroups

Alternatively, we could add an **axis subgroup** to each axis, which is a subgroup of the stabilizer of the axis in the grip group from which twists on that axis must be constructed. I.e., it's some subgroup that keeps the axis fixed.

Then the **rotational subpuzzle** is the puzzle where all the axis subgroups have had reflections removed. This works!

Axis subgroups are also nice because they capture more structure than twist subsets: for example, they enforce that composing two twists on an axis always results in another twist.
