from flask import Flask, request, render_template, redirect, url_for, flash
import google.generativeai as genai
import os
from dotenv import load_dotenv
from PyPDF2 import PdfReader
import docx
import io

# Carrega as variáveis de ambiente com a chave da API
load_dotenv()
chave = os.getenv("API_KEY")
genai.configure(api_key=chave)

# Inicializa a aplicação Flask
app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Defina uma chave para os flash messages

# Função para extrair texto de arquivos PDF
def extract_text_from_pdf(file_stream):
    reader = PdfReader(file_stream)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Função para extrair texto de arquivos DOCX
def extract_text_from_docx(file_stream):
    doc = docx.Document(file_stream)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text
    return text

@app.route('/precorrecao', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Captura o texto do textarea
        fundamentacao_legal_js = request.form.get('fundamentacao_legal_js')

        # Captura o arquivo anexado
        file = request.files.get('file')

        # Verifica se o texto e o arquivo foram fornecidos
        if not fundamentacao_legal_js or not file:
            flash('É necessário fornecer a fundamentação legal e anexar um arquivo.', 'error')
            return redirect(url_for('index'))

        # Lê o conteúdo do arquivo com base no tipo de arquivo diretamente da memória
        if file.filename.endswith('.pdf'):
            arquivo_texto = extract_text_from_pdf(io.BytesIO(file.read()))
        elif file.filename.endswith('.docx'):
            arquivo_texto = extract_text_from_docx(io.BytesIO(file.read()))
        elif file.filename.endswith('.txt'):
            arquivo_texto = file.read().decode('utf-8')
        else:
            flash('Tipo de arquivo não suportado. Apenas PDF, DOCX e TXT são permitidos.', 'error')
            return redirect(url_for('index'))

        # Faz a requisição para a API GenAI para comparar o texto do arquivo e o do textarea
        model = genai.GenerativeModel("gemini-1.5-pro")
        prompt = f"Compare se o conteúdo do arquivo \n\nConteúdo do Arquivo: {arquivo_texto} está de acordo com a \n\nFundamentação Legal: {fundamentacao_legal_js}"
        response = model.generate_content(prompt)

        # Armazena a resposta da API
        genai_response = response.text

        # Redireciona para a página de resultados passando a resposta
        return render_template('result.html', genai_response=genai_response)

    return render_template('index.html')
