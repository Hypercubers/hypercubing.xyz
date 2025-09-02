# Group Theory

<style>
.green { color: #00c853; }
.red { color: #ff5252; }
</style>

## Basic group theory

A **group** is a set of **elements** that can be composed using an **operation** to get a new element.

!!! abstract "Notation"

    - $G$ is often a **group**.
    - Lowercase letters are often **group elements**.
        - $e$ is often the **identity element** (defined below).
    - Depending on the group, composing two elements $a$ and $b$ sometimes uses a symbol (like $a + b$ or $a \times b$) and sometimes uses no symbol (like $ab$).
    - The **inverse** (defined below) of an element $a$ is written $a^{-1}$.

The **order** of a group is the number of elements it has. The order of a group may be infinite.

There are four **group axioms**, which are the requirements in order for something to be a group:

<div class="grid cards" markdown>

-   :material-dots-circle: **Closure**

    ---

    $ab \in G$ <small>(for all $a,b \in G$)</small>

    _Composing two elements in the group must give a new element in the group._

-   :material-home: **Identity**

    ---

    $ea = ae = a$ <small>(for all $a \in G$)</small>

    _There is some **identity element** $e$ in the group that has no effect on other elements._

-   :material-undo-variant: **Inverse**

    ---

    $a a^{-1} = a^{-1} a = e$ <small>(for all $a \in G$)</small>

    _Every element has an inverse element in the group. Composing an element with its inverse on either side results in the identity element._

-   :material-code-parentheses: **Associativity**

    ---

    $(ab)c = a(bc)$ <small>(for all $a,b,c \in G$)</small>

    _Parentheses don't matter when composing elements, so we can just write $abc$._

</div>

There are lots of structures in mathematics that obey these rules, so if we prove things using only the group axioms then we know they'll be true for in a lot of different domains.

!!! example "Examples"

    !!! success "Integer addition"

        Addition on integers is an infinite group. The elements are integers and the operation is addition $a + b$.

        - :material-check:{.green} **Closure:** Adding two integers results in an integer.
        - :material-check:{.green} **Identity:** $0 + a = a + 0 = a$
        - :material-check:{.green} **Inverse:** The inverse of an integer is its negative. $a + (-a) = (-a) + a = 0$
        - :material-check:{.green} **Associativity:** $(a + b) + c = a + (b + c)$

    Before opening the other examples, ask yourself:

    - What are the **elements**?
    - What is the **order**?
    - What is the **operation**?
    - Which ones of the four group axioms does it obey?

    ??? failure "Integer subtraction"

        Subtraction on integers is not a group.

        - :material-check:{.green} **Closure:** Subtracting two integers results in an integer.
        - :material-close:{.red} **Identity:** $a - 0 = a$, but $0 - a \ne a$
        - :material-check:{.green} **Inverse:** The inverse of an integer is itself. $a - a = 0$
        - :material-close:{.red} **Associativity:** $(a - b) - c \ne a - (b - c)$

    ??? failure "Integer multiplication"

        Multiplication on integers is not group.

        - :material-check:{.green} **Closure:** Multiplying two integers results in an integer.
        - :material-check:{.green} **Identity:** $a \times 1 = 1 \times a = a$
        - :material-close:{.red} **Inverse:** There is no integer $b$ such that $0 \times b = b \times 0 = 1$
        - :material-check:{.green} **Associativity:** $(a \times b) \times c = a \times (b \times c)$

    ??? success "Nonzero rational multiplication"

        Multiplication on nonzero rational numbers is an infinite group. The elements are rational numbers $\frac a b$ where $a$ and $b$ are nonzero integers, and the operation is multiplication.

        - :material-check:{.green} **Closure:** Multiplying two rational numbers $\frac a b$ and $\frac c d$ results in a rational number $\frac{a c}{b d}$.
        - :material-check:{.green} **Identity:** $\frac a b \times 1 = 1 \times \frac a b = \frac a b$.
        - :material-check:{.green} **Inverse:** The inverse of a rational number $\frac a b$ is $\frac b a$. $\frac a b \times \frac b a = 1$.
            - We can't include zero because it would have no inverse.
        - :material-check:{.green} **Associativity:** $\left( \frac a b \times \frac c d \right) \times \frac p q = \frac a b \times \left( \frac c d \times \frac p q \right)$

    ??? success "Rotations of a square"

        The rotations of a square are a finite group of order 4. It has 4 elements:

        - identity (do-nothing transformation)
        - 3 rotations (90° clockwise, 90° counterclockwise, and 180°)

        The operation is doing one rotation and then the other. For example, a 90° clockwise rotation composed with a 180° rotation results in a 90° counterclockwise rotation.

        - :material-check:{.green} **Closure:** Doing one transformation after another is equivalent to doing just one transformation.
        - :material-check:{.green} **Identity:** The identity transformation has no effect when composed with another transformation.
        - :material-check:{.green} **Inverse:** Every transformation has an inverse, and composing a transformation with its inverse results in the identity.
            - The identity transformation it its own inverse.
            - The inverse of each 90° rotation is the other 90° rotation.
            - The inverse of the 180° rotation is itself.
        - :material-check:{.green} **Associativity:** $(a b) c = a (b c)$

    ??? success "Rotations and reflections of a square"

        The rotations and reflections of a square are a finite group of order 8. It has 8 elements:

        - identity (do-nothing transformation)
        - 3 rotations (90° clockwise, 90° counterclockwise, and 180°)
        - 4 reflections (horizontal, vertical, and two diagonals)

        The operation is doing one rotation and then the other. For example, a horizontal reflection composed with a 90° counterclockwise rotation results in a diagonal reflection.

        - :material-check:{.green} **Closure:** Doing one transformation after another is equivalent to doing just one transformation.
        - :material-check:{.green} **Identity:** The identity transformation has no effect when composed with another transformation.
        - :material-check:{.green} **Inverse:** Every transformation has an inverse, and composing a transformation with its inverse results in the identity.
            - The identity transformation it its own inverse.
            - The inverse of each 90° rotation is the other 90° rotation.
            - The inverse of the 180° rotation is itself.
            - Each reflection is its own inverse.
        - :material-check:{.green} **Associativity:** $(a b) c = a (b c)$

        !!! question "Exercise"

            Prove the closure property by all composing all 64 pairs of transformations and see what transformation each one results in. (If you don't want to do all 64, just try a handful.)

    ??? success "Rotations of a cube"

        The symmetry-preserving rotations of a cube are a finite group of order 24. It has 24 elements:

        - identity (do-nothing transformation)
        - six 90° rotations around a face
        - three 180° rotations around a face
        - six 180° rotations around an edge
        - eight 120° rotations around a vertex

        The operation is doing one rotation and then the other. For example, a 90° rotation clockwise around the top face composed with a 90° clockwise rotation around the front face results in a 120° clockwise rotation around the top-front-right vertex.

        - :material-check:{.green} **Closure:** Doing one transformation after another is equivalent to doing just one transformation.
        - :material-check:{.green} **Identity:** The identity transformation has no effect when composed with another transformation.
        - :material-check:{.green} **Inverse:** Every transformation has an inverse, and composing a transformation with its inverse results in the identity.
        - :material-check:{.green} **Associativity:** $(a b) c = a (b c)$

### Commutative groups

A group is **commutative** if $a b = b a$ is always true for any elements $a$ and $b$. A commutative group is also called an **abelian group**.

- :material-check:{.green} Integer addition is commutative because $a + b = b + a$.
- :material-check:{.green} Nonzero rational multiplication is commutative because $a \times b = b \times a$.
- :material-close:{.red} The rotation group of a cube is not commutative because these two sequences give different results:
    - A 90° clockwise rotation around the **top** face followed by a 90° clockwise rotation around the **front** face results in a 120° clockwise rotation around the top-front-**right** vertex.
    - A 90° clockwise rotation around the **front** face followed by a 90° clockwise rotation around the **top** face results in a 120° clockwise rotation around the top-front-**left** vertex.

!!! question "Exercises"

    - :material-check:{.green} Prove that the group of rotations of a square is commutative by showing that for all 16 possible combinations of elements $a$ and $b$, $a b = b a$.
    - :material-close:{.red} Prove that the group of rotations and reflections of a square is _not_ commutative by finding two elements $a$ and $b$ such that $a b \ne b a$.

### Generators

A **generatoring set** for a group is a subset of the elements that can **generate** any element in the group using composition and inverses.

!!! example "Example: Integer addition"

    - :material-check:{.green} $\{ 1 \}$ is a generating set for the group.
        - We can invert $1$ to get $-1$.
        - We can compose $1$ with $-1$ to get $1 + (-1) = 0$.
        - We can compose $1$ with itself to get $1 + 1 = 2$.
        - We can compose $2$ with $1$ to get $2 + 1 = 3$.
        - etc.
    - :material-check:{.green} $\{ -1 \}$ is a generating set for the group.
    - :material-check:{.green} $\{ 1, 16, -544 \}$ is a generating set for the group. (We don't have to use $16$ and $-544$.)
    - :material-close:{.red} $\{ 2 \}$ is not a generating set for the group because there is no way to generate $1$.
    - :material-check:{.green} $\{ 4, 17 \}$ is a generating set for the group.
        - We can generate $1$ as $17 + (-4) + (-4) + (-4) + (-4)$.
        - We can generate all the other elements using $1$.

!!! example "Example: Nonzero rational multiplication"

    - :material-close:{.red} A finite set can't generate the whole group.
        - For example, the set $\{ 2, 3 \}$ can't generate any multiple of $5$.
    - :material-close:{.red} A set with only positive numbers can't generate the whole group, because it can't generate negative numbers.
        - Multiplying two positive numbers always results in a positive number.
        - The inverse of a positive number is still positive.
    - :material-check:{.green} The union of $\{ -1 \}$ with the set of the prime numbers is a generating set.
        - For example, we can generate $-\frac{22}{7}$ as $(-1) \times 2 \times 11 \times 7^{-1}$.

!!! question "Exercises"

    For each of the following groups, find one of the smallest possible generating sets and prove that it is a generating set by constructing every element in the group:

    - Rotations of a square (4 elements total; smallest generating set should have 1 element)
    - Rotations & reflections of a square (8 elements total; smallest generating set should have 2 elements)
    - **Challenge:** rotations of a cube (24 elements total; smallest generating set should have 2 elements)

Every group generates itself. In other words, the set of all a group's elements _is_ a generating set for the group.

### Subgroups

A **subgroup** is a group whose elements are a subset of another group. The operation of a subgroup has to be the same as the operation of the original group.

!!! example "Examples"

    - :material-check:{.green} The rotations of a square are a subgroup of the rotations & reflections of a square.
    - :material-close:{.red} The reflections of a square are not a subgroup of the rotations & reflections of a square.
        - There is no identity element.
        - Composing two reflections may result in a rotation, which is not a reflection.
    - :material-close:{.red} The positive integers are not a subgroup of the integers under addition.
        - The positive integers are not a group because there are no inverses.
    - :material-check:{.green} The even integers (positive and negative) are a subgroup of integers under addition.
    - :material-close:{.red} The odd integers are not a subgroup of the integers under addition.
        - There is no identity element.
        - Adding two odd integers results in an even integer.
    - :material-check:{.green} In general, the positive and negative multiples of any integer $n$ are a subgroup of integers under addition.

A set $A$ is a **proper subset** of $B$ if $A \subseteq B$ and $A \ne B$. (The term **strict subset** is also used and means the same thing.) This is often written $A \varsubsetneq B$.[^subset-notation]

!!! warning "The rest of this page is under construction"

### Cosets

### Permutation groups

- function notation to apply a permutation to an element

#### Cycle notation

### Group actions

## Examples using puzzles
