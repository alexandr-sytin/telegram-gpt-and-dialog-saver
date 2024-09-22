from datetime import datetime
from sqlalchemy.orm import mapped_column, Mapped

from .base import Base


class Message(Base):
    """List of messages"""

    __tablename__ = 'messages'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(default=None, nullable=True)
    username: Mapped[str] = mapped_column(default=None, nullable=True)
    request: Mapped[str] = mapped_column(default=None, nullable=True)
    request_type: Mapped[str] = mapped_column(default=None, nullable=True)
    response: Mapped[str] = mapped_column(default=None, nullable=True)
    response_type: Mapped[str] = mapped_column(default=None, nullable=True)
    time: Mapped[datetime]


    def __init__(
        self, 
        user_id: int | None = None,
        username: str | None = None,
        request: str | None = None,
        request_type: str | None = None,
        response: str | None = None,
        response_type: str | None = None,
        ):

        self.user_id = user_id
        self.username = username
        self.request = request
        self.request_type = request_type
        self.response = response
        self.response_type = response_type
        self.time = datetime.utcnow()

