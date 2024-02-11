# How does it work?

There are a few ways to project a 5-cell into 3d space. In a vertex-first projection the "hidden" cell is on the "outside" of the others while in a cell-first projection it is on the "inside". My design for the 4D pyraminx represents the latter way. In a solved state we have 4 colors on the outside and one on the inside of the puzzle.

![Projections](https://jimdo-storage.freetls.fastly.net/image/439495539/fccef95a-09fd-41a9-8931-2d565339e4d9.png?quality=80,90&auto=webp&disable=upscale&width=724&height=760) ![VertexFirst](https://jimdo-storage.freetls.fastly.net/image/439487284/cc59ec54-4aad-48a6-8606-47d50d1698d9.png?quality=80,90&auto=webp&disable=upscale&width=298&height=296) ![CellFirst](https://jimdo-storage.freetls.fastly.net/image/439487283/9f17e459-bf93-4e28-9652-73571216bbf3.png?quality=80,90&auto=webp&disable=upscale&width=299&height=293)

(pictures: projections [Source](https://www.researchgate.net/figure/2D-visualizations-of-3D-perspective-projections-of-the-first-iteration-of-a_fig1_280734511), vertex first pyraminx, cell first pyraminx [Source](https://rayzz.me/articles/hypercubing/4-simplex-solution.html)

## The Pieces


There are ten tetrahedron-shaped 3-colored edge pieces where the fourth face is split into three colors.

![EdgePiece](https://jimdo-storage.freetls.fastly.net/image/439487591/e93c90c6-7bd4-4da3-8ac2-19fdeab9a6b7.jpg?format=pjpg&quality=80,90&auto=webp&disable=upscale&width=1920&height=1798)

Then there are five octahedron-shaped 4-colored center pieces where four of the faces are split into three colors of the adjacent faces.

![CenterPiece](https://jimdo-storage.freetls.fastly.net/image/439487837/890e1dcf-5c7f-48d0-9b55-fd24ea6537ae.jpg?format=pjpg&quality=80,90&auto=webp&disable=upscale&width=1920&height=1727)

The five 4-colored trivial tips can also be represented by tetrahedrons but with the current design they would need to be a separate arrangement. So this puzzle without the trivial tips represents just the truncated pyramnix.

![TrivialTips](https://jimdo-storage.freetls.fastly.net/image/439487834/7efb5dd9-ad7c-4c0e-a86e-c3fd4c8b2736.gif?quality=80,90&auto=webp&disable=upscale&width=600&height=600)

## Chirality


For the pieces to fit together in the correct color arrangement they need to have the same chirality. There is a left-handed and a right-handed version of the pieces and the centers and trivial tips need to have the same order of colors. Since the edges are allowed to be in more states the chirality doesn't matter as much but if the chiralities don't line up one color will be "favored" in a certain orientation.

## Moves:

There are some legal moves that don't represent a movement in the 4D puzzle.

### Edge Migration


You can move edges to a corresponding position on the "free center" and back.

![EdgeMigration](https://jimdo-storage.freetls.fastly.net/image/439487756/f8bc9fa5-c176-4a8b-a4ea-be84bca4fe4d.gif?quality=80,90&auto=webp&disable=upscale&width=600&height=600) ![EdgeMigrationBack](https://jimdo-storage.freetls.fastly.net/image/439487601/9b2205b4-cb11-4df4-9c71-d868eb66d64c.gif?quality=80,90&auto=webp&disable=upscale&width=600&height=600)

### Reorient Edges


Edges can be in two states in relation to a center. They can align with the split face towards the center which will be call a "correct" state or the split face can be away from the center which will be called an "incorrect" state. In the latter case the edge can legally be oriented in three different ways.

![IncorrectEdge](https://jimdo-storage.freetls.fastly.net/image/439487919/56e87c49-83ed-418b-bc1c-e838c6c8cc75.jpg?format=pjpg&quality=80,90&auto=webp&disable=upscale&width=1920&height=1440) ![CorrectEdge](https://jimdo-storage.freetls.fastly.net/image/439487936/ade54d9b-17c9-4a06-a3e1-1fcabc888049.jpg?format=pjpg&quality=80,90&auto=webp&disable=upscale&width=1920&height=1440)

![OrientEdge](https://jimdo-storage.freetls.fastly.net/image/439487791/12b61e85-0346-4b91-ab6f-fab90d28475d.gif?quality=80,90&auto=webp&disable=upscale&width=600&height=600)

Next we have moves which do represent a movement in the 4D puzzle. Unlike the normal 3D pyraminx the tips can't legally be twisted. Other than that the four different moves of turning two layers of the pyraminx is legal. In the 4D version of the puzzle we have 20 different of such slice moves. Here are the four axes of rotations that are allowed for each 2-layered pyramid.

![Move1](https://jimdo-storage.freetls.fastly.net/image/439487489/bdb767ed-56fb-4179-b334-742a2f42011d.gif?quality=80,90&auto=webp&disable=upscale&width=600&height=600) ![Move2](https://jimdo-storage.freetls.fastly.net/image/439487533/176cf069-4d39-48e4-95be-1c837baeed90.gif?quality=80,90&auto=webp&disable=upscale&width=600&height=600) ![Move3](https://jimdo-storage.freetls.fastly.net/image/439487488/f29cc53a-fd63-425c-b417-16d63801ff0e.gif?quality=80,90&auto=webp&disable=upscale&width=600&height=600) ![Move4](https://jimdo-storage.freetls.fastly.net/image/439487466/76ad51a9-6717-4e12-940d-e720b77a5aa1.gif?quality=80,90&auto=webp&disable=upscale&width=600&height=600)

If you perform such a move on each of the four sides of the tetrahedron you get a total of 16 moves. For the missing four moves we can "equip" the free octahedron with the edges by swapping them onto it and perform the rest of the rotations that way.

![Equip](https://jimdo-storage.freetls.fastly.net/image/439487932/ca9fe796-91e8-4c8a-a2a2-91818f3edae0.gif?quality=80,90&auto=webp&disable=upscale&width=600&height=600) 

![Move5](https://jimdo-storage.freetls.fastly.net/image/439487356/e60dd499-b91b-4121-914c-f28abc0b2997.gif?quality=80,90&auto=webp&disable=upscale&width=600&height=600) ![Move6](https://jimdo-storage.freetls.fastly.net/image/439487699/daf50c3d-f579-4720-9416-5f490b891396.gif?quality=80,90&auto=webp&disable=upscale&width=600&height=600) ![Move7](https://jimdo-storage.freetls.fastly.net/image/439487390/0c1d8a31-b258-47cc-b60a-2992959e54f6.gif?quality=80,90&auto=webp&disable=upscale&width=600&height=600) ![Move8](https://jimdo-storage.freetls.fastly.net/image/439487496/fa790eab-d3c3-415e-ad81-ff761e4a93b3.gif?quality=80,90&auto=webp&disable=upscale&width=600&height=600) 

After the rotation you have can move the edges back.

![Unequip](https://jimdo-storage.freetls.fastly.net/image/439487754/1415fecf-34b2-449d-a786-c5df77e9318c.gif?quality=80,90&auto=webp&disable=upscale&width=600&height=600)
...

This is not necessary for a solve, though, since you have access to all the edge pieces through the 16 other moves.

## Legal States


To keep the puzzle in a legal state sometimes after certain rotations we need to make edge reorientations. When performing a non-standard slice move an edge that isn't in a correct state regarding the center that has rotated can after a turn show a split face.

![UnorientedEdge](https://jimdo-storage.freetls.fastly.net/image/439487835/288d1a59-da63-49f9-ab3b-159e47f3afcd.jpg?format=pjpg&quality=80,90&auto=webp&disable=upscale&width=1842&height=1920)

If it isn't in a tip position it needs to be reoriented for otherwise the puzzle can get into an illegal or impossible state and also the color alignment becomes unknown for practical purposes when the puzzle is scrambled.

How does this work? Before the rotation the colors A and B are on the outside.

![EdgeCorrect](https://jimdo-storage.freetls.fastly.net/image/439487798/33cfe483-fac4-44d1-a1ed-ba179f796d25.jpg?format=pjpg&quality=80,90&auto=webp&disable=upscale&width=1792&height=2560)

After a non-standard rotation either A or B will be on the inside and then there are two possible cases. Firstly, if the edge is "correct" then the split face will remain touching the rotated center and the full face with color C will show on the outside.

![EdgeCorrectAfterRotation](https://jimdo-storage.freetls.fastly.net/image/439487793/cc380643-2ec0-49c7-be01-9f5fe5fda2a9.jpg?format=pjpg&quality=80,90&auto=webp&disable=upscale&width=1796&height=2560)

The other case is when the edge is "incorrect". Here the split face will be on the outside and the full color C will be touching the center.

![EdgeIncorrect](https://jimdo-storage.freetls.fastly.net/image/439487934/9cfaee9f-9013-4d92-9963-1ff0b1e8597f.jpg?format=pjpg&quality=80,90&auto=webp&disable=upscale&width=1920&height=2560) ![EdgeIncorrectAfterRotation](https://jimdo-storage.freetls.fastly.net/image/439487832/12715858-a560-4945-a7f1-638757b2c3db.jpg?format=pjpg&quality=80,90&auto=webp&disable=upscale&width=1792&height=2560)

As a rule you can now rotate the edge in the "down" direction in regards to the the rotation (where the center would be in the "up" direction) as shown here.

![EdgeRorientation](https://jimdo-storage.freetls.fastly.net/image/439487465/0642de7c-3955-4598-a45e-9772b80318c6.gif?quality=80,90&auto=webp&disable=upscale&width=600&height=600) ![UpDown](https://jimdo-storage.freetls.fastly.net/image/439487320/f9bf0657-d83d-4a43-8312-ac7c9f9c7118.jpg?format=pjpg&quality=80,90&auto=webp&disable=upscale&width=300&height=300)

This way we can simulate a 3-cycle of the faces A, B and C with the 4-sided shape of the tetrahedron.

## Gyro


While it isn't necessary for a solve it is possible to reorient the whole puzzle by what's usually called a gyro. There might be better ways to do it but here is one way that can be done in four steps.

### Step 1


First you have to align the free octahedron with one of the “outer” edges. Regarding the colors it’s best to look at the colors of the adjacent octahedron. In this step you have two cases. Either the edge is already correct the you don’t have to do anything or the edge is incorrect then you have to reorient it towards the free octahedron.

![Align](https://jimdo-storage.freetls.fastly.net/image/439487931/614a6656-f464-4bdf-acc3-4c2b1d0be979.jpg?format=pjpg&quality=80,90&auto=webp&disable=upscale&width=1920&height=2560) ![OrientTipEdge](https://jimdo-storage.freetls.fastly.net/image/439487939/4d757d4c-5196-47e9-be52-efbe2cd6aef1.gif?quality=80,90&auto=webp&disable=upscale&width=600&height=600)

### Step 2


Now you have to separate one 2-layered pyramid next to the aligned free octahedron. Here you have to watch out for the three edges facing you. In case they are “incorrect” you have to reorient them towards you. Then you can move it together towards the free octahedron.

![Separate](https://jimdo-storage.freetls.fastly.net/image/439487391/5fe4d03c-4562-4b66-a030-1c8031f23e53.gif?quality=80,90&auto=webp&disable=upscale&width=600&height=600) ![Orient1](https://jimdo-storage.freetls.fastly.net/image/439487495/6c75741c-6e75-4f21-9dd0-d737c4b2088d.gif?quality=80,90&auto=webp&disable=upscale&width=600&height=600) ![MoveTogether](https://jimdo-storage.freetls.fastly.net/image/439487395/410ce111-99fc-4b7d-ba4b-639fa721856b.gif?quality=80,90&auto=webp&disable=upscale&width=600&height=600)

### Step 3


Here you have to look at what’s left of the “upper pyramid”. The topmost piece and the “inner” piece have to be reoriented in case they are incorrect. This time the direction you have to reorient them towards is “down”, which means it’s just like you would do in a normal slice move. One handy thing is that for the “inner” piece you simply have to look on the inside by only taking these three pieces off and if you see a whole face you can just leave the piece there. If the face is 3 colored you can just take it and rotate it together with the other pieces and it will be correct.

![HighlightedPieces](https://jimdo-storage.freetls.fastly.net/image/439487855/131a93f1-e3ce-4acf-b277-d2b8ccb12460.jpg?format=pjpg&quality=80,90&auto=webp&disable=upscale&width=1920&height=2560) ![Orient2](https://jimdo-storage.freetls.fastly.net/image/439487590/9974f2a3-cad6-4594-989c-6161f3542a9c.gif?quality=80,90&auto=webp&disable=upscale&width=600&height=600) ![Flip1](https://jimdo-storage.freetls.fastly.net/image/439487538/ed1e00ff-68dd-4788-9f10-2ddfd0545338.gif?quality=80,90&auto=webp&disable=upscale&width=600&height=600) ![Flip2](https://jimdo-storage.freetls.fastly.net/image/439487663/e804072d-9e9b-4aa4-8930-153612503a36.gif?quality=80,90&auto=webp&disable=upscale&width=600&height=600)

### Step 4


The last step only involves the last edge. Again, if it’s incorrect you first have to reorient it, this time towards the “down” direction. And then you take the piece and move it “over the Pyraminx”, like this, and simply put it in the right spot.

![Orient3](https://jimdo-storage.freetls.fastly.net/image/439487467/59b37b48-53de-4fd6-b98f-a82d5610a8f6.gif?quality=80,90&auto=webp&disable=upscale&width=600&height=600) ![MoveOver](https://jimdo-storage.freetls.fastly.net/image/439487396/07314289-6169-47cd-a7d4-212bc5c35c54.gif?quality=80,90&auto=webp&disable=upscale&width=600&height=600)

That’s all there is to the gyro and here we have all in one movement.

![Gyro](https://jimdo-storage.freetls.fastly.net/image/439487856/af455204-87d9-40cd-80d5-515cd86fda4e.gif?quality=80,90&auto=webp&disable=upscale&width=600&height=600)

...


## Comparison of Moves with MC4D

| Dominik's Pyraminx | MagicCube 4D |
| ---------------------------- | ------------------------------------ |
| ![Move1](https://jimdo-storage.freetls.fastly.net/image/439487489/bdb767ed-56fb-4179-b334-742a2f42011d.gif?quality=80,90&auto=webp&disable=upscale&width=600&height=600) | ![MC4DMove1](https://jimdo-storage.freetls.fastly.net/image/439485424/c0d4447b-8cf3-42a6-a5a1-d649922cccfb.gif?quality=80,90&auto=webp&disable=upscale&width=239&height=288) |
| ![Move2](https://jimdo-storage.freetls.fastly.net/image/439487533/176cf069-4d39-48e4-95be-1c837baeed90.gif?quality=80,90&auto=webp&disable=upscale&width=600&height=600) | ![MC4DMove2](https://jimdo-storage.freetls.fastly.net/image/439485423/1f1df09d-612f-4982-ab2c-c9f491120a9d.gif?quality=80,90&auto=webp&disable=upscale&width=236&height=286) |
| ![Move3](https://jimdo-storage.freetls.fastly.net/image/439487488/f29cc53a-fd63-425c-b417-16d63801ff0e.gif?quality=80,90&auto=webp&disable=upscale&width=600&height=600) | ![MC4DMove3](https://jimdo-storage.freetls.fastly.net/image/439485422/24c5d3de-a539-4b5e-a956-0f32e4fc51ad.gif?quality=80,90&auto=webp&disable=upscale&width=236&height=285) |
| ![Move4](https://jimdo-storage.freetls.fastly.net/image/439487466/76ad51a9-6717-4e12-940d-e720b77a5aa1.gif?quality=80,90&auto=webp&disable=upscale&width=600&height=600) | ![MC4DMove4](https://jimdo-storage.freetls.fastly.net/image/439485421/ad43d862-dca1-4542-beee-34e35169c2ff.gif?quality=80,90&auto=webp&disable=upscale&width=236&height=286) |
| ![Move5](https://jimdo-storage.freetls.fastly.net/image/439487356/e60dd499-b91b-4121-914c-f28abc0b2997.gif?quality=80,90&auto=webp&disable=upscale&width=600&height=600)| ![MC4DMove5](https://jimdo-storage.freetls.fastly.net/image/439485428/074041b7-000b-48bf-90cb-6c876fa33919.gif?quality=80,90&auto=webp&disable=upscale&width=236&height=286) |
| ![Move6](https://jimdo-storage.freetls.fastly.net/image/439487699/daf50c3d-f579-4720-9416-5f490b891396.gif?quality=80,90&auto=webp&disable=upscale&width=600&height=600)| ![MC4DMove6](https://jimdo-storage.freetls.fastly.net/image/439485427/00971522-d025-4784-a99a-710a626c8144.gif?quality=80,90&auto=webp&disable=upscale&width=235&height=287) |
| ![Move7](https://jimdo-storage.freetls.fastly.net/image/439487390/0c1d8a31-b258-47cc-b60a-2992959e54f6.gif?quality=80,90&auto=webp&disable=upscale&width=600&height=600)| ![MC4DMove7](https://jimdo-storage.freetls.fastly.net/image/439485429/7ab5751e-85cf-4103-a3ed-7833d7b1b93b.gif?quality=80,90&auto=webp&disable=upscale&width=234&height=284) |
| ![Move8](https://jimdo-storage.freetls.fastly.net/image/439487496/fa790eab-d3c3-415e-ad81-ff761e4a93b3.gif?quality=80,90&auto=webp&disable=upscale&width=600&height=600) | ![MC4DMove8](https://jimdo-storage.freetls.fastly.net/image/439485426/c1fe2a21-b798-43e7-b52f-d1f344975bc2.gif?quality=80,90&auto=webp&disable=upscale&width=234&height=286) |
| ![Gyro](https://jimdo-storage.freetls.fastly.net/image/439487856/af455204-87d9-40cd-80d5-515cd86fda4e.gif?quality=80,90&auto=webp&disable=upscale&width=600&height=600) | ![MC4DGyro](https://jimdo-storage.freetls.fastly.net/image/439487319/d3521c35-3cb6-4172-82d8-983cc02857b1.gif?quality=80,90&auto=webp&disable=upscale&width=237&height=286) |


## Example solve


Here is a link to a video of an example scamble and solve of the puzzle: [Link](https://youtu.be/ouciU8p1Wto?si=wD7nbHjl6S_ivAWQ).

## Notes for a solve


The 4D pyraminx can end up with a single edge flipped incorrectly unlike the 3D pyraminx. This state can be solved with an algorithm that flips two edges, the right slice move and an additional two edges flip. But if a piece was moved in a wrong way accidentally it can also end up in a state that’s not solvable like this. The reason for this is that there are three states that flipping an edge moves between: (a) solved state, (b) one edge correct and the other two flipped and (c) all edges incorrect.

Going from (c) to (a) requires two flips so the method above can flip edge A from (b) to (a) or (c) but then edge B will go to state (b). In the following tree diagram it can be seen how all 2 flip moves only lead to looping between unsolved states:

![Tree](https://jimdo-storage.freetls.fastly.net/image/439487323/a5996e11-1851-4e8d-ab62-72680c36dc92.jpg?format=pjpg&quality=80,90&auto=webp&disable=upscale&width=900&height=600)
