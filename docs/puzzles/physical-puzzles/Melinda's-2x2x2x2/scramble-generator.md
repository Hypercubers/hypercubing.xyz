# Physical 2x2x2x2 Scramble Generator

<p>Scrambles: <span id="demo2">5</span></p>
<input type="range" min="1" max="20" value="5" class="slider" id="myRange">
<br>
<button onclick="myFunction()" style="background-color: #e7e7e7; color: black; padding: 8px 8px; border-radius: 12px;">Generate Scrambles</button>
!!! Scrambles
    <p id="demo"></p>
    <img id="imgShow" src="#">
<canvas id="myCanvas" hidden="hidden" width="350" height="125" style="border:1px solid #000000;">
</canvas>

<script>

var colors = ["orange","red","blue","green","purple","pink","yellow","white","gray"];
const canvas = document.getElementById('myCanvas');
const ctx = canvas.getContext('2d');

const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);

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

function getRandomInt(max) {
  return Math.floor(Math.random() * max);
}
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
function turn(input,turnNum)
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
function myFunction() {
    var scrambleLength = [16, 14, 12];
    var Lphysmoves = ["Ly", "Ly'", "Ly2", "Lx2", "Lz2", "Lx2,y", "Lx2,y'", "Lx", "Lx,y", "Lx,y'", "Lx,y2", "Lx'", "Lx',y", "Lx',y'", "Lx',y2", "Lz", "Lz,y", "Lz,y'", "Lz,y2", "Lz'", "Lz',y", "Lz',y'", "Lz',y2", ""];
    var Rphysmoves = ["Ry", "Ry'", "Ry2", "Rx2", "Rz2", "Rx2,y", "Rx2,y'", "Rx", "Rx,y", "Rx,y'", "Rx,y2", "Rx'", "Rx',y", "Rx',y'", "Rx',y2", "Rz", "Rz,y", "Rz,y'", "Rz,y2", "Rz'", "Rz',y", "Rz',y'", "Rz',y2", ""];
    var message_text = "";
    canvas.height = 150 * document.getElementById("myRange").value;
    for (var j = 0; j < document.getElementById("myRange").value; ++j) 
    {
        var puzzleState = [[[0,7,2,5],[0,7,2,4],[0,7,3,4],[0,7,3,5],[0,6,2,5],[0,6,2,4],[0,6,3,4],[0,6,3,5]],[[1,7,2,4],[1,7,2,5],[1,7,3,5],[1,7,3,4],[1,6,2,4],[1,6,2,5],[1,6,3,5],[1,6,3,4]]];
        var tempmsg =  "<br>" + (j+1) + ". ";
        if(j == 0)
        {
            tempmsg =  (j+1) + ". ";
        }
        var scrambleLen = scrambleLength[getRandomInt(3)];
        for (var i = 0; i < scrambleLen; ++i) {
            var Lrand = getRandomInt(24);
            puzzleState[0] = turn(puzzleState[0],Lrand);
            rand = Lphysmoves[Lrand];
            var Rrand = getRandomInt(24);
            puzzleState[1] = turn(puzzleState[1],Rrand);
            rand2 = Rphysmoves[Rrand];
            tempmsg += rand + " " + rand2 + " # ";
            puzzleState = hashtag(puzzleState)
        }
        message_text += tempmsg;
        cube(0,150 * j,puzzleState);
    }
    document.getElementById("demo").innerHTML = message_text;
    var imagedata = canvas.toDataURL("image/png");
    document.getElementById("imgShow").src = imagedata;
}
document.getElementById("myRange").oninput = function() {
    document.getElementById("demo2").innerHTML = this.value;
}
if(urlParams.has('scrambles'))
{
    document.getElementById("myRange").value = urlParams.get('scrambles');
    document.getElementById("demo2").innerHTML = urlParams.get('scrambles');
    myFunction();
}

</script>