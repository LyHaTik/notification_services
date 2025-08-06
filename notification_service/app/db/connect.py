import os
import asyncpg
from contextlib import asynccontextmanager
from dotenv import load_dotenv


load_dotenv()

@asynccontextmanager
async def get_conn():
    conn = await asyncpg.connect(
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        database=os.getenv("POSTGRES_DB"),
        host=os.getenv("POSTGRES_HOST"),
        port=os.getenv("POSTGRES_PORT"),
    )
    try:
        yield conn
    finally:
        await conn.close()