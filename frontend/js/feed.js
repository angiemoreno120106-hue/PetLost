function cargarReportesFeed(){

    const contenedor = document.getElementById("grid-reportes-comunitarios");

    const reportes = JSON.parse(
        localStorage.getItem("reportesMascotas")
    ) || [];

    if(reportes.length === 0){

        contenedor.innerHTML = `
            <h3>No existen reportes activos</h3>
        `;

        return;
    }

    contenedor.innerHTML = "";

    reportes.reverse().forEach(reporte => {

        const tarjeta = `
        <div class="pet-card"
             onclick='abrirDetallesMascota(${JSON.stringify(reporte)})'>

            <div class="pet-img-container">
                ${reporte.foto}
            </div>

            <div class="pet-card-content">
                <h3>${reporte.titulo}</h3>

                <p>📍 ${reporte.ubicacion}</p>
                <p>🎨 ${reporte.color}</p>
                <p>📞 ${reporte.telefono}</p>
            </div>
        </div>
        `;

        contenedor.innerHTML += tarjeta;
    });
}

function abrirDetallesMascota(reporte){

    document.getElementById("modalDetalles").style.display = "flex";

    document.getElementById("modal-img-container").innerHTML = reporte.foto;

    document.getElementById("modal-titulo").innerText = reporte.titulo;

    document.getElementById("modal-descripcion").innerText = reporte.descripcion;

    document.getElementById("modal-contacto").innerText = reporte.telefono;
}