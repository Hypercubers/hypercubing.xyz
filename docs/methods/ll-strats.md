# Last Layer Strategies

This page is a work in progress.

This page documents some common last layer strategies for hypercubes (variants of these techniques will work on other puzzles too).

## OLL/PLL

First all of the pieces are oriented in increasing order by number of stickers.

To orient 2c pieces, use [EOLL algorithms](https://www.speedsolving.com/wiki/index.php?title=EOLL) from 2-look OLL.

To orient the 3c pieces, use RKT to set up the E slice of the last cell into a configuration that looks like a possible OCLL case. Then use OCLL algorithms to solve that case. 

!!!warning "Avoiding monotwist/flip"
    In higher dimensions, it's possible to have a single 3c+ piece twisted in place. To avoid this situation, make sure that your last OCLL algorithm setup will solve all of the remaining pieces of that piece type. For example if you have five pieces left to orient, don't set up an alg that orients four of them, because then you will be left with one. Instead, you can do an alg that orients three pieces, followed by an alg that orients two more.

To orient the 4c pieces, use RKT to set up OCLL cases, but this time you have to perform the OCLL alg with RKT. Again, it's possible to have just 1 4C left to orient, so be smart about your last setup and algorithm.

ّFor 4c pieces in 2^4, because of a lack of a need to preserve 2 and 3cs, something that can be done is grouping 4 unoriented corners together in a 1x1x2x2 block; then all 4 of these pieces can be oriented with just a U OLL case (F R U R' U' F') with big moves. Something similar can be done with the T and L OLL shapes as well. This way of orienting pieces is useful because not only are you solving more pieces at a time, but they don't take many moves to do so compared to doing the algs in RKT. If after reaching the OLL step, there are 5 4cs that are misoriented, it may be preferable do something else instead (solve a group of 3, and then 2), as you would want to avoid a monoflip.

To orient 5c+ pieces, you have to use RKT to setup OCLL cases, and then do the algorithm using double/triple/etc RKT.

For PLL, first permute the 2c pieces using U-perms or other EPLL algorithms. Then use RKT to permute the last layer like a lower dimensional puzzle using RKT.

## Direct LL

In 4D+, you can use F2L isolations to help you orient and permute blocks of pieces at the same time.

## Partial Direct LL

If you use direct LL techniques to just solve the F2L of the LL recursively until you're left with a "square" of pieces that need orienting and permuting. This group of pieces is the same amount as in 3D, except they can be oriented wrong in many different ways. From here, you can use algorithms to orient them, and then just normal PLL algorithms to permute them.

