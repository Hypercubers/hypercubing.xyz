# RKT Cancel Algorithms

!!! warning "These won't help you solve a puzzle for the first time"

    You do not need to learn RKT cancel algs to solve any puzzle. RKT can and should be done completely intuitively unless you are already speedsolving at a high level and wish to improve this step.

- See [Notation](https://hypercubing.xyz/theory/notation/) and [Commutator notation](https://hypercubing.xyz/techniques/commutators/) first.
- Single letter moves are the "Big 3D" moves. (`R` = `RO`, `U` = `UO`, etc.)

## RKT Cancel Algorithms

### 4^4^ edge swap parity

| Image                                                                                                                                      | Description             | RKT Cancel Algorithm             |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------- | -------------------------------- |
| ![4^4 edge swap parity](http://cube.rider.biz/visualcube.php?fmt=svg&size=75&pzl=4&view=plan&bg=t&fc=yyyyyyyyyyyyyyyyrbbrrrrrrrrrrrrrbrrb) | UF and UR edges swapped | `[f' l': [[r' U' l': D2], Iy2]]` |

### F2L triggers

| Image                                                                                                                                      | Description             | 2RKT Cancel Algorithm             |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------- | -------------------------------- |
| ![Made Insert](https://cube.rider.biz/visualcube.php?fmt=svg&size=75&pzl=3&bg=t&alg=RUR%27) | Made Insert | `R {1-2}Ozx2 U' R' {1-2}Ozx2` |
| ![Split Insert](https://cube.rider.biz/visualcube.php?fmt=svg&size=75&pzl=3&bg=t&alg=RU%27R%27) | Split Insert | `{1-2}Ozx2 R U {1-2}Ozx2 R'` |
| ![Double Sexy](https://cube.rider.biz/visualcube.php?fmt=svg&size=75&pzl=3&bg=t&alg=URU%27R%27URU%27R%27) | Double Sexy | `R U R' U' {1-2}Ozx2 R U R' U' {1-2}Ozx2` |

### EOLL

| Image                                                                                                                                     | Name     | RKT Cancel Algorithm                              |
| ----------------------------------------------------------------------------------------------------------------------------------------- | -------- | ------------------------------------------------- |
| ![Dots EOLL](https://cube.rider.biz/visualcube.php?fmt=svg&size=75&view=plan&bg=t&fc=llllmlllllmllllllllmllllllllmllllllllmlmllllllmlm)   | Dots     | `F (R U R' U') F' 2Oy2 Fw (R U R' U') Fw'`        |
| ![Backwards L EOLL](https://cube.rider.biz/visualcube.php?fmt=svg&size=75&view=plan&bg=t&fc=lmlmmlllllmllllllllmllllllllllllllllllllllllllll)   | Backwards L     | `F (R U R' U') {1-2}Ozx2 (R U R' U') {1-2}Ozx2 F'`        |
| ![Line EOLL](https://cube.rider.biz/visualcube.php?fmt=svg&size=75&view=plan&bg=t&fc=lllmmmlllllllllllllmllllllllllllllllllllllllllml)   | Line     | `F (R U {1-2}Ozx2 R' U' {1-2}Ozx2) F'`        |

### OCLL

| Image                                                                                                                                     | Name     | RKT Cancel Algorithm                              |
| ----------------------------------------------------------------------------------------------------------------------------------------- | -------- | ------------------------------------------------- |
| ![Sune OCLL](http://cube.rider.biz/visualcube.php?fmt=svg&size=75&view=plan&bg=t&fc=lmlmmmmmlllmllllllllmllllllllllllllllllllllllllm)     | Sune     | `R U R' {1-2}Ozx2 U R {1-2}Ozx2 U2 R'`                      |
| ![Antisune OCLL](http://cube.rider.biz/visualcube.php?fmt=svg&size=75&view=plan&bg=t&fc=lmmmmmlmlmllllllllmlllllllllllllllllmlllllllllll) | Antisune | `R U2 {1-2}Ozx2 R' U' {1-2}Ozx2 R U' R'`                    |
| ![H OCLL](http://cube.rider.biz/visualcube.php?fmt=svg&size=75&view=plan&bg=t&fc=lmlmmmlmllllllllllmlmllllllllllllllllllllllllmlm)        | H        | `R U2 R' U' {1-2}Ozx2 R U R' U' {1-2}Ozx2 R U' R'`          |
| ![U OCLL](http://cube.rider.biz/visualcube.php?fmt=svg&size=75&view=plan&bg=t&fc=mmmmmmlmllllllllllmlmlllllllllllllllllllllllllll)        | U        | `(R U R' U R U2 R') Iy (R U2 R' U' R U' R') Iy'`  |
| ![T OCLL](http://cube.rider.biz/visualcube.php?fmt=svg&size=75&view=plan&bg=t&fc=lmmmmmlmmlllllllllmllllllllllllllllllllllllllllm)        | T        | `(R U R' U R U2 R') Iy' (R U2 R' U' R U' R') Iy`  |
| ![L OCLL](http://cube.rider.biz/visualcube.php?fmt=svg&size=75&view=plan&bg=t&fc=mmlmmmlmmllmllllllmlllllllllllllllllllllllllllll)        | L        | `(R U R' U R U2 R') Iy2 (R U2 R' U' R U' R') Iy2` |
| ![Pi OCLL](http://cube.rider.biz/visualcube.php?fmt=svg&size=75&view=plan&bg=t&fc=lmlmmmlmllllllllllllmlllllllllllllllmlmllllllmll)       | Pi       | `R U2 {1-2}Ozx2 R2 U' R2 U' R2 {1-2}Ozx2 U2 R`              |

### CPLL

| Image                                                                                                | Name | RKT Cancel Algorithm                                                 |
| ---------------------------------------------------------------------------------------------------- | ---- | -------------------------------------------------------------------- |
| ![Aa CPLL](https://cube.rider.biz/visualcube.php?fmt=svg&size=75&view=plan&bg=t&case=R%27FR%27B2RF%27R%27B2R2) | Aa   | `(Ix) R' U {1-2}Oz R' D2 R {1-2}Oz' U' R' D2 {1-2}Oz' R2` |
| ![Ab CPLL](https://cube.rider.biz/visualcube.php?fmt=svg&size=75&view=plan&bg=t&alg=R%27FR%27B2RF%27R%27B2R2)  | Ab   | ` (Ix) R2 {1-2}Oz D2 R U {1-2}Oz R' D2 R {1-2}Oz' U' R`         |
| ![Na CPLL](https://cube.rider.biz/visualcube.php?fmt=svg&size=75&view=plan&bg=t&case=RU%27LU2R%27UL%27RU%27LU2R%27UL%27)     | Na | `R U' L U2 R' U L' {1-2}Oy2 R U' L U2 R' U L'`     |
| TODO      | Nb   |     |

### EPLL

| Image                                                                                                              | Name | RKT Cancel Algorithm                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ---- | ----------------------------------------------------------------------------------------------------------- |
| ![Ub EPLL](http://cube.rider.biz/visualcube.php?fmt=svg&size=75&view=plan&bg=t&alg=RU%27RURURU%27R%27U%27R2)               | Ub   | `R2 U R U {1-2}Ozx2 R' U' R' U' R' {1-2}Ozx2 U R'`                                                                    |
| ![Ua EPLL](http://cube.rider.biz/visualcube.php?fmt=svg&size=75&view=plan&bg=t&alg=R2URUR%27U%27R%27U%27R%27UR%27) | Ua   | `R U' {1-2}Ozx2 R U R U R {1-2}Ozx2 U' R' U' R2`                                                                      |
| ![Z EPLL](http://cube.rider.biz/visualcube.php?fmt=svg&size=75&view=plan&bg=t&alg=M2U%27M2U%27M%27U2M2U2M%27)      | Z    | `(R U' R U R U R U' R' U' R2) Iy2 (R2 U R U R' U' R' U' R' U R') Iy2`<br>alternate: `M2 U' M U2 M' Iy2 M U2 M' U M2` |
| ![H EPLL](http://cube.rider.biz/visualcube.php?fmt=svg&size=75&view=plan&bg=t&alg=M2UM2U2M2UM2)                    | H    | `M2 U' M2 U2 M Iy2 M' U2 M Iy2 M U M2`<br>alternate: `R2 U2 R U2 {1-2}Ozx2 R2 U2 R2 {1-2}Ozx2 U2 R U2 R2`     |


## 2RKT Cancel Algorithms

| Image                                                                                                                                      | Description             | 2RKT Cancel Algorithm             |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------- | -------------------------------- |
| ![Double Sexy Move](https://cube.rider.biz/visualcube.php?fmt=svg&size=75&pzl=3&bg=t&alg=URU%27R%27URU%27R%27) | Double Sexy Move | `R U {1-2}Ozx2 R' U' {1-2}Azx2 R U {1-2}Ozx2 R' U' {1-2}Azx2` |

### OCLL

| Image                                                                                                                                     | Name     | RKT Cancel Algorithm                              |
| ----------------------------------------------------------------------------------------------------------------------------------------- | -------- | ------------------------------------------------- |
| ![H OCLL](http://cube.rider.biz/visualcube.php?fmt=svg&size=75&view=plan&bg=t&fc=lmlmmmlmllllllllllmlmllllllllllllllllllllllllmlm)        | H        | `R U2 {1-2}Azx2 R' U' {1-2}Ozx2 R U {1-2}Azx2 R' U' {1-2}Ozx2 R U' R'`          |
| ![U OCLL](http://cube.rider.biz/visualcube.php?fmt=svg&size=75&view=plan&bg=t&fc=mmmmmmlmllllllllllmlmlllllllllllllllllllllllllll)        | U        | `(R U R' {1-2}Azx2 U R {1-2}Azx2 U2 R') Iy (R U2 {1-2}Azx2 R' U' {1-2}Azx2 R U' R') Iy'`  |
| ![T OCLL](http://cube.rider.biz/visualcube.php?fmt=svg&size=75&view=plan&bg=t&fc=lmmmmmlmmlllllllllmllllllllllllllllllllllllllllm)        | T        | `(R U R' {1-2}Azx2U R {1-2}Azx2 U2 R') Iy' (R U2 {1-2}Azx2 R' U' {1-2}Azx2 R U' R') Iy`  |
| ![L OCLL](http://cube.rider.biz/visualcube.php?fmt=svg&size=75&view=plan&bg=t&fc=mmlmmmlmmllmllllllmlllllllllllllllllllllllllllll)        | L        | `(R U R' {1-2}Azx2 U R {1-2}Azx2 U2 R') Iy2 (R U2 {1-2}Azx2 R' U' {1-2}Azx2 R U' R') Iy2` |

### EPLL

| Image                                                                                                              | Name | RKT Cancel Algorithm                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ---- | ----------------------------------------------------------------------------------------------------------- |
| ![Z EPLL](http://cube.rider.biz/visualcube.php?fmt=svg&size=75&view=plan&bg=t&alg=M2U%27M2U%27M%27U2M2U2M%27)      | Z    | `(R U' {1-2}Azx2R U R U R {1-2}Azx2 U' R' U' R2) Iy2 (R2 U R U {1-2}Azx2 R' U' R' U' R' {1-2}Azx2 U R') Iy2`|