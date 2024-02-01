# Steps of CFOP on 3^d


<p>CFOP on: 3<sup><span id="sliderDisplay">5</span></sup></p>
<input type="range" min="3" max="10" value="3" class="slider" id="myRange">


<script>
    var slider = document.getElementById("myRange");
    var output = document.getElementById("sliderDisplay");
    output.innerHTML = slider.value;

    slider.oninput = function() {
        output.innerHTML = this.value;
    }

   
    // document.getElementById("demo2").value =  document.getElementById("myRange").innerHTML;

</script>