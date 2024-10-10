function validadorArquivo() {
    const fileInput = document.getElementById("inputFile");
    const filePath = fileInput.value;
    const allowedExtensions = /(\.pdf|\.docx|\.txt)$/i;

    if (!allowedExtensions.exec(filePath)) {
        Swal.fire({
            icon: "error",
            title: "Arquivo inválido!",
            text: "O arquivo anexado não é permitido. Apenas PDF, DOCX e TXT são suportados.",
        });
        fileInput.value = "";
        return false;
    }
    return true;
}
