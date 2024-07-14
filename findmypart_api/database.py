from psycopg2 import connect
from psycopg2.extras import RealDictCursor


def get_db():
    conn = connect(
        database="app",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432",
        cursor_factory=RealDictCursor)
    try:
        yield conn
    finally:
        conn.close()
