# Group Theory

<style>
.green { color: #00c853; }
.red { color: #ff5252; }
.rot45 { transform: rotate(45deg) }
.spoiler:not(:hover) {
    color: black;
    background: black;
}
</style>

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

    _Parentheses have no effect when composing elements, so we can just write $abc$._

</div>

There are lots of structures in mathematics that obey these rules, so if we prove facts using only the group axioms then we know those facts will be true in a lot of different domains.

!!! example "Examples of groups"

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

    A structure is a group only if it obeys all four of the group axioms.

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

        - :material-crop-square: Identity (do-nothing transformation)
        - three rotations (:material-rotate-right: 90° clockwise, :material-rotate-left: 90° counterclockwise, and
        :material-arrow-all: 180° rotation)

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

        - :material-crop-square: Identity (do-nothing transformation)
        - three rotations (:material-rotate-right: 90° clockwise, :material-rotate-left: 90° counterclockwise, and
        :material-arrow-all: 180° rotation)
        - four reflections (:material-arrow-left-right: horizontal, :material-arrow-up-down: vertical, and :material-arrow-left-right:{.rot45} :material-arrow-up-down:{.rot45} two diagonals)

        The operation is doing one rotation after the other. For example, a horizontal reflection composed with a 90° counterclockwise rotation results in a diagonal reflection.

        - :material-check:{.green} **Closure:** Doing one transformation after another is equivalent to doing just one transformation.
        - :material-check:{.green} **Identity:** The identity transformation has no effect when composed with another transformation.
        - :material-check:{.green} **Inverse:** Every transformation has an inverse, and composing a transformation with its inverse results in the identity.
            - The identity transformation it its own inverse.
            - The inverse of each 90° rotation is the other 90° rotation.
            - The inverse of the 180° rotation is itself.
            - Each reflection is its own inverse.
        - :material-check:{.green} **Associativity:** $(a b) c = a (b c)$

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

    ??? success "Trivial group"

        The **trivial group** containing only the element $e$ is a group.

        - :material-check:{.green} **Closure:** The only composition is $ee = e$.
        - :material-check:{.green} **Identity:** The identity is $e$. $ee = e$.
        - :material-check:{.green} **Inverse:** $e^{-1} = e$, so $ee^{-1} = e^{-1}e = ee = e$.
        - :material-check:{.green} **Associativity:** $(e e) e = e (e e)$ because (and I cannot stress this enough) $ee = e$.

!!! warning "Group elements are not orientations"

    A common misconception is that the orientations of a cube (or other shape) are group elements. Although there is a one-to-one correspondence between transformations and orientations, they are different kinds of objects. There is not an obvious way to compose orientations, so they are not group elements. Transformations, on the other hand, can be composed.

    There is a connection between transformations and orientations, which we'll explore later in the [Group actions](#group-actions) section.

!!! info "Composing transformations is like composing functions"

    If you're familiar with function composition, you'll know that $(f \circ g \circ h)(x) = f(g(h(x)))$. To apply all three functions, you have to do $h$ first and then $g$ and then $f$. Composing transformations works the same way: to apply $ab$, we apply $b$ first and then $a$.

    Consider a square. If $a =$ :material-rotate-right: (90° clockwise rotation) and $b =$ :material-arrow-left-right: (horizontal reflection), then to apply $ab$ we apply :material-arrow-left-right: (horizontal reflection) first and then :material-rotate-right: (90° clockwise rotation). The end result is :material-arrow-left-right:{.rot45} (diagonal reflection that swaps the top-left and bottom-right corners).

    When composing transformations, read the sequence right-to-left, like function application.

!!! question "Exercises"

    Find a piece of paper and a writing utensil. A marker or sharpie that bleeds through paper will work best. Write a capital letter `F` on one side of the paper and write a mirrored letter `F` on the other side of the paper, tracing over the original `F`.

    1. Apply each of the 8 elements of the group of rotations and reflections of a square to your piece of paper and see what happens.

        - :material-crop-square: Identity
        - :material-rotate-right: 90° clockwise rotation
        - :material-rotate-left: 90° counterclockwise rotation
        - :material-arrow-all: 180° rotation
        - :material-arrow-left-right: Horizontal reflection (flip the paper while holding the middle of the top and bottom edges)
        - :material-arrow-up-down: Vertical reflection (flip the paper while holding the middle of the left and right edges)
        - :material-arrow-left-right:{.rot45} TL-DR diagonal reflection (flip the paper while holding the top-right and bottom-left corners)
        - :material-arrow-up-down:{.rot45} TR-DL diagonal reflection (flip the paper while holding the top-left and bottom-right corners)

    2. Apply each of these compositions using your piece of paper and determine the resulting transformation:

        - :material-rotate-left: and :material-rotate-left: (90° rotation counterclockwise $\times$ 90° rotation counterclockwise)  
          Answer <span class="spoiler">:material-arrow-all: 180° rotation</span>
        - :material-arrow-all: and :material-arrow-all: (180° rotation $\times$ 180° rotation)  
          Answer <span class="spoiler">:material-crop-square: identity</span>
        - :material-arrow-left-right: and :material-arrow-up-down:{.rot45} (horizontal reflection $\times$ TR-DL diagonal reflection)  
          _Remember that transformations compose right-to-left._  
          Answer: <span class="spoiler">:material-rotate-right: 90° clockwise rotation</span>
        - :material-arrow-left-right: and :material-crop-square: (horizontal reflection $\times$ identity)  
          Answer: <span class="spoiler">:material-arrow-left-right: horizontal reflection</span>
        - :material-arrow-up-down:{.rot45} and :material-arrow-left-right: (TR-DL diagonal reflection $\times$ horizontal reflection)  
          Answer: <span class="spoiler">:material-rotate-left: 90° counterclockwise rotation</span>
        - :material-arrow-up-down:{.rot45} and :material-rotate-right: (TR-DL diagonal reflection $\times$ 90° clockwise rotation)  
          Answer: <span class="spoiler">:material-arrow-up-down: vertical reflection</span>

## Cyclic groups

$\mathbb{Z}_n$ is the **cyclic group of order $n$**. Its elements are usually written using the integers $0,1,\dots,n-1$. To compose two elements, add the numbers and add or subtract $n$ to get back within the set. This is called **modular arithmetic**, and the "add or subtract $n$" step is a specific way of taking the remainder after division called the **modulo operation**.[^modulo]

[^modulo]: Taking the remainder of $(-7) \div 3$ would usually result in $-1$ because $-7 = 3 \times (-2) + (-1)$, but $-7 \pmod 3$ is $2$ because the result must be one of $\{ 0,1,2 \}$ and $-7 = 3 \times (-3) + 2$.

!!! example "Examples of cyclic groups"

    !!! success "Minutes on a clock"

        Clocks use the cyclic group of order 60 to track minutes. The only valid minutes are the numbers $00,01,\dots,59$.

        - :material-check:{.green} **Closure:** Adding minutes past $59$ wraps back around to $0$.
        - :material-check:{.green} **Identity:** $a + 0 = 0 + a = a$.
        - :material-check:{.green} **Inverse:** The inverse of an element $a$ is $60-a$ because $a + (60 - a) = 60$, which wraps around to $0$.
            - For example: $19 + (60-19) = 19 + 41 = 60$
        - :material-check:{.green} **Associativity:** Addition is associative, and the modulo operation doesn't change this.

    !!! success "Cyclic group of order 5"

    The cyclic group of order 5 contains five elements: $\{ 0,1,2,3,4 \}$.

    - :material-check:{.green} **Closure:** The only composition is $ee = e$.
    - :material-check:{.green} **Identity:** The identity is $e$. $ee = e$.
    - :material-check:{.green} **Inverse:** $e^{-1} = e$, so $ee^{-1} = e^{-1}e = ee = e$.
    - :material-check:{.green} **Associativity:** $(e e) e = e (e e)$ because (and I cannot stress this enough) $ee = e$.

## Isomorphism

Two groups are **isomorphic** if you can make a two-way map elements between them relabel the elements of one group to get the other group such that composition still works the same way. To be more precise: if your mapping is $f$, then applying the mapping before composition has to be equivalent to applying the mapping after composition: $f(a)f(b) = f(ab)$.

If two groups are isomorphic, we often say that they are "the same group." The labeling of the elements in a group is just a useful tool to let us talk about them; it doesn't actually matter for the correctness of the math.

!!! question "Exercise"

    Find a mapping between the group of rotations of a square (identity, 90° clockwise, 90° counterclockwise, and 180°) and the cyclic group of order 4 $\{ 0,1,2,3 \}$.

## Commutative groups

A group is **commutative** if $a b = b a$ is always true for any elements $a$ and $b$. A commutative group is also called an **abelian group**.

- :material-check:{.green} Integer addition is commutative because $a + b = b + a$.
- :material-check:{.green} Nonzero rational multiplication is commutative because $a \times b = b \times a$.
- :material-close:{.red} The rotation group of a cube is not commutative because these two sequences give different results:
    - A 90° clockwise rotation around the **top** face followed by a 90° clockwise rotation around the **front** face results in a 120° clockwise rotation around the top-front-**right** vertex.
    - A 90° clockwise rotation around the **front** face followed by a 90° clockwise rotation around the **top** face results in a 120° clockwise rotation around the top-front-**left** vertex.

!!! question "Exercises"

    - :material-check:{.green} Prove that the group of **rotations** of a square is commutative by showing that for all 16 possible combinations of elements $a$ and $b$, $a b = b a$.
    - :material-close:{.red} Prove that the group of **rotations and reflections** of a square is **not** commutative by finding two elements $a$ and $b$ such that $a b \ne b a$.

## Generators

A **generatoring set** for a group is a [subset](set-theory.md#subsets) of the elements that can **generate** any element in the group using composition and inverses.

!!! example "Examples of generating sets for the integers under addition"

    - :material-check:{.green} $\{ 1 \}$ is a generating set for the integers under addition.
        - We can invert $1$ to get $-1$.
        - We can compose $1$ with $-1$ to get $1 + (-1) = 0$.
        - We can compose $1$ with itself to get $1 + 1 = 2$.
        - We can compose $2$ with $1$ to get $2 + 1 = 3$.
        - etc.
    - :material-check:{.green} $\{ -1 \}$ is a generating set for the integers under addition.
    - :material-check:{.green} $\{ 1, 16, -544 \}$ is a generating set for the integers under addition. (We don't have to use $16$ and $-544$.)
    - :material-close:{.red} $\{ 2 \}$ is not a generating set for the integers under addition because there is no way to generate $1$.
    - :material-check:{.green} $\{ 4, 17 \}$ is a generating set for the integers under addition.
        - We can generate $1$ as $17 + (-4) + (-4) + (-4) + (-4)$.
        - We can generate all the other elements using $1$.

!!! example "Examples of generating sets for the nonzero rationals under multiplication"

    - :material-close:{.red} A finite set can't generate all the nonzero rationals under multiplication.
        - For example, the set $\{ 2, 3 \}$ can't generate any multiple of $5$.
    - :material-close:{.red} A set with only positive numbers can't generate the whole group, because it can't generate negative numbers.
        - Multiplying two positive numbers always results in a positive number.
        - The inverse of a positive number is still positive.
    - :material-check:{.green} The [union](set-theory.md#union) of $\{ -1 \}$ with the set of the prime numbers is a generating set for the nonzero rationals under multiplication.
        - For example, we can generate $-\frac{22}{7}$ as $(-1) \times 2 \times 11 \times 7^{-1}$.

!!! question "Exercises"

    For each of the following groups, find one of the smallest possible generating sets and prove that it is a generating set by constructing every element in the group:

    - Rotations of a square (4 elements total; smallest generating set should have 1 element)
    - Rotations & reflections of a square (8 elements total; smallest generating set should have 2 elements)
    - **Challenge:** rotations of a cube (24 elements total; smallest generating set should have 2 elements)

Every group generates itself. In other words, the set of all a group's elements _is_ a generating set for the group.

## Subgroups

A **subgroup** is a group whose elements are a subset of another group. The operation of a subgroup has to be the same as the operation of the original group.

!!! example "Examples of subgroups"

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
    - The trivial group $\{ e \}$ is a subgroup of every group.
        - Even if the identity element is named something other than $e$ (like $1$ or :material-crop-square:) it is still equivalent in structure.

Just like a [proper subset](set-theory.md#subsets) is a subset that is not equal to the original set, a **proper subgroup** is a subgroup that is not equal to the original group.

!!! warning "The rest of this page is under construction"

## Cosets

Once you have a 

- right cosets (because right action)

## Permutation groups

- function notation to apply a permutation to an element

### Cycle notation

- if an element stays in the same place, don't write it

## Group actions

- Given an initial orientation, there is a one-to-one correspondence between transformations and orientations. Also, transformations tell you how to change one orientation into another. We'll learn more about this in [group actions](#group-actions).

## Examples using puzzles
