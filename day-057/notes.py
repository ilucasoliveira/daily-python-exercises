# Day 57 - paper practice: WebSocket with multiple clients (broadcast)
# send_text responde so para quem mandou.
# broadcast manda para todos os conectados - e o que faz um chat de verdade.

from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()


class ConnectionManager:
    def __init__(self):
        self.active_connections = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()


@app.websocket("/ws")
async def chat(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"someone said: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast("a user left the chat")
