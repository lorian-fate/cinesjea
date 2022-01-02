

var userCount = 0;
var filmCount = 0;
var roomCount = 0;
var proyCount = 0;


function show_fiml_op(){
    var userBar = document.getElementById("adminUsernav");
    var filmBar = document.getElementById("adminfilmnav");
    var roomBar = document.getElementById("adminRoomnav");
    var proyBar = document.getElementById("adminProynav");
    var divfilm = document.getElementById('allFilm');
    
    if ((userCount == 1) || (roomCount == 1) || (proyCount == 1)){
        userBar.style.display = 'none';
        roomBar.style.display = 'none';
        proyBar.style.display = 'none';
        userCount = 0;
        roomCount = 0;
        proyCount = 0;

        if (filmCount == 0){
            filmBar.style.display = 'block';
            filmCount = 1;
            divfilm.style.marginTop = '80px';
        }
    }
    else{
        if (filmCount == 0){
            filmBar.style.display = 'block';
            filmCount = 1;
            divfilm.style.marginTop = '80px';
        }
        else if (filmCount == 1){
            filmBar.style.display = 'none';
            filmCount = 0;
            divfilm.style.marginTop = '150px';
        }
    }
    

}
function show_user_op(){
    var userBar = document.getElementById("adminUsernav");
    var filmBar = document.getElementById("adminfilmnav");
    var roomBar = document.getElementById("adminRoomnav");
    var proyBar = document.getElementById("adminProynav");
    var divfilm = document.getElementById('allFilm');

    if ((filmCount == 1) || (roomCount == 1) || (proyCount == 1)){
        filmBar.style.display = 'none';
        roomBar.style.display = 'none';
        proyBar.style.display = 'none';
        filmCount = 0;
        roomCount = 0;
        proyCount = 0;
        if(userCount == 0){
            userBar.style.display = 'block';
            userCount = 1;
            divfilm.style.marginTop = '80px';
        }
    }
    else {
        if(userCount == 0){
            userBar.style.display = 'block';
            userCount = 1;
            divfilm.style.marginTop = '80px';
        }
        else if(userCount == 1){
            userBar.style.display = 'none';
            userCount = 0;
            divfilm.style.marginTop = '150px';
        }
    }

}



function show_room_op(){
    var userBar = document.getElementById("adminUsernav");
    var filmBar = document.getElementById("adminfilmnav");
    var roomBar = document.getElementById("adminRoomnav");
    var proyBar = document.getElementById("adminProynav");
    var divfilm = document.getElementById('allFilm');

    if ((filmCount == 1) || (userCount == 1) || (proyCount == 1)){
        filmBar.style.display = 'none';
        userBar.style.display = 'none';
        proyBar.style.display = 'none';
        filmCount = 0;
        userCount = 0;
        proyCount = 0;
        if(roomCount == 0){
            roomBar.style.display = 'block';
            roomCount = 1;
            divfilm.style.marginTop = '80px';
        }
    }
    else {
        if(roomCount == 0){
            roomBar.style.display = 'block';
            roomCount = 1;
            divfilm.style.marginTop = '80px';
        }
        else if(roomCount == 1){
            roomBar.style.display = 'none';
            roomCount = 0;
            divfilm.style.marginTop = '150px';
        }
    }

}
function show_pro_op(){
    var userBar = document.getElementById("adminUsernav");
    var filmBar = document.getElementById("adminfilmnav");
    var roomBar = document.getElementById("adminRoomnav");
    var proyBar = document.getElementById("adminProynav");
    var divfilm = document.getElementById('allFilm');

    if((filmCount == 1) || (userCount == 1) || (roomCount == 1)){
        filmBar.style.display = 'none';
        userBar.style.display = 'none';
        roomBar.style.display = 'none';
        filmCount = 0;
        userCount = 0;
        roomCount = 0;
        if(proyCount == 0){
            proyBar.style.display = 'block';
            proyCount = 1;
            divfilm.style.marginTop = '80px';
        }
    }
    else {
        if(proyCount == 0){
            proyBar.style.display = 'block';
            proyCount = 1;
            divfilm.style.marginTop = '80px';
        }
        else if(proyCount == 1){
            proyBar.style.display = 'none';
            proyCount = 0;
            divfilm.style.marginTop = '150px';
        }
    }

}


