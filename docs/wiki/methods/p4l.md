# P4L

## History

PBLBC/P4L/PAL is an advanced algorithm set for speedsolving Melinda’s Physical 2x2x2x2. It is used after orientation and separation of 2 opposite cells, followed by (or simultaneously) orienting both layers on both of those cells. This leaves you with two 2x2x2 PBL cases, one on each cell. The original idea for this came from Connor Lindsay, who created most of the algorithms in his [algorithm sheet](https://12070019537911455222.googlegroups.com/attach/161f36cf43a69/2x2x2x2%20Algortithm%20Sheet.pdf?part=0.1&view=1&vt=ANaJVrGw6i3FB09hTT_j1I-MrwlEO06HD4aNgAMeVX9dhKhuSAwlgi86dUTi35_aIYhKNcy2kDcCHsOiajFmrosVdlso2N6w7DZeADzufEf001q0wFc9hnw).

2 years later, Rowan tried optimizing the algorithms, and compiling them in a new document, which can be found [here](https://docs.google.com/document/d/12CriaqJ1dYtAMpeY3c0dyLSCG9j37DEPKRWr4cl5i9U/edit?usp=sharing).

## Algorithms
Each layer can be in 3 different permutations: solved, adjacent swap, and opposite swap. This gives us 81 cases, but some of these are impossible. Cases can also be rearranged via Case Manipulation, further reducing the number of cases to 29. Practically however, only a few algorithms are used because all the bad cases are really slow to execute.

### Big 3D Cases
Big 3D cases are the cases where you have 2 pairs of the same layers, such as OOAA. In such a case, you can just use the normal 2^3^ PBL algorithm for that case (but it must be a version with the moveset `<R2,L2,F2,B2,U*,D*>` only, due to the restrictions in turning the puzzle).
