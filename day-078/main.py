import os
import psycopg

from dotenv import load_dotenv

load_dotenv()

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")

conninfo = f"host=localhost port=5433 dbname={POSTGRES_DB} user={POSTGRES_USER} password={POSTGRES_PASSWORD}"
with psycopg.connect(conninfo) as conn:
    cur = conn.execute("""CREATE TABLE IF NOT EXISTS register_orders (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            price NUMERIC(10, 2) NOT NULL CHECK (price > 0),
            quantity INTEGER NOT NULL CHECK (quantity >= 1)
            )""")

    sql = "INSERT INTO register_orders (name, price, quantity) VALUES (%s, %s, %s) ON CONFLICT DO NOTHING"
    orders = [
        ("BrushTeeth", 3.14, 10),
        ("Soap", 2.15, 3),
        ("Sweep", 10.99, 1),
        ("Kit Spoons", 23.99, 2),
        ("Apple", 3.99, 13),
    ]
    cur = conn.cursor()
    cur.executemany(sql, orders)

    sql = "SELECT * FROM register_orders WHERE (price > %s) ORDER BY price DESC"
    cur = conn.execute(sql, (3,))
    lines = cur.fetchall()
    for row in lines:
        print(row)
