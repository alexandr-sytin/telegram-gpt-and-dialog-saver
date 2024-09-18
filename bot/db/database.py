from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, close_all_sessions
from dotenv import load_dotenv
import os

from .models import Base
from .manager import DbManager

load_dotenv('.env')

class Database:
    def __init__(self, url: str = os.environ.get('DATABASE_URL')):
        self._engine: AsyncEngine = create_async_engine(url)
        self.manager: DbManager = DbManager(self._engine)

    async def _init(self):
        print('ASDFSADSADSADSADSA')
        await self.create_tables()

    async def create_tables(self):
        async with self._engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    async def shutdown(self):
        await close_all_sessions()
        await self._engine.dispose()


db = Database()
