
var shortList = document.getElementsByClassName("shorttime");
var longList = document.getElementsByClassName("longtime");

var isoList = document.getElementsByClassName("isodate");
var relativeList = document.getElementsByClassName("relativedate");

function LongTime() {
    // switches to the long time format
    for (var i = 0; i < shortList.length; i++) {
        shortList[i].style.display = "none";
        longList[i].style.display = "block";
    } 
    document.getElementById("long-time-format").classList.add("md-button--primary"); 
    document.getElementById("wca-time-format").classList.remove("md-button--primary"); 
    sessionStorage.setItem("timeFormat", "long");
}

function ShortTime() {
    // switches to the short time format
    for (var i = 0; i < longList.length; i++) {
        longList[i].style.display = "none";
        shortList[i].style.display = "block";
    }  
    document.getElementById("long-time-format").classList.remove("md-button--primary"); 
    document.getElementById("wca-time-format").classList.add("md-button--primary"); 
    sessionStorage.setItem("timeFormat", "short");
}

function RelativeDate() {
    // switches to the relative date format
    for (var i = 0; i < isoList.length; i++) {
        isoList[i].style.display = "none";
        relativeList[i].style.display = "block";
    } 
    document.getElementById("relative-date-format").classList.add("md-button--primary"); 
    document.getElementById("iso-date-format").classList.remove("md-button--primary"); 
    sessionStorage.setItem("dateFormat", "relative");
}

function ISODate() {
    // switches to the iso date format
    for (var i = 0; i < relativeList.length; i++) {
        relativeList[i].style.display = "none";
        isoList[i].style.display = "block";
    } 
    document.getElementById("iso-date-format").classList.add("md-button--primary"); 
    document.getElementById("relative-date-format").classList.remove("md-button--primary"); 
    sessionStorage.setItem("dateFormat", "iso");
}


document.addEventListener("DOMContentLoaded", load);
document.addEventListener("hashchange", load);

function load() {
    // load cookies for view options
    var timeFormat = sessionStorage.getItem("timeFormat");
    if (timeFormat == "short") {
        ShortTime();
    } else {
        LongTime();
    }
    var dateFormat = sessionStorage.getItem("dateFormat");
    if (dateFormat == "relative") {
        RelativeDate();
    } else {
        ISODate();
    }
}

load();