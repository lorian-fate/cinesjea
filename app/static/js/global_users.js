
var countTick = 0;
var countProy = 0;

function myTicket(){
    var myticket = document.getElementById('dicTicket');
    var myproyection = document.getElementById('divPro');
    if (countProy == 1){
        myproyection.style.display = 'none';
        countProy = 0;

        if (countTick == 0){
            myticket.style.display = 'block';
            countTick = 1;
        }

    }
    else{
        if(countTick == 0){
            myproyection.style.display = 'none';
            countProy = 0;
            myticket.style.display = 'block';
            countTick = 1;
        }
        else if(countTick == 1){
            myticket.style.display = 'none';
            countTick = 0;
            myproyection.style.display = 'block';
            countProy = 1;
        }
    }
}

function myProyec(){
    var myticket = document.getElementById('dicTicket');
    var myproyection = document.getElementById('divPro');
    if (countTick == 1){
        myticket.style.display = 'none';
        countTick = 0;

        if (countProy == 0){
            myproyection.style.display = 'block';
            countProy = 1;
        }

    }
    else{
        if(countProy == 0){
            myproyection.style.display = 'block';
            countTick = 1;
        }
        else if(countProy == 1){
            myproyection.style.display = 'block';
            countTick = 0;
        }
    }
}