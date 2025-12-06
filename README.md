Projeto de exemplo usando Django e Django REST Framework.

## Funcionalidades
- Criar, editar e remover posts
- Visualizar posts recentes
- API REST para posts

## Como rodar
1. Clone o repositório e entre na pasta:
```
git clone <URL_DO_REPOSITORIO>
cd aula11
```

2. Crie e ative o ambiente virtual:
```
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. Instale as dependências:
```
pip install -r requirements.txt
```

4. Rode as migrações e inicie o servidor:
```
python manage.py migrate
python manage.py runserver
```

5. Acesse no navegador:
- Frontend: [http://127.0.0.1:8000/inicio/](http://127.0.0.1:8000/inicio/)  
- API: [http://127.0.0.1:8000/api/posts/](http://127.0.0.1:8000/api/posts/)
