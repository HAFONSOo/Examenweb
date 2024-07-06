

let botones = document.querySelectorAll('.boton');

let precio = document.getElementsByName('precio');
/*
let boton = document.querySelector('.boton_prueba'),
texto = document.querySelector('.polla');
*/
/*
let tipo = document.getElementsByName('tipo').value;

var desde1 = document.getElementById('id_desde_alojamiento').value,
hasta1 = document.getElementById('id_hasta_alojamiento').value;

var desde = new Date(desde1), hasta = new Date(hasta1)


function diferencia(){
    texto.innerText = typeof(desde),' ',desde;
    console.log(desde)
}

boton.addEventListener('click', diferencia)

*/
/*
desde= request.POST['desde_alojamiento']
hasta=request.POST['hasta_alojamiento']
*/



for(let i=0; i<botones.length; i++){
    botones[i].addEventListener('click',function(){
        if(botones[i].innerText == 'Quitar'){
            botones[i].innerText = 'Agregar';
            botones[i].setAttribute('class',"btn btn-primary");
        }
        else{
            botones[i].innerText = 'Quitar';
            botones[i].setAttribute('class',"btn btn-danger");
        }
    })
}

