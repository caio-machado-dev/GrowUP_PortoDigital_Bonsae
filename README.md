# GrowUP Porto Digital

![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=EM+DESENVOLVIMENTO&color=GREEN&style=for-the-badge)
 
## Pré-requesitos

Antes de começar, verifique se você tem os seguintes pré-requisitos instalados em seu ambiente:

- Git 
- Visual Studio Code (IDE)
- Python
- Django(Framework)

## Passo 01: Clonar o Repositório

- Clonar o repositório do projeto para a sua máquina local, atráves do PowerShell

```
git clone https://github.com/caio-machado-dev/GrowUP_PortoDigital_Bonsae.git
```

## Passo 02: Entrar na pasta do Projeto

```
cd GrowUP_PortoDigital_Bonsae
```

## Passo 03: Criar um ambiente virtual

```
python -m venv .venv
```

## Passo 04: Ativar o ambiente virtual

```
.venv\Scripts\activate
```

- Caso aconteça um erro ao executar o comando `.venv\Scripts\activate`, você pode habilitar a execução de scripts PowerShell com o comando `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` e tentar novamente.

## Passo 05: Instalar as dependências do Projeto

Com o ambiente virtual ativado, instale as dependências:

```
pip install -r requirements.txt

```

## Passo 06: Execute o Servidor

```
python .\manage.py runserver

```

## Passo 07: Acessar o Localhost no Navegador

**A URL ESTARÁ LOCALIZADA NO SEU TERMINAL**

