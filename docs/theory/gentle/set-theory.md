# Set Theory

<style>
.green { color: #00c853; }
.red { color: #ff5252; }
</style>

A **set** is a collection of objects with no duplicates. Ordering within a set doesn't matter.

!!! example "Examples of sets"

    - $\{ 1, 2, 3, 4, 5 \}$ is a set with five elements.
    - $\{ \square, \triangle \}$ is a set with two elements.

!!! info "Common infinite sets"

    - $\mathbb{Z}$ is often used for the set of integers
    - $\mathbb{Q}$ is often used for the set of rational numbers (fractions)
    - $\mathbb{R}$ is often used for the set of real numbers (everything on the number line)

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

!!! example "Example"

    The union of $\{ 1, 2, 3, 4, 5 \}$ and $\{ 2, 4, 6, 8, 10 \}$ is $\{ 1, 2, 3, 4, 5, 6, 8, 10 \}$.

### Intersection

The **intersection** of two sets is the set with all the elements in both.

!!! example "Example"

    The intersection of $\{ 1, 2, 3, 4, 5 \}$ and $\{ 2, 4, 6, 8, 10 \}$ is $\{ 2, 4 \}$.
