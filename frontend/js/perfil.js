function renderizarMisReportes(){

    const contenedor = document.getElementById("mis-reportes-lista");

    const usuario = JSON.parse(localStorage.getItem("usuarioActivo"));

    const reportes = JSON.parse(
        localStorage.getItem("reportesMascotas")
    ) || [];

    const misReportes = reportes.filter(
        r => r.userId === usuario.id
    );

    contenedor.innerHTML = "";

    misReportes.forEach(reporte => {

        contenedor.innerHTML += `
        <div class="pet-card">
            ${reporte.foto}
            <h3>${reporte.titulo}</h3>
            <button onclick="eliminarReporte('${reporte.id}')">
                ELIMINAR
            </button>
        </div>
        `;
    });
}

function eliminarReporte(id){

    let reportes = JSON.parse(
        localStorage.getItem("reportesMascotas")
    ) || [];

    reportes = reportes.filter(r => r.id != id);

    localStorage.setItem(
        "reportesMascotas",
        JSON.stringify(reportes)
    );

    renderizarMisReportes();
}