# Day 58 - paper practice: cycle review (async, celery, websocket) + CI/CD intro

# ==========================================================
# PART 1 - key lines from memory
# ==========================================================

# --- Async: run coroutines in parallel ---
import asyncio

async def main():
    await asyncio.gather(coro1(), coro2(), coro3())


# --- Celery: dispatch a task to run in background ---
from celery import Celery

app = Celery(
    "tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

@app.task
def sum_number(x, y):
    return x + y

# .delay() dispatches to the queue WITHOUT await (Celery is not awaitable)
result = sum_number.delay(5, 9)


# --- WebSocket: send a message to a connected client ---
# from fastapi import WebSocket

@app.websocket("/chat")
async def chat(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(data)


# ==========================================================
# PART 2 - CI/CD with GitHub Actions
# ==========================================================
# File path: .github/workflows/test.yml
#
# name: Tests
#
# on: [push]
#
# jobs:
#   test:
#     runs-on: ubuntu-latest
#     steps:
#       - uses: actions/checkout@v4
#       - name: Set up Python
#         uses: actions/setup-python@v5
#         with:
#           python-version: "3.12"
#       - name: Install dependencies
#         run: pip install -r requirements.txt
#       - name: Run tests
#         run: pytest
#
# On every push, GitHub spins up a Linux machine, checks out the code,
# installs Python and dependencies, and runs pytest. Green if tests pass,
# red if they fail. It prevents broken code from going unnoticed.
