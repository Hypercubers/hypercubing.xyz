# Steps of CFOP on 3^d


<p>CFOP on: 3<sup><span id="sliderDisplay">5</span></sup></p>
<input type="range" min="3" max="10" value="3" class="slider" id="myRange">


## Cross

<p id="cross"></p> can be characterized by

<p id="text"></p>


<script>
    var slider = document.getElementById("myRange");
    var output = document.getElementById("sliderDisplay");
    output.innerHTML = slider.value;
    // updates the text above the slider when you slide the slider by sliding it in the slidy way that you can slide a slider
    slider.oninput = function() {
        output.innerHTML = this.value;
        myFunction(this.value);
    }


    function myFunction(dim) {
        // displays cross-n
        message_text = "Cross-" + dim + "<br>";
        // displays F2L-(dim)(letter), n times
        for(var i = 1; i<(dim-1); i++) {
            message_text = message_text + "F2L-"+dim+String.fromCharCode('A'.charCodeAt() + i-1)+"<br>";
        }
        message_text += "OLL-" + dim + "<br>";
        message_text += "PLL-" + dim + "<br>";

        //updates the text at the very end
        document.getElementById("text").innerHTML = message_text;
        document.getElementById("cross").innerHTML = "Cross-" + dim;
    }

myFunction(3);
</script>