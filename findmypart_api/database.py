import os

from dotenv import load_dotenv
from psycopg2 import connect
from psycopg2.extras import RealDictCursor

load_dotenv()


def get_db():
    conn = connect(
        database=os.getenv('DB'),
        user=os.getenv('NAME_USER'),
        password=os.getenv('PASS_WEB'),
        host="db",
        port="5432",
        cursor_factory=RealDictCursor)
    try:
        yield conn
    finally:
        conn.close()
