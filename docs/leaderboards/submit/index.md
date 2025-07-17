---
title: Submit
---

# Hypercubing Leaderboard Submission Form

<form id="submission-form">
    <div>
        <label for="name">Username: </label>
        <input class="submit-input" required="true" type="text" name="name" placeholder="name" id="nameInput">
    </div>
    <div>
        <label for="date">Date of solve: </label>
        <input class="submit-input" required="true" type="date" id="dateInput">
    </div>
    <div>
        <label for="puzzles">Puzzle: </label>
        <select id="puzzles">
            <option value="3x3x3x3">3x3x3x3</option>
            <option value="2x2x2x2">2x2x2x2</option>
            <option value="4x4x4x4">4x4x4x4</option>
            <option value="5x5x5x5">5x5x5x5</option>
            <option value="6x6x6x6">6x6x6x6</option>
            <option value="7x7x7x7">7x7x7x7</option>
            <option value="1x3x3x3">1x3x3x3</option>
            <option value="2x2x2x3">2x2x2x3</option>
            <option value="2x2x3x3">2x2x3x3</option>
            <option value="phys_2x2x2x2">Physical 2x2x2x2</option>
            <option value="phys_3x3x3x3">Physical 3x3x3x3</option>
            <option value="virt_phys_3x3x3x3">Virtual Physical 3x3x3x3</option>
            <option value="3-layer_simplex">3-Layer Simplex</option>
            <option value="3x3x3x3x3">3x3x3x3x3</option>
            <option value="2x2x2x2x2">2x2x2x2x2</option>
            <option value="4x4x4x4x4">4x4x4x4x4</option>
            <option value="3x3x3x3x3x3">3x3x3x3x3x3</option>
            <option value="hemimegaminx">Hemimegaminx</option>
            <option value="klein_quartic">Canon-Cut Klein Quartic</option>
            <option value="dyck_map">Canon-Cut Dyck Map</option>
            <option value="3x3x3_1d">3x3x3 in 2D projection with 1D Vision</option>
        </select>
    </div>
    <div>
        <label for="formats">Format: </label>
        <select id="formats">
            <option value="single">Single solve</option>
            <option value="ao5">Average of 5</option>
            <option value="nf">No filters single solve</option>
            <option value="bld">Blindfolded single solve</option>
            <option value="oh">One handed single solve</option>
        </select>
    </div>
    <div>
        <label for="programs">Program used: </label>
        <select id="programs">
            <option value="HSC">Hyperspeedcube</option>
            <option value="MPU">Magic Puzzle Ultimate</option>
            <option value="MC3D">Magic Cube 3D</option>
            <option value="MC4D">Magic Cube 4D</option>
            <option value="MC5D">Magic Cube 5D</option>
            <option value="MC7D">Magic Cube 7D</option>
            <option value="MT">Magic Tile</option>
            <option value="AKKEI-SIM">Akkei's 3^4 sim</option>
            <option value="-">None (physical puzzle)</option>
        </select>
    </div>
    <div style="display: flex; flex-direction: row; align-items: center;">
        <label for ="t_0-hour">Time: </label>
        <input class="submit-input" required="true" type="number" id="hour" placeholder="0" value="0" name="t_0-hour" maxlength="3" min="0" max="23" autocomplete="off" value="">
        <div>h</div>
        <input class="submit-input" required="true" type="number" id="minute" placeholder="0" value="0" name="t_0-minute" maxlength="2" min="0" max="59" autocomplete="off" value="">
        <div>m</div>
        <input class="submit-input" required="true" type="number" id="second" placeholder="0.000" value="0.000" name="t_0-second" maxlength="6" min="0.0" max="59.999" step="0.001" autocomplete="off" value="">
        <div>s</div>
    </div>
    <div>
        <label for="link">Video link: </label>
        <input class="submit-input" required="true" placeholder="https://youtu.be/watch?v=QTc-rG-nunA" type="text" id="linkInput">
    </div>
</form>

!!! info "Verification"
    All runs are verified by a team of moderators to ensure they comply with our rules. Make ensure the above information is accurate before submitting.

<button onclick="webhook();return false;" id="submit-button" type="submit" class="md-button md-button--primary">Submit</button>

<script>

    // call checkIntupValidity every 1/4 second
    setInterval(checkInputValidity, 250);

    function checkInputValidity() {
        var validName = document.getElementById('nameInput').value !== "";
        var validDate = document.getElementById('dateInput').value !== "";
        var validLink = document.getElementById('linkInput').value !== "";
        var validTime = validateTime();

        if (validName && validDate && validLink && validTime) {
            document.getElementById('submit-button').style.display = "block";
        } else {
            document.getElementById('submit-button').style.display = "none";
        }
        
    }

    function validateTime() {
        var h = document.getElementById('hour').value;
        var m = document.getElementById('minute').value;
        var s = document.getElementById('second').value;
        // console.log(""+h+" "+m+" "+s);

        var hReg = /[0-9]{1,2}/;
        var mReg = /[0-9]{1,2}/;
        var sReg = /[0-9]{1,2}\.[0-9]{1,3}/;

        return (hReg.test(h) && mReg.test(m) && sReg.test(s));
    }

    function webhook() {
        var hook = new XMLHttpRequest();

        hook.open('POST', 'https://discord.com/api/webhooks/1394188268685492264/PfgjTildULXqqd8FTKInL4FbclHmpCOwe8XMrTMSeKkpxR9jGrJwU5PXiAMkfQ2hHD80');

        hook.setRequestHeader('Content-type', 'application/json');

        var name = document.getElementById('nameInput').value;
        var date = document.getElementById('dateInput').value;
        var link = document.getElementById('linkInput').value;
        var puzzle = document.getElementById('puzzles').value;
        var format = document.getElementById('formats').value;
        var program = document.getElementById('programs').value;

        var hour = document.getElementById('hour').value;
        var minute = document.getElementById('minute').value;
        var second = document.getElementById('second').value;

        var timeText = "" + hour + "h " + minute + "m " + second + "s";

        if (hour === "0") {
            timeText = "" + minute + "m " + second + "s";
        }
        if (hour === "0" && minute === "0") {
            timeText = "" + second + "s";
        } 
        
        
        

        var DiscordMessage = {
            content: ("**" + name + "** just submitted a **[" + timeText + " " + puzzle + " " + format + "](" + link + ")** to the leaderboard form! \nDetails: `" + date + ", " + link + ", " + timeText + ", " + program + ", " + name + ", " + puzzle + ", " + format + "`")
        }

        hook.send(JSON.stringify(DiscordMessage));
        console.log("submitted!");

        // send the user to the confirmation page
        window.location.href = 'https://hypercubing.xyz/leaderboards/submit/confirmation';
    }

</script>