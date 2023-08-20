# RKT Cancel Algs

## Notation

- single letter moves are the "big 3d" moves. (R = RO, U = UO, etc)


## OCLL
| OCLL Case      | RKT Cancel Algorithm                          |
| ----------- | ------------------------------------ |
| Sune<br>![Sune OCLL](http://cube.rider.biz/visualcube.php?fmt=svg&size=100&view=plan&bg=t&fc=lmlmmmmmlllmllllllllmllllllllllllllllllllllllllm)       | `R U R' ORUw U R ORUw U2 R'` |
| Antisune<br>![Antisune OCLL](http://cube.rider.biz/visualcube.php?fmt=svg&size=100&view=plan&bg=t&fc=lmmmmmlmlmllllllllmlllllllllllllllllmlllllllllll)       | `R U2 ORUw R' U' ORUw R U' R'` |
| H<br>![H OCLL](http://cube.rider.biz/visualcube.php?fmt=svg&size=100&view=plan&bg=t&fc=lmlmmmlmllllllllllmlmllllllllllllllllllllllllmlm)  | `R U2 R' U' ORUw R U R' U' ORUw R U' R'` |
| U<br>![U OCLL](http://cube.rider.biz/visualcube.php?fmt=svg&size=100&view=plan&bg=t&fc=mmmmmmlmllllllllllmlmlllllllllllllllllllllllllll)       | `(R U R' U R U2 R') IU (R U2 R' U' R U' R') IU'`  |
| T<br>![T OCLL](http://cube.rider.biz/visualcube.php?fmt=svg&size=100&view=plan&bg=t&fc=lmmmmmlmmlllllllllmllllllllllllllllllllllllllllm) | `(R U R' U R U2 R') IU' (R U2 R' U' R U' R') IU` |
| L<br>![L OCLL](http://cube.rider.biz/visualcube.php?fmt=svg&size=100&view=plan&bg=t&fc=mmlmmmlmmllmllllllmlllllllllllllllllllllllllllll) | `(R U R' U R U2 R') IU2 (R U2 R' U' R U' R') IU2` |
| Pi<br>![Pi OCLL](http://cube.rider.biz/visualcube.php?fmt=svg&size=100&view=plan&bg=t&fc=lmlmmmlmllllllllllllmlllllllllllllllmlmllllllmll) | `R U2 ORUw R2 U' R2 U' R2 ORUw U2 R` |

## EPLL
| EPLL Case | RKT Cancel Algorithm |
| ----------- | ------------------------------------ |
| Ub<br>![Ub EPLL](http://cube.rider.biz/visualcube.php?fmt=svg&size=100&view=plan&bg=t&alg=RU'RURURU'R'U'R2) | `R2 U R U ORUw R' U' R' U' R' ORUw U R'` |
| Ua<br>![Ua EPLL](http://cube.rider.biz/visualcube.php?fmt=svg&size=100&view=plan&bg=t&alg=R2URUR%27U%27R%27U%27R%27UR%27) | `R U' ORUw R U R U R ORUw U' R' U' R2` |
| Z<br>![Z EPLL](http://cube.rider.biz/visualcube.php?fmt=svg&size=100&view=plan&bg=t&alg=M2U%27M2U%27M%27U2M2U2M%27) | `(R U' R U R U R U' R' U' R2) IU2 (R2 U R U R' U' R' U' R' U R') IU2` <br> `M2 U' M U2 M' Iy2 M U2 M' U M2` |
| H<br> ![H EPLL](http://cube.rider.biz/visualcube.php?fmt=svg&size=100&view=plan&bg=t&alg=M2UM2U2M2UM2) | `M2 U' M2 U2 M IU2 M' U2 M IU2 M U M2` |