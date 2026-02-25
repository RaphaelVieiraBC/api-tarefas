# API de Tarefas - CRUD completo com FastAPI
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Tarefa(BaseModel):
    titulo: str
    descricao: str | None = None


banco_dados = []


@app.get("/")
def root():
    return {"mensagem": "API de Tarefas Ativa!"}


@app.post("/tarefas")
async def criar_tarefa(tarefa: Tarefa):
    nova_tarefa = {
        "id": len(banco_dados) + 1,
        "titulo": tarefa.titulo,
        "descricao": tarefa.descricao,
    }
    banco_dados.append(nova_tarefa)
    return {"mensagem": "Tarefa criada", "detalhes": nova_tarefa}


@app.get("/tarefas")
async def listar_tarefas():
    return banco_dados


@app.get("/tarefas/{tarefa_id}")
async def buscar_tarefa(tarefa_id: int):
    for tarefa in banco_dados:
        if tarefa["id"] == tarefa_id:
            return tarefa
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")


@app.put("/tarefas/{tarefa_id}")
async def atualizar_tarefa(tarefa_id: int, tarefa_atualizada: Tarefa):
    for tarefa in banco_dados:
        if tarefa["id"] == tarefa_id:
            tarefa["titulo"] = tarefa_atualizada.titulo
            tarefa["descricao"] = tarefa_atualizada.descricao
            return {"mensagem": "Tarefa atualizada", "item": tarefa}
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")


@app.delete("/tarefas/{tarefa_id}")
async def deletar_tarefa(tarefa_id: int):
    for i, tarefa in enumerate(banco_dados):
        if tarefa["id"] == tarefa_id:
            removida = banco_dados.pop(i)
            return {"mensagem": "Tarefa removida", "item": removida}
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")
