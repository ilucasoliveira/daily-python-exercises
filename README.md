# Daily Python Exercises

![Tests](https://github.com/ilucasoliveira/daily-python-exercises/actions/workflows/tests.yml/badge.svg)

Daily hands-on exercises to sharpen my Python fundamentals and back-end skills. The goal is one exercise per day, each small enough to finish in 20 to 40 minutes, with at least one commit to keep a steady learning habit.

## How it works

Each day lives in its own folder (`day-001`, `day-002`, and so on). A day is self-contained: enter the folder and run its main file. Review days revisit earlier topics and combine them into a single, larger exercise.

The weekly rhythm mixes Python fundamentals with practical back-end tools: several days of core Python, then FastAPI, Docker, databases, and a review day that ties the week together.

## Topics covered

### Python fundamentals

- **day-001** - Strings and slicing (`[start:stop:step]`, negative step, palindromes)
- **day-002** - List basics and methods (`append`, `insert`, `remove`, indexing)
- **day-003** - Dictionary basics (keys, values, updating, iterating with `.items()`)
- **day-004** - Sets and operations (deduplication, intersection, union)
- **day-007** - Refactoring into reusable functions (`return` vs `print`) + integrated review
- **day-008** - List comprehensions (transforms and filters)
- **day-009** - Dict comprehensions (key/value transforms with filters)
- **day-010** - `*args` and `**kwargs` (variable arguments) + review
- **day-011** - Variable scope (local vs global)
- **day-014** - Integrated review: comprehensions, `*args`, `**kwargs` and scope
- **day-015** - Reading and writing text files (`with`, read/write/append modes)
- **day-016** - Working with JSON (`json.dump` / `json.load`, preserving types)
- **day-017** - Reading and writing CSV (`DictReader` / `DictWriter`)
- **day-018** - Error handling with `try` / `except` (specific exceptions)
- **day-019** - Working with dates and times (`datetime`, `strftime`, `timedelta`)
- **day-020** - Modules and imports (splitting code across files)
- **day-021** - Integrated review: an expense tracker combining JSON, datetime, error handling and modules
- **day-022** - Object-oriented programming: classes, objects, `__init__`, `self`
- **day-023** - Inheritance and `super()` (plus method overriding and polymorphism)
- **day-026** - Generators and `yield` (lazy evaluation, generator pipelines)
- **day-027** - Decorators (wrapping functions with `*args` / `**kwargs`)
- **day-028** - Integrated review: an inventory system combining OOP, generators and decorators
- **day-029** - Context managers (`@contextmanager`, `yield`, `try` / `finally`)
- **day-030** - Type hints (parameters, returns, `list[]` / `dict[]`, `Optional`)
- **day-031** - Advanced type hints (`Union`, type aliases, `Callable`)
- **day-036** - Consuming external APIs with `requests` (status codes, JSON, error handling)
- **day-037** - Requests with POST, headers and query params
- **day-038** - Environment variables with `.env` (`python-dotenv`, keeping secrets out of git)
- **day-059** - Logging (levels, `basicConfig`, structured log messages)

### Testing

- **day-032** - First tests with pytest (`assert`, test discovery, edge cases)
- **day-033** - Testing exceptions (`pytest.raises`, `raise`) and parametrized tests
- **day-034** - Fixtures and testing classes (setup/teardown with `yield`)
- **day-035** - Integrated: a typed FastAPI app tested with pytest and `TestClient`

### Databases (SQLAlchemy)

- **day-041** - First steps with the SQLAlchemy ORM (models, engine, insert and query)
- **day-042** - Full CRUD (create, read, update, delete) with separate functions
- **day-043** - Relationships (one-to-many with `ForeignKey` and `relationship`, cascade delete)

### FastAPI

- **day-005** - First routes with GET and JSON responses
- **day-012** - Path parameters and automatic type validation
- **day-024** - POST requests and data validation with Pydantic (`BaseModel`)
- **day-044** - FastAPI with SQLAlchemy: database-backed CRUD, `Depends` and dependency injection
- **day-046** - Integrated review: a blog API with related authors and posts (relationships, cascade)

### Authentication & Security

- **day-047** - Password hashing with bcrypt (salting, never storing plain text)
- **day-048** - JSON Web Tokens with PyJWT (`encode` / `decode`, `sub` / `exp`, HS256)
- **day-049** - Full auth API: register, login with OAuth2, protected routes with `Depends`
- **day-050** - Authentication + authorization: a notes API where each user only reaches their own data (ownership checks, 403)

### Async / Concurrency

- **day-051** - `async` / `await` fundamentals (`asyncio.gather`, sync vs async)
- **day-052** - Async FastAPI consuming external APIs with `httpx` (parallel requests with `gather`)
- **day-053** - Background tasks with Celery and Redis (`.delay()`, workers, retries)
- **day-054** - Celery integrated with FastAPI (dispatch a task, poll its result by id)
- **day-056** - WebSockets (real-time connection, `accept`, receive / send loop)
- **day-057** - WebSocket broadcast (a connection manager for multiple clients)

### Docker

- **day-006** - Dockerfile for a simple Python script
- **day-013** - Dockerizing a FastAPI application (Poetry, `EXPOSE`, Uvicorn)
- **day-025** - Docker Compose with two services (FastAPI + Redis)
- **day-039** - Redis as a cache (cache-aside pattern with TTL)
- **day-045** - Dockerized FastAPI + PostgreSQL with Compose (volumes, healthcheck, env vars)

### CI/CD

- **day-058** - Continuous integration with GitHub Actions (running pytest automatically on every push)

## Continuous integration

Every push runs the test suite automatically through GitHub Actions, across the pytest days (`day-032` to `day-034`). The badge at the top reflects the current status.

## How to run

Most days are plain Python and run directly:

    python day-001/main.py

Test days run with pytest from inside the day's folder:

    pytest -v

FastAPI days run with the development server from inside the day's folder:

    fastapi dev main.py

Docker days build and run a container:

    docker build -t day006 .
    docker run day006

Docker Compose days start every service together:

    docker compose up --build

## About

I'm a Python full-stack developer with a back-end focus, using this repository to build consistency and document my progress one day at a time.
