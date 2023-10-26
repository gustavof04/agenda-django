# 📒 Agenda em Django

Agenda eletrônica feita em Python utilizando o framework Django. É utilizada como um sistema para a criação, edição e remoção de contatos que são armazenados em uma base de dados SQLite e gerenciados por um owner (usuário) logado na agenda.

## 🔧 Tecnologias utilizadas
Python V.: 3.11.1 || Django V.: 4.2.5

OBS.: É obrigatória a instalação manual do Python na versão citada acima para ser possível a criação do ambiente virtual e instalação das dependências do projeto.

- Windows 8+

https://www.python.org/ftp/python/3.11.1/python-3.11.1-amd64.exe

- macOS 10.9+

https://www.python.org/ftp/python/3.11.1/python-3.11.1-macos11.pkg

## ⚙️ Configurando o ambiente virtual
* No seu terminal, navegue até a pasta raiz do projeto e execute o seguinte comando para criar um ambiente virtual:

  ```bash
  python -m venv nome_da_virtualenv
  ```

* Rode o comando de acordo com seu sistema para ativar seu ambiente virtual:

  Windows
  ```bash
  .\nome_da_virtualenv\Scripts\activate
  ```

  Linux ou macOS
  ```bash
  source nome_da_virtualenv/bin/activate
  ``` 

## 🧑‍🔬 Instalando as dependências
* Com o ambiente virtual **ativado**, instale as dependências do projeto com o seguinte comando:

  ```bash
  pip install -r requirements.txt
  ```

## 🚀 Iniciando a agenda
* Faça as migrations com o comando abaixo:
  ```bash
  python manage.py migrate
  ```

* Execute o seguinte comando para iniciar o servidor:

  ```bash
  python manage.py runserver
  ```

* Clique segurando CTRL/Command no endereço localhost de sua máquina para ser redirecionado à agenda.
* Crie seu usuário clicando em "Register".
* Comece a criar seus contatos!

