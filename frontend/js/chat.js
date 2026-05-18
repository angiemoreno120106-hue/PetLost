function enviarMensaje(){

    const input = document.getElementById("mensaje-input");

    const chatBox = document.getElementById("chat-box");

    const mensaje = input.value;

    if(!mensaje) return;

    chatBox.innerHTML += `
        <div class="mensaje usuario">
            ${mensaje}
        </div>
    `;

    const respuestaIA = analizarCoincidencias(mensaje);

    setTimeout(() => {

        chatBox.innerHTML += `
            <div class="mensaje ia">
                ${respuestaIA}
            </div>
        `;

        chatBox.scrollTop = chatBox.scrollHeight;

    }, 800);

    input.value = "";
}