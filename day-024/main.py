# 3. Enunciado do exercício (post with validation)

# Crie day-024/main.py. Importe FastAPI e BaseModel. O programa deve:

# Criar um modelo Pydantic (herdando de BaseModel) representando algo a seu critério (exemplo: User com name, email, age), com pelo menos 3 campos tipados
# Uma rota POST que receba esse modelo no corpo e retorne os dados recebidos numa resposta JSON (pode adicionar uma mensagem tipo "created")
# Uma rota GET em / simples de boas-vindas
# Testar enviando dados válidos e ver a resposta, e enviar dados inválidos (faltando campo ou tipo errado) pra ver a validação automática recusar

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

list_users = []

class User(BaseModel):
    name: str
    email: EmailStr
    age: int

app = FastAPI()

@app.post("/users", status_code=201)
def create_user(user: User):
    
    new_user = user.model_dump()
    list_users.append(new_user)
    
    return {"created": new_user}

@app.get("/")
def greeting():
    return {"message":"Welcome"}