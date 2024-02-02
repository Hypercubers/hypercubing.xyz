# Steps of CFOP on 3^d


<p>CFOP on: 3<sup><span id="sliderDisplay">5</span></sup></p>
<input type="range" min="3" max="10" value="3" class="slider" id="myRange">


## Cross

<p id="cross_text"></p> 

## F2L

<p id="f2l_text"></p> 

## OLL

<p id="oll_text"></p> 

## PLL

<p id="pll_text"></p> 


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
        // array of piece types
        const pieces = [
            [1],
            [1,2],
            [1,4,4],
            [1,6,12,8],
            [1,8,24,32,16],
            [1,10,40,80,80,32],
            [1,12,60,160,240,192,64],
            [1,14,84,280,560,672,448,128],
            [1,16,112,448,1120,1792,1792,1024,256],
            [1,18,144,672,2016,4032,5376,4608,2304,512],
            [1,20,180,960,3360,8064,13440,15360,11520,5120,1024]
        ];

        total_pieces = (3**dim)-1;

        // cross text
        cross_text = "Solve all " + ((pieces[dim][1])-2) + " of the 2c pieces around one of the centers.";
        document.getElementById("cross_text").innerHTML = cross_text;

        // F2L text
        f2l_text = dim + "-dimensional F2L consists of " + (dim-2) + " type" + (dim-2>1?`s`:``)+" of pair"+ (dim-2>1?`s`:``)+":<br>";
        for(var i = 1; i<(dim+1); i++) {
            if (i<3) continue;
            if (i==dim) { // the last pair with nc pieces and n-1c pieces
                f2l_text = f2l_text + ((pieces[dim][i])/2) + " F2L-"+dim+String.fromCharCode('a'.charCodeAt() + i-3)+" pairs (" + dim + "c & " + (dim-1) +"c pieces)<br>";
                break;
            } 
            f2l_text = f2l_text + ((pieces[dim][i]-pieces[dim-1][i])/2) + " F2L-"+dim+String.fromCharCode('a'.charCodeAt() + i-3)+" pairs (" + (i) + "c & " + (i-1) +"c pieces)<br>"; 
        }
        document.getElementById("f2l_text").innerHTML = f2l_text;

        //OLL text

        //PLL text
        

        

        // temporary OLL and PLL text
        // message_text += "OLL-" + dim + "<br>";
        // message_text += "PLL-" + dim + "<br>";

    }

myFunction(3);
</script>