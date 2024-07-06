

!!! warning "Work in progress"

The Sphenic Biaxial is a 2D puzzle meant to teach beginners about cycles, parity, and commutators.

<svg
  id="sim"
  width="100%"
  height="auto"
  viewBox="-1 -1 101 51"
  xmlns="http://www.w3.org/2000/svg">
  <rect width="98%" height="97%" style="stroke-width:1; stroke:gray;" rx="2" fill-opacity="0"/>
  <circle r="10" cx="25" cy="25" fill="red" stroke="black" class="left" id="Lcircle"/>
  <line x1="25" y1="25" x2="35" y2="25" stroke="black" id="line2" stroke-linecap="round"/>
  <circle r="20" cx="75" cy="25" fill="orange" stroke="black" class="left" id="Rcircle"/>
  <line x1="75" y1="25" x2="75" y2="5" stroke="black" id="line3" stroke-linecap="round"/>

</svg>

<script>
    var svg = document.getElementById('sim');

    var target = 0;
    var currentTargetAmount = 0;
    var target2 = 0;
    var currentTargetAmount2 = 0;

    function animate() {
        currentTargetAmount++;
        document.getElementById('line2').setAttribute("transform", "rotate(" + currentTargetAmount + " 25 25)");
        if (currentTargetAmount != target) requestAnimationFrame(animate);
        if (currentTargetAmount > target) currentTargetAmount = target;
    }

    function animate2() {
        currentTargetAmount2++;
        document.getElementById('line3').setAttribute("transform", "rotate(" + currentTargetAmount2 + " 75 25)");
        if (currentTargetAmount2 != target2) requestAnimationFrame(animate2);
        if (currentTargetAmount2 > target2) currentTargetAmount2 = target2;
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
