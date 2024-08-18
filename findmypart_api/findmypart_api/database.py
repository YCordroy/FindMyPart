import os

import asyncpg
from dotenv import load_dotenv
from fastapi import FastAPI

app = FastAPI()
load_dotenv()

user = os.getenv('NAME_USER')
database = os.getenv('DB')
password = os.getenv('PASS_WEB')


@app.on_event("startup")
async def startup():
    app.state.pool = await asyncpg.create_pool(
        user=user, password=password, database=database, host='db'
    )


@app.on_event("shutdown")
async def shutdown():
    await app.state.pool.close()


async def db():
    async with app.state.pool.acquire() as conn:
        yield conn
