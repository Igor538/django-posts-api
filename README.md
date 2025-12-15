📝 Projeto Django + Django REST Framework
Projeto de exemplo utilizando Django e Django REST Framework, desenvolvido para demonstrar conceitos de CRUD, API REST, ambiente virtual e boas práticas no backend.

✨ Funcionalidades
✔ Criar, editar e remover posts/tarefas
✔ Visualizar posts/tarefas recentes
✔ API REST completa
✔ Suporte a CORS
✔ Estrutura limpa e organizada

🚀 Como Rodar o Projeto
1️⃣ Clonar o repositório direto no VS Code

git clone https://github.com/Igor538/django-posts-api.git
code django-posts-api

2️⃣ Criar e ativar o ambiente virtual

Windows (PowerShell):

python -m venv venv
.\venv\Scripts\Activate.ps1

Windows (cmd):

python -m venv venv
.\venv\Scripts\activate

Linux/Mac:

python3 -m venv venv
source venv/bin/activate

3️⃣ Instalar as dependências

python -m pip install --upgrade pip
pip install -r requirements.txt

4️⃣ Entrar na pasta do projeto

cd aula11

🗝  Gerar uma chave aleatória para o Django SECRET_KEY

No terminal do VS Code, rode:

python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

Copie o valor gerado e substitua a variável `SECRET_KEY` em `settings.py`.

5️⃣ Ajustar o settings.py

Certifique-se de que DEBUG=True para desenvolvimento.

6️⃣ Executar as migrações

python manage.py migrate

7️⃣ Iniciar o servidor de desenvolvimento

python manage.py runserver
