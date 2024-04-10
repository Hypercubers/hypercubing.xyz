---
title: Canonical Moves
---

# Physical 2×2×2×2 Canonical Moves & Notation

!!! info
    Watch [Melinda Green's video](https://www.youtube.com/watch/DzRH8BOJL8Q) for a quick overview of the canonical moves

The Canonical Moveset is a set of moves agreed upon by the community for solving the physical 2^4^. To get accepted into the official [Hall of Fame](https://superliminal.com/cube/2x2x2x2/#solutions), you **must** follow the canonical moves exactly. Make sure that you have already solved a [virtual 2^4^](/puzzles/2x2x2x2.md), and are familiar with how the pieces of the [physical 2^4^](/puzzles/physical/2x2x2x2/index.md) correspond. Also make sure that you know your 3D rotations (`x` `y` `z`) very well.

## Canonical Moves

### Simple Rotations

!!! example inline end "Simple Rotations"
    ![Simple puzzle rotations on Melinda's 2×2×2×2](https://cloud.hypercubing.xyz/assets/img/phys/melinda_2x2x2x2_rotations.png)

A lot of the whole puzzle reorientations can be reached without the need for the [gyro algorithm](#gyro). These are called simple rotations, and consist of rotaing the L and R cells together in opposing directions (as to not change the state of the puzzle, only its orientation).

`zy` `yz` `yw` `wy` `zw` `wz`

### Cell Twists

The left and right cells of the puzzle can be twisted into any reorientation of a cube. In other words, there are 23 different twists of the L/R cells:

Left cell twists: `Ly` `Ly'` `Ly2` `Lx2` `Lz2` `Lx2,y` `Lx2,y'` `Lx` `Lx,y` `Lx,y'` `Lx,y2` `Lx'` `Lx',y` `Lx',y'` `Lx',y2` `Lz` `Lz,y` `Lz,y'` `Lz,y2` `Lz'` `Lz',y` `Lz',y'` `Lz',y2`

Right cell twists: `Ry` `Ry'` `Ry2` `Rx2` `Rz2` `Rx2,y` `Rx2,y'` `Rx` `Rx,y` `Rx,y'` `Rx,y2` `Rx'` `Rx',y` `Rx',y'` `Rx',y2` `Rz` `Rz,y` `Rz,y'` `Rz,y2` `Rz'` `Rz',y` `Rz',y'` `Rz',y2`

Each move here either starts with an L or an R, followed by the rotations (separated by commas).

### Inside/Outside Twists

!!! example inline end "Ix2 twist"
    ![Ix2 move on physical 2×2×2×2](https://cloud.hypercubing.xyz/assets/img/phys/melinda_2x2x2x2_canonical_Ix2.png)

The I and O cells are the sides with the next most turning freedom after L and R. This was referred to as an "axial twist" in Melinda's video. The canonical moves for the I/IO cells are `Ix` `Ix'` `Ix2` `Ox` `Ox'` `Ox2`

These twists can be difficult to perform for speedsolving, so most people tend to split it up by temporarily doing 2 illegal 90 degree twists that yield the same result. Be careful though, as this can lead to an illegal state if you accidentally screw up while doing it this way.


### Slab Twists

!!! example inline end "U2 twist"
    ![U2 move on physical 2×2×2×2](https://cloud.hypercubing.xyz/assets/img/phys/melinda_2x2x2x2_canonical_U2.png)

The remaining canonical twists involve picking up a 2x2x4 "slab" off the puzzle, and rotating it 180 degrees in the same plane. These slabs you can pick up are the U, F, D, and B cells. Because the slabs can only be turned 180 degrees those moves will just be referred to as `U2` `F2` `D2` `B2`


### Gyro

If you try to scramble the puzzle with all the moves above, you will quickly notice that the 2 colours on the x-axis aren't mixing with the other colours. This is because the simple rotations and slab twists are restricting what we can do because of the symmetry of the physical puzzle. To fix this, we need a series of illegal moves that rotate the puzzle 4-dimensionally in a way that changes the x-axis. This is called the Gyro, and will allow us to access all the rest of the puzzle rotations (`xz` `zx` `yx` `xy` `xw` `wx`)

![Rowan performing the Gyro algorithm](https://cloud.hypercubing.xyz/assets/img/phys/melinda_2x2x2x2_gyro.gif)

There are several different algorithms for this, some of which gyro different axes. Melinda has several videos about different gyro algorithms, the shortest known one being 6 snaps. Below is a common gyro algorithm that several people in the community use.

- Take the left endcap off and put it on the right so it becomes the right endcap (this brings the puzzle into the inverted state)
- `Ly` `Ry'`
- Take the right endcap off and put it on the left so it becomes the left endcap (this brings the puzzle back into the normal state)
- `Rx2` `B2` `D2` `Lx2`

## Expanded Canonical Moveset

The expanded canonical moveset is what is accepted for the [Hypercubing.xyz leaderboards](/leaderboards/index.md). These moves all correspond perfectly with twists on the [virtual puzzle](/puzzles/2x2x2x2.md), but weren't allowed in the canonical moveset because people agreed not to for some reason.

### Extra slab twists

Several new slab twists are added. For the U cell, this means going from having just `Uy2` to now having `Uy2` `Ux,y2` `Ux',y2` `Ux` `Ux'` `Ux2` `Uz2`

### Extra I/O cell twists

`Iz2` `Iy2` `Oz2` `Oy2` are added (although they are very hard to fingertrick and perform quickly).
