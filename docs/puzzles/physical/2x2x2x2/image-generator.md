# Physical 2x2x2x2 Image Generator

Generate an image of a physical 2x2x2x2 in a certain state. (input must use standard physical 2^4 notation and have an **even** number of #'s)


<label for="textinput">Input moves:</label>
<textarea id="textinput" name="textinput" rows="4" cols="50">
</textarea>



<button onclick="myFunction()" style="background-color: #e7e7e7; color: black; padding: 8px 8px; border-radius: 12px;" id="buttin">Generate Image</button>

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
    return input
}

function D2(input)
{
    input[0] = turn(input[0],3);
    input[1] = turn(input[1],3);
    input = U2(input);
    input[0] = turn(input[0],3);
    input[1] = turn(input[1],3);
    return input
}

function F2(input)
{
    input[0] = turn(input[0],7);
    input[1] = turn(input[1],7);
    input = U2(input);
    input[0] = turn(input[0],11);
    input[1] = turn(input[1],11);
    return input
}

// end slab twist functions


function turn(input,turnNum)
// input = L or R
// turn num is just what turn it does

{
    if(turnNum == 0)
    {
        return y(input);
    }
    else if(turnNum == 1)
    {
        return y(y(y(input)));
    }
    else if(turnNum == 2)
    {
        return y(y(input));
    }
    else if(turnNum == 3)
    {
        return x(x(input));
    }
    else if(turnNum == 4)
    {
        return z(z(input));
    }
    else if(turnNum == 5)
    {
        return y(x(x(input)));
    }
    else if(turnNum == 6)
    {
        return y(y(y(x(x(input)))));
    }
    else if(turnNum == 7)
    {
        return x(input);
    }
    else if(turnNum == 8)
    {
        return y(x(input));
    }
    else if(turnNum == 9)
    {
        return y(y(y(x(input))));
    }
    else if(turnNum == 10)
    {
        return y(y(x(input)));
    }
    else if(turnNum == 11)
    {
        return x(x(x(input)));
    }
    else if(turnNum == 12)
    {
        return y(x(x(x(input))));
    }
    else if(turnNum == 13)
    {
        return y(y(y(x(x(x(input))))));
    }
    else if(turnNum == 14)
    {
        return y(y(x(x(x(input)))));
    }
    else if(turnNum == 15)
    {
        return z(input);
    }
    else if(turnNum == 16)
    {
        return y(z(input));
    }
    else if(turnNum == 17)
    {
        return y(y(y(z(input))));
    }
    else if(turnNum == 18)
    {
        return y(y(z(input)));
    }
    else if(turnNum == 19)
    {
        return z(z(z(input)));
    }
    else if(turnNum == 20)
    {
        return y(z(z(z(input))));
    }
    else if(turnNum == 21)
    {
        return y(y(y(z(z(z(input))))));
    }
    else if(turnNum == 22)
    {
        return y(y(z(z(z(input)))));
    }
    else
    {
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



function myFunction() {
    var slabmoves = ["U2", "F2", "B2", "D2"]
    var IOmoves = ["Ix", "Ix'", "Ix2", "Ox", "Ox'", "Ox2"]
    var Lphysmoves = ["Ly", "Ly'", "Ly2", "Lx2", "Lz2", "Lx2,y", "Lx2,y'", "Lx", "Lx,y", "Lx,y'", "Lx,y2", "Lx'", "Lx',y", "Lx',y'", "Lx',y2", "Lz", "Lz,y", "Lz,y'", "Lz,y2", "Lz'", "Lz',y", "Lz',y'", "Lz',y2", ""];
    var Rphysmoves = ["Ry", "Ry'", "Ry2", "Rx2", "Rz2", "Rx2,y", "Rx2,y'", "Rx", "Rx,y", "Rx,y'", "Rx,y2", "Rx'", "Rx',y", "Rx',y'", "Rx',y2", "Rz", "Rz,y", "Rz,y'", "Rz,y2", "Rz'", "Rz',y", "Rz',y'", "Rz',y2", ""];
    canvas.height = 150;

    var puzzleState = [[[0,7,2,5],[0,7,2,4],[0,7,3,4],[0,7,3,5],[0,6,2,5],[0,6,2,4],[0,6,3,4],[0,6,3,5]],[[1,7,2,4],[1,7,2,5],[1,7,3,5],[1,7,3,4],[1,6,2,4],[1,6,2,5],[1,6,3,5],[1,6,3,4]]];
    // set puzzle to the solved state

    var userinput = document.getElementById("textinput").value;
    // getting what the user typed from the text box
    var movestodo = userinput.split(" ");
    console.log(movestodo);
    // everything the user typed split into an array by spaces
    
    if (slabmoves.includes(movestodo[0])) {
        slabTurns(puzzleState, slabmoves.indexOf(movestodo[0]));
    } else if (Lphysmoves.includes(movestodo[0])) {
        turn(puzzleState[0], Lphysmoves.indexOf(movestodo[0]));
    } else if (Rphysmoves.includes(movestodo[0])) {
        turn(puzzleState[1], Rphysmoves.indexOf(movestodo[0]));
    } else {
        puzzleState = [[[8,8,8,8],[8,8,8,8],[8,8,8,8],[8,8,8,8],[8,8,8,8],[8,8,8,8],[8,8,8,8],[8,8,8,8]],[[8,8,8,8],[8,8,8,8],[8,8,8,8],[8,8,8,8],[8,8,8,8],[8,8,8,8],[8,8,8,8],[8,8,8,8]]];
        // TURNS THE WHOLE PUZZLE RED IF USER TYPED SOMETHING OTHER THAN A MOVE
        //var element = document.getElementById("buttin");
        //element.value = "ERROR: BAD SYNTAX";
    }
    console.log(movestodo);

    // for (var i = 0; i < movestodo.length; ++j) 
    // {
    // }


    
    //puzzleState[0] = turn(puzzleState[0],2);
    //puzzleState = F2(puzzleState);

    cube(0,10,puzzleState);

}
</script>