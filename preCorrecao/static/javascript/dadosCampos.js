async function carregarDados() {
  try {
    // Carrega o JSON da pasta json
    const resposta = await fetch('/static/json/estados-cidades.json');
    const { estados } = await resposta.json();

    const estadoSelect = document.getElementById('estadoSelect');
    const cidadeSelect = document.getElementById('cidadesSelect');

    // Preenche o select de estados com as siglas e nomes
    estados.forEach(estado => {
      const option = document.createElement('option');
      option.value = estado.sigla;  // Usamos a sigla como valor
      option.textContent = `${estado.sigla}`;
      estadoSelect.appendChild(option);
    });

    // Adiciona evento para exibir as cidades ao selecionar a sigla do estado
    estadoSelect.addEventListener('change', function () {
      const siglaSelecionada = this.value;

      // Encontra o estado correspondente pela sigla
      const estadoSelecionado = estados.find(
        estado => estado.sigla === siglaSelecionada
      );

      // Limpa as opções de cidades
      cidadeSelect.innerHTML = '<option value="">Selecione uma cidade</option>';

      // Habilita o select de cidades se um estado foi selecionado
      cidadeSelect.disabled = !estadoSelecionado;

      if (estadoSelecionado) {
        estadoSelecionado.cidades.forEach(cidade => {
          const option = document.createElement('option');
          option.value = cidade;
          option.textContent = `Comarca ${cidade}`;
          cidadeSelect.appendChild(option);
        });
      }
    });
  } catch (erro) {
    console.error('Erro ao carregar o JSON:', erro);
  }
}

// Chama a função ao carregar a página
carregarDados();


// Enviar JSON e Receber resposta da IA
const form = document.querySelector('form');
form.addEventListener('submit', async (e) => {
  e.preventDefault();

  const formData = new FormData(form);

  const jsonData = {
    estadoCompetencia: document.getElementById('estadoSelect').value,
    competencia: document.getElementById('cidadesSelect').value,
    segredo: document.getElementById("segredo").value,
    parteContraria: document.getElementById('parteContraria').value,
    tipo: document.getElementById("tipo").value,
    fundamentacaoLegal: document.getElementById('textareaFundamentacao')?.value || ''
  };

  formData.append('json_data', JSON.stringify(jsonData));

  try {
    const response = await fetch(form.action, {
      method: 'POST',
      body: formData,
      headers: {
        'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
      }
    });

    if (!response.ok){
      const errorData = await response.json()
      console.error("Erro da API", errorData.error)
      alert(`Erro: ${errorData.error}`)
      return;
    }

    const result = await response.json();
    console.log('Resposta do servidor:', result);

    // Exibe apenas o texto da resposta no HTML
    const responseContent = document.getElementById('responseContent');
    responseContent.textContent = result.resultado;

    // Torna o container visível
    const responseContainer = document.getElementById('responseContainer');
    responseContainer.style.visibility = 'visible';
    responseContainer.style.display = 'block';

  } catch (error) {
    console.error('Erro na requisição:', error);
    alert('Ocorreu um erro na comunicação com o servidor.');
  }
});

