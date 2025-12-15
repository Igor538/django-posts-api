# 📝 Projeto Django + Django REST Framework
Projeto de exemplo utilizando Django e Django REST Framework, desenvolvido para demonstrar conceitos de CRUD, API REST, ambiente virtual e boas práticas no backend.


## ✨ Funcionalidades

- Criar, editar e remover posts/tarefas  
- Visualizar posts/tarefas recentes  
- API REST completa  
- Suporte a CORS  

---

## 🚀 Como Rodar o Projeto

### 1️⃣ Clonar o repositório direto no VS Code
```bash
git clone https://github.com/Igor538/django-posts-api.git
code django-posts-api
```
---

### 2️⃣ Criar e ativar o ambiente virtual
```bash
# Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1

# Windows (cmd)
python -m venv venv
.\venv\Scripts\activate

# Linux / Mac
python3 -m venv venv
source venv/bin/activate
```
---

### 3️⃣ Instalar as dependências
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```
---

### 4️⃣ 🔑 Gerar uma chave aleatória para o Django SECRET_KEY
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
# Copie o valor gerado e substitua a variável SECRET_KEY em settings.py
```
---

### 5️⃣ Ajustar o settings.py
```bash
No settings.py deixe DEBUG = True
```
---

### 6️⃣ Entrar na pasta do projeto
```bash
cd aula11
```
---

### 7️⃣ Executar as migrações
```bash
python manage.py migrate
```
---

### 8️⃣ Iniciar o servidor
```bash
python manage.py runserver
```
