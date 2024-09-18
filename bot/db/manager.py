from sqlalchemy.sql.expression import select, desc, update
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, AsyncEngine
from sqlalchemy import and_, func, or_
from contextlib import asynccontextmanager
from typing import Iterable, Sequence
from datetime import datetime, timedelta
import asyncio

from .models import Message


class DbManager:
    def __init__(self, engine: AsyncEngine):
        self._engine: AsyncEngine = engine
        self._Session = async_sessionmaker(bind=self._engine, class_=AsyncSession, expire_on_commit=True)
        self.lock = asyncio.Lock()
        
    @asynccontextmanager
    async def get_session(self):
        session = self._Session()
        try:
            yield session
        except:
            await session.rollback()
            raise
        finally:
            await session.close()

    async def add_message(self, message: Message) -> int:
        async with self.get_session() as session:
            session.add(message)
            await session.commit()
            await session.refresh(message)
        return message.id

    async def update_message(self, id: int, response: str) -> None:
        print('updating')
        print(id, response)
        async with self.get_session() as session:
            statement = update(Message).where(Message.id == id).values(response=response)
            await session.execute(statement=statement)
            await session.commit()
