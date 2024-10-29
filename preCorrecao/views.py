from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, JsonResponse, HttpResponseBadRequest
from django.conf import settings
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
# from openai import OpenAI
import google.generativeai as genai
import os
from dotenv import load_dotenv
from PyPDF2 import PdfReader
import docx
import io
import json

# client = OpenAI()
# Carregar a variável de Ambiente
load_dotenv()
chave = os.getenv("API_KEY")
genai.configure(api_key=chave)
if not chave:
    raise ValueError("Chave da API Gemini não encontrada")

# Extrair textos de arquivos PDF
def extract_text_from_pdf(file_stream):
    reader = PdfReader(file_stream)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def extract_text_from_docx(file_stream):
    doc = docx.Document(file_stream)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text
    return text

@csrf_exempt
def precorrecao_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.POST.get('json_data'))
            # print("Dados recebidos:", data)
        except json.JSONDecodeError:
            return HttpResponseBadRequest("Erro: JSON inválido")

        file = request.FILES.get('file')
        
        if file.name.endswith('.pdf'):
            arquivo_texto = extract_text_from_pdf(io.BytesIO(file.read()))
        elif file.name.endswith('.docx'):
            arquivo_texto = extract_text_from_docx(io.BytesIO(file.read()))
        elif file.name.endswith('.txt'):
            arquivo_texto = file.read().decode('utf-8')
        else:
            return JsonResponse({"error": "Nenhum arquivo foi anexado"}, status=400)

        prompt = (
            "De acordo com os dados presentes no arquivo JSON abaixo, "
            "compare com o arquivo anexado e corrija com base nos principais "
            "requisitos de uma petição inicial.\n\n"
            f"Dados do JSON: {json.dumps(data, indent=4)}\n\n" 
            f"Conteúdo do Arquivo: {arquivo_texto}"
            "Trate essa correção como se fosse um professor. Apenas traga sua análise"
            # Melhorar o prompt / OBS: Passar mais informações específicas
        )
        
        try:
            model = genai.GenerativeModel("gemini-1.5-pro")
            response = model.generate_content(prompt)
            genai_response = response.text
            # print(genai_response)
            # client.api_key = chave
            # response = client.chat.completions.create(
            #     model="gpt-3.5-turbo",
            #     messages=[
            #         {"role": "system", "content": "Você é um professor de Direito"},
            #         {"role": "user", "content": prompt}
            #     ],
            #     temperature=1,
            #     timeout=60
            # )
            
            # print("Resposta Completa da API", response)
        
            # chatgpt_response = json.loads( response.model_dump_json())['choices'][0]['message']['content']
            # print("Resposta da IA:", chatgpt_response)
            
            # if "choices" in resposta and len(resposta.choices) > 0:
            #     chatgpt_response = resposta.choices[0].message['content']
            #     print("Resposta da IA:", chatgpt_response)
            # else:
            #     return JsonResponse({"error": "Resposta inesperada da API"}, status=500)
        except Exception as e:
            return JsonResponse({"error": f"Erro inesperado: {str(e)}"}, status=500)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Erro ao decodificar JSON"}, status=400)
        # Retorna a resposta da IA para o front-end
        return JsonResponse({"resultado": genai_response})
        # return JsonResponse({"resultado": genai_response})
    
    return render(request, "preCorrecao/formulario.html")
