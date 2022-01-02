



var clickCount = 0;
window.addEventListener('click', function(e) {
    var improfl = document.getElementById("myprofile");
    /*2. Si el div con id clickbox contiene a e. target*/
    if (document.getElementById('mydivhide').contains(e.target)) {
        if (clickCount == 0){
            improfl.style.display = "block";
            clickCount = 1;
        }
        else if(clickCount == 1){
            improfl.style.display = "none";
            clickCount = 0;

        }
    } else {
        if(clickCount == 1){
            improfl.style.display = "none";
            clickCount = 0;

        }
        else if(clickCount == 0){
            clickCount = 0;
        }
    }
})