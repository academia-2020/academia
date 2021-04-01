$(function(){
	var enlace = $('#link_busqueda');
	enlace.on('click',function(){
		var texto = $('#tx_busqueda');
		enlace.attr('href','http://127.0.0.1:8000/visitante/lista_cursos/?criterio=' + texto.val());
	});
}())

// Colapsar descripcion

var coll = document.getElementsByClassName("collapsible");
var i;
for (i=0;i<coll.length; i++){
	coll[i].innerHTML = '(Ver descripcion..)';
	coll[i].addEventListener("click", function(){
		var content= this.nextElementSibling;
		if(content.style.display==='block'){
			this.innerHTML = '(Ver descripcion..)'
			content.style.display = "none";

		}
		else{
			content.style.display = "block";
			this.innerHTML = '(Ocultar descripcion..)'
		}
	});
}

// var coll = document.getElementsByClassName("collapsible");
// var i;

// for (i = 0; i < coll.length; i++) {
//     coll[i].innerHTML = '(Ver Descripcion ..)';
//   	coll[i].addEventListener("click", function() {
//     var content = this.nextElementSibling;
//     if (content.style.display === "block") {
//     	this.innerHTML = '(Ver Descripcion ..)'
//       content.style.display = "none";
//     } else {
//       content.style.display = "block";
//     	this.innerHTML = '(Ocultar Descripcion ..)'
//     }
//   });
// }