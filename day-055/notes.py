# Day 55 - paper practice (async + celery), no PC
# Part 1 - async/await
import asyncio


async def fetch_data(name, seconds):
    print(f"task {name} has started")
    await asyncio.sleep(seconds)
    print(f"task {name} has finished")


async def main():
    response = await asyncio.gather(
        fetch_data("uncle ze", 3),
        fetch_data("aunt beth", 4),
        fetch_data("mom silvana", 5)
    )

asyncio.run(main())


# Part 2 - Celery with Redis
import time
from celery import Celery

app = Celery(
    "tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)


@app.task
def send_mail(to, subject):
    time.sleep(3)
    print(f"Mail was sent to {to} about {subject}")


result = send_mail.delay("laura", "I miss you")

print(result.id)
print(result.get())

