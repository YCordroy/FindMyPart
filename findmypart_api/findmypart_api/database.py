import os

import asyncpg
from dotenv import load_dotenv

load_dotenv()

user = os.getenv('NAME_USER')
database = os.getenv('DB')
password = os.getenv('PASS_WEB')


async def db():
    conn = await asyncpg.connect(user=user, password=password,
                                 database=database, host='127.0.0.1')
    try:
        yield conn
    finally:
        await conn.close()
