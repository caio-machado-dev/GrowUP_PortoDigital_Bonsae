// Variável para controlar se o título e o textarea estão visíveis
let secaoFundamentacaoVisivel = false;

// Função para adicionar ou remover a seção "Fundamentação Legal"
function alternarSecaoFundamentacao() {
  const container = document.querySelector(".container-fluid.bg-white");
  const botao = document.querySelector(".btn-fundamentacao img");
  const uploadDiv = document.querySelector(".upload-container");

  if (!secaoFundamentacaoVisivel) {
    // Cria o título h6 com margem superior
    const tituloFundamentacao = document.createElement("h6");
    tituloFundamentacao.innerText = "Fundamentação Legal";
    tituloFundamentacao.setAttribute("id", "tituloFundamentacao");
    tituloFundamentacao.style.marginTop = "2vh"; // Adiciona margem superior

    // Cria o textarea
    const textarea = document.createElement("textarea");
    textarea.classList.add("form-control", "mt-2");
    textarea.setAttribute("id", "textareaFundamentacao");
    textarea.setAttribute("name", "fundamentacao_legal_js")
    textarea.setAttribute("rows", "10");
    textarea.setAttribute("placeholder", "Digite a Fundamentação Legal");
    textarea.style.resize = "none"; // Altura fixa

    // Adiciona o título e textarea ao container
    container.appendChild(tituloFundamentacao);
    container.appendChild(textarea);
    container.appendChild(uploadDiv);

    botao.src = removeIconUrl;

    secaoFundamentacaoVisivel = true;
  } else {
    // Remove o título e textarea se já estiverem visíveis
    const tituloFundamentacao = document.getElementById("tituloFundamentacao");
    const textarea = document.getElementById("textareaFundamentacao");

    if (tituloFundamentacao) tituloFundamentacao.remove();
    if (textarea) textarea.remove();

    const originalParent = document.querySelector(".original-upload-location");
    originalParent.appendChild(uploadDiv);

    botao.src = addIconUrl;
    secaoFundamentacaoVisivel = false;
  }
}

// Adiciona o evento de clique ao botão "Adicionar Fundamentação"
document
  .querySelector(".btn-fundamentacao")
  .addEventListener("click", alternarSecaoFundamentacao);
