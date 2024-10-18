// Função para limpar todos os campos do formulário
function limparCampos() {
    // Seleciona todos os inputs e selects do formulário
    const inputs = document.querySelectorAll("input[type='text']");
    const selects = document.querySelectorAll("select");
  
    // Limpa todos os inputs
    inputs.forEach(input => input.value = '');
  
    // Restaura os selects para a primeira opção (geralmente a "Selecione")
    selects.forEach(select => select.selectedIndex = 0);
  }
  
  // Adiciona o evento de clique no botão de "Limpar Seção"
  document.querySelector(".btn-limpar").addEventListener("click", function(event) {
    event.preventDefault(); // Impede o envio do formulário
    limparCampos(); // Chama a função para limpar os campos
  });
  