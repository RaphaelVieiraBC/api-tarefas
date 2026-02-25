# api-tarefas
API REST de CRUD de tarefas construída com **FastAPI**.
# 📝 API de Tarefas

API REST de CRUD de tarefas construída com **FastAPI**.

## 🚀 Como rodar

**1. Clone o repositório:**
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

**2. Instale as dependências:**
pip install -r requirements.txt

**3. Inicie o servidor:**
uvicorn main:app --reload

**4. Acesse a documentação interativa:**
http://127.0.0.1:8000/docs

## 📌 Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/tarefas` | Lista todas as tarefas |
| GET | `/tarefas/{id}` | Busca tarefa por ID |
| POST | `/tarefas` | Cria uma nova tarefa |
| PUT | `/tarefas/{id}` | Atualiza uma tarefa |
| DELETE | `/tarefas/{id}` | Remove uma tarefa |
