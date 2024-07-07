

!!! warning "Work in progress"

The Sphenic Biaxial is a 2D puzzle meant to teach beginners about cycles, parity, and commutators.

<svg
  id="sim"
  width="100%"
  height="auto"
  viewBox="-1 -1 101 51"
  xmlns="http://www.w3.org/2000/svg">
  <rect width="98%" height="97%" style="stroke-width:1; stroke:gray;" rx="2" fill-opacity="0"/>
  <circle r="10" cx="30" cy="25" fill-opacity="0" stroke="black" id="Lcircle"/>
  <circle r="20" cx="60" cy="25" fill-opacity="0" stroke="black" id="Rcircle"/>
  <circle r="3" cx="20" cy="25" fill="grey" class="L" id="bead0"/>
  <circle r="3" cx="40" cy="25" fill="white" class="L R" id="bead1"/>
  <circle r="3" cx="46" cy="11" fill="green" class="R" id="bead2"/>
  <circle r="3" cx="60" cy="5" fill="red" class="R" id="bead3"/>
  <circle r="3" cx="74" cy="11" fill="magenta" class="R" id="bead4"/>
  <circle r="3" cx="80" cy="25" fill="yellow" class="R" id="bead5"/>
  <circle r="3" cx="74" cy="39" fill="blue" class="R" id="bead6"/>
  <circle r="3" cx="60" cy="45" fill="orange" class="R" id="bead7"/>
  <circle r="3" cx="46" cy="39" fill="purple" class="R" id="bead8"/>


</svg>

<script>
    var svg = document.getElementById('sim');

    var Lbeads = ["bead0, bead1"];
    var Rbeads = ["bead1", "bead2", "bead3", "bead4", "bead5", "bead6", "bead7", "bead8"];

    var target = 0;
    var currentTargetAmount = 0;
    var target2 = 0;
    var currentTargetAmount2 = 0;

    function animate() {
        currentTargetAmount++;
        var LList = document.getElementsByClassName("L");
        for (var m = 0; m < LList.length; m++) {
            LList[m].setAttribute("transform", "rotate(" + currentTargetAmount + " 30 25)");
        }
        if (currentTargetAmount != target) requestAnimationFrame(animate);
        if (currentTargetAmount >= target) { 
            currentTargetAmount = target;
            var temp = Lbeads[0];
            Lbeads[0] = Lbeads[1];
            Lbeads[1] = temp;
            document.getElementById(Lbeads[1]).classList.add("R");
            document.getElementById(Lbeads[0]).classList.remove("R");
            console.log(document.getElementById(Lbeads[1]).classList);
            printBeads();
        }
    }

    function printBeads() {
        console.log("bead1: " );



    }

    function animate2() {
        currentTargetAmount2++;


        var RList = document.getElementsByClassName("R");
        for (var m = 0; m < RList.length; m++) {
            RList[m].setAttribute("transform", "rotate(" + currentTargetAmount2 + " 60 25)");
        }
        if (currentTargetAmount2 != target2) requestAnimationFrame(animate2);
        if (currentTargetAmount2 > target2) {
            currentTargetAmount2 = target2;
            var temp = Rbeads[0];
            Rbeads[0] = Rbeads[7];
            Rbeads[7] = Rbeads[6];
            Rbeads[6] = Rbeads[5];
            Rbeads[5] = Rbeads[4];
            Rbeads[4] = Rbeads[3];
            Rbeads[3] = Rbeads[2];
            Rbeads[2] = Rbeads[1];
            Rbeads[1] = temp;
            document.getElementById(Rbeads[1]).classList.remove("L");
            document.getElementById(Rbeads[0]).classList.add("L");
        }
    }


    document.getElementById('Lcircle').addEventListener('click', function(event) {
        target += 180;
        requestAnimationFrame(animate);
    }, false);

    document.getElementById('Rcircle').addEventListener('click', function(event) {
        target2 += 45;
        requestAnimationFrame(animate2);
    }, false);

    
    


</script>

!!! Settings
