
var shortList = document.getElementsByClassName("shorttime");
var longList = document.getElementsByClassName("longtime");

function LongTime() {
    // switches to the long time format
    for (var i = 0; i < shortList.length; i++) {
        shortList[i].style.display = "none";
        longList[i].style.display = "block";
    } 
    document.getElementById("long-time-format").classList.add("md-button--primary"); 
    document.getElementById("wca-time-format").classList.remove("md-button--primary"); 
}

function ShortTime() {
    // switches to the short time format
    for (var i = 0; i < longList.length; i++) {
        longList[i].style.display = "none";
        shortList[i].style.display = "block";
    }  
    document.getElementById("long-time-format").classList.remove("md-button--primary"); 
    document.getElementById("wca-time-format").classList.add("md-button--primary"); 
}

document.addEventListener("DOMContentLoaded", (event) => {
    for (var i = 0; i < shortList.length; i++) {
        shortList[i].style.display = "none";
    }
});