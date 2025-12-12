# 📝 Projeto Django + Django REST Framework

Projeto de exemplo utilizando **Django** e **Django REST Framework**, desenvolvido para demonstrar conceitos de CRUD, API REST, ambiente virtual, uso de variáveis de ambiente e boas práticas no backend.

---

## ✨ Funcionalidades
- ✔ Criar, editar e remover posts/tarefas  
- ✔ Visualizar posts/tarefas recentes  
- ✔ API REST completa  
- ✔ Suporte a CORS  
- ✔ Estrutura limpa e organizada  
- ✔ Deploy facilmente configurável  

---

## 🚀 Como Rodar o Projeto

### 1️⃣ Clone o repositório
```bash
git clone https://github.com/seu-usuario/aula12.git
cd aula12
```

### 2️⃣ Crie e ative o ambiente virtual

**Windows (PowerShell):**
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Windows (cmd):**
```bash
python -m venv venv
.\venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Instale as dependências
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

## 🔐 4️⃣ Gerar SECRET_KEY e criar o `.env` (seguro)

### Gerar SECRET_KEY com Django:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Criar `.env` automaticamente

**Linux/macOS:**
```bash
cat > .env <<EOF
SECRET_KEY=cole_sua_chave_aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
EOF
```

**Windows (PowerShell):**
```powershell
"SECRET_KEY=cole_sua_chave_aqui" > .env
"DEBUG=True" >> .env
"ALLOWED_HOSTS=localhost,127.0.0.1" >> .env
"DATABASE_URL=sqlite:///db.sqlite3" >> .env
```

> **Importante:** Adicione o `.env` ao `.gitignore`  
```bash
echo ".env" >> .gitignore
```

---

## ⚙️ 5️⃣ Execute as migrações
```bash
python manage.py migrate
```

## ▶️ 6️⃣ Inicie o servidor
```bash
python manage.py runserver
```
