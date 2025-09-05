# Grip Theory

<style>
.spoiler:not(:hover) {
    color: black;
    background: black;
}
</style>

!!! warning "This whole page is under construction"

Now that you understand the fundamentals of [group theory](group-theory.md), we can introduce grip theory. At its core, grip theory is very simple, but there are a lot of extensions that allow us to model more complicated puzzles.

## Grips

- A **grip** is a thing you can turn. Every puzzle has a **grip set**, denoted using $\Gamma$ (capital gamma).
- The **grip group** is a permutation group that acts on the grip set, denoted using $G$.

!!! info

    Note: The elements of the grip group are _transformations_, not grips. Each element of the grip group is a permutation of the grip set.

On a 3×3×3:

- The grip set is $\{ R, L, U, D, F, B \}$.
- The grip group is the group of rotations of a cube.
- The grip group acts on the set of grips the same way it acts on the faces of a cube.

This is already enough to construct cube rotations. For example, a `y` rotation applies the 4-cycle $(RFLB)$ to the grip set.

!!! example "Exercise"

    Consider an `x2` rotation on a 3×3×3.

    - What is the permutation applied to the grip set? Answer: <span class="spoiler">$(UD)(FB)$</span>
    - What grips are fixed by the permutation? Answer: <span class="spoiler">$\{ R, L \}$</span>

## Twists

A **twist** is defined using a grip $g \in \Gamma$ and an element of the grip group $\sigma \in G$ that keeps that grip fixed (i.e., $\sigma[g] = g$).

!!! warning "Confusing notation"

    - $\Gamma$ is the grip set. $g$ is a grip.
    - $G$ is the group group. $\sigma$ is a group element.

    I'm terribly sorry.

    In the wider world of mathematics, $G$ is often used for groups and $\sigma$ is often used for [permutations](https://en.wikipedia.org/wiki/Permutation), so we really don't have many letters left to choose for "grip" and "grip set."

For example, on a 3×3×3 the `R'` twist is defined as $R[(UFDB)]$.

On most puzzles we care about, all valid twists exist. In other words, any grip can be have any transformation applied to it as long as that grip stays fixed.

!!! example "Exercises"

    - What is the `D2` twist? Answer: <span class="spoiler">$D[(RL)(FB)]$</span>
    - Is $L[(URF)]$ a valid twist on 3×3×3? Answer: <span class="spoiler">No, because $(URF)$ is not an element of the grip group.</span>
    - Is $L[(URF)(LDB)]$ a valid twist on 3×3×3? Answer: <span class="spoiler">No, because $(URF)(LDB)$ doesn't keep $L$ fixed.</span>

## Pieces

- A **piece** is a a thing that moves around. On a 3^3^, there are 27 pieces. Every puzzle has a set of pieces.
- A **grip signature** is a subset of a puzzle's grips.
- Each piece has a **grip signature**, which is a subset of the 6 grips that determines which twists affect the piece. For example, the grip signature of the RUF corner is $\{ R, U, F \}$.

The grip signature tells us which twists affect which pieces.

Surprisingly, a grip signature is the only thing we need in order to describe how a piece behaves.

## Applying twists

To apply a twist $g[\sigma]$ to a puzzle:

1. Take every piece that has the grip $g$ in its grip signature.
2. 

!!! warning "The rest of this page is under construction"

## Grip group from twists

## Complex puzzles

### Anti moves

## Indistinguishable pieces

TODO: attitude sets

## Blocked grips

To model bandaging, ...

TODO

## Jumbling

TODO: ouch
