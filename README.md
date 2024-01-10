# 📒 Agenda em Django

Agenda eletrônica feita em Python utilizando o framework Django. É utilizada como um sistema para a criação, edição e remoção de contatos que são armazenados em uma base de dados SQLite e gerenciados por um owner (usuário) logado na agenda.

> Status do Projeto: ✔️ (concluído)

## 🔧 Tecnologias utilizadas
Python V.: 3.11.1 || Django V.: 4.2.5 || SQLite || Whitenoise V.: 6.6.0

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
* Faça as migrações com o comando abaixo:
  ```bash
  python manage.py migrate
  ```

* Execute o seguinte comando para iniciar o servidor:
  ```bash
  python manage.py runserver
  ```

* Em um navegador de sua preferência, pesquise pelo endereço <code>127.0.0.1:8000</code> para ser redirecionado para a agenda.
* Crie seu usuário clicando em "Register" e preencha suas informações.
* Comece a criar seus contatos!

## 🔓 Bônus (acessando o admin)
* Crie um superusuário no seu terminal com <code>python manage.py createsuperuser</code>.
* Se estiver com uma conta logada na agenda, faça o logout.
* Acesse o painel admin no seu navegador com <code>127.0.0.1:8000/admin</code> e faça login com o superusuário que você acabou de criar.
* Agora, como administrador, você pode analisar as models, seus campos e todos os dados em funcionamento, bem como manipulá-los da forma que desejar.
