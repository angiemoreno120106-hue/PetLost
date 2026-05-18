class ReporteMascota {

    constructor(
        titulo,
        estado,
        tipo,
        color,
        ubicacion,
        descripcion,
        foto,
        telefono
    ) {

        this.id =
            "rep_" + Date.now();

        this.userId =
            localStorage.getItem("userIdActual");

        this.titulo = titulo;
        this.estado = estado;
        this.tipo = tipo;
        this.color = color;
        this.ubicacion = ubicacion;
        this.descripcion = descripcion;
        this.foto = foto;
        this.telefono = telefono;

        this.fecha =
            new Date().toLocaleDateString();
    }

    validar() {

        if (
            !this.titulo ||
            !this.descripcion ||
            !this.telefono
        ) {
            throw new Error(
                "Todos los campos son obligatorios."
            );
        }

        if (this.telefono.length < 7) {
            throw new Error(
                "Número telefónico inválido."
            );
        }
    }

    obtenerObjeto() {

        return {
            id: this.id,
            userId: this.userId,
            titulo: this.titulo,
            estado: this.estado,
            tipo: this.tipo,
            color: this.color,
            ubicacion: this.ubicacion,
            descripcion: this.descripcion,
            foto: this.foto,
            telefono: this.telefono,
            fecha: this.fecha
        };
    }
}