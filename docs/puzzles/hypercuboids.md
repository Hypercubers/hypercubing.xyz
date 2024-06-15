
# Hypercuboids

## Introduction
A hypercuboid is the multi-dimensional version of a cuboid.  
In a general context, we define a hypercuboid as an $n$-dimensional puzzle denoted by $a_1 \times a_2 \times \dots \times a_n$.  
 For the sake of clarity and consistency, we will use $a_1,a_2, \dots a_n$ as non-decreasing values.  
 
## Structure
A hypercuboid, as defined, is composed of $2n$ cells, each of which is $(n-1)$-dimensional.

For a general element $a_i$, we will define  $\bar{a_i}= \max (0, a_i-2)$.

Given $k>0$ and $n \geq 1$, we can denote the cyclic sum of the products of elements $\bar{a_1}, \bar{a_2}, \dots, \bar{a_n}$ taken $n-k$ at a time by $Cyc(n,k)$.  
- For example: $Cyc(5,4) = \bar{a_1} + \bar{a_2} + \bar{a_3}  + \bar{a_4} +\bar{a_5}$, i.e. the sum of groups of 5-4=1 elements, chosen in $\bar{a_1}, \bar{a_2}, \bar{a_3}, \bar{a_4}, \bar{a_5}$.   
- Another example: $Cyc(4,2) = \bar{a_1} \bar{a_2} + \bar{a_1} \bar{a_3} + \bar{a_1} \bar{a_4} + \bar{a_2} \bar{a_3} + \bar{a_2} \bar{a_4} + \bar{a_3} \bar{a_4}$, i.e., the sum of the products of all possible ordered pairs made with $\bar{a_1}, \bar{a_2}, \bar{a_3}, \bar{a_4}$.


Note that $Cyc(n,k)$ has $C_{n,k} = \binom{n}{k}$ terms.  
We can also define $Cyc(n,n)=1$

Using the above notation, the $a_1 \times a_2 \times \dots \times a_n$ hypercuboid has $2^k\cdot C(n,k)$ pieces which are $k$-colored.

For example, consider the $2 \times 3 \times 5 \times 7$ hypercuboid, in this case:  

- $a_1$ =2, so $\bar{a_1}=0$,  
- $a_2$ =3, so $\bar{a_2}=1$,  
- $a_3$ =5, so $\bar{a_3}=3$,  
- $a_4$ =7, so $\bar{a_4}=5$.    

So there will be:  

- For 1-colored pieces we have:  
  $2^1 \cdot Cyc(4,1)=2^1\cdot (0\cdot1\cdot3 + 0\cdot 3 \cdot 5 + 1 \cdot 3 \cdot 5 + 0\cdot 1 \cdot5 )=$  
  $=2 \cdot (0+0+15+0)=30$  pieces.  

- For 2-colored pieces we have:  
  $2^2 \cdot Cyc(4,2)=2^2\cdot ( 0\cdot 1+ 0\cdot 3 +0 \cdot 5  + 1\cdot3 +1\cdot 5 + 3\cdot 5  )=$  
  $=4 \cdot (0+0+0+3+5+15)=92$  pieces.    

- For 3-colored pieces we have:    
  $2^3 \cdot Cyc(4,3)=2^3\cdot (0+1+3+5  )=$   
  $=8 \cdot 9=72$  pieces.

- For 4-colored pieces we have:  
  $2^4 \cdot Cyc(4,4)=2^4\cdot 1=  16$ pieces.  


## 4D Hypercuboids

In 4 dimensions, a hypercuboid is denoted as $a \times b \times c \times d$.  
$a \times b \times c \times d$ is composed of 8 cells: 2 $(a \times b \times  c)$-cells, 2 $(a \times b \times  d)$-cells, 2 $(b \times c \times  d)$-cells  and 2 $(a \times c \times  d)$-cells.  
In the following sections, we will denote some of these cells using the classic 3-dimensional puzzle names, in particular: 

- "tower cell" will indicate a $2 \times 2 \times  3$-cell;
- "domino cell"  will indicate a  $2 \times 3 \times  3$-cell;
- " $n$ -cubic cell" will indicate a  $n \times n \times  n$-cell.

### General solving strategies
- Hypercuboids in the form $1 \times a \times b \times c$ can be solved by first orienting the $a \times b \times c$-cells, then solving the puzzle like a 3-dimensional $a \times b \times c$.
- Hypercuboids in the form $2 \times a \times b \times c$ can be solved first by solving the $a \times b \times c$-cells and then solving the opposite, eventually adapting the solution for new possible cases.
- If 2 dimensions have the same values, the puzzle can be seen as a duoprism. 
- If 3 dimensions have the same values, i.e. there is a couple of $n$-cubic cells, RKT can be used on these cells.
- If 4 dimensions have the same values, we have a hypercube.


### Some notable 4D hypercuboids

In some cases an idea of a possible solution method provided by [Ema](/leaderboards/solvers/battistin.md) will be present but not spoiled.

#### 1×3×3×3
| Puzzle | 4c pieces | 3c pieces | 2c pieces | 1c pieces | 
|:---:|:---:|:---:|:---:|:---:| 
| 1×1×3×3 | 16 | 24 | 12 | 2 |

<details>
  <summary>Solve idea (click to reveal)</summary>
- Orient both cubic cells.<br>  
- Solve 3^3 cube, paying attention to corner orientation.<br> 
</details>

#### 2×2×2×3


| Puzzle | 4c pieces | 3c pieces | 2c pieces | 1c pieces | 
|:---:|:---:|:---:|:---:|:---:| 
| 2×2×2×3 | 16 | 8 | 0 | 0 |

<details>
  <summary>Solve idea (click to reveal)</summary>
- Solve the middle 3-colored pieces of a tower cell (similar to solving a $1 \times 2 \times 2 \times 2$ ).<br>
- Orient both $2$-cubic cells at the same time, slicing the solved part for exchanging pieces,being careful to use an even number of slice moves.  <br>   
- Use RKT to solve the cubic cells, using the same tower cells as R.    <br>
- Fix tower cell middle layer.  <br>
</details>

#### 2×2×3×3

| Puzzle | 4c pieces | 3c pieces | 2c pieces | 1c pieces | 
|:---:|:---:|:---:|:---:|:---:| 
| 2×2×3×3 | 16 | 16 | 4 | 0 |
  

<details>
  <summary>Solve idea (click to reveal)</summary>
- Solve a domino cell.  <br>   
- Orient the opposite domino cell, potentially re-solving the first cell.  <br>   
- Move pieces on the correct layers of the last cell.  <br>   
- Solve last domino cell using 3-dimensional cuboid algorithms an even number of times and conjugating between them.  <br>   
</details>

#### 2×3×3×3
| Puzzle | 4c pieces | 3c pieces | 2c pieces | 1c pieces | 
|:---:|:---:|:---:|:---:|:---:| 
| 2×3×3×3 | 16 | 24 | 12 | 2 |

<details>
  <summary>Solve idea (click to reveal)</summary>
- Orient both 3-cubic cells at the same time.   <br>   
- Solve first cubic cell.   <br>   
- Solve the second cubic cell using RKT. <br>   
</details>

#### 2×2×2×4
| Puzzle | 4c pieces | 3c pieces | 2c pieces | 1c pieces | 
|:---:|:---:|:---:|:---:|:---:| 
| 2×2×2×4 | 16 | 16 | 0 | 0 |

#### 2×3×4×5
| Puzzle | 4c pieces | 3c pieces | 2c pieces | 1c pieces | 
|:---:|:---:|:---:|:---:|:---:| 
| 2×3×4×5 | 16 | 48 | 44 | 12 |

The smallest 4-dimensional "brick" hypercuboid.  

## Create your 4D hypercuboids in MPUlt
Here is a way to create your own  4D hypercuboid in MPUlt.  
The result would not be isometric, but still working.

Step 1: Recognize the form of your hypercuboid in one of the following

- $a \times b \times c \times d$,
- $a \times a \times b \times c$,
- $a \times a \times b \times b$,
- $a \times b \times b \times b$,
- $a \times a \times a \times a$ (hypercubes).

Step 2: Recognize the values of the letters, then substitute the letter with the corresponding string from the following table:

| Value| String |
|:----|:----|
|2 | 0.0 |
|3 | 0.333 -0.333 |
|4 | 0.5 0.0 -0.5 |
|5 | 0.6 0.2 -0.2 -0.6 |
|6 | 0.667 0.333 0.0 -0.333 -0.667 |
|7 | 0.714 0.429 0.143 -0.143 -0.429 -0.714 |
|8 | 0.75 0.5 0.25 0.0 -0.25 -0.5 -0.75 |
|9 | 0.778 0.556 0.333 0.111 -0.111 -0.333 -0.556 -0.778 |

So if $a=3$, you need to change "CUT-A" with "0.333 -0.333" in the general puzzle code, and so on.

Step 3: Insert the created code in "MPUlt_puzzles.txt" file, save and enjoy your puzzle.

### Case a×b×c×d

General code:  
```
Puzzle NAME_AXBXCXD
Dim 4
NAxis 4
Faces 1,0,0,0 0,1,0,0 0,0,1,0 0,0,0,1
Group 1,0,0,0/0,1,0,0 1,0,0,0/0,0,1,0 1,0,0,0/0,0,0,1
Axis 1,0,0,0
Twists 0,1,0,0/0,0,1,0 0,1,0,0/0,0,0,1 0,0,1,0/0,0,0,1
Cuts CUT-A
Axis 0,1,0,0
Twists 1,0,0,0/0,0,1,0 1,0,0,0/0,0,0,1 0,0,1,0/0,0,0,1
Cuts CUT-B
Axis 0,0,1,0
Twists 1,0,0,0/0,1,0,0 1,0,0,0/0,0,0,1 0,0,0,1/0,1,0,0
Cuts CUT-C
Axis 0,0,0,1
Twists 1,0,0,0/0,1,0,0 1,0,0,0/0,0,1,0 0,0,1,0/0,1,0,0
Cuts CUT-D
```

### Case a×a×b×c

General code: 
```
Puzzle NAME_AXAXBXC
Dim 4
NAxis 3
Faces 1,0,0,0 0,0,1,0 0,0,0,1
Group 1,0,0,0/1,1,0,0 1,0,0,0/0,0,1,0 1,0,0,0/0,0,0,1
Axis 1,0,0,0
Twists 0,1,0,0/0,0,1,0 0,1,0,0/0,0,0,1 0,0,1,0/0,0,0,1
Cuts CUT-C
Axis 0,0,1,0
Twists 1,0,0,0/1,1,0,0 1,0,0,0/0,0,0,1 0,0,0,1/0,1,0,0
Cuts CUT-B
Axis 0,0,0,1
Twists 1,0,0,0/1,1,0,0 1,0,0,0/0,0,1,0 0,0,1,0/0,1,0,0
Cuts CUT-A
```

### Case a×a×b×b
General code: 
```
Puzzle NAME_AXAXBXB
Dim 4
NAxis 2
Faces 1,0,0,0 0,0,1,0
Group 1,0,0,0/1,1,0,0 1,0,0,0/0,0,1,0 0,0,1,0/0,0,1,1
Axis 1,0,0,0
Twists 0,0,1,0/0,0,1,1 0,1,0,0/0,0,1,0 0,1,0,0/0,0,1,1
Cuts CUT-A
Axis 0,0,1,0
Twists 1,0,0,0/1,1,0,0 0,0,0,1/1,0,0,0 0,0,0,1/1,1,0,0
Cuts CUT-B
```
### Case a×b×b×b
General code: 
```
Puzzle NAME_AXBXBXB
Dim 4
NAxis 2
Faces 1,0,0,0 0,0,0,1
Group 1,0,0,0/1,1,0,0 1,0,0,0/1,0,1,0 1,0,0,0/0,0,0,1
Axis 1,0,0,0
Twists 0,1,0,0/0,1,1,0 0,1,0,0/0,0,0,1
Cuts CUT-B
Axis 0,0,0,1
Twists 1,0,0,0/1,1,0,0 1,0,0,0/1,0,1,0
Cuts CUT-A
```

### Case a×a×a×a
General code: 
```
Puzzle NAME_AXAXAXA
Dim 4
NAxis 1
Faces 1,0,0,0
Group 1,0,0,0/1,1,0,0 1,0,0,0/1,0,1,0 1,0,0,0/1,0,0,1
Axis 1,0,0,0
Twists 0,1,0,0/0,1,1,0 0,1,-1,0/0,0,0,1 0,2,-1,-1/0,1,1,-2
Cuts CUT-A
```


## 5D+ Hypercuboids
This hypercuboids are not studied yet, except for some "simpler" versions with a lots of $1$- s.



## 5D+ Hypercuboids
This hypercuboids are not studied yet, except for some "simpler" versions with a lots of $1$- s.
