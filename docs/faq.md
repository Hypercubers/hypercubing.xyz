# FAQ

## What is hypercubing?

??? question "What does hypercubing mean?"
    Just as cubing is the hobby of solving 3D twisty puzzles, *Hypercubing* is solving 4D+ twisty puzzles.

??? question "What is the 4th dimension?"
    Hypercubing deals with higher dimensions of space. Essentially all this means is just another direction (humans can only percieve 3 orthogonal directions, which is what makes this so challenging).
    ??? question "Isn't the 4th dimension time?"
        While time is a dimension, it behaves completely differently from the spatial dimensions. You can't move backward through it, measure shapes in it, etc. Another factor that can lead to confusion is the term spacetime or 4D spacetime. This is why physicists sometimes use the term 3+1 dimensions to describe our world, meaning that hypercubing would take place in 4+1 dimensions (or n+1 where n>3).
    See <https://www.qfbox.info/4d/4dfaq> for answers to other similar questions.

??? question "What is a 4-dimensional Rubik's cube? How does that make any sense?"
    Read the [MC4D FAQ](https://superliminal.com/cube/faq.html)


??? question "Where can I interact with other hypercubers?"
    The [Hypercubers Discord Server](https://discord.gg/7cdBEm49xQ) has the most active community of hypercubers and contains the latest updates on developing projects and speedsolving strategies. The [Hypercubing Google Group](https://groups.google.com/g/hypercubing) is a good option for those who prefer mailing lists or less frequent updates. Also check out the [r/Hypercubers subreddit](https://www.reddit.com/r/Hypercubers/).

## Virtual puzzles

??? question "What program should I download?"
    It depends on what exactly you want to do, but generally, [Hyperspeedcube](https://ajfarkas.dev/hyperspeedcube/) and MC4D will suit your needs. See the [software](/software) page for links to all the major programs.

??? question "How do I start learning to solve 4D puzzles?"
    First, download [Hyperspeedcube](https://ajfarkas.dev/hyperspeedcube/) or MC4D and start experimenting with the 3^4^! Try to solve one-move scrambles and keep practicing that until you're comfortable. Once you can solve one-move scrambles with ease, pick a [method](/methods) to learn.

??? question "Why not start with the 2^4^?"
    The 2^4^ is particularly disorienting for beginners because half of the puzzle turns at once. As a result, while the 2^4^ strategy is technically simpler, it's actually more challenging to wrap your head around, especially when you're new to 4D puzzles. Just like how the 3^3^ is a better starting puzzle in 3D, you can learn lots of important concepts from the 3^4^ that will help you with other 4D puzzles.

??? question "What methods exist for the 3^4^?"
    Many 3D methods can just be scaled up and used on the 4D cube. Some notable methods are:

    - [Layer-by-layer](https://youtu.be/h4n_QdZGXf8)
    - [CFOP](/methods/3x3x3x3/cfop) — 4D CFOP
    - [3Block](/methods/3x3x3x3/3block) — 4D FreeFOP, ~20% fewer moves compared to CFOP
    - [Octachoroux](/methods/3x3x3x3/octachoroux) — 4D Roux, but awkward to use and contains many parity issues

    Alternatively, join a voice chat on the [Hypercubers Discord Server](https://discord.gg/7cdBEm49xQ) and someone will teach you!

??? question "What's [God's number][cube20] for \[puzzle]?"
    God's number for 3^3^ took [lots of creative mathematical work and 35 years of CPU time][cube20] to scan $\sim 4.3 \times 10^{19}$ states. For comparison, the 2^4^ has $\sim 3.4 \times 10^{27}$ states and 4^3^ has $\sim 7.4 \times 10^{45}$ states. **There isn't a single nontrivial 4D puzzle for which God's number is known, let alone remotely possible to compute.**

    There are three strategies we can use to estimate it:

    1. We can set a **lower bound** using the branching factor of move sequences. Let's take the 2^4^, for example. There are 92 possibilities for the first move and 69 possibilities for each subsequent move.[^24moves] To even have a chance of reaching $4.3 \times 10^{19}$ states, we need at least that many move sequences. $log_{69}(\frac{4.3 \times 10^{19}}{92}) \approx 9.6$, so **God's number for 2^4^ is at least 10**.
    2. We can set an **upper bound** by analyzing the worst-case solution of every stage in a given method. [Here is an example calculation for 3^4^ using 3-block.](https://discord.com/channels/852389089268858922/867087791342223430/1118646417091743746) Anderson Taurence wrote a [3-stage 2^4^ solver](https://github.com/ajtaurence/Hypersolve) using a method that has a worst case of 39 STM, so **God's number for 2^4^ is at most 39**.
    3. We can get an **estimate** by measuring move counts produced by a near-optimal solver. For example, Anderson's solver typically produces solutions in the range of 20-30 STM. Note that **this solver does not produce optimal solutions**[^optimal], and **we cannot measure _every_ scramble** so it's impossible to use this to put a hard bound on God's number, but **God's number for 2^4^ is probably not higher than 20-30**.

    In summary, **God's number for 2^4^ is definitely between 10 and 39 inclusive, and probably $\sim 15 \pm 5$**. A better method or lots of compute time might improve slightly on the upper bound, but unless there is some fundamental breakthrough in our understanding of computation, there's basically no way to improve on the lower bound or estimate. If you're an expert in quantum computing then perhaps you can devise some clever quantum algorithm to help, but as of 2023 quantum computers haven't solved a single real-world problem faster than a classical computer so we remain skeptical.

[cube20]: http://cube20.org/
[^24moves]: Only one cell on each axis matters. Each face has 24 orientations, but one of those is the identity and so doesn't matter. $23 \times 4 = 92$. For subsequent moves, must turn a different axis. $23 \times 3 = 69$ (nice)
[^optimal]: It does converge on optimal solutions when run for a very long time, but this is impractical for all but the simplest scrambles.

## Physical puzzles

??? question "What is a physical 4D puzzle?"
    The physical 4D puzzles are puzzles that are perfectly analogous to the virtual 4D puzzles, but implemented in the physical world. See our [physical puzzles](/puzzles/physical) page, the [Physical Puzzle page on the Superliminal wiki](http://wiki.superliminal.com/wiki/Physical_Puzzle), and [Rowan Fortier's video about the history of physical hypercubes](https://www.youtube.com/watch?v=QTc-rG-nunA).

??? question "How do I get Melinda's Physical 2^4^?"
    All the information can be found on [the Superliminal website](https://superliminal.com/cube/2x2x2x2/), including the history, statistics, and Hall of Fame.

??? question "Can I purchase any of Grant's hypercuboids?"
    No. Currently, they are one-of-a-kind. You would have to design and 3D print them yourself.

??? question "What physical 4D puzzles exist?"
    [1x2x2x2](/puzzles/physical/1x2x2x2), [1x2x2x3](/puzzles/physical/1x2x2x3), [1x2x3x3](/puzzles/physical/1x2x3x3), [1x3x3x3](/puzzles/physical/1x3x3x3), [2x2x2x2](/puzzles/physical/2x2x2x2), [2x2x2x3](/puzzles/physical/2x2x2x3), [2x2x3x3](/puzzles/physical/2x2x3x3), [2x3x3x3](/puzzles/physical/2x3x3x3), [3x3x3x3](/puzzles/physical/3x3x3x3), and [simplex](/puzzles/physical/4d-pyraminx).


??? question "Which 4D shapes can be turned into physical puzzles?"
    While it's always possible to just arrange the stickers on a table, the real challenge is in finding a design that is piece-based instead of sticker-based and fits in a compact shape that isn't too horrendous to turn. It just requires out-of-the-box thinking. We currently have several renderings for physical puzzles that haven't been built in real life yet; see the [Physical Puzzles](/puzzles/physical) page for an incomplete list.

## Speedsolving

??? question "What are the speedsolving records for 4D puzzles?"
    See the [leaderboards](/leaderboards). To get on the leaderboard, read the [submission guidelines](/leaderboards/rules) and submit a video of your solve to [this form](https://forms.gle/Y7Vpi3pb8989Ay8W8).

??? question "Why not use speedrun.com?"
    Speedrun.com does not allow "generic Rubik's Cube simulators." We applied and were rejected.

??? question "I don't know full OLL/PLL/ZBLL/etc. Can I still get fast at 4D?"
    Absolutely! Most 4D speed methods are highly intuitive, and world-record times often use just 2-look OLL and PLL. Executing algorithms is a very negligible part of the solve compared to the massive amounts of pair or block building.

??? question "Does full OLL/PLL/etc. exist for 4D puzzles? What about 4D algorithm explorers?"
    There's so many cases for each step of the solve that creating a complete algorithm set is basically impossible, and there's so many options for moves that algorithm explorers are infeasible. Almost every algorithm we have is based on an algorithm from 3D, and the only search program we have is a sort of optimizer for one very specific kind of algorithm derived from 3D.

## Does this puzzle exist?

??? question "4D Square-1"
    Square-1 is fundamentally a bandaged dodecagonal prism. There are so many ways to extend that into 4D that there isn't really a canonical "4D square-1"

??? question "4D Skewb"
    Again, there's lots of ways to generalize a skewb. If you just want cuts that look like a skewb, there's a few different puzzles that emulate that. If you want a half-cut vertex-turning hypercube, that's a thing too! It just doesn't "look like" a traditional skewb. For more 4D skewbs, including pictures, see [here](/puzzles/4d-skewb).

??? question "8-dimensional and higher"
    Above 5 dimensions, cube puzzles aren't more difficult or interesting, just more tedious and computationally expensive. But there might be some wild hyperpuzzles yet to be discovered up there, say one based on the very special geometry of the [E8 Lattice](https://en.wikipedia.org/wiki/E8_lattice)!

??? question "3D Rubik's Clock"
    Instead of rotating circles in 2D, you can rotate spheres in 3D. This is a more interesting puzzle than the traditional Rubik's Clock because moves don't commute. No one's written a program yet to simulate it but you totally could!

??? question "How do I make a 4D \[thing]?"
    **:sparkles: Generalising Things to 4D: A Handy Guide :sparkles:**

    1. Understand and define the thing you're generalising
    2. Find where your definitions reference or assume something dimension-specific
    3. Rewrite your definitions to avoid dimension-specific references or assumptions
    4. Find what 4D object fits your new definitions (there may be one, several, or none)
