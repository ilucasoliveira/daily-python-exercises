# Daily Python Exercises

Daily hands-on exercises to sharpen my Python fundamentals and back-end skills. The goal is one exercise per day, each small enough to finish in 20 to 40 minutes, with at least one commit to keep a steady learning habit.

## How it works

Each day lives in its own folder (`day-001`, `day-002`, and so on). A day is self-contained: enter the folder and run its main file. Review days revisit earlier topics and combine them into a single, larger exercise.

The weekly rhythm mixes Python fundamentals with practical back-end tools: several days of core Python, then FastAPI, Docker, and a review day that ties the week together.

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

### FastAPI

- **day-005** - First routes with GET and JSON responses
- **day-012** - Path parameters and automatic type validation

### Docker

- **day-006** - Dockerfile for a simple Python script
- **day-013** - Dockerizing a FastAPI application (Poetry, `EXPOSE`, Uvicorn)

## How to run

Most days are plain Python and run directly:

    python day-001/main.py

FastAPI days run with the development server from inside the day's folder:

    fastapi dev main.py

Docker days build and run a container:

    docker build -t day006 .
    docker run day006

## About

I'm a Python full-stack developer with a back-end focus, using this repository to build consistency and document my progress one day at a time.
