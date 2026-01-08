---
search:
  exclude: true
---

# Set Theory

<style>
.green { color: #00c853; }
.red { color: #ff5252; }
.spoiler:not(:hover) {
    color: black !important;
    background: black;
}
</style>

A **set** is a collection of objects with no duplicates. Ordering within a set doesn't matter.

!!! example "Examples of sets"

    - $\{ 1, 2, 3, 4, 5 \}$ is a set with five elements.
    - $\{ \square, \triangle \}$ is a set with two elements.

!!! info "Common infinite sets"

    - $\mathbb{Z}$ is the set of integers
    - $\mathbb{Q}$ is the set of rational numbers (fractions)
    - $\mathbb{R}$ is the set of real numbers (everything on the number line)
    - $\mathbb{Z}^+$ is the set of positive integers
    - $\mathbb{Q}^+$ is the set of positive rational numbers
    - $\mathbb{R}^+$ is the set of positive real numbers

The empty set $\{\}$ has zero elements. It is often written with the symbol $\varnothing$.

### Elements

The symbol $\in$ (pronounced "in" or "element of") can be used to write statements about whether an element is in a set. For example:

- $3 \in \{ 1, 2, 3, 4 \}$
- $16 \notin \{ 1, 2, 3, 4 \}$
- $\pi \in \mathbb{R}$
- $\pi \notin \mathbb{Q}$

### Subsets

A set $A$ is **subset** of another set $B$ if all the elements in $A$ are also elements in $B$. This is often written $A \subseteq B$.

!!! example "Examples of subsets"

    - $\varnothing$, $\{ 4 \}$, $\{ 1, 3 \}$, and $\{ 1, 2, 3, 4, 5 \}$ are all subsets of $\{ 1, 2, 3, 4, 5 \}$.
    - $\{ 1, 2, 3, 4, 5 \} \subseteq \mathbb{Z}$
    - $\mathbb{Z} \subseteq \mathbb{Q} \subseteq \mathbb{R}$

!!! info "Facts about subsets"

    - Every set is a subset of itself: $A \subseteq A$
    - $\varnothing$ is a subset of every set: $\varnothing \subseteq A$
    - If $A \subseteq B$ and $B \subseteq C$, then $A \subseteq C$.
    - If $A \subseteq B$ and $B \subseteq A$, then $A = B$.

A set $A$ is a **proper subset** of $B$ if $A \subseteq B$ and $A \ne B$. (The term **strict subset** is also used and means the same thing.) This is often written $A \varsubsetneq B$.[^subset-notation]

[^subset-notation]: We avoid the symbol $\subset$ because some authors use it to for subsets and some authors use it for proper subsets.

### Union

The **union** of two sets is the set with all the elements in either one.

!!! example "Examples of unions"

    The union of $\{ 1, 2, 3, 4, 5 \}$ and $\{ 2, 4, 6, 8, 10 \}$ is $\{ 1, 2, 3, 4, 5, 6, 8, 10 \}$.

### Intersection

The **intersection** of two sets is the set with all the elements in both.

!!! example "Examples of intersections"

    The intersection of $\{ 1, 2, 3, 4, 5 \}$ and $\{ 2, 4, 6, 8, 10 \}$ is $\{ 2, 4 \}$.

## Permutation

A **permutation** of a rearrangement of the elements in a set.

!!! warning "To-do: examples of permutations"

## Maps

A **map** or **function** is a way of turning elements from an input set (the **domain**) into elements of an output set (the **codomain**). If you're familiar with the "vertical line test" on a graph, that's equivalent to saying that each element from the input maps to at exactly one element of the output.

## Bijections

A **bijection** is a two-way map between sets where each element in one set matches with exactly one element from the other set. If the sets are finite, they must have the same number of elements, or else the map couldn't go both ways. A bijection always has an **inverse** bijection that goes the other wya.

It's common to use the notation $x \mapsto y$ to mean $x$ (from the input set) maps to $y$ (from the output set).

If the sets are finite, we can write a bijection by listing what each element maps to. If the sets are infinite, we have to be use variables to handle infinitely many values at once.

!!! example "Examples of bijections on finite sets"

    !!! success "Bijection"

        Here is a bijection between $\{ 0,1,2,3 \}$ and $\{ A,B,C,D \}$:

        - $0 \mapsto C$
        - $1 \mapsto D$
        - $2 \mapsto A$
        - $3 \mapsto B$

        Here is its inverse:

        - $A \mapsto 2$
        - $B \mapsto 3$
        - $C \mapsto 0$
        - $D \mapsto 1$

    !!! failure "Not a bijection"

        This is not a bijection between $\{ 0,1,2,3 \}$ and $\{ A,B,C,D \}$, because $2$ and $3$ both map to $B$ and nothing maps to $D$:

        - $0 \mapsto C$
        - $1 \mapsto A$
        - $2 \mapsto B$
        - $3 \mapsto B$

        Notice that we can't make the inverse bijection either:

        - $A \mapsto 1$
        - $B \mapsto {?}$
        - $C \mapsto 0$
        - $D \mapsto {?}$

!!! example "Examples of bijections on infinite sets"

    - :material-check:{.green} $x \mapsto x+1$ is a bijection on the integers $\mathbb{Z}$. Its inverse is the bijection $x \mapsto x-1$.
    - :material-close:{.red} $x \mapsto 2x$ is not a bijection on the integers $\mathbb{Z}$. Nothing maps to odd numbers.
    - :material-check:{.green} $x \mapsto 2x$ is a bijection on the real numbers $\mathbb{R}$. Its inverse is the bijection $x \mapsto \frac{x}{2}$.

!!! example "Exercises"

    For each of the following maps, determine whether it is a bijection. If it is a bijection, find its inverse.

    You are welcome to use a [graphing calculator](https://www.desmos.com/calculator) to help.

    - $x \mapsto x^2 \quad (\mathbb{R} \to \mathbb{R})$  
      Answer: <span class="spoiler">:material-close: This is not a bijection on the real numbers $\mathbb{R}$. Nothing maps to negative numbers.</span>
    - $x \mapsto x^2 \quad (\mathbb{R}^+ \to \mathbb{R}^+)$  
      Answer: <span class="spoiler">:material-check: This is a bijection on the positive real numbers $\mathbb{R}^+$. Its inverse is the bijection $x \mapsto \sqrt x$.</span>
    - $x \mapsto -\sqrt[3]x \quad (\mathbb{R} \to \mathbb{R})$  
      Answer: <span class="spoiler">:material-check: This is a bijection on the real numbers $\mathbb{R}$. Its inverse is the bijection $x \mapsto x^3$.</span>
    - $x \mapsto 42 \quad (\mathbb{R} \to \mathbb{R})$  
      Answer: <span class="spoiler">:material-close: This is not a bijection on the real numbers $\mathbb{R}$. Nothing maps to anything other than 42.</span>
    - $x \mapsto \begin{cases}2x+1 & x \ge 0 \\ -2x & x < 0\end{cases} \quad (\mathbb{Z} \to \mathbb{Z}^+)$  
      Answer: <span class="spoiler">:material-check: This is a bijection from the integers $\mathbb{Z}$ to the positive integers $\mathbb{Z}^+$. Its inverse is $x \mapsto \begin{cases}\frac{x-1}{2} & x \text{ is odd} \\ -\frac{x}{2} & x \text{ is even}\end{cases} \quad (\mathbb{Z}^+ \to \mathbb{Z})$</span>
