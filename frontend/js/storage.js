function obtenerUsuarios(){
    return JSON.parse(localStorage.getItem("usuarios_petlost")) || [];
}

function guardarUsuarios(lista){
    localStorage.setItem("usuarios_petlost", JSON.stringify(lista));
}

function obtenerReportes(){
    return JSON.parse(localStorage.getItem("reportesMascotas")) || [];
}

function guardarReportes(lista){
    localStorage.setItem("reportesMascotas", JSON.stringify(lista));
}