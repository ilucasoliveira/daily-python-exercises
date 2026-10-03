# Day 56 - paper practice: WebSockets (concept)
# HTTP normal: pergunta e resposta, conexao fecha.
# WebSocket: linha aberta, os dois falam quando quiserem.

from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()


# Echo simples
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"you said: {data}")


# Echo em maiusculas, com tratamento de desconexao
@app.websocket("/chat")
async def websocket_chat(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"ECHO: {data.upper()}")
    except WebSocketDisconnect:
        print("client disconnected")
