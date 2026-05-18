const API_BASE_URL = "http://localhost:8000";

function registrarUsuario(nombre, email, telefono, password){

    let usuarios = JSON.parse(localStorage.getItem("usuarios_petlost")) || [];

    email = email.toLowerCase().trim();

    if(usuarios.find(u => u.email === email)){
        throw new Error("El usuario ya existe");
    }

    const nuevoUsuario = {
        id: Date.now(),
        name: nombre,
        email,
        phone: telefono,
        password,
        role: email.includes("admin") ? "admin" : "user"
    };

    usuarios.push(nuevoUsuario);

    localStorage.setItem(
        "usuarios_petlost",
        JSON.stringify(usuarios)
    );

    return nuevoUsuario;
}

function iniciarSesion(email, password){

    let usuarios = JSON.parse(localStorage.getItem("usuarios_petlost")) || [];

    const usuario = usuarios.find(
        u => u.email === email && u.password === password
    );

    if(!usuario){
        throw new Error("Credenciales incorrectas");
    }

    localStorage.setItem(
        "usuarioActivo",
        JSON.stringify(usuario)
    );

    localStorage.setItem(
        "token",
        "local-jwt-" + btoa(email)
    );

    return usuario;
}

function cerrarSesion(){
    localStorage.removeItem("usuarioActivo");
    localStorage.removeItem("token");
}