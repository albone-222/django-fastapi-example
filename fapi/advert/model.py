from datetime import datetime
from typing import Annotated
import uuid

from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column
from .schemas import Advert
from fapi.database import Base

uuidpk = Annotated[uuid.UUID, mapped_column(primary_key=True, default=uuid.uuid4())]
created_at = Annotated[datetime, mapped_column(server_default=text('TIMEZONE("utc", now())'))]
updated_at = Annotated[datetime, mapped_column(server_default=text('TIMEZONE("utc", now())'), server_onupdate=text('TIMEZONE("utc", now())'))]

class Adverts(Base):
    __tablename__ = 'adverts'
    id: Mapped[uuidpk] = mapped_column(primary_key=True, default=uuid.uuid4())
    owner: Mapped[uuid.UUID] = mapped_column(ForeignKey('users.uuid'), ondelete='CASCADE')
    name: Mapped[str]
    price: Mapped[int]
    contact: Mapped[str]
    description: Mapped[str]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    def __init__(self, advert: Advert, user):
        for attr in [a for a in dir(advert) if not a.startswith('__')]:
            setattr(self, attr, advert[attr])