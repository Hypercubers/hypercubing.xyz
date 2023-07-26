# Physical 2x2x2x2 Image Generator

Generate an image of a physical 2x2x2x2 by inputting moves using [canonical moves notation](/puzzles/physical/2x2x2x2/canonical-moves).


**Moves that the generator will accept:**

`zy`  `yz`  `xz`  `zx`  `yx`  `xy`  `yw`  `wy`  `xw`  `wx`  `zw`  `wz` `Ly`  `Ly'`  `Ly2`  `Lx2`  `Lz2`  `Lx2,y`  `Lx2,y'` `Lx` `Lx,y` `Lx,y'` `Lx,y2` `Lx'` `Lx',y` `Lx',y'` `Lx',y2` `Lz` `Lz,y` `Lz,y'` `Lz,y2` `Lz'` `Lz',y` `Lz',y'` `Lz',y2` `Ry` `Ry'` `Ry2` `Rx2` `Rz2` `Rx2,y` `Rx2,y'` `Rx` `Rx,y` `Rx,y'` `Rx,y2` `Rx'` `Rx',y` `Rx',y'` `Rx',y2` `Rz` `Rz,y` `Rz,y'` `Rz,y2` `Rz'` `Rz',y` `Rz',y'` `Rz',y2` `Ix` `Ix'` `Ix2` `Ox` `Ox'` `Ox2` `U2` `F2` `B2` `D2`


<label for="textinput">Input moves: (separated by spaces)</label>
<textarea id="textinput" name="textinput" rows="4" cols="50">
</textarea>



<button onclick="myFunction()" style="background-color: #e7e7e7; color: black; padding: 8px 8px; border-radius: 12px;" id="buttin">Generate Image</button>

<p id="errormsg" markdown="block"></p>

<p id="demo"></p>
<img id="imgShow" hidden="hidden" src="#">
<canvas id="myCanvas"  width="350" height="125" style="border:0px solid #000000;">
</canvas>



<script>

var colors = ["orange","red","blue","green","purple","pink","yellow","white","gray"];
const canvas = document.getElementById('myCanvas');
const ctx = canvas.getContext('2d');


function triangle(x,y,height,width,color)
{
    ctx.beginPath();
    ctx.moveTo(x, y);
    ctx.lineTo(x + width, y);
    ctx.lineTo(x, y + height);
    ctx.fillStyle = colors[color];
    ctx.closePath();
    ctx.fill();
    ctx.stroke();
}
function triangleShift(x,y,xShift,yShift,xFactor,yFactor,height,width,color)
{
    ctx.beginPath();
    ctx.moveTo(x, y);
    ctx.lineTo(x + width * xFactor, y + (yShift / 2) * yFactor);
    ctx.lineTo(x + (xShift / 2) * xFactor, y + height * yFactor);
    ctx.fillStyle = colors[color];
    ctx.closePath();
    ctx.fill();
    ctx.stroke();
}
function face(x,y,c1,c2,c3,c4,c5,c6,c7,c8)
{
    triangle(x+25,y+25,-25,-25, c1);
    triangle(x+25,y+25,-25,25,  c2);
    triangle(x+25,y+25,25,-25,  c3);
    triangle(x+25,y+25,25,25,   c4);
    triangle(x,y,25,25,         c5);
    triangle(x+50,y,25,-25,     c6);
    triangle(x+50,y+50,-25,-25, c7);
    triangle(x,y+50,-25,25,     c8);
}
function faceShift(x,y,xShift,yShift,xFactor,yFactor,c1,c2,c3,c4,c5,c6,c7,c8)
{
    triangleShift(x+(25+xShift/2)*xFactor,y+(25+yShift/2)*yFactor,-xShift,-yShift,xFactor,yFactor,-25,-25, c1);
    triangleShift(x+(25+xShift/2)*xFactor,y+(25+yShift/2)*yFactor,-xShift,yShift,xFactor,yFactor,-25,25,   c2);
    triangleShift(x+(25+xShift/2)*xFactor,y+(25+yShift/2)*yFactor,xShift,-yShift,xFactor,yFactor,25,-25,   c3);
    triangleShift(x+(25+xShift/2)*xFactor,y+(25+yShift/2)*yFactor,xShift,yShift,xFactor,yFactor,25,25,     c4);
    triangleShift(x,y,xShift,yShift,xFactor,yFactor,25,25,                                                 c5);
    triangleShift(x+(50)*xFactor,y+(yShift)*yFactor,xShift,-yShift,xFactor,yFactor,25,-25,                 c6);
    triangleShift(x+(50+xShift)*xFactor,y+(50+yShift)*yFactor,-xShift,-yShift,xFactor,yFactor,-25,-25,     c7);
    triangleShift(x+(xShift)*xFactor,y+(50)*yFactor,-xShift,yShift,xFactor,yFactor,-25,25,                 c8);
}
function cube(x,y,state)
{
    face(x,y+25,                      state[0][0][3],state[0][3][3],state[0][4][3],state[0][7][3],state[0][0][0],state[0][3][0],state[0][7][0],state[0][4][0]);
    face(x+50,y+25,                   state[0][3][2],state[0][2][2],state[0][7][2],state[0][6][2],state[0][3][0],state[0][2][0],state[0][6][0],state[0][7][0]);
    face(x+50,y+75,                   state[0][7][1],state[0][6][1],state[0][4][1],state[0][5][1],state[0][7][0],state[0][6][0],state[0][5][0],state[0][4][0]);
    face(x+125,y,                     state[0][1][2],state[0][0][2],state[0][5][2],state[0][4][2],state[0][1][0],state[0][0][0],state[0][4][0],state[0][5][0]);
    faceShift(x+75,y,-25,0,1,0.5,     state[0][0][1],state[0][1][1],state[0][3][1],state[0][2][1],state[0][0][0],state[0][1][0],state[0][2][0],state[0][3][0]);
    faceShift(x+100,y+25,0,-25,0.5,1, state[0][2][3],state[0][1][3],state[0][6][3],state[0][5][3],state[0][2][0],state[0][1][0],state[0][5][0],state[0][6][0]);

    face(x+175,y,                     state[1][1][2],state[1][0][2],state[1][5][2],state[1][4][2],state[1][1][0],state[1][0][0],state[1][4][0],state[1][5][0]);
    face(x+250,y+25,                  state[1][3][2],state[1][2][2],state[1][7][2],state[1][6][2],state[1][3][0],state[1][2][0],state[1][6][0],state[1][7][0]);
    face(x+250,y+75,                  state[1][7][1],state[1][6][1],state[1][4][1],state[1][5][1],state[1][7][0],state[1][6][0],state[1][5][0],state[1][4][0]);
    face(x+300,y+25,                  state[1][2][3],state[1][1][3],state[1][6][3],state[1][5][3],state[1][2][0],state[1][1][0],state[1][5][0],state[1][6][0]);
    faceShift(x+225,y,0,25,0.5,1,     state[1][0][3],state[1][3][3],state[1][4][3],state[1][7][3],state[1][0][0],state[1][3][0],state[1][7][0],state[1][4][0]);
    faceShift(x+225,y,25,0,1,0.5,     state[1][0][1],state[1][1][1],state[1][3][1],state[1][2][1],state[1][0][0],state[1][1][0],state[1][2][0],state[1][3][0]);
}
//LR UD FB IO


function x(input)
{
    input = [input[3],input[2],input[6],input[7],input[0],input[1],input[5],input[4]];
    for(var i = 0; i < 8; i++)
    {
        [input[i][1],input[i][2]] = [input[i][2],input[i][1]]
    }
    return input;
}
function y(input)
{
    input = [input[3],input[0],input[1],input[2],input[7],input[4],input[5],input[6]];
    for(var i = 0; i < 8; i++)
    {
        [input[i][3],input[i][2]] = [input[i][2],input[i][3]]
    }
    return input;
}
function z(input)
{
    input = [input[4],input[0],input[3],input[7],input[5],input[1],input[2],input[6]];
    for(var i = 0; i < 8; i++)
    {
        [input[i][1],input[i][3]] = [input[i][3],input[i][1]]
    }
    return input;
}
function hashtag(input)
{
    input = [[input[1][2],input[1][3],input[1][0],input[1][1],input[0][4],input[0][5],input[0][6],input[0][7]],[input[0][2],input[0][3],input[0][0],input[0][1],input[1][4],input[1][5],input[1][6],input[1][7]]];
    input = [[input[0][1],input[1][0],input[1][3],input[0][2],input[0][5],input[1][4],input[1][7],input[0][6]],[input[1][1],input[0][0],input[0][3],input[1][2],input[1][5],input[0][4],input[0][7],input[1][6]]];
    for(var j = 0; j < 2; j++)
    {
        for(var i = 0; i < 8; i++)
        {
            [input[j][i][0],input[j][i][3],input[j][i][1],input[j][i][2]] = [input[j][i][3],input[j][i][0],input[j][i][2],input[j][i][1]]
        }
    }
    return input;
}
function hashtagInv(input)
{
    input = [[input[1][2],input[1][3],input[1][0],input[1][1],input[0][4],input[0][5],input[0][6],input[0][7]],[input[0][2],input[0][3],input[0][0],input[0][1],input[1][4],input[1][5],input[1][6],input[1][7]]];
    input = [[input[0][1],input[1][0],input[1][3],input[0][2],input[0][5],input[1][4],input[1][7],input[0][6]],[input[1][1],input[0][0],input[0][3],input[1][2],input[1][5],input[0][4],input[0][7],input[1][6]]];
    for(var j = 0; j < 2; j++)
    {
        for(var i = 0; i < 8; i++)
        {
            [input[j][i][3],input[j][i][0],input[j][i][2],input[j][i][1]] = [input[j][i][0],input[j][i][3],input[j][i][1],input[j][i][2]]
        }
    }
    return input;
}

// start slab twist functions

function U2(input)
{
    input = [[input[1][2],input[1][3],input[1][0],input[1][1],input[0][4],input[0][5],input[0][6],input[0][7]],[input[0][2],input[0][3],input[0][0],input[0][1],input[1][4],input[1][5],input[1][6],input[1][7]]];
    return input;
}

function D2(input)
{
    input[0] = turn(input[0],3);
    input[1] = turn(input[1],3);
    input = U2(input);
    input[0] = turn(input[0],3);
    input[1] = turn(input[1],3);
    return input;
}

function F2(input)
{
    input[0] = turn(input[0],7);
    input[1] = turn(input[1],7);
    input = U2(input);
    input[0] = turn(input[0],11);
    input[1] = turn(input[1],11);
    return input;
}

function B2(input)
{
    input[0] = turn(input[0],11);
    input[1] = turn(input[1],11);
    input = U2(input);
    input[0] = turn(input[0],7);
    input[1] = turn(input[1],7);
    return input;
}

// end slab twist functions



// start IO twist functions

function Ix(input) {
    // [LUBO LUBI LUFI LUFO LDBO LDBI LDFI LDFO], [RUBI RUBO RUFO RUFI RDBI RDBO RDFI RDFO]
    // "orange","red","blue","green","purple","pink","yellow","white","gray"
    var temp = input[0][1]; // save LUBI
    input[0][1] = input[0][2]; // LUBI = LUFI
    input[0][2] = input[0][6]; // LUFI = LDFI
    input[0][6] = input[0][5]; // LDFI = LDBI
    input[0][5] = temp; // LDBI = LUBI
    // reorienting those pieces
    [input[0][1][1], input[0][1][2]] = [input[0][1][2], input[0][1][1]];
    [input[0][2][1], input[0][2][2]] = [input[0][2][2], input[0][2][1]];
    [input[0][5][1], input[0][5][2]] = [input[0][5][2], input[0][5][1]];
    [input[0][6][1], input[0][6][2]] = [input[0][6][2], input[0][6][1]];
    // now for the RI pieces:
    var temp = input[1][0]; // save RUBI
    input[1][0] = input[1][3]; // RUBI = RUFI
    input[1][3] = input[1][7]; // RUFI = RDFI
    input[1][7] = input[1][4]; // RDFI = RDBI
    input[1][4] = temp; // RDBI = RUBI
    // reorienting those pieces
    [input[1][0][1], input[1][0][2]] = [input[1][0][2], input[1][0][1]];
    [input[1][3][1], input[1][3][2]] = [input[1][3][2], input[1][3][1]];
    [input[1][7][1], input[1][7][2]] = [input[1][7][2], input[1][7][1]];
    [input[1][4][1], input[1][4][2]] = [input[1][4][2], input[1][4][1]];
    
    return input;
}


// end IO twist functions


function turn(input,turnNum)
// input = just L or R
// turn num is just what turn it does
{
    if(turnNum == 0){
        return y(input);
    }
    else if(turnNum == 1){
        return y(y(y(input)));
    }
    else if(turnNum == 2){
        return y(y(input));
    }
    else if(turnNum == 3) {
        return x(x(input));
    }
    else if(turnNum == 4) {
        return z(z(input));
    }
    else if(turnNum == 5) {
        return y(x(x(input)));
    }
    else if(turnNum == 6) {
        return y(y(y(x(x(input)))));
    }
    else if(turnNum == 7){
        return x(input);
    }
    else if(turnNum == 8) {
        return y(x(input));
    }
    else if(turnNum == 9) {
        return y(y(y(x(input))));
    }
    else if(turnNum == 10) {
        return y(y(x(input)));
    }
    else if(turnNum == 11){
        return x(x(x(input)));
    }
    else if(turnNum == 12){
        return y(x(x(x(input))));
    }
    else if(turnNum == 13){
        return y(y(y(x(x(x(input))))));
    }
    else if(turnNum == 14){
        return y(y(x(x(x(input)))));
    }
    else if(turnNum == 15){
        return z(input);
    }
    else if(turnNum == 16){
        return y(z(input));
    }
    else if(turnNum == 17){
        return y(y(y(z(input))));
    }
    else if(turnNum == 18){
        return y(y(z(input)));
    }
    else if(turnNum == 19){
        return z(z(z(input)));
    }
    else if(turnNum == 20){
        return y(z(z(z(input))));
    }
    else if(turnNum == 21){
        return y(y(y(z(z(z(input))))));
    }
    else if(turnNum == 22){
        return y(y(z(z(z(input)))));
    }
    else{
        return input;
    }
}

function slabTurns(input, turnNum) {
    if (turnNum == 0) {
        return U2(input);
    } else if (turnNum == 1) {
        return F2(input);
    } else if (turnNum == 2) {
        return B2(input);
    } else if (turnNum == 3) {
        return D2(input);
    }
}

function IOTurns(input, turnNum) {
    if (turnNum == 0) {
        return Ix(input);
    } else if (turnNum == 1) {
        return Ix(Ix(Ix(input)));
    }
    else if (turnNum == 2) {
        return Ix(Ix(input));
    } else if (turnNum == 3) {
        input = rotatings(input, 10);
        input = rotatings(input, 10);
        input = (Ix(Ix(Ix(input))));
        input = rotatings(input, 10);
        input = rotatings(input, 10);
        return input;
    } else if (turnNum == 4) {
        input = rotatings(input, 10);
        input = rotatings(input, 10);
        input = (Ix(input));
        input = rotatings(input, 10);
        input = rotatings(input, 10);
        return input;
    } else if (turnNum == 5) {
        input = rotatings(input, 10);
        input = rotatings(input, 10);
        input = (Ix(Ix(input)));
        input = rotatings(input, 10);
        input = rotatings(input, 10);
        return input;
    }
    // rotatings(input, 10)
}

function rotatings(input, turnNum) {
    if (turnNum == 0) {
        // zy rotation
        input[0] = turn(input[0],7);
        input[1] = turn(input[1],7);
        return input;
    } else if (turnNum == 1) {
        // yz rotation
        input[0] = turn(input[0],11);
        input[1] = turn(input[1],11);
        return input;
    } else if (turnNum == 2) {
        // xz gyro
        input = rotatings(input, 0);
        input = rotatings(input, 5);
        input = rotatings(input, 1);
        return input;
    } else if (turnNum == 3) {
        // zx gyro
        input = rotatings(input, 2);
        input = rotatings(input, 2);
        input = rotatings(input, 2);
        return input;
    } else if (turnNum == 4) {
        // yx gyro
        input = rotatings(input, 5);
        input = rotatings(input, 5);
        input = rotatings(input, 5);
        return input;
    } else if (turnNum == 5) {
        // xy gyro
        // # wz # Rx2 F2 D2 Rz2
        input = hashtag(input);
        input = rotatings(input, 11);
        input = hashtag(input);
        input[1] = turn(input[1], 3);
        input = F2(input);
        input = D2(input);
        input[1] = turn(input[1], 4);
        return input;
    } else if (turnNum == 6) {
        // yw rotation
        input[0] = turn(input[0],19);
        input[1] = turn(input[1],15);
        return input;
    } else if (turnNum == 7) {
        // wy rotation
        input[0] = turn(input[0],15);
        input[1] = turn(input[1],19);
        return input;
    } else if (turnNum == 8) {
        // xw gyro
        input = rotatings(input, 9);
        input = rotatings(input, 9);
        input = rotatings(input, 9);
        return input;
    } else if (turnNum == 9) {
        // wx gyro
        // wy yx yw
        input = rotatings(input, 7);
        input = rotatings(input, 4);
        input = rotatings(input, 6);
        return input;
    } else if (turnNum == 10) {
        // zw rotation
        input[0] = turn(input[0],0);
        input[1] = turn(input[1],1);
        return input;
    } else if (turnNum == 11) {
        // wz rotation
        input[0] = turn(input[0],1);
        input[1] = turn(input[1],0);
        return input;
    }
}



function myFunction() {
    var rotations = ["zy", "yz", "xz", "zx", "yx", "xy", "yw", "wy", "xw", "wx", "zw", "wz"];
    var slabmoves = ["U2", "F2", "B2", "D2"];
    var IOmoves = ["Ix", "Ix'", "Ix2", "Ox", "Ox'", "Ox2"];
    var Lphysmoves = ["Ly", "Ly'", "Ly2", "Lx2", "Lz2", "Lx2,y", "Lx2,y'", "Lx", "Lx,y", "Lx,y'", "Lx,y2", "Lx'", "Lx',y", "Lx',y'", "Lx',y2", "Lz", "Lz,y", "Lz,y'", "Lz,y2", "Lz'", "Lz',y", "Lz',y'", "Lz',y2", ""];
    var Rphysmoves = ["Ry", "Ry'", "Ry2", "Rx2", "Rz2", "Rx2,y", "Rx2,y'", "Rx", "Rx,y", "Rx,y'", "Rx,y2", "Rx'", "Rx',y", "Rx',y'", "Rx',y2", "Rz", "Rz,y", "Rz,y'", "Rz,y2", "Rz'", "Rz',y", "Rz',y'", "Rz',y2", ""];
    canvas.height = 150;

    var puzzleState = [[[0,7,2,5],[0,7,2,4],[0,7,3,4],[0,7,3,5],[0,6,2,5],[0,6,2,4],[0,6,3,4],[0,6,3,5]],[[1,7,2,4],[1,7,2,5],[1,7,3,5],[1,7,3,4],[1,6,2,4],[1,6,2,5],[1,6,3,5],[1,6,3,4]]];
    // "orange","red","blue","green","purple","pink","yellow","white","gray"
    // set puzzle to the solved state
    // [LUBO LUBI LUFI LUFO LDBO LDBI LDFI LDFO], [RUBI RUBO RUFO RUFI RDBI RDBO RDFI RDFO]

    var userinput = document.getElementById("textinput").value;
    // getting what the user typed from the text box
    var movestodo = userinput.split(" ");
    console.log(movestodo);
    // everything the user typed split into an array by spaces
    
    // counting hashes
    var numHashes = 0;
    for (var i = 0; i < movestodo.length; ++i) {
        if (movestodo[i] == "#") {
            numHashes++;
        }
    }
    document.getElementById("errormsg").innerHTML = "";
    for (var i = 0; i < movestodo.length; ++i) {
        //for each item in the list of moves to do:
        if (numHashes > 0 && numHashes %2 == 1) {
            // if the number of # is odd, set color to gray and break
            puzzleState = [[[8,8,8,8],[8,8,8,8],[8,8,8,8],[8,8,8,8],[8,8,8,8],[8,8,8,8],[8,8,8,8],[8,8,8,8]],[[8,8,8,8],[8,8,8,8],[8,8,8,8],[8,8,8,8],[8,8,8,8],[8,8,8,8],[8,8,8,8],[8,8,8,8]]];
            var message_text = "⚠️ <b>Warning:</b> There must be an <i>even</i> number of # in the input";
            document.getElementById("errormsg").innerHTML = message_text;
            break;
        }
        if (slabmoves.includes(movestodo[i])) {
            puzzleState = slabTurns(puzzleState, slabmoves.indexOf(movestodo[i]));
        } else if (movestodo[i] == "#") {
            puzzleState = hashtag(puzzleState);
        } else if (Lphysmoves.includes(movestodo[i])) {
            puzzleState[0] = turn(puzzleState[0], Lphysmoves.indexOf(movestodo[i]));
        } else if (Rphysmoves.includes(movestodo[i])) {
            puzzleState[1] = turn(puzzleState[1], Rphysmoves.indexOf(movestodo[i]));
        } else if (IOmoves.includes(movestodo[i])) {
            puzzleState = IOTurns(puzzleState, IOmoves.indexOf(movestodo[i]));
        } else if (rotations.includes(movestodo[i])) {
            puzzleState = rotatings(puzzleState, rotations.indexOf(movestodo[i]));
        } else {
            puzzleState = [[[8,8,8,8],[8,8,8,8],[8,8,8,8],[8,8,8,8],[8,8,8,8],[8,8,8,8],[8,8,8,8],[8,8,8,8]],[[8,8,8,8],[8,8,8,8],[8,8,8,8],[8,8,8,8],[8,8,8,8],[8,8,8,8],[8,8,8,8],[8,8,8,8]]];
            var message_text = "⚠️ <b>Warning:</b> Unknown input detected. Check canonical moves carefully";
            document.getElementById("errormsg").innerHTML = message_text;
        }
    }


    
   

    cube(0,10,puzzleState);

}
</script>