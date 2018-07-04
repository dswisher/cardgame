
// Toggle between adding and removing the "responsive" class to topnav
// when the user clicks on the icon
// TODO - refactor this - put in a namespace, give a better name, don't rely on id, etc.
function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}

