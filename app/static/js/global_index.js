

var todCount = 0;
var semCount = 0;
var mesCount = 0;
var estCount = 0;

function mostrar_todas(){
	var todBar = document.getElementById("mostrados_todas");
	var semBar = document.getElementById("mostrados_semana");
	var mesBar = document.getElementById("mostrados_mes");
	var estBar = document.getElementById("mostrados_estrenos");
	var proBar = document.getElementById("mostrados_proximas");

	var divuno = document.getElementById("div1");
	var divdos = document.getElementById("div2");
	var divtre = document.getElementById("div3");
	var divcua = document.getElementById("div4");
	var divcin = document.getElementById("div5");

	if ((semCount == 1) || (mesCount == 1) || (estCount == 1)){
		semBar.style.display = 'none';
		mesBar.style.display = 'none';
		estBar.style.display = 'none';
		semCount = 0;
		mesCount = 0;
		estCount = 0;

		

		if(todCount == 0){
			divtre.style.display = 'none';
			divcua.style.display = 'none';
			divcin.style.display = 'none';
			divuno.style.display = 'none';

			proBar.style.display = 'none';
			todBar.style.display = 'block';
			divdos.style.display = 'block';
			//divdos.style.order = -1;
			todCount = 1;
		}
	}
	else{
		if (todCount == 0){
			divuno.style.display = 'none';

			proBar.style.display = 'none';
			todBar.style.display = 'block';
			divdos.style.display = 'block';
			//divdos.style.order = -1;
			todCount = 1;
		}
		else if(todCount == 1){
			divuno.style.display = 'block';
			proBar.style.display = 'block';
			todBar.style.display = 'none';
			divdos.style.display = 'none';
			//divdos.style.order = '0';
			todCount = 0;
		}
	}
}

function mostrar_semanas(){
	var todBar = document.getElementById("mostrados_todas");
	var semBar = document.getElementById("mostrados_semana");
	var mesBar = document.getElementById("mostrados_mes");
	var estBar = document.getElementById("mostrados_estrenos");
	var proBar = document.getElementById("mostrados_proximas");

	var divuno = document.getElementById("div1");
	var divdos = document.getElementById("div2");
	var divtre = document.getElementById("div3");
	var divcua = document.getElementById("div4");
	var divcin = document.getElementById("div5");

	if ((todCount == 1) || (mesCount == 1) || (estCount == 1)){
		todBar.style.display = 'none';
		mesBar.style.display = 'none';
		estBar.style.display = 'none';
		todCount = 0;
		mesCount = 0;
		estCount = 0;

		if(semCount == 0){
			divuno.style.display = 'none';
			divtre.style.display = 'none';
			divcin.style.display = 'none';
			divdos.style.display = 'none';

			proBar.style.display = 'none';
			divcua.style.display = 'block';
			semBar.style.display = 'block';
			semCount = 1;
		}
	}
	else{
		if (semCount == 0){
			divuno.style.display = 'none';
			proBar.style.display = 'none';

			divcua.style.display = 'block';
			semBar.style.display = 'block';
			semCount = 1;
		}
		else if(semCount == 1){
			proBar.style.display = 'block';
			divuno.style.display = 'block';

			divcua.style.display = 'none';
			semBar.style.display = 'none';
			semCount = 0;
		}
	}
}

function mostrar_mes(){
	var todBar = document.getElementById("mostrados_todas");
	var semBar = document.getElementById("mostrados_semana");
	var mesBar = document.getElementById("mostrados_mes");
	var estBar = document.getElementById("mostrados_estrenos");
	var proBar = document.getElementById("mostrados_proximas");

	var divuno = document.getElementById("div1");
	var divdos = document.getElementById("div2");
	var divtre = document.getElementById("div3");
	var divcua = document.getElementById("div4");
	var divcin = document.getElementById("div5");

	if ((todCount == 1) || (semCount == 1) || (estCount == 1)){
		todBar.style.display = 'none';
		semBar.style.display = 'none';
		estBar.style.display = 'none';
		todCount = 0;
		semCount = 0;
		estCount = 0;

		if(mesCount == 0){
			divuno.style.display = 'none';
			divdos.style.display = 'none';
			divcua.style.display = 'none';
			divcin.style.display = 'none';

			proBar.style.display = 'none';
			mesBar.style.display = 'block';
			divtre.style.display = 'block';
			mesCount = 1;
		}
	}
	else{
		if (mesCount == 0){
			divuno.style.display = 'none';
			proBar.style.display = 'none';

			mesBar.style.display = 'block';
			divtre.style.display = 'block';
			mesCount = 1;
		}
		else if(mesCount == 1){
			proBar.style.display = 'block';
			divuno.style.display = 'block';

			divtre.style.display = 'none';
			mesBar.style.display = 'none';
			mesCount = 0;
		}
	}
}

function mostrar_est(){
	var todBar = document.getElementById("mostrados_todas");
	var semBar = document.getElementById("mostrados_semana");
	var mesBar = document.getElementById("mostrados_mes");
	var estBar = document.getElementById("mostrados_estrenos");
	var proBar = document.getElementById("mostrados_proximas");

	var divuno = document.getElementById("div1");
	var divdos = document.getElementById("div2");
	var divtre = document.getElementById("div3");
	var divcua = document.getElementById("div4");
	var divcin = document.getElementById("div5");

	if ((todCount == 1) || (semCount == 1) || (mesCount == 1)){
		todBar.style.display = 'none';
		semBar.style.display = 'none';
		mesBar.style.display = 'none';
		todCount = 0;
		semCount = 0;
		mesCount = 0;

		if(estCount == 0){
			divuno.style.display = 'none';
			divdos.style.display = 'none';
			divtre.style.display = 'none';
			divcua.style.display = 'none';

			proBar.style.display = 'none';
			divcin.style.display = 'block';
			estBar.style.display = 'block';
			estCount = 1;
		}
	}
	else{
		if (estCount == 0){
			proBar.style.display = 'none';
			divuno.style.display = 'none';

			divcin.style.display = 'block';
			estBar.style.display = 'block';
			estCount = 1;
		}
		else if(estCount == 1){
			proBar.style.display = 'block';
			divuno.style.display = 'block';

			divcin.style.display = 'none';
			estBar.style.display = 'none';
			estCount = 0;
		}
	}
}