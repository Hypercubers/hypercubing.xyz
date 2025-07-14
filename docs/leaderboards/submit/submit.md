---
title: Submit
---

# Hypercubing Leaderboard Submission Form

<form>
    <div>
        <label for="name">Username: </label>
        <input type="text" name="name" placeholder="name" class="submit-form">
    </div>
    <div>
        <label for="date">Date of solve: </label>
        <input type="date">
    </div>
    <div>
        <label for="puzzles">Puzzle: </label>
        <select id="puzzles">
            <option value="3x3x3x3">3x3x3x3</option>
            <option value="Firefox">
            <option value="Chrome">
            <option value="Opera">
            <option value="Safari">
        </select>
    </div>
    <div>
        <label for="formats">Format: </label>
        <select id="formats">
            <option value="single">Single solve</option>
            <option value="ao5">Average of 5</option>
            <option value="nf">No filters</option>
            <option value="bld">Blindfolded<option>
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
    
    
    <button type="submit" class="md-button md-button--primary">Submit</button>
</form>