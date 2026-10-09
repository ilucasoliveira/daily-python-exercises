# revisão de logging + WebSocket
# Objetivo: remontar o chat WebSocket de memória (sem abrir o day-060) e encaixar logging em cada evento. Dois exercícios num arquivo só.

# Exercício 1: o chat que registra tudo
# Cria day-061/main.py. Monta o ConnectionManager e a rota de novo, de cabeça. A novidade é logging em três pontos:
# no connect: depois do accept(), um logger.info avisando que um cliente entrou
# na rota, quando chega mensagem: um logger.info com o conteúdo recebido
# no disconnect (quando cai no WebSocketDisconnect): um logger.warning avisando que um cliente saiu
# Começa pelo topo do arquivo: o setup do logging (aquele basicConfig com level e format, mais o getLogger). Você fez isso no Bloco 1 ontem, tenta de memória.

# Exercício 2 (o segundo, que vale o review): contagem de conectados
# Faz cada log mostrar quantos clientes estão conectados naquele momento. Dica: a informação já está no self.active_connections. Pensa em como contar os itens de uma lista.
# Resultado esperado: você abre duas abas em http://localhost:8000, manda mensagem, ela aparece nas duas (WebSocket funcionando),
# e no terminal do uvicorn aparecem os logs com timestamp e a contagem subindo/descendo conforme abre e fecha aba.
# Pontos que eu quero te ver acertar sem ajuda (são os teus erros recorrentes):
import logging
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger()

class ConnectionManager:
    def __init__(self) -> None:
        self.active_connections = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        logger.info("a user got in the chat")
        self.active_connections.append(websocket)
        logger.info(f"users' quantity: {len(self.active_connections)}")

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)
        logger.info(f"users' quantity: {len(self.active_connections)}")
        logger.warning("a user left the chat")

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

@app.get("/")
async def get():
    from fastapi.responses import FileResponse
    return FileResponse("index.html")


@app.websocket("/chat")
async def chat(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            logger.info(data)
            await manager.broadcast(f"someone said: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast("a user left the chat")
