from datetime import datetime
from sqlalchemy.orm import mapped_column, Mapped

from .base import Base


class Message(Base):
    """List of messages"""

    __tablename__ = 'messages'

    id: Mapped[int] = mapped_column(primary_key=True)
    sender: Mapped[str] = mapped_column(default=None, nullable=True)
    receiver: Mapped[str] = mapped_column(default=None, nullable=True)
    type: Mapped[str] = mapped_column(default=None, nullable=True)
    request: Mapped[str] = mapped_column(default=None, nullable=True)
    response: Mapped[str] = mapped_column(default=None, nullable=True)
    time: Mapped[datetime]


    def __init__(
        self, 
        sender: str | None = None,
        receiver: str | None = None,
        type: str | None = None,
        request: str | None = None,
        response: str | None = None,
        ):

        self.sender = sender
        self.receiver = receiver
        self.type = type
        self.request = request
        self.response = response
        self.time = datetime.utcnow()

