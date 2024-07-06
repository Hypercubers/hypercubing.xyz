

!!! warning "Work in progress"
    - refactor to use SVG

<canvas id="myCanvas" style="border:2px solid #000000; display: block; width:100%; border-radius: 12px;"> </canvas>

!!! Settings


    Number of thingies: <span id="sliderDisplay">5</span>

    <input type="range" min="1" max="20" value="5" class="slider" id="myRange">

    <button onclick="update()" style="background-color: #e7e7e7; color: black; padding: 8px 8px; border-radius: 12px;">Reset</button>

    <button onclick="twistL()" style="background-color: #e7e7e7; color: black; padding: 8px 8px; border-radius: 12px;">TWISTS</button>

<script>


const canvas = document.getElementById('myCanvas');
const ctx = canvas.getContext('2d');

var slider = document.getElementById("myRange");

var output = document.getElementById("sliderDisplay");
output.innerHTML = slider.value;




var twistAmount = 0;
var twistTarget = 0;


// get the markdown color theme
const computedStyle = getComputedStyle(canvas);
const typesetColor = computedStyle.getPropertyValue("--md-typeset-color");

slider.oninput = function() {
    output.innerHTML = this.value;
    draw();
}

const r1 = 150;

const r2 = 100;

 
window.addEventListener('resize', resizeCanvas, false);
        
  function resizeCanvas() {
    let rect = canvas.getBoundingClientRect();
    canvas.width = rect.width;
    canvas.height = rect.width/2;

    canvas.style.height = canvas.height + "px";

    ctx.scale(devicePixelRatio, devicePixelRatio)

    draw(); 
  }

function drawLeftCircle(x, y, start) {
    ctx.beginPath();
    ctx.arc(x, y, r2, start + Math.PI/2,  start + 3*Math.PI/2);
    ctx.fillStyle = "grey";
    ctx.fill();

    ctx.beginPath();
    ctx.arc(x,y, r2, start + 3*Math.PI/2,  start + Math.PI/2);
    ctx.fillStyle = "red";
    ctx.fill();
}

function drawRightCircle(x, y) {
    ctx.beginPath();
    ctx.arc(x, y, r1, 0, 2 * Math.PI);
    ctx.strokeStyle = typesetColor;
    ctx.stroke();
}

function twistL() {
    twistTarget = twistTarget + Math.PI;

    // twistAmount += Math.PI;
    draw();
}


function draw() {

    if (twistTarget != twistAmount) requestAnimationFrame(draw);
    twistAmount += 0.1;
    if (twistAmount > twistTarget) twistAmount = twistTarget;

    
   
    ctx.clearRect(0, 0, canvas.width, canvas.height)
   
    console.log(slider.value);

    

    output.innerHTML = slider.value;
    
    
    // ctx.translate(canvas.width/2-r2, canvas.height/2);
    // ctx.rotate(new Date() / 1000 % (2 * Math.PI));
    drawLeftCircle(canvas.width/2-r2, canvas.height/2, twistAmount);
    // ctx.translate(-1*(canvas.width/2-r2),-1*(canvas.height/2));
    drawRightCircle(canvas.width/2+r1, canvas.height/2);
}



function update() {
    resizeCanvas();
}

update();

</script>






test:

<svg
  id="sim"
  width="100%"
  height="auto"
  viewBox="-1 -1 101 51"
  xmlns="http://www.w3.org/2000/svg">
  <rect width="98%" height="97%" style="stroke-width:1; stroke:gray;" rx="2" fill-opacity="0"/>
  <circle r="15" cx="50" cy="25" fill="red" stroke="black" class="left" id="corcle"/>
  <line x1="50" y1="25" x2="50" y2="10" stroke="black" id="line2" stroke-linecap="round"/>

</svg>

<script>
    var svg = document.getElementById('sim');

    var cols = ["orange", "red"];
    var count = 0;
    var target = 90;
    var currentTargetAmount = 0;

    function animate() {
        currentTargetAmount++;
        document.getElementById('line2').setAttribute("transform", "rotate(" + currentTargetAmount + " 50 25)");
        if (currentTargetAmount != target) requestAnimationFrame(animate);
        if (currentTargetAmount > target) currentTargetAmount = target;
    }


    document.getElementById('corcle').addEventListener('click', function(event) {
        // document.getElementById('corcle').style.fill = cols[(count++)%2];
        target += 90;
        requestAnimationFrame(animate);
    }, false);

    
    


</script>