function analizarCoincidencias(mensaje){

    const reportes = JSON.parse(
        localStorage.getItem("reportesMascotas")
    ) || [];

    mensaje = mensaje.toLowerCase();

    let coincidencias = [];

    reportes.forEach(rep => {

        if(
            mensaje.includes(rep.color.toLowerCase()) ||
            mensaje.includes(rep.ubicacion.toLowerCase()) ||
            mensaje.includes(rep.tipo.toLowerCase())
        ){
            coincidencias.push(rep);
        }
    });

    if(coincidencias.length === 0){
        return `No encontré mascotas relacionadas.`;
    }

    let respuesta = "Coincidencias encontradas:<br><br>";

    coincidencias.forEach(rep => {

        respuesta += `
        <b>${rep.titulo}</b><br>
        📍 ${rep.ubicacion}<br>
        🎨 ${rep.color}<br>
        📞 ${rep.telefono}<br><br>
        `;
    });

    return respuesta;
}