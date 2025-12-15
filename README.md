# 📝 Projeto Django + Django REST Framework

Projeto de exemplo utilizando Django e Django REST Framework, desenvolvido para demonstrar conceitos de CRUD, API REST, ambiente virtual e boas práticas no backend.

## ✨ Funcionalidades

✔ Criar, editar e remover posts/tarefas  
✔ Visualizar posts/tarefas recentes  
✔ API REST completa  
✔ Suporte a CORS  
✔ Estrutura limpa e organizada  

## 🚀 Como Rodar o Projeto

1️⃣ **Clonar o repositório direto no VS Code**

```bash
git clone https://github.com/Igor538/django-posts-api.git
code django-posts-api
```

2️⃣ **Criar e ativar o ambiente virtual**

**Windows (PowerShell):**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Windows (cmd):**

```cmd
python -m venv venv
.\venv\Scripts\activate
```

**Linux/Mac:**

```bash
python3 -m venv venv
source venv/bin/activate
```

3️⃣ **Instalar as dependências**

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

4️⃣ **Entrar na pasta do projeto**

```bash
cd aula11
```

5️⃣ **Ajustar o `settings.py`**

> Certifique-se de que `DEBUG=True` para desenvolvimento.

6️⃣ **Executar as migrações**

```bash
python manage.py migrate
```

7️⃣ **Iniciar o servidor de desenvolvimento**

```bash
python manage.py runserver
```
