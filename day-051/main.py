# Enunciado do exercício (async basics)
# Crie a pasta day-051 com main.py. O programa deve demonstrar a diferença de tempo entre síncrono e assíncrono:

# Uma função sync_task(name, seconds) síncrona que imprime que começou, usa time.sleep(seconds), e imprime que terminou.
# Uma corotina async_task(name, seconds) assíncrona que faz o mesmo, mas com await asyncio.sleep(seconds).
# Uma parte síncrona que roda 3 tarefas em sequência e mede o tempo total (use time.perf_counter() antes e depois). Deve dar ~3 segundos.
# Uma corotina main() que roda as 3 tarefas assíncronas com asyncio.gather e mede o tempo total. Deve dar ~1 segundo.
# Imprima os dois tempos, mostrando que o assíncrono foi ~3x mais rápido pro mesmo trabalho (porque era só espera).
import time
import asyncio

def sync_task(name: str, seconds: int) -> None:
    print(f"time's started {name}")
    time.sleep(seconds)
    print(f"time's finished {name}")

async def async_task(name: str, seconds: int) -> None:
    print(f"time's started {name}")
    await asyncio.sleep(seconds)
    print(f"time's finished {name}")

start = time.perf_counter()
sync_task("lucas", 2)
sync_task("isabella", 3)
sync_task("laura", 4)
finish = time.perf_counter()
print(finish - start)


async def main():
    await asyncio.gather(async_task("lucas", 2), async_task("isabella", 3),async_task("laura", 4))

async_start = time.perf_counter()
asyncio.run(main())
async_finish = time.perf_counter()
print(async_finish - async_start)