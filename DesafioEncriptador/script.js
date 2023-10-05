function encriptar() {

    // Reemplazar los patrones encriptados con sus letras correspondientes
    var texto = document.getElementById("texto").value;
    var resultado = texto;
    
    resultado = resultado.replace(/e/g, 'enter');
    resultado = resultado.replace(/i/g, 'imes');
    resultado = resultado.replace(/a/g, 'ai');
    resultado = resultado.replace(/o/g, 'ober');
    resultado = resultado.replace(/u/g, 'ufat');

    document.getElementById("resultado").value = resultado;
}

function desencriptar() {
    var texto = document.getElementById("texto").value;
    var resultado = texto;

    // Reemplazar los patrones encriptados con sus letras correspondientes
    resultado = resultado.replace(/enter/g, 'e');
    resultado = resultado.replace(/imes/g, 'i');
    resultado = resultado.replace(/ai/g, 'a');
    resultado = resultado.replace(/ober/g, 'o');
    resultado = resultado.replace(/ufat/g, 'u');

    document.getElementById("resultado").value = resultado;
}

function copiarResultado() {

    //limpia las secciones de resultado e introducir texto y lo copia en el porta papeles
    var resultado = document.getElementById("resultado").value;
    navigator.clipboard.writeText(resultado);
    document.getElementById("texto").value = resultado;
    document.getElementById("resultado").value = "";
}
