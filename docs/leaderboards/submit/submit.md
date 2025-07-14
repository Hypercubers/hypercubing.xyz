---
title: Submit
---

# Hypercubing Leaderboard Submission Form

<div id="submitted-text">
    <p>Thank you for your submission to the Hypercubing.xyz leaderboard! A moderator will review this at some point.</p>
</div>

<form onsubmit="webhook();return false;" id="submission-form">
    <div>
        <label for="name">Username: </label>
        <input type="text" name="name" placeholder="name" class="submit-form" id="nameInput">
    </div>
    <div>
        <label for="date">Date of solve: </label>
        <input type="date" id="dateInput">
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
    <div style="display: flex;">
        <label for ="t_0-hour">Time: </label>
        <input type="number" name="t_0-hour" maxlength="3" min="0" max="23" autocomplete="off" value="">
        <div>h</div>
        <input type="number" name="t_0-minute" maxlength="2" min="0" max="59" autocomplete="off" value="">
        <div>m</div>
        <input type="number" name="t_0-second" maxlength="2" min="0" max="59" autocomplete="off" value="">
        <div>s</div>
        <input type="number" name="t_0-millisecond" maxlength="3" min="0" max="999" autocomplete="off" value="">
        <div>ms</div>
    </div>
    <div>
        <label for="link">Video link: </label>
        <input type="text" id="linkInput">
    </div>
    <button type="submit" class="md-button md-button--primary">Submit</button>

</form>


<script>
    function webhook() {
        console.log("submitted!");
        var hook = new XMLHttpRequest();

        hook.open('POST', 'https://discord.com/api/webhooks/1394188268685492264/PfgjTildULXqqd8FTKInL4FbclHmpCOwe8XMrTMSeKkpxR9jGrJwU5PXiAMkfQ2hHD80');

        hook.setRequestHeader('Content-type', 'application/json');

        var name = document.getElementById('nameInput').value;
        var date = document.getElementById('dateInput').value;
        var link = document.getElementById('linkInput').value;

        var content = {
            content: ("**New Submission:** `" + date + ", " + link + ", " + name + "`")
        }

        hook.send(JSON.stringify(content));

        document.getElementById('submission-form').style.display = "none";
        document.getElementById('submitted-text').style.display = "block";
    }

</script>